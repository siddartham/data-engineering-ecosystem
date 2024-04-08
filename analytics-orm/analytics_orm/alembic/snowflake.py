from alembic.ddl import DefaultImpl  # type: ignore


class SnowflakeImpl(DefaultImpl):

    __dialect__ = "snowflake"
