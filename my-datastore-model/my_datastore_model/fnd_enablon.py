from sqlalchemy import (  # type: ignore
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    ForeignKeyConstraint,
    Integer,
    String,
)

from .base import Base

SCHEMA: str = __name__.split(".")[-1].upper()


class HoUnitLevel(Base):
    """
    HO_UNIT_LEVEL

    Primary Key:

    - level_no (int)

    Other Columns/Properties:

    - color (str)
    - name (str)
    - last_mod (datetime.datetime)
    - created_on (datetime.datetime)
    - modified_on (datetime.datetime)
    """

    level_no = Column(
        "LEVEL_NO",
        Integer,
        primary_key=True,
        autoincrement=False,
    )
    color = Column(
        "COLOR",
        String,
    )
    name = Column(
        "NAME",
        String,
    )
    last_mod = Column(
        "LAST_MOD",
        DateTime,
    )
    created_on = Column(
        "CREATED_ON",
        DateTime,
    )
    modified_on = Column(
        "MODIFIED_ON",
        DateTime,
    )
