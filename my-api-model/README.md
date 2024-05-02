# my-api-model

[![test](https://github.com/siddartham/data-engineering-ecosystem/my-api-model/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/my-api-model/actions/workflows/test.yml)
[![deploy](https://github.com/siddartham/data-engineering-ecosystem/my-api-model/actions/workflows/deploy.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/my-api-model/actions/workflows/deploy.yml)


This *library* is an object relational model for the My APIs
database and provides a command line interface for initializing the database.

This *project* also holds the alembic version history for this database.

## Install

### Basic Installation


```shell script
pip3 install
```

### Development Installation

```shell script
git clone\
 https://github.com/siddartham/data-engineering-ecosystem.git
cd data-engineering-ecosystem/my-api-model
make
```

## Running Unit Tests

To run "unit" tests for this package, just run `tox -p all` in the project
root.

## Updating the Model

Mapping classes for this model should go in
`my_api_model.public`, and should inherit from the
declarative base `my_api_model.base.Base`.

Note: This documentation will not cover basic usage of SQLAlchemy's ORM, please
refer to the
[SQLAlchemy ORM documentation](https://docs.sqlalchemy.org/en/latest/orm/) if
you are unfamiliar with the SQLAlchemy ORM library.

### Adding a Table or View

Example:
```python
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
)
from .base import Base
from analytics_orm import view

class Dimension(Base):
    """
    This class will create a table named "DIMENSION".
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

## Command Line Interface

The command-line interface can be used to create the database, or to drop all
tables/views in the database

### PostgreSQL

```text
$ my-api-model postgresql -h
usage: my-api-model postgresql [-h] [-e] [-cf] [-vo]
                                                [-u USER] [-p PASSWORD]
                                                [--host HOST] [--port PORT]
                                                [-d DATABASE]
                                                [-ucp USER_CERBERUS_PATH]
                                                [-pcp PASSWORD_CERBERUS_PATH]
                                                [-hcp HOST_CERBERUS_PATH]
                                                [--port-cerberus-path PORT_CERBERUS_PATH]
                                                [-dcp DATABASE_CERBERUS_PATH]
                                                [-ud] [-udo]
                                                command environment

positional arguments:
  command               create|drop
  environment           dev|qa|prod

optional arguments:
  -h, --help            show this help message and exit
  -e, --echo            this flag causes all sqlalchemy statements to be
                        printed to `sys.stdout` following compilation
  -cf, --checkfirst     this flag causes `create database`, `create schema`,
                        `create view`, and `create table` statements to only
                        be executed for databases/schemas/tables/views which
                        do not yet exist
  -vo, --views-only     this flag causes `create database`, `create schema`,
                        and `create view` statements to be executed, but *not*
                        `create table` statements
  -u USER, --user USER  a username with which to authenticate the database
                        connection
  -p PASSWORD, --password PASSWORD
                        a password with which to authenticate the database
                        connection
  --host HOST           the hostname of the database server
  --port PORT           the port on which the database is being served
  -d DATABASE, --database DATABASE
                        the database name
  -ucp USER_CERBERUS_PATH, --user-cerberus-path USER_CERBERUS_PATH
                        a Cerberus secure data path and key (in the format
                        "secure/data/path/key") pointing to a username with
                        which to authenticate this connection
  -pcp PASSWORD_CERBERUS_PATH, --password-cerberus-path PASSWORD_CERBERUS_PATH
                        a Cerberus secure data path and key (in the format
                        "secure/data/path/key") pointing to a password with
                        which to authenticate this connection
  -hcp HOST_CERBERUS_PATH, --host-cerberus-path HOST_CERBERUS_PATH
                        a Cerberus secure data path and key (in the format
                        "secure/data/path/key") pointing to the hostname of
                        the database server
  --port-cerberus-path PORT_CERBERUS_PATH
                        a Cerberus secure data path and key (in the format
                        "secure/data/path/key") pointing to the port on which
                        the database is served
  -dcp DATABASE_CERBERUS_PATH, --database-cerberus-path DATABASE_CERBERUS_PATH
                        a Cerberus secure data path and key (in the format
                        "secure/data/path/key") pointing to the database name
  -ud, --undeclared     this flag causes tables/views which are undeclared to
                        be dropped (only applicable with the "drop" command)
  -udo, --undeclared-only
                        this flag causes *only* tables/views which are
                        undeclared to be dropped (only applicable with the
                        "drop" command)
```

### SQLite

```text
$ my-api-model sqlite -h
usage: my-api-model sqlite [-h] [-e] [-cf] [-vo] [-ud] [-udo]
                                            command [path]

positional arguments:
  command               create|drop
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
```

## Initializing the Aurora PostgreSQL Databases

Initializing a new instance of the PostgreSQL database *shouldn't* be necessary,
however just in case—below is outlined the procedure for doing so *from an
empty database*. If the database is not empty—you can simply follow the
guidelines for [Upgrading the Aurora PostgreSQL Databases
](#Upgrading-the-Aurora-PostgreSQL-Databases).

To initialize one of the databases, first make sure you have [cloned
this repository and installed it with the [dev]
option](#Development-Installation) and obtained temporary AWS credentials with
`gimme-aws-creds`, then execute one (or all) of the following
commands (depending on which environment you want to initialize):

```shell script
my-api-model postgresql create dev -cf -e
my-api-model postgresql create qa -cf -e
my-api-model postgresql create prod -cf -e
```

If you don't have any migration scripts generated yet, create one:

```shell script
alembic -n postgresql-dev revision -m "initial revision"
```

Once you have created your environment(s), stamp them with the latest alembic
database version by executing one or more of the following command(s):

```shell script
alembic -n postgresql-dev stamp head
alembic -n postgresql-qa stamp head
alembic -n postgresql-prod stamp head
```

## Upgrading the Aurora PostgreSQL Databases

Note: You should have already [cloned this repository and installed it with the
[all] option](#Development-Installation).

When/if you make changes to this package which need to be reflected in the
databases, you will need to create a migration script.

- Create your migration script by executing the following command from the
  project root:

  ```shell script
  alembic -n postgresql-dev revision --autogenerate -m "Description of changes"
  ```

  Note: The migration script only needs to be generated against one environment,
  in this case "dev" (indicated by setting the "-n" flag, above, to
  "postgresql-dev").

  You will now find a new (auto-generated) migration script under the directory
  "./alembic/versions/postgresql". This script will often require manual editing,
  so make sure to examine and update the contents before executing your
  upgrades. *Do not delete any pre-existing migration scripts*—these hold
  your version history.

- Execute your upgrade in the "dev" database with the following command:

  ```shell script
  alembic -n postgresql-dev upgrade head
  ```

  If you encounter issues with the upgrade, you can rollback your changes with
  the alembic "downgrade" command:

  ```shell script
  alembic -n postgresql-dev downgrade -1
  ```

  Once you have performed all testing and verification required for the "dev"
  environment, merging your changes into the main branch will trigger
  the same upgrades for the QA and prod environments.

  Note: In order to perform the upgrades/downgrades described above, you will
  need one of the following Active Directory role (which can be requested
  through [IDLocker](https://idlocker.my.com/)):

  - App.Digital.Ngap2.SustainabilityEngineering.Users
  - App.Digital.Ngap2.SustainabilityEngineeringNonProd.Users
  - Application.AWS.Nike.1234567.AdminRole
  - Application.AWS.Nike.1234567.PowerRole

## Connecting to an Environment's Database

```python
# TODO: Please provide examples!
```

## Querying the Database

```python
# TODO: Please provide examples!
```

## Updating this Project

If/when you upgrade or add any dependencies, you need to run
`make requirements` before committing (and before testing, even locally, with
tox).

Deployment to Artifactory will occur when your changes are merged into the
"main" branch, however only if you have incremented the version number.

You can increment the version number by changing the **version** parameter in
the `setup()` function call in **setup.py**.
