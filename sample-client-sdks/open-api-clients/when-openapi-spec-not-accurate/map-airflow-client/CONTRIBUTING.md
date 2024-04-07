# Contributing

[Development Environment Setup](https://github.com/siddartham/data-engineering-ecosystem/dev-env-setup)

## Installation

```shell script
git clone https://github.com/siddartham/data-engineering-ecosystem.git && \ 
cd ./data-engineering-ecosystem/map-airflow-client && \
make
```

## Updating this Project

### API Updates

To update the client and model to reflect minor version updates to the
Airflow stable REST API (v1), run `make remodel`.

### Dependency Updates

If/when you upgrade or add dependencies to setup.cfg, you will need to
run `make requirements` before committing (and before testing, even locally,
with tox).

To update *existing requirements* to reflect the most recent compatible
versions, run `make upgrade`.

## Testing

To run unit tests for this package, just run `make test` in the project
directory.

## Deployment

Distribution of this package to Artifactory will occur when your changes are
merged into the "main" branch *if* you have incremented the version number.

You can increment the version number by changing the **version** argument in
**setup.cfg**.
