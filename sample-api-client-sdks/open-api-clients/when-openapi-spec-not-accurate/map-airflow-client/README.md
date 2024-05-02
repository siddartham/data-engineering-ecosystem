# map-airflow-client

[![test](https://github.com/siddartham/data-engineering-ecosystem/sample-client-sdks/openapi-clients/when-openapi-spec-not-accurate/map-airflow-client/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/sample-client-sdks/openapi-clients/when-openapi-spec-not-accurate/map-airflow-client/actions/workflows/test.yml)
[![distribute](https://github.com/siddartham/data-engineering-ecosystem/sample-client-sdks/openapi-clients/when-openapi-spec-not-accurate/map-airflow-client/actions/workflows/distribute.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/sample-client-sdks/openapi-clients/when-openapi-spec-not-accurate/map-airflow-client/actions/workflows/distribute.yml)

A python client for Airflow's REST APIs, for clusters running
on Managed Airflow Platform(MAP).

## Installation

To install:

```shell script
pip3 install map-airflow-client
```

## Usage

Please note that before using this client, you must setup your
[OAuth application](https://bit.ly/3jD1WxK) and add it to your
MAP cluster permissions. Complete instruction for this can be found
[in the MAP documentation](https://swoo.sh/3rLMyUn).

### CLI

The CLI for this client does not cover all functionality implemented
in the library. The CLI aims to cover functionality needed to fully automate
deployment and testing of a DAG using a CI pipeline, when used in concert
with [`epctl map`](https://epctl.platforms.my.com/reference/map/).
For more complex use cases, refer to the [Library](#Library) usage examples.

```text
$ map-airflow-client -h
Usage:
  map-airflow-client <command> [options]

Commands:
  run                         Trigger a DAG run.
  pause                       Pause a DAG.
  unpause                     Un-pause a DAG.
  create-connection           Create a connection.
  delete-connection           Delete a connection.
```

#### map-airflow-client run

```text
$ map-airflow-client run -h
usage: map-airflow-client run [-h] [-cn CLUSTER_NAME] [-r REGION]
                                   [-cid CLIENT_ID] [-cs CLIENT_SECRET]
                                   [-cscp CLIENT_SECRET_CERBERUS_PATH]
                                   [-l LOG] [-e] [-did DAG_ID]
                                   [-dfn DAG_FILE_NAME] [-d]

Trigger a DAG run.

optional arguments:
  -h, --help            show this help message and exit
  -cn CLUSTER_NAME, --cluster-name CLUSTER_NAME
                        The name of your MAP cluster.
  -r REGION, --region REGION
                        Your MAP cluster's AWS region: us-west-2 | us-east-1 |
                        etc.
  -cid CLIENT_ID, --client-id CLIENT_ID
                        Your OAuth2 client ID.
  -cs CLIENT_SECRET, --client-secret CLIENT_SECRET
                        Your OAuth2 client secret.
  -cscp CLIENT_SECRET_CERBERUS_PATH, --client-secret-cerberus-path CLIENT_SECRET_CERBERUS_PATH
                        A Cerberus secure data path where your OAuth2 client
                        secret is stored.
  -l LOG, --log LOG     Log output path
  -e, --echo            Echo requests/responses
  -did DAG_ID, --dag-id DAG_ID
                        The ID of one or more DAGs to run.
  -dfn DAG_FILE_NAME, --dag-file-name DAG_FILE_NAME
                        The file name of one or more DAGs. Please note that
                        this argument is only valid for use with clusters
                        using Airflow version 2 or later. For Airflow version
                        1 MAP clusters, please provide DAG IDs using the
                        `--dag-id` parameter.
  -d, --detach          Detached mode: Do not wait for the DAG run to finish.
                        Please only use this flag if you do not need to ensure
                        the successful completion of the triggered DAG run, as
                        detached mode does not wait to verify successful
                        completion of the run prior to exit.
```

#### map-airflow-client pause

```text
$ map-airflow-client pause -h
usage: map-airflow-client pause [-h] [-cn CLUSTER_NAME] [-r REGION]
                                     [-cid CLIENT_ID] [-cs CLIENT_SECRET]
                                     [-cscp CLIENT_SECRET_CERBERUS_PATH]
                                     [-l LOG] [-e] [-did DAG_ID]
                                     [-dfn DAG_FILE_NAME]

Pause DAG(s).

optional arguments:
  -h, --help            show this help message and exit
  -cn CLUSTER_NAME, --cluster-name CLUSTER_NAME
                        The name of your MAP cluster.
  -r REGION, --region REGION
                        Your MAP cluster's AWS region: us-west-2 | us-east-1 |
                        etc.
  -cid CLIENT_ID, --client-id CLIENT_ID
                        Your OAuth2 client ID.
  -cs CLIENT_SECRET, --client-secret CLIENT_SECRET
                        Your OAuth2 client secret.
  -cscp CLIENT_SECRET_CERBERUS_PATH, --client-secret-cerberus-path CLIENT_SECRET_CERBERUS_PATH
                        A Cerberus secure data path where your OAuth2 client
                        secret is stored.
  -l LOG, --log LOG     Log output path
  -e, --echo            Echo requests/responses
  -did DAG_ID, --dag-id DAG_ID
                        The ID of one or more DAGs to run.
  -dfn DAG_FILE_NAME, --dag-file-name DAG_FILE_NAME
                        The file name of one or more DAGs. Please note that
                        this argument is only valid for use with clusters
                        using Airflow version 2 or later. For Airflow version
                        1 MAP clusters, please provide DAG IDs using the
                        `--dag-id` parameter.
```

#### map-airflow-client unpause

```text
$ map-airflow-client unpause -h
usage: map-airflow-client unpause [-h] [-cn CLUSTER_NAME] [-r REGION]
                                       [-cid CLIENT_ID] [-cs CLIENT_SECRET]
                                       [-cscp CLIENT_SECRET_CERBERUS_PATH]
                                       [-l LOG] [-e] [-did DAG_ID]
                                       [-dfn DAG_FILE_NAME]

Un-pause DAG(s).

optional arguments:
  -h, --help            show this help message and exit
  -cn CLUSTER_NAME, --cluster-name CLUSTER_NAME
                        The name of your MAP cluster.
  -r REGION, --region REGION
                        Your MAP cluster's AWS region: us-west-2 | us-east-1 |
                        etc.
  -cid CLIENT_ID, --client-id CLIENT_ID
                        Your OAuth2 client ID.
  -cs CLIENT_SECRET, --client-secret CLIENT_SECRET
                        Your OAuth2 client secret.
  -cscp CLIENT_SECRET_CERBERUS_PATH, --client-secret-cerberus-path CLIENT_SECRET_CERBERUS_PATH
                        A Cerberus secure data path where your OAuth2 client
                        secret is stored.
  -l LOG, --log LOG     Log output path
  -e, --echo            Echo requests/responses
  -did DAG_ID, --dag-id DAG_ID
                        The ID of one or more DAGs to run.
  -dfn DAG_FILE_NAME, --dag-file-name DAG_FILE_NAME
                        The file name of one or more DAGs. Please note that
                        this argument is only valid for use with clusters
                        using Airflow version 2 or later. For Airflow version
                        1 MAP clusters, please provide DAG IDs using the
                        `--dag-id` parameter.
```

#### map-airflow-client create-connection

```text
$ map-airflow-client create-connection -h
usage: map-airflow-client create-connection [-h]
                                                 [-cn CLUSTER_NAME]
                                                 [-r REGION]
                                                 [-cid CLIENT_ID]
                                                 [-cs CLIENT_SECRET]
                                                 [-cscp CLIENT_SECRET_CERBERUS_PATH]
                                                 [-l LOG] [-e]
                                                 [--connection-id CONNECTION_ID]
                                                 [--connection-type CONNECTION_TYPE]
                                                 [--description DESCRIPTION]
                                                 [--host HOST]
                                                 [--login LOGIN]
                                                 [--schema SCHEMA]
                                                 [--port PORT]
                                                 [--password PASSWORD]
                                                 [--extra EXTRA]

Create or update a connection

optional arguments:
  -h, --help            show this help message and exit
  -cn CLUSTER_NAME, --cluster-name CLUSTER_NAME
                        The name of your MAP cluster.
  -r REGION, --region REGION
                        Your MAP cluster's AWS region: us-west-2
                        | us-east-1 | etc.
  -cid CLIENT_ID, --client-id CLIENT_ID
                        Your OAuth2 client ID.
  -cs CLIENT_SECRET, --client-secret CLIENT_SECRET
                        Your OAuth2 client secret.
  -cscp CLIENT_SECRET_CERBERUS_PATH, --client-secret-cerberus-path CLIENT_SECRET_CERBERUS_PATH
                        A Cerberus secure data path where your
                        OAuth2 client secret is stored.
  -l LOG, --log LOG     Log output path
  -e, --echo            Echo requests/responses
  --connection-id CONNECTION_ID
  --connection-type CONNECTION_TYPE
  --description DESCRIPTION
  --host HOST
  --login LOGIN
  --schema SCHEMA
  --port PORT
  --password PASSWORD
  --extra EXTRA
```

#### map-airflow-client delete-connection

```text
$ map-airflow-client delete-connection -h
usage: map-airflow-client delete-connection [-h] [-cn CLUSTER_NAME]
                                                 [-r REGION]
                                                 [-cid CLIENT_ID]
                                                 [-cs CLIENT_SECRET]
                                                 [-cscp CLIENT_SECRET_CERBERUS_PATH]
                                                 [-l LOG] [-e]
                                                 [--connection-id CONNECTION_ID]

Delete a connection

optional arguments:
  -h, --help            show this help message and exit
  -cn CLUSTER_NAME, --cluster-name CLUSTER_NAME
                        The name of your MAP cluster.
  -r REGION, --region REGION
                        Your MAP cluster's AWS region: us-west-2 | us-
                        east-1 | etc.
  -cid CLIENT_ID, --client-id CLIENT_ID
                        Your OAuth2 client ID.
  -cs CLIENT_SECRET, --client-secret CLIENT_SECRET
                        Your OAuth2 client secret.
  -cscp CLIENT_SECRET_CERBERUS_PATH, --client-secret-cerberus-path CLIENT_SECRET_CERBERUS_PATH
                        A Cerberus secure data path where your OAuth2
                        client secret is stored.
  -l LOG, --log LOG     Log output path
  -e, --echo            Echo requests/responses
  --connection-id CONNECTION_ID
```

### Library

This package really implements *two* Airflow clients:

1. `map_airflow_client.experimental.client.Client`:
   This client is compatible with Airflow 1x. You can also enable this API
   in Airflow 2 by setting a config value as described
   [here](https://bit.ly/3JKE8mf) (not recommended).
2. `map_airflow_client.v1.client.Client`:
   This client is compatible with Airflow 2x.

When using the CLI, your API version is automatically inferred, however
for more complex use cases you will need to identify the version of Airflow
you are using and choose your client accordingly.

#### V1 API Examples

```python
import os
import typing
from time import sleep
from map_airflow_client import model
from map_airflow_client.client import Client

# In the below snippet, replace "cluster-name" with the name of your cluster,
# "us-west-2" with the region in which your cluster is running,
# "oauth.client.id" with your OAuth client ID, and "app/your-sdb/path/key"
# with the Cerberus secure data path where you have stored your client
# secret.
client: Client = Client(
    "https://proxy.us-west-2.map.my.com/cluster-name/api/v1",
    oauth2_client_id="oauth.client.id",
    oauth2_client_secret_cerberus_path=(
        "app/your-sdb/path/key"
    ),
    oauth2_token_url="https://api.aegis.mycloud.com/v1/prod/token",
    echo=True,
)

# Retrieve information about your DAGs
dag_collection: model.DAGCollection = client.get_dags()

# Un-pause a DAG
client.patch_dags_dag_id(
    dag=model.DAG(is_paused=False),
    dag_id="your_dag_id"
)

# Trigger a DAG run
dag_run: model.DAGRun = client.post_dags_dag_id_dag_runs(
    dag_run=model.DAGRun(),
    dag_id="your_dag_id"
)

# Determine the state of a DAG run
dag_run = client.get_dags_dag_id_dag_runs_dag_run_id(
    dag_id=dag_run.dag_id,
    dag_run_id=dag_run.dag_run_id,
)

# Wait for a DAG run to complete
while dag_run.state in (
    "running",
    "queued",
    "scheduled",
    "none",
):
    sleep(10)
    dag_run = client.get_dags_dag_id_dag_runs_dag_run_id(
        dag_id=dag_run.dag_id,
        dag_run_id=dag_run.dag_run_id,
    )

# Ensure the DAG finished successfully
assert dag_run.state == "success"

# Retrieve DAG info by file name
dag: model.DAG
my_dags: typing.Iterable[model.DAG] = filter(
    lambda dag: os.path.basename(dag) == "your_dag_file_name.py",
    dag_collection.dags or ()
)
```

## CI/CD

Example Jenkinsfile:

```groovy
pipeline {
    agent any
    stages {
        stage('install'){
            steps {
                // Install python3.10
                sh 'sudo add-apt-repository -y ppa:deadsnakes/ppa'
                sh 'sudo apt-get update'
                sh 'sudo apt-get install -y software-properties-common'
                sh 'sudo apt-get install -y python3.10-full'
                // Install EPCTL
                sh (
                    "curl https://epctl.platforms.my.com/binaries/"
                    + "latest/epctl_linux_amd64 -o /usr/local/bin/epctl && "
                    + "chmod +x /usr/local/bin/epctl"
                )
                // Create Virtual Environment
                sh "python3 -m venv venv"
                // Install CI/CD tools
                sh (
                    "venv/bin/pip3 install --no-cache-dir "
                    + "map-airflow-client cerberus-assistant"
                )
            }
        }
        stage('test') {
            // Run tests if package files have changed, tests have changed,
            // requirements have changed, this is our first build, or
            // the previous build failed
            when {
                anyOf {
                    changeset "airflow/dags/**"
                    expression {
                        return currentBuild.previousBuild == null
                    }
                    expression {
                        !("SUCCESS".equals(currentBuild.previousBuild.result))
                    }
                }
            }
            steps {
                // Login to EPCTL using your OAuth client ID and secret
                sh (
                    "epctl login --production "
                    + '--client-id my.client.id '
                    + '--client-secret "$(cerberus-assistant get '
                    + 'app/my-secure-drop-box/map/my.client.id)"'
                )
                // Upload the DAG file to a pre-production (QA) MAP cluster
                // named "my-qa-cluster"
                sh (
                    "epctl map upload-dag --production --region us-west-2 "
                    + "--file-path airflow/dags/my_dag.py "
                    + "--file-name my_dag.py "
                    + "--cluster-name my-qa-cluster"
                )
                // Run the DAG file that was just uploaded.
                // This command will raise an error if the DAG run does not
                // finish with a state of "success".
                sh (
                    "venv/bin/map-airflow-client run "
                    + "-r us-west-2 "
                    + "-cn my-qa-cluster "
                    + "-dfn my_dag.py "
                    + "-cid my.client.id "
                    + "-cscp app/my-secure-drop-box/map/my.client.id"
                )
            }
        }
        stage("deploy") {
            // Deploy the DAG to production if the QA run was successful
            when {
                branch "main"
                anyOf {
                    changeset "airflow/dags/**"
                    expression {
                        return currentBuild.previousBuild == null
                    }
                    expression {
                        !("SUCCESS".equals(currentBuild.previousBuild.result))
                    }
                }
            }
            steps {
                // Upload the DAG file to a production (prod) MAP cluster
                // named "my-prod-cluster"
                sh (
                    "epctl map upload-dag --production --region us-west-2 "
                    + "--file-path airflow/dags/my_dag.py "
                    + "--file-name my_dag.py "
                    + "--cluster-name my-prod-cluster"
                )
                // Un-pause the DAG file that was just uploaded, so that it
                // will run at the next scheduled time
                sh (
                    "venv/bin/map-airflow-client unpause "
                    + "-r us-west-2 "
                    + "-cn my-prod-cluster "
                    + "-dfn my_dag.py "
                    + "-cid my.client.id "
                    + "-cscp app/my-secure-drop-box/map/my.client.id"
                )
            }
        }
    }
    post {
        always {
            // Create the Virtual Environment (in case the "install" stage
            // failed)
            sh "python3 -m venv venv" 
            // Install CI/CD tools (in case the "install" stage
            // failed)
            sh (
                "venv/bin/pip3 install --no-cache-dir mail-client"
            )
        }
        // Email Build Results to the Author of the Commit
        success {
            sh (
                "venv/bin/mail-client send " +
                "-t \"\$(git --no-pager show -s --format=%ae ${env.GIT_COMMIT})\" " +
                "-pcp \"app/sustainability/bmx/a.BMX.SUSTAINABILITY\" " +
                "-s \"Success - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\" || " +
                "mail-client send " +
                "-t ${env.CHANGE_AUTHOR_EMAIL} " +
                "-pcp \"app/sustainability/bmx/a.BMX.SUSTAINABILITY\" " +
                "-s \"Success - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\""
            )
        }
        failure {
            sh (
                "venv/bin/mail-client send " +
                "-t \"\$(git --no-pager show -s --format=%ae ${env.GIT_COMMIT})\" " +
                "-pcp \"app/sustainability/bmx/a.BMX.SUSTAINABILITY\" " +
                "-s \"Failure - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\" || " +
                "mail-client send " +
                "-t ${env.CHANGE_AUTHOR_EMAIL} " +
                "-pcp \"app/sustainability/bmx/a.BMX.SUSTAINABILITY\" " +
                "-s \"Failure - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\""
            )
        }
        aborted {
            sh (
                "venv/bin/mail-client send " +
                "-t \"\$(git --no-pager show -s --format=%ae ${env.GIT_COMMIT})\" " +
                "-pcp \"app/sustainability/bmx/a.BMX.SUSTAINABILITY\" " +
                "-s \"Aborted - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\" || " +
                "mail-client send " +
                "-t ${env.CHANGE_AUTHOR_EMAIL} " +
                "-pcp \"app/sustainability/bmx/a.BMX.SUSTAINABILITY\" " +
                "-s \"Aborted - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\""
            )
        }
    }
}
```
