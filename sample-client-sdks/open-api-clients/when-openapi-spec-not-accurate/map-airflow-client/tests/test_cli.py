import os
import sys
from typing import List, Sequence, Set, Tuple

import pytest
from daves_dev_tools.utilities import run as _run

from map_airflow_client import experimental, v1
from map_airflow_client._utilities import iter_client_file_dag_ids


def test_get_client(
    v1_client: v1.client.Client,
    experimental_client: experimental.client.Client,
) -> None:
    assert isinstance(v1_client, v1.client.Client)
    assert isinstance(experimental_client, experimental.client.Client)


def test_iter_client_file_dag_ids(
    v1_client: v1.client.Client, dags: Sequence[Tuple[str, str]]
) -> None:
    item: Tuple[str, str]  # noqa
    dag_file_names: Tuple[str, ...] = tuple(
        map(lambda item: os.path.basename(item[1]), dags)
    )
    dag_ids: Set[str] = set(map(lambda item: item[0], dags))
    assert (
        set(iter_client_file_dag_ids(v1_client, file_names=dag_file_names))
        == dag_ids
    )


def test_pause(dags: Sequence[Tuple[str, str]]) -> None:
    command: List[str] = [
        sys.executable,
        "-m",
        "map_airflow_client",
        "pause",
        "-cn",
        "airflow-client-test",
        "-r",
        "us-west-2",
        "-cid",
        "sustainability.etl",
        "-cscp",
        "app/sustainability/etl/client-secret",
    ]
    dag_id: str
    dag_file_name: str
    for dag_id, dag_file_name in dags:
        command.extend(("-dfn", dag_file_name))
    _run(command)


def test_create_connection() -> None:
    # We run the command twice to make sure it
    # works when the connection already exists
    for index in range(2):
        _run(
            (
                sys.executable,
                "-m",
                "map_airflow_client",
                "create-connection",
                "--connection-id",
                "airflow-client-test-connection",
                "--connection-type",
                "HTTP",
                "--description",
                "Test connection.",
                "--host",
                "localhost",
                "--port",
                "8080",
                "--password",
                "123ABC",
                "--extra",
                "{}",
                "--cluster-name",
                "airflow-client-test",
                "-r",
                "us-west-2",
                "-cid",
                "sustainability.etl",
                "-cscp",
                "app/sustainability/etl/client-secret",
                "-e",
            )
        )
    _run(
        [
            sys.executable,
            "-m",
            "map_airflow_client",
            "delete-connection",
            "--connection-id",
            "airflow-client-test-connection",
            "--cluster-name",
            "airflow-client-test",
            "-r",
            "us-west-2",
            "-cid",
            "sustainability.etl",
            "-cscp",
            "app/sustainability/etl/client-secret",
            "-e",
        ]
    )


def test_unpause(dags: Sequence[Tuple[str, str]]) -> None:
    command: List[str] = [
        sys.executable,
        "-m",
        "map_airflow_client",
        "unpause",
        "-cn",
        "airflow-client-test",
        "-r",
        "us-west-2",
        "-cid",
        "sustainability.etl",
        "-cscp",
        "app/sustainability/etl/client-secret",
    ]
    dag_id: str
    dag_file_name: str
    for dag_id, dag_file_name in dags:
        command.extend(("-dfn", dag_file_name))
    _run(command)


def test_run(dags: Sequence[Tuple[str, str]]) -> None:
    command: List[str] = [
        sys.executable,
        "-m",
        "map_airflow_client",
        "run",
        "-cn",
        "airflow-client-test",
        "-r",
        "us-west-2",
        "-cid",
        "sustainability.etl",
        "-cscp",
        "app/sustainability/etl/client-secret",
    ]
    dag_id: str
    dag_file_name: str
    for dag_id, dag_file_name in dags:
        command.extend(("-dfn", dag_file_name))
    _run(command)


if __name__ == "__main__":
    pytest.main()
