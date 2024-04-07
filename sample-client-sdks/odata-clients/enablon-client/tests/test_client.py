import csv
import functools
import os
import pickle
import unittest
import sob
from pathlib import Path
from typing import Any, Optional, Tuple
from nike.enablon_client import model
from nike.enablon_client.client import Client

PROJECT_PATH: Path = Path(__file__).absolute().parent.parent
lru_cache: Any = functools.lru_cache


class TestClient(unittest.TestCase):
    @property  # type: ignore
    @lru_cache()
    def client(self) -> Client:
        return Client(
            url_cerberus_path="app/sustainability/enablon/url-prod",
            user_cerberus_path="app/sustainability/enablon/user-prod",
            password_cerberus_path=(
                "app/sustainability/enablon/password-prod"
            ),
            echo=False,
        )

    def test_pickle(self) -> None:
        """
        Verify that the client is pickle-able
        """
        self.client.get()
        pickle.loads(pickle.dumps(self.client))

    def test_get(self) -> None:
        service_root: model.ServiceRootResponse = self.client.get()
        assert isinstance(service_root, model.ServiceRootResponse)
        sob.test.json(service_root)

    def test_services(self) -> None:
        service_root: model.ServiceRootResponse = self.client.get()
        service: model.ServiceRoot
        data_directory: Path = PROJECT_PATH.joinpath("tests", ".data")
        os.makedirs(data_directory, exist_ok=True)
        if service_root.value:
            for service in service_root.value:
                if service.kind == "EntitySet" and service.name:
                    try:
                        response_data: Any = next(
                            iter(
                                getattr(
                                    self.client,
                                    sob.utilities.string.property_name(
                                        service.name
                                    ),
                                )()
                            )
                        )
                    except AttributeError:
                        continue
                    sob.model.validate(response_data)
                    sob.model.replace_nulls(response_data)
                    if response_data.value and response_data.value[0]:
                        metadata: Optional[
                            sob.abc.ObjectMeta
                        ] = sob.meta.object_read(response_data.value[0])
                        if metadata is None:
                            raise ValueError(
                                "No metadata found for rows returned by "
                                f"the service: {service.name}\n"
                                "Most likely, you need to run "
                                "`make force-remodel` to refresh your models."
                            )
                        with open(
                            data_directory.joinpath(f"{service.name}.csv"),
                            "w",
                            encoding="utf-8",
                        ) as response_data_io:
                            writer: Any = csv.writer(response_data_io)
                            if metadata.properties:
                                writer.writerow(
                                    property_.name
                                    for property_ in (
                                        metadata.properties.values()
                                    )
                                )
                                property_names: Tuple[str, ...] = tuple(
                                    metadata.properties.keys()
                                )
                                writer.writerows(
                                    (
                                        getattr(row, property_name_)
                                        for property_name_ in property_names
                                    )
                                    for row in response_data.value
                                )

    def test_filter_orderby(self) -> None:
        next(
            iter(
                self.client.sd_entities_data(
                    orderby="ReportingPeriod desc", top=1
                )
            )
        )
        next(
            iter(
                self.client.sd_entities_data(
                    orderby="ReportingPeriod asc", top=1
                )
            )
        )
        next(
            iter(
                self.client.sd_entities_data(
                    filter="ReportingPeriod eq null", top=1
                )
            )
        )
        next(
            iter(
                self.client.sd_entities_data(
                    filter="ReportingPeriod eq 2020-06-01", top=10
                )
            )
        )


if __name__ == "__main__":
    unittest.main()
