## Data Engineering Ecosystem

### Sub Repo Status

| Index  |             package              |                                                            Next Work |                                                                                                                                                                                                                                                                        Things to Learn |
|:------:|:--------------------------------:|---------------------------------------------------------------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| **1**  |         `dev-env-setup`          |                                                                      |                                                                                                                                                                                                                     Instructions to setup development environment in the local system. |
| **2**  |    `python-package-template`     | Fix Regex to accept all package name types, right now it errors out. |                                                                                                                                                                                                                                          A cookiecutter template for python libraries. |
| **3**  |           `dev-tools`            |                   Add support for all the operations. Read the code. |                                                                                                                                                                                              Tools needed in workflow - ex: distribute to pypi, deploy to airflow, trigger airflow etc |
| **4**  |       `cerberus-assistant`       |                                                       Read the code. |                                            A user friendly cerberus wrapper, to use in all places where authentication is needed by accessing secrets from cerberus SDB(secure deposit box). ex: To access API client secrets, authenticate for snowflake, databricks, artifactory etc |
| **5**  |          `mail-client`           |                                                       Read the code. |                                                                                                                                                                                                     This package is a python library and CLI providing simple SMTP email capabilities. |
| **6**  |       `docker-utiltities`        |                                                                      |                                                                                                                                                                                                         A cli tool to build and distribute docker images and check if an image exists. |
| **7**  |     `sample-api-client-sdks`     |                                                                      |                                            This folder explores different ways of building type validated client SDKs for APIs in different scenarios such as having no OpenAPI schema provided or inaccurate OpenAPI schema using `oapi`, `sob`, `openapi-core` and other frameworks. |
| **8**  |         `analytics-orm`          |                                                                      |                                                                                    This package defines a declarative base and related utilities for defining a SQLAlchemy ORM (object relational model) which is compatible with Hive, Databricks, Snowflake, PostgreSQL, and SQLite. |
| **9**  |         `analytics-etl`          |                                                                      |                                                                                                                                                                                                                                 This package provides a common framework for ETL jobs. |
| **10** |       `file-system-client`       |                                                                      |                                                                                                                                                                                                        A common framework for interfacing with cloud(s3, dbfs) and local file systems. |
| **11** |        `my-datestore-etl`        |                                                                      |                                                                                                          This package provides a common framework for My DataStore's "Extract, Transform and Load" (ETL) jobs, setting up the right permissions and defaults specific to my datastore. |
| **12** |       `my-datestore-model`       |                                                                      |                                                                                                                                                                   This library defines a SQLAlchemy object relational model (ORM) for my datastore in snowflake/databricks delta lake. |
| **13** |    `my-datestore-validation`     |                                                                      |                                                                                                                                                    This package performs validations against the databases defined in `my-datastore-model` stored in snowflake/ databricks delta lake. |
| **14** |          `sample-etls`           |                                                                      | This folder provides sample ETLs, that use `my-datastore-etl` framework to Extract from sources(tabular or API or files), transforms data and loads data to data store(snowflake, delta lake) using `my-datastore-model` ORM classes and cloud file system using `file-system-client`. |
| **15** | `my-materialize-snowflake views` |                                                                      |                                                                                                                                 This package triggers queries in snowflake and materialize the results as BCL objects, for transformations that doesn't warrant Spark Transformations. |


### Fundamental Questions in building a Data Engineering environment?
* Why and How to build a common file-system interface to interact with databricks file system, local file system, s3 etc. ? - `file-system-client`
* Why and How to build an ORM framework - internal mechanics of ORM ? - `analytics-orm`
* Why and How to build an ORM model for your database, to set urls, permissions? - `my-datastore-model`
* Why and How to build an ETL framework? - `analytics-etl`
* Why and How to build an ETL wrapper for your team, to set permissions? - `my-datastore-etl`
* How to build an ETL based on framework? - `sample-etl`
* Why and How to write a Client SDK, what is the need for `oapi`, instead of `openapi-codegen`, `openapi-core`?
* How to use metaprogramming, abstract base classes, decorators, hooks to build tools and packages ?  ex: client generation, foundational libraries, class generation


### Data Engineering Foundational Libraries
The idea is to have a data engineering ecosystem that is easy to use and maintain. 


