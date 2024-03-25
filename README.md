## Data Engineering Ecosystem


### Fundamental Questions in building a Data Engineering environment?
* Why and How to build a common file-system interface to interact with databricks file system, local file system, s3 etc. ? 
* Why and How to build an ORM framework - internal mechanics of ORM ? 
* Why and How to build an ORM model for your database, to set urls, permissions? 
* Why and How to build an ETL framework? 
* Why and How to build an ETL wrapper for your team, to set permissions? 
* How to build an ETL based on framework? 
* Why and How to write a Client SDK, what is the need for oapi, instead of openapi-codegen? 
* How to use metaprogramming, abstract base classes, decorators, hooks to build tools and packages ?


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
2. `orm-framework` - provides a declarative way to define the schema of the databases across different data stores and environments.
   * This is a wrapper over sqlalchemy, to build a declarative base class for ORM classes.
   * Provides wrappers to connectors to different data stores & computes
     * `psycopg2` for postgres
     * `pyhive[hive,presto,sqlalchemy]` for Hive, Presto
     * `snowflake-sqlalchemy` for Snowflake
     * `databricks-sql-connector` for Databricks
     * `pyspark` for Spark
     * `pyarrow`, `pandas` for multi-threaded processing, API extraction
     * `cerberus-python-client` for pulling secrets from cerberus, for testing connections with data stores.
3. `etl-framework` - package provides a common framework for "Extract, Transform and Load" (ETL) jobs - using multi processing and pyspark patterns to process data
   * This depends on `file-system-client[s3]` and `orm-framework[pyarrow]`
4. `data-quality-framework` - provides a common framework for data quality checks.


Above 4 foundational libraries - that can used by any company, any team to build their own data engineering ecosystem.


### Data Store Wide Libraries(i.e org specific libraries)
Using foundational libraries, we can build team/org specific data engineering ecosystem, for etl configuration and interface management, host schema for the org, data quality management for the org etc.

Above 3 functionalities can be achieved by 3 packages.

1. `my-datastore-orm` - Hosting schema of your data store(using orm-framework base class), across different environments, different data stores(Hive, Delta Lake, Snowflake etc).
2. `my-datastore-etl-wrapper` - a wrapper over `etl-framework` to provide a common interface for all ETLs over your data stores and file systems.
3. `my-datastore-data-quality` - This package provides an example of how to use the data-quality-framework to perform data quality checks



### Example ETL to load objects to Data Store
1. `sample-etl` - A sample ETL provides an example of how to use the `my-etl-wrapper` to process data

### Attribute Naming Standards
`attribute-name-validator` - This package provides a tool for attribute name validation against the naming standards.



### Current Status

#### Development Setup & Tools
- [x] `dev-tools`  - common CLI to interact with airflow, managed spark, docker, pypi
- [x] `dev-env-setup` - set up development environment
- [x] `python-package-template` - template for python packages

#### Foundational Libraries
- [x] `file-system-client`
- [x] `orm-framework`
- [x] `etl-framework`
- [x] `data-quality-framework`

#### Data Store Wide Libraries
- [x] `my-datastore-orm`
- [x] `my-datastore-etl-wrapper`
- [ ] `my-datastore-data-quality`

#### Example ETL to load objects to Data Store
- [x] `my-sample-etl`

#### Attribute Naming Standards
- [x] `attribute-name-validator`