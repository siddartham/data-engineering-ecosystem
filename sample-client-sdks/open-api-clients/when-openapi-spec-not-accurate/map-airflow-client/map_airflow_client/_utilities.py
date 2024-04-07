import os
from time import sleep
from typing import Any, Dict, Iterable, Optional, Tuple, Union
from urllib.error import HTTPError

from . import experimental, v1
from .errors import DAGRunError

TOKEN_URL: str = "https://api.aegis.mycloud.com/v1/prod/token"
STATUS_CHECK_INTERVAL: int = 10


def _get_client(
    cluster_name: str,
    region: str,
    api_version: str,
    client_id: str,
    client_secret: str = "",
    client_secret_cerberus_path: str = "",
    echo: bool = False,
) -> Union[v1.client.Client, experimental.client.Client]:
    assert api_version in ("v1", "experimental")
    assert client_secret or client_secret_cerberus_path
    kwargs: Dict[str, Any] = dict(
        oauth2_client_id=client_id,
        oauth2_token_url=TOKEN_URL,
        echo=echo,
    )
    if client_secret_cerberus_path:
        kwargs.update(
            oauth2_client_secret_cerberus_path=(client_secret_cerberus_path)
        )
    if client_secret:
        kwargs.update(oauth2_client_secret=client_secret)
    return (
        v1.client.Client  # type: ignore
        if api_version == "v1"
        else experimental.client.Client
    )(
        (
            f"https://proxy.{region}.map.my.com/{cluster_name}/"
            f"api/{api_version}"
        ),
        **kwargs,
    )


def get_client(
    cluster_name: str,
    region: str,
    client_id: str,
    client_secret: str = "",
    client_secret_cerberus_path: str = "",
    echo: bool = False,
    api_version: str = "",
) -> Union[v1.client.Client, experimental.client.Client]:
    """
    Parameters:

    - cluster_name (str)
    - region (str): The AWS region. For example: "us-west-2" or "us-east-1".
    - client_id (str): Your OAuth client ID.
    - client_secret (str): Your OAuth client secret.
    - client_secret_cerberus_path (str): A cerberus secure data path where
      your OAuth2 client secret is stored.
    - echo (bool) = False: If `True`, requests/responses will be printed to
      `sys.stdout`.
    - api_version (str) = "": Either "v1" or "experimental". If neither is
      provided, the API version will be automatically inferred.
    """
    client: Union[v1.client.Client, experimental.client.Client]
    error: Optional[HTTPError] = None
    api_versions: Tuple[str, ...] = (
        (api_version,) if api_version else ("v1", "experimental")
    )
    for api_version in api_versions:
        try:
            client = _get_client(
                cluster_name=cluster_name,
                region=region,
                api_version=api_version,
                client_id=client_id,
                client_secret=client_secret,
                client_secret_cerberus_path=client_secret_cerberus_path,
                echo=echo,
            )
            # Make a dummy API call to test for connectivity
            if isinstance(client, v1.client.Client):
                client.get_version()
            else:
                client.get_latest_runs()
            return client
        except HTTPError as error_:
            if error is None:
                error = error_
    assert error
    raise error


def iter_client_file_dag_ids(
    client: Union[v1.client.Client, experimental.client.Client],
    file_names: Iterable[str],
) -> Iterable[str]:
    """
    Yield the DAG IDs for all dags in the specified files.

    Parameters:

    - client (
        map_airflow_client.v1.client.Client|
        map_airflow_client.experimental.client.Client
      )
    - file_names ([str])
    """
    if isinstance(file_names, str):
        file_names = (file_names,)
    if isinstance(client, v1.client.Client):
        dag: v1.model.DAG
        for dag in client.get_dags().dags or ():
            if (
                dag.dag_id
                and dag.fileloc
                and (os.path.basename(dag.fileloc) in file_names)
            ):
                yield dag.dag_id
    else:
        raise ValueError(
            "DAGs cannot be reference by file name for MAP clusters "
            'using the "experimental" API (the only API for Airflow 1x). '
            "Please provide DAG IDs instead, using the `--dag-id` parameter."
        )


def run_experimental_client_dag(
    client: experimental.client.Client, dag_id: str, detach: bool = False
) -> None:
    is_paused: bool = client.get_dag_paused(dag_id).is_paused or False
    # Un-pause the DAG
    client.get_dag_paused(dag_id, False)
    post_response: experimental.model.PostDagRunResponse = client.post_dag_run(
        dag_id
    )
    assert post_response.execution_date is not None
    try:
        if not detach:
            dag_run: experimental.model.DagRun = experimental.model.DagRun(
                dag_id=dag_id,
                state="queued",
                execution_date=post_response.execution_date,
            )
            while dag_run.state in (
                "running",
                "queued",
                "scheduled",
                "none",
            ):
                sleep(STATUS_CHECK_INTERVAL)
                dag_run = client.get_dag_run(
                    dag_id, post_response.execution_date
                )
            if dag_run.state != "success":
                raise DAGRunError(dag_run)
    finally:
        if is_paused:
            # Restore the original paused-state of the DAG
            client.get_dag_paused(dag_id, True)


def run_v1_client_dag(
    client: v1.client.Client, dag_id: str, detach: bool = False
) -> None:
    dag = client.get_dags_dag_id(dag_id)
    is_paused: bool = (
        dag.is_paused if isinstance(dag.is_paused, bool) else False
    )
    # Un-pause the DAG
    client.patch_dags_dag_id(dag=v1.model.DAG(is_paused=False), dag_id=dag_id)
    try:
        # Trigger a DAG run
        dag_run: v1.model.DAGRun = client.post_dags_dag_id_dag_runs(
            dag_run=v1.model.DAGRun(),
            dag_id=dag_id,
        )
        if not detach:
            assert isinstance(dag_run.dag_run_id, str)
            # Wait for the DAG run to finish
            while dag_run.state in (
                "running",
                "queued",
                "scheduled",
                "none",
            ):
                sleep(STATUS_CHECK_INTERVAL)
                dag_run = client.get_dags_dag_id_dag_runs_dag_run_id(
                    dag_id=dag_id,
                    dag_run_id=dag_run.dag_run_id,
                )
            if dag_run.state != "success":
                raise DAGRunError(dag_run)
    finally:
        if is_paused:
            client.patch_dags_dag_id(
                dag=v1.model.DAG(is_paused=True), dag_id=dag_id
            )


def pause_v1_client_dag(client: v1.client.Client, dag_id: str) -> None:
    client.patch_dags_dag_id(dag=v1.model.DAG(is_paused=True), dag_id=dag_id)


def pause_experimental_client_dag(
    client: experimental.client.Client, dag_id: str
) -> None:
    client.get_dag_paused(dag_id, True)


def unpause_v1_client_dag(client: v1.client.Client, dag_id: str) -> None:
    client.patch_dags_dag_id(dag=v1.model.DAG(is_paused=False), dag_id=dag_id)


def unpause_experimental_client_dag(
    client: experimental.client.Client, dag_id: str
) -> None:
    client.get_dag_paused(dag_id, False)
