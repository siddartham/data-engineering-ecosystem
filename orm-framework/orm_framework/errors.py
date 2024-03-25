import sys
from itertools import starmap
from traceback import format_exception
from typing import Any, Callable, List, Optional, Sequence, Tuple, Union

from sqlalchemy.sql.type_api import TypeEngine  # type: ignore


def get_exception_text() -> str:
    """
    When called within an exception, this function returns a text
    representation of the error matching what is found in
    `traceback.print_exception`, but is returned as a string value rather than
    printing.
    """
    return "".join(format_exception(*sys.exc_info()))


def append_exception_text(error: Exception, message: str) -> None:
    """
    Cause `message` to be appended to an error's exception text.
    """
    last_attribute_name: str
    repr_last_attribute_value: str
    for last_attribute_name in ("strerror", "msg"):
        last_attribute_value = getattr(error, last_attribute_name, "")
        if last_attribute_value:
            setattr(
                error, last_attribute_name, f"{last_attribute_value}{message}"
            )
            break
    if not last_attribute_value:
        index: int
        arg: Any
        reversed_args: List[Any] = list(reversed(error.args)) or [""]
        for index, value in enumerate(reversed_args):
            if isinstance(value, str):
                reversed_args[index] = f"{value}{message}"
                break
        error.args = tuple(reversed(reversed_args))


class NotNamedTupleError(TypeError):

    pass


class ValidationError(Exception):
    def __init__(self) -> None:
        super().__init__(repr(self))

    def __reduce__(self) -> Tuple[Callable[..., "ValidationError"], Tuple]:
        return (type(self), ())


class ForeignKeyMissingReferenceError(ValidationError):
    def __init__(self, name: str = "", message: str = "") -> None:
        self.name: str = name
        self.message: str = message
        super().__init__()

    def __reduce__(
        self,
    ) -> Tuple[Callable[..., "ForeignKeyMissingReferenceError"], Tuple]:
        return (type(self), (self.name, self.message))

    def __repr__(self) -> str:
        message: str
        if self.message:
            message = f"\n{self.message}"
        else:
            message = ""
        return f"Foreign key has missing references: {self.name}{message}"


class TableValidationError(ValidationError):
    def __init__(
        self,
        schema: Optional[str] = None,
        table_name: Sequence[str] = "",
        message: str = "",
    ) -> None:
        self.schema: Optional[str] = schema
        self.table_name: Sequence[str] = table_name
        self.message: str = message
        super().__init__()

    def __reduce__(
        self,
    ) -> Tuple[Callable[..., "TableValidationError"], Tuple]:
        return (type(self), (self.schema, self.table_name, self.message))

    def _repr(self, message: str) -> str:
        def get_qualified_table_name(table_name: str) -> str:
            if self.schema:
                return f"{self.schema}.{table_name}"
            else:
                return table_name

        table_name_message: str
        if isinstance(self.table_name, str):
            table_name_message = get_qualified_table_name(self.table_name)
        else:
            table_name_message = ", ".join(
                map(get_qualified_table_name, self.table_name)
            )
        message = f"{message}: {table_name_message}"
        if self.message:
            message = f"{message}\n{self.message}"
        return message

    def __repr__(self) -> str:
        return self._repr("Table validation error")


class TableNotReflectedError(TableValidationError):
    def __repr__(self) -> str:
        s: str = "" if isinstance(self.table_name, str) else "s"
        return self._repr(f"Table{s} not found in reflected metadata")


class TableNotDeclaredError(TableValidationError):
    def __repr__(self) -> str:
        s: str = "" if isinstance(self.table_name, str) else "s"
        return self._repr(f"Reflected table{s} not declared")


class PrimaryKeyNotUniqueError(TableValidationError):
    def __repr__(self) -> str:
        return self._repr("Primary key is not unique")


class ViewValidationError(TableValidationError):
    def __init__(
        self,
        schema: Optional[str] = None,
        view_name: Sequence[str] = (),
        message: str = "",
    ) -> None:
        super().__init__(schema=schema, table_name=view_name, message=message)

    def __repr__(self) -> str:
        return self._repr("View validation error")


class ViewCacheError(ViewValidationError):
    def __init__(
        self,
        schema: Optional[str] = None,
        view_name: Sequence[str] = (),
        response_time_seconds: float = 0.0,
        threshold_seconds: float = 0.0,
        message: str = "",
    ) -> None:
        assert response_time_seconds > threshold_seconds, (
            "Response time must be greater than threshold: "
            f"{threshold_seconds} <= {response_time_seconds}"
        )
        if message:
            message = f"{message}\n"
        message = (
            f"{message}"
            f"Response time: {response_time_seconds} seconds\n"
            f"Error threshold: {threshold_seconds} seconds"
        )
        self._args: Tuple[Optional[str], Sequence[str], float, float, str] = (
            schema,
            view_name,
            response_time_seconds,
            threshold_seconds,
            message,
        )
        super().__init__(schema=schema, view_name=view_name, message=message)

    def __reduce__(self) -> Tuple[Callable[..., "ViewCacheError"], Tuple]:
        return (type(self), self._args)

    def __repr__(self) -> str:
        return self._repr("View cache validation error")