An ideal Data Engineering ecosystem should enable the following:
1. Develop platform agnostic data pipelines 
   * To avoid Vendor Lock-in and high cost of migration across platforms.
2. Automated Schema Management across data stores, environments to avoid schema drift
   * To avoid schema drift across different environments and data stores. 
3. Automated Data Quality Checks to ensure data quality and integrity.


As a part of the efforts to avoid **vendor lock-in** & **schema drift** and maintain **data quality**, we need the following abilities:

1. Ability to interact with different file systems using an uniform interface. 
   * When the file system changes, the code that interacts with file systems should not change beyond parameters.
2. Ability to maintain schema across different environments(dev, qa, prod) and data stores(hive, snowflake, databricks) with a same code. 
   * When the data store software changes, the code that maintains schema should not change.
   * There should not be schema drift across different environments.
3. Using Above two abilities, develop an Ability to perform ETL across different processing paradigms(multi-threaded vs spark) and different file systems and data stores with a uniform interface.
   * A uniform interface to perform ETL across different processing paradigms, file systems and data stores.
4. Ability to perform data quality checks across different data stores with a uniform interface.


Thus, we need to have the following packages:

1. `file-system-client` - provides an uniform interface to access files from different file systems, dbfs, s3, local file system
   * This is wrapper over `boto3`(for S3) and `localstack-client`(for local testing)
2. `analytics-orm` - provides a declarative way to define the schema of the databases across different data stores and environments.
   * This is a wrapper over sqlalchemy, to build a declarative base class for ORM classes.
   * Provides wrappers to connectors to different data stores & computes
     * `psycopg2` for postgres
     * `pyhive[hive,presto,sqlalchemy]` for Hive, Presto
     * `snowflake-sqlalchemy` for Snowflake
     * `databricks-sql-connector` for Databricks
     * `pyspark` for Spark
     * `pyarrow`, `pandas` for multi-threaded processing, API extraction
     * `cerberus-python-client` for pulling secrets from cerberus, for testing connections with data stores.
3. `analytics-etl` - package provides a common framework for "Extract, Transform and Load" (ETL) jobs - using multi processing and pyspark patterns to process data
   * This depends on `file-system-client[s3]` and `analytics-orm[pyarrow]`
4. `data-quality-framework` - provides a common framework for data quality checks.


Above 4 foundational libraries - that can used by any company, any team to build their own data engineering ecosystem.


### Data Store Wide Libraries(i.e org specific libraries)
Using foundational libraries, we can build team/org specific data engineering ecosystem, for etl configuration and interface management, host schema for the org, data quality management for the org etc.

Above 3 functionalities can be achieved by 3 packages.

1. `my-datastore-model` - Hosting schema of your data store(using analytics-orm base class), across different environments, different data stores(Hive, Delta Lake, Snowflake etc).
2. `my-datastore-etl` - a wrapper over `analytics-etl` to provide a common interface for all ETLs over your data stores and file systems.
3. `my-datastore-data-quality` - This package provides an example of how to use the data-quality-framework to perform data quality checks


### Example ETL to load objects to Data Store
1. `sample-etl` - A sample ETL provides an example of how to use the `my-datastore-etl` and `my-datastore-model` to process data and load data

### Attribute Naming Standards
`attribute-name-validator` - This package provides a tool for attribute name validation against the naming standards.

### Miscellaneous Libraries/Folders

1. `cerberus-assistant` - to retrieve secrets from cerberus vault
2. `docker-utilties` - to publish docker images
3. `mail-client` - a CLI & library to send updates as mails
4. `dev-env-setup` - instructions to setup development environment


### Current Status

#### Development Setup & Tools
- [x] `dev-tools`  - common CLI to interact with airflow, managed spark, docker, pypi
- [x] `dev-env-setup` - set up development environment
- [x] `python-package-template` - template for python packages

#### Foundational Libraries
- [x] `file-system-client`
- [x] `analytics-orm`
- [x] `analytics-etl`
- [x] `my-datastore-validation` - can factor out common code to `data-quality-framework`

#### Data Store Wide Libraries
- [x] `my-datastore-model`
- [x] `my-datastore-etl`

#### Example ETL to load objects to Data Store
- [x] `my-sample-etl`

#### Attribute Naming Standards
- [x] `attribute-name-validator`
