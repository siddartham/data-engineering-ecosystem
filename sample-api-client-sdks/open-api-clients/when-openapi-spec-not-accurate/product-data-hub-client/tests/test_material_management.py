import functools
import pickle
import unittest
from json import JSONDecodeError
from typing import Any, Callable, Iterable, Optional, Set, Type, Union
from urllib.error import HTTPError

import sob
from more_itertools import ichunked
from pyspark import cloudpickle  # type: ignore
from sob.utilities import properties_values

from product_data_hub_client.line_management.reference_model import (
    Links as LineManagementLinks,
)
from product_data_hub_client.material_management.client import Client
from product_data_hub_client.material_management.model import (
    Links as MaterialManagementLinks,
)
from product_data_hub_client.material_management.model import (
    MaterialManagementDataMaterialPalettesGetDataunits,
    MaterialManagementDataMaterialPalettesGetObjectId,
    MaterialManagementDataMaterialPalettesObjectIdGetDataunits,
    MaterialManagementDataSuppliedMaterialBOMsGetDataunits,
    MaterialManagementDataSuppliedMaterialBOMsGetObjectId,
    MaterialManagementDataSuppliedMaterialsObjectIdGetDataunits,
    MaterialManagementSearchMaterialPalettesGetDivision,
    MaterialPaletteBulkResponse,
    MaterialPaletteResponse,
    MaterialPricesBulkResponse,
    MaterialProcurementDataMaterialPricesGetDataunits,
    MaterialProcurementDataMaterialPricesGetObjectId,
    MaterialTypeBulkResponse,
    MaterialTypeBulkResponseContent,
    MaterialTypeBulkResponseContents,
    Reference,
    RelationshipResponse,
    SearchResponse,
    SearchResponseContent,
    SearchResponseContents,
    SuppliedMaterialBOMBulkResponse,
    SuppliedMaterialResponse,
)
from product_data_hub_client.material_management.reference_client import (
    ReferenceClient,
)
from product_data_hub_client.material_management.reference_model import (  # noqa
    AnimalSourceBulkResponse,
    AnimalSourceBulkResponseContent,
    AnimalSourceBulkResponseContents,
    ApplicationLocationBulkResponse,
    ApplicationLocationBulkResponseContent,
    ApplicationLocationBulkResponseContents,
    ArtworkTechniqueBulkResponse,
    ArtworkTechniqueBulkResponseContent,
    ArtworkTechniqueBulkResponseContents,
    ChemicalPolymerTypeBulkResponse,
    ChemicalPolymerTypeBulkResponseContent,
    ChemicalPolymerTypeBulkResponseContents,
    ComponentConstructionTypeBulkResponse,
    ComponentConstructionTypeBulkResponseContent,
    ComponentConstructionTypeBulkResponseContents,
    ComponentTypeBulkResponse,
    ComponentTypeBulkResponseContent,
    ComponentTypeBulkResponseContents,
    ContentSourceBulkResponse,
    ContentSourceBulkResponseContent,
    ContentSourceBulkResponseContents,
    ContentTypeBulkResponse,
    ContentTypeBulkResponseContent,
    ContentTypeBulkResponseContents,
    CushioningTypeBulkResponse,
    CushioningTypeBulkResponseContents,
    CushioningTypeResponseContent,
    DimensionWidthIndicatorBulkResponse,
    DimensionWidthIndicatorBulkResponseContent,
    DimensionWidthIndicatorBulkResponseContents,
    DyeMethodBulkResponse,
    DyeMethodBulkResponseContent,
    DyeMethodBulkResponseContents,
    DyeTypeBulkResponse,
    DyeTypeBulkResponseContent,
    DyeTypeBulkResponseContents,
    FinishProcessBulkResponse,
    FinishProcessBulkResponseContent,
    FinishProcessBulkResponseContents,
    HardOrSoftComponentBulkResponse,
    HardOrSoftComponentBulkResponseContent,
    HardOrSoftComponentBulkResponseContents,
    MaterialEndUseBulkResponse,
    MaterialEndUseBulkResponseContent,
    MaterialEndUseBulkResponseContents,
    MaterialPaletteStateBulkResponse,
    MaterialPricingModeBulkResponse,
    MaterialPricingModeBulkResponseContent,
    MaterialPricingModeBulkResponseContents,
    MaterialTechnologyBulkResponse,
    MaterialTechnologyBulkResponseContent,
    MaterialTechnologyBulkResponseContents,
    MethodOfMakeBulkResponse,
    MethodOfMakeBulkResponseContent,
    MethodOfMakeBulkResponseContents,
    NonWovenSubstrateTypeBulkResponse,
    NonWovenSubstrateTypeBulkResponseContent,
    NonWovenSubstrateTypeBulkResponseContents,
    NonWovenWebBondingMethodBulkResponse,
    NonWovenWebBondingMethodBulkResponseContent,
    NonWovenWebBondingMethodBulkResponseContents,
    PaletteTypeBulkResponse,
    ReferencePriceUnitOfMeasurementBulkResponse,
    ReTannageBulkResponse,
    ReTannageBulkResponseContent,
    ReTannageBulkResponseContents,
    ScrimBulkResponse,
    ScrimBulkResponseContent,
    ScrimBulkResponseContents,
    SubstrateConstructionBulkResponse,
    SubstrateConstructionBulkResponseContent,
    SubstrateConstructionBulkResponseContents,
    SuppliedMaterialStateBulkResponse,
    SuppliedMaterialStateBulkResponseContent,
    SuppliedMaterialStateBulkResponseContents,
    TextileConstructionTypeBulkResponse,
    TextileConstructionTypeBulkResponseContent,
    TextileConstructionTypeBulkResponseContents,
    TextileVariationBulkResponse,
    TextileVariationBulkResponseContent,
    TextileVariationBulkResponseContents,
    ThicknessBulkResponse,
    ThicknessBulkResponseContent,
    ThicknessBulkResponseContents,
    VisualMaterialNameVariationBulkResponse,
    VisualMaterialNameVariationBulkResponseContent,
    VisualMaterialNameVariationBulkResponseContents,
    WebFormationBulkResponse,
    WebFormationBulkResponseContent,
    WebFormationBulkResponseContents,
    WeightMaterialNameVariationBulkResponse,
    WeightMaterialNameVariationBulkResponseContent,
    WeightMaterialNameVariationBulkResponseContents,
    YarnPlyBrandBulkResponse,
    YarnPlyBrandBulkResponseContent,
    YarnPlyBrandBulkResponseContents,
    YarnPlyNumberSystemBulkResponse,
    YarnPlyNumberSystemBulkResponseContent,
    YarnPlyNumberSystemBulkResponseContents,
    YarnPlySpinningMethodBulkResponse,
    YarnPlySpinningMethodBulkResponseContent,
    YarnPlySpinningMethodBulkResponseContents,
    YarnPlyTextureBulkResponse,
    YarnPlyTextureBulkResponseContent,
    YarnPlyTextureBulkResponseContents,
    YarnPlyTypeBulkResponse,
    YarnPlyTypeBulkResponseContent,
    YarnPlyTypeBulkResponseContents,
)
from product_data_hub_client.utilities import lru_cache


