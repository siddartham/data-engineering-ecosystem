"""
This module defines a declarative base and common types for all models in this
library
"""

import decimal
import logging
import math
import numbers
import sys
from collections import OrderedDict, deque
from itertools import chain
from types import ModuleType
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
)

from sqlalchemy import Column  # type: ignore
from sqlalchemy import MetaData as _MetaData  # type: ignore
from sqlalchemy import Table, create_engine, event, inspect
from sqlalchemy.engine import CursorResult  # type: ignore
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.engine.mock import MockConnection  # type: ignore
from sqlalchemy.engine.row import Row  # type: ignore
from sqlalchemy.engine.url import URL  # type: ignore
from sqlalchemy.exc import ProgrammingError  # type: ignore
from sqlalchemy.ext import declarative  # type: ignore
from sqlalchemy.orm import Mapper  # type: ignore
from sqlalchemy.orm import (
    declarative_base as _declarative_base,  # type: ignore
)
from sqlalchemy.sql.ddl import CreateSchema  # type: ignore

from .ddl import register_hive_create_table_compiler
from .errors import NotNamedTupleError
from .utilities import (
    get_bind_dialect_name,
    get_bind_schema,
    get_bind_table_names,
    get_bind_view_names,
    get_class_qualified_name,
)
from .utilities import get_class_table_name as get_class_name_table_name
from .utilities import (
    iter_recursive_subclasses,
    lru_cache,
    patch_urllib_parse_uses,
    translate_all_bind_schemas_to,
    update_all_dialects_construct_arguments,
)

# region Dialect-specific imports
update_all_dialects_construct_arguments(Table, **{"*": None})
patch_urllib_parse_uses("s3")
try:
    from . import snowflake  # noqa: F401
except ImportError:
    pass
try:
    from . import postgresql  # noqa: F401
except ImportError:
    pass
try:
    from . import databricks  # noqa: F401
except ImportError:
    pass

_hive: Optional[ModuleType]
try:
    from . import _hive
except ImportError:
    _hive = None

# endregion

__all__: List[str] = [
    "MetaData",
    "Base",
    "declarative_base",
    "as_declarative",
    "get_base_schema_qualified_table_name",
    "iter_base_sorted_subclasses",
    "get_base_table_name_subclass",
    "get_base_table_names_subclasses",
    "get_base_table_schema_name",
    "get_base_table_subclass",
    "get_class_column_names",
    "get_class_dialect_name",
    "get_class_mapper",
    "get_class_primary_key_and_column_names",
    "get_class_primary_key_column_names",
    "get_class_primary_key_indices",
    "get_class_properties_column_names",
    "get_class_property_names",
    "get_class_table_args",
    "get_class_table_name",
    "get_metadata_dialect_name",
    "get_base_schema_names",
]


