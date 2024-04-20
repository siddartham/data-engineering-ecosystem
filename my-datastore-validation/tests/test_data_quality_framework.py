import functools
import os
import pickle
import unittest
from io import BytesIO
from typing import IO, Any, Callable, Tuple

from analytics_orm.errors import ValidationError
from my_datastore_model.base import Base
from my_datastore_model.common_dimension import Calculator
from my_datastore_model.dialects.sqlite import create_all
from sqlalchemy.engine.base import Engine  # type: ignore
from sqlalchemy.orm.session import Session, sessionmaker  # type: ignore
from sqlalchemy.schema import Column  # type: ignore
from sqlalchemy.sql.sqltypes import Integer, String  # type: ignore

from data_quality_framework.base import validate
from data_quality_framework.errors import (
    NonContiguousSeasonYearCodeError,
)

session_lru_cache: Callable[..., Session] = functools.lru_cache  # type: ignore
engine_lru_cache: Callable[..., Engine] = functools.lru_cache  # type: ignore
str_lru_cache: Callable[..., str] = functools.lru_cache  # type: ignore


SQLITE_PATH: str = os.path.join(os.path.dirname(__file__), ".sqlite")


class _TestSeasonYear(Base):
    test_id = Column("TEST_ID", Integer, primary_key=True, autoincrement=False)
    season_year_code = Column("SEASON_YEAR_CODE", String, primary_key=True)


class TestValidation(unittest.TestCase):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        if os.path.exists(SQLITE_PATH):
            os.remove(SQLITE_PATH)
        super().__init__(*args, **kwargs)

    @property  # type: ignore
    @engine_lru_cache()
    def bind(self) -> Engine:
        return create_all(SQLITE_PATH, checkfirst=True)

    @property  # type: ignore
    @session_lru_cache()
    def session(self) -> Session:
        return sessionmaker(self.bind)()

    def test_validate(self) -> None:
        # Populate incomplete data
        self.session.add_all(
            (
                _TestSeasonYear(test_id=1, season_year_code="SP1999"),
                _TestSeasonYear(test_id=1, season_year_code="SU1999"),
                _TestSeasonYear(test_id=1, season_year_code="FA1999"),
                _TestSeasonYear(test_id=1, season_year_code="HO1999"),
                _TestSeasonYear(test_id=1, season_year_code="SU2000"),
                Calculator(calculator_version="0.0.0", ordinal=0),
                Calculator(calculator_version="1.0.0", ordinal=1),
            )
        )
        self.session.commit()
        errors: Tuple[ValidationError, ...] = validate(  # type: ignore
            Base, bind=self.bind, return_type=Exception
        )
        assert errors and isinstance(
            errors[0], NonContiguousSeasonYearCodeError
        )
        # Verify that the error can be pickled
        pickle_io: IO[bytes]
        with BytesIO() as pickle_io:
            pickle.dump(errors[0], pickle_io)
            pickle_io.seek(0)
            assert isinstance(
                pickle.load(pickle_io), NonContiguousSeasonYearCodeError
            )
        # Complete the series
        self.session.add(_TestSeasonYear(test_id=2, season_year_code="SP2000"))
        self.session.commit()
        errors = validate(  # type: ignore
            Base, bind=self.bind, return_type=Exception
        )
        assert not errors


if __name__ == "__main__":
    unittest.main()
