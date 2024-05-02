# databricks-jobs

[![test](https://github.com/siddartham/data-engineering-ecosystem/databricks-jobs/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/databricks-jobs/actions/workflows/test.yml)
[![distribute](https://github.com/siddartham/data-engineering-ecosystem/databricks-jobs/actions/workflows/distribute.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/databricks-jobs/actions/workflows/distribute.yml)


## Install


```shell script
pip3 install databricks-jobs
```

## Usage

This package provides functionality for updating the PYPI libraries
associated with one or more Databricks jobs based on a requirements.txt file.

### CLI

#### databricks-jobs update-libraries

```command-prompt
$ databricks-jobs update-libraries -h
usage: databricks-jobs update-libraries [-h] [-r REQUIREMENTS]
                                             [--host HOST] [-t TOKEN]
                                             [-tcp TOKEN_CERBERUS_PATH]
                                             [-tk TASK_KEYS]
                                             [job-name [job-name ...]]

This command updates PYPI libraries for one or more databricks job(s)
based on the provided requirements file

positional arguments:
  job-name             The name of the jobs to update.

optional arguments:
  -h, --help            show this help message and exit
  -r REQUIREMENTS, --requirements REQUIREMENTS
                        The path to a requirements file.
  --host HOST           The databricks API host.
  -t TOKEN, --token TOKEN
                        An authentication token.
  -tcp TOKEN_CERBERUS_PATH, --token-cerberus-path TOKEN_CERBERUS_PATH
                        An authentication token.
  -tk TASK_KEY, --task-key TASK_KEY
                        If provided, only tasks with the specified keys
                        will be updated.
```

##### Example Usage

Update libraries for all tasks in the job "my-job-name":

```command-prompt
$ databricks-jobs update-libraries\
    --token-cerberus-path app/sustainability/sustainability/ServicePrincipal_community.cloud.databricks.com_App.Sole.teamname.Developer\
    -r requirements.txt\
    my-job-name
```

Update libraries for tasks named "task_a" and "task_b" in the job
"my-job-name":

```command-prompt
$ databricks-jobs update-libraries\
    --token-cerberus-path app/sustainability/sustainability/ServicePrincipal_community.cloud.databricks.com_App.Sole.teamname.Developer\
    -r requirements.txt\
    -tk task_a\
    -tk task_b\
    my-job-name
```

#### databricks-jobs upload

```command-prompt
$ databricks-jobs upload -h
usage: databricks-jobs upload [-h] [--host HOST] [-t TOKEN]
                                   [-tcp TOKEN_CERBERUS_PATH]
                                   [-f LOCAL_FILE_PATH WORKSPACE_PATH]

This command uploads a file to your Databricks workspace.

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           The databricks API host.
  -t TOKEN, --token TOKEN
                        An authentication token.
  -tcp TOKEN_CERBERUS_PATH, --token-cerberus-path TOKEN_CERBERUS_PATH
                        An authentication token.
  -f LOCAL_FILE_PATH WORKSPACE_PATH, --file LOCAL_FILE_PATH WORKSPACE_PATH
```

#### databricks-jobs update-init-scripts

```command-prompt
$ databricks-jobs update-init-scripts -h
usage: databricks-jobs update-init-scripts [-h] [-is INIT_SCRIPT]
                                                [--host HOST] [-t TOKEN]
                                                [-tcp TOKEN_CERBERUS_PATH]
                                                [-tk TASK_KEY]
                                                [job-name [job-name ...]]

This command updates init scripts for one or more databricks job(s). All
init scripts must have been previously uploaded to the workspace.

positional arguments:
  job-name              The name of the jobs to update.

optional arguments:
  -h, --help            show this help message and exit
  -is INIT_SCRIPT, --init-script INIT_SCRIPT
                        The workspace path to one or more init scripts.
                        If not provided, all init scripts will be
                        removed from the specified jobs/tasks.
  --host HOST           The databricks API host.
  -t TOKEN, --token TOKEN
                        An authentication token.
  -tcp TOKEN_CERBERUS_PATH, --token-cerberus-path TOKEN_CERBERUS_PATH
                        An authentication token.
  -tk TASK_KEY, --task-key TASK_KEY
                        If provided, only tasks with the specified keys
                        will be updated.
```

### Library

#### databricks_jobs.update_libraries.update_jobs_libraries

This function updates PYPI libraries for one or more databricks jobs based
on a provided requirements file.

Parameters:

- job_names ([str]|str): The name of the job (or jobs) to update.
- requirements (str|Path): The path to a requirements file.
- task_keys ((str,)) = (): If provided only tasks with the specified
  keys will be updated.
- host (str): The databricks API host.
- token (str): An authentication token.
- token_cerberus_path (str): A Cerberus secure drop box path from
  which an authentication token can be retrieved.

##### Example Usage

```python
from databricks_jobs.update_libraries import update_jobs_libraries

update_jobs_libraries(
    job_names=("my-job-name",),
    requirements="requirements.txt",
    token_cerberus_path=(
        "app/secure-drop-box-name/teamname/"
        "ServicePrincipal_community.cloud.databricks.com_"
        "App.Sole.teamname.Developer"
    )
)
```

#### databricks_jobs.update_libraries.upload.upload

This function uploads files to your Databricks workspace.

Parameters:

- files ([(str, str)]|{str: str}): A mapping of local file paths to
  the workspace paths to which you wish to upload.
- token (str): An authentication token.
- token_cerberus_path (str): A Cerberus secure drop box path from
  which an authentication token can be retrieved.

##### Example Usage

The following uploads `requirements.txt` to the workspace path
`/Workspace/Shared/my-shared-directory/requirements.txt`.

```python
from databricks_jobs.update_libraries.upload import upload


upload(
  files={
    "requirements.txt":
    "/Workspace/Shared/my-shared-directory/requirements.txt"
  },
  host="community.cloud.databricks.com",
  token_cerberus_path="app/my-secure-drop-box/my-secret/key"
)
```

#### databricks_jobs.update_libraries.update_init_scripts

This function updates init scripts for one or more databricks job.
All init scripts must have been previously uploaded to the workspace.

Parameters:

- job_names ([str]|str): The name of the job (or jobs) to update.
- init_scripts ([str]|str): The worksapce path to one or more init scripts.
- host (str): The databricks API host.
- task_keys ((str,)) = (): If provided only tasks with the specified
  keys will be updated.
- token (str): An authentication token.
- token_cerberus_path (str): A Cerberus secure drop box path from
  which an authentication token can be retrieved.

##### Example Usage

The following applies init scripts for "my-job-name", to the job
cluster used by the task with task-key "task-a". Please note that this
cluster could also used by any other tasks.

```python
from databricks_jobs.update_init_scripts.update_jobs_init_scripts import (
  update_jobs_init_scripts
)


update_jobs_init_scripts(
  job_names=("my-job-name",),
  init_scripts=(
    "/Workspace/Shared/my-shared-directory/requirements.txt",
  ),
  task_keys=("task-a",),
  host="community.cloud.databricks.com",
  token_cerberus_path="app/my-secure-drop-box/my-secret/key"
)
```

### pyproject.toml

Default values for all arguments *except* `token` can be provided in your
`pyproject.toml`, under `[tool.databricks-jobs]`, as follows:

```toml
[tool.databricks-jobs]
host = "community.cloud.databricks.com"
token-cerberus-path = "app/secure-drop-box-name/team-name/ServicePrincipal_community.cloud.databricks.com_App.Sole.team-name.Developer"
requirements = "requirements.txt"
init-scripts = [
    "/Workspace/Shared/my-shared-directory/init.sh",
]

[tool.databricks-jobs.files]
"init.sh" = "/Workspace/Shared/databricks-jobs-test/init.sh"
"requirements.txt" = "/Workspace/Shared/my-shared-directory/requirements.txt"
```

You may not set `token` in your `pyproject.toml` for security reasons, instead
please use `token-cerberus-path` and set your token in a Cerberus
secure-drop-box.
