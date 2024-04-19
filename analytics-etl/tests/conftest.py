import pytest
from my_datastore_etl.broker import Broker


@pytest.fixture(name="map_prod_broker", scope="session")
def get_map_prod_broker() -> Broker:
    return Broker("map-prod", echo=True)


@pytest.fixture(name="map_dev_broker", scope="session")
def get_map_dev_broker() -> Broker:
    return Broker("map-dev", echo=True)


@pytest.fixture(name="local_broker", scope="session")
def get_local_broker() -> Broker:
    return Broker("local", echo=True)
