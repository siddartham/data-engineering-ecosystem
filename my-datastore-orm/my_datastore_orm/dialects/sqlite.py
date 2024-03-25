from typing import Callable, Iterable, Optional, Union

from orm_framework import sqlite
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.sql.schema import ForeignKeyConstraint, Table  # type: ignore

from ..base import Base


def create_all(
    path: str = "",
    echo: bool = False,
    checkfirst: bool = True,
    tables: Optional[Iterable[Table]] = None,
    views_only: bool = False,
    bind: Union[Engine, Connection, None] = None,
) -> Engine:
    return sqlite.create_all(
        Base,
        path=path,
        echo=echo,
        checkfirst=checkfirst,
        tables=tables,
        views_only=views_only,
        bind=bind,
    )


def drop_all(
    path: str = "",
    echo: bool = False,
    checkfirst: bool = True,
    tables: Optional[Iterable[Table]] = None,
    views_only: bool = False,
    bind: Union[Engine, Connection, None] = None,
    undeclared: bool = False,
    undeclared_only: bool = False,
) -> Engine:
    sqlite.drop_all(
        Base,
        path=path,
        echo=echo,
        checkfirst=checkfirst,
        tables=tables,
        views_only=views_only,
        bind=bind,
        undeclared=undeclared,
        undeclared_only=undeclared_only,
    )


def validate(
    path: str = "",
    echo: bool = False,
    bind: Union[Engine, Connection, None] = None,
    ignore_foreign_keys: Union[
        Iterable[str], Callable[[ForeignKeyConstraint], bool], None
    ] = None,
) -> Engine:
    """
    Validate the sqlite database at the specified `path`, or represented by
    the specified `bind`, against sub-classes of the declarative `base`.

    Parameters:

    - echo (bool)
    - bind (sqlalchemy.Engine|sqlalchemy.Connection|None)
    - ignore_foreign_keys ([str]|callable)
    """
    sqlite.validate(
        Base,
        path=path,
        echo=echo,
        bind=bind,
        ignore_foreign_keys=ignore_foreign_keys,
    )


def main() -> None:
    """
    This function is the entry point for the
    `my-datastore-orm sqlite` command.
    Execute `my-datastore-orm sqlite -h` for information
    about his command.
    """
    sqlite.main(Base, "my-datastore-orm sqlite")


if __name__ == "__main__":
    main()
