import logging
from inspect import signature
from typing import Any, Callable, Type, Union

from sqlalchemy import event  # type: ignore
from sqlalchemy.engine import Connection, Engine  # type: ignore
from sqlalchemy.exc import DatabaseError  # type: ignore
from sqlalchemy.sql import Selectable  # type: ignore
from sqlalchemy.sql.ddl import DropTable  # type: ignore
from sqlalchemy.sql.schema import SchemaItem, Table  # type: ignore

from .ddl import CreateView, DropView
from .declarative import Base
from .utilities import get_dialect_table_name

log: logging.Logger = logging.getLogger(__name__)


def _drop_table(table: Table, bind: Union[Engine, Connection]) -> None:
    """
    Attempt to drop a table for `bind`. Ignore all errors.
    """
    connection: Connection = (
        bind if isinstance(bind, Connection) else bind.connect()
    )
    try:
        if "if_exists" in signature(DropTable).parameters:
            connection.execute(DropTable(table, if_exists=True))
        else:
            # Prior to SQLAlchemy 1.4.0, `DropTable` had no "if_exists"
            # parameter
            connection.execute(DropTable(table))
    except Exception:
        pass


def _get_bind_select_statement(
    bind: Union[Engine, Connection],
    statement: Union[
        str,
        Selectable,
        Callable[[Union[Engine, Connection]], Union[str, Selectable, None]],
    ],
) -> Union[str, Selectable, None]:
    if not isinstance(statement, (str, Selectable)):
        statement = statement(bind)
    return statement


def create_as(
    statement: Union[
        str,
        Selectable,
        Callable[[Union[Engine, Connection]], Union[str, Selectable, None]],
    ],
    materialized: bool = False,
) -> Callable[[Type[Base]], Type[Base]]:
    """
    This function is a decorator which will cause an Object Relational Mapper
    to create a view rather than a table, where `statement` is the query.

    Parameters:
    - statement (str|sqlalchemy.sql.selectable.Selectable|
      sqlalchemy.engine.Engine|sqlalchemy.engine.Connection):
      This can be a string SELECT statement, a result from `sqlalchemy.select`,
      or a function which accepts a bind connection or engine and returns
      a SELECT statement or `sqlalchemy.select` result.
    - cascade_on_drop (bool) = True: This is only applicable if `materialized`
      is `False`.
    - materialized (bool) = False: Create a "materialized" view, if
      supported.
    - indexes ([sqlalchemy.Index]) = None: An optional list of indexes.
    - aliases ([sqlalchemy.sql.Alias]) = None: An optional list of aliases.
    """

    def wrapper(cls: Type[Base]) -> Type[Base]:
        """
        Create a materialized view from a `SELECT` statement or an instance of
        `sqlalchemy.sql.selectable.Selectable`.

        Parameters:

        - name (str)
        - statement (str|sqlalchemy.sql.selectable.Selectable): A string
          or an instance of
        - indexes ([sqlalchemy.sql.schema.Index)
        - metadata (sqlalchemy.sql.schema.Metadata)
        """
        # Flag this table as being a view
        cls.__table__.info.update(
            is_view=True, is_materialized_view=materialized
        )

        def before_create(
            target: SchemaItem, connection: Connection, **kwargs: Any
        ) -> None:
            # Only do something if the dialect-specific name is not
            # an empty string
            if get_dialect_table_name(connection.dialect, cls.__table__):
                _drop_table(cls.__table__, connection)
                try:
                    connection.execute(
                        DropView(
                            cls.__table__,
                            materialized=materialized,
                            if_exists=True,
                            bind=connection,
                        )
                    )
                except DatabaseError:
                    pass

        event.listen(cls.metadata, "before_create", before_create)

        def after_create(
            target: SchemaItem, connection: Connection, **kwargs: Any
        ) -> None:
            statement_: Union[str, Selectable] = _get_bind_select_statement(
                connection, statement
            )
            # Only do something if the dialect-specific name is not
            # an empty string
            if (
                (statement_ is not None)
                and statement_ != ""
                and get_dialect_table_name(
                    connection.dialect.name, cls.__table__
                )
            ):
                connection.execute(
                    CreateView(
                        cls.__table__,
                        statement_,
                        materialized=materialized,
                        bind=connection,
                    )
                )

        event.listen(cls.metadata, "after_create", after_create)

        def before_drop(
            target: SchemaItem, connection: Connection, **kwargs: Any
        ) -> None:
            if get_dialect_table_name(connection.dialect.name, cls.__table__):
                connection.execute(
                    DropView(
                        cls.__table__,
                        materialized=materialized,
                        bind=connection,
                    )
                )

        event.listen(cls.metadata, "before_drop", before_drop)
        return cls

    return wrapper
