from collections import deque
from datetime import datetime
from itertools import starmap
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

from sqlalchemy import types  # type: ignore
from sqlalchemy.engine.base import Connection  # type: ignore
from sqlalchemy.engine.base import Engine  # type: ignore
from sqlalchemy.engine.create import create_engine  # type: ignore
from sqlalchemy.engine.url import URL, make_url  # type: ignore
from sqlalchemy.orm import aliased  # type: ignore
from sqlalchemy.orm.mapper import Mapper  # type: ignore
from sqlalchemy.sql import Alias  # type: ignore
from sqlalchemy.sql.expression import (  # type: ignore
    BinaryExpression,
    and_,
    select,
)
from sqlalchemy.sql.functions import count  # type: ignore
from sqlalchemy.sql.schema import (  # type: ignore
    Column,
    ForeignKey,
    ForeignKeyConstraint,
    Table,
)
from sqlalchemy.sql.selectable import Select  # type: ignore
from sqlalchemy.sql.sqltypes import (  # type: ignore
    JSON,
    DateTime,
    Enum,
    Integer,
    NullType,
    Numeric,
    String,
)
from sqlalchemy.sql.type_api import TypeEngine  # type: ignore

from .declarative import (
    Base,
    MetaData,
    get_base_schema_names,
    get_bind_dialect_name,
    get_class_mapper,
    get_class_schema_name,
    get_class_table_name,
)
from .errors import (
    ColumnNameError,
    ColumnNotReflectedError,
    ColumnsNotDeclaredError,
    ColumnTypeError,
    ColumnValidationError,
    ForeignKeyMissingReferenceError,
    PrimaryKeyNotUniqueError,
    TableNotDeclaredError,
    TableNotReflectedError,
    ValidationError,
    ViewCacheError,
)
from .types import Array, Object
from .utilities import (
    get_bind_schema,
    is_view,
    iter_recursive_subclasses,
    lru_cache,
)

SNOWFLAKE_CACHED_VIEW_RESPONSE_ERROR_THRESHOLD_SECONDS: float = 30.0


def _validate_column_compatibility(
    declared_column: Column,
    reflected_column: Column,
) -> Optional[ColumnTypeError]:
    declared_column_type_class: Type[TypeEngine] = type(declared_column.type)
    reflected_column_type_class: Type[TypeEngine] = type(reflected_column.type)
    # The Databricks dialect uses custom types as part of its dialect
    # So we need to get the implemented type to enable the below comparisons
    if issubclass(reflected_column_type_class, types.TypeDecorator):
        reflected_column_type_class = reflected_column_type_class.impl

    if (
        (
            issubclass(declared_column_type_class, String)
            and issubclass(reflected_column_type_class, String)
            and declared_column.type.length
            and reflected_column.type.length
            and declared_column.type.length != reflected_column.type.length
        )
        or (
            issubclass(declared_column_type_class, Numeric)
            and issubclass(reflected_column_type_class, Numeric)
            and (
                (
                    (declared_column.type.precision is not None)
                    and (reflected_column.type.precision is not None)
                    and (
                        declared_column.type.precision
                        > reflected_column.type.precision
                    )
                )
                or (
                    (declared_column.type.scale is not None)
                    and (reflected_column.type.scale is not None)
                    and (
                        declared_column.type.scale
                        > reflected_column.type.scale
                    )
                )
            )
        )
        or not (
            issubclass(reflected_column_type_class, declared_column_type_class)
            or (
                issubclass(reflected_column_type_class, NullType)
                and declared_column.nullable
            )
            or (
                issubclass(declared_column_type_class, Integer)
                and issubclass(reflected_column_type_class, Numeric)
                and reflected_column.type.scale == 0
            )
            or (
                issubclass(declared_column_type_class, DateTime)
                and (
                    "TIMESTAMP"
                    in getattr(
                        reflected_column_type_class, "__visit_name__"
                    ).upper()
                )
            )
            or (
                issubclass(reflected_column_type_class, String)
                and issubclass(declared_column_type_class, Enum)
            )
            or (
                issubclass(reflected_column_type_class, (JSON, String))
                and issubclass(declared_column_type_class, (Object, Array))
            )
            or (
                getattr(reflected_column_type_class, "__visit_name__", "")
                == "ARRAY"
                and issubclass(declared_column_type_class, Array)
            )
            or (
                getattr(reflected_column_type_class, "__visit_name__", "")
                == "OBJECT"
                and issubclass(declared_column_type_class, Object)
            )
        )
    ):
        return ColumnTypeError(
            schema=(
                declared_column.table.schema
                if declared_column.table is not None
                else None
            ),
            table_name=(
                declared_column.table.name
                if declared_column.table is not None
                else ""
            ),
            column_name=declared_column.name or "{column}",
            declared_type=declared_column.type,
            reflected_type=reflected_column.type,
        )
    return None


