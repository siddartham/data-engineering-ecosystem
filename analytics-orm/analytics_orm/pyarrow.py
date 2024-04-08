from typing import Dict, List, Type

import pyarrow  # type: ignore
from sqlalchemy import Column, inspect  # type: ignore
from sqlalchemy.sql import sqltypes  # type: ignore

from .declarative import Base

__all__: List[str] = ["get_schema_from_mapping"]


def get_schema_from_mapping(mapping_class: Type[Base]) -> pyarrow.Schema:
    """
    Given a sub-class of `analytics_orm.base.Base`, return a
    corresponding instance of `pyarrow.Schema` for use in writing parquet
    files with pandas + pyarrow.
    """
    assert issubclass(mapping_class, Base)
    fields: List[pyarrow.Field] = []
    column: Column
    for column in inspect(mapping_class).columns.values():
        kwargs: Dict[str, int] = {}
        if isinstance(column.type, sqltypes.Numeric):
            if isinstance(column.type.precision, int):
                kwargs["precision"] = column.type.precision
            if isinstance(column.type.scale, int):
                kwargs["scale"] = column.type.scale
        data_type: pyarrow.DataType = (
            pyarrow.string()
            if isinstance(column.type, sqltypes.String)
            else (
                pyarrow.bool_()
                if isinstance(column.type, sqltypes.Boolean)
                else (
                    pyarrow.int64()
                    if isinstance(column.type, sqltypes.Integer)
                    else (
                        pyarrow.float64()
                        if isinstance(column.type, sqltypes.Float)
                        else (
                            pyarrow.decimal128(**kwargs)
                            if isinstance(column.type, sqltypes.Numeric)
                            else (
                                pyarrow.timestamp("us")
                                if isinstance(column.type, sqltypes.DateTime)
                                else (
                                    pyarrow.date32()
                                    if isinstance(column.type, sqltypes.Date)
                                    else pyarrow.null()
                                )
                            )
                        )
                    )
                )
            )
        )
        fields.append(pyarrow.field(column.name, data_type))
    return pyarrow.schema(fields)
