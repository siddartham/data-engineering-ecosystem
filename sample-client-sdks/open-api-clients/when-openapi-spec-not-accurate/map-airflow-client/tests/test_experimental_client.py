"""
This module tests methods of
`map_airflow_client.experimental.client.Client`, and validates the data
returned
"""
import functools
import pickle
from typing import Any, Callable
from urllib.error import HTTPError

import pytest
import sob

from map_airflow_client.experimental import model
from map_airflow_client.experimental.client import Client

lru_cache: Callable[
    [], Callable[..., Callable[..., Any]]
] = functools.lru_cache  # type: ignore


@lru_cache()
def get_latest_runs_response(
    experimental_client: Client,
) -> model.LatestRunsResponse:
    return experimental_client.get_latest_runs()


def test_pickle(experimental_client: Client) -> None:
    """
    Verify that the client is pickle-able
    """
    get_latest_runs_response(experimental_client)  # type: ignore
    pickle.loads(pickle.dumps(experimental_client))


def test_get_latest_runs(experimental_client: Client) -> None:
    response: model.LatestRunsResponse = get_latest_runs_response(
        experimental_client
    )
    assert isinstance(response, model.LatestRunsResponse)
    sob.model.validate(response)


def test_get_dag_runs(experimental_client: Client) -> None:
    latest_run: model.LatestRun
    for latest_run in get_latest_runs_response(experimental_client).items:
        assert latest_run.dag_id
        try:
            dag_runs: model.DagRuns = experimental_client.get_dag_runs(
                latest_run.dag_id
            )
        except HTTPError as error:
            if (
                error.code == 400
                and "not found" in sob.errors.get_exception_text()
            ):
                # This DAG has been deleted
                continue
            raise
        assert isinstance(dag_runs, model.DagRuns)
        sob.model.validate(dag_runs)
        sob.test.json(dag_runs)
        dag_run: model.DagRun
        for dag_run in dag_runs:
            assert dag_run.dag_id
            assert dag_run.execution_date
            dag_run = experimental_client.get_dag_run(
                dag_run.dag_id, dag_run.execution_date
            )
            assert isinstance(dag_run, model.DagRun)
            sob.model.validate(dag_run)
            sob.test.json(dag_run)


def _test_post_dag_run(experimental_client: Client) -> None:
    latest_run: model.LatestRun = next(
        iter(get_latest_runs_response(experimental_client).items)
    )
    assert latest_run.dag_id
    response: model.PostDagRunResponse = experimental_client.post_dag_run(
        latest_run.dag_id
    )
    assert isinstance(response, model.PostDagRunResponse)
    sob.model.validate(response)
    sob.test.json(response)


if __name__ == "__main__":
    pytest.main()
