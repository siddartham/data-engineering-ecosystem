# analytics-etl

[![test](https://github.com/siddartham/data-engineering-ecosystem/analytics-etl/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/analytics-etl/actions/workflows/test.yml)
[![distribute](https://github.com/siddartham/data-engineering-ecosystem/analytics-etl/actions/workflows/distribute.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/analytics-etl/actions/workflows/distribute.yml)

[Development Environment Setup](https://github.com/siddartham/data-engineering-ecosystem/dev-env-setup)
This package provides a common framework for ETL jobs.

## Install

You can install this package

```shell script
pip3 install git+https://github.com/siddartham/data-engineering-ecosystem/analytics-etl[all]
```
## Usage


### CLI


## Modules

### [analytics_etl.broker](./analytics_etl/broker.py)

#### Broker

Instances of this class, or more typically sub-classes of this class,
broker exchanges data between systems and distribute tasks to instances
of [Work](#work) or a [Work](#work) sub-class.

Parameters:


- file_system (file_system_client.base.FileSystem)
- parallelism (int) = None: If this is 0 or `None`, the default
      parallelism for the Spark cluster will be used.
- concurrency (analytics_etl.concurrency.Concurrency)
  = analytics_etl.concurrency.Concurrency.MULTIPROCESSING
- databricks_base (typing.Type[analytics_orm.declarative.Base]|None)
- snowflake_base (typing.Type[analytics_orm.declarative.Base]|None)
- postgresql_base (typing.Type[analytics_orm.declarative.Base]|None)
- postgresql_connection_string (str)
- snowflake_connection_string (str)
- databricks_connection_string (str)
- tables_directory: str = "tables/"
- temp_directory: str = "temp/"
- snowflake_s3_stage_name: str = ""
for writing dataframes to s3, in lieu of the file system root
- started (datetime.datetime|None):
The date and time at which the job started, for bookmarking purposes.
- echo (bool) = False: If `True`, all logging will be printed to the
    console.
- work: Union[Work, Type[Work]] = Work
- consolidate_dont_raise_exceptions ((Exception, ...)) = ():
A tuple of exceptions which should not be raised by the `consolidate`
method, only logged. This should only be used for known local testing
scenarios.

#### Work

This class encapsulates work to be performed by individual processes in a
multi-process pool.

Parameters:

- file_system (file_system_client.base.FileSystem)
- databricks_base (typing.Type[analytics_orm.declarative.Base]|None)
- snowflake_base (typing.Type[analytics_orm.declarative.Base]|None)
- postgresql_base (typing.Type[analytics_orm.declarative.Base]|None)
- postgresql_connection_string (str)
- snowflake_connection_string (str)
- databricks_connection_string (str)
- tables_directory: str = "tables/"
- temp_directory: str = "temp/"
- snowflake_s3_stage_name: str = ""
  for writing dataframes to s3, in lieu of the file system root
- started (datetime.datetime|None):
  The date and time at which the job started, for bookmarking purposes.
- echo (bool) = False: If `True`, all logging will be printed to the
    console.

### [analytics_etl.concurrency](analytics_etl/concurrency.py)

#### Concurrency

This class enumerates the types of concurrency supported by this package,
and is primarily used to determine the concurrency model applied to
functions called with `my_datastore_etl_wrapper.broker.Broker.map` and
`my_datastore_etl_wrapper.broker.Broker.starmap`:

-  `analytics_etl.concurrency.Concurrency.NONE`:
   Use sequential processing (no concurrency)
-  `analytics_etl.concurrency.Concurrency.SPARK`:
   Use Apache Spark distributed processing
-  `analytics_etl.concurrency.Concurrency.MULTIPROCESSING`:
   Use the python `multiprocessing` module (part of the core library)
   for parallel processing
-  `analytics_etl.concurrency.Concurrency.FUTURES`:
   Use the python `concurrent.futures` module (part of the core library)
   for parallel processing

### [analytics_etl.transformer](analytics_etl/transformer.py)

This module provides a mechanism for *safely* transforming data into rows of
named tuples with column names and data types matching the data model defined
in [my-datastore-orm](https://github.com/data-engineering-ecosystem/my-datastore-orm).

#### Transformer

A base class for transforming source data into (validated) iterables
of named tuples suitable for populating Sustainability Analytics'
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
- base (typing.Type[analytics_orm.declarative.Base]):
      A SQLAlchemy ORM declarative base

#### Session
This class wraps a SQLAlchemy ORM Session in order to capture a set
    identifying all classes which have data added/merged in the session

## Updating this Project

If/when you upgrade or add any dependencies, you need to run
`make requirements` before committing (and before testing, even locally, with
tox).

Deployment to Artifactory will occur when your changes are merged into the
"master" branch, however only if you have incremented the version number.

You can increment the version number by changing the **version** parameter in
the `setup()` function call in **setup.py**.

