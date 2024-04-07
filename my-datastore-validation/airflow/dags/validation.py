import functools
from datetime import datetime, timedelta
from typing import List, Optional

import pendulum  # type: ignore
from airflow.decorators import task  # type: ignore

from airflow import DAG  # type: ignore


@functools.lru_cache()
def get_start_date() -> datetime:
    return (
        pendulum.now(tz="America/Los_Angeles").replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        - timedelta(days=2)
    ).astimezone(pendulum.tz.UTC)


def get_schedule_interval() -> Optional[str]:
    from airflow.configuration import conf  # type: ignore

    interval: Optional[str] = None
    if conf.get("ae_compute", "env") == "prod":
        start_date: datetime = get_start_date()
        interval = "{} {} * * *".format(start_date.minute, start_date.hour)
    return interval


with DAG(
    dag_id="validation",
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
        open("/usr/local/airflow/code/validation_requirements.txt")
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

        from data_quality_framework.dialects.snowflake import (
            validate_environment,
        )

        environment = conf.get("compute", "env")
        validate_environment(environment, echo=False)

    main()
