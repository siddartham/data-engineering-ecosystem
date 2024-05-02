import functools
import os
import platform
import sys
from shutil import which
from subprocess import CalledProcessError, call, check_call
from tempfile import gettempdir
from time import sleep
from typing import Any, Callable, Iterable, Sequence, Tuple
from warnings import warn

import pytest
import sob
from daves_dev_tools.utilities import run as _run

from map_airflow_client import experimental, v1
from map_airflow_client._utilities import get_client

lru_cache: Callable[
    [], Callable[..., Callable[..., Any]]
] = functools.lru_cache  # type: ignore
v1_client_lru_cache: Callable[
    [], Callable[..., Callable[..., v1.client.Client]]
] = functools.lru_cache  # type: ignore
experimental_client_lru_cache: Callable[
    [], Callable[..., Callable[..., experimental.client.Client]]
] = functools.lru_cache  # type: ignore
TESTS_DIRECTORY: str = os.path.abspath(os.path.dirname(__file__))
BASE_DIRECTORY: str = os.path.dirname(TESTS_DIRECTORY)
DAGS_DIRECTORY: str = os.path.join(TESTS_DIRECTORY, "airflow", "dags")
DAGS: Sequence[Tuple[str, str]] = (
    ("test_dag_1", os.path.join(DAGS_DIRECTORY, "dag1.py")),
    ("test_dag_2", os.path.join(DAGS_DIRECTORY, "dag2.py")),
    ("test_dag_3", os.path.join(DAGS_DIRECTORY, "dag3.py")),
)
EPCTL: str = which("epctl") or os.path.join(gettempdir(), "epctl")


@pytest.fixture(name="epctl", autouse=True, scope="session")
def install_epctl() -> str:
    """
    If the `epctl` command is not available, we attempt to install it,
    and raise an error if that is not possible
    """
    try:
        check_call((EPCTL, "update"))
    except (CalledProcessError, FileNotFoundError, OSError):
        platform_name: str
        if sys.platform.startswith("darwin"):
            platform_name = "darwin"
        elif sys.platform.startswith("linux"):
            platform_name = "linux"
        elif os.name == "nt":
            platform_name = "windows"
        else:
            raise
        architecture: str = "amd64" if "64" in platform.machine() else "386"
        check_call(
            (
                "curl",
                "https://epctl.platforms.my.com/binaries/latest/"
                f"epctl_{platform_name}_{architecture}",
                "-o",
                EPCTL,
            )
        )
        if platform_name in ("linux", "darwin"):
            call(("chmod", "+rwx", EPCTL))
    return EPCTL


@pytest.fixture(name="v1_client", autouse=True, scope="session")
def get_v1_client() -> v1.client.Client:
    return get_client(  # type: ignore
        cluster_name="airflow-client-test",
        region="us-west-2",
        client_id="sustainability.etl",
        client_secret_cerberus_path="app/sustainability/etl/client-secret",
        api_version="v1",
        echo=True,
    )


@pytest.fixture(name="v1_read_only_client", autouse=True, scope="session")
def get_v1_read_only_client() -> v1.client.Client:
    return get_client(  # type: ignore
        cluster_name="tdp-sm-ga-prd-use1-2",
        region="us-east-1",
        client_id="sustainability.etl",
        client_secret_cerberus_path="app/sustainability/etl/client-secret",
        api_version="v1",
        echo=True,
    )


@pytest.fixture(name="experimental_client", autouse=True, scope="session")
def get_experimental_client() -> experimental.client.Client:
    return get_client(  # type: ignore
        cluster_name="airflow-client-test",
        region="us-west-2",
        client_id="sustainability.etl",
        client_secret_cerberus_path="app/sustainability/etl/client-secret",
        api_version="experimental",
        echo=True,
    )


def delete_dags(v1_client: v1.client.Client, epctl: str) -> None:
    _run(
        (
            epctl,
            "login",
            "--production",
            "--client-id",
            v1_client.oauth2_client_id,
            "--client-secret",
            v1_client.oauth2_client_secret,
        )
    )
    path: str
    dag_id: str
    for dag_id, path in DAGS:
        # Delete a dag in order to have something to work with
        file_name: str = os.path.basename(path)
        print(f"Deleting {file_name}")
        # Using the Airflow API to delete dags is not allowed,
        # (`self.client.delete_dags_dag_id(dag_id=dag_id)`), so we
        # must use epctl
        try:
            _run(
                (
                    epctl,
                    "map",
                    "delete-dag",
                    "--production",
                    "--region",
                    "us-west-2",
                    "--file-name",
                    file_name,
                    "--cluster-name",
                    "airflow-client-test",
                )
            )
        except (CalledProcessError, FileNotFoundError):
            warn(sob.errors.get_exception_text())


@pytest.fixture(autouse=True, name="dags", scope="session")
def upload_dags(
    v1_client: v1.client.Client,
    epctl: str,
) -> Iterable[Sequence[Tuple[str, str]]]:
    _run(
        (
            epctl,
            "login",
            "--production",
            "--client-id",
            v1_client.oauth2_client_id,
            "--client-secret",
            v1_client.oauth2_client_secret,
        )
    )
    path: str
    dag_id: str
    for dag_id, path in DAGS:
        print(f"Uploading {dag_id}")
        # Upload a dag in order to have something to work with
        _run(
            (
                epctl,
                "map",
                "upload-dag",
                "--production",
                "--region",
                "us-west-2",
                "--file-path",
                path,
                "--file-name",
                os.path.basename(path),
                "--cluster-name",
                "airflow-client-test",
            )
        )
    dag_collection: v1.model.DAGCollection = v1_client.get_dags()
    while not dag_collection.total_entries:
        sleep(10)
        dag_collection = v1_client.get_dags()
    yield DAGS
    # Teardown
    delete_dags(v1_client, epctl)
