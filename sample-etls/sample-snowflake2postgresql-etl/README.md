# sample-snowflake2postgresql-etl

This package extracts data from Snowflake and performs a truncate and
reload to ingest the data into PostgreSQL.

## Install

### Basic Installation

You can install this package from Nike's Artifactory PYPI:

```shell script
pip3 install sample-snowflake2postgresql-etl\
 --extra-index-url\
 https://artifactory.org.com/artifactory/api/pypi/python-virtual/simple\
 --trusted-host artifactory.org.com
```

### Development Installation

```shell script
git clone https://github.com/siddartham/data-engineering-ecosystem.git
cd data-engineering-ecosystem/sample-snowflake2postgresql-etl
make
```

## Usage

### CLI

```text
$ sample-snowflake2postgresql-etl -h
usage: sample-snowflake2postgresql-etl [-h] [-p PARALLELISM]
                                                    [-l LOG] [-c CONCURRENCY]
                                                    [-e]
                                                    environment

positional arguments:
  operation             extract | load
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
```

### Library

```python
# TODO
```

## Updating this Project

If/when you upgrade or add any dependencies, you need to run
`make requirements` before committing (and before testing, even locally, with
tox).

Deployment to Artifactory will occur when your changes are merged into the
"master" branch, however only if you have incremented the version number.

You can increment the version number by changing the **version** argument in
**setup.cfg**.

## Testing

To run "unit" tests for this package, just execute `tox`:

```shell
tox -r -p
```
