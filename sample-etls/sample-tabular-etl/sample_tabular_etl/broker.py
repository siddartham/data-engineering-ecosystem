from logging import Logger
from typing import Callable, Optional, Tuple

from my_datastore_etl.broker import Broker as _Broker
from my_datastore_etl.broker import Concurrency, Work
from my_datastore_etl.utilities import get_print_logger
from my_datastore_orm.dialects.snowflake import validate_environment
from pyspark.sql.dataframe import DataFrame

from ._business_logic.extract import (
    extract_statement1,
    extract_statement2,
    extract_statement3,
    extract_statement4,
    extract_statement5,
)
from ._business_logic.transform import (
    transform1,
    transform2,
    transform3,
    transform4,
    transform5,
)

# Create a logger which writes to `sys.stdout`
log: Logger = get_print_logger(__name__)

SAMPLE_TABLE_NAME: str = "SAMPLE_TABLE"


def _default_load_filter_function(table_name: str) -> bool:
    """
    This function is used to limit which tables are loaded into Snowflake.
    """
    unqualified_table_name: str = table_name.split(".")[-1].upper()
    return unqualified_table_name == "SAMPLE_TABLE"


class Broker(_Broker):
    """
    This class brokers exchanges of data between source systems and
    sustainability data stores.

    Parameters:

    - environment (str): "dev", "qa", or "prod"
    - parallelism (int) = None: If this is 0 or `None`, the default
      parallelism for the Spark cluster will be used.
    - concurrency (my_datastore_etl.concurrency.Concurrency)
      = my_datastore_etl.concurrency.Concurrency.SPARK
    - echo (bool) = False: If `True`, all logging will be printed to
        the console.
    """

    work: Work

    def __init__(
        self,
        environment: str = "",
        parallelism: Optional[int] = None,
        echo: bool = True,
    ) -> None:
        super().__init__(
            environment=environment,
            parallelism=parallelism,
            concurrency=Concurrency.SPARK,
            echo=echo,
            work=Work(
                environment=environment,
                echo=echo,
            ),
        )

    def extract_transform(self) -> DataFrame:

        # extract
        log.info("Extracting data from snowflake source")

        table1: DataFrame = (
            self.work.get_snowflake_spark_dataframe(
                table=f"({extract_statement1})"
            ).cache()
        )
        table2: DataFrame = (
            self.work.get_snowflake_spark_dataframe(
                table=f"({extract_statement2})"
            ).cache()
        )
        table3: DataFrame
        table4: DataFrame
        table5: DataFrame

        # modify queries to point to the correct environment
        query_default_environments: Tuple[str, ...] = (
            "local",
            "test",
            "qa",
            "sole-qa",
        )
        if self.work.environment not in query_default_environments:
            environment: str = self.work.environment.rpartition("-")[
                -1
            ].upper()
            extract_statement_new = (
                enablon_reference_code_select_statement.replace(
                    "SNOWFLAKE_QA",
                    f"SNOWFLAKE_{environment}",
                )
            )
            df1 = self.work.get_snowflake_spark_dataframe(
                table=f"({enablon_reference_code_select_statement_new})"
            )
            enablon_unit_select_statement_new = (
                enablon_unit_select_statement.replace(
                    "SNOWFLAKE_QA",
                    f"SNOWFLAKE_{environment}",
                )
            )
            df2 = self.work.get_snowflake_spark_dataframe(
                table=f"({extract_statement2})"
            )
        else:
            df3 = self.work.get_snowflake_spark_dataframe(
                table=f"({extract_statement3})"
            )
            df4 = (
                self.work.get_snowflake_spark_dataframe(
                    table=f"({extract_statement4})"
                )
            )
            df5 = self.work.get_snowflake_spark_dataframe(
                table=f"({extract_statement5})"
            )

        # transform
        log.info("Transforming the data")

        df1: DataFrame = (
            transform1(df0)
        )
        df2: DataFrame = (
            transform2(df0)
        )
        df3: DataFrame = (
            transform3(df0)
        )
        df4: DataFrame = (
            transform4(
                df0
            )
        )
        df1: DataFrame = (
            transform4(df0)
        )
        df2: DataFrame = (
            transform2(
                df1
            )
        )
        df3: DataFrame = transform3(
            df0
        )
        df4_1: DataFrame = (
            df3.unionAll(df1)
            .unionAll(df2)
            .unionAll(df3)
            .unionAll(df4)
            .unionAll(df5)
        )
        df10: DataFrame = transform5(
            df6,
            df7,
            df8,
            df9,
        )
        return df10

    def snowflake_load(
        self,
        filter_function: Callable[[str], bool] = _default_load_filter_function,
    ) -> None:
        """
        This method loads the "semantic" data from S3 into Snowflake
            - filter_function
        """
        super().snowflake_load(filter_function=filter_function)
        validate_environment(
            bind=self.work.snowflake_session.bind,
            only=(SAMPLE_TABLE_NAME,),
            echo=True,
        )

    def main(
        self,
    ) -> None:
        df: DataFrame = (
            self.extract_transform()
        )
        self.merge(
            data=df,
            table_name=SAMPLE_TABLE_NAME,
        )
        self.snowflake_load()