class MetaData(_MetaData):
    """
    This MetaData class injects dialect-specific pre-bind operations
    """

    tables: Dict[str, Table]
    _tables_tags: Dict[str, Dict[str, str]] = {}

    def __init__(
        self, base: Optional[Type["Base"]] = None, *args: Any, **kwargs: Any
    ) -> None:
        self._bind: Union[Engine, Connection, None] = None
        self.base: Optional[Type["Base"]] = base
        self.bind = kwargs.pop("bind", None)
        super().__init__(*args, **kwargs)

    @property
    def bind(self) -> Union[Engine, Connection]:
        return self._bind

    @bind.setter
    def bind(
        self, bind: Union[str, Union[Engine, Connection, str, URL]]
    ) -> None:
        do_rebind: bool = self._before_bind(bind)
        if do_rebind:
            if isinstance(bind, (str, URL)):
                bind = create_engine(bind)
            self._bind = bind
            self._after_bind()

    def get_dialect_name(
        self, bind: Optional[Union[str, Union[Engine, Connection]]] = None
    ) -> str:
        return get_bind_dialect_name(bind or self.bind)

    def _compare_bind(
        self, bind: Union[str, Union[Engine, Connection]]
    ) -> bool:
        """
        Determine whether an incoming bind is comparable to the existing bind.
        A return value of `False` will cause re-binding to occur.
        """
        if (bind is None) or (bind == self._bind):
            # If the bind argument is `None`,
            # or is the same as the existing bind,
            # leave the existing bind in place
            return True
        elif (
            # If a URL has been passed, just check to see that it does not
            # match the existing connection or engine binding
            isinstance(bind, (URL, str))
            # If the existing bind is empty, always re-bind
            and (self._bind is not None)
            # Always re-bind mock connections
            and not isinstance(bind, MockConnection)
        ):
            engine: Engine
            if isinstance(self._bind, Engine):
                engine = self._bind
            else:
                engine = self._bind.engine
            if isinstance(bind, str):
                return engine.url.render_as_string(hide_password=False) == bind
            else:
                return engine.url == bind
        return False

    def _before_bind(
        self, bind: Union[str, Union[Engine, Connection, str, URL]]
    ) -> bool:
        """
        Perform dialect-specific pre-bind operations, then return `True` if
        we need to re-bind
        """
        # No pre-bind operations needed *for current dialects*.
        # TODO: This will likely be needed for databricks, but if it is *not*
        # used for databricks--remove this method once that dialect is
        # implemented
        return not self._compare_bind(bind)

    def _after_bind(self) -> None:
        """
        Perform dialect-specific after-bind operations
        """
        if self.bind:
            assert self.base is not None
            dialect_name: str = get_bind_dialect_name(self.bind)
            # Schemas should only be used for the Snowflake dialect,
            # so translate all schemas as `None` for other dialects
            if dialect_name != "snowflake":
                translate_all_bind_schemas_to(self.bind.engine, None)
                if self.bind is not self.bind.engine:
                    translate_all_bind_schemas_to(self.bind, None)

            _convert_column_names(self.base, dialect_name=dialect_name)
            _base_apply_table_args(self.base, dialect_name=dialect_name)

            if dialect_name == "databricks":
                self._reflect_table_tags()
                event.listen(
                    Table, "after_parent_attach", self._add_table_tags
                )

    def _add_table_tags(self, table: Table, parent: _MetaData) -> None:
        """
        Updates a reflected table's info with its tags
        """
        table_tags: Dict[str, str] = self._tables_tags.get(table.name, {})
        table.info.update({"tags": table_tags})

    def _reflect_table_tags(self) -> None:
        """
        Loads all table tags for the active connection into a cache to be used
        during table reflection
        """
        dialect_name: str = get_bind_dialect_name(self.bind)
        if dialect_name == "databricks":
            schema: Optional[str] = get_bind_schema(self.bind)
            assert schema
            bind: Union[Engine, Connection] = self.bind
            if isinstance(bind, Engine):
                bind = bind.connect()
            row: Row
            for row in bind.exec_driver_sql(
                (
                    "select table_name, tag_name, tag_value "
                    "from information_schema.table_tags "
                    "where schema_name = %(table_schema)s"
                ),
                {"table_schema": schema},
            ):
                if row.table_name not in self._tables_tags:
                    self._tables_tags[row.table_name] = {}
                self._tables_tags[row.table_name][row.tag_name] = row.tag_value

    def create_views(
        self,
        bind: Union[Engine, Connection] = None,
        checkfirst: bool = True,
    ) -> None:
        """
        Create or re-create all *views*.
        """
        self.create_all(
            bind=bind,
            tables=filter(
                lambda table: table.info.get("is_view", False),
                self.tables.values(),
            ),
            checkfirst=checkfirst,
        )

    def drop_views(
        self, bind: Union[Engine, Connection] = None, checkfirst: bool = True
    ) -> None:
        """
        Drop all *views*.
        """
        table: Table
        self.drop_all(
            bind=bind,
            tables=filter(
                lambda table: table.info.get("is_view", False),
                self.tables.values(),
            ),
            checkfirst=checkfirst,
        )

    def create_all(
        self,
        bind: Union[Engine, Connection, None] = None,
        tables: Optional[Iterable[Table]] = None,
        checkfirst: bool = True,
        hive_location: Optional[str] = None,
        hive_stored_as: Optional[str] = "PARQUET",
        hive_tblproperties: Union[
            Dict[str, str], Sequence[Tuple[str, str]], None
        ] = (
            ("has_encrypted_data", "false"),
            ("classification", "parquet"),
        ),
    ) -> None:
        """
        Create all tables in the database.

        - **bind** (sqlalchemy.engine.interfaces.Connectable):
          An instance of `sqlalchemy.engine.Engine` or
          `sqlalchemy.engine.Connection`.
        - **tables** ([sqlalchemy.Table]) = None:
          An (optional) list of table objects to create. If none are
          provided, all tables will be created.
        - **checkfirst** (bool) = True: If `True`, only tables which don't
          yet exist will be created (otherwise errors will be raised for
          existing tables).
        - **hive_location** (str) = None: If provided, this will be used as
          the root URL/path for Hive tables (specified with the "LOCATION"
          keyword in the "CREATE TABLE" statement), and all "hive_location"
          keys in a mapping's `__table_args__` attribute will be joined with
          this value (if specified as relative paths, or left as the default).
        - **hive_stored_as** (str) = "PARQUET": The default value for the
          "STORED AS" argument for Hive "CREATE TABLE" statements.
        - **hive_tblproperties** ({str: str}) = {"has_encrypted_data":
          "false", "classification": "parquet"}: This argument is used as the
          default value for the "TBLPROPERTIES" argument in Hive "CREATE
          TABLE" statements.
        """
        self.bind = bind
        dialect_name: str = get_bind_dialect_name(self.bind)
        if dialect_name == "hive":
            checkfirst = False
            assert _hive is not None
            if not hive_location:
                raise ValueError(
                    "A value for the `hive_location` parameter is required. "
                    "This should be the base URL under which your external "
                    "hive tables are stored."
                )
            register_hive_create_table_compiler(
                location=hive_location,
                stored_as=hive_stored_as,
                tblproperties=hive_tblproperties,
            )
            getattr(_hive, "listen_and_drop_table_before_create")(self.bind)
        super().create_all(bind=bind, tables=tables, checkfirst=checkfirst)

    def drop_undeclared(self, bind: Union[Engine, Connection] = None) -> None:
        """
        Drop undeclared tables
        """
        assert self.base is not None
        bind = bind or self.bind
        dialect_name: str = get_bind_dialect_name(bind) if bind else ""
        reflected_metadata: _MetaData
        table: Table
        declared_table_schemas_names: Set[Tuple[str, str]] = set()
        schema_name: str
        undeclared: Tuple[Table, ...] = ()
        cls: Type[Base]
        table_name: str
        for cls in iter_recursive_subclasses(self.base):
            table_name = get_class_table_name(
                cls, dialect_name=dialect_name
            ).lower()
            if table_name:
                schema_name = get_class_schema_name(
                    cls, dialect_name=dialect_name
                ).lower()
                key = (schema_name, table_name)
                if key in declared_table_schemas_names:
                    raise ValueError(
                        "The same schema + table name was found for multiple "
                        "classes.\n"
                        f"- Schema Name: {repr(key[0])}\n"
                        f"- Table Name: {repr(key[1])}"
                    )
                declared_table_schemas_names.add(key)
        for schema_name in get_base_schema_names(
            self.base,
            dialect_name=dialect_name,
        ):
            undeclared_table_schemas_names: Set[Tuple[str, str]] = set()
            undeclared_table_names: Set[str] = set()
            reflected_metadata = MetaData(
                base=self.base, schema=schema_name, bind=bind
            )
            name: str
            for name in chain(
                get_bind_table_names(bind, schema=schema_name),
                get_bind_view_names(bind, schema=schema_name),
            ):
                key = (
                    schema_name.lower() if schema_name else "",
                    name.lower(),
                )
                if key not in declared_table_schemas_names:
                    undeclared_table_schemas_names.add(key)
                    undeclared_table_names.add(name)
            reflected_metadata.reflect(
                bind=bind,
                only=undeclared_table_names,
                views=True,
            )
            schema_undeclared: Tuple[Table, ...] = tuple(
                filter(
                    lambda table: (
                        (
                            (
                                str(table.schema).lower()
                                if table.schema
                                else ""
                            ),
                            str(table.name).lower(),
                        )
                        in undeclared_table_schemas_names
                    ),
                    reflected_metadata.tables.values(),
                ),
            )
            assert len(schema_undeclared) == len(
                undeclared_table_schemas_names
            )
            undeclared += schema_undeclared
        if undeclared:
            tables_string: str = ", ".join(
                sorted(
                    map(
                        lambda table: (
                            f"{table.schema}.{table.name}"
                            if table.schema
                            else table.name
                        ),
                        undeclared,
                    )
                )
            )
            logging.info(f"Dropping Tables/Views: {tables_string}")
            deque(map(Table.drop, undeclared), maxlen=0)
        else:
            logging.info("No undeclared tables were found to drop.")

    def drop_all(
        self,
        bind: Union[Engine, Connection] = None,
        tables: Optional[Iterable[Table]] = None,
        checkfirst: bool = True,
    ) -> None:
        self.bind = bind
        super().drop_all(bind=self.bind, tables=tables, checkfirst=checkfirst)

    def reflect(
        self,
        bind: Union[Engine, Connection, None] = None,
        schema: Optional[str] = None,
        views: bool = False,
        only: Optional[Union[Callable, Iterable]] = None,
        extend_existing: bool = False,
        autoload_replace: bool = True,
        resolve_fks: Optional[bool] = True,
        **dialect_kwargs: Any,
    ) -> None:
        self.bind = bind
        super().reflect(
            bind=bind,
            schema=schema,
            views=views,
            only=only,
            extend_existing=extend_existing,
            autoload_replace=autoload_replace,
            resolve_fks=resolve_fks,
            **dialect_kwargs,
        )

    def _create_schemas(self, bind: Union[Engine, Connection, None]) -> None:
        """
        This function creates schemas on table creation (if they don't already
        exist)
        """
        if bind:
            schema_names: Set[str] = set()
            table: Table
            for table in self.tables.values():
                if table.schema and (table.schema not in schema_names):
                    schema_names.add(table.schema)
                    connection: Connection
                    if isinstance(bind, Connection):
                        connection = bind
                    else:
                        connection = bind.connect()
                    try:
                        connection.execute(CreateSchema(table.schema))
                    except ProgrammingError as error:
                        if "exists" not in str(error).lower():
                            raise error


