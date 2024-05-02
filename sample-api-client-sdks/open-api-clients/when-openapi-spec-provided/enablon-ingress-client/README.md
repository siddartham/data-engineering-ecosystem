# enablon-ingress-client

[![test](https://github.com/siddartham/data-engineering-ecosystem/sample-client-sdks/open-api-clients/when-openapi-spec-provided/enablon-ingress-client/actions/workflows/test.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/sample-client-sdks/open-api-clients/when-openapi-spec-provided/enablon-ingress-client/actions/workflows/test.yml)
[![distribute](https://github.com/siddartham/data-engineering-ecosystem/sample-client-sdks/open-api-clients/when-openapi-spec-provided/enablon-ingress-client/actions/workflows/distribute.yml/badge.svg)](https://github.com/siddartham/data-engineering-ecosystem/sample-client-sdks/open-api-clients/when-openapi-spec-provided/enablon-ingress-client/actions/workflows/distribute.yml)

See [CONTRIBUTING.md](./CONTRIBUTING.md) for information pertaining to
development of this package.

## Install

```shell script
pip3 install enablon-ingress-client
```

## Usage

```python
from enablon_ingress_client import model
from logging import Logger, getLogger
from enablon_ingress_client.client import Client

log: Logger = getLogger(__name__)

client: Client = Client(
    # Either a user/password or Cerberus paths
    # to each must be provided
    url_cerberus_path="app/sustainability/enablon-ingress/url-uat",
    user_cerberus_path="app/sustainability/enablon-ingress/user-uat",
    password_cerberus_path=(
        "app/sustainability/enablon-ingress/password-uat"
    ),
    # If provided, API requests and responses will be logged using this logger
    logger=log,
    # If `echo == True`, your API requests and responses will be printed
    # to `sys.stdout` (for debugging, etc.)
    echo=True
)

response: model.UpdateIndicatorValueResponse = (
    client.update_indicator_values(
        update_indicator_value_request=(
            model.UpdateIndicatorValueRequest(
                fct_name="CS_ImportMetricsData",
                params=model.Params(
                    s_entity_code="N.1.10.4.6.1",
                    n_calendar_year=2023,
                    n_calendar_month=3,
                    n_calendar_day=1,
                    an_indicators_ref=(
                        model.ParamsAnIndicatorsRef(
                            ("MAT-1.1b", "MAT-1.1c")
                        )
                    ),
                    an_indicators_values=(
                        model.ParamsAnIndicatorsValues(
                            ("1.7", "1.8")
                        )
                    ),
                    an_indicators_uom=(
                        model.ParamsAnIndicatorsUOM(
                            ("kg", "lb")
                        )
                    ),
                    an_indicators_comments=(
                        model.ParamsAnIndicatorsComments(
                            ("", "")
                        )
                    ),
                ),
            )
        )
    )
)

print(response)
```
Executing the snippet above prints the following:

```text
enablon_ingress_client.model.UpdateIndicatorValueResponse(
    status='OK',
    login=1,
    data='Response|200\\r\\nMAT-1.1b| Indicator updated successfully.\\r\\nMAT-1.1c| Indicator updated successfully.'
)
```
