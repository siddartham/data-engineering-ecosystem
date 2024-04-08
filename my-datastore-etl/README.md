# my-datastore-etl

[![test](https://github.com/siddartham/data-engineering-ecosystem/my-datastore-etl/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/my-datastore-etl/actions/workflows/test.yml)
[![distribute](https://github.com/siddartham/data-engineering-ecosystem/my-datastore-etl/actions/workflows/distribute.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/my-datastore-etl/actions/workflows/distribute.yml)

[Development Environment Setup](https://github.com/siddartham/data-engineering-ecosystem/dev-env-setup)

This package provides a common framework for  MyDataStore's
"Extract, Transform and Load" (ETL) jobs.


## Installation


```shell
pip3 install 'my-datastore-etl[all]'
```

Please note that the above command installs this package with *all* extras
(spark, snowflake, and postgresql). This is rarely needed
or desirable, instead you should replace "all" with the extras you
actually need, separated by commas.

## Usage

This library should be used as a framework for creating ETL packages for
MyDataStore.

To create a new ETL package:

1. Follow [these instructions](https://github.com/siddarthm/data-engineering-ecosystem/python-package-template/blob/master/README.md)
   to create the skeleton of your local repository:

   - The recommended naming pattern for your project/package
     is: "{job-name}-etl". Note: Your _job name_ can
     be your data product's name, if there will only be one ETL job for the
     data product, or a concatenation of the source system name _and_ the
     data product name. Use your best judgement.
   - Leave your root package name unmodified in the prompt, it  will follow
     a pattern derived from your project name, following the pattern:
     "{job_name}_etl".

2. In your project directory, run `make` to create your virtual environment,
   then activate your virtual environment by running `. venv/bin/activate`.

3. Install "my-datastore-etl" in your project's virtual environment,
   making sure to include any extras you need for your package (spark,
   snowflake, and/or postgresql).

   - Almost all jobs will need the "snowflake"
     extra.
   - All spark jobs will need the "spark" extra.

   For a spark job, you would typically want
   **my-datastore-etl[spark,snowflake]**, so you'd install as
   follows:

   ```shell script
   pip install 'my-datastore-etl[spark,snowflake]'
   ```

4. In ./setup.cfg, add "my-datastore-etl[spark,snowflake]~=0.0"
   to your **install_requires** option (modified to include only the extras
   you need). Note: do not
   copy/paste the following example, it should only be used for reference:

   ```ini
   [metadata]
   name = sample-etl
   version = 0.0.0
   author_email = reddy.siddartha53@gmail.com
   description = A short description of the job
   long_description = file: README.md
   long_description_content_type = text/markdown
   url = https://github.com/siddartham/sample-etl

   [options]
   python_requires = ~=3.8
   include_package_data = True
   packages =
       sample_etl
   install_requires =
       my-datastore-etl[snowflake,spark]~=0.0

   [options.entry_points]
   console_scripts =
       sample-etl = sample_etl.__main__:main

   [options.package_data]
   * = py.typed
   ```

5. Run `make requirements`. This will update your required package versions
   in setup.cfg to match the package versions you've installed (in this
   example, that's just my-datastore-etl), and will update
   ./requirements.txt to match.

6. Create a sub-module named "broker" under in your package directory (this
   would be in a file path looking something like
   "./{job_name}_etl/broker.py"). Your project structure
   should now look something like the following:

   ```text
   sample-etl
   ├── .dockerignore
   ├── .editorconfig
   ├── .flake8
   ├── .gitignore
   ├── Jenkinsfile
   ├── Makefile
   ├── README.md
   ├── mypy.ini
   ├── sample_etl
   │   ├── __init__.py
   │   ├── __main__.py
   │   ├── broker.py
   │   └── py.typed
   ├── pyproject.toml
   ├── requirements.txt
   ├── ci_requirements.txt
   ├── dev_requirements.txt
   ├── setup.py
   ├── setup.cfg
   ├── tests
   │     └── test_job_name_etl.py
   └── tox.ini
   ```

7. In your broker module, you will need to create sub-classes of
   `sample_etl.broker.Broker` and
   `sample_etl.broker.Work` (please see the annotated
   [example](#spark-broker-module-example) below).

8. For each step you want to represent as a separate DAG task (corresponding to
   a spark-submit job when using Spark), create a public method on your
   `Broker` class. For complex tasks, you may need to break down your method
   further, in these cases please create either *private* methods on your
   `Broker` class, or public (and potentially private) methods on your `Work`
   class. Please note that:
   - Methods comprising code which must be executed on the driver (Spark) or
     main process (multiprocessing) should be created on your `Broker` class
     (*not* your `Work` class). This includes code which will utilize or
     manipulate Spark data frames.
   - Operations which will be parallelized (executed with
     `Broker.map` or `Broker.starmap`), you will need to create as methods of
     your `Work` class. `Work` class methods which are, or should/can be,
     called directly from your broker (either by passing the method to
     `Broker.map`/`Broker.starmap` or by calling directly) should be public
     methods. Methods only intended to be called from other `Work` methods
     should be private methods.

9. Create your CLI in ./{job_name}_etl/\_\_main\_\_.py
   (see this [example](#spark-main-module-example) below)).

10. Create your Airflow DAG under the sub-directory "./airflow/dags/" in your
    project directory. To ensure the file name is unique, it is recommended that
    you use a snake-cased variation of your job name + "_etl.py", so for our
    example the relative file path would be "./airflow/dags/job_name_etl.py".

    Your project structure will now look something like this:

    ```text
    job-name-etl
    ├── .dockerignore
    ├── .editorconfig
    ├── .flake8
    ├── .gitignore
    ├── airflow
    │     └── dags
    │         └── job_name_etl.py
    ├── Jenkinsfile
    ├── Makefile
    ├── README.md
    ├── mypy.ini
    ├── job_name_etl
    │         ├── __init__.py
    │         ├── __main__.py
    │         ├── broker.py
    │         └── py.typed
    ├── pyproject.toml
    ├── requirements.txt
    ├── ci_requirements.txt
    ├── dev_requirements.txt
    ├── setup.py
    ├── setup.cfg
    ├── tests
    │     └── job_name_etl.py
    └── tox.ini
    ```

    Please the annotated [example](#spark-airflow-dag-example) below.

11. Update your Jenkinsfile to include the commands needed to deploy your
    Spark job, if applicable (see the below
    [example](#spark-jenkinsfile-example))

### Spark Broker Module Example

The following example of a broker module implements the same operation
using two different methods. In each of these `Broker` methods we populate a
table named SEASON_YEAR, which is a rollup of
CALENDAR_PROD.ENTERPRISECALENDAR_V. Please note that SEASON_YEAR is not a real
table in our database, it is just used as a simple example.

```python
import my_datastore_etl.broker
from logging import Logger
from my_datastore_etl.broker import Concurrency
from my_datastore_etl.utilities import get_print_logger
from my_datastore_orm.dialects.snowflake import SEMANTIC_PATH
from file_system_client.s3 import S3
from typing import Optional, Tuple
from pyspark.sql.dataframe import DataFrame
from pyspark.sql import functions as pyspark_sql_functions
from my_datastore_orm.dialects.s3 import SEMANTIC_PATH
# Note: The databricks dialect is a WIP
from my_datastore_orm.dialects.databricks import validate_environment

# Create a logger which writes to `sys.stdout`
log: Logger = get_print_logger(__name__)


# This work class does not implement any custom functionality, and as such
# could simply be replaced by the parent class in usage by our broker, but
# is included in this example for annotation purposes.
class Work(my_datastore_etl.broker.Work):
    """
    Your docstring can look much like the parent class' docstring, but
    if you add any additional parameters please include them:

        This class encapsulates work to be performed by individual
        processes in a multi-process pool.

        Parameters:

        - **environment** (str)
        - **echo** (bool)
    """

    file_system: S3

    def __init__(
        self,
        environment: str,
        echo: bool = False,
        # Add any additional parameters which need to be passed to each
        # instance *here*, before the private parameters (if any are
        # needed)
        _snowflake_connection_string: str = "",
        _file_system: Optional[S3] = None,
    ) -> None:
        super().__init__(
            environment,
            echo=echo,
            _snowflake_connection_string=_snowflake_connection_string,
            _file_system=_file_system,
        )

    # You must include a __reduce__ method, as this class contains
    # data and logic which must be serialized (pickled) for distributing
    # to disparate processes and/or executors
    def __reduce__(self) -> Tuple[type, Tuple]:
        return (
            Work,
            (
                self.environment,
                self.echo,
                # Include values to use for any additional parameters you
                # created specific to this work sub-class *here*
                self._snowflake_connection_string,
                self.file_system,
            ),
        )


def _default_load_filter_function(table_name: str) -> bool:
    """
    This function is used to limit which tables are loaded into Snowflake.
    """
    unqualified_table_name: str = table_name.split(".")[-1].upper()
    return unqualified_table_name == "SEASON_YEAR"


# This class acts as a broker of data between source systems and
# mydatastore. The "work" property of this class is an instance of `Work`,
# and is where we cache/hold most configuration and connection
# information/objects.
class Broker(my_datastore_etl.broker.Broker):
    """
    Your docstring can look much like the parent class' docstring, but
    if you add any additional parameters please include them:

        This class brokers exchanges of data between {source-system} and
        mydatastore.

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
        concurrency: Concurrency = Concurrency.SPARK,
        echo: bool = False,
    ) -> None:
        super().__init__(
            environment=environment,
            parallelism=parallelism,
            concurrency=concurrency,
            echo=echo,
            work=Work(
                environment=environment,
                echo=echo,
            ),
        )

    # You should create a public method for each DAG task you want to perform.
    def spark_sql_to_s3_example(self) -> None:
        """
        In this example we execute a Spark SQL query to aggregate source
        data, then write to S3.

        This method would be executed with a command looking something like
        `sample-etl spark-sql-to-s3-example
        {dev|qa|prod|local|test|sole-dev|sole-qa|sole-prod}`.
        """
        select_statement: str = (
            "SELECT SEASON_YEAR_CD AS SEASON_YEAR_CODE, "
            "SEASON_NBR AS SEASON_NUMBER, "
            "YEAR_NBR AS YEAR_NUMBER, "
            "MIN(CALENDAR_DT) AS SEASON_YEAR_START "
            "FROM CALENDAR_PROD.ENTERPRISECALENDAR_V "
            "GROUP BY SEASON_YEAR_CD, "
            "SEASON_NBR, "
            "YEAR_NBR"
        )
        season_year_dataframe: DataFrame
        if self.work.environment == "test":
            # Because when testing locally we don't have access to the
            # hive metastore, we query against Databricks and read the results into
            # a DataFrame. We also need to modify the query in order to
            # specify the catalog (NGAP_HIVE).
            select_statement = select_statement.replace(
                "CALENDAR_PROD.ENTERPRISECALENDAR_V",
                "NGAP_HIVE.CALENDAR_PROD.ENTERPRISECALENDAR_V"
            )
            season_year_dataframe = self.work.get_databricks_dataframe(
                table=f"({select_statement})"
            )
        else:
            # Read Spark SQL query results into a DataFrame
            season_year_dataframe = self.work.spark_session.sql(
                select_statement
            )
        # The following assumes a table exists in our ORM
        # (my-datastore-orm) named "SEASON_YEAR". Please note
        # that this is not a real table, it is just used as an example.
        table_name: str = "SEASON_YEAR"
        # Resolve the correct S3 prefix for the current environment + table
        target_prefix: str = self.work.file_system.get_absolute_path(
            f"{SEMANTIC_PATH}/{table_name}/"
        )
        # Get the S3 URL for our target prefix
        target_url: str = self.work.file_system.get_url(target_prefix)
        # Delete the _SUCCESS file so that other processes trying to access
        # these files will know an update is in progress
        # self.work.file_system.delete_success(target_prefix)
        # Write the data to S3
        season_year_dataframe.write.mode("overwrite").parquet(
            target_url, partitionBy=None
        )
        # Put the _SUCCESS file, to signal the data is complete
        # once again to other processes attempting to access the files
        self.work.file_system.put_success(target_prefix)
        # Add a note to the log indicating our files were successfully written
        log.info(f"Successfully wrote parquet files to {target_url}")
        if self.work.environment != "test":
            # Validate that the primary key is unique, column data types are
            # correct, etc. This is useful to include in the ETL job rather
            # than only during CI testing if we are sourcing data from
            # untrusted sources (from any team without end-to-end validation).
            validate_environment(
                bind=self.work.databricks_session.bind,
                only=("SEASON_YEAR",),
                echo=True,
            )

    def spark_table_to_s3_example(self) -> None:
        """
        In this example we read from a table, aggregate using data frames,
        then write to S3.

        This method would be executed with a command looking something like
        `sample-etl spark-table-to-s3-example
        {dev|qa|prod|local|test|sole-dev|sole-qa|sole-prod}`.

        Please note that this example cannot be replicated locally for unit
        tests, because it requires use of the hive metastore.
        """
        # Read the table into a DataFrame
        calendar_dataframe: DataFrame
        if self.work.environment == "test":
            # Because when testing locally we don't have access to the
            # hive metastore, we load the table from Databricks. We also need to
            # include the catalog (NGAP_HIVE) in the table name.
            calendar_dataframe = self.work.get_databricks_dataframe(
                table="NGAP_HIVE.CALENDAR_PROD.ENTERPRISECALENDAR_V",
            )
        else:
            # Load the table into a DataFrame
            calendar_dataframe = self.work.spark_session.read.table(
                "CALENDAR_PROD.ENTERPRISECALENDAR_V",
            )
        season_year_dataframe = calendar_dataframe.select(
            calendar_dataframe["season_year_cd"].alias("SEASON_YEAR_CODE"),
            calendar_dataframe["season_nbr"].alias("SEASON_NUMBER"),
            calendar_dataframe["year_nbr"].alias("YEAR_NUMBER"),
            calendar_dataframe["calendar_dt"]
        ).groupBy(
            "SEASON_YEAR_CODE",
            "SEASON_NUMBER",
            "YEAR_NUMBER",
        ).agg(
            pyspark_sql_functions.min(
                calendar_dataframe["calendar_dt"]
            ).alias("SEASON_YEAR_START")
        )
        # The following assumes a table exists in our ORM
        # (my-datastore-orm) named "SEASON_YEAR". Please note
        # that this is not a real table, it is just used as an example.
        table_name: str = "SEASON_YEAR"
        # Resolve the correct S3 prefix for the current environment + table
        target_prefix: str = self.work.file_system.get_absolute_path(
            f"{SEMANTIC_PATH}/{table_name}/"
        )
        # Get the S3 URL for our target prefix
        target_url: str = self.work.file_system.get_url(target_prefix)
        # Delete the _SUCCESS file so that other processes trying to access
        # these files will know an update is in progress
        self.work.file_system.delete_success(target_prefix)
        # Write the data to S3
        season_year_dataframe.write.mode("overwrite").parquet(
            target_url, partitionBy=None
        )
        # Put the _SUCCESS indicator, to signal the data is complete
        # once again to other processes attempting to access these files
        self.work.file_system.put_success(target_prefix)
        # Add a note to the log indicating our files were successfully written
        log.info(f"Successfully wrote parquet files to {target_url}")
        if self.work.environment != "test":
            # Validate that the primary key is unique, column data types are
            # correct, etc. This is useful to include in the ETL job rather
            # than only during CI testing if we are sourcing data from
            # untrusted sources (from any team without end-to-end validation).
            validate_environment(
                bind=self.work.databricks_session.bind,
                only=("SEASON_YEAR",),
                echo=True,
            )

    def snowflake_sql_to_s3_example(self) -> None:
        """
        In this example we execute a Snowflake SQL query to aggregate source
        data, then write to S3.

        This method would be executed with a command looking something like
        `sample-etl snowflake-sql-to-s3-example
        {dev|qa|prod|local|test|sole-dev|sole-qa|sole-prod}`.
        """
        select_statement: str = (
            "SELECT SEASON_YEAR_CD AS SEASON_YEAR_CODE, "
            "SEASON_NBR AS SEASON_NUMBER, "
            "YEAR_NBR AS YEAR_NUMBER, "
            "MIN(CALENDAR_DT) AS SEASON_YEAR_START "
            "FROM CALENDAR_PROD.BCL.ENTERPRISECALENDAR_V "
            "GROUP BY SEASON_YEAR_CD, "
            "SEASON_NBR, "
            "YEAR_NBR"
        )
        # Read Snowflake SQL query results into a DataFrame
        season_year_dataframe: DataFrame = (
            self.work
        ).get_spark_snowflake_dataframe(
            table=f"({select_statement})"
        )
        # The following assumes a table exists in our ORM
        # (my-datastore-orm) named "SEASON_YEAR". Please note
        # that this is not a real table, it is just used as an example.
        table_name: str = "SEASON_YEAR"
        # Resolve the correct S3 prefix for the current environment + table
        target_prefix: str = self.work.file_system.get_absolute_path(
            f"{SEMANTIC_PATH}/{table_name}/"
        )
        # Get the S3 URL for our target prefix
        target_url: str = self.work.file_system.get_url(target_prefix)
        # Delete the _SUCCESS file so that other processes trying to access
        # these files will know an update is in progress
        # self.work.file_system.delete_success(target_prefix)
        # Write the data to S3
        season_year_dataframe.write.mode("overwrite").parquet(
            target_url, partitionBy=None
        )
        # Put the _SUCCESS file, to signal the data is complete
        # once again to other processes attempting to access the files
        self.work.file_system.put_success(target_prefix)
        # Add a note to the log indicating our files were successfully written
        log.info(f"Successfully wrote parquet files to {target_url}")
        if self.work.environment != "test":
            # Validate that the primary key is unique, column data types are
            # correct, etc. This is useful to include in the ETL job rather
            # than only during CI testing if we are sourcing data from
            # untrusted sources (from any team without end-to-end validation).
            validate_environment(
                bind=self.work.databricks_session.bind,
                only=("SEASON_YEAR",),
                echo=True,
            )


    def snowflake_load(
        self,
        filter_function: Callable[[str], bool] = _default_load_filter_function,
    ) -> None:
        """
        Your docstring can look much like the parent class' docstring:

            This method loads the "semantic" data from S3 into Snowflake, in
            an order determined by foreign-key relationships (tables with
            referenced keys are loaded before all tables which reference those
            keys).

            - filter_function: This parameter is exposed in order for this
              class to retain the same signature as its parent, however it is
              not used. The default value applies the desired filter.
        """
        super().snowflake_load(_default_load_filter_function)
```

### Spark Main Module Example

Your `__main__` sub-module will implement your CLI entry point. The following
example creates an appropriate CLI for use with the above
[Broker Module Example](#spark-broker-module-example).

```python
import argparse
import logging
from .broker import Broker


def spark_table_to_s3_example(
    environment: str,
    echo: bool = False
) -> None:
    Broker(
        environment=environment,
        echo=echo,
    ).spark_table_to_s3_example()


def spark_sql_to_s3_example(
    environment: str,
    echo: bool = False
) -> None:
    Broker(
        environment=environment,
        echo=echo,
    ).spark_sql_to_s3_example()


def load(environment: str, echo: bool = False) -> None:
    return Broker(environment=environment, echo=echo).snowflake_load()


def main() -> None:
    """
    This is the main entry point for your CLI
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--log",
        action="store",
        type=str,
        default=None,
        help="Log output path",
    )
    parser.add_argument(
        "-e",
        "--echo",
        action="store_const",
        const=True,
        default=False,
        help="Echo requests/responses",
    )
    parser.add_argument(
        "operation",
        help="spark-sql-to-s3-example | spark-table-to-s3-example | load",
    )
    parser.add_argument(
        "environment",
        help="dev|qa|prod|local|test|sole-dev|sole-qa|sole-prod"
    )
    arguments: argparse.Namespace = parser.parse_args()
    if arguments.log:
        logging.basicConfig(filename=arguments.log, level=logging.INFO)
    operation = arguments.operation.lower()
    assert operation in (
        "spark-sql-to-s3-example", "spark-table-to-s3-example", "load"
    )
    if operation == "spark-sql-to-s3-example":
        spark_sql_to_s3_example(
            environment=arguments.environment,
            echo=arguments.echo,
        )
    elif operation == "spark-table-to-s3-example":
        spark_table_to_s3_example(
            environment=arguments.environment,
            echo=arguments.echo,
        )
    elif operation == "load":
        load(environment=arguments.environment, echo=arguments.echo)


# The following is needed in order to be able to execute this CLI using the
# command `python -m sample_etl.__main__
# {OPERATION} {ENVIRONMENT}`, often desirable when there is a potential for
# for conflicting executable names in the system path.
if __name__ == "__main__":
    main()
```

### Spark Airflow DAG Example

Create your Airflow DAG under the sub-directory "./airflow/dags/" in your
project directory. To ensure the file name is unique, it is recommended that
you use a snake-cased variation of your job name + "_etl.py", so for our
example the relative file path would be "./airflow/dags/job_name_etl.py".

```python
import functools
import pendulum  # type: ignore
from airflow.operators import EmrOperator  # type: ignore
from airflow.operators import (  # type: ignore
    SparkSubmitOperator,
)
from datetime import datetime, timedelta
from typing import List, Optional, Union
from airflow import DAG  # type: ignore
from airflow.configuration import conf  # type: ignore
from airflow.exceptions import AirflowConfigException  # type: ignore
from airflow.operators.dummy_operator import DummyOperator  # type: ignore
from airflow.utils.trigger_rule import TriggerRule  # type: ignore

ENVIRONMENT: str
REGION: str
try:
    ENVIRONMENT = conf.get("ae_compute", "env") or ""
    REGION = conf.get("ae_compute", "runtime_region") or ""
except AirflowConfigException:
    # This facilitates static analysis of the DAG
    ENVIRONMENT = "dev"
    REGION = "us-west-2"
    conf.add_section("ae_compute")
    conf.set("ae_compute", "env", ENVIRONMENT)
    conf.set("ae_compute", "runtime_region", REGION)

# The global constant `VERSION` is required for deployment to work correctly
VERSION: str = "0.0.0"

# Include additional email addresses in this list if others need alerted of
# a DAG failure for this job
EMAIL: List[str] = ["reddy.siddartha53@gmail.com"]

PACKAGE_NAME: str = "sample-etl"
CLUSTER_NAME: str = f"{PACKAGE_NAME}-{ENVIRONMENT}-{REGION}"
GROUP = (
    "Engineering"
    if ENVIRONMENT == "prod"
    else "EngineeringNonProd"
)
JOB_ENTRY_POINT: str = (
    f"s3://managed-spark/"
    f"{ENVIRONMENT}/{PACKAGE_NAME}/{VERSION}/"
    f"{PACKAGE_NAME.replace('-', '_')}-{VERSION}-py3-none-any.whl"
)
DOCKER_IMAGE_URI: str = (
    f"1234567.dkr.ecr.{REGION}.amazonaws.com/managed-spark/"
    f"{GROUP.lower()}/{ENVIRONMENT}/{PACKAGE_NAME}:{VERSION}"
)


@functools.lru_cache()
def get_start_date() -> datetime:
    """
    This function returns a start date of two days ago at midnight Pacific
    Time, as written. Adjust as needed.
    """
    return (
        pendulum.now(tz="America/Los_Angeles").replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        - timedelta(days=2)
    ).astimezone(pendulum.tz.UTC)


def get_schedule_interval() -> Optional[str]:
    """
    This function returns a cron-formatted interval string for daily
    recurrence, as written. Adjust as needed.
    """
    interval: Optional[str] = None
    if ENVIRONMENT == "prod":
        start_date: datetime = get_start_date()
        interval = "{} {} * * *".format(start_date.minute, start_date.hour)
    return interval


def get_spark_submit_operator(
    operation: str, dag: DAG, echo: bool = False
) ->  SparkSubmitOperator:
    """
    This function returns an operator for submitting a job to your EMR cluster
    for an "operation", which corresponds to a sub-command
    passed to your packages' entry-point, so `operation="sub-command-name"`
    would execute the command `sample-etl
    sub-command-name {ENVIRONMENT}`.

    Parameters:

    - operation (str): A sub-command
    - dag (airflow.DAG)
    - echo (bool): If `True`, all SQL commands will be output to your EMR logs
    """
    job_arguments: List[str] = [
        operation,
        ENVIRONMENT
    ]
    if echo:
        job_arguments.append("-e")
    spark_operator: SparkSubmitOperator = SparkSubmitOperator(
        task_id=operation,
        jobName=f"{PACKAGE_NAME}-{operation}-{ENVIRONMENT}",
        jobType="spark-python",
        jobEntryPoint=JOB_ENTRY_POINT,
        # The `className` should be the module path you specified for your
        # entry point in your setup.cfg file
        className="sample_etl.__main__",
        jobArguments=job_arguments,
        image=DOCKER_IMAGE_URI,
        hints={
            "eap.compute.job.size": "S",
            "eap.compute.cluster.type": "memory",
            "eap.compute.region": REGION,
            "eap.compute.runtime": "EMR",
            "eap.spark.cluster.name": CLUSTER_NAME,
        },
        dag=dag,
        version="3.0.1",
    )
    # We create a dummy operator for each submissions so that failure of a task
    # causes the DAG to fail, but doesn't prevent the "terminate"
    # EmrOperator from being triggered
    spark_operator >> DummyOperator(task_id=f"{operation}_test", dag=dag)
    return spark_operator


def get_spinup_emr_operator(task_id: str, dag: DAG) -> EmrOperator:
    """
    """
    return EmrOperator(
        dag=dag,
        task_id=task_id,
        group=GROUP,
        classification="platinum",
        cluster_action="spinup",
        queue="airflow",
        cluster_name=CLUSTER_NAME,
        # EMR version 6.2.1 is the most recent version we currently
        # have access to which does not use a Spark versions with JDBC
        # connection issues
        emr_version="6.2.1",
        core_bid_type="ON_DEMAND",
        task_bid_type="SPOT",
        tags=[dict(Key="routable", Value="true")],
        properties=[
            # Set the PySpark python version to 3.*
            dict(
                Classification="spark-env",
                Configurations=[
                    dict(
                        Classification="export",
                        Properties=dict(
                            PYSPARK_PYTHON="python3",
                            PYSPARK_DRIVER_PYTHON="python3",
                        ),
                    )
                ],
            ),
        ],
        applications=["hive", "spark"],
        master_inst_type="r5.xlarge",
        core_inst_type="r5.xlarge",
        num_core_nodes=1,
        num_task_nodes=1,
    )


def get_terminate_emr_operator(task_id: str, dag: DAG) -> EmrOperator:
    return EmrOperator(
        task_id=task_id,
        trigger_rule=TriggerRule.ALL_DONE,
        cluster_action="terminate",
        cluster_name=CLUSTER_NAME,
        dag=dag,
    )


with DAG(
    dag_id="job_name_etl",
    start_date=get_start_date(),
    default_args=dict(
        email=EMAIL,
        email_on_failure=True,
    ),
    schedule_interval=get_schedule_interval(),
) as job_name_etl_dag:
    task: Union[
        EmrOperator,
        SparkSubmitOperator,
        None,
    ] = get_spinup_emr_operator("start", job_name_etl_dag)
    task_id_: str
    echo: bool
    # For the "extract" and "transform" operations, we need lots of executors,
    # but not a lot of memory or processing power for each executor.
    # This is because these operations are making a lot of parallel API
    # requests rather than processing large dataframes.
    for task_id_, echo in (
        ("spark-sql-to-s3-example", False),
        ("spark-table-to-s3-example", False),
        ("load", True),
    ):
        next_task: SparkSubmitOperator = get_spark_submit_operator(
            task_id_,
            job_name_etl_dag,
            echo=echo,
        )
        if task is not None:
            task >> next_task
        task = next_task
    task >> get_terminate_emr_operator("stop", job_name_etl_dag)
```

### Spark Jenkinsfile Example

For an ETL job you will need to modify, minimally, your "deploy" stage steps
from the template default. The template default is for a library, so
distributes your package to Artifactory, whereas we want to deploy our package
to the Managed Spark ECR repository, and do not want to distribute it to
Artifactory.

```groovy
pipeline {
    agent {
        docker {
            image 'docker.com:9001/test-corretto11-python38-spark30'
            args (
                '-ti ' +
                '-u ci ' +
                '-v /var/run/docker.sock:/var/run/docker.sock ' +
                '--network host ' +
                '--uts=host'
            )
        }
    }
    stages {
        stage('install'){
            when {
                anyOf {
                    branch "master"
                    branch "PR-*"
                }
            }
            steps {
                sh "make ci-install"
            }
        }
        stage('test') {
            when {
                anyOf {
                    branch "master"
                    branch "PR-*"
                }
                anyOf {
                    changeset "my_datastore_etl/**"
                    changeset "setup.py"
                    changeset "setup.cfg"
                    changeset "tests/**"
                    buildingTag()
                    expression {
                        return currentBuild.previousBuild == null
                    }
                    expression {
                        !("SUCCESS".equals(currentBuild.previousBuild.result))
                    }
                }
            }
            steps {
                sh 'make test'
            }
        }
        stage('deploy') {
            when {
                branch "master"
                anyOf {
                    changeset "airflow/**"
                    changeset "my_datastore_etl/**"
                    changeset "setup.py"
                    changeset "setup.cfg"
                    changeset "requirements.txt"
                    buildingTag()
                    expression {
                        return currentBuild.previousBuild == null
                    }
                    expression {
                        !("SUCCESS".equals(currentBuild.previousBuild.result))
                    }
                }
            }
            steps {
                // This is where you will need to modify your Jenkinsfile.
                // You can remove PYPI deployment steps, as there is no reason
                // to distribute your package to Artifactory, but instead
                // we need to include these Spark deployment steps.
                sh 'venv/bin/daves-dev-tools spark deploy dev qa'
                sh 'venv/bin/daves-dev-tools airflow deploy dev qa'
                sh 'venv/bin/daves-dev-tools airflow run qa'
                sh 'venv/bin/daves-dev-tools spark deploy prod'
                sh 'venv/bin/daves-dev-tools airflow deploy prod'
            }
        }
    }
    post {
        always {
            sh "python3 -m venv venv"
            sh "venv/bin/pip3 install mail-client"
        }
        success {
            sh (
                "venv/bin/mail-client send " +
                "-t \"\$(git --no-pager show -s --format=%ae ${env.GIT_COMMIT})\" " +
                "-pcp \"app/mydatastore/jenkins/MAIL_ID\" " +
                "-s \"Success - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\" || " +
                "venv/bin/mail-client send " +
                "-t ${env.CHANGE_AUTHOR_EMAIL} " +
                "-pcp \"app/mydatastore/jenkins/MAIL_ID\" " +
                "-s \"Success - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\""
            )
        }
        failure {
            sh (
                "venv/bin/mail-client send " +
                "-t \"\$(git --no-pager show -s --format=%ae ${env.GIT_COMMIT})\" " +
                "-pcp \"app/mydatastore/jenkins/MAIL_ID\" " +
                "-s \"Failure - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\" || " +
                "venv/bin/mail-client send " +
                "-t ${env.CHANGE_AUTHOR_EMAIL} " +
                "-pcp \"app/mydatastore/jenkins/MAIL_ID\" " +
                "-s \"Failure - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\""
            )
        }
        aborted {
            sh (
                "venv/bin/mail-client send " +
                "-t \"\$(git --no-pager show -s --format=%ae ${env.GIT_COMMIT})\" " +
                "-pcp \"app/mydatastore/jenkins/MAIL_ID\" " +
                "-s \"Aborted - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\" || " +
                "venv/bin/mail-client send " +
                "-t ${env.CHANGE_AUTHOR_EMAIL} " +
                "-pcp \"app/mydatastore/jenkins/MAIL_ID\" " +
                "-s \"Aborted - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\""
            )
        }
    }
}
```

## Modules

### [my_datastore_etl.broker](my_datastore_etl/broker.py)

#### Broker

Instances of this class, or more typically sub-classes of this class,
broker exchanges of data between systems and distribute tasks to instances
of [Work](#work) or a [Work](#work) sub-class.

Parameters:

- environment (str): "dev", "qa", or "prod"
- parallelism (int) = None: If this is 0 or `None`, the default
    parallelism for the Spark cluster will be used.
- concurrency (my_datastore_etl.concurrency.Concurrency)
    = my_datastore_etl.concurrency.Concurrency.SPARK
- echo (bool) = False: If `True`, all logging will be printed to the
    console.

#### Work

This class encapsulates work to be performed by individual processes in a
multi-process pool.

Parameters:

- environment (str)
- echo (bool)

### [my_datastore_etl.concurrency](my_datastore_etl/concurrency.py)

#### Concurrency

This class enumerates the types of concurrency supported by this package,
and is primarily used to determine the concurrency model applied to
functions called with `my_datastore_etl.broker.Broker.map` and
`my_datastore_etl.broker.Broker.starmap`:

- `my_datastore_etl.concurrency.Concurrency.NONE`:
  Use sequential processing (no concurrency)
- `my_datastore_etl.concurrency.Concurrency.SPARK`:
  Use Apache Spark distributed processing
- `my_datastore_etl.concurrency.Concurrency.MULTIPROCESSING`:
  Use the python `multiprocessing` module (part of the core library)
  for parallel processing

### [my_datastore_etl.config](my_datastore_etl/config.py)

This module holds public constants for use by this package and dependants.

### [my_datastore_etl.transformer](my_datastore_etl/transformer.py)

This module provides a mechanism for *safely* transforming data into rows of
named tuples with column names and data types matching the data model defined
in [my-datastore-orm](https://github.com/siddartham/my-datastore-orm).

#### Transformer

A base class for transforming source data into (validated) iterables
of named tuples suitable for populating My Data Store's'
Snowflake, Hive/Presto, and PostgreSQL databases.

Iterating over an instance of this class will yield 3-part tuples:

- [0] (str) The table name
- [1] (type) The table ORM class
- [2] (typing.Iterable[tuple]) The results from `SELECT * from
    {SCHEMA}.{TABLE}`, as named tuples

Public Properties:

- session (sqlalchemy.orm.Session): A SQLAlchemy ORM session
  for interacting with the in-memory SQLite database representation of `data`

Initialization Parameters:

- data: If provided, this is passed to `.add()`
- echo (bool): If `True`, all SQL statements are printed to
    `sys.stdout`

### [my_datastore_etl.utilities](my_datastore_etl/utilities.py)

TODO