class Base:
    """
    This class is used to construct a declarative base with extended
    functionality, including multi-dialect compatibility: Snowflake, Hive
    and SQLite.
    """

    __table__: Table
    metadata: MetaData

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        This is a dummy initialization method to prevent IDE's from
        erroneously indicating the presence of code issues. This will be
        replaced for base classes created by
        `analytics_orm.declarative.declarative_base`.
        """
        pass

    @property
    def bind(self) -> Union[Engine, Connection]:
        return self.metadata.bind

    @bind.setter
    def bind(
        self, bind: Union[str, Union[Engine, Connection, str, URL]]
    ) -> None:
        self.metadata.bind = bind

    @declarative.declared_attr
    def __tablename__(cls) -> str:
        return get_class_name_table_name(getattr(cls, "__name__"))

    @declarative.declared_attr
    def __table_args__(cls) -> Dict[str, Any]:
        return _get_class_default_table_args(cls)  # type: ignore

    def __iter__(self) -> Iterable[Any]:
        """
        Yield property values
        """
        cls: Any = type(self)
        mapper: Mapper = get_class_mapper(cls)
        for property_name_ in mapper.columns.keys():
            yield getattr(self, property_name_, None)

    @property
    def _items(self) -> Iterable[Tuple[str, Any]]:
        """
        Yield a series of tuples, each consisting of a property name + value
        """
        cls: Any = type(self)
        mapper: Mapper = get_class_mapper(cls)
        for property_name_ in mapper.columns.keys():
            yield property_name_, getattr(self, property_name_)

    def __repr__(self) -> str:
        return "{}(\n{}\n)".format(
            get_class_qualified_name(type(self)),
            ",\n".join(
                f"    {property_name_}={repr(value)}"
                for property_name_, value in self._items
            ),
        )


def get_class_primary_key_indices(cls: Type[Base]) -> Tuple[int, ...]:
    """
    Return a list of indices for the columns representing this table's
    primary keys.
    """
    mapper: Mapper = get_class_mapper(cls)
    primary_key_column_names: Set[str] = set(
        column.name for column in mapper.primary_key
    )
    indices: List[int] = []
    column: Column
    for index, column in enumerate(mapper.columns.values()):
        if column.name in primary_key_column_names:
            indices.append(index)
    return tuple(indices)


def get_class_primary_key_and_column_names(
    cls: Type[Base],
) -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    """
    Return two tuples: the first consisting of primary key column names,
    and the second a list of the remaining (non-key) columns.
    """
    mapper: Mapper = get_class_mapper(cls)
    primary_key_column_names: Tuple[str, ...] = tuple(
        column.name for column in mapper.primary_key
    )
    return (
        primary_key_column_names,
        tuple(
            column.name
            for column in mapper.columns.values()
            if column.name not in primary_key_column_names
        ),
    )


def get_class_primary_key_column_names(cls: Type[Base]) -> Tuple[str, ...]:
    """
    Return a list of primary key column names.
    """
    mapper: Mapper = get_class_mapper(cls)
    return tuple(column.name for column in mapper.primary_key)


@lru_cache()
def get_class_properties_column_names(cls: Type[Base]) -> Dict[str, str]:
    """
    Return a dictionary of the column names for this mapping's table.
    """
    return OrderedDict(
        [
            (property_name_, column.name)
            for property_name_, column in get_class_mapper(cls).columns.items()
        ]
    )


@lru_cache()
def get_class_column_names(cls: Tuple[Type]) -> Tuple[str, ...]:
    """
    Return a `tuple` of the column names for this mapping's table.
    """
    return tuple(
        column.name for column in get_class_mapper(cls).columns.values()
    )


@lru_cache()
def get_class_columns(cls: Tuple[Type]) -> Tuple[Column, ...]:
    return tuple(column for column in get_class_mapper(cls).columns.values())


@lru_cache()
def get_class_property_names(cls: Type[Base]) -> Tuple[str, ...]:
    """
    Return a `tuple` of the property names for this mapping.
    """
    return tuple(get_class_mapper(cls).columns.keys())


def iter_base_sorted_subclasses(base: Type[Base]) -> Iterable[Type["Base"]]:
    """
    This class-method iterates over all sub-classes of a declarative base,
    in a sequence where mappings to tables which are the target of a
    foreign key reference will always precede the table constrained by that
    foreign key.
    """
    subclass: Type["Base"]
    return sorted(
        iter_recursive_subclasses(base),
        key=lambda subclass: base.metadata.sorted_tables.index(
            subclass.__table__
        ),
    )


# For backwards-compatibility
get_base_sorted_subclasses = iter_base_sorted_subclasses


def get_base_table_subclass(base: Type[Base], table: Table) -> Type["Base"]:
    """
    Get the subclass representing this table's mapping.

    Parameters:

    - **table** (sqlalchemy.Table)
    """
    return get_base_table_name_subclass(
        base, _get_table_schema_qualified_name(table)
    )


def get_class_table_name(cls: Type[Base], dialect_name: str = "") -> str:
    """
    Return this mapping class'es table name
    """
    if not dialect_name:
        dialect_name = get_class_dialect_name(cls)
    class_dialect_table_name: str = _get_class_dialect_table_name(
        cls, dialect_name
    )
    return class_dialect_table_name


def get_class_qualified_table_name(
    cls: Type[Base], dialect_name: str = ""
) -> str:
    """
    Return this mapping's schema-qualified table name, if
    it has non-default schema for the current bind, otherwise
    return the naked table name.
    """
    if not dialect_name:
        dialect_name = get_class_dialect_name(cls)
    table_name: str = _get_class_dialect_table_name(cls, dialect_name)
    # Only look for a schema name if the table name is not empty
    if table_name:
        schema: str = _get_class_dialect_schema_name(cls, dialect_name)
        if schema:
            table_name = f"{schema}.{table_name}"
    return table_name


def get_base_table_name_subclass(
    base: Type[Base], table_name: str
) -> Type["Base"]:
    """
    Return a subclass of this declarative base associated with the
    indicated table name.

    Parameters:

    - **table_name** (str)
    """
    table_names_subclasses: Dict[str, Type[Base]] = (
        get_base_table_names_subclasses(base)
    )
    try:
        return table_names_subclasses.get(
            table_name, table_names_subclasses[table_name.rpartition(".")[-1]]
        )
    except KeyError as error:
        # Check to see if we just have a casing mismatch.
        # We use `any` rather than `all` to save computation time,
        # because all tables should have the same casing.
        if table_name.isupper():
            if any(
                map(str.islower, filter(None, table_names_subclasses.keys()))
            ):
                return get_base_table_name_subclass(base, table_name.lower())
        elif table_name.islower():
            if any(
                map(str.isupper, filter(None, table_names_subclasses.keys()))
            ):
                return get_base_table_name_subclass(base, table_name.upper())
        # Raise the error
        error.args = (
            f"{table_name} not in "
            f"{tuple(sorted(table_names_subclasses.keys()))}",
        )
        raise error


def get_base_table_names_subclasses(
    base: Type[Base],
) -> Dict[str, Type["Base"]]:
    """
    Return a dictionary of (schema-qualified, if applicable) table
    names to their corresponding mappings.
    """
    return _get_base_dialect_table_names_subclasses(
        base, get_class_dialect_name(base)
    )


def _get_class_default_table_args(cls: Type[Base]) -> Dict[str, Any]:
    snowflake_schema: str = cls.__module__.split(".")[-1].upper()
    return OrderedDict(
        [
            ("schema", None),
            ("postgresql_schema", None),
            ("sqlite_schema", None),
            ("snowflake_schema", snowflake_schema),
            ("databricks_schema", None),
            ("presto_schema", None),
            ("hive_schema", None),
            ("hive_table_name", cls.__tablename__),
            ("hive_stored_as", "PARQUET"),
            ("hive_location", f"./{cls.__tablename__}/"),
        ]
    )


def _convert_column_names(base: Type[Base], dialect_name: str = "") -> None:
    subclass: Type[Base]
    for subclass in iter_recursive_subclasses(base):
        columns: Tuple[Column, ...] = get_class_columns(subclass)
        if dialect_name == "databricks":
            column: Column
            for column in columns:
                if dialect_name == "databricks":
                    column.name = column.name


def _base_apply_table_args(base: Type[Base], dialect_name: str = "") -> None:
    subclass: Type[Base]
    for subclass in iter_recursive_subclasses(base):
        table_args: Dict[str, Any] = get_class_table_args(subclass)
        dialect_schema: Optional[str] = table_args.get(
            f"{dialect_name}_schema", None
        )
        table_args["schema"] = dialect_schema
        setattr(
            subclass,
            "__table_args__",
            table_args,
        )

        subclass.__table__.schema = dialect_schema
        subclass.__table__.name = get_class_table_name(
            subclass, dialect_name=dialect_name
        )
        subclass.__table__.fullname = get_class_qualified_table_name(
            subclass, dialect_name=dialect_name
        )


@lru_cache()
def get_class_mapper(cls: Type[Base]) -> Mapper:
    """
    This method creates, caches, and returns an instance of
    `sqlalchemy.orm.mapper.Mapper` created from inspecting this class.
    """
    return inspect(cls)


def get_class_table_args(
    cls: Type[Base],
    table_args_update: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    This function returns default table arguments updated with any
    values in `cls.__table__args__`.
    """
    table_args: Dict[str, Any] = _get_class_default_table_args(cls)
    if cls.__table_args__:
        table_args.update(cls.__table_args__)
    if table_args_update:
        table_args.update(table_args_update, **kwargs)
    else:
        table_args.update(**kwargs)
    return table_args