def are_column_types_compatible(
    declared_column_type: TypeEngine,
    reflected_column_type: TypeEngine,
) -> bool:
    return (
        _validate_column_compatibility(
            Column(declared_column_type), Column(reflected_column_type)
        )
        is None
    )


def _get_ignore_foreign_key_constraint_function(
    ignore_foreign_keys: Union[
        Iterable[str], Callable[[ForeignKeyConstraint], bool], None
    ]
) -> Callable[[ForeignKeyConstraint], bool]:
    ignore_foreign_key_constraint: Callable[[ForeignKeyConstraint], bool]
    if ignore_foreign_keys is None:

        def ignore_foreign_key_constraint(
            foreign_key_constraint: ForeignKeyConstraint,
        ) -> bool:
            return False

    elif callable(ignore_foreign_keys):
        ignore_foreign_key_constraint = ignore_foreign_keys
    else:
        if isinstance(ignore_foreign_keys, str):
            ignore_foreign_keys = (ignore_foreign_keys,)
        if "*" in ignore_foreign_keys:

            def ignore_foreign_key_constraint(
                foreign_key_constraint: ForeignKeyConstraint,
            ) -> bool:
                return True

        else:

            def ignore_foreign_key_constraint(
                foreign_key_constraint: ForeignKeyConstraint,
            ) -> bool:
                return (
                    foreign_key_constraint.name  # type: ignore
                    in ignore_foreign_keys
                )

    return ignore_foreign_key_constraint


def _get_exclude_from_cache_validation_function(
    exclude_from_cache_validation: Union[
        Iterable[str], Callable[[Table], bool], None
    ]
) -> Callable[[Table], bool]:
    exclude_from_cache_validation_: Callable[[Table], bool]
    if exclude_from_cache_validation is None:

        def exclude_from_cache_validation_(
            table: Table,
        ) -> bool:
            return False

    elif callable(exclude_from_cache_validation):
        exclude_from_cache_validation_ = exclude_from_cache_validation
    else:
        if isinstance(exclude_from_cache_validation, str):
            exclude_from_cache_validation = (exclude_from_cache_validation,)
        if "*" in exclude_from_cache_validation:

            def exclude_from_cache_validation_(
                table: Table,
            ) -> bool:
                return True

        else:

            def exclude_from_cache_validation_(
                table: Table,
            ) -> bool:
                return (
                    table.name in exclude_from_cache_validation  # type: ignore
                )

    return exclude_from_cache_validation_


