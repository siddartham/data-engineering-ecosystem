import functools
from abc import ABC, abstractmethod
from collections import namedtuple
from typing import (
    Any,
    Callable,
    Iterable,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
)

import sqlalchemy.engine  # type: ignore
import sqlalchemy.orm  # type: ignore
from orm_framework.declarative import (
    Base,
    create_engine,
    get_class_table_name,
)
from sqlalchemy.engine import Connection  # type: ignore
from sqlalchemy.engine.row import Row  # type: ignore

_CONNECTION_STRING: str = "sqlite:///:memory:"


class Session(sqlalchemy.orm.Session):
    """
    This class wraps a SQLAlchemy ORM Session in order to capture a set
    identifying all classes which have data added/merged in the session
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.populated_classes: Set[Type[Base]] = set()
        super().__init__(*args, **kwargs)

    def add(self, instance: Base) -> None:
        self.populated_classes.add(type(instance))
        super().add(instance)

    def merge(
        self,
        instance: Base,
        load: bool = True,
        options: Optional[Sequence[Any]] = None,
    ) -> None:
        self.populated_classes.add(type(instance))
        super().merge(instance, load=load, options=options)


session_lru_cache: Callable[..., Session] = functools.lru_cache  # type: ignore


def _default_filter_function(table_name: str, cls: Type[Base]) -> bool:
    return True


class Transformer(ABC):
    """
    A base class for transforming source data into (validated) iterables
    of named tuples suitable for populating Sustainability Analytics'
    Snowflake, Hive/Presto, and PostgreSQL databases.

    Iterating over an instance of this class will yield 3-part tuples:

    - [0] (str) The table name
    - [1] (type) The table ORM class
    - [2] (typing.Iterable[tuple]) The results from `SELECT * from
      {SCHEMA}.{TABLE}`, as named tuples

    Public Properties:

    - session (sqlalchemy.orm.Session): A SQLAlchemy ORM session
      for interacting with the in-memory SQLite representation of `data`

    Initialization Parameters:
    - data: If provided, this is passed to `.add()`
    - echo (bool): If `True`, all SQL statements are printed to
      `sys.stdout`
    - base (typing.Type[orm_framework.declarative.Base]):
      A SQLAlchemy ORM declarative base
    """

    def __init__(
        self,
        data: Any = None,
        echo: bool = False,
        base: Type[Base] = Base,
    ) -> None:
        self.base: Type[Base] = base
        self.echo: bool = echo
        if data:
            self.add(data)

    @abstractmethod
    def add(self, data: Any) -> None:
        raise NotImplementedError()

    @property  # type: ignore
    @session_lru_cache()
    def session(self) -> Session:
        """
        Invoking this property:

        - Creates a cached, in-memory, SQLite database (or accesses
          that cached database)
        - Creates tables in the database conforming to the model defined in
          your declarative base
        - Returns an ORM session
        """
        engine: sqlalchemy.engine.Engine = create_engine(
            _CONNECTION_STRING,
            echo=self.echo,
        )
        connection: Connection = engine.connect()
        session: sqlalchemy.orm.Session = sqlalchemy.orm.sessionmaker(
            bind=connection, class_=Session
        )()
        assert self.base is not Base, "You must provide a declarative base"
        self.base.metadata.create_all(bind=connection)
        # Ensure tables were actually created
        table_count: int = next(
            connection.exec_driver_sql(
                "SELECT count(*) as table_count "
                "FROM sqlite_master where type='table'"
            )
        )[0]
        assert table_count, "No tables were created!"
        return session

    def _iter_table_rows(self, table: Type[Base]) -> Iterable[tuple]:
        """
        This method fetches all rows from a table in our in-memory SQLite
        database, and yields each row as a named tuple
        """
        row_type: type = tuple
        row: Row
        for row in self.session.bind.execute(
            self.session.query(table).statement
        ):
            if row_type is tuple:
                row_type = namedtuple("Row", row.keys())  # type: ignore
            yield row_type(*row)

    def iter_tables(
        self,
        filter_function: Callable[
            [str, Type[Base]], bool
        ] = _default_filter_function,
    ) -> Iterable[Tuple[str, Type[Base], Iterable[tuple]]]:
        """
        Yields three-item tuples where the first item is the table name, the
        second is the mapping class, and the third is an iterable of named
        tuples representing the rows in that table which were added to this
        transformer's session

        Parameters:

        - filter_function: A function which accepts a table name and mapping
          class (in that order) as positional arguments and returns a boolean
          indicating whether to include the table in our resulting iterable
        """
        cls: Type[Base]
        for cls in self.session.populated_classes:
            table_name: str = get_class_table_name(cls, dialect_name="sqlite")
            if table_name != "" and filter_function(table_name, cls):
                yield (
                    table_name,
                    cls,
                    self._iter_table_rows(cls),
                )

    def __iter__(self) -> Iterable[Tuple[str, Type[Base], Iterable[tuple]]]:
        """
        Iterating over an instance of this class yields three-item tuples where
        the first item is the table name, the second is the mapping class, and
        the third is an iterable of named tuples representing the rows in that
        table which were added to this transformer's session. To filter
        results, use `.iter_tables(filter_)
        """
        return self.iter_tables()
