import argparse
import json
import os
import re
from multiprocessing.pool import Pool
from typing import Dict, Iterable, Optional, Sequence, Tuple
from urllib.parse import quote

from daves_dev_tools.utilities.cerberus import get_cerberus_secrets
from company.map_airflow_client.experimental.client import Client

from company.,myteam_dev_tools.airflow.utilities import get_client
from company.,myteam_dev_tools.config import CERBERUS_URL
from .config import DEFAULT_DAG_DIRECTORY
from .inspect import iter_dag_ids
from ..utilities import (
    base64_encode,
    epctl_login,
    get_package_version,
    run,
    multiprocessing_set_start_method,
)

multiprocessing_set_start_method()


def set_dag_constant(source: str, name: str, value: str) -> str:
    if name in source:
        source = re.sub(
            (
                r"((?:^|\n)\s*"
                f"{name}"
                r"(?:\s*:\s*[A-Za-z0-9_]+)\s*=\s*)"
                r'("[^"]+")'
            ),
            f'\\1"{format(value)}"',
            source,
        )
    return source


def iter_dags(
    directory: str = DEFAULT_DAG_DIRECTORY,
    setup_path: Optional[str] = None,
) -> Iterable[Tuple[str, str, Tuple[str, ...]]]:
    """
    Iterate over all DAG files, yielding a tuple consisting of 3 items:

    - The file name (`str`)
    - The DAG file's source code (`str`)
    - A `tuple` of all DAG IDs defined in the file
    """
    version: str = get_package_version(setup_path)
    file_name: str
    for file_name in os.listdir(directory):
        if file_name.endswith(".py"):
            path: str = os.path.join(directory, file_name)
            source: str = set_dag_constant(
                open(path).read(), "VERSION", version
            )
            yield (
                file_name,
                base64_encode(source),
                tuple(iter_dag_ids(source)),
            )


def _sync_environment_region_dags(
    environment: str,
    region: str,
    dag_directory: str,
    setup_path: Optional[str],
) -> None:
    airflow_client: Client = get_client(environment, region=region)
    for file_name, base64_dag, dag_ids in iter_dags(
        setup_path=setup_path, directory=dag_directory
    ):
        run(
            "epctl map upload-dag "
            "--production "
            f"--region {region} "
            f"--file-name {file_name} "
            f"--encoded-contents {base64_dag} "
            f"--cluster-name ,myteam-{environment}"
        )
        # Un-pause the DAGs we've just uploaded
        dag_id: str
        for dag_id in dag_ids:
            airflow_client.get_dag_paused(dag_id, False)


def sync_dags(
    environments: Iterable[str],
    regions: Iterable[str] = ("us-west-2",),
    dag_directory: str = DEFAULT_DAG_DIRECTORY,
    setup_path: Optional[str] = None,
) -> None:
    """
    This function uploads any DAGs in `../airflow/dags/` to the MAP (Managed
    Airflow Platform) cluster corresponding to each environment. This function
    does *not* delete other DAGs, as this repo is not the sole source of DAGs
    for ,myteam's MAP clusters.
    """
    region: str
    environment: str
    epctl_login()

    def iter_arguments() -> Iterable[Tuple[str, str, str, Optional[str]]]:
        region: str
        for region in regions:
            environment: str
            for environment in environments:
                yield environment, region, dag_directory, setup_path

    pool: Pool
    with Pool() as pool:
        list(pool.starmap(_sync_environment_region_dags, iter_arguments()))


def _get_environment_ngap_gid(environment: str) -> str:
    assert environment in ("dev", "qa", "prod")
    return f"a.NGAP.SE{'' if environment == 'prod' else '.NP'}"


def _add_environment_region_ngap_emr_api_connection(
    environment: str, region: str, secrets: Dict[str, Dict[str, str]]
) -> None:
    """
    This function adds all required Airflow connections
    """
    login: str = _get_environment_ngap_gid(environment)
    password: str = secrets["ngap"][login]
    endpoint: str = secrets["ngap-emr-api"][f"{region}-endpoint"]
    conn_extra: str = json.dumps(
        dict(
            pub_key_endpoint=secrets["ngap-emr-api"]["public-key-endpoint"],
            token_endpoint=secrets["ngap-emr-api"]["token-endpoint"],
            managed_spark_endpoint=secrets["ngap-emr-api"][
                "managed-spark-endpoint"
            ],
        )
    ).replace("'", r"\'")
    # First, delete the connection if it exists
    try:
        run(
            "epctl map delete-connection "
            "--production "
            f"--region '{region}' "
            f"--cluster-name ',myteam-{environment}' "
            f"--conn-id ae_token_creds"
        )
    except OSError:
        pass
    run(
        "epctl map add-connection "
        "--production "
        f"--region '{region}' "
        f"--cluster-name ',myteam-{environment}' "
        f"--conn-id ae_token_creds "
        f"--conn-uri 'http://{quote(login)}:{quote(password)}@"
        f"{quote(endpoint, safe='')}' "
        f"--conn-extra '{conn_extra}'"
    )


def add_connections(
    environments: Iterable[str] = ("dev",),
    regions: Iterable[str] = ("us-west-2",),
) -> None:
    if isinstance(environments, str):
        environments = (environments,)
    region: str
    environment: str
    epctl_login()
    secrets: Dict[str, Dict[str, str]] = {
        "ngap": get_cerberus_secrets(CERBERUS_URL, "app/,myteam/ngap"),
        "ngap-emr-api": get_cerberus_secrets(
            CERBERUS_URL, "app/,myteam/ngap-emr-api"
        ),
    }

    def iter_arguments() -> Iterable[
        Tuple[str, str, Dict[str, Dict[str, str]]]
    ]:
        region: str
        for region in regions:
            environment: str
            for environment in environments:
                yield environment, region, secrets

    pool: Pool
    with Pool() as pool:
        list(
            pool.starmap(
                _add_environment_region_ngap_emr_api_connection,
                iter_arguments(),
            )
        )


def main() -> None:
    """
    This function is the entry point for using this script as a CLI.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument(
        "--directory",
        "-d",
        type=str,
        default=DEFAULT_DAG_DIRECTORY,
        help="The path to a directory where the DAGs are stored",
    )
    parser.add_argument(
        "--region",
        "-r",
        type=str,
        action="append",
        default=[],
        help='"us-west-2" or "us-east-1"',
    )
    parser.add_argument(
        "environments",
        nargs="*",
        help='Which environments ("dev", "qa", and/or "prod")?',
    )
    arguments: argparse.Namespace = parser.parse_args()
    environments: Sequence[str] = arguments.environments or ("dev",)
    regions: Sequence[str] = arguments.region or ("us-west-2",)
    add_connections(environments=environments, regions=regions)
    sync_dags(
        environments=environments,
        regions=regions,
        dag_directory=arguments.directory,
    )
