import functools
import os
import pickle
import unittest
from inspect import Parameter, signature
from io import BytesIO
from itertools import islice
from typing import IO, Any, Callable, Dict, Optional, Tuple, Type

from analytics_orm.declarative import declarative_base
from analytics_orm.errors import (
    ColumnNameError,
    ColumnsNotDeclaredError,
    ColumnTypeError,
    ColumnValidationError,
    ForeignKeyMissingReferenceError,
    PrimaryKeyNotUniqueError,
    TableNotDeclaredError,
    TableNotReflectedError,
    TablesNotDeclaredError,
    TablesValidationError,
    TableValidationError,
    ValidationError,
    ViewCacheError,
    ViewValidationError,
)
from analytics_orm.utilities import iter_recursive_subclasses
from analytics_orm.validation import _Validator, validate
from sqlalchemy.engine.base import Engine  # type: ignore
from sqlalchemy.engine.create import create_engine  # type: ignore
from sqlalchemy.engine.url import URL  # type: ignore
from sqlalchemy.orm.session import Session, sessionmaker  # type: ignore
from sqlalchemy.sql.schema import (  # type: ignore # noqa
    Column,
    ForeignKey,
    ForeignKeyConstraint,
)
from sqlalchemy.types import Integer, String  # type: ignore

session_lru_cache: Callable[..., Session] = functools.lru_cache  # type: ignore
engine_lru_cache: Callable[..., Engine] = functools.lru_cache  # type: ignore
ERRORS: Tuple[Type[ValidationError], ...] = (
    ValidationError,
    ForeignKeyMissingReferenceError,
    TableValidationError,
    TableNotReflectedError,
    TableNotDeclaredError,
    PrimaryKeyNotUniqueError,
    ViewValidationError,
    ViewCacheError,
    TablesValidationError,
    TablesNotDeclaredError,
    ColumnValidationError,
    ColumnNameError,
    ColumnTypeError,
    ColumnsNotDeclaredError,
)

ValidBase: Any = declarative_base(name="ValidBase")


class ValidA(ValidBase):
    __tablename__: str = "A"

    a_id: int = Column("A_ID", Integer, primary_key=True)
    name: str = Column("NAME", String)


class ValidB(ValidBase):
    __tablename__: str = "B"

    b_id: int = Column("B_ID", Integer, primary_key=True)
    name: str = Column("NAME", String)


class ValidAB1(ValidBase):
    __tablename__: str = "AB1"

    a_id: int = Column(
        "A_ID", Integer, ForeignKey(ValidA.a_id), primary_key=True
    )
    b_id: int = Column(
        "B_ID", Integer, ForeignKey(ValidB.b_id), primary_key=True
    )
    name: str = Column("NAME", String)


class ValidAB2(ValidBase):
    __tablename__: str = "AB2"

    a_id: int = Column("A_ID", Integer, primary_key=True)
    b_id: int = Column("B_ID", Integer, primary_key=True)
    name: str = Column("NAME", String)


class ValidABC1(ValidBase):
    __tablename__: str = "ABC1"

    a_id: int = Column("A_ID", Integer, primary_key=True)
    b_id: int = Column("B_ID", Integer, primary_key=True)
    c_id: int = Column("c_ID", Integer, primary_key=True)
    name: str = Column("NAME", String)


class ValidABCD1(ValidBase):
    __tablename__: str = "ABCD1"

    a_id: int = Column("A_ID", Integer, primary_key=True)
    b_id: int = Column("B_ID", Integer, primary_key=True)
    c_id: int = Column("C_ID", Integer, primary_key=True)
    d_id: int = Column("D_ID", Integer)
    name: str = Column("NAME", String)


ForeignKeyConstraint(
    columns=("B_ID",),
    refcolumns=(ValidABCD1.d_id,),
    table=ValidABCD1.__table__,
)

InvalidBase1: Any = declarative_base(name="InvalidBase1")


class Invalid1A(InvalidBase1):
    __tablename__: str = "A"

    a_id: int = Column("A_ID", Integer, primary_key=True)
    name: str = Column("NAME", String)


class Invalid1B(InvalidBase1):
    __tablename__: str = "B"

    b_id: int = Column("B_ID", Integer, primary_key=True)
    name: str = Column("NAME", String)


class Invalid1C(InvalidBase1):
    __tablename__: str = "C"

    c_id_typo: int = Column("C_ID", Integer, primary_key=True)
    name: str = Column("NAME", String)


class Invalid1AB1(InvalidBase1):
    __tablename__: str = "AB1"

    a_id: int = Column(
        "A_ID", Integer, ForeignKey(Invalid1A.a_id), primary_key=True
    )
    b_id: int = Column(
        "B_ID", Integer, ForeignKey(Invalid1B.b_id), primary_key=True
    )
    name: str = Column("NAME", String)


class Invalid1AB2(InvalidBase1):
    __tablename__: str = "AB2"

    a_id: int = Column(
        "A_ID", Integer, ForeignKey(Invalid1A.a_id), primary_key=True
    )
    b_id: int = Column(
        "B_ID", Integer, ForeignKey(Invalid1B.b_id), primary_key=True
    )
    name: str = Column("NAME", String)


