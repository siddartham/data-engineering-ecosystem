# my-datastore-validation

[![test](https://github.com/siddartham/data-engineering-ecosystem/my-datastore-validation/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/my-datastore-validation/actions/workflows/test.yml)
[![distribute](https://github.com/siddartham/data-engineering-ecosystem/my-datastore-validation/actions/workflows/distribute.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/my-datastore-validation/actions/workflows/distribute.yml)

[Development Environment Setup](https://github.com/siddartham/data-engineering-ecosystem/dev-env-setup)

This package performs validations against the
databases defined in [my-datastore-orm
](https://github.com/siddartham/data-engineering-ecosystem/my-datastore-validation).

## Install

### Basic Installation

You can install this package from PYPI:

```shell script
pip3 install my-datastore-validation
```

### Development Installation

```shell script
git clone https://github.com/siddartham/data-engineering-ecosystem/my-datastore-validation.git
cd my-datastore-validation
make
```

## Usage

### CLI

#### my-datastore-validation snowflake

```text
$ my-datastore-validation snowflake -h
usage: my-datastore-validation snowflake [-h] [-u USER] [-p PASSWORD]
                                                [-d DATABASE] [-w WAREHOUSE]
                                                [-s SCHEMA] [-r ROLE]
                                                [-a AUTHENTICATOR] [-e]
                                                [-ucp USER_CERBERUS_PATH]
                                                [-pcp PASSWORD_CERBERUS_PATH]
                                                [-wcp WAREHOUSE_CERBERUS_PATH]
                                                [-scp SCHEMA_CERBERUS_PATH]
                                                [-rcp ROLE_CERBERUS_PATH]
                                                [-dcp DATABASE_CERBERUS_PATH]
                                                [-acp AUTHENTICATOR_CERBERUS_PATH]
                                                [--log LOG]
                                                [-ov ONLY_VALIDATE]
                                                [-ifk IGNORE_FOREIGN_KEY]
                                                [-efcv EXCLUDE_FROM_CACHE_VALIDATION]
                                                environment

positional arguments:
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
                        "externalbrowser" or "https://my.okta.com"if no
                        authenticator is specified, "externalbrowser" will be
                        inferred for human users, and "https://my.okta.com"
                        for applications
  -e, --echo            this flag causes all sqlalchemy statements to be
                        printed to `sys.stdout` following compilation
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

#### my-datastore-validation sqlite

```text
$ my-datastore-validation sqlite -h
usage: my-datastore-validation sqlite [-h] [-e] [--log LOG]
                                             [-ov ONLY_VALIDATE]
                                             [-ifk IGNORE_FOREIGN_KEY]

optional arguments:
  -h, --help            show this help message and exit
  -e, --echo            this flag causes all sqlalchemy statements to be
                        printed to `sys.stdout` following compilation
  --log LOG             Log output path
  -ov ONLY_VALIDATE, --only-validate ONLY_VALIDATE
                        If provided, only the specified view/table name(s)
                        will be validated
  -ifk IGNORE_FOREIGN_KEY, --ignore-foreign-key IGNORE_FOREIGN_KEY
                        The name of a foreign key to ignore for validation
                        purposes only (only applicable for the "validation"
                        command)
```

## Updating this Project

If/when you upgrade or add any dependencies, you need to run
`make requirements` before committing (and before testing, even locally, with
tox).

Deployment to Artifactory will occur when your changes are merged into the
"main" branch, however only if you have incremented the version number.

You can increment the version number by changing the **version** argument in
**setup.cfg**.

## Testing

To run "unit" tests for this package, just execute `tox`:

```shell
tox -p
```
