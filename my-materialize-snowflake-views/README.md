# my-materialize-snowflake-views

[![test](https://github.com/siddartham/data-engineering-ecosystem/my-materialize-snowflake-views/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/my-materialize-snowflake-views/actions/workflows/test.yml)
[![deploy](https://github.com/siddartham/data-engineering-ecosystem/my-materialize-snowflake-views/actions/workflows/deploy.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/my-materialize-snowflake-views/actions/workflows/deploy.yml)


This package refreshes "materialized" views in Snowflake.
Snowflake does not permit complex/multi-table materialized views,
so when the query populating a view is not performant, this package
is used to instead truncate and reload an equivalent table.

## Install

### Basic Installation


```shell script
pip3 install my-materialize-snowflake-views
```

### Development Installation

```shell script
git clone https://github.com/siddartham/data-engineering-ecosystem/my-materialize-snowflake-views.git
cd cd data-engineering-ecosystem/my-materialize-snowflake-views
make
```
  
## Usage

### CLI

```text
$ my-materialize-snowflake-views -h
usage: my-materialize-snowflake-views [-h] [-p PARALLELISM]
                                                       [-l LOG]
                                                       [-c CONCURRENCY] [-e]
                                                       [--include INCLUDE]
                                                       [--exclude EXCLUDE]
                                                       environment

positional arguments:
  environment           dev | qa | prod

optional arguments:
  -h, --help            show this help message and exit
  -p PARALLELISM, --parallelism PARALLELISM
  -l LOG, --log LOG     Log output path
  -c CONCURRENCY, --concurrency CONCURRENCY
                        Which mechanism to use for parallel processing:
                        "spark" ("s"), "multiprocessing" ("m"), or "none"
                        ("n")
  -e, --echo            Echo requests/responses
  --include INCLUDE     One or more tables ("materialized views") to refresh.
                        If this argument is not provided, all "materialized
                        view" tables will be refreshed
  --exclude EXCLUDE     One or more tables ("materialized views") to exclude
                        (not refresh). If this argument is not provided, all
                        "materialized view" tables will be refreshed.
```

## Updating this Project

If/when you upgrade or add any dependencies, you need to run
`make requirements` before committing (and before testing, even locally, with
tox).

Deployment to Artifactory will occur when your changes are merged into the
"main" branch, however only if you have incremented the version number.

You can increment the version number by changing the **version** argument in
**setup.cfg**.

### Adding "Materialized" Views

To populate additional "materialized" views with this package:

- Create a table in the PROCESSED schema by adding a mapping in [
  my-datastore-model
  ](../my-datastore-model)
  (see the repo's README for instructions). This table should have a
  suffix of "_MV". Note: Don't forget to create an Alembic migration.
- Add a SQL file containing your SELECT statement to [
  my_materialize_snowflake_views/_select_statements
  ](my_materialize_snowflake_views/_select_statements). The
  file name should be the same as the name of the new table you created.
- Increment the version number for this package in [setup.cfg](setup.cfg).
- Create a pull request. Once deployed, your materialized view(s) should
  be populated and will be refreshed nightly.

## Testing

To run "unit" tests for this package, just execute `tox`:

```shell
tox -r -p
```
