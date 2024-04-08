import importlib
import json
from types import ModuleType
from typing import Any, Dict, Sequence, Type, Union

from sqlalchemy import JSON, String, types  # type: ignore
from sqlalchemy.engine import Dialect  # type: ignore
from sqlalchemy.ext.mutable import MutableDict, MutableList  # type: ignore
from sqlalchemy.sql.type_api import TypeEngine  # type: ignore

from .utilities import SUPPORTED_DIALECTS

try:
    from snowflake.sqlalchemy import ARRAY, OBJECT  # type: ignore
except ImportError:
    OBJECT = None


class Enum(types.Enum):
    """
    This class serves as a wrapper for `sqlalchemy.sql.types.Enum` which
    defaults the argument *create_constraint* to `False` instead of `True`.
    This is because Snowflake and Hive do not support `CHECK` constraints, and
    we don't really want to incur the overhead of a constraint--we just want
    to reduce storage use when/if a *native* ENUM type is available.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs["create_constraint"] = False
        super().__init__(*args, **kwargs)


def _get_dialect_name(dialect: Dialect) -> str:
    dialect_name: Union[str, bytes] = getattr(dialect, "name")
    if isinstance(dialect_name, bytes):
        dialect_name = str(dialect_name, encoding="utf-8")
    if dialect_name not in SUPPORTED_DIALECTS:
        raise ValueError(dialect_name)
    return dialect_name


class Object(types.TypeDecorator):
    """
    This type is a stand-in which is swapped out for
    `snowflake.sqlalchemy.OBJECT` when using Snowflake,
    `sqlalchemy.JSON` when using JSON-compatible databases, or
    `sqlalchemy.String` when using all other databases.

    Please note that this type in not mutable, use `MutableObject`
    if value changes must be propagated.
    """

    cache_ok: bool = True
    impl: Type[types.TypeEngine] = types.JSON

    def load_dialect_impl(self, dialect: Dialect) -> TypeEngine:
        dialect_name: str = _get_dialect_name(dialect)
        if isinstance(dialect_name, bytes):
            dialect_name = str(dialect_name, encoding="utf-8")
        if dialect_name == "snowflake":
            return dialect.type_descriptor(OBJECT())
        elif dialect_name in ("hive", "presto", "default"):
            return dialect.type_descriptor(types.String())
        elif dialect_name in ("sqlite", "postgresql"):
            return dialect.type_descriptor(types.JSON())
        elif dialect_name in ("databricks",):
            return dialect.type_descriptor(types.String())
        else:
            raise ValueError(dialect_name)

    def process_bind_param(
        self, value: Union[Dict[str, Any], str, None], dialect: Dialect
    ) -> Union[Dict[str, Any], str, None]:
        dialect_name: str = _get_dialect_name(dialect)
        if isinstance(value, dict) and dialect_name in (
            "hive",
            "snowflake",
            "databricks",
        ):
            return json.dumps(value)
        else:
            return value

    def process_result_value(
        self, value: Union[Dict[str, Any], str, None], dialect: Dialect
    ) -> Union[Dict[str, Any], None]:
        if isinstance(value, str):
            return json.loads(value)
        else:
            return value


MutableObject: Type[Object] = MutableDict.as_mutable(Object)


class Array(types.TypeDecorator):
    """
    This type is a stand-in which is swapped out for
    `snowflake.sqlalchemy.ARRAY` when using Snowflake,
    `sqlalchemy.JSON` when using JSON-compatible databases, or
    `sqlalchemy.String` when using all other databases.
    """

    cache_ok: bool = True
    impl: Type[types.TypeEngine] = types.JSON

    def load_dialect_impl(self, dialect: Dialect) -> TypeEngine:
        dialect_name: str = _get_dialect_name(dialect)
        if dialect_name in ("snowflake",):
            return dialect.type_descriptor(ARRAY())
        elif dialect_name in ("hive", "presto", "default"):
            return dialect.type_descriptor(types.String())
        elif dialect_name in ("sqlite", "postgresql"):
            return dialect.type_descriptor(types.JSON())
        elif dialect_name in ("databricks",):
            return dialect.type_descriptor(types.String())
        else:
            raise ValueError(dialect_name)

    def process_bind_param(
        self, value: Union[Sequence[str], str, None], dialect: Dialect
    ) -> Union[Sequence[str], str, None]:
        dialect_name: str = _get_dialect_name(dialect)
        if (
            isinstance(value, Sequence)
            and not isinstance(value, str)
            and dialect_name
            in (
                "hive",
                "snowflake",
                "databricks",
            )
        ):
            return json.dumps(value)
        else:
            return value

    def process_result_value(
        self, value: Union[Sequence[str], str, None], dialect: Dialect
    ) -> Union[Sequence[str], str, None]:
        if isinstance(value, str):
            return json.loads(value)
        else:
            return value


MutableArray: Type[Array] = MutableList.as_mutable(Array)


def get_column_type_class(
    column_type: Union[Type[TypeEngine], TypeEngine]
) -> Union[Type[TypeEngine], TypeEngine]:
    """
    SQLAlchemy column types can either be a sub-class of `TypeEngine` or an
    instance of a sub-class of `TypeEngine`, so this is a convenience
    function to return the *class*.
    """
    if isinstance(column_type, type):
        return column_type
    else:
        return type(column_type)


def _get_snowflake_column_type(
    generic_column_type: Union[Type[TypeEngine], TypeEngine]
) -> Union[Type[TypeEngine], TypeEngine]:
    """
    This function returns an equivalent of `generic_column_type` which is
    specific to Snowflake, if one exists, otherwise `generic_column_type`
    is returned
    """
    column_type: Union[Type[TypeEngine], TypeEngine]
    column_type_class: Type[TypeEngine]
    # Dynamically import Snowflake custom types to account for installations
    # which do not include the "snowflake" extra requirements
    snowflake_custom_types: ModuleType = importlib.import_module(
        "snowflake.sqlalchemy.custom_types"
    )
    # The column type can be either a class or a class instance, so here
    # we get the *class*
    generic_column_type_class: Type[TypeEngine] = get_column_type_class(
        generic_column_type
    )
    if issubclass(generic_column_type_class, (Object, Array)):
        # If the column type is a sub-class of a type for which we have
        # a dialect-specific alternative, we replace it
        if issubclass(generic_column_type_class, Array):
            column_type_class = getattr(snowflake_custom_types, "ARRAY")
        else:
            column_type_class = getattr(snowflake_custom_types, "OBJECT")
        if generic_column_type_class is generic_column_type:
            # If the generic column type we received was a class,
            # pass back the equivalent Snowflake type
            column_type = column_type_class
        else:
            # If the generic column type we received was a class instance,
            # create an instance of the equivalent Snowflake type
            column_type = column_type_class()
    else:
        # If the column type is *not* a sub-class of a type for which we have
        # a dialect-specific alternative, we return the generic column type
        column_type = generic_column_type
    return column_type


def _get_hive_column_type(
    generic_column_type: Union[Type[TypeEngine], TypeEngine]
) -> Union[Type[TypeEngine], TypeEngine]:
    """
    This function returns an equivalent of `generic_column_type` which is
    compatible with Hive/Presto
    """
    column_type: Union[Type[TypeEngine], TypeEngine]
    column_type_class: Type[TypeEngine]
    # The column type can be either a class or a class instance, so here
    # we get the *class*
    generic_column_type_class: Type[TypeEngine] = get_column_type_class(
        generic_column_type
    )
    if issubclass(generic_column_type_class, (Object, Array)):
        # Both arrays and objects are represented as strings for Hive/Presto
        column_type_class = String
        if generic_column_type_class is generic_column_type:
            # If the generic column type we received was a class,
            # pass back the equivalent Snowflake type
            column_type = column_type_class
        else:
            # If the generic column type we received was a class instance,
            # create an instance of the equivalent Snowflake type
            column_type = column_type_class(
                *generic_column_type.__reduce__()[-1]
            )
    else:
        # If the column type is *not* a sub-class of a type for which we have
        # a dialect-specific alternative, we return the generic column type
        column_type = generic_column_type
    return column_type


def _get_sqlite_column_type(
    generic_column_type: Union[Type[TypeEngine], TypeEngine]
) -> Union[Type[TypeEngine], TypeEngine]:
    """
    This function returns an equivalent of `generic_column_type` which is
    compatible with SQLite
    """
    column_type: Union[Type[TypeEngine], TypeEngine]
    column_type_class: Type[TypeEngine]
    # The column type can be either a class or a class instance, so here
    # we get the *class*
    generic_column_type_class: Type[TypeEngine] = get_column_type_class(
        generic_column_type
    )
    if issubclass(generic_column_type_class, (Object, Array)):
        # Both arrays and objects are represented as strings for Hive/Presto
        column_type_class = JSON
        if generic_column_type_class is generic_column_type:
            # If the generic column type we received was a class,
            # pass back the equivalent Snowflake type
            column_type = column_type_class
        else:
            # If the generic column type we received was a class instance,
            # create an instance of the equivalent Snowflake type
            column_type = column_type_class()
    else:
        # If the column type is *not* a sub-class of a type for which we have
        # a dialect-specific alternative, we return the generic column type
        column_type = generic_column_type
    return column_type


def _get_postgresql_column_type(
    generic_column_type: Union[Type[TypeEngine], TypeEngine]
) -> Union[Type[TypeEngine], TypeEngine]:
    """
    This function returns an equivalent of `generic_column_type` which is
    compatible with SQLite
    """
    # PostgreSQL can use all the same types as SQLite
    return _get_sqlite_column_type(generic_column_type)


def get_dialect_specific_column_type(
    dialect_name: str, column_type: Union[Type[TypeEngine], TypeEngine]
) -> Union[Type[TypeEngine], TypeEngine]:
    """
    This function returns a column type which is specific to the indicated
    `dialogue_name` (snowflake", "hive", "presto", or "sqlite").
    """
    if dialect_name == "snowflake":
        return _get_snowflake_column_type(column_type)
    elif dialect_name in ("hive", "presto"):
        return _get_hive_column_type(column_type)
    elif dialect_name == "sqlite":
        return _get_sqlite_column_type(column_type)
    elif dialect_name == "postgresql":
        return _get_postgresql_column_type(column_type)
    else:
        raise ValueError(dialect_name)
