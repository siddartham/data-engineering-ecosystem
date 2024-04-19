import pytest
from cerberus_assistant.get import get_secret
from sqlalchemy.engine.base import Connection  # type: ignore

from analytics_orm.databricks import create_engine

DATABRICKS_HTTP_PATH: str = "/sql/1.0/warehouses/1234rrrree33254ff"
DATABRICKS_DEV_SCHEMA: str = "my_datastore_dev"
DATABRICKS_ACCESS_TOKEN: str = get_secret(
    "app/sustainability/sustainability/ServicePrincipal-react."
    "cloud.databricks.com_App.community.sustainability.Developer"
)


@pytest.fixture(name="databricks_dev_connection", scope="session")
def get_databricks_dev_connection() -> Connection:
    return create_engine(
        schema=DATABRICKS_DEV_SCHEMA,
        http_path=DATABRICKS_HTTP_PATH,
        access_token=DATABRICKS_ACCESS_TOKEN,
    ).connect()
