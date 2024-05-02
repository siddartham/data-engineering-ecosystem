# nike-enablon-client

[Development Environment Setup](https://swoo.sh/38PnIMp)

## Install

```shell script
git clone https://github.com/nike-sustainability/nike-enablon-client.git
cd nike-enablon-client
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

## [Create a Pull Request](https://github.com/nike-sustainability/nike-enablon-client/pulls)

Please create a pull request for all/any requested changes to this package.

## Updating the Data Model and Client Methods

To update the data model and client methods for this project, based on the
currently published metadata for our Enablon endpoints, just run
`make remodel`. Please pay attention to the following in order to determine
additional work needed for downstream packages:

- If any new model classes are added as a result of remodeling, a markdown
  table mapping class names to table names will be printed
- Please review your
  [nike/enablon_client/model.py](nike/enablon_client/model.py) stage/commit
  diff to identify any tables/classes which might have fields which have been
  added/removed/renamed
- Please review [metadata.xml](metadata.xml) to identify foreign key
  relationships for columns corresponding to any newly added fields

Please create JIRA tickets to address any changes needed to the following
downstream packages:
- [nike-sustainability-model
  ](https://github.com/nike-sustainability/nike-sustainability-model)
- [nike-enablon-etl
  ](https://github.com/nike-sustainability/nike-enablon-etl)

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
