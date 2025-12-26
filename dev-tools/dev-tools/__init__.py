"""
## Commands

### company-myteam-dev-tools airflow deploy

This command deploys all DAGs in a sub-directory to one of myteam
Analytics' Managed Airflow Platform clusters ("dev", "qa" or "prod").

Usage:

`company-myteam-dev-tools airflow deploy [options] {dev|qa|prod}...`

Options:

-d, --directory: The directory where your DAGs are stored (defaults to
"airflow/dags")

### company-myteam-dev-tools airflow run

Usage:

`company-myteam-dev-tools airflow run [options] {dev|qa|prod}...`

Options:

-d, --directory: The directory where your DAGs are stored (defaults to
"airflow/dags")

### company-myteam-dev-tools docker distribute

Usage:

`company-myteam-dev-tools docker distribute [options]`

Options:

-d, --directory: The directory where your `setup.py` file resides, and the
working directory for Docker (defaults to "./")

-ba, --build-arg (repeatable): A build argument, passed to `docker build` as-is
(see `docker build --help` for details)

-f, --file: The name/path of your Dockerfile (defaults to `Dockerfile`)

### company-myteam-dev-tools pypi distribute

Usage:

`company-myteam-dev-tools pypi distribute [options] [<directory>]`

Options:

See `twine upload --help` for a complete list of options, as all options are
passed on to twine.

### company-myteam-dev-tools spark deploy

This command uploads a bootstrap action and spark app to the
"company-emr-bin-west" S3 bucket.

Usage:

`company-myteam-dev-tools spark deploy [options] {dev|qa|prod}...`

Options:

-d, --directory: The directory where your `setup.py` file resides.

-r, --requirement (repeatable): The name/path of a requirements file. If
none is provided, requirements will be inferred based on setup.py.

### company-myteam-dev-tools spark update-requirements

This command updates a requirements.txt file based on package dependencies,
excluding packages which would be installed by `pyspark`.

Usage:

`company-myteam-dev-tools spark update-requirements [options]`

Options:

-f, --file: The name/path of the requirements file (defaults to
"requirements.txt").

-n, --name: The name of the package for which to generate requirements (if
not provided this will be inferred from `setup.py`).

-d, --directory: The directory or path where `setup.py` can be found (this
defaults to the current directory).
"""
