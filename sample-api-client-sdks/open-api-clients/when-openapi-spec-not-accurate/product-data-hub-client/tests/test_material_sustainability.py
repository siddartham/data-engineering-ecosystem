import base64
import functools
import json
import pickle
import unittest
from typing import Callable

from pyspark import cloudpickle  # type: ignore

from my.product_data_hub_client.material_sustainability.client import Client
from my.product_data_hub_client.material_sustainability.model import (
    PDHStreamAdaptorItems,
    PDHStreamAdaptorItemsChanges,
    PDHStreamAdaptorItemsEntitlements,
    PdhStreamsAdaptorDataPut0,
)

sustainability_client_lru_cache: Callable[
    [], Callable[..., Callable[..., Client]]
] = functools.lru_cache  # type: ignore


class TestMaterialSustainability(unittest.TestCase):
    @property  # type: ignore
    @sustainability_client_lru_cache()
    def client(self) -> Client:
        return Client(
            url=(
                "https://"
                "materialmanagement.api-product.pes-preprod.my.com/stg/v1"
            ),
            oauth2_token_url="https://api.aegis.nikecloud.com/v1/qa/token",
            api_key_cerberus_path="app/sustainability/pdh/stg-x-api-key",
            oauth2_client_id_cerberus_path="app/sustainability/pdh/client_id",
            oauth2_client_secret_cerberus_path=(
                "app/sustainability/pdh/dev_client_secret"
            ),
            timeout=60,
            echo=False,
        )

    def test_pickle(self) -> None:
        """
        Verify that the client is pickle-able
        """
        pickle.loads(pickle.dumps(self.client))
        cloudpickle.loads(cloudpickle.dumps(self.client))

    def test_put_pdh_streams_adaptor_data(self) -> None:
        items: PDHStreamAdaptorItems = PDHStreamAdaptorItems(
            domain="MM",
            event_type="UPDATE",
            source_system="Sustainability",
            object_id="354535",
            object_type="MSI_SCORE",
            object_version=1683866962083,
            api_version=1,
            correlation_id="1683870238351",
            changes=PDHStreamAdaptorItemsChanges(),
            entitlements=PDHStreamAdaptorItemsEntitlements(),
            full_object=base64.b64encode(
                json.dumps(
                    {
                        "suppliedMaterialSustainabilityScore": 10.0,
                        "suppliedMaterialIdentifier": 12343,
                        "carbonFootprintKgCO2ePerKg": 26.0,
                        "nikeSustainabilityRanking": (
                            "Test Nike Sustainbility Ranking"
                        ),
                        "nikeSustainabilityRankingDescription": (
                            "Test Nike Sustainbility Ranking Description"
                        ),
                    }
                ).encode("utf-8")
            ).decode("utf-8"),
        )
        self.client.put_pdh_streams_adaptor_data(
            PdhStreamsAdaptorDataPut0(items=[items])
        )


if __name__ == "__main__":
    unittest.main()
