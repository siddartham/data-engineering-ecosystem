# sample-datastore-model

[![test](https://github.com/siddartham/data-engineering-ecosystem/my-datastore-orm/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/my-datastore-orm/actions/workflows/test.yml)
[![distribute](https://github.com/siddartham/data-engineering-ecosystem/my-datastore-orm/actions/workflows/distribute.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/my-datastore-orm/actions/workflows/distribute.yml)


This library defines a SQLAlchemy object relational model (ORM) for my datastore

## Additional References

- [Data Dictionary](./dictionary.tsv)

## Install

### Basic Installation

To install this library with all optional extras:

```shell script
pip3 install 'git+https://github.com/siddartham/data-engineering-ecosystem/my-datastore-orm.git[all]'
```

To install this library only for use with sqlite:

```shell script
pip3 install 'git+https://github.com/siddartham/data-engineering-ecosystem/my-datastore-orm.git'
```

Extras available for this package include:

- Database support:

  - snowflake

- Dataframe Utilities:

  - pyspark
  - pyarrow

For example, to install this library for use with Snowflake, and with `pyarrow`
data-frame utilities:

```shell script
pip3 install 'git+https://github.com/siddartham/data-engineering-ecosystem/my-datastore-orm.git[snowflake,pyarrow]'
```

### Development Installation

You will want to clone this repository and install it in editable mode if you
need to:

- Develop or test *this* library, or...
- Initialize or perform schema migrations on one of the Snowflake databases

```shell script
git clone https://github.com/siddartham/data-engineering-ecosystem && \
cd my-datastore-orm && \
make
```

## Updating the ORM

Mappings in this project are organized into modules which match the
schema name in which each reside in Snowflake. Modules starting with
"bcl_" contain "business consumption layer" views.

- common_dimension: Dimension tables shared by more than one logical grouping

Note: This documentation will not cover basic usage of SQLAlchemy's ORM, please
refer to the
[SQLAlchemy ORM documentation](https://docs.sqlalchemy.org/en/latest/orm/) if
you are unfamiliar with the SQLAlchemy ORM library.

### Adding a Snowflake Schema

The only dialect supported by this model for which we want to employ
multiple schemas is Snowflake. In order to create a new Snowflake schema,
you need to:

1. Create a new module under
   [`my_datastore_orm`](my_datastore_orm), named as you
   want the schema to be named, except lowercase (and with the extension ".py",
   of course)
2. Add your module to the imports in
  [`my_datastore_orm.__init__`](my_datastore_orm/__init__.py),
  as well as to `my_datastore_orm.__init__.__all__`.
3. In [`my_datastore_orm.dialects.snowflake.py`](my_datastore_orm/dialects/snowflake.py),
   add the name of your schema to the tuple
   `my_datastore_orm.dialects.snowflake.SCHEMAS`.

### Adding a Table or View

For each table or view, you need to create a mapping class in the module
corresponding to the Snowflake schema in which it will reside. For mappings
which are not intended for Snowflake (see the section below on
[dialect-specific tables and views](#Dialect-Specific-Tables-and-Views)),
choose the module which most closely represents the logical grouping for your
table.

Example:

```python
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
)
from my_datastore_orm.base import Base
from orm_framework import view

class Dimension(Base):
    """
    This class will create a table named "DIMENSION".
    - The schema where this table resides in Snowflake will be inferred
      based on the module in which this class is defined.
    - For all other dialects, this table will land in the default schema,
      or the schema specified in the connection.
    """

    primary_key_column_name = Column(
      "DIMENSION_ID", Integer, primary_key=True
    )


@view.create_as(
    Dimension.__table__.select()
)
class DimensionViewFromSelectable(Base):
    """
    This class will create a view named "DIMENSION_VIEW_FROM_SELECTABLE", which
    acts as a proxy for *TABLE_NAME*.
    """

    dimension_id = Column(
      "DIMENSION_ID", Integer, primary_key=True
    )


@view.create_as(
    "SELECT * FROM DIMENSION"
)
class DimensionViewFromSQL(Base):
    """
    This class will create a view named "DIMENSION_VIEW_FROM_SQL", which
    acts as a proxy for *TABLE_NAME*.
    """

    dimension_id = Column(
      "DIMENSION_ID", Integer, primary_key=True
    )


class Fact(Base):
    """
    This class will create a table named "FACT", with a column named
    "DIMENSION_ID" with a foreign key constraint referencing
    "DIMENSION"."DIMENSION_ID".
    """

    fact_id = Column(
      "FACT_ID", Integer, primary_key=True
    )
    dimension_id = Column(
        "DIMENSION_ID", Integer, ForeignKey(Dimension.dimension_id)
    )
```

All tables in this model are sub-classes of a declarative base defined in
`my_datastore_orm.base.Base`.

Please adhere to the following conventions/guidelines when defining your tables:

- Table names are inferred based on the class name, so you do *not* need to
  include a `__tablename__` property with your mapping class definitions.
  Instead, use CamelCasing for your class names (as described in
  [PEP-8
  ](https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions)).
  Table names will be inferred from the class name, with CamelCasing translated
  to all-uppercase, underscore-separated table names. Where more than two
  uppercase characters occur in a row, acronyms are inferred (as opposed to
  inferring single-character words).

### Dialect Specific Tables and Views

In order to exclude a table from being used for a specific dialect,
you need to create a dictionary attribute on the mapping class named
"__table_args__". In order to exclude this mapping from creating a
corresponding table when this ORM is employed for a dialect, add a key
to the `.__table_args__` dictionary with a name adhering to the pattern
"{dialect_name}_table_name".

Example:

```python
from sqlalchemy import (
    Column,
    Integer,
)
from my_datastore_orm.base import Base

class SnowflakeOnly(Base):
    """
    This class will create a table named "SNOWFLAKE_ONLY".
    - The schema where this table resides in Snowflake will be inferred
      based on the module in which this class is defined.
    - For all other dialects, this table will not be created.
    """
    __table_args__: Dict[str, Any] = dict(
        hive_table_name="",  # Don't use this table in Hive
        postgresql_table_name="",  # Don't use this table in PostgreSQL
        sqlite_table_name="",  # Don't use this table in SQLite
    )

    primary_key_column_name = Column(
      "SNOWFLAKE_ONLY_ID", Integer, primary_key=True
    )
```

### Updating the Data Dictionary

After making any changes to this project, please update the dictionary
by running `make dictionary` in the project's root directory.

## Running Unit Tests

The simplest way to run unit tests locally is with `tox`:

```shell script
git clone\
 https://github.com/siddarthm/my-datastore-orm.git\
 my-datastore-orm
cd ./my-datastore-orm
pip3 install tox  # Install tox
tox  # Run tox in the repository's root directory
```

The `tox.ini` file is currently configured to test against python version 3.6.

## Library

### my_datastore_orm

Each module in this package corresponds to a database schema, except for
`my_datastore_orm.dialects` and `my_datastore_orm.base` (
home for the [declarative base](
https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/basic_use.html
)). Within each module, classes inheriting from the declarative base each
describe a table in the corresponding schema.

Module, class and property names in this package align with their corresponding
schema, table, and column names with the following modifications:

- Module and columns names are lowercase, with words
  separated by underscores, in compliance with [
    PEP-8 guidelines concerning variable names.
  ](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)
  The corresponding schema and column names are *uppercase* variations of the
  same names, in accordance with enterprise
  guidelines.
- Class names utilize "CapWords" casing (camelCasing where the first letter is
  also capitalized) in compliance with
  [PEP-8 guidelines concerning class names](
  https://www.python.org/dev/peps/pep-0008/#class-names).
  In accordance with common practice (and enterprise guidelines), the
  corresponding table names are of uniform casing, with words separated by
  underscores. In accordance with enterprise guidelines, these table names are
  uniformly *uppercase*.

## Command Line Interface

### sqlite

```text
$ my-datastore-orm slite -h
usage: my-datastore-orm sqlite [-h] [-e] [-cf] [-vo] [-ud] [-udo]
                                        [-l LOG] [-ov ONLY_VALIDATE]
                                        command [path]

positional arguments:
  command               create|drop|validate
  path                  The file path where this database will be created

optional arguments:
  -h, --help            show this help message and exit
  -e, --echo            this flag causes all sqlalchemy statements to be
                        printed to `sys.stdout` following compilation
  -cf, --checkfirst     this flag causes `create table` statements to only be
                        executed for tables which do not yet exist
  -vo, --views-only     this flag causes `create database`, `create schema`,
                        and `create view` statements to be executed, but *not*
                        `create table` statements
  -ud, --undeclared     this flag causes tables/views which are undeclared to
                        be dropped (only applicable with the "drop" command)
  -udo, --undeclared-only
                        this flag causes *only* tables/views which are
                        undeclared to be dropped (only applicable with the
                        "drop" command)
  -l LOG, --log LOG     Log output path
  -ov ONLY_VALIDATE, --only-validate ONLY_VALIDATE
                        If provided, only the specified view/table name(s)
                        will be validated
```

### snowflake

```text
$ my-datastore-orm snowflake -h
usage: my-datastore-orm snowflake [-h] [-u USER] [-p PASSWORD]
                                           [-d DATABASE] [-w WAREHOUSE]
                                           [-s SCHEMA] [-r ROLE]
                                           [-a AUTHENTICATOR] [-sn STAGE_NAME]
                                           [-sff STAGE_FILE_FORMAT]
                                           [-su STAGE_URL]
                                           [-ssi STAGE_STORAGE_INTEGRATION]
                                           [-cf] [-e] [-vo]
                                           [-ucp USER_CERBERUS_PATH]
                                           [-pcp PASSWORD_CERBERUS_PATH]
                                           [-wcp WAREHOUSE_CERBERUS_PATH]
                                           [-scp SCHEMA_CERBERUS_PATH]
                                           [-rcp ROLE_CERBERUS_PATH]
                                           [-dcp DATABASE_CERBERUS_PATH]
                                           [-acp AUTHENTICATOR_CERBERUS_PATH]
                                           [-ud] [-udo] [-dusr] [--log LOG]
                                           [-ov ONLY_VALIDATE]
                                           [-ifk IGNORE_FOREIGN_KEY]
                                           [-efcv EXCLUDE_FROM_CACHE_VALIDATION]
                                           command environment

positional arguments:
  command               create|drop|validate
  environment           dev|qa|prod

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  a username with which to authenticate the database
                        connection
  -p PASSWORD, --password PASSWORD
                        a password with which to authenticate the database
                        connection
  -d DATABASE, --database DATABASE
                        the name of a database with which to connect
  -w WAREHOUSE, --warehouse WAREHOUSE
                        the warehouse with which to execute queries
  -s SCHEMA, --schema SCHEMA
                        the name of a schema to use as the default schema
  -r ROLE, --role ROLE  the name of a role to be assumed
  -a AUTHENTICATOR, --authenticator AUTHENTICATOR
                        "externalbrowser" or "https://org.okta.com"if no
                        authenticator is specified, "externalbrowser" will be
                        inferred for human users, and "https://org.okta.com"
                        for applications
  -sn STAGE_NAME, --stage-name STAGE_NAME
                        The (schema-qualified) name of the stage from which S3
                        objects are loaded
  -sff STAGE_FILE_FORMAT, --stage-file-format STAGE_FILE_FORMAT
                        The file format name to use as the default for for the
                        S3 stage
  -su STAGE_URL, --stage-url STAGE_URL
                        The base URL for staging of S3 objects
  -ssi STAGE_STORAGE_INTEGRATION, --stage-storage-integration STAGE_STORAGE_INTEGRATION
                        The name of the integration to use for staged S3
                        objects
  -cf, --checkfirst     this flag causes `create database`, `create schema`,
                        `create view`, and `create table` statements to only
                        be executed for databases/schemas/tables/views which
                        do not yet exist
  -e, --echo            this flag causes all sqlalchemy statements to be
                        printed to `sys.stdout` following compilation
  -vo, --views-only     this flag causes `create database`, `create schema`,
                        and `create view` statements to be executed, but *not*
                        `create table` statements
  -ucp USER_CERBERUS_PATH, --user-cerberus-path USER_CERBERUS_PATH
                        a Cerberus secure data path and key (in the format
                        "secure/data/path/key") pointing to a username with
                        which to authenticate this connection
  -pcp PASSWORD_CERBERUS_PATH, --password-cerberus-path PASSWORD_CERBERUS_PATH
                        a Cerberus secure data path and key (in the format
                        "secure/data/path/key") pointing to a password with
                        which to authenticate this connection
  -wcp WAREHOUSE_CERBERUS_PATH, --warehouse-cerberus-path WAREHOUSE_CERBERUS_PATH
                        a Cerberus secure data path and key (in the format
                        "secure/data/path/key") pointing to the name of a
                        warehouse with which to execute queries
  -scp SCHEMA_CERBERUS_PATH, --schema-cerberus-path SCHEMA_CERBERUS_PATH
                        a Cerberus secure data path and key (in the format
                        "secure/data/path/key") pointing to a schema name
  -rcp ROLE_CERBERUS_PATH, --role-cerberus-path ROLE_CERBERUS_PATH
                        a Cerberus secure data path and key (in the format
                        "secure/data/path/key") pointing to the name of a role
                        to assume
  -dcp DATABASE_CERBERUS_PATH, --database-cerberus-path DATABASE_CERBERUS_PATH
                        a Cerberus secure data path and key (in the format
                        "secure/data/path/key") pointing to the database name
  -acp AUTHENTICATOR_CERBERUS_PATH, --authenticator-cerberus-path AUTHENTICATOR_CERBERUS_PATH
                        a Cerberus secure data path and key (in the format
                        "secure/data/path/key") pointing to the authenticator
                        name
  -ud, --undeclared     this flag causes tables/views which are undeclared to
                        be dropped (only applicable with the "drop" command)
  -udo, --undeclared-only
                        this flag causes *only* tables/views which are
                        undeclared to be dropped (only applicable with the
                        "drop" command)
  -dusr, --dont-use-secondary-roles
                        this flag prevents use of secondary roles
  --log LOG             Log output path
  -ov ONLY_VALIDATE, --only-validate ONLY_VALIDATE
                        If provided, only the specified view/table name(s)
                        will be validated
  -ifk IGNORE_FOREIGN_KEY, --ignore-foreign-key IGNORE_FOREIGN_KEY
                        The name of a foreign key to ignore for validation
                        purposes only (only applicable for the "validation"
                        command)
  -efcv EXCLUDE_FROM_CACHE_VALIDATION, --exclude-from-cache-validation EXCLUDE_FROM_CACHE_VALIDATION
                        The name of one or more tables/views to exclude from
                        query result cache validation, or "*" to exclude all
```

## Initializing Snowflake Databases

Initializing a new Snowflake database *shouldn't* be necessary, however just in
case—below is outlined the procedure for doing so *from an empty database*. If
the database is not empty—you can simply follow the guidelines for [Upgrading
Snowflake Databases](#Upgrading-Snowflake-Databases).

To initialize one of the Snowflake databases first make sure you have
followed the instructions for
[Development Installation](#Development-Installation) and obtained temporary
AWS credentials with `gimme-aws-creds`, then execute one (or all) of the
following commands (depending on which environment you want to initialize):

```shell script
my-datastore-orm snowflake create dev -cf -e
my-datastore-orm snowflake create qa -cf -e
my-datastore-orm snowflake create prod -cf -e
```

If you don't have any migration scripts generated yet, create one:

```shell script
alembic -n snowflake-dev revision -m "initial revision"
```

Once you have created your environment(s), stamp them with the latest alembic
database version by executing one or more of the following command(s):

```shell script
alembic -n snowflake-dev stamp head
alembic -n snowflake-qa stamp head
alembic -n snowflake-prod stamp head
```

## Upgrading Snowflake Databases

Note: You should have already
[cloned and installed this package](#Development-Installation).

When/if you make changes to this package which need to be reflected in the
databases, you will need to create a migration script. It is recommended that
you get a review for database changes before generating a new alembic
migration.

- Create your migration script by executing the following command from the
  project root:

  ```shell script
  make migration
  # alembic -n snowflake-dev revision --autogenerate -m "$(git rev-parse --abbrev-ref HEAD | awk -F / '{print $NF}')"
  ```

  Note: The migration script only needs to be generated against one
  environment, in this case "dev" (indicated by setting the "-n" flag, above,
  to "snowflake-dev").

  You will now find a new (auto-generated) migration script under the directory
  "./alembic/versions/snowflake". This script will often require manual
  editing, so make sure to examine and update the contents before executing
  your upgrades. *Do not delete any pre-existing migration scripts*—these hold
  your version history.

- Execute your upgrade in the "dev" database with the following command:

  ```shell script
  alembic -n snowflake-dev upgrade head
  ```

  If you encounter issues with the upgrade, you CANNOT rollback your changes
  the alembic "downgrade" command unless the upgrade completed successfully.
  You will need to manually revert any partial upgrades.

  Once you have performed all testing and verification required for the "dev"
  environment, merging your changes into the master branch will trigger
  the same upgrades for the QA and prod environments.

  Note: In order to perform the upgrades/downgrades described above, you will
  need the following Active Directory role (which can be requested through
  [IDLocker](https://idlocker.org.com/)):

  - APP.SNOWFLAKE.DEV.SDF_FOUNDATION_ADMIN"