@lru_cache()
def _get_class_dialect_schema_name(cls: Type[Base], dialect_name: str) -> str:
    """
    Given a table name, return the schema name.
    """
    table_args: Dict[str, str] = get_class_table_args(cls)
    for schema_key in chain(
        ((f"{dialect_name}_schema",) if dialect_name else ()), ("schema",)
    ):
        schema: Optional[str] = table_args.get(schema_key, None)
        if schema is not None:
            if dialect_name == "snowflake":
                schema = schema.upper()
            elif dialect_name == "databricks":
                schema = schema.lower()
            return schema
    return ""


def get_class_schema_name(cls: Type[Base], dialect_name: str = "") -> str:
    """
    Given a table name, return the schema name.
    """
    if not dialect_name:
        dialect_name = get_class_dialect_name(cls)
    # The following is a separate function for caching purposes
    return _get_class_dialect_schema_name(cls, dialect_name)


def get_base_table_schema_name(
    base: Type[Base], table_name: str, dialect_name: str = ""
) -> str:
    """
    Given a non-qualified table name, return the schema name.
    """
    if not dialect_name:
        dialect_name = get_class_dialect_name(base)
    table_name = table_name.split(".")[-1]
    if dialect_name == "snowflake":
        table_name = table_name.upper()
    elif dialect_name == "databricks":
        table_name = table_name.lower()
    return _get_base_dialect_table_schemas(base, dialect_name)[table_name]


