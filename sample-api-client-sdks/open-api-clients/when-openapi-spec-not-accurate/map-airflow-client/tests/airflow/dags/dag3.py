from datetime import datetime, timedelta

import pendulum
from airflow.operators.dummy_operator import DummyOperator  # type: ignore

from airflow import DAG  # type: ignore


def get_start_date() -> datetime:
    return (
        pendulum.now(tz="America/Los_Angeles").replace(
            hour=12, minute=0, second=0, microsecond=0
        )
        - timedelta(days=2)
    ).astimezone(pendulum.tz.UTC)


with DAG(dag_id="test_dag_3", start_date=get_start_date()) as dag:
    (
        DummyOperator(task_id="task_1")
        >> DummyOperator(task_id="task_2")
        >> DummyOperator(task_id="task_3")
    )
