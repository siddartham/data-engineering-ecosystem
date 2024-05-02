import re
from abc import ABC
from typing import (
    Any,
    Callable,
    Dict,
    Hashable,
    Mapping,
    Sequence,
    Tuple,
    Union,
)

import oapi
import sob

from ..line_management import model as line_management_model
from ..line_management import (
    reference_model as line_management_reference_model,
)
from ..material_management.model import (
    ArtworkGraphicResponse,
    Links,
    MaterialPaletteResponse,
    MaterialPricesResponse,
    MaterialsResponse,
    MaterialTypeResponse,
    PricingEffectivityResponse,
    Reference,
    SuppliedMaterialResponse,
)
from ..material_management.reference_model import (
    AirbagProcessResponse,
    AnimalSourceResponse,
    ApplicationTechniqueResponse,
    ArtworkGraphicTypeResponse,
    ArtworkTechniqueResponse,
    BrandNameResponse,
    ChemicalPolymerTypeResponse,
    CoatingTypeResponse,
    ComponentConstructionTypeResponse,
    ComponentTypeResponse,
    ContentSourceResponse,
    ContentTypeResponse,
    CoreConstructionTypeResponse,
    CountryOfOriginResponse,
    CureProcessResponse,
    CushioningTypeResponse,
    CustomsDescriptionResponse,
    DevelopmentReasonResponse,
    DimensionWidthIndicatorResponse,
    DyeMethodResponse,
    DyeTypeResponse,
    EdgeEndFinishResponse,
    EmbossTypeResponse,
    FancyYarnResponse,
    FiberCrossSectionResponse,
    FiberPreparationResponse,
    FiberTypeResponse,
    FinishProcessResponse,
    GrainLeatherSubTypeResponse,
    HardOrSoftComponentResponse,
    InsulationPaddingTypeResponse,
    LeatherTypeResponse,
    LiquidBaseTypeResponse,
    MachineryTypeResponse,
    MaterialDevelopmentTeamResponse,
    MaterialEndUseResponse,
    MaterialPaletteStateResponse,
    MaterialPricingModeResponse,
    MaterialTechnologyResponse,
    MethodOfMakeResponse,
    NonWovenSubstrateTypeResponse,
    NonWovenWebBondingMethodResponse,
    PaletteTypeResponse,
    ProcessTypeResponse,
    PuChemistryResponse,
    ReTannageResponse,
    ScrimResponse,
    SteamMethodResponse,
    SubPaletteContentResponse,
    SubstrateConstructionResponse,
    SubstrateProcessingTypeResponse,
    TeethSizeResponse,
    TextileConstructionTypeResponse,
    TextileSubVariationResponse,
    TextileSubVariationTwoResponse,
    TextileVariationResponse,
    VisualEffectResponse,
    WebFormationResponse,
    YarnPlyBrandResponse,
    YarnPlyDyeMethodResponse,
    YarnPlyLusterResponse,
    YarnPlyNumberSystemResponse,
    YarnPlySpinningMethodResponse,
    YarnPlyTextureResponse,
    YarnPlyTwistResponse,
    YarnPlyTypeResponse,
    YarnVisualEffectResponse,
    ZipperPerformanceResponse,
)
from ..material_vendor_management import (
    model as material_vendor_management_model,
)
from ..material_vendor_management.model import (
    SupplierLocationResponse,
    SupplierResponse,
)
from ..product_development import model as product_development_model
from ..product_development.model import (
    BillOfMaterialsResponse,
    BillOfMaterialsSourceResponse,
)
from ..product_development.reference_model import (
    BillOfMaterialsSectionResponse,
    BillOfMaterialsUnitOfMeasurementResponse,
    DevelopmentTeamGroupResponse,
    PartNameResponse,
)
from ..utilities import lru_cache