def get_base_schema_qualified_table_name(
    base: Type[Base], table_name: str, dialect_name: str = ""
) -> str:
    """
    Given a non-qualified table name, return the schema-qualified name.
    """
    if not dialect_name:
        dialect_name = get_class_dialect_name(base)
    if dialect_name == "snowflake":
        table_name = table_name.upper()
    elif dialect_name == "databricks":
        table_name = table_name.lower()
    table_name = table_name.split(".")[-1]
    schema_name: str = get_base_table_schema_name(base, table_name)
    return f"{schema_name}.{table_name}" if schema_name else table_name


def get_base_schema_names(
    base: Type[Base], dialect_name: str = ""
) -> Iterable[str]:
    """
    Yield the name of all schemas having declared sub-classes of`base`
    """
    if not dialect_name:
        dialect_name = get_class_dialect_name(base)
    return _get_base_dialect_schema_names(base, dialect_name)


@lru_cache()
def _get_base_dialect_schema_names(
    base: Type[Base], dialect_name: str
) -> Tuple[str, ...]:
    def get_class_schema_name_(cls: Type[Base]) -> str:
        return get_class_schema_name(cls, dialect_name=dialect_name)

    return tuple(
        sorted(
            set(map(get_class_schema_name_, iter_recursive_subclasses(base)))
        )
    )


