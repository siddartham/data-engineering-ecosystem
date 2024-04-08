import unittest

from delta import configure_spark_with_delta_pip
from analytics_orm.snowflake import create_engine
from analytics_orm.utilities import is_ci, lru_cache
from pyspark.sql import SparkSession  # type: ignore
from pyspark.sql.dataframe import DataFrame  # type: ignore
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.engine.url import URL  # type: ignore

GID_USER: str = "a.SF.D.ORG.RW"
PASSWORD_CERBERUS_PATH: str = f"app/org/snowflake/{GID_USER}"
WAREHOUSE: str = "DEV_WAREHOUSE"


class TestSnowflake(unittest.TestCase):
    @property
    @lru_cache()
    def bind(self) -> Connection:
        engine: Engine
        if is_ci():
            engine = create_engine(
                database="SNOWFLAKE_DEV_DB",
                user=GID_USER,
                password_cerberus_path=PASSWORD_CERBERUS_PATH,
                role="READWRITE_DEV",
                warehouse=WAREHOUSE,
                authenticator="https://org.okta.com",
            )
        else:
            engine = create_engine(
                database="SNOWFLAKE_DEV_DB",
                role="READWRITE_DEV",
                warehouse=WAREHOUSE,
                authenticator="externalbrowser",
            )
        return engine.connect()

    def test_create_engine(self) -> None:
        assert "COMMON_DIMENSION" in map(
            lambda row: row[1],
            self.bind.exec_driver_sql("SHOW SCHEMAS IN SNOWFLAKE_DEV_DB"),
        )

    def test_get_snowflake_spark_dataframe(self) -> None:
        url: URL = self.bind.engine.url
        data_frame: DataFrame = (
            configure_spark_with_delta_pip(
                SparkSession.builder.config(
                    "spark.sql.extensions",
                    "io.delta.sql.DeltaSparkSessionExtension",
                ).config(
                    "spark.sql.catalog.spark_catalog",
                    "org.apache.spark.sql.delta.catalog.DeltaCatalog",
                )
            )
            .getOrCreate()
            .read.jdbc(
                url=f"jdbc:snowflake://{url.host}.snowflakecomputing.com",
                table="SNOWFLAKE_DEV_DB.COMMON_DIMENSION.ALEMBIC_MIGRATION",
                properties=dict(
                    user=url.username,
                    role="ALL",
                    warehouse=url.query["warehouse"],
                    authenticator=url.query["authenticator"],
                    **(
                        {}
                        if url.query["authenticator"] == "externalbrowser"
                        else {
                            "password": url.password,
                        }
                    ),
                ),
            )
        )
        assert isinstance(data_frame, DataFrame)


if __name__ == "__main__":
    unittest.main()
