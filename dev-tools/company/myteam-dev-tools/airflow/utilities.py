import functools
from typing import Any, Callable

from company.map_airflow_client.experimental.client import Client
from company.map_airflow_client.experimental.config import Config

lru_cache: Callable[..., Any] = functools.lru_cache


@lru_cache()
def get_client(environment: str, region: str = "us-west-2") -> Client:
    assert region in ("us-west-2", "us-east-1")
    return Client(
        Config(
            f"myteam-{environment}",
            region=region,
            client_id="company.myteam.etl",
            client_secret_cerberus_path=(
                "app/myteam/etl/client-secret"
            ),
        ),
        echo=True,
    )