@lru_cache()
def _get_base_dialect_table_schemas(
    cls: Type[Base], dialect_name: str = ""
) -> Dict[str, str]:
    if not dialect_name:
        dialect_name = get_class_dialect_name(cls)
    subclass: type
    table_schemas: Dict[str, str] = {}
    for subclass in iter_recursive_subclasses(cls):
        assert issubclass(subclass, Base)
        table_name: str = _get_class_dialect_table_name(
            subclass, dialect_name=dialect_name
        )
        table_schemas[table_name] = get_class_schema_name(
            subclass, dialect_name=dialect_name
        )
    return table_schemas


def _get_table_schema_qualified_name(table: Table) -> str:
    """
    Get the schema-qualified table name for an instance of `sqlalchemy.Table`
    instance
    """
    table_name: str = table.name
    if table.schema:
        table_name = f"{table.schema}.{table.name}"
    return table_name


@lru_cache()
def _get_base_dialect_table_names_subclasses(
    base: Type[Base], dialect: str
) -> Dict[str, Type[Base]]:
    """
    Return a dictionary of (schema-qualified) table
    names to their corresponding mappings.
    """
    table_names_mappings: Dict[str, Type[Base]] = OrderedDict()
    for subclass in iter_recursive_subclasses(base):
        table_names_mappings[
            _get_class_dialect_table_name(subclass, dialect)
        ] = subclass
    return table_names_mappings


