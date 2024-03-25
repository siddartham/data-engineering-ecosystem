# orm-framework

[![test](https://github.com/siddartham/orm-framework/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/orm-framework/actions/workflows/test.yml)
[![distribute](https://github.com/siddartham/orm-framework/actions/workflows/distribute.yml/badge.svg)](https://github.com/siddartham/orm-framework/actions/workflows/distribute.yml)

This library defines a declarative base and related utilities for defining
a SQLAlchemy ORM (object relational model) which is compatible with Hive, Databricks,
Snowflake, PostgreSQL, and SQLite.

[Setting up your Development Environment](https://github.com/siddartham/development-environment-setup)
## Installation

To install this library with all optional utilities:

```shell script
pip3 install git+https://github.com/siddartham/orm-framwork.git[all]
```

To install this library only for use with sqlite:

```shell script
pip3 install git+https://github.com/siddartham/orm-framwork.git
```

### Clone and Install

You will want to clone this repository and install it in editable mode if you
need to develop, test, or distribute *this* library.

```shell script
git clone\
 https://github.com/siddartham/orm-framework.git\
 orm-framework
cd ./orm-framework
make
```

### CLI

#### orm-framework spark install-snowflake-jdbc-driver

This command will add a JDBC driver for Snowflake to your
Spark extra class paths, facilitating use of a Snowflake JDBC connection
with Spark.


```shell
$ orm-framework spark install-snowflake-jdbc-driver -h
usage: orm-framework spark install-snowflake-jdbc-driver [-h]

Configure Spark to load and use a Snowflake JDBC driver

optional arguments:
  -h, --help  show this help message and exit
```
## Modules

### orm_framework.declarative

This module defines a declarative base and common types for all models in this
library

#### declarative_base

This function wraps `sqlalchemy.ext.declarative.declarative_base`

#### as_declarative

This function is a class decorator for
`orm_framework.declarative.declarative_base` which provides a
syntactical shortcut to the `cls` argument sent to
`orm_framework.declarative.declarative_base`, allowing the
base class to be converted in-place to a "declarative" base. For example:

```
from sqlalchemy import Integer
from orm_framework.declarative import as_declarative

@as_declarative()
class Base:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class MyMappedClass(Base):

    id = Column(Integer, primary_key=True)
```

All keyword arguments passed to
`orm_framework.declarative.as_declarative` are passed along to
`orm_framework.declarative.declarative_base`.

### orm_framework.utilities

#### lru_cache

Least-recently-used cache decorator.

If *maxsize* is set to None, the LRU features are disabled and the cache
can grow without bound.

If *typed* is True, arguments of different types will be cached separately.
For example, f(3.0) and f(3) will be treated as distinct calls with
distinct results.

Arguments to the cached function must be hashable.

View the cache statistics named tuple (hits, misses, maxsize, currsize)
with f.cache_info().  Clear the cache and statistics with f.cache_clear().
Access the underlying function with f.__wrapped__.

See:  http://en.wikipedia.org/wiki/Cache_algorithms#Least_Recently_Used

#### patch_urllib_parse_uses

This function add a schema/protocol to `urllib.parse.uses_relative`,
`urllib.parse.uses_netloc`, and `urllib.parse.uses_params` in order to
allow `urllib.parse.urljoin` to be used with URLs having this protocol.

#### get_class_table_name

Converts a CamelCasedClassName to an UNDERSCORE_SEPARATED_TABLE_NAME.

>>> print(get_class_table_name('theBirdsAndTheBees'))
the_birds_and_the_bees

>>> print(get_class_table_name('FYIThisIsAnAcronym'))
fyi_this_is_an_acronym

>>> print(get_class_table_name('in'))
in_

>>> print(get_class_table_name('id'))
id_

>>> print(get_class_table_name('one2one'))  # No change needed
one2one

>>> print(get_class_table_name('One2One'))
one_2_one

>>> print(get_class_table_name('@One2One'))
one_2_one

#### get_class_qualified_name

>>> from orm_framework import declarative
>>> print(get_class_qualified_name(declarative.Base))
orm_framework.declarative.Base

#### get_bind_dialect_name

Given a connectable `bind` (connection or engine) object, return the name
of the dialect used (for example: "sqlite", "snowflake",
or "postgresql").

#### apply_conditional_defaults

This function decorates another function in order to apply a set of
*default* keyword or positional/keyword argument values based on the
return of a `condition` function, which should accept the same parameters
as the wrapped function.

For example:

```python
from typing import Any
from orm_framework.utilities import apply_conditional_defaults
from orm_framework.postgresql import get_connection_url


def is_qa(
    environment: str, *args: Any, **kwargs: Any
) -> bool:
    return environment.lower() == "qa"


@apply_conditional_defaults(
    is_qa,
    user="qa-user",
    password="qa-password",
    host="qa-host",
    database="qa"
)
def get_environment_connection_string(
    environment: str,
    user: str = "",
    password: str = "",
    host: str = "",
    port: int = "",
    database: str = "",
    schema: str = ""
) -> str:
    return str(get_connection_url(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database,
        schema=schema
    ))
```

For the above example, `get_environment_connection_string("qa")` would
return "postgresql://qa-user:qa-password@qa-host:5432/qa?schema=public".

This decorator can be chained in order to apply defaults for more than one
condition.

#### apply_environment_defaults

This function decorates another function in order to apply a set of
*default* keyword or positional/keyword argument values when the value for
the `environment` argument is equal to that passed to the decorator.

For example:

```python
from orm_framework.utilities import apply_environment_defaults
from orm_framework.postgresql import get_connection_url


@apply_environment_defaults(
    "qa",
    user="qa-user",
    password="qa-password",
    host="qa-host",
    database="qa"
)
def get_environment_connection_string(
    environment: str,
    user: str = "",
    password: str = "",
    host: str = "",
    port: int = "",
    database: str = "",
    schema: str = ""
) -> str:
    return str(get_connection_url(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database,
        schema=schema
    ))
```

For the above example, `get_environment_connection_string("qa")` would
return "postgresql://qa-user:qa-password@qa-host:5432/qa?schema=public".

This decorator can be chained in order to apply defaults for multiple
environments.

#### apply_role_defaults

This function decorates another function in order to apply a set of
*default* keyword or positional/keyword argument values when the value for
the `role` argument is equal to that passed to the decorator.

For example:

```python
from orm_framework.utilities import apply_role_defaults
from orm_framework.postgresql import get_connection_url


@apply_role_defaults(
    "default-role",
    user="qa-user",
    password="qa-password",
    host="qa-host",
    database="qa"
)
def get_role_connection_string(
    role: str = "",
    user: str = "",
    password: str = "",
    host: str = "",
    port: int = "",
    database: str = "",
    schema: str = ""
) -> str:
    return str(get_connection_url(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database,
        schema=schema
    ))
```

For the above example, `get_role_connection_string("qa-user")`
would return
"postgresql://qa-user:qa-password@qa-host:5432/qa?schema=public".

This decorator can be chained in order to apply defaults for multiple
users, environments, or other conditions.

#### update_all_dialects_construct_arguments

Update the `.construct_arguments` property for all supported dialects.

#### update_dialect_construct_arguments

This function updates construct arguments for the specified `dialect`,
or raises a `sqlalchemy.exc.NoSuchModuleError`.

#### is_jenkins_bmx

#### is_ci

#### is_current_user_human#### 

### orm_framework.pyarrow

#### get_schema_from_mapping

Given a sub-class of `orm_framework.base.Base`, return a
corresponding instance of `pyarrow.Schema` for use in writing parquet
files with pandas + pyarrow.

### orm_framework.spark

#### get_data_frame_with_unique_primary_keys

This function takes a data frame and a sub-class of
`orm_framework.base.Base` and returns a data frame
where there is only one record for each primary key, as defined by
`table`.

#### get_struct_type_from_mapping

This function obtains an instance of `pyspark_sql_types.StructType`
generated from a table ORM class.

### orm_framework.snowflake

#### get_connection_url

This function assembles and returns a snowflake connection string.

Parameters:

- **user** (str) = "": A username with which to authenticate
- **password** (str) = "": A password with which to authenticate
- **database** (str) = ""
- **warehouse** (str) = ""
- **schema** (str) = "INFORMATION_SCHEMA": A schema name.
- **role** (str) = "ALL": A Snowflake role to be assumed, or "ALL" (the
  default).
- **authenticator** (str) = "": Either "https://org.okta.com" or
  "externalbrowser", if provided, otherwise this will be determined to
  be "externalbrowser" for human users, and "https://org.okta.com" for
  service accounts (GIDs).

...the following parameters are a path + key to a cerberus secret stored
in a [vault](https://cerberus.cloud.com). For
example: "app/siddartham/snowlake-prod/password".

- **user_cerberus_path** (str) = ""
- **password_cerberus_path** (str) = ""
- **database_cerberus_path** (str) = ""
- **warehouse_cerberus_path** (str) = ""
- **schema_cerberus_path** (str) = ""
- **role_cerberus_path** (str) = ""
- **authenticator_cerberus_path** (str) = ""

#### create_engine

#### create_all

#### parse_arguments

Parse CLI arguments and return the resulting instance of
`argparse.Namespace`.

Parameters:

- prog (str): The CLI command or command + sub-command
  triggering this function. For example:
  "my-datastore-orm snowflake".
- environments ([str]) = ("dev", "qa", "prod"): The environment names
  to consider valid
- roles ([str]) = (): The roles to consider valid. If none are provided,
  any value is considered valid for this argument

This function returns a `Namespace` object with the following
properties:

- command (str): The sub-sub-command to perform (create).
- environments ([str]): A list of one or more environments.
- echo (bool): If `True`, sqlalchemy statements should be printed
  to `sys.stdout` on statement compilation.

### orm_framework.postgresql

#### get_connection_url

This function assembles a PostgreSQL connection string.

Parameters:

- **user** (str) = "postgres"
- **password** (str) = ""
- **host** (str) = "localhost"
- **port** (int) = 5432
- **database** (str) = "postgres"

...the following parameters are a path + key to a cerberus secret stored
in a [vault](https://cerberus.cloud.com).. For
example: "app/siddartham/postgres-prod/password".

- **user_cerberus_path** (str) = ""
- **password_cerberus_path** (str) = ""
- **host_cerberus_path** (str) = ""
- **port_cerberus_path** (str) = ""
- **database_cerberus_path** (str) = ""

#### create_engine

Create a SQLAlchemy engine for connecting to a PostgreSQL
database.

Parameters:

- **user** (str) = "postgres"
- **password** (str) = ""
- **host** (str) = "localhost"
- **port** (int) = 5432
- **database** (str) = "postgres"
- **echo** (bool)

...the following parameters are a path + key to a cerberus secret stored
in a [vault](https://cerberus.cloud.com). For
example: "app/siddartham/postgres-prod/password".

- **user_cerberus_path** (str) = ""
- **password_cerberus_path** (str) = ""
- **port_cerberus_path** (str) = ""
- **database_cerberus_path** (str) = ""


Please note that this connection is cached and re-used in subsequent calls
referencing the same environment, so  maintaining a persistent reference
within the client application is not necessary.

#### create_all

Create the database, schemas, views and tables.

Parameters:

- **declarative_base** (type): A declarative base class created
  using `orm_framework.declarative.declarative_base()`
  or a class decorated with
  `@orm_framework.declarative.declarative_base()`.
- **user** (str) = "postgres"
- **password** (str) = ""
- **host** (str) = "localhost"
- **port** (int) = 5432
- **database** (str) = "postgres"

...the following parameters are a path + key to a cerberus secret stored
in a [vault](https://cerberus.cloud.com). For
example: "app/siddartham/postgres-prod/password".

- **user_cerberus_path** (str) = ""
- **password_cerberus_path** (str) = ""
- **port_cerberus_path** (str) = ""
- **database_cerberus_path** (str) = ""

#### parse_arguments

Parse postgresql CLI arguments and return the resulting instance of
`argparse.Namespace`.

Parameters:

- prog (str): The CLI command or command + sub-command
  triggering this function. For example:
  "my-datastore-orm postgresql".
- environments ([str]) = ("dev", "qa", "prod"): The environment names
  to consider valid

This function returns a `Namespace` object with the following
properties:

- command (str): The sub-sub-command to perform (create).
- environments ([str]): A list of one or more environments.
- echo (bool): If `True`, sqlalchemy statements should be printed
  to `sys.stdout` on statement compilation.

### orm_framework.sqlite

#### get_connection_url

Get a connection string for a SQLite database located at `path`.

#### create_engine

Create a SQLAlchemy engine for connecting to (or creating) a SQLite
database located at `path`.

Parameters:

- **path** (str): The file path where the database is, or will be, located.
- **echo** (bool)

Please note that this connection is cached and re-used in subsequent calls
referencing the same environment, so  maintaining a persistent reference
within the client application is not necessary.

#### create_all

Create the database and all schemas & tables in the database.

#### parse_arguments

Parse sqlite CLI arguments and return the resulting instance of
`argparse.Namespace`. This function is intended to parse
arguments for a sub-command under `parent_command`.

Parameters:

- prog (str): The CLI command or command + sub-command
  triggering this function. For example:
  "my-datastore-orm sqlite".

This function returns a `Namespace` object with the following
properties:

- command (str): The sub-sub-command to perform (create).
- path (str): The file path where the database should be created.
- echo (bool): If `True`, sqlalchemy statements should be printed
  to `sys.stdout` on statement compilation.

#### main

This function parses command-line arguments and executes a function
based on the input using the provided `declarative_base`. The program
name (`prog`) is used for reference in the CLI's `--help` documentation.

Parameters:

- declarative_base (type)
- prog (str) = "": The command or command + sub-command triggering this
  function. For example: "my-datastore-orm create".

## Running Unit Tests

The simplest way to run unit tests locally is with `tox`:
```shell script
git clone\
 https://github.com/siddartham/orm-framework.git\
 orm-framework
cd ./orm-framework
pip3 install tox  # Install tox
tox  # Run tox in the repository's root directory
```

The `tox.ini` file is currently configured to test against python version 3.6
only.