class _Validator:
    """
    This class encapsulates the logic needed to validate a declarative base
    against a `bind` (an engine or connection object).
    """

    def __init__(
        self,
        base: Type[Base],
        bind: Union[Engine, Connection, URL, str, None] = None,
        ignore_foreign_keys: Union[
            Iterable[str], Callable[[ForeignKeyConstraint], bool], None
        ] = None,
        exclude_from_cache_validation: Union[
            Iterable[str], Callable[[Table], bool], None
        ] = None,
    ) -> None:
        if bind is None:
            bind = base.metadata.bind
        else:
            if isinstance(bind, str):
                bind = make_url(bind)
            if isinstance(bind, URL):
                bind = create_engine(bind)
            base.metadata.bind = bind
        assert (
            bind
        ), "A bind is required in order to validate a declarative base"
        self.base: Type[Base] = base
        if isinstance(bind, Engine):
            bind = bind.connect()
        self.bind: Connection = bind
        self.dialect_name: str = get_bind_dialect_name(bind)
        # Initialize Ignored FKs
        self.ignore_foreign_key_constraint: Callable[
            [ForeignKeyConstraint], bool
        ] = _get_ignore_foreign_key_constraint_function(ignore_foreign_keys)
        # Initialize Ignored View Cache Validation
        self.exclude_from_cache_validation: Callable[[Table], bool] = (
            _get_exclude_from_cache_validation_function(
                exclude_from_cache_validation
            )
        )

    @property
    @lru_cache()
    def schema(self) -> Optional[str]:
        return get_bind_schema(self.bind)

    def __reduce__(
        self,
    ) -> Tuple[
        Callable[
            [Type[Base], Union[Engine, Connection, URL, str, None]],
            "_Validator",
        ],
        Tuple[Type[Base], Union[Engine, Connection, URL, str, None]],
    ]:
        return type(self), (self.base, self.bind.engine.url)

    @lru_cache()
    def reflect_schema_metadata(
        self, schema: Optional[str], only: Tuple[str, ...] = ()
    ) -> MetaData:
        schema = schema or self.schema
        metadata: MetaData = MetaData(
            base=self.base, bind=self.bind, schema=schema
        )
        kwargs: Dict[str, Any] = {}
        if only:
            kwargs.update(only=only)
        if self.dialect_name.startswith("sqlite"):
            kwargs.update(sqlite_include_auto_indexes=False)
        metadata.reflect(
            bind=self.bind,
            views=True,
            **kwargs,
        )
        return metadata

    @lru_cache()
    def reflect_schema_table(
        self, schema: Optional[str], table_name: str
    ) -> Table:
        schema = schema or self.schema
        metadata: MetaData = (
            # TODO: Optimize databricks metadata reflection
            self.reflect_schema_metadata(schema, only=(table_name,))
            if self.dialect_name == "databricks"
            else self.reflect_schema_metadata(schema)
        )
        table: Table = metadata.tables.get(
            table_name,
            (
                metadata.tables.get(f"{schema}.{table_name}", None)
                if schema
                else None
            ),
        )
        if table is None:
            raise TableNotReflectedError(schema, table_name)
        return table

    def include_class(self, cls: Type[Base]) -> bool:
        """
        Return `True` if `cls` is applicable to the bind dialect
        `self.dialect_name`, otherwise return `False`
        """
        return bool(get_class_table_name(cls, self.dialect_name))

    def validate_property_column_name(
        self, property_name: str, column: Column
    ) -> Optional[ColumnNameError]:
        """
        Ensure naming convention conformity for `property_name` and
        `column.name`.

        Parameters:

        - property_name (str)
        - column (sqlalchemy.sql.schema.Column)
        """
        # Verify the property name is simply a lowercase variation of the
        # column name
        if column.name.lower() != property_name:
            return ColumnNameError(
                column.table.schema or self.schema,
                column.table.name,
                column.name,
                property_name,
            )
        return None

    def validate_column(
        self, column: Column, table: Optional[Table] = None
    ) -> Union[ColumnValidationError, TableNotReflectedError, None]:
        """
        Validate `column` against `self.bind` and ensure
        naming convention conformity for `property_name` and `column.name`,
        and return the column name.

        Parameters:

        - column (sqlalchemy.sql.schema.Column)
        """
        # Get the reflected table metadata
        if table is None:
            try:
                table = self.reflect_schema_table(
                    column.table.schema or self.schema, column.table.name
                )
            except TableNotReflectedError as error:
                return error
        # Verify that the class defined column metadata matches the
        # reflected metadata for that column
        reflected_column: Optional[Column] = table.columns.get(
            column.name, None
        )
        if reflected_column is None:
            return ColumnNotReflectedError(
                column.table.schema or self.schema,
                column.table.name,
                column.name,
            )
        return _validate_column_compatibility(column, reflected_column)

    def validate_table_primary_key(
        self, table: Table
    ) -> Iterable[PrimaryKeyNotUniqueError]:
        """
        Verify that a table's primary key is unique
        """
        select_key_count: Select = (
            select(count().label("NUMBER_OF_OCCURENCES"), *table.primary_key)
            .group_by(*table.primary_key)
            .alias()
        )
        select_repeated_key_count: Select = select(select_key_count).where(
            select_key_count.c["NUMBER_OF_OCCURENCES"] > 1
        )
        if self.bind.execute(select_repeated_key_count).fetchone():
            yield PrimaryKeyNotUniqueError(
                table.schema or self.schema,
                table.name,
                message=select_repeated_key_count.compile(
                    compile_kwargs={"literal_binds": True}
                ),
            )

    def validate_foreign_key_constraint(
        self, foreign_key_constraint: ForeignKeyConstraint
    ) -> Optional[ForeignKeyMissingReferenceError]:
        if self.ignore_foreign_key_constraint(foreign_key_constraint):
            print(
                f"Ignoring foreign key: {foreign_key_constraint.name}"
                if foreign_key_constraint.name
                else "Ignoring un-named foreign key"
            )
            return None
        print(
            f"Validating foreign key: {foreign_key_constraint.name}"
            if foreign_key_constraint.name
            else "Validating un-named foreign key"
        )
        column: Column
        foreign_key: ForeignKey
        where_and_conditions: List[BinaryExpression] = []
        join_and_conditions: List[BinaryExpression] = []

        table_alias: Alias = aliased(foreign_key_constraint.table)
        referred_table_alias: Alias = aliased(
            foreign_key_constraint.referred_table
        )

        constraint_columns: List[Column] = []
        unbound_column: Column
        unbound_foreign_key_column: Column
        for column, foreign_key in zip(
            foreign_key_constraint.columns, foreign_key_constraint.elements
        ):
            unbound_column = Column(name=column.name)
            unbound_column.table = table_alias
            unbound_foreign_key_column = Column(name=foreign_key.column.name)
            unbound_foreign_key_column.table = referred_table_alias

            join_and_conditions.append(
                unbound_column == unbound_foreign_key_column
            )
            where_and_conditions += [
                unbound_column != None,  # noqa
                unbound_foreign_key_column == None,  # noqa
            ]
            constraint_columns.append(unbound_column)
        select_missing_references: Select = (
            select(*constraint_columns)
            .select_from(
                table_alias.outerjoin(
                    referred_table_alias,
                    and_(*join_and_conditions),
                )
            )
            .where(and_(*where_and_conditions))
        )
        if self.bind.execute(select_missing_references).fetchone():
            return ForeignKeyMissingReferenceError(
                foreign_key_constraint.name,
                select_missing_references.compile(
                    compile_kwargs={"literal_binds": True}
                ),
            )
        return None

    def validate_table_foreign_keys(
        self, table: Table
    ) -> Iterable[ForeignKeyMissingReferenceError]:
        """
        Verify that a table's foreign key relationships are intact
        """
        yield from filter(
            None,
            map(
                self.validate_foreign_key_constraint,
                table.foreign_key_constraints,
            ),
        )

    def validate_view_cache(self, cls: Type[Base]) -> Iterable[ViewCacheError]:
        if (
            self.dialect_name == "snowflake"
            and is_view(cls.__table__, self.bind)
            and not self.exclude_from_cache_validation(cls.__table__)
        ):
            view_name: str = get_class_table_name(cls)
            select_statement: str = str(
                select(cls)
                .limit(10)
                .compile(compile_kwargs={"literal_binds": True})
            )
            connection: Connection = self.bind.connect()
            print(f"Validating query cache for {view_name}")
            # Execute once to generate the cache, if needed
            deque(connection.exec_driver_sql(select_statement), maxlen=0)
            # Execute once again (this time it should be cached)
            start: datetime = datetime.now()
            deque(connection.exec_driver_sql(select_statement), maxlen=0)
            cached_response_time_seconds: float = (
                datetime.now() - start
            ).total_seconds()
            if (
                cached_response_time_seconds
                > SNOWFLAKE_CACHED_VIEW_RESPONSE_ERROR_THRESHOLD_SECONDS
            ):
                yield ViewCacheError(
                    schema=get_class_schema_name(cls, self.dialect_name)
                    or self.schema,
                    view_name=view_name,
                    response_time_seconds=cached_response_time_seconds,
                    threshold_seconds=(
                        SNOWFLAKE_CACHED_VIEW_RESPONSE_ERROR_THRESHOLD_SECONDS
                    ),
                )

    def validate_class(self, cls: Type[Base]) -> Iterable[ValidationError]:
        """
        Validate a mapping class (`cls`) against `self.bind`.

        Parameters:

        - cls (analytics_orm.declarative.Base)
        - bind (
            sqlalchemy.engine.base.Engine
            | sqlalchemy.engine.base.Connection
        )
        """
        print(
            "Validating declared property/column names: "
            f"{cls.__module__}.{cls.__name__}"
        )
        mapper: Mapper = get_class_mapper(cls)
        yield from filter(
            None,
            starmap(
                self.validate_property_column_name, mapper.columns.items()
            ),
        )
        # If the class is not applicable to the dialect of the bind,
        # no further validation should be performed
        if self.include_class(cls):
            print(
                "Validating declared table metadata against reflected table "
                f"metadata: {cls.__module__}.{cls.__name__}"
            )
            declared_column_names: Set[str] = set()
            schema: str = (
                get_class_schema_name(cls, self.dialect_name) or self.schema
            )
            table_name: str = get_class_table_name(cls, self.dialect_name)
            reflected_table: Table = self.reflect_schema_table(
                schema, table_name
            )

            def validate_column(
                column: Column,
            ) -> Union[ColumnValidationError, TableNotReflectedError, None]:
                assert column.name and column.table.name
                error: Union[
                    ColumnValidationError, TableNotReflectedError, None
                ] = self.validate_column(column, reflected_table)
                if error is None:
                    declared_column_names.add(column.name)
                return error

            yield from filter(
                None, map(validate_column, mapper.columns.values())
            )
            # Verify that all reflected columns are declared in the mapping
            # class

            column: Column
            reflected_column_names: Set[str] = set(
                map(lambda column: column.name, reflected_table.columns)
            )
            undeclared_column_names: Set[str] = (
                reflected_column_names - declared_column_names
            )
            if undeclared_column_names:
                yield ColumnsNotDeclaredError(
                    schema or self.schema,
                    table_name,
                    tuple(sorted(undeclared_column_names)),
                )
            # Verify Primary Keys are Unique
            yield from self.validate_table_primary_key(cls.__table__)
            # Validate Foreign Key Relationships
            yield from self.validate_table_foreign_keys(cls.__table__)
            # Validate Snowflake Persistent Query Results
            yield from self.validate_view_cache(cls)

    def iter_declared_schemas_table_names(self) -> Iterable[Tuple[str, str]]:
        cls: Type[Base]
        for cls in iter_recursive_subclasses(self.base):
            yield get_class_schema_name(
                cls, self.dialect_name
            ) or self.schema, get_class_table_name(cls, self.dialect_name)

    def iter_reflected_schemas_table_names(self) -> Iterable[Tuple[str, str]]:
        schema: str
        for schema in get_base_schema_names(self.base, self.dialect_name):
            table: Table
            for table in self.reflect_schema_metadata(
                schema or self.schema
            ).tables.values():
                yield table.schema or schema or self.schema, table.name

    def validate(self, only: Sequence[str] = ()) -> Iterable[ValidationError]:
        """
        Perform all validations
        """
        # Verify that all reflected tables and views are declared
        schema: str
        table_name: str
        declared_schema_table_names: Set[Tuple[str, str]] = set(
            self.iter_declared_schemas_table_names()
        )
        message: str = "Declared tables: {}".format(
            ", ".join(
                f"{schema}.{table_name}"
                for schema, table_name in sorted(declared_schema_table_names)
            )
        )
        for schema, table_name in (
            set(self.iter_reflected_schemas_table_names())
            - declared_schema_table_names
        ):
            yield TableNotDeclaredError(
                schema,
                table_name,
                message,
            )
        # Validate each declared mapping class
        subclasses: Iterable[Type[Base]] = iter_recursive_subclasses(self.base)
        if only:
            if isinstance(only, str):
                only = (only,)
            # Limit validation to specified tables
            cls: Type[Base]
            subclasses = filter(
                lambda cls: (
                    get_class_table_name(cls, self.dialect_name) in only
                ),
                subclasses,
            )
        errors: Iterable[ValidationError]
        for errors in map(
            self.validate_class,
            subclasses,
        ):
            yield from errors


