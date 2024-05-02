import functools
import pendulum  # type: ignore
from datetime import datetime, timedelta
from typing import List, Optional
from airflow import DAG
from airflow.decorators import task


@functools.lru_cache()
def get_start_date() -> datetime:
    return (
        pendulum.now(tz="America/Los_Angeles").replace(
            hour=2, minute=0, second=0, microsecond=0
        )
        - timedelta(days=2)
    ).astimezone(pendulum.tz.UTC)


def get_schedule_interval() -> Optional[str]:
    from airflow.configuration import conf  # type: ignore

    interval: Optional[str] = None
    if conf.get("compute", "env") == "prod":
        start_date: datetime = get_start_date()
        interval = "{} {} * * *".format(start_date.minute, start_date.hour)
    return interval


with DAG(
    dag_id="snowflake2postgresql_etl",
    start_date=get_start_date(),
    default_args=dict(
        email=["reddy.siddartha53@gmail.com"],
        email_on_failure=True,
    ),
    schedule_interval=get_schedule_interval(),
) as dag:
    requirements: List[str] = (
        open(
            "/usr/local/airflow/code/"
            "snowflake2postgresql_etl_requirements.txt"
        )
        .read()
        .strip()
        .split("\n")
    )

    @task.virtualenv(
        task_id="main",
        requirements=requirements[0].split(" ") + requirements[1:],
        system_site_packages=True,
        execution_timeout=timedelta(hours=2),
    )
    def main() -> None:
        from sample_snowflake2postgresql_etl.broker import Broker
        from airflow.configuration import conf  # type: ignore

        environment = conf.get("compute", "env")
        Broker(environment=f"map-{environment}", echo=True).main()

    main()
