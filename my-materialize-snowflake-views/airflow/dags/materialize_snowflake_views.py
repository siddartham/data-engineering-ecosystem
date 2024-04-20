import functools
from datetime import datetime, timedelta
from typing import List, Optional

import pendulum  # type: ignore
from airflow.configuration import conf  # type: ignore
from airflow.decorators import task  # type: ignore
from airflow.exceptions import AirflowConfigException  # type: ignore

from airflow import DAG  # type: ignore

ENVIRONMENT: str
try:
    ENVIRONMENT = conf.get("compute", "env") or ""
except AirflowConfigException:
    # This facilitates static analysis of the DAG
    ENVIRONMENT = "dev"


@functools.lru_cache()
def get_start_date() -> datetime:
    return (
        pendulum.now(tz="America/Los_Angeles").replace(
            hour=7, minute=0, second=0, microsecond=0
        )
        - timedelta(days=2)
    ).astimezone(pendulum.tz.UTC)


def get_schedule_interval() -> Optional[str]:
    interval: Optional[str] = None
    if ENVIRONMENT == "prod":
        start_date: datetime = get_start_date()
        interval = "{} {} * * *".format(start_date.minute, start_date.hour)
    return interval


with DAG(
    dag_id="materialize_snowflake_views",
    start_date=get_start_date(),
    default_args=dict(
        email=["reddy.siddartha53@gmail.com"],
        email_on_failure=True,
    ),
    schedule_interval=get_schedule_interval(),
    max_active_runs=1,
    dagrun_timeout=timedelta(days=1),
) as dag:
    requirements: List[str] = (
        open(
            "/usr/local/airflow/code/"
            "my_materialize_snowflake_views_requirements.txt"
        )
        .read()
        .strip()
        .split("\n")
    )

    @task.virtualenv(
        task_id="main",
        requirements=requirements[0].split(" ") + requirements[1:],
        system_site_packages=True,
    )
    def main() -> None:
        from airflow.configuration import conf  # type: ignore

        from my_materialize_snowflake_views.broker import (  # type: ignore  # noqa
            Broker,
        )

        environment = conf.get("compute", "env")
        Broker(environment=f"map-{environment}", echo=False).materialize(
            exclude=(
                "ONEBOX_SUSTAINABILITY_MV",
                "ONEBOX_BOOKINGS_SUSTAINABILITY_MV",
            )
        )

    main()