def validate(
    base: Type[Base],
    bind: Union[Engine, Connection, None] = None,
    only: Sequence[str] = (),
    ignore_foreign_keys: Union[
        Iterable[str], Callable[[ForeignKeyConstraint], bool], None
    ] = None,
    exclude_from_cache_validation: Union[
        Iterable[str], Callable[[Table], bool], None
    ] = None,
    raise_exceptions: bool = True,
) -> Iterable[ValidationError]:
    """
    Validate the specified `bind` against sub-classes of the
    declarative `base`. If no `bind` is provided, one will be inferred from
    `base`, if possible.

    Parameters:

    - base (analytics_orm.declarative.Base)
    - bind (
        sqlalchemy.engine.base.Engine
        | sqlalchemy.engine.base.Connection
        | None
      )
    - only ([str]) = (): One or more table names
    - ignore_foreign_key_constraints ([str]): Name(s) of foreign keys
      to ignore, or a function accepting a `sqlalchemy.ForeignKeyConstraint`
      and returning a `bool`.
    - exclude_from_cache_validation ([str]): Name(s) of views to exclude
      from persisted query result (cache) validations (applied to Snowflake
      Only)
    """
    errors: Iterable[ValidationError] = _Validator(
        base=base,
        bind=bind,
        ignore_foreign_keys=ignore_foreign_keys,
        exclude_from_cache_validation=exclude_from_cache_validation,
    ).validate(only=only)
    if raise_exceptions:
        error: ValidationError
        for error in errors:
            raise error
    return errors
