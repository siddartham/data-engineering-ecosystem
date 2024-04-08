# docker-utilities

[Development Environment Setup](https://github.com/siddarthm/data-engineering-ecosystem/dev-env-setup)

## Install

```shell script
git clone "https://$(id -u -n | tr '[:upper:]' '[:lower:]')_nike@github.com/nike-sustainability/nike-docker-utilities.git"
cd docker-utilities
make
```

## Create a Feature Branch

This project adheres to a feature branching strategy with the following naming
conventions:

| Issue Type  | Branch Name Pattern      |
|:------------|:-------------------------|
| Task        | feature/{JIRA_ISSUE_KEY} |
| Story       | feature/{JIRA_ISSUE_KEY} |
| Bug         | bugfix/{JIRA_ISSUE_KEY}  |

## Testing

Please create a unit test for any/all public functions or methods you
introduce.

To *run* unit tests for this package, just run `make test` in the project
directory.

## [Create a Pull Request](https://github.com/siddarthm/data-engineering-ecosystem/pulls)

## Upgrade/Update Requirements

If/when you upgrade or add dependencies to setup.cfg, you will need to
run `make requirements` before committing (and before testing, even locally,
with tox).

To update *existing requirements* to reflect the most recent compatible
versions, run `make upgrade` (this will also update requirements once
upgrades are complete).

## Deployment

Distribution of this package to Artifactory will occur when your changes are
merged into the "main" branch *if* you have incremented the version number.

You can increment the version number by changing the **version** argument in
**setup.cfg**.

Distribution of this package to Artifactory will occur when your changes are
merged into the "main" branch *if* you have incremented the version number.

You can increment the version number by changing the **version** argument in
**setup.cfg**.
