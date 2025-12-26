import argparse
from multiprocessing.pool import Pool
from time import sleep
from typing import Iterable, Tuple

from company.map_airflow_client.experimental.client import Client
from company.map_airflow_client.experimental.model import (
    DagRun,
    PostDagRunResponse,
)

from .config import DEFAULT_DAG_DIRECTORY, STATUS_CHECK_INTERVAL
from .inspect import iter_dags_ids
from company.myteam_dev_tools.airflow.utilities import get_client
from ..utilities import multiprocessing_set_start_method

multiprocessing_set_start_method()


def _run_environment_region_dag(
    environment: str, region: str, dag_id: str
) -> None:
    airflow_client: Client = get_client(environment, region=region)
    post_response: PostDagRunResponse = airflow_client.post_dag_run(dag_id)
    airflow_client.get_dag_paused(dag_id, False)
    dag_run: DagRun = DagRun(state="running")
    while dag_run.state in (
        "running",
        "queued",
        "scheduled",
        "none",
    ):
        sleep(STATUS_CHECK_INTERVAL)
        assert post_response.execution_date is not None
        dag_run = airflow_client.get_dag_run(
            dag_id, post_response.execution_date
        )
    if dag_run.state != "success":
        raise RuntimeError(f"DAG run response: {str(dag_run)}")


def run_dags(
    environments: Iterable[str],
    regions: Iterable[str] = ("us-west-2",),
    directory: str = DEFAULT_DAG_DIRECTORY,
) -> None:
    """
    This function will run each DAG in this package, in each environment
    passed, until complete, and will raise an error if any fail.
    """
    environment: str
    dag_ids: Tuple[str, ...] = tuple(iter_dags_ids(directory=directory))

    def iter_arguments() -> Iterable[Tuple[str, str, str]]:
        region: str
        for region in regions:
            assert region in ("us-west-2", "us-east-1")
            environment: str
            for environment in environments:
                assert environment in ("dev", "qa", "prod")
                dag_id: str
                for dag_id in dag_ids:
                    yield environment, region, dag_id

    pool: Pool
    with Pool() as pool:
        list(pool.starmap(_run_environment_region_dag, iter_arguments()))


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
    run_dags(
        environments=arguments.environments or ["us-west-2"],
        regions=arguments.region or ["dev"],
        directory=DEFAULT_DAG_DIRECTORY,
    )
