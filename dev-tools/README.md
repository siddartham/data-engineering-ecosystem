# company-myteam-dev-tools 

This package is a CLI providing deployment and distribution tools for company
myteam Analytics.

- [Development Environment Setup](https://github.company.com/myteam/company-myteam-documentation/blob/master/development-environment-setup.md#setting-up-your-development-environment)
- [Installation](#Installation)
- [Updating this Package](#Updating-this-Package)
  - [Adding New "Materialized" Views](#Adding-New-Materialized-Views)
- [Testing](#Testing)

## Installation

You can install this package from company's Artifactory PYPI:

```shell
pip3 install company-myteam-dev-tools[all]\
 --extra-index-url\
 https://artifactory.company.com/artifactory/api/pypi/python-virtual/simple\
 --trusted-host artifactory.company.com
```

To install *for development*:

- Make sure you have [docker](https://docs.docker.com/docker-for-mac/install/)
  installed.
- Make sure you have [epctl](https://epctl.platforms.company.com/) installed.
- Clone the repository:
  ```shell script
  git clone\
   https://github.company.com/myteam/\
  company-myteam-dev-tools.git\
   company-myteam-dev-tools
  cd company-myteam-dev-tools
  ```
- Create and activate a new virtual environment:
  ```shell
  python3 -m venv venv
  source venv/bin/activate
  ```
- Install the package in-place:
  ```shell script
  pip3 install -e '.[test]'\
   --extra-index-url\
   https://artifactory.company.com/artifactory/api/pypi/python-virtual/simple\
   --trusted-host artifactory.company.com
  ```

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

### company-myteam-dev-tools requirements update

This command updates the requirement versions for a "setup.py" file, and
(optionally) updates or creates a "requirements.txt" file.

Usage: 

`company-myteam-dev-tools requirements update [options] [<setup_script>...]`

Setup Script:

A directory or file path where a `setup.py` script can be found (this
defaults to "./setup.py").

Options:

-r, --requirements: The name/path at which to save create/update a requirements
file (if not provided, no requirements file is created/update).

-e, --exclude: A comma separated list of package names to exclude from the
requirements file (only applicable if "-r" or "--requirements" are provided).

## Updating this Package

Following any changes to this package (at least any changes for which you
want to trigger a build), the version number should be updated in `setup.py`,
in the `setup()` call's `version` parameter, and you should also run `python3
scripts/update_setup_requirements.py` to ensure all installation requirements
are up-to-date. Deployment to Artifactory will occur when changes are merged
into the "master" branch.
  
## Testing

To run "unit" tests for this package, just execute `tox`:

```shell
tox
```