def get_class_dialect_name(cls: Type[Base]) -> str:
    dialect_name: str = "default"
    if cls.metadata:
        return get_metadata_dialect_name(cls.metadata)
    return dialect_name


def get_metadata_dialect_name(metadata: MetaData) -> str:
    dialect_name: str = "default"
    if metadata.bind:
        return get_bind_dialect_name(metadata.bind)
    return dialect_name


@lru_cache()
def _get_class_dialect_table_name(cls: Type[Base], dialect_name: str) -> str:
    table_name: str = getattr(cls, "__tablename__")
    table_args: Dict[str, str] = get_class_table_args(cls)
    dialect_table_name_key: str = f"{dialect_name}_table_name"
    if dialect_table_name_key in table_args:
        table_name = table_args[dialect_table_name_key]
    if dialect_name == "snowflake":
        table_name = table_name.upper()
    elif dialect_name == "databricks":
        table_name = table_name.lower()
    return table_name


def _replace_nan_with_none(value: Any) -> Any:
    """
    Some SQLAlchemy dialects don't handle `NaN` values—so we need to replace
    them with `None`.
    """
    if isinstance(value, numbers.Number):
        if isinstance(value, (numbers.Real, decimal.Decimal)):
            return None if math.isnan(value) else value
        else:
            return value
    else:
        return value


def _get_class_kwargs_from_namedtuple(
    cls: Base, namedtuple_instance: Union[tuple, Row]
) -> Dict[str, Any]:
    assert isinstance(namedtuple_instance, (tuple, Row))
    as_dict: Optional[Callable] = getattr(
        namedtuple_instance,
        "_asdict",  # namedtuple
        getattr(namedtuple_instance, "asDict", None),  # pyspark.Row
    )
    if (as_dict is None) or (not callable(as_dict)):
        raise NotNamedTupleError(repr(namedtuple_instance))
    unmapped_keys: Set[str] = set()
    kwargs: Dict[str, Any] = as_dict()
    for key in kwargs.keys():
        if not hasattr(cls, key):
            unmapped_keys.add(key)
    # If no matching property names are found for any keys--check to see
    # if they are column names
    if unmapped_keys:
        mapping_class: type = type(cls)
        mapper: Mapper = inspect(mapping_class)
        property_name_: str
        column: Column
        for property_name_, column in mapper.columns.items():
            if column.name in unmapped_keys:
                kwargs[property_name_] = kwargs.pop(column.name)
                unmapped_keys.remove(column.name)
        if unmapped_keys:
            raise ValueError(
                "Not all `namedtuple` properties could be mapped: "
                f"{repr(unmapped_keys)}"
            )
    return kwargs


