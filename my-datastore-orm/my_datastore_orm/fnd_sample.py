from typing import Any, Dict

from sqlalchemy import (  # type: ignore
    Boolean,
    Column,
    DateTime,
    Float,
    Integer,
    String,
)

from .base import Base


class SampleObject(Base):
    """
    SAMPLE_OBJECT

    Primary Key:

    - entity_uuid (str)
    - entity_id (int)
    - entity_nm (str)
    - reporting_period_dt (datetime)
    - service_type_nm (str)
    - indicator_id (int)

    Other Columns/Properties:

    - indicator_cd (str)
    - indicator_nm (str)
    - indicator_type_nm (str)
    - reporting_period_year_nbr (int)
    - reporting_period_month_nbr (int)
    - reporting_period_day_nbr (int)
    - address (str)
    - city_nm (str)
    - state_nm (str)
    - country_nm (str)
    - zip_cd (int)
    - geographical_axis (str)
    - latitude (float)
    - longitude (float)
    - area_in_sqft (float)
    - keyword (str)
    - entity_status_desc (str)
    - frequency_cd (int)
    - frequency_nm (str)
    - reporting_period_fiscal_year_nbr (str)
    - reporting_period_fiscal_quarter_nbr (str)
    - value_original_nbr (str)
    - value_code_nbr (str)
    - source_uom (str)
    - scope_nm (str)
    - extrapolation_ind (bool)
    - campaign_check_txt (str)
    """

    __table_args__: Dict[str, Any] = dict(sqlite_table_name="")
    entity_uuid = Column("ENTITY_UUID", String, primary_key=True)
    entity_id = Column("ENTITY_ID", Integer, primary_key=True)
    entity_nm = Column("ENTITY_NM", String, primary_key=True)
    reporting_period_dt = Column(
        "REPORTING_PERIOD_DT", DateTime, primary_key=True
    )
    service_type_nm = Column("SERVICE_TYPE_NM", String, primary_key=True)
    indicator_id = Column("INDICATOR_ID", Integer, primary_key=True)
    indicator_cd = Column("INDICATOR_CD", String)
    indicator_nm = Column("INDICATOR_NM", String)
    indicator_type_nm = Column("INDICATOR_TYPE_NM", String)
    reporting_period_year_nbr = Column("REPORTING_PERIOD_YEAR_NBR", Integer)
    reporting_period_month_nbr = Column("REPORTING_PERIOD_MONTH_NBR", Integer)
    reporting_period_day_nbr = Column("REPORTING_PERIOD_DAY_NBR", Integer)
    corporate_id = Column("CORPORATE_ID", Integer)
    corporate_cd = Column("CORPORATE_CD", String)
    corporate_nm = Column("CORPORATE_NM", String)
    brand_id = Column("BRAND_ID", Integer)
    brand_cd = Column("BRAND_CD", String)
    brand_nm = Column("BRAND_NM", String)
    lease_nbr = Column("LEASE_NBR", String)
    address = Column("ADDRESS", String)
    city_nm = Column("CITY_NM", String)
    state_nm = Column("STATE_NM", String)
    country_nm = Column("COUNTRY_NM", String)
    zip_cd = Column("ZIP_CD", Integer)
    latitude = Column("LATITUDE", Float)
    longitude = Column("LONGITUDE", Float)
    area_in_sqft = Column("AREA_IN_SQFT", Float)
    keyword = Column("KEYWORD", String)
    frequency_cd = Column("FREQUENCY_CD", String)
    frequency_nm = Column("FREQUENCY_NM", String)
    reporting_period_fiscal_year_nbr = Column(
        "REPORTING_PERIOD_FISCAL_YEAR_NBR", String
    )
    reporting_period_fiscal_quarter_nbr = Column(
        "REPORTING_PERIOD_FISCAL_QUARTER_NBR", String
    )
