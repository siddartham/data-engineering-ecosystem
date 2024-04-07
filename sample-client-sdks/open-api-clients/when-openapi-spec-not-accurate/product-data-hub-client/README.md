# product-data-hub-client

[![test](https://github.com/siddartham/data-engineering-ecosystem/sample-client-sdks/openapi-clients/when-openapi-spec-not-accurate/product-data-hub-client/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/sample-client-sdks/openapi-clients/when-openapi-spec-not-accurate/product-data-hub-client/actions/workflows/test.yml)
[![distribute](https://github.com/siddartham/data-engineering-ecosystem/sample-client-sdks/openapi-clients/when-openapi-spec-not-accurate/product-data-hub-client/actions/workflows/distribute.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/sample-client-sdks/openapi-clients/when-openapi-spec-not-accurate/product-data-hub-client/actions/workflows/distribute.yml)


This library is an SDK for interacting with Product Data Hub API's.
This distribution is a work-in-progress, not all endpoints and/or APIs are
implemented. If you would like to contribute, please contact
[reddy.siddartha53@gmail.com](
mailto:reddy.siddartha53@gmail.com)

## Install

### Basic Installation


```shell script
pip3 install product-data-hub-client
```

### Development Installation

```shell script
git clone https://github.com/siddartham/data-engineering-ecosystem/sample-client-sdks/openapi-clients/when-openapi-spec-not-accurate/product-data-hub-client.git
cd product-data-hub-client
make
```

## Usage

This library provides clients for multiple Product Data Hub APIs, each of which
is represented by a sub-package of this distribution's top-level package,
`product_data_hub_client`.

Each API "client" is represented by a class which is specific to the API, and
implements a method for each API endpoint. For instance, the class [
    `product_data_hub_client.material_management.client.Client`
](product_data_hub_client/material_management/client.py) exposes a
method for each endpoint in the Material Management API (and its
corresponding "reference" API).

Each of the Product Data Hub API client classes must be instantiated with
a `config` argument which is an instance of [
    `product_data_hub_client.config.Config`
](./product_data_hub_client/config.py). The config object holds
information needed to authenticate requests. Credentials for this object
may either be passed directly when initializing an instance, or
Cerberus secure drop box paths can be provided (using the latter is
strongly recommended). The config object handles OAuth, including retrieval of
new tokens prior to expiration.

Examples:

```python
from product_data_hub_client.material_management import (
    model, reference_model
)
from product_data_hub_client.material_management.client import Client
from product_data_hub_client.config import Config
from typing import Optional

# Note: The code in this example requires the host to have
# AWS credentials which permit access to the "app/sustainability"
# Cerberus secure drop box

# Initialize a Client
client: Client = Client(
    config=Config(
        cerberus_x_api_key_path="app/sustainability/pdh/x-api-key",
        cerberus_client_id_path="app/sustainability/pdh/client_id",
        cerberus_client_secret_path=(
            "app/sustainability/pdh/client_secret"
        ),
    )
)

# Search for Supplied Materials
search_results_supplied_materials: model.SearchResponse = (
    client.get_material_management_search_supplied_materials(
        count=10,
        offset=0,
        supplier_location=[2, 5, 6]
    )
)

# Search for Material Palettes
search_results_material_palettes: model.SearchResponse = (
    client.get_material_management_search_material_palettes(
        count=10,
        offset=10,
        division=[10, 20],
        material_palette_status_indicator=True
    )
)

# Get a Material Palette by ID
material_palette_data: model.MaterialPaletteResponse = (
    client.get_material_management_data_material_palettes_object_id(
        object_id=470,
        dataunits=[
            "mpMaterialColorAndTeamPlayerList",
            "mpParentPalette",
            "mpClassification",
            "mpState"
        ],
    )
)

# Get a Supplied Material's Relationships
relationships: Optional[model.RelationshipResponse] = (
    client.get_material_management_data_supplied_materials_object_id_relationships(
        object_id=101569
    )
)

# Price Unit-of-Measure Reference Data
reference_data: reference_model.ReferencePriceUnitOfMeasurementBulkResponse = (
    client.get_material_procurement_data_reference_price_unit_of_measurements()
)

# Get Material Prices
material_prices_bulk_response: model.MaterialPricesBulkResponse = (
    client.get_material_procurement_data_material_prices(
        object_id=(
            111832, 111325, 110104, 111598, 111563, 101595, 112640, 111819,
            112908, 154668, 111916, 109093, 111738, 114858, 101542, 101553,
            101576, 368148, 101569, 154670
        ),
        dataunits=["supmatPriceCore", "supmatPriceComment"]
    )
)
```

## Updating this Project

If/when you upgrade or add any dependencies to this project, you need to run
`make requirements` before committing (and before testing, even locally, with
tox).

Deployment to Artifactory will occur when your changes are merged into the
"main" branch, however only if you have incremented the version number.

You can increment the version number by changing the **version** parameter's
value in the **metadata** section of [setup.cfg](setup.cfg). Please increment
the minor version with each update, and increment the major version for any
breaking changes.

### Updating API Data Models

- Run `make remodel`
- Increment the minor version of this project in the **version** parameter of
  the **metadata** section of [setup.cfg](setup.cfg).

## Testing

```shell
make test
```