def _get_kwargs_from_args(cls: Base, args: Tuple[Any, ...]) -> Dict[str, Any]:
    mapping_class: type = type(cls)
    mapper: Mapper = inspect(mapping_class)
    property_name_: str
    column: Column
    property_name_column: Tuple[str, Column]
    kwargs: Dict[str, Any] = {}
    args_length: int = len(args)
    for index, property_name_column in enumerate(mapper.columns.items()):
        property_name_, column = property_name_column
        if index < args_length:
            # Set values according to column ordinal
            kwargs[property_name_] = args[index]
        else:
            # If the number of arguments is fewer than the number of columns--
            # the remaining columns are set to `None` (null)
            kwargs[property_name_] = None
    return kwargs


def _get_calling_module_name(depth: int = 1) -> str:
    """
    This function returns the name of the module from which the function
    which invokes this function was called.

    Parameters:

    - depth (int): This defaults to `1`, indicating we want to return the name
      of the module wherein `calling_module_name` is being called. If set to
      `2`, it would instead indicate the module

    >>> print(_get_calling_module_name())
    analytics_orm.base

    >>> print(_get_calling_module_name(2))
    doctest
    """
    name: str
    try:
        name = getattr(sys, "_getframe")(depth).f_globals.get(
            "__name__", "__main__"
        )
    except (AttributeError, ValueError):
        name = "__main__"
    return name


def declarative_base(
    bind: Union[Engine, Connection, None] = None,
    cls: Union[Type[object], Tuple[Type[object], ...], None] = None,
    name: str = "Base",
) -> Any:
    """
    This function wraps `sqlalchemy.ext.declarative.declarative_base`
    """
    if cls is not None:
        if not isinstance(cls, tuple):
            cls = (cls,)
        cls += (Base,)
    base: Any = _declarative_base(
        cls=Base,
        name=name,
        metadata=MetaData(
            naming_convention={
                "ix": "IX_%(column_0_label)s",
                "uq": "UQ_%(table_name)s_%(column_0_N_name)s",
                "ck": "CK_%(table_name)s_%(constraint_name)s",
                "fk": (
                    "FK_%(table_name)s_"
                    "%(column_0_N_name)s_"
                    "%(referred_table_name)s"
                ),
                "pk": "PK_%(table_name)s",
            }
        ),
    )
    base.metadata.bind = bind
    base.metadata.base = base
    # This must be set explicitly in order to be compatible with
    # `pyspark.cloudpickle`
    base.__module__ = _get_calling_module_name(2)
    _default_declarative_constructor: Callable = getattr(base, "__init__")

    def _base_constructor(self: Base, *args: Any, **kwargs: Any) -> None:
        """
        This function serves as a constructor which can accept column values as
        non-keyword arguments or as a single `namedtuple()` argument.
        """
        if args:
            if len(args) == 1 and isinstance(args[0], (tuple, Row)):
                try:
                    kwargs = _get_class_kwargs_from_namedtuple(self, args[0])
                except NotNamedTupleError:
                    kwargs = _get_kwargs_from_args(self, args)
            else:
                kwargs = _get_kwargs_from_args(self, args)
        bind: Union[Engine, Connection, URL, str, None] = kwargs.pop(
            "bind", None
        )
        _default_declarative_constructor(
            self,
            **{
                key: _replace_nan_with_none(value)
                for key, value in kwargs.items()
            },
        )
        if bind:
            self.bind = bind

    _base_constructor.__name__ = "__init__"
    setattr(base, "__init__", _base_constructor)
    return base


def as_declarative(**kwargs: Any) -> Callable[..., Type[Base]]:
    """
    This function is a class decorator for
    `analytics_orm.declarative.declarative_base` which provides a
    syntactical shortcut to the `cls` argument sent to
    `analytics_orm.declarative.declarative_base`, allowing the
    base class to be converted in-place to a "declarative" base. For example:

    ```
    from sqlalchemy import Integer
    from analytics_orm.declarative import as_declarative

    @as_declarative()
    class Base:

        @declared_attr
        def __tablename__(cls):
            return cls.__name__.lower()


    class MyMappedClass(Base):

        id = Column(Integer, primary_key=True)
    ```

    All keyword arguments passed to
    `analytics_orm.declarative.as_declarative` are passed along to
    `analytics_orm.declarative.declarative_base`.
    """

    def decorate(cls: type) -> Type[Base]:
        kwargs["cls"] = cls
        kwargs["name"] = cls.__name__
        return declarative_base(**kwargs)

    return decorate
