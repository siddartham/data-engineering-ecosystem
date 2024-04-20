from argparse import Namespace
from typing import TYPE_CHECKING, Callable, Sequence, Union

from analytics_orm.sqlite import create_engine, parse_arguments
from my_datastore_model.base import Base
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.sql.schema import ForeignKeyConstraint  # type: ignore

from ..base import validate as _validate


def validate(
    path: str = "",
    echo: bool = False,
    bind: Union[Engine, Connection, None] = None,
    ignore_foreign_keys: Union[
        Sequence[str], Callable[[ForeignKeyConstraint], bool], None
    ] = None,
    only: Sequence[str] = (),
) -> Engine:
    """
    Validate the sqlite database at the specified `path`, or represented by
    the specified `bind`, against sub-classes of the declarative `base`.

    Parameters:

    - echo (bool)
    - bind (sqlalchemy.Engine|sqlalchemy.Connection|None)
    - ignore_foreign_keys ([str]|callable)
    - only ([str])
    """
    if not bind:
        bind = create_engine(path=path, echo=echo)
    _validate(
        Base,
        bind=bind,
        ignore_foreign_keys=ignore_foreign_keys,
        only=only,
        echo=echo,
    )
    if isinstance(bind, Engine):
        return bind
    else:
        if TYPE_CHECKING:
            assert bind and isinstance(bind.engine, Engine)
        return bind.engine


def main() -> None:
    """
    This function is the entry point for the
    `my-datastore-validation sqlite` command.
    Execute `my-datastore-model sqlite -h` for information
    about his command.
    """
    arguments: Namespace = parse_arguments(
        "my-datastore-validation sqlite",
        commands=(),
        include=(
            "echo",
            "ignore_foreign_key",
            "log",
            "only_validate",
            "path",
        ),
    )
    validate(
        path=arguments.path,
        ignore_foreign_keys=arguments.ignore_foreign_keys,
        only=arguments.only,
        echo=arguments.echo,
    )
