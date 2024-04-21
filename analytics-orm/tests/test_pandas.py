from datetime import datetime
from typing import Tuple, Type

import pandas
import pytest
from sqlalchemy import Column, DateTime, Integer, String  # type: ignore

from analytics_orm.declarative import Base as _Base
from analytics_orm.declarative import declarative_base
from analytics_orm.pandas import (
    add_drop_data_frame_table_columns,
    get_data_frame_with_unique_primary_keys,
    iter_column_aligned_data_frames,
    merge_data_frames,
)

Base: Type[_Base] = declarative_base()  # type: ignore


class Entity(Base):  # type: ignore
    entity_id: int = Column("ENTITY_ID", Integer, primary_key=True)
    version: int = Column("VERSION", Integer, primary_key=True)
    name: str = Column("NAME", String)
    updated: datetime = Column("UPDATED", DateTime)


def test_get_data_frame_with_unique_primary_keys() -> None:
    assert get_data_frame_with_unique_primary_keys(
        pandas.DataFrame(
            {
                "ENTITY_ID": [1, 2, 3, 2, 3],
                "VERSION": [1, 1, 1, 1, 1],
                "NAME": ["one", "two", None, "two (duplicate)", "three"],
                "UPDATED": [
                    datetime(1999, 1, 1),
                    datetime(1999, 1, 2),
                    datetime(1999, 1, 3),
                    datetime(1999, 1, 4),
                    datetime(1999, 1, 5),
                ],
            }
        ),
        Entity,
    ).to_dict() == {
        "ENTITY_ID": {0: 1, 1: 2, 3: 3},
        "VERSION": {0: 1, 1: 1, 3: 1},
        "NAME": {0: "one", 1: "two", 3: "three"},
        "UPDATED": {
            0: pandas.Timestamp("1999-01-01 00:00:00"),
            1: pandas.Timestamp("1999-01-02 00:00:00"),
            3: pandas.Timestamp("1999-01-05 00:00:00"),
        },
    }


def test_add_drop_data_frame_table_columns() -> None:
    assert add_drop_data_frame_table_columns(
        pandas.DataFrame(
            {
                "ENTITY_ID": [1, 2, 3],
                "VERSION": [1, 1, 1],
                "NAME": ["one", "two", "three"],
                "NONSENSE": ["nonsense", "nonsense", "nonsense"],
            }
        ),
        Entity,
        defaults={"UPDATED": datetime(1999, 1, 1)},
    ).to_dict() == {
        "ENTITY_ID": {0: 1, 1: 2, 2: 3},
        "VERSION": {0: 1, 1: 1, 2: 1},
        "NAME": {0: "one", 1: "two", 2: "three"},
        "UPDATED": {
            0: pandas.Timestamp("1999-01-01 00:00:00"),
            1: pandas.Timestamp("1999-01-01 00:00:00"),
            2: pandas.Timestamp("1999-01-01 00:00:00"),
        },
    }


def test_iter_column_aligned_data_frames() -> None:
    data_frames: Tuple[pandas.DataFrame, ...] = tuple(
        iter_column_aligned_data_frames(
            (
                pandas.DataFrame(
                    {
                        "ENTITY_ID": [1, 2, 3],
                        "VERSION": [1, 1, 1],
                        "NAME": ["one", "two", "three"],
                        "NONSENSE": ["nonsense", "nonsense", "nonsense"],
                    }
                ),
                pandas.DataFrame(
                    {
                        "ENTITY_ID": [1, 2, 1, 2],
                        "VERSION": [1, 1, 2, 2],
                        "NAME": ["one", "two", "one - v1", "two - v2"],
                        "UPDATED": [
                            datetime(1999, 1, 1),
                            datetime(1999, 1, 2),
                            datetime(1999, 1, 3),
                            datetime(1999, 1, 4),
                        ],
                    }
                ),
            )
        )
    )
    assert data_frames[0].to_dict() == {
        "ENTITY_ID": {0: 1, 1: 2, 2: 3},
        "VERSION": {0: 1, 1: 1, 2: 1},
        "NAME": {0: "one", 1: "two", 2: "three"},
        "NONSENSE": {0: "nonsense", 1: "nonsense", 2: "nonsense"},
        "UPDATED": {0: None, 1: None, 2: None},
    }
    assert data_frames[1].to_dict() == {
        "ENTITY_ID": {0: 1, 1: 2, 2: 1, 3: 2},
        "VERSION": {0: 1, 1: 1, 2: 2, 3: 2},
        "NAME": {0: "one", 1: "two", 2: "one - v1", 3: "two - v2"},
        "UPDATED": {
            0: pandas.Timestamp("1999-01-01 00:00:00"),
            1: pandas.Timestamp("1999-01-02 00:00:00"),
            2: pandas.Timestamp("1999-01-03 00:00:00"),
            3: pandas.Timestamp("1999-01-04 00:00:00"),
        },
        "NONSENSE": {0: None, 1: None, 2: None, 3: None},
    }


def test_merge_data_frames() -> None:
    assert merge_data_frames(
        (
            pandas.DataFrame(
                {
                    "ENTITY_ID": [1, 2, 3],
                    "VERSION": [1, 1, 1],
                    "NAME": ["one", "two", "three"],
                    "NONSENSE": ["nonsense", "nonsense", "nonsense"],
                }
            ),
            pandas.DataFrame(
                {
                    "ENTITY_ID": [1, 2, 1, 2],
                    "VERSION": [1, 1, 2, 2],
                    "NAME": ["one b", "two b", "one - v2", "two - v2"],
                    "UPDATED": [
                        datetime(1999, 1, 1),
                        datetime(1999, 1, 2),
                        datetime(1999, 1, 3),
                        datetime(1999, 1, 4),
                    ],
                }
            ),
        ),
        Entity,
    ).to_dict() == {
        "ENTITY_ID": {0: 1, 1: 2, 2: 3, 5: 1, 6: 2},
        "VERSION": {0: 1, 1: 1, 2: 1, 5: 2, 6: 2},
        "NAME": {
            0: "one",
            1: "two",
            2: "three",
            5: "one - v2",
            6: "two - v2",
        },
        "UPDATED": {
            0: pandas.NaT,
            1: pandas.NaT,
            2: pandas.NaT,
            5: pandas.Timestamp("1999-01-03 00:00:00"),
            6: pandas.Timestamp("1999-01-04 00:00:00"),
        },
    }


if __name__ == "__main__":
    pytest.main()