class InvalidABC1(InvalidBase1):
    __tablename__: str = "ABC1"

    a_id: int = Column("A_ID", Integer, primary_key=True)
    b_id: int = Column("B_ID", Integer, primary_key=True)
    c_id: int = Column("c_ID", Integer)
    name: str = Column("NAME", String)


class InvalidABCD1(InvalidBase1):
    __tablename__: str = "ABCD1"

    a_id: int = Column("A_ID", Integer, primary_key=True)
    b_id: int = Column("B_ID", Integer, primary_key=True)
    c_id: int = Column("C_ID", Integer, primary_key=True)
    d_id: int = Column("D_ID", Integer)
    name: str = Column("NAME", String)


SQLITE_PATH: str = os.path.join(os.path.dirname(__file__), ".sqlite")


def get_validation_error_init_kwargs(
    cls: Type[ValidationError],
) -> Dict[str, Any]:
    """
    Generate dummy keyword arguments for error class initialization
    """
    kwargs: Dict[str, Any] = {}
    parameter: Parameter
    for parameter in islice(
        signature(cls.__init__).parameters.values(), 1, None
    ):
        if isinstance(parameter.annotation, type):
            if issubclass(parameter.annotation, str):
                kwargs[parameter.name] = "DUMMY_VALUE"
            elif issubclass(parameter.annotation, int):
                kwargs[parameter.name] = 1
            elif issubclass(parameter.annotation, float):
                kwargs[parameter.name] = 1.0
            else:
                kwargs[parameter.name] = ()
        else:
            kwargs[parameter.name] = ()
    if issubclass(cls, ViewCacheError):
        kwargs.update(response_time_seconds=2.0)
    return kwargs


class TestValidation(unittest.TestCase):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        if os.path.exists(SQLITE_PATH):
            os.remove(SQLITE_PATH)
        super().__init__(*args, **kwargs)

    @property  # type: ignore
    @engine_lru_cache()
    def bind(self) -> Engine:
        engine: Engine = create_engine(
            URL.create("sqlite", database=SQLITE_PATH),
        )
        ValidBase.metadata.bind = engine
        ValidBase.metadata.drop_all()
        ValidBase.metadata.create_all(checkfirst=True)
        return engine

    @property  # type: ignore
    @session_lru_cache()
    def session(self) -> Session:
        return sessionmaker(self.bind)()

    def test_pickle(self) -> None:
        """
        Verify that a validator and all errors can be pickled and unpickled
        """
        validator: _Validator = _Validator(base=ValidBase, bind=self.bind)
        pickle_io: IO[bytes]
        with BytesIO() as pickle_io:
            pickle.dump(validator, pickle_io)
            pickle_io.seek(0)
            unpickled_validator: _Validator = pickle.load(pickle_io)
            assert isinstance(unpickled_validator, _Validator)
        Error_: Type[ValidationError]
        for Error_ in ERRORS:
            with BytesIO() as pickle_io:
                kwargs: Dict[str, Any] = get_validation_error_init_kwargs(
                    Error_
                )
                pickle.dump(Error_(**kwargs), pickle_io)
                pickle_io.seek(0)
                unpickled_error: Exception = pickle.load(pickle_io)
                assert isinstance(unpickled_error, Error_)

    def populate(self) -> None:
        self.session.add_all(
            (
                ValidA(a_id=0, name="A0"),
                ValidA(a_id=1, name="A1"),
                ValidA(a_id=2, name="A2"),
                ValidB(b_id=0, name="B0"),
                ValidB(b_id=1, name="B1"),
                ValidB(b_id=2, name="B2"),
                ValidAB1(a_id=0, b_id=0, name="A0B0"),
                ValidAB1(a_id=1, b_id=1, name="A1B1"),
                ValidAB1(a_id=2, b_id=2, name="A2B2"),
                ValidAB2(a_id=3, b_id=3, name="A3B3"),
                ValidAB2(a_id=4, b_id=4, name="A4B4"),
                ValidAB2(a_id=5, b_id=5, name="A5B5"),
                ValidABC1(a_id=0, b_id=0, c_id=0, name="A0B0C0"),
                ValidABC1(a_id=0, b_id=0, c_id=1, name="A0B0C1"),
                ValidABC1(a_id=0, b_id=0, c_id=2, name="A0B0C2"),
                ValidABCD1(a_id=0, b_id=0, c_id=2, d_id=0, name="A0B0C2D2"),
                ValidABCD1(a_id=0, b_id=0, c_id=3, d_id=3, name="A0B0C3D3"),
            )
        )
        self.session.commit()

    def test_validate(self) -> None:
        assert len(tuple(iter_recursive_subclasses(ValidBase))) > 0
        self.populate()
        validate(ValidBase, self.bind)
        validation_error: Optional[ValidationError] = None
        try:
            validate(InvalidBase1, self.bind, only="C")
        except ColumnNameError as error:
            validation_error = error
        assert isinstance(
            validation_error, ColumnNameError
        ), f"{type(validation_error).__name__} != ColumnNameError"
        validation_error = None
        try:
            validate(InvalidBase1, self.bind, only="AB2")
        except ForeignKeyMissingReferenceError as error:
            validation_error = error
        assert isinstance(validation_error, ForeignKeyMissingReferenceError), (
            f"{type(validation_error).__name__} != "
            "ForeignKeyMissingReferenceError"
        )


if __name__ == "__main__":
    unittest.main()
