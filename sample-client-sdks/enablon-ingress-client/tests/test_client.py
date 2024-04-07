import unittest
from datetime import datetime, timedelta
from functools import lru_cache
from typing import Optional

import pytest
import pytz  # type: ignore
import sob
from enablon_client import model as egress_model
from enablon_client.client import Client as EgressClient

from enablon_ingress_client import model as ingress_model
from enablon_ingress_client.client import Client as IngressClient


class TestClient(unittest.TestCase):
    @property  # type: ignore
    @lru_cache()
    def ingress_client(self) -> IngressClient:
        return IngressClient(
            url_cerberus_path="app/sustainability/enablon-ingress/url-uat",
            user_cerberus_path="app/sustainability/enablon-ingress/user-uat",
            password_cerberus_path=(
                "app/sustainability/enablon-ingress/password-uat"
            ),
            echo=False,
        )

    @property  # type: ignore
    @lru_cache()
    def egress_client(self) -> EgressClient:
        return EgressClient(
            url_cerberus_path="app/sustainability/enablon/url-uat",
            user_cerberus_path="app/sustainability/enablon/user-uat",
            password_cerberus_path="app/sustainability/enablon/password-uat",
            echo=False,
        )

    @pytest.mark.first
    def test_update_indicator_value(self) -> None:
        """
        update indicator value in enablon uat
        NOTE: Change the date of the indicator in future if the campaign
        that below indicators are part of is not is draft state
        """
        response: ingress_model.UpdateIndicatorValueResponse = (
            self.ingress_client.update_indicator_value(
                update_indicator_value_request=(
                    ingress_model.UpdateIndicatorValueRequest(
                        fct_name="CS_ImportMetricsData",
                        params=ingress_model.Params(
                            s_entity_code="N.1.10.4.6.1",
                            n_calendar_year=2023,
                            n_calendar_month=3,
                            n_calendar_day=1,
                            an_indicators_ref=(
                                ingress_model.ParamsAnIndicatorsRef(
                                    ("MAT-1.1b", "MAT-1.1c")
                                )
                            ),
                            an_indicators_values=(
                                ingress_model.ParamsAnIndicatorsValues(
                                    ("1.7", "1.8")
                                )
                            ),
                            an_indicators_uom=(
                                ingress_model.ParamsAnIndicatorsUOM(
                                    ("kg", "lb")
                                )
                            ),
                            an_indicators_comments=(
                                ingress_model.ParamsAnIndicatorsComments(
                                    ("", "")
                                )
                            ),
                        ),
                    )
                )
            )
        )
        if response is not None:
            sob.model.validate(response)

    @pytest.mark.second
    def test_validate_updated_indicator_value(self) -> None:
        """
        validate updated indicator value in enablon uat by querying the
        indicators via OData API. Use a narrow filter to avoid returning
        all the indicators.
        """
        sd_entity_data_metadata: Optional[sob.abc.ObjectMeta] = (
            sob.meta.object_read(egress_model.SDEntityData)
        )
        properties: Optional[sob.abc.Properties] = (
            sd_entity_data_metadata.properties  # type: ignore
        )
        assert properties
        assert properties["modified_on"].name
        modified_on_name: str = properties["modified_on"].name

        assert properties["ref"].name
        ref_name: str = properties["ref"].name

        # assuming update was done within the last 2 minutes, through the
        # previous test
        datetime_2_minutes_ago = datetime.now(pytz.utc) - timedelta(minutes=2)

        ref_value_list = [
            (entry.ref, entry.value_number)
            for entry in next(  # type: ignore
                iter(
                    self.egress_client.sd_entities_data(
                        filter=f"{modified_on_name} gt {datetime_2_minutes_ago.isoformat()} and "  # noqa: E501
                        f"({ref_name} eq 'MAT-1.1b' or {ref_name} eq 'MAT-1.1c')"  # noqa: E501
                    )
                )
            ).value
        ]
        assert ("MAT-1.1b", 1.7) in ref_value_list
        assert ("MAT-1.1c", 1.8) in ref_value_list


if __name__ == "__main__":
    unittest.main()
