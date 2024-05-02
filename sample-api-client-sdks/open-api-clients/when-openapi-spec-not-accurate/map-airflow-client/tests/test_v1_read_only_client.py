"""
This module tests methods of `map_airflow_client.v1.client.Client`, and
validates the data returned
"""
import pytest
import sob

from map_airflow_client.v1 import model
from map_airflow_client.v1.client import Client


def test_refresh_token(v1_read_only_client: Client) -> None:
    """
    Verify that we can retrieve a new token successfully
    """
    authorization: str = (
        v1_read_only_client._get_oauth2_client_credentials_authorization()
    )
    v1_read_only_client._oauth2_authorization_expires = 0
    assert (
        v1_read_only_client._get_oauth2_client_credentials_authorization()
        != authorization
    )


def test_get_version(v1_read_only_client: Client) -> None:
    sob.model.validate(v1_read_only_client.get_version())


def test_event_logs(v1_read_only_client: Client) -> None:
    event_log_collection: model.EventLogCollection = (
        v1_read_only_client.get_event_logs(limit=5)
    )
    sob.model.validate(event_log_collection)
    event_log: model.EventLog
    for event_log in event_log_collection.event_logs or ():
        assert event_log.event_log_id
        # Get the individual event log
        event_log = v1_read_only_client.get_event_logs_event_log_id(
            event_log_id=event_log.event_log_id
        )
        sob.model.validate(event_log)
        assert event_log.event_log_id


def test_dags(v1_read_only_client: Client) -> None:
    dag_collection: model.DAGCollection = v1_read_only_client.get_dags()
    sob.model.validate(dag_collection)
    assert dag_collection.total_entries or 0 >= 3
    dag: model.DAG
    for dag in dag_collection.dags or ():
        assert dag.dag_id
        dag = v1_read_only_client.get_dags_dag_id(dag.dag_id)
        sob.model.validate(dag)


if __name__ == "__main__":
    pytest.main()
