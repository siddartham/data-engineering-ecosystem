import functools
import os
import unittest
from pathlib import Path
from typing import Any, Callable

from my_datastore_orm.dialects.sqlite import (
    create_all,
    drop_all,
    validate,
)

lru_cache: Callable[..., Any] = functools.lru_cache
SQLITE_PATH: Path = (
    Path(__file__).absolute().parent.joinpath("data", "my_org.sqlite")
)


class TestSQLite(unittest.TestCase):
    """
    This test case verifies that the model can be used to create a SQLite
    database
    """

    def test_create(self) -> None:
        """
        Make sure creating the database from scratch can be done without
        errors.
        """
        try:
            os.remove(SQLITE_PATH)
        except FileNotFoundError:
            os.makedirs(SQLITE_PATH.parent, exist_ok=True)
        index: int
        for index in range(2):
            create_all(str(SQLITE_PATH), echo=True)
        create_all(str(SQLITE_PATH), views_only=True)
        validate(str(SQLITE_PATH), echo=True)
        drop_all(str(SQLITE_PATH), echo=True)


if __name__ == "__main__":
    unittest.main()