_RELATIONSHIPS_CLASSES: Dict[
    str, Callable[[sob.abc.Readable], sob.abc.Model]
] = {
    "MATERIALPALETTE": MaterialPaletteResponse,
    "MATERIALPRICING": MaterialPricesResponse,
    "MATERIALPRICES": MaterialPricesResponse,
    "ISOCOUNTRY": line_management_reference_model.ISOCountryResponse,
    "CYCLEYEAR": line_management_reference_model.CycleYearResponse,
    "PALETTETYPE": PaletteTypeResponse,
    "DIVISION": line_management_reference_model.DivisionResponse,
    "DEVELOPMENTTEAMGROUP": DevelopmentTeamGroupResponse,
    "CURRENCY": line_management_reference_model.CurrencyResponse,
    "SUBPALETTECONTENT": SubPaletteContentResponse,
    "SUPPLIEDMATERIAL": SuppliedMaterialResponse,
    "CUSTOMSDESCRIPTION": CustomsDescriptionResponse,
    "MATERIALTYPE": MaterialTypeResponse,
    "MATERIALPALETTESTATE": MaterialPaletteStateResponse,
    "MATERIALPRICINGMODE": MaterialPricingModeResponse,
    "MATERIAL": MaterialsResponse,
    "MATERIALSUPPLIERLOCATION": SupplierLocationResponse,
    "PRICINGEFFECTIVITY": PricingEffectivityResponse,
    "DEVELOPMENTTEAM": line_management_reference_model.DevelopmentTeamResponse,
    "AIRBAGPROCESS": AirbagProcessResponse,
    "COUNTRYOFORIGIN": CountryOfOriginResponse,
    "ANIMALSOURCE": AnimalSourceResponse,
    "APPLICATIONTECHNIQUE": ApplicationTechniqueResponse,
    "ARTWORKGRAPHICTYPE": ArtworkGraphicTypeResponse,
    "ARTWORKGRAPHIC": ArtworkGraphicResponse,
    "ARTWORKTECHNIQUE": ArtworkTechniqueResponse,
    "BRANDNAME": BrandNameResponse,
    "CHEMICALPOLYMERTYPE": ChemicalPolymerTypeResponse,
    "COATINGTYPE": CoatingTypeResponse,
    "COMPONENTCONSTRUCTIONTYPE": ComponentConstructionTypeResponse,
    "COMPONENTTYPE": ComponentTypeResponse,
    "CONTENTSOURCE": ContentSourceResponse,
    "CORECONSTRUCTIONTYPE": CoreConstructionTypeResponse,
    "CUREPROCESS": CureProcessResponse,
    "CUSHIONINGTYPE": CushioningTypeResponse,
    "DEVELOPMENTREASON": DevelopmentReasonResponse,
    "DIMENSIONWIDTHINDICATOR": DimensionWidthIndicatorResponse,
    "DYEMETHOD": DyeMethodResponse,
    "DYETYPE": DyeTypeResponse,
    "EDGEENDFINISH": EdgeEndFinishResponse,
    "EMBOSSTYPE": EmbossTypeResponse,
    "FANCYYARN": FancyYarnResponse,
    "FIBERCROSSSECTION": FiberCrossSectionResponse,
    "FIBERPREPARATION": FiberPreparationResponse,
    "FIBERTYPE": FiberTypeResponse,
    "FINISHPROCESS": FinishProcessResponse,
    "GRAINLEATHERSUBTYPE": GrainLeatherSubTypeResponse,
    "HARDORSOFTCOMPONENT": HardOrSoftComponentResponse,
    "INSULATIONPADDINGTYPE": InsulationPaddingTypeResponse,
    "LEATHERTYPE": LeatherTypeResponse,
    "LIQUIDBASETYPE": LiquidBaseTypeResponse,
    "MACHINERYTYPE": MachineryTypeResponse,
    "MATERIALDEVELOPMENTTEAM": MaterialDevelopmentTeamResponse,
    "MATERIALENDUSE": MaterialEndUseResponse,
    "MATERIALTECHNOLOGY": MaterialTechnologyResponse,
    "MATERIALTECHNOLOGIES": MaterialTechnologyResponse,
    "METHODOFMAKE": MethodOfMakeResponse,
    "NONWOVENSUBSTRATETYPE": NonWovenSubstrateTypeResponse,
    "NONWOVENWEBBONDINGMETHOD": NonWovenWebBondingMethodResponse,
    "PROCESSTYPE": ProcessTypeResponse,
    "PUCHEMISTRY": PuChemistryResponse,
    "RETANNAGE": ReTannageResponse,
    "SCRIM": ScrimResponse,
    "STEAMMETHOD": SteamMethodResponse,
    "SUBSTRATECONSTRUCTION": SubstrateConstructionResponse,
    "SUBSTRATEPROCESSINGTYPE": SubstrateProcessingTypeResponse,
    "SUPPLIER": SupplierResponse,
    "MATERIALSUPPLIER": SupplierResponse,
    "TEETHSIZE": TeethSizeResponse,
    "TEXTILECONSTRUCTIONTYPE": TextileConstructionTypeResponse,
    "TEXTILESUBVARIATION": TextileSubVariationResponse,
    "TEXTILESUBVARIATIONTWO": TextileSubVariationTwoResponse,
    "TEXTILEVARIATION": TextileVariationResponse,
    "VISUALEFFECT": VisualEffectResponse,
    "WEBFORMATION": WebFormationResponse,
    "YARNPLYBRAND": YarnPlyBrandResponse,
    "YARNPLYDYEMETHOD": YarnPlyDyeMethodResponse,
    "YARNPLYLUSTER": YarnPlyLusterResponse,
    "YARNPLYNUMBERSYSTEM": YarnPlyNumberSystemResponse,
    "YARNPLYSPINNINGMETHOD": YarnPlySpinningMethodResponse,
    "YARNPLYTEXTURE": YarnPlyTextureResponse,
    "YARNPLYTWIST": YarnPlyTwistResponse,
    "YARNPLYTYPE": YarnPlyTypeResponse,
    "YARNVISUALEFFECT": YarnVisualEffectResponse,
    "ZIPPERPERFORMANCE": ZipperPerformanceResponse,
    "CONTENTTYPE": ContentTypeResponse,
    "BOM": BillOfMaterialsResponse,
    "SOURCEBOM": BillOfMaterialsSourceResponse,
    "BILLOFMATERIALSSECTION": BillOfMaterialsSectionResponse,
    "BILLOFMATERIALSUNITOFMEASUREMENT": (
        BillOfMaterialsUnitOfMeasurementResponse
    ),
    "PARTNAME": PartNameResponse,
    "PRODUCTOFFERING": line_management_model.GlobalOfferingResponse,
    "GLOBALCATEGORYCOREFOCUS": (
        line_management_reference_model.GlobalCategoryCoreFocusResponse
    ),
}


