from argparse import Namespace
from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from sqlalchemy import Table  # type: ignore
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.engine.create import (  # type: ignore  # noqa
    create_engine as create_engine_,
)
from sqlalchemy.engine.url import URL  # type: ignore
from sqlalchemy.sql.schema import ForeignKeyConstraint  # type: ignore

from .cli import parse_arguments as _parse_arguments
from .declarative import Base
from .utilities import translate_all_engine_schemas_to
from .validation import validate as _validate

__all__: List[str] = [
    "parse_arguments",
    "get_connection_string",
    "create_engine",
    "main",
]
COMMANDS: Tuple[str, ...] = ("create", "drop", "validate")


def get_connection_string(path: str) -> URL:
    """
    Get a connection string for a SQLite database located at `path`.
    """
    return URL.create(drivername="sqlite", database=path.replace("\\", "\\\\"))


def parse_arguments(
    prog: str = "",
    commands: Sequence[str] = COMMANDS,
    include: Iterable[str] = (
        "checkfirst",
        "command",
        "echo",
        "ignore_foreign_key",
        "log",
        "only_validate",
        "path",
        "undeclared",
        "undeclared_only",
        "views_only",
    ),
) -> Namespace:
    """
    Parse sqlite CLI arguments and return the resulting instance of
    `argparse.Namespace`. This function is intended to parse
    arguments for a sub-command under `parent_command`.

    Parameters:

    - prog (str): The CLI command or command + sub-command
      triggering this function. For example:
      "my-datastore-model sqlite".
    - commands ([str]) = ("dev", "qa", "prod"):
      Valid values for the `command` argument. If an empty tuple/list is
      provided, no "command" argument is added to the parser
    - include ({str}): An iterable of the names of all parameters to include.
      If not provided, *all* parameters are used

    This function returns a `Namespace` object with properties corresponding
    to those specified in the `include` argument.
    """
    return _parse_arguments(prog=prog, commands=commands, include=include)


def create_engine(
    path: Union[URL, str], echo: bool = False, **kwargs: Any
) -> Engine:
    """
    Create a SQLAlchemy engine for connecting to (or creating) a SQLite
    database located at `path`.

    Parameters:

    - **path** (str): The file path where the database is, or will be, located.
    - **echo** (bool) = False
    - **kwargs (typing.Any): Additional keyword argument to pass to
      `sqlalchemy.engine.create_engine`.
    """
    if isinstance(path, str):
        path = get_connection_string(path)
    return translate_all_engine_schemas_to(
        create_engine_(path, echo=echo, future=True, **kwargs),
        None,
    )


def create_all(
    base: Type[Base],
    path: str = "",
    echo: bool = False,
    checkfirst: bool = True,
    tables: Optional[Iterable[Table]] = None,
    views_only: bool = False,
    bind: Union[Engine, Connection, None] = None,
) -> Engine:
    """
    Create the database and all schemas & (optionally) tables in the database.
    """
    if not bind:
        bind = create_engine(path=path, echo=echo)
    if views_only and not tables:
        base.metadata.create_views(  # type: ignore
            bind=bind, checkfirst=checkfirst
        )
    else:
        base.metadata.create_all(  # type: ignore
            bind=bind, checkfirst=checkfirst, tables=tables
        )
    return bind


def drop_all(
    base: Type[Base],
    path: str = "",
    echo: bool = False,
    checkfirst: bool = True,
    tables: Optional[Iterable[Table]] = None,
    views_only: bool = False,
    bind: Union[Engine, Connection, None] = None,
    undeclared: bool = True,
    undeclared_only: bool = False,
) -> Engine:
    """
    Drop all views & (optionally) tables in the database.
    """
    if not bind:
        bind = create_engine(path=path, echo=echo)
    if undeclared or undeclared_only:
        base.metadata.drop_undeclared(bind=bind)  # type: ignore
        if undeclared_only:
            return bind
    if views_only and not tables:
        base.metadata.drop_views(  # type: ignore
            bind=bind, checkfirst=checkfirst
        )
    else:
        base.metadata.drop_all(  # type: ignore
            bind=bind, checkfirst=checkfirst, tables=tables
        )
    return bind


def validate(
    base: Type[Base],
    path: str = "",
    echo: bool = False,
    bind: Union[Engine, Connection, None] = None,
    only: Sequence[str] = (),
    ignore_foreign_keys: Union[
        Iterable[str], Callable[[ForeignKeyConstraint], bool], None
    ] = None,
) -> Engine:
    """
    Validate the sqlite database at the specified `path`, or represented by
    the specified `bind`, against sub-classes of the declarative `base`.
    """
    if not bind:
        bind = create_engine(path=path, echo=echo)
    _validate(base, bind, only=only, ignore_foreign_keys=ignore_foreign_keys)
    return bind.engine if isinstance(bind, Connection) else bind


def main(base: Type[Base], prog: str = "") -> None:
    """
    This function parses command-line arguments and executes a function
    based on the input using the provided `base`. The program
    name (`prog`) is used for reference in the CLI's `--help` documentation.

    Parameters:

    - base (type)
    - prog (str) = "": The command or command + sub-command triggering this
      function. For example: "my-datastore-model create".
    """
    arguments: Namespace = parse_arguments(prog)
    if arguments.command in COMMANDS:
        if arguments.command == "create":
            create_all(
                base=base,
                path=arguments.path,
                echo=arguments.echo,
                checkfirst=arguments.checkfirst,
                views_only=arguments.views_only,
            )
        elif arguments.command == "drop":
            drop_all(
                base=base,
                path=arguments.path,
                echo=arguments.echo,
                checkfirst=arguments.checkfirst,
                views_only=arguments.views_only,
                undeclared=arguments.undeclared,
                undeclared_only=arguments.undeclared_only,
            )
        else:
            validate(
                base=base,
                path=arguments.path,
                echo=arguments.echo,
                only=arguments.only_validate,
            )
