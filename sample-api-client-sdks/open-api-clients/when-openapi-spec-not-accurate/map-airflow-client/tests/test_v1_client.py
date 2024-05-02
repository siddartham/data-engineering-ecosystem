"""
This module tests methods of `map_airflow_client.v1.client.Client`, and
validates the data returned
"""
import pickle
from time import sleep

import pytest
import sob

from map_airflow_client.v1 import model
from map_airflow_client.v1.client import Client


def test_refresh_token(v1_client: Client) -> None:
    """
    Verify that we can retrieve a new token successfully
    """
    authorization: str = (
        v1_client._get_oauth2_client_credentials_authorization()
    )
    v1_client._oauth2_authorization_expires = 0
    assert (
        v1_client._get_oauth2_client_credentials_authorization()
        != authorization
    )


def test_get_version(v1_client: Client) -> None:
    sob.model.validate(v1_client.get_version())


def test_pickle(v1_client: Client) -> None:
    v1_client.get_connections()
    pickle.loads(pickle.dumps(v1_client))


def test_connections(v1_client: Client) -> None:
    connection_collection: model.ConnectionCollection = (
        v1_client.get_connections()
    )
    sob.model.validate(connection_collection)
    if connection_collection.connections:
        connection: model.Connection
        for connection in tuple(connection_collection.connections)[:3]:
            assert connection.connection_id
            connection = v1_client.get_connections_connection_id(
                connection.connection_id
            )
            sob.model.validate(connection)
            # Connection validation not currently usable
            # sob.model.validate(
            #     v1_client.post_connections_test(connection)
            # )
            assert connection.connection_id
            connection.connection_id += "_"
            try:
                v1_client.delete_connections_connection_id(
                    connection.connection_id
                )
            except Exception:
                pass
            sob.model.validate(v1_client.post_connections(connection))
            sob.model.validate(
                v1_client.patch_connections_connection_id(
                    connection=model.Connection(extra="Lorem Ipsum"),
                    connection_id=connection.connection_id,
                )
            )
            v1_client.delete_connections_connection_id(
                connection.connection_id
            )


def test_event_logs(v1_client: Client) -> None:
    event_log_collection: model.EventLogCollection = v1_client.get_event_logs(
        limit=5
    )
    sob.model.validate(event_log_collection)
    event_log: model.EventLog
    for event_log in event_log_collection.event_logs or ():
        assert event_log.event_log_id
        # Get the individual event log
        event_log = v1_client.get_event_logs_event_log_id(
            event_log_id=event_log.event_log_id
        )
        sob.model.validate(event_log)
        assert event_log.event_log_id


def test_dags(v1_client: Client) -> None:
    """
    TODO: patch_dags
    TODO: patch_dags_dag_id
    TODO: post_dags_dag_id_clear_task_instances
    TODO: post_dags_dag_id_clear_task_instances
    *TODO: get_dags_dag_id_dag_runs
    TODO: post_dags_dag_id_dag_runs
    TODO: get_dags_dag_id_dag_runs_dag_run_id
    TODO: delete_dags_dag_id_dag_runs_dag_run_id
    TODO: patch_dags_dag_id_dag_runs_dag_run_id
    TODO: get_dags_dag_id_dag_runs_dag_run_id_task_instances
    TODO: get_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id
    TODO: get_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_links
    TODO: get_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_list_mapped  # noqa
    TODO: get_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_logs_task_try_number  # noqa
    TODO: get_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_xcom_entries  # noqa
    TODO: get_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_xcom_entries_xcom_key  # noqa
    TODO: get_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_map_index  # noqa
    TODO: get_dags_dag_id_details
    TODO: get_dags_dag_id_tasks
    TODO: get_dags_dag_id_tasks_task_id
    TODO: post_dags_dag_id_update_task_instances_state
    TODO: post_dags_dag_runs_list
    TODO: post_dags_dag_runs_task_instances_list
    """
    dag_collection: model.DAGCollection = v1_client.get_dags()
    sob.model.validate(dag_collection)
    assert dag_collection.total_entries or 0 >= 3
    dag: model.DAG
    for dag in dag_collection.dags or ():
        assert dag.dag_id
        dag = v1_client.get_dags_dag_id(dag.dag_id)
        sob.model.validate(dag)
        # Un-pause the DAG
        assert dag.dag_id
        v1_client.patch_dags_dag_id(
            dag=model.DAG(is_paused=False), dag_id=dag.dag_id
        )
        # Trigger a DAG run
        dag_run: model.DAGRun = v1_client.post_dags_dag_id_dag_runs(
            dag_run=model.DAGRun(), dag_id=dag.dag_id
        )
        sob.model.validate(dag_run)
        assert dag_run.dag_id
        assert isinstance(dag_run.dag_run_id, str)
        # Get the DAG run state
        dag_run = v1_client.get_dags_dag_id_dag_runs_dag_run_id(
            dag_id=dag_run.dag_id,
            dag_run_id=dag_run.dag_run_id,
        )
        sob.model.validate(dag_run)
        assert dag_run.dag_id
        assert isinstance(dag_run.dag_run_id, str)
        # Wait for the DAG run to finish
        while dag_run.state in (
            "running",
            "queued",
            "scheduled",
            "none",
        ):
            sleep(10)
            dag_run = v1_client.get_dags_dag_id_dag_runs_dag_run_id(
                dag_id=dag_run.dag_id,
                dag_run_id=dag_run.dag_run_id,
            )
        assert dag_run.state == "success", dag_run.state


if __name__ == "__main__":
    pytest.main()
