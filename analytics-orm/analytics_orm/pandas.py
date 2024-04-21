from typing import (
    AbstractSet,
    Any,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Type,
)

import pandas
from ordered_set import OrderedSet

from .declarative import (
    Base,
    get_class_column_names,
    get_class_primary_key_and_column_names,
    get_class_primary_key_column_names,
)


def get_data_frame_with_unique_primary_keys(
    data_frame: pandas.DataFrame,
    table_mapping: type,
) -> pandas.DataFrame:
    """
    This function takes a data frame and a sub-class of
    `analytics_orm.base.Base` and returns a data frame
    where there is only one record for each primary key, as defined by
    `table_mapping`. The record associated with the first use of a primary key
    is used.
    """
    assert issubclass(table_mapping, Base)
    # Get the column names, broken out by those which are and are not part
    # of the primary key
    primary_key_column_names: List[str]
    non_primary_key_column_names: List[str]
    (
        primary_key_column_names,
        non_primary_key_column_names,
    ) = map(
        # Note: pandas doesn't handle tuples correctly for the `by` parameter,
        # so we convert these to lists
        list,
        get_class_primary_key_and_column_names(table_mapping),
    )
    if non_primary_key_column_names:
        # Create a ranked data frame where the window is partitioned by
        # the primary key, and sorted by the remaining keys (granting
        # precedence to non-null values)
        return (
            data_frame.sort_values(
                primary_key_column_names + non_primary_key_column_names,
                ignore_index=True,
            )
            .groupby(primary_key_column_names)
            .nth(0)
        )
    return data_frame.drop_duplicates()


def add_drop_data_frame_table_columns(
    data_frame: pandas.DataFrame,
    table_mapping: Optional[Type[Base]] = None,
    columns: Iterable[str] = (),
    defaults: Optional[Dict[str, Any]] = None,
) -> pandas.DataFrame:
    """
    Add and/or drop columns from the provided data frame to align with the
    indicated table class (or a provided tuple of column names).

    Parameters:

    - data_frame (pandas.DataFrame)
    - table_mapping (type|None) = None
    - columns ((str,)) = ()
    - defaults ({str: typing.Any}|None) = None
    """
    assert table_mapping or columns
    if table_mapping and not columns:
        columns = get_class_column_names(table_mapping)
    if not isinstance(columns, AbstractSet):
        columns = OrderedSet(columns)
    data_frame_columns: AbstractSet[str] = OrderedSet(data_frame.columns)
    column: str
    for column in columns - data_frame_columns:
        default: Any = None
        if defaults:
            default = defaults.get(column, None)
        _: pandas.Series
        data_frame[column] = pandas.Series(
            default for _ in range(len(data_frame))
        )
    for column in data_frame_columns - columns:
        data_frame = data_frame.drop(columns=[column])
    return data_frame


def iter_column_aligned_data_frames(
    data_frames: Iterable[pandas.DataFrame],
    defaults: Optional[Dict[str, Any]] = None,
) -> Iterable[pandas.DataFrame]:
    """
    Append columns as needed to data frames such that all have the same
    columns (by name).

    Parameters:

    - data_frames ([pandas.DataFrame]): One or more data frames
    - defaults ({str: typing.Any}|None) = None: A mapping of column
      names to default values to fill in when/if adding columns.
    """
    data_frames = tuple(data_frames)
    columns: OrderedSet[str] = OrderedSet()
    data_frame: pandas.DataFrame
    for data_frame in data_frames:
        columns |= OrderedSet(data_frame.columns)
    for data_frame in data_frames:
        if columns - set(data_frame.columns):
            yield add_drop_data_frame_table_columns(
                data_frame,
                columns=columns,
                defaults=defaults,
            )
        else:
            yield data_frame


def merge_data_frames(
    data_frames: Iterable[pandas.DataFrame],
    table_mapping: Optional[Type[Base]] = None,
    primary_key: Sequence[str] = (),
    defaults: Optional[Dict[str, Any]] = None,
) -> pandas.DataFrame:
    """
    This function takes two or more data frames and a sub-class of
    `analytics_orm.base.Base` and returns a data frame
    wherein a record associated with each primary key is sourced only from the
    first data frame in which it is encountered.

    Parameters:

    - data_frames ([pandas.DataFrame])
    - table_mapping (type|None) = None: A table from which to infer a primary
      key.
    - primary_key ((str,)) = (): A tuple of strings representing the names
      of the primary key columns.
    - defaults ({str: typing.Any}|None) = None: A mapping of column
      names to default values to fill in when/if adding columns.
    """
    if not primary_key:
        if not (
            isinstance(table_mapping, type) and issubclass(table_mapping, Base)
        ):
            raise ValueError(repr(locals()))
        primary_key = get_class_primary_key_column_names(table_mapping)
    if not isinstance(primary_key, list):
        primary_key = list(primary_key)
    if isinstance(data_frames, tuple):
        data_frames = list(data_frames)
    data_frame: pandas.DataFrame
    # Ensure all data frames have matching columns (by name)
    if table_mapping:
        # If a table mapping class was provided, use the table's columns
        data_frames = map(
            lambda data_frame: add_drop_data_frame_table_columns(
                data_frame,
                table_mapping=table_mapping,
                defaults=defaults,
            ),
            data_frames,
        )
    else:
        # If a table mapping class was not provided, expand input data
        # frames to include all columns
        data_frames = iter_column_aligned_data_frames(
            data_frames,
            defaults=defaults,
        )
    return (
        pandas.concat(data_frames, ignore_index=True)
        .groupby(by=primary_key)
        .nth(0)
    )
