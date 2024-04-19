import functools
import unittest
from pathlib import Path
from time import sleep
from typing import Callable

from analytics_orm.utilities import run
from my_datastore_etl.broker import Broker
from my_datastore_orm.dialects.postgresql import create_environment

broker_lru_cache: Callable[[], Broker] = functools.lru_cache  # type: ignore
TESTS_PATH: Path = Path(__file__).absolute().parent


class TestPostgreSQL(unittest.TestCase):
    """
    This test case verifies PostgreSQL integration is functional
    """

    @classmethod
    def setUpClass(cls) -> None:
        run(
            [
                "docker-compose",
                "-f",
                str(TESTS_PATH.joinpath("postgres-docker-compose.yml")),
                "--project-directory",
                str(TESTS_PATH),
                "up",
                "-d",
            ],
        )
        sleep(20)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        run(
            [
                "docker-compose",
                "-f",
                str(TESTS_PATH.joinpath("postgres-docker-compose.yml")),
                "--project-directory",
                str(TESTS_PATH),
                "down",
            ],
        )
        return super().tearDownClass()

    @property  # type: ignore
    @broker_lru_cache()
    def broker(self) -> Broker:
        return Broker("local")

    def test_create(self) -> None:
        create_environment(
            "dev", bind=self.broker.work.postgresql_session.bind
        )


if __name__ == "__main__":
    unittest.main()