class TablesValidationError(ValidationError):
    def __init__(
        self,
        schemas_table_names: Union[
            Sequence[str], Sequence[Tuple[Optional[str], str]]
        ],
    ) -> None:
        if isinstance(schemas_table_names, str):
            schemas_table_names = ((None, schemas_table_names),)
        elif schemas_table_names and isinstance(schemas_table_names[0], str):
            table_name: str
            schemas_table_names = tuple(  # type: ignore
                map(
                    lambda table_name: (None, table_name),
                    schemas_table_names,
                )
            )
        else:
            schemas_table_names = tuple(schemas_table_names)  # type: ignore
        self.schemas_table_names: Tuple[
            Tuple[Optional[str], str], ...
        ] = schemas_table_names  # type: ignore
        super().__init__()

    def __reduce__(
        self,
    ) -> Tuple[Callable[..., "TablesValidationError"], Tuple]:
        return (type(self), (self.schemas_table_names,))

    def _repr(self, message: str) -> str:
        def get_qualified_schema_table_name(
            schema: str, table_name: str
        ) -> str:
            if schema:
                return f"{schema}.{table_name}"
            else:
                return table_name

        table_names_message: str = ", ".join(
            starmap(get_qualified_schema_table_name, self.schemas_table_names)
        )
        return f"{message}: {table_names_message}"

    def __repr__(self) -> str:
        return self._repr("Table validation errors")


class TablesNotDeclaredError(TablesValidationError):
    def __repr__(self) -> str:
        return self._repr("Reflected tables not declared")


def _get_qualified_table_name(schema: Optional[str], table_name: str) -> str:
    if schema:
        return f"{schema}.{table_name}"
    else:
        return table_name


class ColumnValidationError(ValidationError):
    pass


class ColumnNameError(ColumnValidationError):
    def __init__(
        self,
        schema: Optional[str],
        table_name: str,
        column_name: str,
        property_name: str,
    ) -> None:
        self.schema: Optional[str] = schema
        self.table_name: str = table_name
        self.column_name: str = column_name
        self.property_name: str = property_name
        super().__init__()

    def __reduce__(self) -> Tuple[Callable[..., "ColumnNameError"], Tuple]:
        return (
            type(self),
            (
                self.schema,
                self.table_name,
                self.column_name,
                self.property_name,
            ),
        )

    def _repr(self, message: str) -> str:
        qualified_table_name: str = _get_qualified_table_name(
            self.schema, self.table_name
        )
        return (
            f"{message}: {qualified_table_name}.{self.column_name} "
            f"(property name: {self.property_name})"
        )

    def __repr__(self) -> str:
        return self._repr("Invalid column or property name")


class ColumnTypeError(ColumnValidationError):
    def __init__(
        self,
        schema: Optional[str],
        table_name: Optional[str],
        column_name: str,
        declared_type: TypeEngine,
        reflected_type: TypeEngine,
    ) -> None:
        assert column_name
        self.schema: Optional[str] = schema
        self.table_name: Optional[str] = table_name
        self.column_name: str = column_name
        self.declared_type: TypeEngine = declared_type
        self.reflected_type: TypeEngine = reflected_type
        super().__init__()

    def __reduce__(self) -> Tuple[Callable[..., "ColumnTypeError"], Tuple]:
        return (
            type(self),
            (
                self.schema,
                self.table_name,
                self.column_name,
                self.declared_type,
                self.reflected_type,
            ),
        )

    def _repr(self, message: str) -> str:
        qualified_table_name: Optional[str] = None
        if self.table_name is not None:
            qualified_table_name = _get_qualified_table_name(
                self.schema, self.table_name
            )

        qualified_column_name: str = (
            f"{qualified_table_name}.{self.column_name}"
            if qualified_table_name is not None
            else self.column_name
        )

        return (
            f"{message}: {qualified_column_name}\n"
            f"{type(self.declared_type).__module__}.{repr(self.declared_type)}"
            f" is not compatible with "
            f"{type(self.reflected_type).__module__}."
            f"{repr(self.reflected_type)}"
        )

    def __repr__(self) -> str:
        return self._repr(
            "There is a discrepancy between the declared and reflected "
            "columns' data types"
        )


class ColumnNotReflectedError(ColumnValidationError):
    def __init__(
        self,
        schema: Optional[str],
        table_name: str,
        column_name: str,
    ) -> None:
        self.schema: Optional[str] = schema
        self.table_name: str = table_name
        self.column_name: str = column_name
        super().__init__()

    def __reduce__(
        self,
    ) -> Tuple[Callable[..., "ColumnNotReflectedError"], Tuple]:
        return (type(self), (self.schema, self.table_name, self.column_name))

    def _repr(self, message: str) -> str:
        qualified_table_name: str = _get_qualified_table_name(
            self.schema, self.table_name
        )
        return f"{message}: " f"{qualified_table_name}.{self.column_name}"

    def __repr__(self) -> str:
        return self._repr("Column not found in reflected metadata")


class ColumnsNotDeclaredError(ColumnValidationError):
    def __init__(
        self,
        schema: Optional[str],
        table_name: str,
        column_names: Sequence[str],
    ) -> None:
        self.schema: Optional[str] = schema
        self.table_name: str = table_name
        self.column_names: Sequence[str] = column_names
        super().__init__()

    def __reduce__(
        self,
    ) -> Tuple[Callable[..., "ColumnsNotDeclaredError"], Tuple]:
        return (type(self), (self.schema, self.table_name, self.column_names))

    def _repr(self, message: str) -> str:
        qualified_table_name: str = _get_qualified_table_name(
            self.schema, self.table_name
        )
        column_name: str
        qualified_column_names_message: str = ", ".join(
            map(
                lambda column_name: (f"{qualified_table_name}.{column_name}"),
                self.column_names,
            )
        )
        return f"{message}: {qualified_column_names_message}"

    def __repr__(self) -> str:
        return self._repr("Reflected columns not declared")