class Client(oapi.client.Client, ABC):
    def get_reference(
        self,
        reference: Union[
            Reference,
            line_management_model.Reference,
            line_management_reference_model.Reference,
            material_vendor_management_model.Reference,
            product_development_model.Reference,
        ],
        query: Union[
            Mapping[
                str,
                sob.abc.MarshallableTypes,
            ],
            Sequence[
                Tuple[
                    str,
                    sob.abc.MarshallableTypes,
                ]
            ],
        ] = (),
    ) -> Any:
        """
        This method identifies the data type for a referenced link, retrieves
        the link, and deserializes the content of the link as an instance of
        the appropriate class.

        Parameters:

        - link (nike.product_data_hub_clinet.material_management.model.Links)
        - query (dict) = (): A dictionary (or list/tuple) of query string
          arguments.
        """
        assert isinstance(
            reference.link,
            (
                Links,
                line_management_reference_model.Links,
                material_vendor_management_model.Links,
                product_development_model.Links,
                line_management_model.Links,
            ),
        )
        link: Union[
            Links,
            line_management_model.Links,
            line_management_reference_model.Links,
            material_vendor_management_model.Links,
            product_development_model.Links,
        ] = reference.link
        return self.get_link(link, query=query)

    def get_link(
        self,
        link: Union[
            Links,
            line_management_model.Links,
            line_management_reference_model.Links,
            material_vendor_management_model.Links,
            product_development_model.Links,
        ],
        query: Union[
            Mapping[
                str,
                sob.abc.MarshallableTypes,
            ],
            Sequence[
                Tuple[
                    str,
                    sob.abc.MarshallableTypes,
                ]
            ],
        ] = (),
    ) -> Any:
        """
        This method identifies the data type for a link, retrieves the link,
        and deserializes the content of the link as an instance of the
        appropriate class.

        Parameters:

        - link (nike.product_data_hub_clinet.material_management.model.Links)
        - query (dict) = (): A dictionary (or list/tuple) of query string
          arguments.
        """
        if not isinstance(query, Hashable):
            if isinstance(query, Mapping):
                query = map(tuple, query.items())
            query = tuple(query)
        return self._get_link(link, query=query)

    @lru_cache(maxsize=128, typed=False)
    def _get_link(
        self,
        link: Union[
            Links,
            line_management_reference_model.Links,
            material_vendor_management_model.Links,
            product_development_model.Links,
        ],
        query: Tuple[
            Tuple[
                str,
                Union[
                    None,
                    int,
                    float,
                    str,
                    bool,
                    Sequence[int],
                    Sequence[str],
                    Sequence[bool],
                ],
            ],
            ...,
        ] = (),
    ) -> sob.abc.Model:
        assert isinstance(link.rel, str)
        assert isinstance(link.href, str)
        response: sob.abc.Readable = self.request(
            link.href, method="GET", query=query
        )
        response_class: Callable[[sob.abc.Readable], sob.abc.Model]
        try:
            response_class = _RELATIONSHIPS_CLASSES[
                re.sub(r"[^A-Z0-9]", "", link.rel.upper())
            ]
            assert link.href, f"Missing @href: {repr(link)}"
        except (KeyError, AssertionError):
            # trigger a read, in order to print the response content
            response.read()
            raise
        return response_class(response)