def _get_search_response_content_reference_key(
    search_response_content: SearchResponseContent,
) -> int:
    assert isinstance(search_response_content.relationships, Reference)
    assert isinstance(search_response_content.relationships.reference_key, str)
    return int(search_response_content.relationships.reference_key)


client_lru_cache: Callable[
    [], Callable[..., Callable[..., Client]]
] = functools.lru_cache  # type: ignore
reference_client_lru_cache: Callable[
    [], Callable[..., Callable[..., ReferenceClient]]
] = functools.lru_cache  # type: ignore


class TestMaterialManagement(unittest.TestCase):
    @property  # type: ignore
    @client_lru_cache()
    def client(self) -> Client:
        return Client(
            api_key_cerberus_path="app/sustainability/pdh/x-api-key",
            oauth2_client_id_cerberus_path="app/sustainability/pdh/client_id",
            oauth2_client_secret_cerberus_path=(
                "app/sustainability/pdh/client_secret"
            ),
            timeout=60,
            echo=False,
        )

    @property  # type: ignore
    @reference_client_lru_cache()
    def reference_client(self) -> ReferenceClient:
        return ReferenceClient(
            api_key_cerberus_path="app/sustainability/pdh/x-api-key",
            oauth2_client_id_cerberus_path="app/sustainability/pdh/client_id",
            oauth2_client_secret_cerberus_path=(
                "app/sustainability/pdh/client_secret"
            ),
            timeout=60,
            echo=False,
        )

    def test_pickle(self) -> None:
        """
        Verify that the client is pickle-able
        """
        self._search_material_palettes()
        self._get_material_management_search_supplied_materials()
        pickle.loads(
            pickle.dumps(self.client)
        ).get_material_management_search_material_palettes(count=1)
        cloudpickle.loads(
            cloudpickle.dumps(self.client)
        ).get_material_management_search_material_palettes(count=1)
        pickle.loads(
            pickle.dumps(self.reference_client)
        ).get_material_management_data_material_palette_states()
        cloudpickle.loads(
            cloudpickle.dumps(self.reference_client)
        ).get_material_management_data_material_palette_states()

    @lru_cache()
    def _search_material_palettes(self) -> SearchResponse:
        return self.client.get_material_management_search_material_palettes(
            count=20,
            division=MaterialManagementSearchMaterialPalettesGetDivision(
                ["10", "20"]
            ),
            material_palette_status_indicator=True,
        )

    @lru_cache()
    def _get_material_management_search_supplied_materials(
        self,
    ) -> SearchResponse:
        return self.client.get_material_management_search_supplied_materials(
            count=20, offset=0, supplier_location=[2, 5, 6]
        )

    def _validate_link(
        self,
        model: Union[
            MaterialManagementLinks,
            LineManagementLinks,
        ],
        traversed: Optional[Set[int]] = None,
    ) -> None:
        if model.rel != "self":
            dereferenced_model: Optional[sob.abc.Model] = None
            # Check to ensure that the link relationships are
            # implemented, then continue recursion
            try:
                dereferenced_model = self.client.get_link(model)
            except HTTPError as http_error:
                # Some link types are known to produce specific types of
                # errors, so below we catch the errors which are known
                # to exist, while raising any *unanticipated* errors
                if not (
                    isinstance(model.href, str)
                    and "/" in model.href
                    and (
                        # If the entity is missing, there isn't much
                        # we can do about that...
                        http_error.code == 404
                        or (
                            # We don't currently have permission to access
                            # color management
                            http_error.code == 403
                            and model.href.split("/")[-2] == "colors"
                        )
                    )
                ):
                    raise
            if dereferenced_model:
                self._validate_links(dereferenced_model, traversed)

    def _validate_links(
        self, model: Any, traversed: Optional[Set[int]] = None
    ) -> None:
        """
        This method recursively traverses model instances, and retrieves
        references, in order to ensure each reference type needed is supported.
        Note: Each type of model is only traversed once.
        """
        # To facilitate more concise recursion, this method accepts any
        # value for the `model` argument, but only *validates* model instances
        if not isinstance(model, sob.abc.Model):
            return None
        model_hash: int = (
            # hash(model)
            hash(sob.utilities.inspect.qualified_name(type(model)))
        )
        if traversed is None:
            traversed = {model_hash}
        else:
            if model_hash in traversed:
                # If we've already validated this model,
                # we don't need to validate it again
                return None
            else:
                traversed.add(model_hash)
        if isinstance(
            model,
            (
                MaterialManagementLinks,
                LineManagementLinks,
            ),
        ):
            self._validate_link(model, traversed)
        else:
            # Recursively look for links
            key: str
            value: sob.abc.MarshallableTypes
            if isinstance(model, sob.abc.Object):
                for key, value in properties_values(model):
                    self._validate_links(value, traversed)
            elif isinstance(model, sob.abc.Array):
                for value in model:
                    self._validate_links(value, traversed)
            else:
                assert isinstance(model, sob.abc.Dictionary)
                for value in model.values():
                    self._validate_links(value, traversed)

    def _validate_search_response(
        self,
        search_response: SearchResponse,
        item_relationship_class: Optional[Type[sob.abc.Model]] = None,
    ) -> None:
        assert isinstance(search_response, SearchResponse)
        sob.model.validate(search_response)
        item: SearchResponseContent
        assert isinstance(search_response.content, SearchResponseContents)
        traversed: Set[int] = set()
        for item in search_response.content:
            assert isinstance(item.relationships, Reference)
            assert isinstance(
                item.relationships.link,
                (
                    MaterialManagementLinks,
                    LineManagementLinks,
                ),
            )
            response: sob.abc.Model = self.client.get_link(
                item.relationships.link
            )
            if item_relationship_class is not None:
                assert isinstance(response, item_relationship_class)
            self._validate_links(response, traversed)

    def test_get_material_management_search_supplied_materials(self) -> None:
        """
        Test the method used to search against all fields in the
        Supplied Material entity
        """
        self._validate_search_response(
            self._get_material_management_search_supplied_materials(),
            SuppliedMaterialResponse,
        )

    def test_get_material_management_data_supplied_materials_object_id(
        self,
    ) -> None:
        search_response: SearchResponse = (
            self._get_material_management_search_supplied_materials()
        )
        assert isinstance(search_response.content, SearchResponseContents)
        search_response_content: SearchResponseContent
        for search_response_content in search_response.content:
            assert isinstance(search_response_content.relationships, Reference)
            assert isinstance(
                search_response_content.relationships.reference_key, str
            )
            supplied_material_response: SuppliedMaterialResponse = (
                self.client
            ).get_material_management_data_supplied_materials_object_id(
                object_id=int(
                    search_response_content.relationships.reference_key
                ),
                dataunits=MaterialManagementDataSuppliedMaterialsObjectIdGetDataunits(  # noqa
                    [
                        "supmatCore",
                        "supmatLeather",
                        "supmatContent",
                        "supmatChemPoly",
                        "supmatYarnCompositionBreakdown",
                        "supmatYarn",
                        "supmatPlyCompositionBreakdown",
                        "supmatNonWovenProperties",
                        "supmatInsulationAndPadding",
                        "supmatTextiles",
                        "supmatFinishes",
                        "supmatColorAndDye",
                        "supmatArtworkGraphic",
                        "supmatDimension",
                        "supmatCore",
                        "supmatWebFormation",
                        "supmatSyntheticLeather",
                        "supmatLegacyNumber",
                        "matClassification",
                        "supmatInitialSeason",
                        "supmatComponentZipper",
                        "supmatFamily",
                        "supmatComponent",
                        "supmatComponentTapeSnapTape",
                        "supmatComponentDrawcordAglet",
                        "supmatComponentLabel",
                        "supmatComponentLace",
                        "supmatLabelAndPackagingProperties",
                        "supmatState",
                        "supmatStatus",
                        "supmatOwner",
                        "supmatPPS",
                        "supmatInitialPrice",
                        "matTargetPrice",
                        "supmatMCSNumber",
                        "supmatDesignUsageSpecification",
                        "supmatCushioning",
                    ]
                ),
            )
            sob.model.validate(supplied_material_response)
            self._validate_links(supplied_material_response)

    def test_get_material_management_data_material_palette_states(
        self,
    ) -> None:
        """
        Test the method used to get all material palette states
        """
        mp_state_bulk_response: MaterialPaletteStateBulkResponse = (
            self.reference_client
        ).get_material_management_data_material_palette_states()
        sob.model.validate(mp_state_bulk_response)

    def test_get_material_management_data_palette_types(
        self,
    ) -> None:
        """
        Test the method used to get all palette types
        """
        palette_type_bulk_response: PaletteTypeBulkResponse = (
            self.reference_client.get_material_management_data_palette_types()
        )
        sob.model.validate(palette_type_bulk_response)

    def test_get_material_management_search_material_palettes(self) -> None:
        """
        Test the method used to search against all fields in the
        Material Palette entity
        """
        self._validate_search_response(
            self._search_material_palettes(), MaterialPaletteResponse
        )

    def test_get_material_management_data_material_palettes_object_id(
        self,
    ) -> None:
        """
        Test the method used to get a single palette data for material and
        material color.
        """
        search_response: SearchResponse = self._search_material_palettes()
        assert isinstance(search_response.content, SearchResponseContents)
        search_response_content: SearchResponseContent
        for search_response_content in search_response.content:
            assert isinstance(search_response_content.relationships, Reference)
            assert isinstance(
                search_response_content.relationships.reference_key, str
            )
            material_palette_response: MaterialPaletteResponse = (
                self.client
            ).get_material_management_data_material_palettes_object_id(
                object_id=int(
                    search_response_content.relationships.reference_key
                ),
                dataunits=MaterialManagementDataMaterialPalettesObjectIdGetDataunits(  # noqa
                    [  # noqa
                        "mpMaterialColorAndTeamPlayerList",
                        "mpParentPalette",
                        "mpClassification",
                        "mpState",
                    ]
                ),
            )
            sob.model.validate(material_palette_response)
            self._validate_links(material_palette_response)

    def test_get_material_management_data_supplied_materials_object_id_rels(
        self,
    ) -> None:
        """
        Test the method used to get all the relationships of a supplied
        material
        """
        search_response: SearchResponse = (
            self._get_material_management_search_supplied_materials()
        )
        assert isinstance(search_response.content, SearchResponseContents)
        search_response_content: SearchResponseContent
        for search_response_content in search_response.content:
            assert isinstance(search_response_content.relationships, Reference)
            assert isinstance(
                search_response_content.relationships.reference_key, str
            )
            try:
                relationships_response: RelationshipResponse = (
                    self.client
                ).get_material_management_data_supplied_materials_object_id_relationships(  # noqa
                    object_id=int(
                        search_response_content.relationships.reference_key
                    )
                )
            except JSONDecodeError as error:
                # Only raise an error if a non-empty response was returned
                if len(error.doc):
                    raise
                else:
                    continue
            assert isinstance(relationships_response, RelationshipResponse)
            sob.model.validate(relationships_response)
            self._validate_links(relationships_response)

    def test_get_material_procurement_data_reference_price_unit_of_measurements(  # noqa
        self,
    ) -> None:
        """
        Test the method used to get all the reference data associated with
        referencePriceUnitOfMeasurements
        """
        bulk_response: ReferencePriceUnitOfMeasurementBulkResponse = (
            self.reference_client
        ).get_material_procurement_data_reference_price_unit_of_measurements()
        assert isinstance(
            bulk_response,
            ReferencePriceUnitOfMeasurementBulkResponse,
        )
        sob.model.validate(bulk_response)
        self._validate_links(bulk_response)

    def test_get_material_procurement_data_material_prices(
        self,
    ) -> None:
        """
        Test the method used for getting material prices in bulk
        """
        search_response: SearchResponse = (
            self.client.get_material_management_search_supplied_materials(
                count=20,
                offset=0,  # supplier_location=[2, 5, 6]
            )
        )
        assert isinstance(search_response.content, SearchResponseContents)
        search_response_content: SearchResponseContent
        bulk_response: MaterialPricesBulkResponse = (
            # got the id data from supplied material API
            self.client.get_material_procurement_data_material_prices(
                object_id=MaterialProcurementDataMaterialPricesGetObjectId(
                    map(
                        lambda search_response_content: int(
                            search_response_content.relationships.reference_key
                        ),
                        search_response.content,
                    )
                ),
                dataunits=MaterialProcurementDataMaterialPricesGetDataunits(
                    (
                        "supmatPriceCore",
                        "supmatPriceComment",
                        "supmatPriceDetails",
                    )
                ),
            )
        )
        assert isinstance(bulk_response, MaterialPricesBulkResponse)
        sob.model.validate(bulk_response)
        self._validate_links(bulk_response)

    def _test_get_material_management_data_supplied_material_boms(
        self,
    ) -> None:
        """
        Test the method used for getting material prices in bulk
        """
        search_response: SearchResponse = (
            self.client.get_material_management_search_supplied_materials(
                count=20,
                offset=0,
            )
        )
        assert isinstance(search_response.content, SearchResponseContents)
        search_response_content: SearchResponseContent
        bulk_response: SuppliedMaterialBOMBulkResponse = (
            # got the id data from supplied material API
            self.client.get_material_management_data_supplied_material_boms(
                object_id=(
                    MaterialManagementDataSuppliedMaterialBOMsGetObjectId(
                        map(
                            lambda search_response_content: int(
                                (
                                    search_response_content
                                ).relationships.reference_key
                            ),
                            search_response.content,
                        )
                    )
                ),
                dataunits=(
                    MaterialManagementDataSuppliedMaterialBOMsGetDataunits(
                        (
                            "supmatBomCore",
                            "supmatBomComment",
                        )
                    )
                ),
            )
        )
        assert isinstance(bulk_response, SuppliedMaterialBOMBulkResponse)
        sob.model.validate(bulk_response)
        self._validate_links(bulk_response)

    def test_get_material_management_data_material_palettes(self) -> None:
        search_response: SearchResponse = self._search_material_palettes()
        assert isinstance(search_response.content, SearchResponseContents)
        object_ids: Iterable[int]
        # We break up the object IDs into chunks of no more than 3
        # because PDH throws an error when attempting to retrieve too
        # many at once
        for object_ids in ichunked(
            map(
                _get_search_response_content_reference_key,
                search_response.content,
            ),
            3,
        ):
            material_palette_bulk_response: MaterialPaletteBulkResponse = (
                self.client.get_material_management_data_material_palettes(
                    object_id=(
                        MaterialManagementDataMaterialPalettesGetObjectId(
                            object_ids
                        )
                    ),
                    dataunits=(
                        MaterialManagementDataMaterialPalettesGetDataunits(
                            (
                                "mpMaterialColorAndTeamPlayerList",
                                "mpParentPalette",
                                "mpClassification",
                                "mpState",
                            )
                        )
                    ),
                )
            )
            sob.model.validate(material_palette_bulk_response)

    @lru_cache()
    def _get_material_management_data_animal_sources(
        self,
    ) -> AnimalSourceBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_animal_sources()

    def test_get_material_management_data_animal_sources(self) -> None:
        sob.model.validate(self._get_material_management_data_animal_sources())

    def test_get_material_management_data_animal_sources_object_id(
        self,
    ) -> None:
        bulk_response: AnimalSourceBulkResponse = (
            self._get_material_management_data_animal_sources()
        )
        assert isinstance(
            bulk_response.content, AnimalSourceBulkResponseContents
        )
        content: AnimalSourceBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_animal_sources_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_application_locations(
        self,
    ) -> ApplicationLocationBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_application_locations()

    def test_get_material_management_data_application_locations(self) -> None:
        sob.model.validate(
            self._get_material_management_data_application_locations()
        )

    def test_get_material_management_data_application_locations_object_id(
        self,
    ) -> None:
        bulk_response: ApplicationLocationBulkResponse = (
            self._get_material_management_data_application_locations()
        )
        assert isinstance(
            bulk_response.content, ApplicationLocationBulkResponseContents
        )
        content: ApplicationLocationBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_application_locations_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_artwork_techniques(
        self,
    ) -> ArtworkTechniqueBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_artwork_techniques()

    def test_get_material_management_data_artwork_techniques(self) -> None:
        sob.model.validate(
            self._get_material_management_data_artwork_techniques()
        )

    def test_get_material_management_data_artwork_techniques_object_id(
        self,
    ) -> None:
        bulk_response: ArtworkTechniqueBulkResponse = (
            self._get_material_management_data_artwork_techniques()
        )
        assert isinstance(
            bulk_response.content, ArtworkTechniqueBulkResponseContents
        )
        content: ArtworkTechniqueBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_artwork_techniques_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_component_construction_types(
        self,
    ) -> ComponentConstructionTypeBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_component_construction_types()

    def test_get_material_management_data_component_construction_types(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_component_construction_types()
        )

    def test_get_material_management_data_component_construction_types_object_id(  # noqa
        self,
    ) -> None:
        bulk_response: ComponentConstructionTypeBulkResponse = (
            self._get_material_management_data_component_construction_types()
        )
        assert isinstance(
            bulk_response.content,
            ComponentConstructionTypeBulkResponseContents,
        )
        content: ComponentConstructionTypeBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_component_construction_types_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_component_types(
        self,
    ) -> ComponentTypeBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_component_types()

    def test_get_material_management_data_component_types(self) -> None:
        sob.model.validate(
            self._get_material_management_data_component_types()
        )

    def test_get_material_management_data_component_types_object_id(
        self,
    ) -> None:
        bulk_response: ComponentTypeBulkResponse = (
            self._get_material_management_data_component_types()
        )
        assert isinstance(
            bulk_response.content, ComponentTypeBulkResponseContents
        )
        content: ComponentTypeBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_component_types_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_content_sources(
        self,
    ) -> ContentSourceBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_content_sources()

    def test_get_material_management_data_content_sources(self) -> None:
        sob.model.validate(
            self._get_material_management_data_content_sources()
        )

    def test_get_material_management_data_content_sources_object_id(
        self,
    ) -> None:
        bulk_response: ContentSourceBulkResponse = (
            self._get_material_management_data_content_sources()
        )
        assert isinstance(
            bulk_response.content, ContentSourceBulkResponseContents
        )
        content: ContentSourceBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_content_sources_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_content_types(
        self,
    ) -> ContentTypeBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_content_types()

    def test_get_material_management_data_content_types(self) -> None:
        sob.model.validate(self._get_material_management_data_content_types())

    def test_get_material_management_data_content_types_object_id(
        self,
    ) -> None:
        bulk_response: ContentTypeBulkResponse = (
            self._get_material_management_data_content_types()
        )
        assert isinstance(
            bulk_response.content, ContentTypeBulkResponseContents
        )
        content: ContentTypeBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_content_types_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_dimension_width_indicators(
        self,
    ) -> DimensionWidthIndicatorBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_dimension_width_indicators()

    def test_get_material_management_data_dimension_width_indicators(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_dimension_width_indicators()
        )

    def test_get_material_management_data_dimension_width_indicators_object_id(
        self,
    ) -> None:
        bulk_response: DimensionWidthIndicatorBulkResponse = (
            self._get_material_management_data_dimension_width_indicators()
        )
        assert isinstance(
            bulk_response.content, DimensionWidthIndicatorBulkResponseContents
        )
        content: DimensionWidthIndicatorBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_dimension_width_indicators_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_dye_methods(
        self,
    ) -> DyeMethodBulkResponse:
        return self.reference_client.get_material_management_data_dye_methods()

    def test_get_material_management_data_dye_methods(
        self,
    ) -> None:
        sob.model.validate(self._get_material_management_data_dye_methods())

    def test_get_material_management_data_dye_methods_object_id(
        self,
    ) -> None:
        bulk_response: DyeMethodBulkResponse = (
            self._get_material_management_data_dye_methods()
        )
        assert isinstance(bulk_response.content, DyeMethodBulkResponseContents)
        content: DyeMethodBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_dye_methods_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_dye_types(
        self,
    ) -> DyeTypeBulkResponse:
        return self.reference_client.get_material_management_data_dye_types()

    def test_get_material_management_data_dye_types(
        self,
    ) -> None:
        sob.model.validate(self._get_material_management_data_dye_types())

    def test_get_material_management_data_dye_types_object_id(
        self,
    ) -> None:
        bulk_response: DyeTypeBulkResponse = (
            self._get_material_management_data_dye_types()
        )
        assert isinstance(bulk_response.content, DyeTypeBulkResponseContents)
        content: DyeTypeBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_dye_types_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_finish_processes(
        self,
    ) -> FinishProcessBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_finish_processes()

    def test_get_material_management_data_finish_processes(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_finish_processes()
        )

    def test_get_material_management_data_finish_processes_object_id(
        self,
    ) -> None:
        bulk_response: FinishProcessBulkResponse = (
            self._get_material_management_data_finish_processes()
        )
        assert isinstance(
            bulk_response.content, FinishProcessBulkResponseContents
        )
        content: FinishProcessBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_finish_processes_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_hard_or_soft_components(
        self,
    ) -> HardOrSoftComponentBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_hard_or_soft_components()  # noqa

    def test_get_material_management_data_hard_or_soft_components(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_hard_or_soft_components()
        )

    def test_get_material_management_data_hard_or_soft_components_object_id(
        self,
    ) -> None:
        bulk_response: HardOrSoftComponentBulkResponse = (
            self._get_material_management_data_hard_or_soft_components()
        )
        assert isinstance(
            bulk_response.content, HardOrSoftComponentBulkResponseContents
        )
        content: HardOrSoftComponentBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_hard_or_soft_components_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_material_end_uses(
        self,
    ) -> MaterialEndUseBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_material_end_uses()

    def test_get_material_management_data_material_end_uses(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_material_end_uses()
        )

    def test_get_material_management_data_material_end_uses_object_id(
        self,
    ) -> None:
        bulk_response: MaterialEndUseBulkResponse = (
            self._get_material_management_data_material_end_uses()
        )
        assert isinstance(
            bulk_response.content, MaterialEndUseBulkResponseContents
        )
        content: MaterialEndUseBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_material_end_uses_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_material_pricing_modes(
        self,
    ) -> MaterialPricingModeBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_material_pricing_modes()

    def test_get_material_management_data_material_pricing_modes(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_material_pricing_modes()
        )

    def test_get_material_management_data_material_pricing_modes_object_id(
        self,
    ) -> None:
        bulk_response: MaterialPricingModeBulkResponse = (
            self._get_material_management_data_material_pricing_modes()
        )
        assert isinstance(
            bulk_response.content, MaterialPricingModeBulkResponseContents
        )
        content: MaterialPricingModeBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_material_pricing_modes_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_material_technologies(
        self,
    ) -> MaterialTechnologyBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_material_technologies()

    def test_get_material_management_data_material_technologies(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_material_technologies()
        )

    def test_get_material_management_data_material_technologies_object_id(
        self,
    ) -> None:
        bulk_response: MaterialTechnologyBulkResponse = (
            self._get_material_management_data_material_technologies()
        )
        assert isinstance(
            bulk_response.content, MaterialTechnologyBulkResponseContents
        )
        content: MaterialTechnologyBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_material_technologies_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_chemical_polymer_types(
        self,
    ) -> ChemicalPolymerTypeBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_chemical_polymer_types()

    def test_get_material_management_data_chemical_polymer_types(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_chemical_polymer_types()
        )

    def test_get_material_management_data_chemical_polymer_types_object_id(
        self,
    ) -> None:
        bulk_response: ChemicalPolymerTypeBulkResponse = (
            self._get_material_management_data_chemical_polymer_types()
        )
        assert isinstance(
            bulk_response.content, ChemicalPolymerTypeBulkResponseContents
        )
        content: ChemicalPolymerTypeBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_chemical_polymer_types_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_material_types(
        self,
    ) -> MaterialTypeBulkResponse:
        return self.client.get_material_management_data_material_types()

    def test_get_material_management_data_material_types(
        self,
    ) -> None:
        sob.model.validate(self._get_material_management_data_material_types())

    def test_get_material_management_data_material_types_object_id(
        self,
    ) -> None:
        bulk_response: MaterialTypeBulkResponse = (
            self._get_material_management_data_material_types()
        )
        assert isinstance(
            bulk_response.content, MaterialTypeBulkResponseContents
        )
        content: MaterialTypeBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.client
                ).get_material_management_data_material_types_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_search_materials(
        self,
    ) -> SearchResponse:
        return self.client.get_material_management_search_materials(count=20)

    def test_get_material_management_search_materials(
        self,
    ) -> None:
        self._validate_search_response(
            self._get_material_management_search_materials()
        )

    def test_get_material_management_data_materials_object_id(
        self,
    ) -> None:
        search_response: SearchResponse = (
            self._get_material_management_search_materials()
        )
        assert isinstance(search_response.content, SearchResponseContents)
        content: SearchResponseContent
        for content in search_response.content:
            assert isinstance(content.relationships, Reference)
            assert isinstance(content.relationships.reference_key, str)
            sob.model.validate(
                (self.client).get_material_management_data_materials_object_id(
                    int(content.relationships.reference_key)
                )
            )

    @lru_cache()
    def _get_material_management_data_methods_of_make(
        self,
    ) -> MethodOfMakeBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_methods_of_make()

    def test_get_material_management_data_methods_of_make(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_methods_of_make()
        )

    def test_get_material_management_data_methods_of_make_object_id(
        self,
    ) -> None:
        bulk_response: MethodOfMakeBulkResponse = (
            self._get_material_management_data_methods_of_make()
        )
        assert isinstance(
            bulk_response.content, MethodOfMakeBulkResponseContents
        )
        content: MethodOfMakeBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_methods_of_make_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_non_woven_substrate_types(
        self,
    ) -> NonWovenSubstrateTypeBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_non_woven_substrate_types()

    def test_get_material_management_data_non_woven_substrate_types(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_non_woven_substrate_types()
        )

    def test_get_material_management_data_non_woven_substrate_types_object_id(
        self,
    ) -> None:
        bulk_response: NonWovenSubstrateTypeBulkResponse = (
            self._get_material_management_data_non_woven_substrate_types()
        )
        assert isinstance(
            bulk_response.content, NonWovenSubstrateTypeBulkResponseContents
        )
        content: NonWovenSubstrateTypeBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_non_woven_substrate_types_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_non_woven_web_bonding_methods(
        self,
    ) -> NonWovenWebBondingMethodBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_non_woven_web_bonding_methods()

    def test_get_material_management_data_non_woven_web_bonding_methods(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_non_woven_web_bonding_methods()
        )

    def test_get_material_management_data_non_woven_web_bonding_methods_object_id(  # noqa
        self,
    ) -> None:
        bulk_response: NonWovenWebBondingMethodBulkResponse = (
            self._get_material_management_data_non_woven_web_bonding_methods()
        )
        assert isinstance(
            bulk_response.content, NonWovenWebBondingMethodBulkResponseContents
        )
        content: NonWovenWebBondingMethodBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_non_woven_web_bonding_methods_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_yarn_ply_number_systems(
        self,
    ) -> YarnPlyNumberSystemBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_yarn_ply_number_systems()

    def test_get_material_management_data_yarn_ply_number_systems(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_yarn_ply_number_systems()
        )

    def test_get_material_management_data_yarn_ply_number_systems_object_id(
        self,
    ) -> None:
        bulk_response: YarnPlyNumberSystemBulkResponse = (
            self._get_material_management_data_yarn_ply_number_systems()
        )
        assert isinstance(
            bulk_response.content, YarnPlyNumberSystemBulkResponseContents
        )
        content: YarnPlyNumberSystemBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_yarn_ply_number_systems_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_re_tannages(
        self,
    ) -> ReTannageBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_re_tannages()

    def test_get_material_management_data_re_tannages(
        self,
    ) -> None:
        sob.model.validate(self._get_material_management_data_re_tannages())

    def test_get_material_management_data_re_tannages_object_id(
        self,
    ) -> None:
        bulk_response: ReTannageBulkResponse = (
            self._get_material_management_data_re_tannages()
        )
        assert isinstance(bulk_response.content, ReTannageBulkResponseContents)
        content: ReTannageBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_re_tannages_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_scrims(
        self,
    ) -> ScrimBulkResponse:
        return (self.reference_client).get_material_management_data_scrims()

    def test_get_material_management_data_scrims(
        self,
    ) -> None:
        sob.model.validate(self._get_material_management_data_scrims())

    def test_get_material_management_data_scrims_object_id(
        self,
    ) -> None:
        bulk_response: ScrimBulkResponse = (
            self._get_material_management_data_scrims()
        )
        assert isinstance(bulk_response.content, ScrimBulkResponseContents)
        content: ScrimBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_scrims_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_substrate_constructions(
        self,
    ) -> SubstrateConstructionBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_substrate_constructions()

    def test_get_material_management_data_substrate_constructions(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_substrate_constructions()
        )

    def test_get_material_management_data_substrate_constructions_object_id(
        self,
    ) -> None:
        bulk_response: SubstrateConstructionBulkResponse = (
            self._get_material_management_data_substrate_constructions()
        )
        assert isinstance(
            bulk_response.content, SubstrateConstructionBulkResponseContents
        )
        content: SubstrateConstructionBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_substrate_constructions_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_supplied_material_states(
        self,
    ) -> SuppliedMaterialStateBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_supplied_material_states()

    def test_get_material_management_data_supplied_material_states(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_supplied_material_states()
        )

    def test_get_material_management_data_supplied_material_states_object_id(
        self,
    ) -> None:
        bulk_response: SuppliedMaterialStateBulkResponse = (
            self._get_material_management_data_supplied_material_states()
        )
        assert isinstance(
            bulk_response.content, SuppliedMaterialStateBulkResponseContents
        )
        content: SuppliedMaterialStateBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_supplied_material_states_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_textile_construction_types(
        self,
    ) -> TextileConstructionTypeBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_textile_construction_types()

    def test_get_material_management_data_textile_construction_types(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_textile_construction_types()
        )

    def test_get_material_management_data_textile_construction_types_object_id(
        self,
    ) -> None:
        bulk_response: TextileConstructionTypeBulkResponse = (
            self._get_material_management_data_textile_construction_types()
        )
        assert isinstance(
            bulk_response.content, TextileConstructionTypeBulkResponseContents
        )
        content: TextileConstructionTypeBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_textile_construction_types_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_textile_variations(
        self,
    ) -> TextileVariationBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_textile_variations()

    def test_get_material_management_data_textile_variations(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_textile_variations()
        )

    def test_get_material_management_data_textile_variations_object_id(
        self,
    ) -> None:
        bulk_response: TextileVariationBulkResponse = (
            self._get_material_management_data_textile_variations()
        )
        assert isinstance(
            bulk_response.content, TextileVariationBulkResponseContents
        )
        content: TextileVariationBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_textile_variations_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_thicknesses(
        self,
    ) -> ThicknessBulkResponse:
        return self.reference_client.get_material_management_data_thicknesses()

    def test_get_material_management_data_thicknesses(
        self,
    ) -> None:
        sob.model.validate(self._get_material_management_data_thicknesses())

    def test_get_material_management_data_thicknesses_object_id(
        self,
    ) -> None:
        bulk_response: ThicknessBulkResponse = (
            self._get_material_management_data_thicknesses()
        )
        assert isinstance(bulk_response.content, ThicknessBulkResponseContents)
        content: ThicknessBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_thicknesses_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_visual_material_name_variations(
        self,
    ) -> VisualMaterialNameVariationBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_visual_material_name_variations()

    def test_get_material_management_data_visual_material_name_variations(
        self,
    ) -> None:
        sob.model.validate(
            (
                self
            )._get_material_management_data_visual_material_name_variations()
        )

    def test_get_material_management_data_visual_material_name_variations_object_id(  # noqa
        self,
    ) -> None:
        bulk_response: VisualMaterialNameVariationBulkResponse = (
            self
        )._get_material_management_data_visual_material_name_variations()
        assert isinstance(
            bulk_response.content,
            VisualMaterialNameVariationBulkResponseContents,
        )
        content: VisualMaterialNameVariationBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_visual_material_name_variations_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_web_formations(
        self,
    ) -> WebFormationBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_web_formations()

    def test_get_material_management_data_web_formations(
        self,
    ) -> None:
        sob.model.validate(self._get_material_management_data_web_formations())

    def test_get_material_management_data_web_formations_object_id(
        self,
    ) -> None:
        bulk_response: WebFormationBulkResponse = (
            self
        )._get_material_management_data_web_formations()
        assert isinstance(
            bulk_response.content, WebFormationBulkResponseContents
        )
        content: WebFormationBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_web_formations_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_weight_material_name_variations(
        self,
    ) -> WeightMaterialNameVariationBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_weight_material_name_variations()

    def test_get_material_management_data_weight_material_name_variations(
        self,
    ) -> None:
        sob.model.validate(
            (
                self
            )._get_material_management_data_weight_material_name_variations()
        )

    def test_get_material_management_data_weight_material_name_variations_object_id(  # noqa
        self,
    ) -> None:
        bulk_response: WeightMaterialNameVariationBulkResponse = (
            self
        )._get_material_management_data_weight_material_name_variations()
        assert isinstance(
            bulk_response.content,
            WeightMaterialNameVariationBulkResponseContents,
        )
        content: WeightMaterialNameVariationBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_weight_material_name_variations_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_yarn_ply_brands(
        self,
    ) -> YarnPlyBrandBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_yarn_ply_brands()

    def test_get_material_management_data_yarn_ply_brands(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_yarn_ply_brands()
        )

    def test_get_material_management_data_yarn_ply_brands_object_id(
        self,
    ) -> None:
        bulk_response: YarnPlyBrandBulkResponse = (
            self
        )._get_material_management_data_yarn_ply_brands()
        assert isinstance(
            bulk_response.content, YarnPlyBrandBulkResponseContents
        )
        content: YarnPlyBrandBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_yarn_ply_brands_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_yarn_ply_spinning_methods(
        self,
    ) -> YarnPlySpinningMethodBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_yarn_ply_spinning_methods()

    def test_get_material_management_data_yarn_ply_spinning_methods(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_yarn_ply_spinning_methods()
        )

    def test_get_material_management_data_yarn_ply_spinning_methods_object_id(
        self,
    ) -> None:
        bulk_response: YarnPlySpinningMethodBulkResponse = (
            self
        )._get_material_management_data_yarn_ply_spinning_methods()
        assert isinstance(
            bulk_response.content, YarnPlySpinningMethodBulkResponseContents
        )
        content: YarnPlySpinningMethodBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_yarn_ply_spinning_methods_object_id(  # noqa
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_yarn_ply_textures(
        self,
    ) -> YarnPlyTextureBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_yarn_ply_textures()

    def test_get_material_management_data_yarn_ply_textures(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_yarn_ply_textures()
        )

    def test_get_material_management_data_yarn_ply_textures_object_id(
        self,
    ) -> None:
        bulk_response: YarnPlyTextureBulkResponse = (
            self
        )._get_material_management_data_yarn_ply_textures()
        assert isinstance(
            bulk_response.content, YarnPlyTextureBulkResponseContents
        )
        content: YarnPlyTextureBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_yarn_ply_textures_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_yarn_ply_types(
        self,
    ) -> YarnPlyTypeBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_yarn_ply_types()

    def test_get_material_management_data_yarn_ply_types(
        self,
    ) -> None:
        sob.model.validate(self._get_material_management_data_yarn_ply_types())

    def test_get_material_management_data_yarn_ply_types_object_id(
        self,
    ) -> None:
        bulk_response: YarnPlyTypeBulkResponse = (
            self
        )._get_material_management_data_yarn_ply_types()
        assert isinstance(
            bulk_response.content, YarnPlyTypeBulkResponseContents
        )
        content: YarnPlyTypeBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_yarn_ply_types_object_id(
                    int(content.object_id)
                )
            )

    @lru_cache()
    def _get_material_management_data_cushioning_types(
        self,
    ) -> CushioningTypeBulkResponse:
        return (
            self.reference_client
        ).get_material_management_data_cushioning_types()

    def test_get_material_management_data_cushioning_types(
        self,
    ) -> None:
        sob.model.validate(
            self._get_material_management_data_cushioning_types()
        )

    def test_get_material_management_data_cushioning_types_object_id(
        self,
    ) -> None:
        bulk_response: CushioningTypeBulkResponse = (
            self
        )._get_material_management_data_cushioning_types()
        assert isinstance(
            bulk_response.content, CushioningTypeBulkResponseContents
        )
        content: CushioningTypeResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            sob.model.validate(
                (
                    self.reference_client
                ).get_material_management_data_cushioning_types_object_id(
                    content.object_id
                )
            )


if __name__ == "__main__":
    unittest.main()
