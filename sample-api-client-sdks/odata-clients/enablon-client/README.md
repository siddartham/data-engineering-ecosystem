# nike-enablon-client

[![test](https://github.com/nike-sustainability/nike-enablon-client/actions/workflows/test.yml/badge.svg)](https://github.com/nike-sustainability/nike-enablon-client/actions/workflows/test.yml)
[![distribute](https://github.com/nike-sustainability/nike-enablon-client/actions/workflows/distribute.yml/badge.svg)](https://github.com/nike-sustainability/nike-enablon-client/actions/workflows/distribute.yml)

This package is a client SDK for reading data from
[Enablon's](https://docs.enablon.com) "Blink"
[OData](https://www.odata.org/) API.

See [CONTRIBUTING.md](CONTRIBUTING.md) for information pertaining to
development of this package.

## Install

You can install this package from Nike's Artifactory PYPI:

```shell script
pip3 install nike-enablon-client\
 --extra-index-url\
 https://artifactory.nike.com/artifactory/api/pypi/python-virtual/simple
```

## Usage

Each method of the class `nike.enablon_client.client.Client`
(except for `.get()` and `.request()`) corresponds to an entity type, and
returns an iterator yielding responses which contain values analogous to
rows in a table.

For example:

```python
from nike.enablon_client import model
from logging import Logger, getLogger
from typing import Iterable
from nike.enablon_client.client import Client

log: Logger = getLogger(__name__)


client: Client = Client(
    # Either a user/password or Cerberus paths
    # to each must be provided
    user_cerberus_path="app/sustainability/enablon/user-prod",
    password_cerberus_path=(
        "app/sustainability/enablon/password-prod"
    ),
    # If provided, API requests and responses will be logged using this logger
    logger=log,
    # If `echo == True`, your API requests and responses will be printed
    # to `sys.stdout` (for debugging, etc.)
    echo=True
)

# Each method of a client instance corresponds to a table, and the return
# value is an iterable yielding paginated response objects, each of which
# has a `value` property holding table records
ho_entities_response: Iterable[model.HoEntitiesResponse]
for ho_entities_response in client.ho_entities(top=3):
    ho_entity: model.HoEntity
    for ho_entity in ho_entities_response.value:
        print(repr(ho_entity))
```

Executing the snippet above prints the following:

```text
nike.enablon_client.model.HoEntity(
    level_fk_level_no=1,
    code='N',
    entity_en='NIKE, INC.',
    order=1.0,
    entity_status_fk_reference=0,
    input_fk_reference=1,
    geography_fk_id=sob.utilities.types.NULL,
    latitude=sob.utilities.types.NULL,
    longitude=sob.utilities.types.NULL,
    business_fk_code=sob.utilities.types.NULL,
    id_=2312
)
nike.enablon_client.model.HoEntity(
    level_fk_level_no=2,
    code='N.1',
    entity_en='Nike',
    order=2.0,
    entity_status_fk_reference=0,
    input_fk_reference=1,
    geography_fk_id=sob.utilities.types.NULL,
    latitude=sob.utilities.types.NULL,
    longitude=sob.utilities.types.NULL,
    business_fk_code=sob.utilities.types.NULL,
    id_=2313
)
nike.enablon_client.model.HoEntity(
    level_fk_level_no=2,
    code='N.2',
    entity_en='IHM',
    order=2.0,
    entity_status_fk_reference=1,
    input_fk_reference=0,
    geography_fk_id=sob.utilities.types.NULL,
    latitude=sob.utilities.types.NULL,
    longitude=sob.utilities.types.NULL,
    business_fk_code=sob.utilities.types.NULL,
    id_=2314
)
```
