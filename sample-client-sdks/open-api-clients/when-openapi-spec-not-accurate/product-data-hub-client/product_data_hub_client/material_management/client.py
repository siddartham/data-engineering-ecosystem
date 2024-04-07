import oapi
import sob
import typing
from . import model
from ..abc.client import Client as _Client
from ..config import TOKEN_URL_PROD
from logging import Logger
from cerberus_assistant.config import CERBERUS_URL
from cerberus_assistant.decorate import apply_cerberus_path_arguments


class Client(_Client):
    """
    Initialization Parameters:

    - url (str): The base URL for API requests.
    - api_key (str): An API key with which to authenticate requests.
    - api_key_name (str): The name of the header, query parameter, or
      cookie parameter in which to convey the API key.
    - oauth2_client_id (str): An OAuth2 client ID.
    - oauth2_client_secret (str): An OAuth2 client secret.
    - oauth2_token_url (str): The token URL to use for OAuth2
      authentication.
      Can be relative to `url`.
    - timeout (int): The number of seconds before a request will timeout
      and throw an error. If this is 0 (the default), the system default
      timeout will be used.
    - retry_number_of_attempts (int): The number of times to retry
      a request which results in an error.
    - retry_for_errors: A tuple of one or more exception types
      on which to retry a request. To retry for *all* errors,
      pass `(Exception,)` for this argument.
    - retry_hook: A function, accepting one argument (an Exception),
      and returning a boolean value indicating whether to retry the
      request (if retries have not been exhausted). This hook applies
      *only* for exceptions which are a sub-class of an exception
      included in `retry_for_errors`.
    - logger (logging.Logger|None):
      A `logging.Logger` to which requests should be logged.
    - echo (bool): If `True`, requests/responses are printed as
      they occur.
    - cerberus_url (str): The root URL for the Cerberus API where
      your secrets are stored.
    - api_key_cerberus_path (str) = "": A Cerberus secure data path (including
      /key) wherein an API key with which to authenticate can be found.
    - oauth2_client_id_cerberus_path (str) = "": A Cerberus secure data path (
      including /key) wherein an OAuth2 client ID with which to authenticate
      can be found.
    - oauth2_client_secret_cerberus_path (str) = "": A Cerberus secure data
      path (including /key) wherein an OAuth2 client secret with which to
      authenticate can be found.
    """

    __slots__: typing.Tuple[str, ...] = oapi.client.CLIENT_SLOTS

    @apply_cerberus_path_arguments(
        api_key="api_key_cerberus_path",
        cerberus_url_parameter_name="cerberus_url",
        oauth2_client_id="oauth2_client_id_cerberus_path",
        oauth2_client_secret="oauth2_client_secret_cerberus_path",
    )
    def __init__(
        self,
        url: str = (
            "https://materialmanagement.api-product.pes-prod.nike.com/v3"
        ),
        api_key: str = "",
        api_key_name: str = "X-API-KEY",
        oauth2_client_id: str = "",
        oauth2_client_secret: str = "",
        oauth2_token_url: str = TOKEN_URL_PROD,
        timeout: int = 0,
        retry_number_of_attempts: int = 3,
        retry_for_errors: typing.Tuple[
            typing.Type[Exception], ...
        ] = oapi.client.DEFAULT_RETRY_FOR_ERRORS,
        retry_hook: typing.Callable[
            [Exception], bool
        ] = oapi.client.default_retry_hook,
        logger: typing.Optional[Logger] = None,
        echo: bool = False,
        cerberus_url: str = CERBERUS_URL,
        api_key_cerberus_path: str = "",
        oauth2_client_id_cerberus_path: str = "",
        oauth2_client_secret_cerberus_path: str = "",
    ) -> None:
        super().__init__(
            url=url,
            api_key=api_key,
            api_key_name=api_key_name,
            oauth2_client_id=oauth2_client_id,
            oauth2_client_secret=oauth2_client_secret,
            oauth2_token_url=oauth2_token_url,
            timeout=timeout,
            retry_number_of_attempts=retry_number_of_attempts,
            retry_for_errors=retry_for_errors,
            retry_hook=retry_hook,
            logger=logger,
            echo=echo,
        )

    def get_material_management_data_materials_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.MaterialManagementDataMaterialsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.MaterialsResponse:
        """
        How you get a single materials.

        Parameters:

        - object_id:
          A single Id of the object (in this case Materials)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materials/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.MaterialsResponse,
            )
        )

    def get_material_management_data_materials_object_id_relationships(
        self,
        object_id: int,
        *,
        depth: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.RelationshipResponse:
        """
        How you get all the relationships to the single object requested, in
        other words the children in the hierarchy to the requested entity

        Parameters:

        - object_id:
          The Id of the object (in this case Materials) where the relationships
          are desired
        - depth:
          This determines how many levels in the hierarcy you wish to traverse,
          default is 2
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materials/{objectId}/relationships".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "depth": oapi.client.format_argument_value(
                    "depth",
                    depth,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.RelationshipResponse,
            )
        )

    def get_material_management_search_materials(
        self,
        **kwargs: typing.Any,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the material entity

        Parameters:

        - count:
          Number of entries the API should attempt to fetch, default is 10
        - offset:
          Offset of the entries the API should attempt to fetch, default is 0
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        - q:
          This parameter is how you pass free text search, if any string is
          passed here it will be searched as free text
        - parent_material_item_identifier:
          The reference key associated with this item:
          parentMaterialItemIdentifier
        - material_type:
          The reference key associated with this item: Material Type
        - customs_description:
          The value associated with this item: customsDescription
        - development_team:
          The value associated with this item: developmentTeam
        - material_name_variation_weight:
          The reference key associated with this item:
          materialNameVariationWeight
        - material_name_variation_visual:
          The reference key associated with this item:
          materialNameVariationVisual
        - target_price:
          The number (float) for targetPrice
        - target_price_uom:
          The reference key associated with this item: targetPriceUOM
        - material_color_control_mode:
          The reference key associated with this item: materialColorControlMode
        - material_pricing_mode:
          The reference key associated with this item: materialPricingMode
        - legacy_created_on_date:
          The reference key associated with this item: legacyCreatedOnDate
        - legacy_material_number:
          The reference key associated with this item: legacyMaterialNumber
        - apparel_pdm_material_number:
          The value associated with this item: apparelPDMMaterialNumber
        - division:
          The reference key associated with this item: #N/A
        - material_development_team:
          The reference key associated with this item: materialDevelopmentTeam
        - target_style:
          The value associated with this item: targetStyle
        - material_initial_category:
          The reference key associated with this item: materialInitialCategory
        - material_initial_cycle_year:
          The reference key associated with this item: materialInitialCycleYear
        - material_target_cycle_year:
          The reference key associated with this item: materialTargetCycleYear
        - material_item_status_indicator:
          The true or false flag associated with this item:
          materialItemStatusIndicator
        - material_bom_indicator:
          The true or false flag associated with this item:
          materialBOMIndicator
        - create_timestamp:
          The reference key associated with this item: Material Change
          Timestamp
        - change_timestamp:
          The reference key associated with this item: Material Change
          Timestamp
        - material_content_percentage:
          The number (float) for materialContentPercentage
        - material_content_type:
          The reference key associated with this item: materialContentType
        - material_content_source:
          The reference key associated with this item: materialContentSource
        - material_label_content_percentage:
          The number (float) for materialLabelContentPercentage
        - material_label_content_type:
          The reference key associated with this item: materialLabelContentType
        - material_label_content_source:
          The reference key associated with this item:
          materialLabelContentSource
        - material_family:
          The reference key associated with this item: materialFamily
        - material_owner:
          The reference key associated with this item: materialOwner
        - artwork_graphic:
          The reference key associated with this item: artworkGraphic
        - artwork_technique:
          The reference key associated with this item: artworkTechnique
        - secondary_process_indicator:
          The true or false flag associated with this item:
          secondaryProcessIndicator
        - artwork_application_location:
          The reference key associated with this item:
          artworkApplicationLocation
        - artwork_repeat_length_cm:
          The number (float) for artworkRepeatLengthCm
        - directional_pattern_indicator:
          The true or false flag associated with this item:
          directionalPatternIndicator
        - garment_location_placement:
          The value associated with this item: garmentLocationPlacement
        - end_use:
          The reference key associated with this item: endUse
        - development_reason:
          The reference key associated with this item: developmentReason
        - material_benefits:
          The reference key associated with this item: materialBenefits
        - fabric_face_designation:
          The reference key associated with this item: fabricFaceDesignation
        - stretch_direction:
          The reference key associated with this item: stretchDirection
        - thickness_mm:
          The number (float) for thicknessMm
        - thickness_selection:
          The reference key associated with this item: thicknessSelection
        - maximum_thickness_mm:
          The number (float) for maximumThicknessMm
        - minimum_thickness_mm:
          The number (float) for maximumThicknessMm
        - length_mm:
          The number (float) for lengthMm
        - length_cm:
          The number (float) for lengthCm
        - dimension_width_indicator:
          The reference key associated with this item: dimensionWidthIndicator
        - width_mm:
          The number (float) for widthMm
        - width_cm:
          The number (float) for widthCm
        - height_mm:
          The number (float) for heightMm
        - height_cm:
          The number (float) for heightCm
        - weight_grams_per_square_meter:
          The number (float) for weightGramsPerSquareMeter
        - external_diameter_mm:
          The number (float) for externalDiameterMm
        - external_length_mm:
          The number (float) for externalLengthMm
        - external_width_mm:
          The number (float) for externalWidthMm
        - internal_diameter_mm:
          The number (float) for internalDiameterMm
        - internal_length_mm:
          The number (float) for internalLengthMm
        - internal_width_mm:
          The number (float) for internalWidthMm
        - gauge_inch:
          The number (float) for gaugeInch
        - grams_per_thousand_pieces:
          The number (float) for gramsPerThousandPieces
        - weight_grams_per_thousand_pieces:
          Weight (grams per 1000 pieces)
        - weight_grams_per_linear_yard:
          Weight (grams per linear yard)
        - weight_grams_per_linear_meter:
          Weight (grams per linear meter)
        - yarn_composition_content_percentage:
          The number (float) for yarnCompositionContentPercentage
        - yarn_composition_content_type:
          The reference key associated with this item:
          yarnCompositionContentType
        - yarn_composition_content_source:
          The reference key associated with this item:
          yarnCompositionContentSource
        - yarn_composition_location:
          The reference key associated with this item: yarnCompositionLocation
        - yarn_composition_type:
          The reference key associated with this item: yarnCompositionType
        - yarn_composition_size:
          The number (float) for yarnCompositionSize
        - yarn_composition_spinning_method:
          The reference key associated with this item:
          yarnCompositionSpinningMethod
        - yarn_composition_count:
          The The number (integer) for yarnCompositionCount
        - yarn_composition_preparation:
          The reference key associated with this item:
          yarnCompositionPreparation
        - yarn_composition_cross_section:
          The reference key associated with this item:
          yarnCompositionCrossSection
        - yarn_composition_filament_count:
          The number (integer) for yarnCompositionFilamentCount
        - yarn_composition_number_system:
          The reference key associated with this item:
          yarnCompositionNumberSystem
        - yarn_composition_luster:
          The reference key associated with this item: yarnCompositionLuster
        - yarn_composition_brand:
          The reference key associated with this item: yarnCompositionBrand
        - yarn_composition_texture:
          The reference key associated with this item: yarnCompositionTexture
        - yarn_composition_twist:
          The reference key associated with this item: yarnCompositionTwist
        - yarn_composition_finish_process:
          The reference key associated with this item:
          yarnCompositionFinishProcess
        - yarn_composition_dye_method:
          The reference key associated with this item: yarnCompositionDyeMethod
        - yarn_composition_visual_effect:
          The reference key associated with this item:
          yarnCompositionVisualEffect
        - yarn_composition_fixed_color:
          The reference key associated with this item:
          yarnCompositionFixedColor
        - yarn_composition_usage_percentage:
          The number (float) for yarnCompositionUsagePercentage
        - ply_content_percentage:
          The number (float) for plyContentPercentage
        - ply_content_type:
          The reference key associated with this item: plyContentType
        - ply_content_source:
          The reference key associated with this item: plyContentSource
        - ply_location:
          The reference key associated with this item: plyLocation
        - ply_type:
          The reference key associated with this item: plyType
        - ply_brand:
          The reference key associated with this item: plyBrand
        - ply_size:
          The number (float) for plySize
        - ply_number_system:
          The reference key associated with this item: plyNumberSystem
        - ply_cross_section:
          The reference key associated with this item: plyCrossSection
        - ply_spinning_method:
          The reference key associated with this item: plySpinningMethod
        - ply_filament_count:
          The number (integer) for plyFilamentCount
        - ply_twist:
          The reference key associated with this item: plyTwist
        - ply_luster:
          The reference key associated with this item: plyLuster
        - ply_texture:
          The reference key associated with this item: plyTexture
        - ply_finish_process:
          The reference key associated with this item: plyFinishProcess
        - ply_dye_method:
          The reference key associated with this item: plyDyeMethod
        - ply_visual_effect:
          The reference key associated with this item: plyVisualEffect
        - ply_fixed_color:
          The reference key associated with this item: plyFixedColor
        - ply_usage_percentage:
          The number (float) for plyUsagePercentage
        - fiber_content_percentage:
          The number (float) for fiberContentPercentage
        - fiber_content_type:
          The reference key associated with this item: fiberContentType
        - fiber_content_source:
          The reference key associated with this item: fiberContentSource
        - fiber_size:
          The number (float) for fiberSize
        - fiber_ply_location:
          The reference key associated with this item: fiberPlyLocation
        - fiber_staple_number_system:
          The reference key associated with this item: fiberStapleNumberSystem
        - fiber_staple_length:
          The number (float) for fiberStapleLength
        - fiber_staple_length_min:
          The number (float) for fiberStapleLengthMin
        - fiber_staple_length_max:
          The number (float) for fiberStapleLengthMax
        - fiber_diameter:
          The number (float) for fiberDiameter
        - fiber_diameter_min:
          The number (float) for fiberDiameterMin
        - fiber_diameter_max:
          The number (float) for fiberDiameterMax
        - fiber_diameter_unit:
          The reference key associated with this item: fiberDiameterUnit
        - fiber_preparation:
          The reference key associated with this item: fiberPreparation
        - fiber_cross_section:
          The reference key associated with this item: fiberCrossSection
        - fiber_luster:
          The reference key associated with this item: fiberLuster
        - fiber_finish_process:
          The reference key associated with this item: fiberFinishProcess
        - fiber_dye_method:
          The reference key associated with this item: fiberDyeMethod
        - fiber_usage_percentage:
          The number (float) for fiberUsagePercentage
        - edge_finish:
          The reference key associated with this item: edgeFinish
        - visual_effect:
          The reference key associated with this item: visualEffect
        - visual_effect_location:
          The reference key associated with this item: visualEffectLocation
        - application_technique:
          The reference key associated with this item: applicationTechnique
        - finish_process:
          The reference key associated with this item: finishProcess
        - finish_location:
          The reference key associated with this item: finishLocation
        - number_of_passes:
          The number (integer) for numberOfPasses
        - material_technologies:
          The reference key associated with this item: materialTechnology
        - release_paper_code:
          The code associated with this item: releasePaperCode
        - release_paper_one:
          The material Id for releasePaperOne
        - release_paper_two:
          The material Id for releasePaperTwo
        - release_paper_side_one:
          The reference key associated with this item: releasePaperSideOne
        - release_paper_side_two:
          The reference key associated with this item: releasePaperSideTwo
        - release_paper_finish_process:
          The reference key associated with this item:
          releasePaperFinishProcess
        - top_layer_material_item:
          The material Id for topLayerMaterialItem
        - middle_layer_1_material_item:
          The material Id for middleLayer1MaterialItem
        - middle_layer_2_material_item:
          The material Id for middleLayer2MaterialItem
        - middle_layer_3_material_item:
          The material Id for middleLayer3MaterialItem
        - bottom_layer_material_item:
          The material Id for bottomLayerMaterialItem
        - non_woven_substrate_type:
          The reference key associated with this item: nonWovenSubstrateType
        - non_woven_web_bonding_method:
          The reference key associated with this item: nonWovenWebBondingMethod
        - color_dominance:
          The reference key associated with this item: colorDominance
        - color_effect:
          The reference key associated with this item: colorEffect
        - color_position:
          The reference key associated with this item: colorPosition
        - color_location:
          The reference key associated with this item: colorLocation
        - color_callout:
          The reference key associated with this item: colorCallout
        - color_fiber:
          The reference key associated with this item: colorFiber
        - dye_method:
          The reference key associated with this item: dyeMethod
        - dye_type:
          The reference key associated with this item: dyeType
        - active_category:
          The reference key associated with this item: activeCategory
        - active_cycle_year:
          The reference key associated with this item: activeCycleYear
        - web_formation:
          The reference key associated with this item: webFormation
        - number_of_colors:
          The reference key associated with this item: numberOfColors
        - last_identifier:
          The last identifier
        - animal_source:
          The reference key associated with this item: animalSource
        - dyed_through_crust_indicator:
          The true or false flag associated with this item:
          dyedThroughCrustIndicator
        - oil_content:
          The reference key associated with this item: oilContent
        - re_tannage:
          The reference key associated with this item: reTannage
        - washable_indicator:
          The true or false flag associated with this item: washableIndicator
        - composition_leather_type:
          The reference key associated with this item: compositionLeatherType
        - grain_leather_type:
          The reference key associated with this item: grainLeatherType
        - grain_leather_sub_type:
          The reference key associated with this item: grainLeatherSubType
        - split_leather_type:
          The reference key associated with this item: splitLeatherType
        - average_pu_thickness:
          The number (float) for averagePUThickness
        - coating_thickness_mm:
          The number (float) for coatingThicknessMm
        - moldable:
          The reference key associated with this item: moldable
        - substrate_processing_type:
          The reference key associated with this item: substrateProcessingType
        - substrate_pu_dipped_indicator:
          The true or false flag associated with this item:
          substratePUDippedIndicator
        - substrate_construction:
          The reference key associated with this item: substrateConstruction
        - textile_construction_type:
          The reference key associated with this item: textileConstructionType
        - textile_sub_variation:
          The reference key associated with this item: textileSubVariation
        - textile_sub_variation_two:
          The reference key associated with this item: textileSubVariationTwo
        - textile_variation:
          The reference key associated with this item: textileVariation
        - ends_per_inch_number:
          The number of endsPerInchNumber
        - picks_per_inch_number:
          The number of picksPerInchNumber
        - machinery_type:
          The reference key associated with this item: machineryType
        - warp_count:
          The number of warpCount
        - weft_count:
          The number of weftCount
        - twill_construction_type:
          The reference key associated with this item: twillConstructionType
        - twill_direction:
          The reference key associated with this item: twillDirection
        - fold_indicator:
          The true or false flag associated with this item: foldIndicator
        - rib_construction:
          The reference key associated with this item: ribConstruction
        - height_indicator:
          The reference key associated with this item: heightIndicator
        - rows_of_spandex:
          The number of rowsOfSpandex
        - part_type_orientation:
          The reference key associated with this item: partTypeOrientation
        - initial_development_product_alias:
          The string value associated with this item:
          initialDevelopmentProductAlias
        - pre_twist_yarn:
          The reference key associated with this item: preTwistYarn
        - program:
          The reference key associated with this item: programIdentifier
        - steam_method:
          The reference key associated with this item: steamMethod
        - structure_testing_reference:
          The reference key associated with this item:
          structureTestingReference
        - structure_reference_number:
          The reference key associated with this item: structureReferenceNumber
        - structure_coverage:
          The reference key associated with this item: structureCoverage
        - blanket_number:
          The reference key associated with this item: blanketNumber
        - yarn_size:
          The number (float) of yarnSize
        - yarn_spinning_method:
          The reference key associated with this item: yarnSpinningMethod
        - all_plys_the_same_indicator:
          The true or false flag associated with this item:
          allPlysTheSameIndicator
        - fancy_yarn:
          The reference key associated with this item: fancyYarn
        - fixed_color:
          The reference key associated with this item: fixedColor
        - yarn_brand:
          The reference key associated with this item: yarnBrand
        - yarn_number_system:
          The reference key associated with this item: yarnNumberSystem
        - yarn_twist:
          The reference key associated with this item: yarnTwist
        - yarn_ply_count:
          The number of yarnPlyCount
        - yarn_type:
          The reference key associated with this item: yarnType
        - yarn_luster:
          The reference key associated with this item: yarnLuster
        - yarn_finish_process:
          The reference key associated with this item: yarnFinishProcess
        - yarn_dye_method:
          The reference key associated with this item: yarnDyeMethod
        - yarn_visual_effect:
          The reference key associated with this item: yarnVisualEffect
        - yarn_number_of_ends:
          The number of yarnNumberOfEnds
        - yarn_filament_count:
          The number of yarnFilamentCount
        - yarn_covering_method:
          The reference key associated with this item: yarnCoveringMethod
        - yarn_texture:
          The reference key associated with this item: yarnTexture
        - microfiber_indicator:
          The true or false flag associated with this item: microfiberIndicator
        - yarn_preparation:
          The reference key associated with this item: yarnPreparation
        - yarn_cross_section:
          The reference key associated with this item: yarnCrossSection
        - yarn_location:
          The reference key associated with this item: yarnLocation
        - yarn_supplied_material:
          The reference key associated with this item: yarnSuppliedMaterial
        - heat_setting:
          The integer for heatSetting
        - intermingling:
          The integer for intermingling
        - chemical_product:
          The string for chemicalProduct
        - chemical_supplier:
          The string for chemicalProduct
        - compliance_accreditation:
          The reference key associated with this item: complianceAccreditation
        - yarn_supplied_material_number_of_ends:
          The integer for yarnSuppliedMaterialNumberOfEnds
        - yarn_usage_percentage:
          The number (float) for yarnUsagePercentage
        - base_type:
          The reference key associated with this item: baseType
        - single_component_indicator:
          The reference key associated with this item: singleComponentIndicator
        - flammability_rating:
          The reference key associated with this item: flammabilityRating
        - hotmelt_type:
          The reference key associated with this item: hotmeltType
        - hydrolysis_resistant_indicator:
          The true or false flag associated with this item:
          hydrolysisResistantIndicator
        - method_of_make:
          The reference key associated with this item: methodOfMake
        - chem_poly_form:
          The reference key associated with this item: chemPolyForm
        - film_type:
          The reference key associated with this item: filmType
        - hotmelt_material_item:
          The reference key associated with this item: Hotmelt Material
          Identifier
        - hotmelt_thickness_number_mm:
          The number (float) for hotmeltThicknessNumberMm
        - opacity:
          The reference key associated with this item: opacity
        - stretch_indicator:
          The true or false flag associated with this item: stretchIndicator
        - foam_type:
          The reference key associated with this item: foamType
        - polyurethane_chemistry:
          The reference key associated with this item: polyurethaneChemistry
        - hardness_asker_c:
          The reference key associated with this item: hardnessAskerC
        - firmness:
          The reference key associated with this item: firmness
        - melting_point_number:
          The number (float) for meltingPointNumber
        - plastic_type:
          The reference key associated with this item: plasticType
        - plastic_sub_type:
          The reference key associated with this item: plasticSubType
        - ultraviolet_inhibitor_indicator:
          The true or false flag associated with this item:
          ultravioletInhibitorIndicator
        - clear_rubber_indicator:
          The true or false flag associated with this item:
          clearRubberIndicator
        - cure_process:
          The reference key associated with this item: cureProcess
        - regrind_content_percentage:
          The number (float) for regrindContentPercentage
        - sport_activity:
          The reference key associated with this item: sportActivity
        - detachable_metal_indicator:
          The true or false flag associated with this item:
          detachableMetalIndicator
        - hard_or_soft_component:
          The reference key associated with this item: hardOrSoftComponent
        - stock_or_custom:
          The reference key associated with this item: stockOrCustom
        - core_construction_type:
          The reference key associated with this item: coreConstructionType
        - component_construction_type:
          The reference key associated with this item:
          componentConstructionType
        - has_core_indicator:
          The true or false flag associated with this item: hasCoreIndicator
        - shape:
          The reference key associated with this item: shape
        - logo_type:
          The reference key associated with this item: logoType
        - logo_name:
          The reference key associated with this item: logoName
        - logo_placement:
          The reference key associated with this item: logoPlacement
        - hotmelt_included_indicator:
          The true or false flag associated with this item:
          hotmeltIncludedIndicator
        - elasticized_indicator:
          The true or false flag associated with this item:
          elasticizedIndicator
        - vendor_color_card_only_indicator:
          The true or false flag associated with this item:
          vendorColorCardOnlyIndicator
        - component_form:
          The reference key associated with this item: componentForm
        - ligne_size_number:
          The number (float) for ligneSizeNumber
        - number_of_holes:
          The number for numberOfHoles
        - adhesive_type:
          The reference key associated with this item: adhesiveType
        - gripper_type:
          The reference key associated with this item: gripperType
        - number_of_gripper_rows:
          The number for numberOfGripperRows
        - end_finish:
          The reference key associated with this item: endFinish
        - for_product_sizes:
          The reference key associated with this item: forProductSizes
        - part_type:
          The reference key associated with this item: partType
        - number_of_rows:
          The number (integer) for numberOfRows
        - amount_per_row:
          The number (integer) for amountPerRow
        - adjuster_type:
          The reference key associated with this item: adjusterType
        - contains_magnet_indicator:
          The true or false flag associated with this item:
          containsMagnetIndicator
        - button_type:
          The reference key associated with this item: buttonType
        - tape_type:
          The reference key associated with this item: tapeType
        - snap_type:
          The reference key associated with this item: snapType
        - snap_part_type:
          The reference key associated with this item: snapPartType
        - tape_width_mm:
          The number (float) for tapeWidthMm
        - snap_width_mm:
          The number (float) for snapWidthMm
        - snap_repeat_length_mm:
          The number (float) for snapRepeatLengthMm
        - cordlock_toggle_type:
          The reference key associated with this item: cordlockToggleType
        - activation_temperature_number:
          The number (float) for activationTemperatureNumber
        - counter_type:
          The reference key associated with this item: counterType
        - dwell_time:
          The value associated with this item: dwellTime
        - general_construction:
          The reference key associated with this item: generalConstruction
        - elastic_type:
          The reference key associated with this item: elasticType
        - crossover_drawcord_indicator:
          The true or false flag associated with this item:
          crossoverDrawcordIndicator
        - elastic_drawcord_content_percentage:
          The number (float) for elasticDrawcordContentPercentage
        - elastic_drawcord_content_type:
          The reference key associated with this item:
          elasticDrawcordContentType
        - elastic_drawcord_content_source:
          The reference key associated with this item:
          elasticDrawcordContentSource
        - elastic_drawcord_aglet_material_item:
          The reference key associated with this item:
          elasticDrawcordAgletMaterialItem
        - elastic_drawcord_has_core_indicator:
          The true or false flag associated with this item:
          elasticDrawcordHasCoreIndicator
        - elastic_drawcord_elasticized_indicator:
          The true or false flag associated with this item:
          elasticDrawcordElasticizedIndicator
        - elastic_drawcord_shape:
          The reference key associated with this item: elasticDrawcordShape
        - elastic_drawcord_logo_name:
          The reference key associated with this item: elasticDrawcordLogoName
        - elastic_drawcord_dimension_width_indicator:
          The reference key associated with this item:
          elasticDrawcordDimensionWidthIndicator
        - elastic_drawcord_gripper_type:
          The reference key associated with this item:
          elasticDrawcordGripperType
        - elastic_drawcord_construction_type:
          The reference key associated with this item:
          elasticDrawcordConstructionType
        - elastic_drawcord_form:
          The reference key associated with this item: elasticDrawcordForm
        - elastic_drawcord_end_finish:
          The reference key associated with this item: elasticDrawcordEndFinish
        - elastic_drawcord_width_mm:
          The number (float) for elasticDrawcordWidthMm
        - elastic_drawcord_artwork_technique:
          The reference key associated with this item:
          elasticDrawcordArtworkTechnique
        - elastic_drawcord_finish_process:
          The reference key associated with this item:
          elasticDrawcordFinishProcess
        - elastic_drawcord_dye_method:
          The reference key associated with this item: elasticDrawcordDyeMethod
        - elastic_drawcord_visual_effect:
          The reference key associated with this item:
          elasticDrawcordVisualEffect
        - elastic_drawcord_number_of_colors:
          he reference key associated with this item:
          elasticDrawcordNumberOfColors
        - elastic_aglet_content_percentage:
          The number (float) for elasticAgletContentPercentage
        - elastic_aglet_content_type:
          The reference key associated with this item: elasticAgletContentType
        - elastic_aglet_content_source:
          The reference key associated with this item:
          elasticAgletContentSource
        - elastic_aglet_logo_name:
          The reference key associated with this item: elasticAgletLogoName
        - elastic_aglet_shape:
          The reference key associated with this item: elasticAgletShape
        - elastic_aglet_construction_type:
          The reference key associated with this item:
          elasticAgletConstructionType
        - elastic_aglet_width_mm:
          The number (float) for elasticAgletWidthMm
        - elastic_aglet_height_mm:
          The number (float) for elasticAgletHeightMm
        - elastic_aglet_internal_diameter_mm:
          The number (float) for elasticAgletInternalDiameterMm
        - elastic_aglet_grams_per_thousand_pieces:
          The number (float) for elasticAgletGramsPerThousandPieces
        - elastic_aglet_finish_process:
          The reference key associated with this item:
          elasticAgletFinishProcess
        - elastic_aglet_dye_method:
          The reference key associated with this item: elasticAgletDyeMethod
        - elastic_aglet_artwork_technique:
          The reference key associated with this item:
          elasticAgletArtworkTechnique
        - elastic_aglet_visual_effect:
          The reference key associated with this item: elasticAgletVisualEffect
        - elastic_aglet_number_of_colors:
          he reference key associated with this item:
          elasticAgletNumberOfColors
        - drawcord_material_item:
          The reference key associated with this item: drawcordMaterialItem
        - drawcord_aglet_material_item:
          The reference key associated with this item:
          drawcordAgletMaterialItem
        - drawcord_aglet_content_percentage:
          The number (float) for drawcordAgletContentPercentage
        - drawcord_aglet_content_type:
          The reference key associated with this item: drawcordAgletContentType
        - drawcord_aglet_content_source:
          The reference key associated with this item:
          drawcordAgletContentSource
        - drawcord_aglet_logo_name:
          The reference key associated with this item: drawcordAgletLogoName
        - drawcord_aglet_shape:
          The reference key associated with this item: drawcordAgletShape
        - drawcord_aglet_construction_type:
          The reference key associated with this item:
          drawcordAgletConstructionType
        - drawcord_aglet_width_mm:
          The number (float) for drawcordAgletWidthMm
        - drawcord_aglet_height_mm:
          The number (float) for drawcordAgletHeightMm
        - drawcord_aglet_internal_diameter_mm:
          The number (float) for drawcordAgletInternalDiameterMm
        - drawcord_aglet_grams_per_thousand_pieces:
          The number (float) for drawcordAgletGramsPerThousandPieces
        - drawcord_aglet_finish_process:
          The reference key associated with this item:
          drawcordAgletFinishProcess
        - drawcord_aglet_dye_method:
          The reference key associated with this item: drawcordAgletDyeMethod
        - drawcord_aglet_artwork_technique:
          The reference key associated with this item:
          drawcordAgletArtworkTechnique
        - drawcord_aglet_visual_effect:
          The reference key associated with this item:
          drawcordAgletVisualEffect
        - drawcord_aglet_number_of_colors:
          he reference key associated with this item:
          drawcordAgletNumberOfColors
        - hook_type:
          The reference key associated with this item: hookType
        - hook_loop_type:
          The reference key associated with this item: hookLoopType
        - label_type:
          The reference key associated with this item: labelType
        - fold_method:
          The reference key associated with this item: foldMethod
        - label_twill_direction:
          The reference key associated with this item: labelTwillDirection
        - backing_type:
          The reference key associated with this item: backingType
        - logo_size:
          The reference key associated with this item: logoSize
        - aglet_material_item:
          The reference key associated with this item: agletMaterialItem
        - has_aglet_indicator:
          The true or false flag associated with this item: hasAgletIndicator
        - number_of_bundles:
          The number for numberOfBundles
        - tip_content:
          The reference key associated with this item: tipContent
        - tip_type:
          The reference key associated with this item: tipType
        - magnet_cover_type:
          The reference key associated with this item: magnetCoverType
        - padding_type:
          The reference key associated with this item: paddingType
        - padding_orientation:
          The reference key associated with this item: paddingOrientation
        - layer_location:
          The reference key associated with this item: layerLocation
        - material_construction:
          The reference key associated with this item: materialConstruction
        - layer_finish_process:
          The reference key associated with this item: layerFinishProcess
        - layer_artwork_technique:
          The reference key associated with this item: layerArtworkTechnique
        - layer_content_percentage:
          The number (float) for layerContentPercentage
        - layer_content_type:
          The reference key associated with this item: layerContentType
        - layer_content_source:
          The reference key associated with this item: layerContentSource
        - pin_badge_type:
          The reference key associated with this item: pinBadgeType
        - plate_orientation:
          The reference key associated with this item: plateOrientation
        - ring_type:
          The reference key associated with this item: ringType
        - bonded_indicator:
          The true or false flag associated with this item: bondedIndicator
        - lubricated_indicator:
          The true or false flag associated with this item: lubricatedIndicator
        - thread_ply:
          The number of threadPly
        - thread_size:
          The number (float) for threadSize
        - alternate_thread_size:
          The number (float) for alternateThreadSize
        - thread_type:
          The reference key associated with this item: threadType
        - thread_brand_name:
          The reference key associated with this item: threadBrandName
        - thread_number_system:
          The reference key associated with this item: threadNumberSystem
        - thread_preparation:
          The reference key associated with this item: threadPreparation
        - thread_filament_count:
          The number for threadFilamentCount
        - thread_ply_count:
          The number for threadPlyCount
        - thread_luster:
          The reference key associated with this item: threadLuster
        - thread_statement_content:
          The reference key associated with this item: threadStatementContent
        - zipper_type:
          The reference key associated with this item: zipperType
        - zip_in_compatible_indicator:
          The true or false flag associated with this item:
          zipInCompatibleIndicator
        - zipper_performance:
          The reference key associated with this item: zipperPerformance
        - slider_pull_logo_name:
          The reference key associated with this item: sliderPullLogoName
        - slider_locking_function:
          The reference key associated with this item: sliderLockingFunction
        - slider_quantity:
          The number for sliderQuantity
        - slider_orientation:
          The reference key associated with this item: sliderOrientation
        - slider_size:
          The reference key associated with this item: sliderSize
        - intended_use_on:
          The reference key associated with this item: intendedUseOn
        - for_ball_type_and_size:
          The reference key associated with this item: forBallTypeAndSize
        - initial_pressure:
          The reference key associated with this item: initialPressure
        - slider_visual_effect:
          The reference key associated with this item: sliderVisualEffect
        - slider_pull_finish_process:
          The reference key associated with this item: sliderPullFinishProcess
        - slider_pull_artwork_technique:
          The reference key associated with this item:
          sliderPullArtworkTechnique
        - zipper_pull_code:
          The reference key associated with this item: zipperPullCode
        - zipper_tape_construction_type:
          The reference key associated with this item:
          zipperTapeConstructionType
        - zipper_tape_logo_name:
          The reference key associated with this item: zipperTapeLogoName
        - zipper_tape_width_mm:
          The number (float) for zipperTapeWidthMm
        - zipper_tape_finish_process:
          The reference key associated with this item: zipperTapeFinishProcess
        - zipper_tape_dye_method:
          The reference key associated with this item: zipperTapeDyeMethod
        - zipper_tape_artwork_technique:
          The reference key associated with this item:
          zipperTapeArtworkTechnique
        - zipper_tape_artwork_graphic:
          The reference key associated with this item: zipperTapeArtworkGraphic
        - zipper_tape_visual_effect:
          The reference key associated with this item: zipperTapeVisualEffect
        - teeth_type:
          The reference key associated with this item: teethType
        - special_zipper_teeth_orientation:
          The reference key associated with this item:
          specialZipperTeethOrientation
        - teeth_size:
          The reference key associated with this item: teethSize
        - teeth_shape:
          The reference key associated with this item: teethShape
        - teeth_repeat_length_mm:
          The number (float) for teethRepeatLengthMm
        - teeth_finish_process:
          The reference key associated with this item: teethFinishProcess
        - teeth_artwork_technique:
          The reference key associated with this item: teethArtworkTechnique
        - teeth_visual_effect:
          The reference key associated with this item: teethVisualEffect
        - contrast_thread_for_coil_indicator:
          The true or false flag associated with this item:
          contrastThreadForCoilIndicator
        - teeth_multi_colored_indicator:
          The true or false flag associated with this item:
          teethMultiColoredIndicator
        - zipper_stop_type:
          The reference key associated with this item: zipperStopType
        - zipper_stop_logo_name:
          The reference key associated with this item: zipperStopLogoName
        - zipper_stop_logo_placement:
          The reference key associated with this item: zipperStopLogoPlacement
        - aglet_construction_type:
          The reference key associated with this item: agletConstructionType
        - airbag_process:
          The reference key associated with this item: airbagProcess
        - airbag_type:
          The reference key associated with this item: airbagType
        - coloration_available:
          The reference key associated with this item: colorationAvailable
        - gas_content:
          The reference key associated with this item: gasContent
        - fill_type:
          The reference key associated with this item: fillType
        - scrim:
          The reference key associated with this item: scrim
        - down_cluster_statement:
          The reference key associated with this item: downClusterStatement
        - fill_power:
          The number for fillPower
        - natural_down_color:
          The reference key associated with this item: naturalDownColor
        - fill_form:
          The reference key associated with this item: fillForm
        - heat_set:
          The reference key associated with this item: heatSet
        - vendor_supplied_indicator:
          The true or false flag associated with this item:
          vendorSuppliedIndicator
        - corporate_designation_indicator:
          The true or false flag associated with this item:
          corporateDesignationIndicator
        - confidential_indicator:
          The true or false flag associated with this item:
          confidentialIndicator
        - country_of_origin_statement_indicator:
          The true or false flag associated with this item:
          countryOfOriginStatementIndicator
        - size_matrix_indicator:
          The true or false flag associated with this item: sizeMatrixIndicator
        - contains_corporate_logo_indicator:
          The true or false flag associated with this item:
          containsCorporateLogoIndicator
        - nav_indicator:
          The true or false flag associated with this item: navIndicator
        - packaging_intent:
          The reference key associated with this item: packagingIntent
        - packaging_statement:
          The reference key associated with this item: packagingStatement
        - card_type:
          The reference key associated with this item: cardType
        - card_construction_type:
          The reference key associated with this item: cardConstructionType
        - fluting_size:
          The reference key associated with this item: flutingSize
        - inner_linerboard_basis_weight:
          The number innerLinerboardBasisWeight
        - inner_linerboard_type:
          The reference key associated with this item: innerLinerboardType
        - medium_paper_basis_weight:
          The the number for mediumPaperBasisWeight
        - medium_paper_type:
          The reference key associated with this item: mediumPaperType
        - outer_linerboard_basis_weight:
          The number for outerLinerboardBasisWeight
        - outer_linerboard_type:
          The reference key associated with this item: outerLinerboardType
        - fastener_type:
          The reference key associated with this item: fastenerType
        - hanger_type:
          The reference key associated with this item: hangerType
        - hangtag_type:
          The reference key associated with this item: hangtagType
        - partition_type:
          The reference key associated with this item: partitionType
        - shoebag_type:
          The reference key associated with this item: shoebagType
        - shoe_form_type:
          The reference key associated with this item: shoeFormType
        - sticker_type:
          The reference key associated with this item: stickerType
        - tissue_type:
          The reference key associated with this item: tissueType
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/search/materials",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    kwargs.get("x_b_3_trace_id", None),
                    style="form",
                    explode=False,
                ),
            },
            query={
                "count": oapi.client.format_argument_value(
                    "count",
                    kwargs.get("count", None),
                    style="form",
                    explode=False,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    kwargs.get("offset", None),
                    style="form",
                    explode=False,
                ),
                "q": oapi.client.format_argument_value(
                    "q",
                    kwargs.get("q", ""),
                    style="form",
                    explode=False,
                ),
                "parentMaterialItemIdentifier": oapi.client.format_argument_value(  # noqa
                    "parentMaterialItemIdentifier",
                    kwargs.get("parent_material_item_identifier", None),
                    style="form",
                    explode=False,
                ),
                "materialType": oapi.client.format_argument_value(
                    "materialType",
                    kwargs.get("material_type", None),
                    style="form",
                    explode=False,
                ),
                "customsDescription": oapi.client.format_argument_value(
                    "customsDescription",
                    kwargs.get("customs_description", None),
                    style="form",
                    explode=False,
                ),
                "developmentTeam": oapi.client.format_argument_value(
                    "developmentTeam",
                    kwargs.get("development_team", None),
                    style="form",
                    explode=False,
                ),
                "materialNameVariationWeight": oapi.client.format_argument_value(  # noqa
                    "materialNameVariationWeight",
                    kwargs.get("material_name_variation_weight", None),
                    style="form",
                    explode=False,
                ),
                "materialNameVariationVisual": oapi.client.format_argument_value(  # noqa
                    "materialNameVariationVisual",
                    kwargs.get("material_name_variation_visual", None),
                    style="form",
                    explode=False,
                ),
                "targetPrice": oapi.client.format_argument_value(
                    "targetPrice",
                    kwargs.get("target_price", None),
                    style="form",
                    explode=False,
                ),
                "targetPriceUOM": oapi.client.format_argument_value(
                    "targetPriceUOM",
                    kwargs.get("target_price_uom", None),
                    style="form",
                    explode=False,
                ),
                "materialColorControlMode": oapi.client.format_argument_value(
                    "materialColorControlMode",
                    kwargs.get("material_color_control_mode", None),
                    style="form",
                    explode=False,
                ),
                "materialPricingMode": oapi.client.format_argument_value(
                    "materialPricingMode",
                    kwargs.get("material_pricing_mode", None),
                    style="form",
                    explode=False,
                ),
                "legacyCreatedOnDate": oapi.client.format_argument_value(
                    "legacyCreatedOnDate",
                    kwargs.get("legacy_created_on_date", None),
                    style="form",
                    explode=False,
                ),
                "legacyMaterialNumber": oapi.client.format_argument_value(
                    "legacyMaterialNumber",
                    kwargs.get("legacy_material_number", None),
                    style="form",
                    explode=False,
                ),
                "apparelPDMMaterialNumber": oapi.client.format_argument_value(
                    "apparelPDMMaterialNumber",
                    kwargs.get("apparel_pdm_material_number", None),
                    style="form",
                    explode=False,
                ),
                "division": oapi.client.format_argument_value(
                    "division",
                    kwargs.get("division", None),
                    style="form",
                    explode=False,
                ),
                "materialDevelopmentTeam": oapi.client.format_argument_value(
                    "materialDevelopmentTeam",
                    kwargs.get("material_development_team", None),
                    style="form",
                    explode=False,
                ),
                "targetStyle": oapi.client.format_argument_value(
                    "targetStyle",
                    kwargs.get("target_style", None),
                    style="form",
                    explode=False,
                ),
                "materialInitialCategory": oapi.client.format_argument_value(
                    "materialInitialCategory",
                    kwargs.get("material_initial_category", None),
                    style="form",
                    explode=False,
                ),
                "materialInitialCycleYear": oapi.client.format_argument_value(
                    "materialInitialCycleYear",
                    kwargs.get("material_initial_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "materialTargetCycleYear": oapi.client.format_argument_value(
                    "materialTargetCycleYear",
                    kwargs.get("material_target_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "materialItemStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "materialItemStatusIndicator",
                    kwargs.get("material_item_status_indicator", None),
                    style="form",
                    explode=False,
                ),
                "materialBOMIndicator": oapi.client.format_argument_value(
                    "materialBOMIndicator",
                    kwargs.get("material_bom_indicator", None),
                    style="form",
                    explode=False,
                ),
                "createTimestamp": oapi.client.format_argument_value(
                    "createTimestamp",
                    kwargs.get("create_timestamp", None),
                    style="form",
                    explode=False,
                ),
                "changeTimestamp": oapi.client.format_argument_value(
                    "changeTimestamp",
                    kwargs.get("change_timestamp", None),
                    style="form",
                    explode=False,
                ),
                "materialContentPercentage": oapi.client.format_argument_value(
                    "materialContentPercentage",
                    kwargs.get("material_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "materialContentType": oapi.client.format_argument_value(
                    "materialContentType",
                    kwargs.get("material_content_type", None),
                    style="form",
                    explode=False,
                ),
                "materialContentSource": oapi.client.format_argument_value(
                    "materialContentSource",
                    kwargs.get("material_content_source", None),
                    style="form",
                    explode=False,
                ),
                "materialLabelContentPercentage": oapi.client.format_argument_value(  # noqa
                    "materialLabelContentPercentage",
                    kwargs.get("material_label_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "materialLabelContentType": oapi.client.format_argument_value(
                    "materialLabelContentType",
                    kwargs.get("material_label_content_type", None),
                    style="form",
                    explode=False,
                ),
                "materialLabelContentSource": oapi.client.format_argument_value(  # noqa
                    "materialLabelContentSource",
                    kwargs.get("material_label_content_source", None),
                    style="form",
                    explode=False,
                ),
                "materialFamily": oapi.client.format_argument_value(
                    "materialFamily",
                    kwargs.get("material_family", None),
                    style="form",
                    explode=False,
                ),
                "materialOwner": oapi.client.format_argument_value(
                    "materialOwner",
                    kwargs.get("material_owner", None),
                    style="form",
                    explode=False,
                ),
                "artworkGraphic": oapi.client.format_argument_value(
                    "artworkGraphic",
                    kwargs.get("artwork_graphic", None),
                    style="form",
                    explode=False,
                ),
                "artworkTechnique": oapi.client.format_argument_value(
                    "artworkTechnique",
                    kwargs.get("artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "secondaryProcessIndicator": oapi.client.format_argument_value(
                    "secondaryProcessIndicator",
                    kwargs.get("secondary_process_indicator", None),
                    style="form",
                    explode=False,
                ),
                "artworkApplicationLocation": oapi.client.format_argument_value(  # noqa
                    "artworkApplicationLocation",
                    kwargs.get("artwork_application_location", None),
                    style="form",
                    explode=False,
                ),
                "artworkRepeatLengthCm": oapi.client.format_argument_value(
                    "artworkRepeatLengthCm",
                    kwargs.get("artwork_repeat_length_cm", None),
                    style="form",
                    explode=False,
                ),
                "directionalPatternIndicator": oapi.client.format_argument_value(  # noqa
                    "directionalPatternIndicator",
                    kwargs.get("directional_pattern_indicator", None),
                    style="form",
                    explode=False,
                ),
                "garmentLocationPlacement": oapi.client.format_argument_value(
                    "garmentLocationPlacement",
                    kwargs.get("garment_location_placement", None),
                    style="form",
                    explode=False,
                ),
                "endUse": oapi.client.format_argument_value(
                    "endUse",
                    kwargs.get("end_use", None),
                    style="form",
                    explode=False,
                ),
                "developmentReason": oapi.client.format_argument_value(
                    "developmentReason",
                    kwargs.get("development_reason", None),
                    style="form",
                    explode=False,
                ),
                "materialBenefits": oapi.client.format_argument_value(
                    "materialBenefits",
                    kwargs.get("material_benefits", None),
                    style="form",
                    explode=False,
                ),
                "fabricFaceDesignation": oapi.client.format_argument_value(
                    "fabricFaceDesignation",
                    kwargs.get("fabric_face_designation", None),
                    style="form",
                    explode=False,
                ),
                "stretchDirection": oapi.client.format_argument_value(
                    "stretchDirection",
                    kwargs.get("stretch_direction", None),
                    style="form",
                    explode=False,
                ),
                "thicknessMm": oapi.client.format_argument_value(
                    "thicknessMm",
                    kwargs.get("thickness_mm", None),
                    style="form",
                    explode=False,
                ),
                "thicknessSelection": oapi.client.format_argument_value(
                    "thicknessSelection",
                    kwargs.get("thickness_selection", None),
                    style="form",
                    explode=False,
                ),
                "maximumThicknessMm": oapi.client.format_argument_value(
                    "maximumThicknessMm",
                    kwargs.get("maximum_thickness_mm", None),
                    style="form",
                    explode=False,
                ),
                "minimumThicknessMm": oapi.client.format_argument_value(
                    "minimumThicknessMm",
                    kwargs.get("minimum_thickness_mm", None),
                    style="form",
                    explode=False,
                ),
                "lengthMm": oapi.client.format_argument_value(
                    "lengthMm",
                    kwargs.get("length_mm", None),
                    style="form",
                    explode=False,
                ),
                "lengthCm": oapi.client.format_argument_value(
                    "lengthCm",
                    kwargs.get("length_cm", None),
                    style="form",
                    explode=False,
                ),
                "dimensionWidthIndicator": oapi.client.format_argument_value(
                    "dimensionWidthIndicator",
                    kwargs.get("dimension_width_indicator", None),
                    style="form",
                    explode=False,
                ),
                "widthMm": oapi.client.format_argument_value(
                    "widthMm",
                    kwargs.get("width_mm", None),
                    style="form",
                    explode=False,
                ),
                "widthCm": oapi.client.format_argument_value(
                    "widthCm",
                    kwargs.get("width_cm", None),
                    style="form",
                    explode=False,
                ),
                "heightMm": oapi.client.format_argument_value(
                    "heightMm",
                    kwargs.get("height_mm", None),
                    style="form",
                    explode=False,
                ),
                "heightCm": oapi.client.format_argument_value(
                    "heightCm",
                    kwargs.get("height_cm", None),
                    style="form",
                    explode=False,
                ),
                "weightGramsPerSquareMeter": oapi.client.format_argument_value(
                    "weightGramsPerSquareMeter",
                    kwargs.get("weight_grams_per_square_meter", None),
                    style="form",
                    explode=False,
                ),
                "externalDiameterMm": oapi.client.format_argument_value(
                    "externalDiameterMm",
                    kwargs.get("external_diameter_mm", None),
                    style="form",
                    explode=False,
                ),
                "externalLengthMm": oapi.client.format_argument_value(
                    "externalLengthMm",
                    kwargs.get("external_length_mm", None),
                    style="form",
                    explode=False,
                ),
                "externalWidthMm": oapi.client.format_argument_value(
                    "externalWidthMm",
                    kwargs.get("external_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "internalDiameterMm": oapi.client.format_argument_value(
                    "internalDiameterMm",
                    kwargs.get("internal_diameter_mm", None),
                    style="form",
                    explode=False,
                ),
                "internalLengthMm": oapi.client.format_argument_value(
                    "internalLengthMm",
                    kwargs.get("internal_length_mm", None),
                    style="form",
                    explode=False,
                ),
                "internalWidthMm": oapi.client.format_argument_value(
                    "internalWidthMm",
                    kwargs.get("internal_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "gaugeInch": oapi.client.format_argument_value(
                    "gaugeInch",
                    kwargs.get("gauge_inch", None),
                    style="form",
                    explode=False,
                ),
                "gramsPerThousandPieces": oapi.client.format_argument_value(
                    "gramsPerThousandPieces",
                    kwargs.get("grams_per_thousand_pieces", None),
                    style="form",
                    explode=False,
                ),
                "weightGramsPerThousandPieces": oapi.client.format_argument_value(  # noqa
                    "weightGramsPerThousandPieces",
                    kwargs.get("weight_grams_per_thousand_pieces", None),
                    style="form",
                    explode=False,
                ),
                "weightGramsPerLinearYard": oapi.client.format_argument_value(
                    "weightGramsPerLinearYard",
                    kwargs.get("weight_grams_per_linear_yard", None),
                    style="form",
                    explode=False,
                ),
                "weightGramsPerLinearMeter": oapi.client.format_argument_value(
                    "weightGramsPerLinearMeter",
                    kwargs.get("weight_grams_per_linear_meter", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionContentPercentage": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionContentPercentage",
                    kwargs.get("yarn_composition_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionContentType": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionContentType",
                    kwargs.get("yarn_composition_content_type", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionContentSource": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionContentSource",
                    kwargs.get("yarn_composition_content_source", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionLocation": oapi.client.format_argument_value(
                    "yarnCompositionLocation",
                    kwargs.get("yarn_composition_location", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionType": oapi.client.format_argument_value(
                    "yarnCompositionType",
                    kwargs.get("yarn_composition_type", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionSize": oapi.client.format_argument_value(
                    "yarnCompositionSize",
                    kwargs.get("yarn_composition_size", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionSpinningMethod": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionSpinningMethod",
                    kwargs.get("yarn_composition_spinning_method", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionCount": oapi.client.format_argument_value(
                    "yarnCompositionCount",
                    kwargs.get("yarn_composition_count", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionPreparation": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionPreparation",
                    kwargs.get("yarn_composition_preparation", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionCrossSection": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionCrossSection",
                    kwargs.get("yarn_composition_cross_section", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionFilamentCount": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionFilamentCount",
                    kwargs.get("yarn_composition_filament_count", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionNumberSystem": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionNumberSystem",
                    kwargs.get("yarn_composition_number_system", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionLuster": oapi.client.format_argument_value(
                    "yarnCompositionLuster",
                    kwargs.get("yarn_composition_luster", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionBrand": oapi.client.format_argument_value(
                    "yarnCompositionBrand",
                    kwargs.get("yarn_composition_brand", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionTexture": oapi.client.format_argument_value(
                    "yarnCompositionTexture",
                    kwargs.get("yarn_composition_texture", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionTwist": oapi.client.format_argument_value(
                    "yarnCompositionTwist",
                    kwargs.get("yarn_composition_twist", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionFinishProcess": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionFinishProcess",
                    kwargs.get("yarn_composition_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionDyeMethod": oapi.client.format_argument_value(
                    "yarnCompositionDyeMethod",
                    kwargs.get("yarn_composition_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionVisualEffect": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionVisualEffect",
                    kwargs.get("yarn_composition_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionFixedColor": oapi.client.format_argument_value(
                    "yarnCompositionFixedColor",
                    kwargs.get("yarn_composition_fixed_color", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionUsagePercentage": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionUsagePercentage",
                    kwargs.get("yarn_composition_usage_percentage", None),
                    style="form",
                    explode=False,
                ),
                "plyContentPercentage": oapi.client.format_argument_value(
                    "plyContentPercentage",
                    kwargs.get("ply_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "plyContentType": oapi.client.format_argument_value(
                    "plyContentType",
                    kwargs.get("ply_content_type", None),
                    style="form",
                    explode=False,
                ),
                "plyContentSource": oapi.client.format_argument_value(
                    "plyContentSource",
                    kwargs.get("ply_content_source", None),
                    style="form",
                    explode=False,
                ),
                "plyLocation": oapi.client.format_argument_value(
                    "plyLocation",
                    kwargs.get("ply_location", None),
                    style="form",
                    explode=False,
                ),
                "plyType": oapi.client.format_argument_value(
                    "plyType",
                    kwargs.get("ply_type", None),
                    style="form",
                    explode=False,
                ),
                "plyBrand": oapi.client.format_argument_value(
                    "plyBrand",
                    kwargs.get("ply_brand", None),
                    style="form",
                    explode=False,
                ),
                "plySize": oapi.client.format_argument_value(
                    "plySize",
                    kwargs.get("ply_size", None),
                    style="form",
                    explode=False,
                ),
                "plyNumberSystem": oapi.client.format_argument_value(
                    "plyNumberSystem",
                    kwargs.get("ply_number_system", None),
                    style="form",
                    explode=False,
                ),
                "plyCrossSection": oapi.client.format_argument_value(
                    "plyCrossSection",
                    kwargs.get("ply_cross_section", None),
                    style="form",
                    explode=False,
                ),
                "plySpinningMethod": oapi.client.format_argument_value(
                    "plySpinningMethod",
                    kwargs.get("ply_spinning_method", None),
                    style="form",
                    explode=False,
                ),
                "plyFilamentCount": oapi.client.format_argument_value(
                    "plyFilamentCount",
                    kwargs.get("ply_filament_count", None),
                    style="form",
                    explode=False,
                ),
                "plyTwist": oapi.client.format_argument_value(
                    "plyTwist",
                    kwargs.get("ply_twist", None),
                    style="form",
                    explode=False,
                ),
                "plyLuster": oapi.client.format_argument_value(
                    "plyLuster",
                    kwargs.get("ply_luster", None),
                    style="form",
                    explode=False,
                ),
                "plyTexture": oapi.client.format_argument_value(
                    "plyTexture",
                    kwargs.get("ply_texture", None),
                    style="form",
                    explode=False,
                ),
                "plyFinishProcess": oapi.client.format_argument_value(
                    "plyFinishProcess",
                    kwargs.get("ply_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "plyDyeMethod": oapi.client.format_argument_value(
                    "plyDyeMethod",
                    kwargs.get("ply_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "plyVisualEffect": oapi.client.format_argument_value(
                    "plyVisualEffect",
                    kwargs.get("ply_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "plyFixedColor": oapi.client.format_argument_value(
                    "plyFixedColor",
                    kwargs.get("ply_fixed_color", None),
                    style="form",
                    explode=False,
                ),
                "plyUsagePercentage": oapi.client.format_argument_value(
                    "plyUsagePercentage",
                    kwargs.get("ply_usage_percentage", None),
                    style="form",
                    explode=False,
                ),
                "fiberContentPercentage": oapi.client.format_argument_value(
                    "fiberContentPercentage",
                    kwargs.get("fiber_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "fiberContentType": oapi.client.format_argument_value(
                    "fiberContentType",
                    kwargs.get("fiber_content_type", None),
                    style="form",
                    explode=False,
                ),
                "fiberContentSource": oapi.client.format_argument_value(
                    "fiberContentSource",
                    kwargs.get("fiber_content_source", None),
                    style="form",
                    explode=False,
                ),
                "fiberSize": oapi.client.format_argument_value(
                    "fiberSize",
                    kwargs.get("fiber_size", None),
                    style="form",
                    explode=False,
                ),
                "fiberPlyLocation": oapi.client.format_argument_value(
                    "fiberPlyLocation",
                    kwargs.get("fiber_ply_location", None),
                    style="form",
                    explode=False,
                ),
                "fiberStapleNumberSystem": oapi.client.format_argument_value(
                    "fiberStapleNumberSystem",
                    kwargs.get("fiber_staple_number_system", None),
                    style="form",
                    explode=False,
                ),
                "fiberStapleLength": oapi.client.format_argument_value(
                    "fiberStapleLength",
                    kwargs.get("fiber_staple_length", None),
                    style="form",
                    explode=False,
                ),
                "fiberStapleLengthMin": oapi.client.format_argument_value(
                    "fiberStapleLengthMin",
                    kwargs.get("fiber_staple_length_min", None),
                    style="form",
                    explode=False,
                ),
                "fiberStapleLengthMax": oapi.client.format_argument_value(
                    "fiberStapleLengthMax",
                    kwargs.get("fiber_staple_length_max", None),
                    style="form",
                    explode=False,
                ),
                "fiberDiameter": oapi.client.format_argument_value(
                    "fiberDiameter",
                    kwargs.get("fiber_diameter", None),
                    style="form",
                    explode=False,
                ),
                "fiberDiameterMin": oapi.client.format_argument_value(
                    "fiberDiameterMin",
                    kwargs.get("fiber_diameter_min", None),
                    style="form",
                    explode=False,
                ),
                "fiberDiameterMax": oapi.client.format_argument_value(
                    "fiberDiameterMax",
                    kwargs.get("fiber_diameter_max", None),
                    style="form",
                    explode=False,
                ),
                "fiberDiameterUnit": oapi.client.format_argument_value(
                    "fiberDiameterUnit",
                    kwargs.get("fiber_diameter_unit", None),
                    style="form",
                    explode=False,
                ),
                "fiberPreparation": oapi.client.format_argument_value(
                    "fiberPreparation",
                    kwargs.get("fiber_preparation", None),
                    style="form",
                    explode=False,
                ),
                "fiberCrossSection": oapi.client.format_argument_value(
                    "fiberCrossSection",
                    kwargs.get("fiber_cross_section", None),
                    style="form",
                    explode=False,
                ),
                "fiberLuster": oapi.client.format_argument_value(
                    "fiberLuster",
                    kwargs.get("fiber_luster", None),
                    style="form",
                    explode=False,
                ),
                "fiberFinishProcess": oapi.client.format_argument_value(
                    "fiberFinishProcess",
                    kwargs.get("fiber_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "fiberDyeMethod": oapi.client.format_argument_value(
                    "fiberDyeMethod",
                    kwargs.get("fiber_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "fiberUsagePercentage": oapi.client.format_argument_value(
                    "fiberUsagePercentage",
                    kwargs.get("fiber_usage_percentage", None),
                    style="form",
                    explode=False,
                ),
                "edgeFinish": oapi.client.format_argument_value(
                    "edgeFinish",
                    kwargs.get("edge_finish", None),
                    style="form",
                    explode=False,
                ),
                "visualEffect": oapi.client.format_argument_value(
                    "visualEffect",
                    kwargs.get("visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "visualEffectLocation": oapi.client.format_argument_value(
                    "visualEffectLocation",
                    kwargs.get("visual_effect_location", None),
                    style="form",
                    explode=False,
                ),
                "applicationTechnique": oapi.client.format_argument_value(
                    "applicationTechnique",
                    kwargs.get("application_technique", None),
                    style="form",
                    explode=False,
                ),
                "finishProcess": oapi.client.format_argument_value(
                    "finishProcess",
                    kwargs.get("finish_process", None),
                    style="form",
                    explode=False,
                ),
                "finishLocation": oapi.client.format_argument_value(
                    "finishLocation",
                    kwargs.get("finish_location", None),
                    style="form",
                    explode=False,
                ),
                "numberOfPasses": oapi.client.format_argument_value(
                    "numberOfPasses",
                    kwargs.get("number_of_passes", None),
                    style="form",
                    explode=False,
                ),
                "materialTechnologies": oapi.client.format_argument_value(
                    "materialTechnologies",
                    kwargs.get("material_technologies", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperCode": oapi.client.format_argument_value(
                    "releasePaperCode",
                    kwargs.get("release_paper_code", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperOne": oapi.client.format_argument_value(
                    "releasePaperOne",
                    kwargs.get("release_paper_one", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperTwo": oapi.client.format_argument_value(
                    "releasePaperTwo",
                    kwargs.get("release_paper_two", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperSideOne": oapi.client.format_argument_value(
                    "releasePaperSideOne",
                    kwargs.get("release_paper_side_one", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperSideTwo": oapi.client.format_argument_value(
                    "releasePaperSideTwo",
                    kwargs.get("release_paper_side_two", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperFinishProcess": oapi.client.format_argument_value(
                    "releasePaperFinishProcess",
                    kwargs.get("release_paper_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "topLayerMaterialItem": oapi.client.format_argument_value(
                    "topLayerMaterialItem",
                    kwargs.get("top_layer_material_item", None),
                    style="form",
                    explode=False,
                ),
                "middleLayer1MaterialItem": oapi.client.format_argument_value(
                    "middleLayer1MaterialItem",
                    kwargs.get("middle_layer_1_material_item", None),
                    style="form",
                    explode=False,
                ),
                "middleLayer2MaterialItem": oapi.client.format_argument_value(
                    "middleLayer2MaterialItem",
                    kwargs.get("middle_layer_2_material_item", None),
                    style="form",
                    explode=False,
                ),
                "middleLayer3MaterialItem": oapi.client.format_argument_value(
                    "middleLayer3MaterialItem",
                    kwargs.get("middle_layer_3_material_item", None),
                    style="form",
                    explode=False,
                ),
                "bottomLayerMaterialItem": oapi.client.format_argument_value(
                    "bottomLayerMaterialItem",
                    kwargs.get("bottom_layer_material_item", None),
                    style="form",
                    explode=False,
                ),
                "nonWovenSubstrateType": oapi.client.format_argument_value(
                    "nonWovenSubstrateType",
                    kwargs.get("non_woven_substrate_type", None),
                    style="form",
                    explode=False,
                ),
                "nonWovenWebBondingMethod": oapi.client.format_argument_value(
                    "nonWovenWebBondingMethod",
                    kwargs.get("non_woven_web_bonding_method", None),
                    style="form",
                    explode=False,
                ),
                "colorDominance": oapi.client.format_argument_value(
                    "colorDominance",
                    kwargs.get("color_dominance", None),
                    style="form",
                    explode=False,
                ),
                "colorEffect": oapi.client.format_argument_value(
                    "colorEffect",
                    kwargs.get("color_effect", None),
                    style="form",
                    explode=False,
                ),
                "colorPosition": oapi.client.format_argument_value(
                    "colorPosition",
                    kwargs.get("color_position", None),
                    style="form",
                    explode=False,
                ),
                "colorLocation": oapi.client.format_argument_value(
                    "colorLocation",
                    kwargs.get("color_location", None),
                    style="form",
                    explode=False,
                ),
                "colorCallout": oapi.client.format_argument_value(
                    "colorCallout",
                    kwargs.get("color_callout", None),
                    style="form",
                    explode=False,
                ),
                "colorFiber": oapi.client.format_argument_value(
                    "colorFiber",
                    kwargs.get("color_fiber", None),
                    style="form",
                    explode=False,
                ),
                "dyeMethod": oapi.client.format_argument_value(
                    "dyeMethod",
                    kwargs.get("dye_method", None),
                    style="form",
                    explode=False,
                ),
                "dyeType": oapi.client.format_argument_value(
                    "dyeType",
                    kwargs.get("dye_type", None),
                    style="form",
                    explode=False,
                ),
                "activeCategory": oapi.client.format_argument_value(
                    "activeCategory",
                    kwargs.get("active_category", None),
                    style="form",
                    explode=False,
                ),
                "activeCycleYear": oapi.client.format_argument_value(
                    "activeCycleYear",
                    kwargs.get("active_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "webFormation": oapi.client.format_argument_value(
                    "webFormation",
                    kwargs.get("web_formation", None),
                    style="form",
                    explode=False,
                ),
                "numberOfColors": oapi.client.format_argument_value(
                    "numberOfColors",
                    kwargs.get("number_of_colors", None),
                    style="form",
                    explode=False,
                ),
                "lastIdentifier": oapi.client.format_argument_value(
                    "lastIdentifier",
                    kwargs.get("last_identifier", None),
                    style="form",
                    explode=False,
                ),
                "animalSource": oapi.client.format_argument_value(
                    "animalSource",
                    kwargs.get("animal_source", None),
                    style="form",
                    explode=False,
                ),
                "dyedThroughCrustIndicator": oapi.client.format_argument_value(
                    "dyedThroughCrustIndicator",
                    kwargs.get("dyed_through_crust_indicator", None),
                    style="form",
                    explode=False,
                ),
                "oilContent": oapi.client.format_argument_value(
                    "oilContent",
                    kwargs.get("oil_content", None),
                    style="form",
                    explode=False,
                ),
                "reTannage": oapi.client.format_argument_value(
                    "reTannage",
                    kwargs.get("re_tannage", None),
                    style="form",
                    explode=False,
                ),
                "washableIndicator": oapi.client.format_argument_value(
                    "washableIndicator",
                    kwargs.get("washable_indicator", None),
                    style="form",
                    explode=False,
                ),
                "compositionLeatherType": oapi.client.format_argument_value(
                    "compositionLeatherType",
                    kwargs.get("composition_leather_type", None),
                    style="form",
                    explode=False,
                ),
                "grainLeatherType": oapi.client.format_argument_value(
                    "grainLeatherType",
                    kwargs.get("grain_leather_type", None),
                    style="form",
                    explode=False,
                ),
                "grainLeatherSubType": oapi.client.format_argument_value(
                    "grainLeatherSubType",
                    kwargs.get("grain_leather_sub_type", None),
                    style="form",
                    explode=False,
                ),
                "splitLeatherType": oapi.client.format_argument_value(
                    "splitLeatherType",
                    kwargs.get("split_leather_type", None),
                    style="form",
                    explode=False,
                ),
                "averagePUThickness": oapi.client.format_argument_value(
                    "averagePUThickness",
                    kwargs.get("average_pu_thickness", None),
                    style="form",
                    explode=False,
                ),
                "coatingThicknessMm": oapi.client.format_argument_value(
                    "coatingThicknessMm",
                    kwargs.get("coating_thickness_mm", None),
                    style="form",
                    explode=False,
                ),
                "moldable": oapi.client.format_argument_value(
                    "moldable",
                    kwargs.get("moldable", None),
                    style="form",
                    explode=False,
                ),
                "substrateProcessingType": oapi.client.format_argument_value(
                    "substrateProcessingType",
                    kwargs.get("substrate_processing_type", None),
                    style="form",
                    explode=False,
                ),
                "substratePUDippedIndicator": oapi.client.format_argument_value(  # noqa
                    "substratePUDippedIndicator",
                    kwargs.get("substrate_pu_dipped_indicator", None),
                    style="form",
                    explode=False,
                ),
                "substrateConstruction": oapi.client.format_argument_value(
                    "substrateConstruction",
                    kwargs.get("substrate_construction", None),
                    style="form",
                    explode=False,
                ),
                "textileConstructionType": oapi.client.format_argument_value(
                    "textileConstructionType",
                    kwargs.get("textile_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "textileSubVariation": oapi.client.format_argument_value(
                    "textileSubVariation",
                    kwargs.get("textile_sub_variation", None),
                    style="form",
                    explode=False,
                ),
                "textileSubVariationTwo": oapi.client.format_argument_value(
                    "textileSubVariationTwo",
                    kwargs.get("textile_sub_variation_two", None),
                    style="form",
                    explode=False,
                ),
                "textileVariation": oapi.client.format_argument_value(
                    "textileVariation",
                    kwargs.get("textile_variation", None),
                    style="form",
                    explode=False,
                ),
                "endsPerInchNumber": oapi.client.format_argument_value(
                    "endsPerInchNumber",
                    kwargs.get("ends_per_inch_number", None),
                    style="form",
                    explode=False,
                ),
                "picksPerInchNumber": oapi.client.format_argument_value(
                    "picksPerInchNumber",
                    kwargs.get("picks_per_inch_number", None),
                    style="form",
                    explode=False,
                ),
                "machineryType": oapi.client.format_argument_value(
                    "machineryType",
                    kwargs.get("machinery_type", None),
                    style="form",
                    explode=False,
                ),
                "warpCount": oapi.client.format_argument_value(
                    "warpCount",
                    kwargs.get("warp_count", None),
                    style="form",
                    explode=False,
                ),
                "weftCount": oapi.client.format_argument_value(
                    "weftCount",
                    kwargs.get("weft_count", None),
                    style="form",
                    explode=False,
                ),
                "twillConstructionType": oapi.client.format_argument_value(
                    "twillConstructionType",
                    kwargs.get("twill_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "twillDirection": oapi.client.format_argument_value(
                    "twillDirection",
                    kwargs.get("twill_direction", None),
                    style="form",
                    explode=False,
                ),
                "foldIndicator": oapi.client.format_argument_value(
                    "foldIndicator",
                    kwargs.get("fold_indicator", None),
                    style="form",
                    explode=False,
                ),
                "ribConstruction": oapi.client.format_argument_value(
                    "ribConstruction",
                    kwargs.get("rib_construction", None),
                    style="form",
                    explode=False,
                ),
                "heightIndicator": oapi.client.format_argument_value(
                    "heightIndicator",
                    kwargs.get("height_indicator", None),
                    style="form",
                    explode=False,
                ),
                "rowsOfSpandex": oapi.client.format_argument_value(
                    "rowsOfSpandex",
                    kwargs.get("rows_of_spandex", None),
                    style="form",
                    explode=False,
                ),
                "partTypeOrientation": oapi.client.format_argument_value(
                    "partTypeOrientation",
                    kwargs.get("part_type_orientation", None),
                    style="form",
                    explode=False,
                ),
                "initialDevelopmentProductAlias": oapi.client.format_argument_value(  # noqa
                    "initialDevelopmentProductAlias",
                    kwargs.get("initial_development_product_alias", None),
                    style="form",
                    explode=False,
                ),
                "preTwistYarn": oapi.client.format_argument_value(
                    "preTwistYarn",
                    kwargs.get("pre_twist_yarn", None),
                    style="form",
                    explode=False,
                ),
                "program": oapi.client.format_argument_value(
                    "program",
                    kwargs.get("program", None),
                    style="form",
                    explode=False,
                ),
                "steamMethod": oapi.client.format_argument_value(
                    "steamMethod",
                    kwargs.get("steam_method", None),
                    style="form",
                    explode=False,
                ),
                "structureTestingReference": oapi.client.format_argument_value(
                    "structureTestingReference",
                    kwargs.get("structure_testing_reference", None),
                    style="form",
                    explode=False,
                ),
                "structureReferenceNumber": oapi.client.format_argument_value(
                    "structureReferenceNumber",
                    kwargs.get("structure_reference_number", None),
                    style="form",
                    explode=False,
                ),
                "structureCoverage": oapi.client.format_argument_value(
                    "structureCoverage",
                    kwargs.get("structure_coverage", None),
                    style="form",
                    explode=False,
                ),
                "blanketNumber": oapi.client.format_argument_value(
                    "blanketNumber",
                    kwargs.get("blanket_number", None),
                    style="form",
                    explode=False,
                ),
                "yarnSize": oapi.client.format_argument_value(
                    "yarnSize",
                    kwargs.get("yarn_size", None),
                    style="form",
                    explode=False,
                ),
                "yarnSpinningMethod": oapi.client.format_argument_value(
                    "yarnSpinningMethod",
                    kwargs.get("yarn_spinning_method", None),
                    style="form",
                    explode=False,
                ),
                "allPlysTheSameIndicator": oapi.client.format_argument_value(
                    "allPlysTheSameIndicator",
                    kwargs.get("all_plys_the_same_indicator", None),
                    style="form",
                    explode=False,
                ),
                "fancyYarn": oapi.client.format_argument_value(
                    "fancyYarn",
                    kwargs.get("fancy_yarn", None),
                    style="form",
                    explode=False,
                ),
                "fixedColor": oapi.client.format_argument_value(
                    "fixedColor",
                    kwargs.get("fixed_color", None),
                    style="form",
                    explode=False,
                ),
                "yarnBrand": oapi.client.format_argument_value(
                    "yarnBrand",
                    kwargs.get("yarn_brand", None),
                    style="form",
                    explode=False,
                ),
                "yarnNumberSystem": oapi.client.format_argument_value(
                    "yarnNumberSystem",
                    kwargs.get("yarn_number_system", None),
                    style="form",
                    explode=False,
                ),
                "yarnTwist": oapi.client.format_argument_value(
                    "yarnTwist",
                    kwargs.get("yarn_twist", None),
                    style="form",
                    explode=False,
                ),
                "yarnPlyCount": oapi.client.format_argument_value(
                    "yarnPlyCount",
                    kwargs.get("yarn_ply_count", None),
                    style="form",
                    explode=False,
                ),
                "yarnType": oapi.client.format_argument_value(
                    "yarnType",
                    kwargs.get("yarn_type", None),
                    style="form",
                    explode=False,
                ),
                "yarnLuster": oapi.client.format_argument_value(
                    "yarnLuster",
                    kwargs.get("yarn_luster", None),
                    style="form",
                    explode=False,
                ),
                "yarnFinishProcess": oapi.client.format_argument_value(
                    "yarnFinishProcess",
                    kwargs.get("yarn_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "yarnDyeMethod": oapi.client.format_argument_value(
                    "yarnDyeMethod",
                    kwargs.get("yarn_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "yarnVisualEffect": oapi.client.format_argument_value(
                    "yarnVisualEffect",
                    kwargs.get("yarn_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "yarnNumberOfEnds": oapi.client.format_argument_value(
                    "yarnNumberOfEnds",
                    kwargs.get("yarn_number_of_ends", None),
                    style="form",
                    explode=False,
                ),
                "yarnFilamentCount": oapi.client.format_argument_value(
                    "yarnFilamentCount",
                    kwargs.get("yarn_filament_count", None),
                    style="form",
                    explode=False,
                ),
                "yarnCoveringMethod": oapi.client.format_argument_value(
                    "yarnCoveringMethod",
                    kwargs.get("yarn_covering_method", None),
                    style="form",
                    explode=False,
                ),
                "yarnTexture": oapi.client.format_argument_value(
                    "yarnTexture",
                    kwargs.get("yarn_texture", None),
                    style="form",
                    explode=False,
                ),
                "microfiberIndicator": oapi.client.format_argument_value(
                    "microfiberIndicator",
                    kwargs.get("microfiber_indicator", None),
                    style="form",
                    explode=False,
                ),
                "yarnPreparation": oapi.client.format_argument_value(
                    "yarnPreparation",
                    kwargs.get("yarn_preparation", None),
                    style="form",
                    explode=False,
                ),
                "yarnCrossSection": oapi.client.format_argument_value(
                    "yarnCrossSection",
                    kwargs.get("yarn_cross_section", None),
                    style="form",
                    explode=False,
                ),
                "yarnLocation": oapi.client.format_argument_value(
                    "yarnLocation",
                    kwargs.get("yarn_location", None),
                    style="form",
                    explode=False,
                ),
                "yarnSuppliedMaterial": oapi.client.format_argument_value(
                    "yarnSuppliedMaterial",
                    kwargs.get("yarn_supplied_material", None),
                    style="form",
                    explode=False,
                ),
                "heatSetting": oapi.client.format_argument_value(
                    "heatSetting",
                    kwargs.get("heat_setting", None),
                    style="form",
                    explode=False,
                ),
                "intermingling": oapi.client.format_argument_value(
                    "intermingling",
                    kwargs.get("intermingling", None),
                    style="form",
                    explode=False,
                ),
                "chemicalProduct": oapi.client.format_argument_value(
                    "chemicalProduct",
                    kwargs.get("chemical_product", None),
                    style="form",
                    explode=False,
                ),
                "chemicalSupplier": oapi.client.format_argument_value(
                    "chemicalSupplier",
                    kwargs.get("chemical_supplier", None),
                    style="form",
                    explode=False,
                ),
                "complianceAccreditation": oapi.client.format_argument_value(
                    "complianceAccreditation",
                    kwargs.get("compliance_accreditation", None),
                    style="form",
                    explode=False,
                ),
                "yarnSuppliedMaterialNumberOfEnds": oapi.client.format_argument_value(  # noqa
                    "yarnSuppliedMaterialNumberOfEnds",
                    kwargs.get("yarn_supplied_material_number_of_ends", None),
                    style="form",
                    explode=False,
                ),
                "yarnUsagePercentage": oapi.client.format_argument_value(
                    "yarnUsagePercentage",
                    kwargs.get("yarn_usage_percentage", None),
                    style="form",
                    explode=False,
                ),
                "baseType": oapi.client.format_argument_value(
                    "baseType",
                    kwargs.get("base_type", None),
                    style="form",
                    explode=False,
                ),
                "singleComponentIndicator": oapi.client.format_argument_value(
                    "singleComponentIndicator",
                    kwargs.get("single_component_indicator", None),
                    style="form",
                    explode=False,
                ),
                "flammabilityRating": oapi.client.format_argument_value(
                    "flammabilityRating",
                    kwargs.get("flammability_rating", None),
                    style="form",
                    explode=False,
                ),
                "hotmeltType": oapi.client.format_argument_value(
                    "hotmeltType",
                    kwargs.get("hotmelt_type", None),
                    style="form",
                    explode=False,
                ),
                "hydrolysisResistantIndicator": oapi.client.format_argument_value(  # noqa
                    "hydrolysisResistantIndicator",
                    kwargs.get("hydrolysis_resistant_indicator", None),
                    style="form",
                    explode=False,
                ),
                "methodOfMake": oapi.client.format_argument_value(
                    "methodOfMake",
                    kwargs.get("method_of_make", None),
                    style="form",
                    explode=False,
                ),
                "chemPolyForm": oapi.client.format_argument_value(
                    "chemPolyForm",
                    kwargs.get("chem_poly_form", None),
                    style="form",
                    explode=False,
                ),
                "filmType": oapi.client.format_argument_value(
                    "filmType",
                    kwargs.get("film_type", None),
                    style="form",
                    explode=False,
                ),
                "hotmeltMaterialItem": oapi.client.format_argument_value(
                    "hotmeltMaterialItem",
                    kwargs.get("hotmelt_material_item", None),
                    style="form",
                    explode=False,
                ),
                "hotmeltThicknessNumberMm": oapi.client.format_argument_value(
                    "hotmeltThicknessNumberMm",
                    kwargs.get("hotmelt_thickness_number_mm", None),
                    style="form",
                    explode=False,
                ),
                "opacity": oapi.client.format_argument_value(
                    "opacity",
                    kwargs.get("opacity", None),
                    style="form",
                    explode=False,
                ),
                "stretchIndicator": oapi.client.format_argument_value(
                    "stretchIndicator",
                    kwargs.get("stretch_indicator", None),
                    style="form",
                    explode=False,
                ),
                "foamType": oapi.client.format_argument_value(
                    "foamType",
                    kwargs.get("foam_type", None),
                    style="form",
                    explode=False,
                ),
                "polyurethaneChemistry": oapi.client.format_argument_value(
                    "polyurethaneChemistry",
                    kwargs.get("polyurethane_chemistry", None),
                    style="form",
                    explode=False,
                ),
                "hardnessAskerC": oapi.client.format_argument_value(
                    "hardnessAskerC",
                    kwargs.get("hardness_asker_c", None),
                    style="form",
                    explode=False,
                ),
                "firmness": oapi.client.format_argument_value(
                    "firmness",
                    kwargs.get("firmness", None),
                    style="form",
                    explode=False,
                ),
                "meltingPointNumber": oapi.client.format_argument_value(
                    "meltingPointNumber",
                    kwargs.get("melting_point_number", None),
                    style="form",
                    explode=False,
                ),
                "plasticType": oapi.client.format_argument_value(
                    "plasticType",
                    kwargs.get("plastic_type", None),
                    style="form",
                    explode=False,
                ),
                "plasticSubType": oapi.client.format_argument_value(
                    "plasticSubType",
                    kwargs.get("plastic_sub_type", None),
                    style="form",
                    explode=False,
                ),
                "ultravioletInhibitorIndicator": oapi.client.format_argument_value(  # noqa
                    "ultravioletInhibitorIndicator",
                    kwargs.get("ultraviolet_inhibitor_indicator", None),
                    style="form",
                    explode=False,
                ),
                "clearRubberIndicator": oapi.client.format_argument_value(
                    "clearRubberIndicator",
                    kwargs.get("clear_rubber_indicator", None),
                    style="form",
                    explode=False,
                ),
                "cureProcess": oapi.client.format_argument_value(
                    "cureProcess",
                    kwargs.get("cure_process", None),
                    style="form",
                    explode=False,
                ),
                "regrindContentPercentage": oapi.client.format_argument_value(
                    "regrindContentPercentage",
                    kwargs.get("regrind_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "sportActivity": oapi.client.format_argument_value(
                    "sportActivity",
                    kwargs.get("sport_activity", None),
                    style="form",
                    explode=False,
                ),
                "detachableMetalIndicator": oapi.client.format_argument_value(
                    "detachableMetalIndicator",
                    kwargs.get("detachable_metal_indicator", None),
                    style="form",
                    explode=False,
                ),
                "hardOrSoftComponent": oapi.client.format_argument_value(
                    "hardOrSoftComponent",
                    kwargs.get("hard_or_soft_component", None),
                    style="form",
                    explode=False,
                ),
                "stockOrCustom": oapi.client.format_argument_value(
                    "stockOrCustom",
                    kwargs.get("stock_or_custom", None),
                    style="form",
                    explode=False,
                ),
                "coreConstructionType": oapi.client.format_argument_value(
                    "coreConstructionType",
                    kwargs.get("core_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "componentConstructionType": oapi.client.format_argument_value(
                    "componentConstructionType",
                    kwargs.get("component_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "hasCoreIndicator": oapi.client.format_argument_value(
                    "hasCoreIndicator",
                    kwargs.get("has_core_indicator", None),
                    style="form",
                    explode=False,
                ),
                "shape": oapi.client.format_argument_value(
                    "shape",
                    kwargs.get("shape", None),
                    style="form",
                    explode=False,
                ),
                "logoType": oapi.client.format_argument_value(
                    "logoType",
                    kwargs.get("logo_type", None),
                    style="form",
                    explode=False,
                ),
                "logoName": oapi.client.format_argument_value(
                    "logoName",
                    kwargs.get("logo_name", None),
                    style="form",
                    explode=False,
                ),
                "logoPlacement": oapi.client.format_argument_value(
                    "logoPlacement",
                    kwargs.get("logo_placement", None),
                    style="form",
                    explode=False,
                ),
                "hotmeltIncludedIndicator": oapi.client.format_argument_value(
                    "hotmeltIncludedIndicator",
                    kwargs.get("hotmelt_included_indicator", None),
                    style="form",
                    explode=False,
                ),
                "elasticizedIndicator": oapi.client.format_argument_value(
                    "elasticizedIndicator",
                    kwargs.get("elasticized_indicator", None),
                    style="form",
                    explode=False,
                ),
                "vendorColorCardOnlyIndicator": oapi.client.format_argument_value(  # noqa
                    "vendorColorCardOnlyIndicator",
                    kwargs.get("vendor_color_card_only_indicator", None),
                    style="form",
                    explode=False,
                ),
                "componentForm": oapi.client.format_argument_value(
                    "componentForm",
                    kwargs.get("component_form", None),
                    style="form",
                    explode=False,
                ),
                "ligneSizeNumber": oapi.client.format_argument_value(
                    "ligneSizeNumber",
                    kwargs.get("ligne_size_number", None),
                    style="form",
                    explode=False,
                ),
                "numberOfHoles": oapi.client.format_argument_value(
                    "numberOfHoles",
                    kwargs.get("number_of_holes", None),
                    style="form",
                    explode=False,
                ),
                "adhesiveType": oapi.client.format_argument_value(
                    "adhesiveType",
                    kwargs.get("adhesive_type", None),
                    style="form",
                    explode=False,
                ),
                "gripperType": oapi.client.format_argument_value(
                    "gripperType",
                    kwargs.get("gripper_type", None),
                    style="form",
                    explode=False,
                ),
                "numberOfGripperRows": oapi.client.format_argument_value(
                    "numberOfGripperRows",
                    kwargs.get("number_of_gripper_rows", None),
                    style="form",
                    explode=False,
                ),
                "endFinish": oapi.client.format_argument_value(
                    "endFinish",
                    kwargs.get("end_finish", None),
                    style="form",
                    explode=False,
                ),
                "forProductSizes": oapi.client.format_argument_value(
                    "forProductSizes",
                    kwargs.get("for_product_sizes", None),
                    style="form",
                    explode=False,
                ),
                "partType": oapi.client.format_argument_value(
                    "partType",
                    kwargs.get("part_type", None),
                    style="form",
                    explode=False,
                ),
                "numberOfRows": oapi.client.format_argument_value(
                    "numberOfRows",
                    kwargs.get("number_of_rows", None),
                    style="form",
                    explode=False,
                ),
                "amountPerRow": oapi.client.format_argument_value(
                    "amountPerRow",
                    kwargs.get("amount_per_row", None),
                    style="form",
                    explode=False,
                ),
                "adjusterType": oapi.client.format_argument_value(
                    "adjusterType",
                    kwargs.get("adjuster_type", None),
                    style="form",
                    explode=False,
                ),
                "containsMagnetIndicator": oapi.client.format_argument_value(
                    "containsMagnetIndicator",
                    kwargs.get("contains_magnet_indicator", None),
                    style="form",
                    explode=False,
                ),
                "buttonType": oapi.client.format_argument_value(
                    "buttonType",
                    kwargs.get("button_type", None),
                    style="form",
                    explode=False,
                ),
                "tapeType": oapi.client.format_argument_value(
                    "tapeType",
                    kwargs.get("tape_type", None),
                    style="form",
                    explode=False,
                ),
                "snapType": oapi.client.format_argument_value(
                    "snapType",
                    kwargs.get("snap_type", None),
                    style="form",
                    explode=False,
                ),
                "snapPartType": oapi.client.format_argument_value(
                    "snapPartType",
                    kwargs.get("snap_part_type", None),
                    style="form",
                    explode=False,
                ),
                "tapeWidthMm": oapi.client.format_argument_value(
                    "tapeWidthMm",
                    kwargs.get("tape_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "snapWidthMm": oapi.client.format_argument_value(
                    "snapWidthMm",
                    kwargs.get("snap_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "snapRepeatLengthMm": oapi.client.format_argument_value(
                    "snapRepeatLengthMm",
                    kwargs.get("snap_repeat_length_mm", None),
                    style="form",
                    explode=False,
                ),
                "cordlockToggleType": oapi.client.format_argument_value(
                    "cordlockToggleType",
                    kwargs.get("cordlock_toggle_type", None),
                    style="form",
                    explode=False,
                ),
                "activationTemperatureNumber": oapi.client.format_argument_value(  # noqa
                    "activationTemperatureNumber",
                    kwargs.get("activation_temperature_number", None),
                    style="form",
                    explode=False,
                ),
                "counterType": oapi.client.format_argument_value(
                    "counterType",
                    kwargs.get("counter_type", None),
                    style="form",
                    explode=False,
                ),
                "dwellTime": oapi.client.format_argument_value(
                    "dwellTime",
                    kwargs.get("dwell_time", None),
                    style="form",
                    explode=False,
                ),
                "generalConstruction": oapi.client.format_argument_value(
                    "generalConstruction",
                    kwargs.get("general_construction", None),
                    style="form",
                    explode=False,
                ),
                "elasticType": oapi.client.format_argument_value(
                    "elasticType",
                    kwargs.get("elastic_type", None),
                    style="form",
                    explode=False,
                ),
                "crossoverDrawcordIndicator": oapi.client.format_argument_value(  # noqa
                    "crossoverDrawcordIndicator",
                    kwargs.get("crossover_drawcord_indicator", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordContentPercentage": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordContentPercentage",
                    kwargs.get("elastic_drawcord_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordContentType": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordContentType",
                    kwargs.get("elastic_drawcord_content_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordContentSource": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordContentSource",
                    kwargs.get("elastic_drawcord_content_source", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordAgletMaterialItem": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordAgletMaterialItem",
                    kwargs.get("elastic_drawcord_aglet_material_item", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordHasCoreIndicator": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordHasCoreIndicator",
                    kwargs.get("elastic_drawcord_has_core_indicator", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordElasticizedIndicator": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordElasticizedIndicator",
                    kwargs.get("elastic_drawcord_elasticized_indicator", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordShape": oapi.client.format_argument_value(
                    "elasticDrawcordShape",
                    kwargs.get("elastic_drawcord_shape", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordLogoName": oapi.client.format_argument_value(
                    "elasticDrawcordLogoName",
                    kwargs.get("elastic_drawcord_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordDimensionWidthIndicator": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordDimensionWidthIndicator",
                    kwargs.get("elastic_drawcord_dimension_width_indicator", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordGripperType": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordGripperType",
                    kwargs.get("elastic_drawcord_gripper_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordConstructionType": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordConstructionType",
                    kwargs.get("elastic_drawcord_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordForm": oapi.client.format_argument_value(
                    "elasticDrawcordForm",
                    kwargs.get("elastic_drawcord_form", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordEndFinish": oapi.client.format_argument_value(
                    "elasticDrawcordEndFinish",
                    kwargs.get("elastic_drawcord_end_finish", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordWidthMm": oapi.client.format_argument_value(
                    "elasticDrawcordWidthMm",
                    kwargs.get("elastic_drawcord_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordArtworkTechnique",
                    kwargs.get("elastic_drawcord_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordFinishProcess": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordFinishProcess",
                    kwargs.get("elastic_drawcord_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordDyeMethod": oapi.client.format_argument_value(
                    "elasticDrawcordDyeMethod",
                    kwargs.get("elastic_drawcord_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordVisualEffect": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordVisualEffect",
                    kwargs.get("elastic_drawcord_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordNumberOfColors": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordNumberOfColors",
                    kwargs.get("elastic_drawcord_number_of_colors", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletContentPercentage": oapi.client.format_argument_value(  # noqa
                    "elasticAgletContentPercentage",
                    kwargs.get("elastic_aglet_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletContentType": oapi.client.format_argument_value(
                    "elasticAgletContentType",
                    kwargs.get("elastic_aglet_content_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletContentSource": oapi.client.format_argument_value(
                    "elasticAgletContentSource",
                    kwargs.get("elastic_aglet_content_source", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletLogoName": oapi.client.format_argument_value(
                    "elasticAgletLogoName",
                    kwargs.get("elastic_aglet_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletShape": oapi.client.format_argument_value(
                    "elasticAgletShape",
                    kwargs.get("elastic_aglet_shape", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletConstructionType": oapi.client.format_argument_value(  # noqa
                    "elasticAgletConstructionType",
                    kwargs.get("elastic_aglet_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletWidthMm": oapi.client.format_argument_value(
                    "elasticAgletWidthMm",
                    kwargs.get("elastic_aglet_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletHeightMm": oapi.client.format_argument_value(
                    "elasticAgletHeightMm",
                    kwargs.get("elastic_aglet_height_mm", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletInternalDiameterMm": oapi.client.format_argument_value(  # noqa
                    "elasticAgletInternalDiameterMm",
                    kwargs.get("elastic_aglet_internal_diameter_mm", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletGramsPerThousandPieces": oapi.client.format_argument_value(  # noqa
                    "elasticAgletGramsPerThousandPieces",
                    kwargs.get("elastic_aglet_grams_per_thousand_pieces", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "elasticAgletFinishProcess": oapi.client.format_argument_value(
                    "elasticAgletFinishProcess",
                    kwargs.get("elastic_aglet_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletDyeMethod": oapi.client.format_argument_value(
                    "elasticAgletDyeMethod",
                    kwargs.get("elastic_aglet_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "elasticAgletArtworkTechnique",
                    kwargs.get("elastic_aglet_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletVisualEffect": oapi.client.format_argument_value(
                    "elasticAgletVisualEffect",
                    kwargs.get("elastic_aglet_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletNumberOfColors": oapi.client.format_argument_value(  # noqa
                    "elasticAgletNumberOfColors",
                    kwargs.get("elastic_aglet_number_of_colors", None),
                    style="form",
                    explode=False,
                ),
                "drawcordMaterialItem": oapi.client.format_argument_value(
                    "drawcordMaterialItem",
                    kwargs.get("drawcord_material_item", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletMaterialItem": oapi.client.format_argument_value(
                    "drawcordAgletMaterialItem",
                    kwargs.get("drawcord_aglet_material_item", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletContentPercentage": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletContentPercentage",
                    kwargs.get("drawcord_aglet_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletContentType": oapi.client.format_argument_value(
                    "drawcordAgletContentType",
                    kwargs.get("drawcord_aglet_content_type", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletContentSource": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletContentSource",
                    kwargs.get("drawcord_aglet_content_source", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletLogoName": oapi.client.format_argument_value(
                    "drawcordAgletLogoName",
                    kwargs.get("drawcord_aglet_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletShape": oapi.client.format_argument_value(
                    "drawcordAgletShape",
                    kwargs.get("drawcord_aglet_shape", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletConstructionType": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletConstructionType",
                    kwargs.get("drawcord_aglet_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletWidthMm": oapi.client.format_argument_value(
                    "drawcordAgletWidthMm",
                    kwargs.get("drawcord_aglet_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletHeightMm": oapi.client.format_argument_value(
                    "drawcordAgletHeightMm",
                    kwargs.get("drawcord_aglet_height_mm", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletInternalDiameterMm": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletInternalDiameterMm",
                    kwargs.get("drawcord_aglet_internal_diameter_mm", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletGramsPerThousandPieces": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletGramsPerThousandPieces",
                    kwargs.get("drawcord_aglet_grams_per_thousand_pieces", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "drawcordAgletFinishProcess": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletFinishProcess",
                    kwargs.get("drawcord_aglet_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletDyeMethod": oapi.client.format_argument_value(
                    "drawcordAgletDyeMethod",
                    kwargs.get("drawcord_aglet_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletArtworkTechnique",
                    kwargs.get("drawcord_aglet_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletVisualEffect": oapi.client.format_argument_value(
                    "drawcordAgletVisualEffect",
                    kwargs.get("drawcord_aglet_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletNumberOfColors": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletNumberOfColors",
                    kwargs.get("drawcord_aglet_number_of_colors", None),
                    style="form",
                    explode=False,
                ),
                "hookType": oapi.client.format_argument_value(
                    "hookType",
                    kwargs.get("hook_type", None),
                    style="form",
                    explode=False,
                ),
                "hookLoopType": oapi.client.format_argument_value(
                    "hookLoopType",
                    kwargs.get("hook_loop_type", None),
                    style="form",
                    explode=False,
                ),
                "labelType": oapi.client.format_argument_value(
                    "labelType",
                    kwargs.get("label_type", None),
                    style="form",
                    explode=False,
                ),
                "foldMethod": oapi.client.format_argument_value(
                    "foldMethod",
                    kwargs.get("fold_method", None),
                    style="form",
                    explode=False,
                ),
                "labelTwillDirection": oapi.client.format_argument_value(
                    "labelTwillDirection",
                    kwargs.get("label_twill_direction", None),
                    style="form",
                    explode=False,
                ),
                "backingType": oapi.client.format_argument_value(
                    "backingType",
                    kwargs.get("backing_type", None),
                    style="form",
                    explode=False,
                ),
                "logoSize": oapi.client.format_argument_value(
                    "logoSize",
                    kwargs.get("logo_size", None),
                    style="form",
                    explode=False,
                ),
                "agletMaterialItem": oapi.client.format_argument_value(
                    "agletMaterialItem",
                    kwargs.get("aglet_material_item", None),
                    style="form",
                    explode=False,
                ),
                "hasAgletIndicator": oapi.client.format_argument_value(
                    "hasAgletIndicator",
                    kwargs.get("has_aglet_indicator", None),
                    style="form",
                    explode=False,
                ),
                "numberOfBundles": oapi.client.format_argument_value(
                    "numberOfBundles",
                    kwargs.get("number_of_bundles", None),
                    style="form",
                    explode=False,
                ),
                "tipContent": oapi.client.format_argument_value(
                    "tipContent",
                    kwargs.get("tip_content", None),
                    style="form",
                    explode=False,
                ),
                "tipType": oapi.client.format_argument_value(
                    "tipType",
                    kwargs.get("tip_type", None),
                    style="form",
                    explode=False,
                ),
                "magnetCoverType": oapi.client.format_argument_value(
                    "magnetCoverType",
                    kwargs.get("magnet_cover_type", None),
                    style="form",
                    explode=False,
                ),
                "paddingType": oapi.client.format_argument_value(
                    "paddingType",
                    kwargs.get("padding_type", None),
                    style="form",
                    explode=False,
                ),
                "paddingOrientation": oapi.client.format_argument_value(
                    "paddingOrientation",
                    kwargs.get("padding_orientation", None),
                    style="form",
                    explode=False,
                ),
                "layerLocation": oapi.client.format_argument_value(
                    "layerLocation",
                    kwargs.get("layer_location", None),
                    style="form",
                    explode=False,
                ),
                "materialConstruction": oapi.client.format_argument_value(
                    "materialConstruction",
                    kwargs.get("material_construction", None),
                    style="form",
                    explode=False,
                ),
                "layerFinishProcess": oapi.client.format_argument_value(
                    "layerFinishProcess",
                    kwargs.get("layer_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "layerArtworkTechnique": oapi.client.format_argument_value(
                    "layerArtworkTechnique",
                    kwargs.get("layer_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "layerContentPercentage": oapi.client.format_argument_value(
                    "layerContentPercentage",
                    kwargs.get("layer_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "layerContentType": oapi.client.format_argument_value(
                    "layerContentType",
                    kwargs.get("layer_content_type", None),
                    style="form",
                    explode=False,
                ),
                "layerContentSource": oapi.client.format_argument_value(
                    "layerContentSource",
                    kwargs.get("layer_content_source", None),
                    style="form",
                    explode=False,
                ),
                "pinBadgeType": oapi.client.format_argument_value(
                    "pinBadgeType",
                    kwargs.get("pin_badge_type", None),
                    style="form",
                    explode=False,
                ),
                "plateOrientation": oapi.client.format_argument_value(
                    "plateOrientation",
                    kwargs.get("plate_orientation", None),
                    style="form",
                    explode=False,
                ),
                "ringType": oapi.client.format_argument_value(
                    "ringType",
                    kwargs.get("ring_type", None),
                    style="form",
                    explode=False,
                ),
                "bondedIndicator": oapi.client.format_argument_value(
                    "bondedIndicator",
                    kwargs.get("bonded_indicator", None),
                    style="form",
                    explode=False,
                ),
                "lubricatedIndicator": oapi.client.format_argument_value(
                    "lubricatedIndicator",
                    kwargs.get("lubricated_indicator", None),
                    style="form",
                    explode=False,
                ),
                "threadPly": oapi.client.format_argument_value(
                    "threadPly",
                    kwargs.get("thread_ply", None),
                    style="form",
                    explode=False,
                ),
                "threadSize": oapi.client.format_argument_value(
                    "threadSize",
                    kwargs.get("thread_size", None),
                    style="form",
                    explode=False,
                ),
                "alternateThreadSize": oapi.client.format_argument_value(
                    "alternateThreadSize",
                    kwargs.get("alternate_thread_size", None),
                    style="form",
                    explode=False,
                ),
                "threadType": oapi.client.format_argument_value(
                    "threadType",
                    kwargs.get("thread_type", None),
                    style="form",
                    explode=False,
                ),
                "threadBrandName": oapi.client.format_argument_value(
                    "threadBrandName",
                    kwargs.get("thread_brand_name", None),
                    style="form",
                    explode=False,
                ),
                "threadNumberSystem": oapi.client.format_argument_value(
                    "threadNumberSystem",
                    kwargs.get("thread_number_system", None),
                    style="form",
                    explode=False,
                ),
                "threadPreparation": oapi.client.format_argument_value(
                    "threadPreparation",
                    kwargs.get("thread_preparation", None),
                    style="form",
                    explode=False,
                ),
                "threadFilamentCount": oapi.client.format_argument_value(
                    "threadFilamentCount",
                    kwargs.get("thread_filament_count", None),
                    style="form",
                    explode=False,
                ),
                "threadPlyCount": oapi.client.format_argument_value(
                    "threadPlyCount",
                    kwargs.get("thread_ply_count", None),
                    style="form",
                    explode=False,
                ),
                "threadLuster": oapi.client.format_argument_value(
                    "threadLuster",
                    kwargs.get("thread_luster", None),
                    style="form",
                    explode=False,
                ),
                "threadStatementContent": oapi.client.format_argument_value(
                    "threadStatementContent",
                    kwargs.get("thread_statement_content", None),
                    style="form",
                    explode=False,
                ),
                "zipperType": oapi.client.format_argument_value(
                    "zipperType",
                    kwargs.get("zipper_type", None),
                    style="form",
                    explode=False,
                ),
                "zipInCompatibleIndicator": oapi.client.format_argument_value(
                    "zipInCompatibleIndicator",
                    kwargs.get("zip_in_compatible_indicator", None),
                    style="form",
                    explode=False,
                ),
                "zipperPerformance": oapi.client.format_argument_value(
                    "zipperPerformance",
                    kwargs.get("zipper_performance", None),
                    style="form",
                    explode=False,
                ),
                "sliderPullLogoName": oapi.client.format_argument_value(
                    "sliderPullLogoName",
                    kwargs.get("slider_pull_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "sliderLockingFunction": oapi.client.format_argument_value(
                    "sliderLockingFunction",
                    kwargs.get("slider_locking_function", None),
                    style="form",
                    explode=False,
                ),
                "sliderQuantity": oapi.client.format_argument_value(
                    "sliderQuantity",
                    kwargs.get("slider_quantity", None),
                    style="form",
                    explode=False,
                ),
                "sliderOrientation": oapi.client.format_argument_value(
                    "sliderOrientation",
                    kwargs.get("slider_orientation", None),
                    style="form",
                    explode=False,
                ),
                "sliderSize": oapi.client.format_argument_value(
                    "sliderSize",
                    kwargs.get("slider_size", None),
                    style="form",
                    explode=False,
                ),
                "intendedUseOn": oapi.client.format_argument_value(
                    "intendedUseOn",
                    kwargs.get("intended_use_on", None),
                    style="form",
                    explode=False,
                ),
                "forBallTypeAndSize": oapi.client.format_argument_value(
                    "forBallTypeAndSize",
                    kwargs.get("for_ball_type_and_size", None),
                    style="form",
                    explode=False,
                ),
                "initialPressure": oapi.client.format_argument_value(
                    "initialPressure",
                    kwargs.get("initial_pressure", None),
                    style="form",
                    explode=False,
                ),
                "sliderVisualEffect": oapi.client.format_argument_value(
                    "sliderVisualEffect",
                    kwargs.get("slider_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "sliderPullFinishProcess": oapi.client.format_argument_value(
                    "sliderPullFinishProcess",
                    kwargs.get("slider_pull_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "sliderPullArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "sliderPullArtworkTechnique",
                    kwargs.get("slider_pull_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "zipperPullCode": oapi.client.format_argument_value(
                    "zipperPullCode",
                    kwargs.get("zipper_pull_code", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeConstructionType": oapi.client.format_argument_value(  # noqa
                    "zipperTapeConstructionType",
                    kwargs.get("zipper_tape_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeLogoName": oapi.client.format_argument_value(
                    "zipperTapeLogoName",
                    kwargs.get("zipper_tape_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeWidthMm": oapi.client.format_argument_value(
                    "zipperTapeWidthMm",
                    kwargs.get("zipper_tape_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeFinishProcess": oapi.client.format_argument_value(
                    "zipperTapeFinishProcess",
                    kwargs.get("zipper_tape_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeDyeMethod": oapi.client.format_argument_value(
                    "zipperTapeDyeMethod",
                    kwargs.get("zipper_tape_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "zipperTapeArtworkTechnique",
                    kwargs.get("zipper_tape_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeArtworkGraphic": oapi.client.format_argument_value(
                    "zipperTapeArtworkGraphic",
                    kwargs.get("zipper_tape_artwork_graphic", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeVisualEffect": oapi.client.format_argument_value(
                    "zipperTapeVisualEffect",
                    kwargs.get("zipper_tape_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "teethType": oapi.client.format_argument_value(
                    "teethType",
                    kwargs.get("teeth_type", None),
                    style="form",
                    explode=False,
                ),
                "specialZipperTeethOrientation": oapi.client.format_argument_value(  # noqa
                    "specialZipperTeethOrientation",
                    kwargs.get("special_zipper_teeth_orientation", None),
                    style="form",
                    explode=False,
                ),
                "teethSize": oapi.client.format_argument_value(
                    "teethSize",
                    kwargs.get("teeth_size", None),
                    style="form",
                    explode=False,
                ),
                "teethShape": oapi.client.format_argument_value(
                    "teethShape",
                    kwargs.get("teeth_shape", None),
                    style="form",
                    explode=False,
                ),
                "teethRepeatLengthMm": oapi.client.format_argument_value(
                    "teethRepeatLengthMm",
                    kwargs.get("teeth_repeat_length_mm", None),
                    style="form",
                    explode=False,
                ),
                "teethFinishProcess": oapi.client.format_argument_value(
                    "teethFinishProcess",
                    kwargs.get("teeth_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "teethArtworkTechnique": oapi.client.format_argument_value(
                    "teethArtworkTechnique",
                    kwargs.get("teeth_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "teethVisualEffect": oapi.client.format_argument_value(
                    "teethVisualEffect",
                    kwargs.get("teeth_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "contrastThreadForCoilIndicator": oapi.client.format_argument_value(  # noqa
                    "contrastThreadForCoilIndicator",
                    kwargs.get("contrast_thread_for_coil_indicator", None),
                    style="form",
                    explode=False,
                ),
                "teethMultiColoredIndicator": oapi.client.format_argument_value(  # noqa
                    "teethMultiColoredIndicator",
                    kwargs.get("teeth_multi_colored_indicator", None),
                    style="form",
                    explode=False,
                ),
                "zipperStopType": oapi.client.format_argument_value(
                    "zipperStopType",
                    kwargs.get("zipper_stop_type", None),
                    style="form",
                    explode=False,
                ),
                "zipperStopLogoName": oapi.client.format_argument_value(
                    "zipperStopLogoName",
                    kwargs.get("zipper_stop_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "zipperStopLogoPlacement": oapi.client.format_argument_value(
                    "zipperStopLogoPlacement",
                    kwargs.get("zipper_stop_logo_placement", None),
                    style="form",
                    explode=False,
                ),
                "agletConstructionType": oapi.client.format_argument_value(
                    "agletConstructionType",
                    kwargs.get("aglet_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "airbagProcess": oapi.client.format_argument_value(
                    "airbagProcess",
                    kwargs.get("airbag_process", None),
                    style="form",
                    explode=False,
                ),
                "airbagType": oapi.client.format_argument_value(
                    "airbagType",
                    kwargs.get("airbag_type", None),
                    style="form",
                    explode=False,
                ),
                "colorationAvailable": oapi.client.format_argument_value(
                    "colorationAvailable",
                    kwargs.get("coloration_available", None),
                    style="form",
                    explode=False,
                ),
                "gasContent": oapi.client.format_argument_value(
                    "gasContent",
                    kwargs.get("gas_content", None),
                    style="form",
                    explode=False,
                ),
                "fillType": oapi.client.format_argument_value(
                    "fillType",
                    kwargs.get("fill_type", None),
                    style="form",
                    explode=False,
                ),
                "scrim": oapi.client.format_argument_value(
                    "scrim",
                    kwargs.get("scrim", None),
                    style="form",
                    explode=False,
                ),
                "downClusterStatement": oapi.client.format_argument_value(
                    "downClusterStatement",
                    kwargs.get("down_cluster_statement", None),
                    style="form",
                    explode=False,
                ),
                "fillPower": oapi.client.format_argument_value(
                    "fillPower",
                    kwargs.get("fill_power", None),
                    style="form",
                    explode=False,
                ),
                "naturalDownColor": oapi.client.format_argument_value(
                    "naturalDownColor",
                    kwargs.get("natural_down_color", None),
                    style="form",
                    explode=False,
                ),
                "fillForm": oapi.client.format_argument_value(
                    "fillForm",
                    kwargs.get("fill_form", None),
                    style="form",
                    explode=False,
                ),
                "heatSet": oapi.client.format_argument_value(
                    "heatSet",
                    kwargs.get("heat_set", None),
                    style="form",
                    explode=False,
                ),
                "vendorSuppliedIndicator": oapi.client.format_argument_value(
                    "vendorSuppliedIndicator",
                    kwargs.get("vendor_supplied_indicator", None),
                    style="form",
                    explode=False,
                ),
                "corporateDesignationIndicator": oapi.client.format_argument_value(  # noqa
                    "corporateDesignationIndicator",
                    kwargs.get("corporate_designation_indicator", None),
                    style="form",
                    explode=False,
                ),
                "confidentialIndicator": oapi.client.format_argument_value(
                    "confidentialIndicator",
                    kwargs.get("confidential_indicator", None),
                    style="form",
                    explode=False,
                ),
                "countryOfOriginStatementIndicator": oapi.client.format_argument_value(  # noqa
                    "countryOfOriginStatementIndicator",
                    kwargs.get("country_of_origin_statement_indicator", None),
                    style="form",
                    explode=False,
                ),
                "sizeMatrixIndicator": oapi.client.format_argument_value(
                    "sizeMatrixIndicator",
                    kwargs.get("size_matrix_indicator", None),
                    style="form",
                    explode=False,
                ),
                "containsCorporateLogoIndicator": oapi.client.format_argument_value(  # noqa
                    "containsCorporateLogoIndicator",
                    kwargs.get("contains_corporate_logo_indicator", None),
                    style="form",
                    explode=False,
                ),
                "navIndicator": oapi.client.format_argument_value(
                    "navIndicator",
                    kwargs.get("nav_indicator", None),
                    style="form",
                    explode=False,
                ),
                "packagingIntent": oapi.client.format_argument_value(
                    "packagingIntent",
                    kwargs.get("packaging_intent", None),
                    style="form",
                    explode=False,
                ),
                "packagingStatement": oapi.client.format_argument_value(
                    "packagingStatement",
                    kwargs.get("packaging_statement", None),
                    style="form",
                    explode=False,
                ),
                "cardType": oapi.client.format_argument_value(
                    "cardType",
                    kwargs.get("card_type", None),
                    style="form",
                    explode=False,
                ),
                "cardConstructionType": oapi.client.format_argument_value(
                    "cardConstructionType",
                    kwargs.get("card_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "flutingSize": oapi.client.format_argument_value(
                    "flutingSize",
                    kwargs.get("fluting_size", None),
                    style="form",
                    explode=False,
                ),
                "innerLinerboardBasisWeight": oapi.client.format_argument_value(  # noqa
                    "innerLinerboardBasisWeight",
                    kwargs.get("inner_linerboard_basis_weight", None),
                    style="form",
                    explode=False,
                ),
                "innerLinerboardType": oapi.client.format_argument_value(
                    "innerLinerboardType",
                    kwargs.get("inner_linerboard_type", None),
                    style="form",
                    explode=False,
                ),
                "mediumPaperBasisWeight": oapi.client.format_argument_value(
                    "mediumPaperBasisWeight",
                    kwargs.get("medium_paper_basis_weight", None),
                    style="form",
                    explode=False,
                ),
                "mediumPaperType": oapi.client.format_argument_value(
                    "mediumPaperType",
                    kwargs.get("medium_paper_type", None),
                    style="form",
                    explode=False,
                ),
                "outerLinerboardBasisWeight": oapi.client.format_argument_value(  # noqa
                    "outerLinerboardBasisWeight",
                    kwargs.get("outer_linerboard_basis_weight", None),
                    style="form",
                    explode=False,
                ),
                "outerLinerboardType": oapi.client.format_argument_value(
                    "outerLinerboardType",
                    kwargs.get("outer_linerboard_type", None),
                    style="form",
                    explode=False,
                ),
                "fastenerType": oapi.client.format_argument_value(
                    "fastenerType",
                    kwargs.get("fastener_type", None),
                    style="form",
                    explode=False,
                ),
                "hangerType": oapi.client.format_argument_value(
                    "hangerType",
                    kwargs.get("hanger_type", None),
                    style="form",
                    explode=False,
                ),
                "hangtagType": oapi.client.format_argument_value(
                    "hangtagType",
                    kwargs.get("hangtag_type", None),
                    style="form",
                    explode=False,
                ),
                "partitionType": oapi.client.format_argument_value(
                    "partitionType",
                    kwargs.get("partition_type", None),
                    style="form",
                    explode=False,
                ),
                "shoebagType": oapi.client.format_argument_value(
                    "shoebagType",
                    kwargs.get("shoebag_type", None),
                    style="form",
                    explode=False,
                ),
                "shoeFormType": oapi.client.format_argument_value(
                    "shoeFormType",
                    kwargs.get("shoe_form_type", None),
                    style="form",
                    explode=False,
                ),
                "stickerType": oapi.client.format_argument_value(
                    "stickerType",
                    kwargs.get("sticker_type", None),
                    style="form",
                    explode=False,
                ),
                "tissueType": oapi.client.format_argument_value(
                    "tissueType",
                    kwargs.get("tissue_type", None),
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SearchResponse,
            )
        )

    def get_material_management_data_material_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.MaterialTypeResponse:
        """
        How you get a single material type resource

        Parameters:

        - object_id:
          The key associated with of the material type object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialTypes/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.MaterialTypeResponse,
            )
        )

    def get_material_management_data_material_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.MaterialTypeBulkResponse:
        """
        How you get all the material types data

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialTypes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.MaterialTypeBulkResponse,
            )
        )

    def get_material_management_data_supplied_materials_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.MaterialManagementDataSuppliedMaterialsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SuppliedMaterialResponse:
        """
        How you get a single supplied material.

        Parameters:

        - object_id:
          A single Id of the object (in this case  Supplied Material)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/suppliedMaterials/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SuppliedMaterialResponse,
            )
        )

    def get_material_management_search_supplied_materials(
        self,
        **kwargs: typing.Any,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the supplied
        material entity

        Parameters:

        - count:
          Number of entries the API should attempt to fetch, default is 10
        - offset:
          Offset of the entries the API should attempt to fetch, default is 0
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        - q:
          This parameter is how you pass free text search, if any string is
          passed here it will be searched as free text
        - material:
          The reference key associated with this item: Material Identifier
        - supplier_location:
          The reference key associated with this item: Supplier Location
          Identifier
        - supplier_material_number
        - supplied_material_description
        - supplied_material_item_name
        - supplemental_material_name
        - material_name_variation_weight
        - material_name_variation_visual
        - manufacturing_countryof_origin:
          The reference key associated with this item: Manufacturing Country Of
          Origin
        - development_team:
          Material Level Development Team
        - retirement_reason_code:
          Material Level Reason Retirement Code
        - initial_season_cycle_year:
          The reference key associated with this item: Supplied Material
          Initial Season
        - target_season_cycle_year:
          The reference key associated with this item: Supplied Material Target
          Season
        - legacy_created_date
        - legacy_supplied_material_number
        - material_content_specification_number
        - supplied_material_state:
          The reference key associated with this item: Supplied Material State
          Identifier
        - supplied_material_status_indicator
        - material_library_locator_code
        - division:
          The reference key associated with this item: Supplied Material
          Division Code
        - supplied_material_development_team:
          The reference key associated with this item:
          suppliedMaterialDevelopmentTeam
        - physical_sample_available_indicator
        - physical_sample_date_added
        - pps_item_number
        - pps_submit_number
        - cross_approval_supplied_material:
          The reference key associated with this item: Cross Approval Supplied
          Material
        - approved_vendor_article_number
        - buy_ready_approver
        - buy_ready_date
        - expiration_date
        - duty_and_compliance:
          The reference key associated with this item: Duty and Compliance
        - primary_supplied_material_indicator
        - expiration_season_cycle_year:
          The reference key associated with this item: Expiration Season Year
        - cuttable_length_number
        - cuttable_length_uom:
          The reference key associated with this item: Supplied Material
          Cuttable Length UOM
        - cuttable_width_number
        - cuttable_width_uom:
          The reference key associated with this item: Supplied Material
          Cuttable Width UOM
        - material_length_number
        - material_length_uom:
          The reference key associated with this item: Supplied Material Length
          UOM
        - material_width_number
        - material_width_uom:
          The reference key associated with this item: Supplied Material Width
          UOM
        - initial_price:
          The number (float) for initialPrice
        - initial_price_uom:
          The reference key associated with this item: Initial Price UOM
        - patent
        - supplied_material_color_identifier
        - supplied_material_color_graphic_description
        - supplied_material_team_player_graphic_identifier
        - team_player_graphic_identifier
        - color:
          The reference key associated with this item: Supplied Material Color
          Identifier - Link to CM
        - supplied_material_color_graphic_primary_color:
          The reference key associated with this item: Supplied Material
          Primary Color Identifier - Link to CM
        - supplied_material_color_graphic_hue_identifier:
          The reference key associated with this item: Supplied Material
          Primary Hue Identifier
        - supplied_material_multi_color_code
        - supplied_material_color_is_multiple_colors
        - supplied_material_color_graphic_initial_cycle_year:
          The reference key associated with this item: Supplied Material Color
          Initial Season
        - supplied_material_color_graphic_status_indicator
        - supplied_material_color_graphic_state_identifier:
          The reference key associated with this item: Supplied Material Color
          State Identifier
        - create_timestamp:
          The reference key associated with this item: Supplied Material
          Created Timestamp
        - change_timestamp:
          The reference key associated with this item: Supplied Material Change
          Timestamp
        - parent_material_item_identifier:
          The reference key associated with this item: Material Level
          parentMaterialItemIdentifier
        - material_type:
          The reference key associated with this item: Material Type
        - material_item_name
        - customs_description:
          The reference key associated with this item: Material Level Customs
          Description
        - core_material_name_variation_weight:
          Material Level Material Name Variation Weight
        - core_material_name_variation_visual:
          Material Level Material Name Variation Visual
        - target_price
        - target_price_uom:
          The reference key associated with this item: Material Level Target
          Price UOM
        - material_color_control_mode:
          The reference key associated with this item: Material Level Color
          Control Mode
        - material_pricing_mode:
          The reference key associated with this item: Material Level Pricing
          Mode
        - legacy_created_on_date:
          The reference key associated with this item: legacyCreatedOnDate
        - legacy_material_number:
          The reference key associated with this item: legacyMaterialNumber
        - apparel_pdm_material_number:
          The reference key associated with this item: apparelPDMMaterialNumber
        - material_development_team:
          The reference key associated with this item: Material Level
          Development Team
        - material_initial_category:
          The reference key associated with this item: Material Level Initial
          Category
        - material_initial_cycle_year:
          The reference key associated with this item: Material Level Initial
          Season
        - material_target_cycle_year:
          The reference key associated with this item: Material Level Target
          Season
        - material_item_status_indicator:
          The true or false flag associated with this item:
          materialItemStatusIndicator
        - material_bom_indicator:
          The true or false flag associated with this item:
          materialBOMIndicator
        - core_material_content_percentage:
          The number (float) for Material Level Content Percentage
        - core_material_content_type:
          The reference key associated with this item: Material Level Content
          Type
        - core_material_content_source:
          The reference key associated with this item: Material Level Content
          Source
        - core_material_family:
          The reference key associated with this item: Material Level Family
        - material_content_percentage:
          The number (float) for materialContentPercentage
        - material_content_type:
          The reference key associated with this item: materialContentType
        - material_content_source:
          The reference key associated with this item: materialContentSource
        - material_label_content_percentage:
          The number (float) for materialLabelContentPercentage
        - material_label_content_type:
          The reference key associated with this item: materialLabelContentType
        - material_label_content_source:
          The reference key associated with this item:
          materialLabelContentSource
        - material_family:
          The reference key associated with this item: materialFamily
        - material_owner:
          The reference key associated with this item: materialOwner
        - artwork_graphic:
          The reference key associated with this item: artworkGraphic
        - artwork_technique:
          The reference key associated with this item: artworkTechnique
        - secondary_process_indicator:
          The true or false flag associated with this item:
          secondaryProcessIndicator
        - artwork_application_location:
          The reference key associated with this item:
          artworkApplicationLocation
        - artwork_repeat_length_cm:
          The number (float) for artworkRepeatLengthCm
        - directional_pattern_indicator:
          The true or false flag associated with this item:
          directionalPatternIndicator
        - garment_location_placement:
          The value associated with this item: garmentLocationPlacement
        - end_use:
          The reference key associated with this item: endUse
        - development_reason:
          The reference key associated with this item: developmentReason
        - material_benefits:
          The reference key associated with this item: materialBenefits
        - fabric_face_designation:
          The reference key associated with this item: fabricFaceDesignation
        - stretch_direction:
          The reference key associated with this item: stretchDirection
        - vendor_special_care_instructions:
          The reference key associated with this item:
          vendorSpecialCareInstructions
        - consideration_and_risks:
          The reference key associated with this item: considerationAndRisks
        - thickness_mm:
          The number (float) for thicknessMm
        - thickness_selection:
          The reference key associated with this item: thicknessSelection
        - maximum_thickness_mm:
          The number (float) for maximumThicknessMm
        - minimum_thickness_mm:
          The number (float) for maximumThicknessMm
        - length_mm:
          The number (float) for lengthMm
        - length_cm:
          The number (float) for lengthCm
        - dimension_width_indicator:
          The reference key associated with this item: dimensionWidthIndicator
        - width_mm:
          The number (float) for widthMm
        - width_cm:
          The number (float) for widthCm
        - height_mm:
          The number (float) for heightMm
        - height_cm:
          The number (float) for heightCm
        - weight_grams_per_square_meter:
          The number (float) for weightGramsPerSquareMeter
        - external_diameter_mm:
          The number (float) for externalDiameterMm
        - external_length_mm:
          The number (float) for externalLengthMm
        - external_width_mm:
          The number (float) for externalWidthMm
        - internal_diameter_mm:
          The number (float) for internalDiameterMm
        - internal_length_mm:
          The number (float) for internalLengthMm
        - internal_width_mm:
          The number (float) for internalWidthMm
        - gauge_inch:
          The number (float) for gaugeInch
        - grams_per_thousand_pieces:
          The number (float) for gramsPerThousandPieces
        - weight_grams_per_thousand_pieces:
          Weight (grams per 1000 pieces)
        - weight_grams_per_linear_yard:
          Weight (grams per linear yard)
        - weight_grams_per_linear_meter:
          Weight (grams per linear meter)
        - yarn_composition_content_percentage:
          The number (float) for yarnCompositionContentPercentage
        - yarn_composition_content_type:
          The reference key associated with this item:
          yarnCompositionContentType
        - yarn_composition_content_source:
          The reference key associated with this item:
          yarnCompositionContentSource
        - yarn_composition_location:
          The reference key associated with this item: yarnCompositionLocation
        - yarn_composition_type:
          The reference key associated with this item: yarnCompositionType
        - yarn_composition_size:
          The number (float) for yarnCompositionSize
        - yarn_composition_spinning_method:
          The reference key associated with this item:
          yarnCompositionSpinningMethod
        - yarn_composition_count:
          The The number (integer) for yarnCompositionCount
        - yarn_composition_preparation:
          The reference key associated with this item:
          yarnCompositionPreparation
        - yarn_composition_cross_section:
          The reference key associated with this item:
          yarnCompositionCrossSection
        - yarn_composition_filament_count:
          The number (integer) for yarnCompositionFilamentCount
        - yarn_composition_number_system:
          The reference key associated with this item:
          yarnCompositionNumberSystem
        - yarn_composition_luster:
          The reference key associated with this item: yarnCompositionLuster
        - yarn_composition_brand:
          The reference key associated with this item: yarnCompositionBrand
        - yarn_composition_texture:
          The reference key associated with this item: yarnCompositionTexture
        - yarn_composition_twist:
          The reference key associated with this item: yarnCompositionTwist
        - yarn_composition_finish_process:
          The reference key associated with this item:
          yarnCompositionFinishProcess
        - yarn_composition_dye_method:
          The reference key associated with this item: yarnCompositionDyeMethod
        - yarn_composition_visual_effect:
          The reference key associated with this item:
          yarnCompositionVisualEffect
        - yarn_composition_fixed_color:
          The reference key associated with this item:
          yarnCompositionFixedColor
        - yarn_composition_usage_percentage:
          The number (float) for yarnCompositionUsagePercentage
        - ply_content_percentage:
          The number (float) for plyContentPercentage
        - ply_content_type:
          The reference key associated with this item: plyContentType
        - ply_content_source:
          The reference key associated with this item: plyContentSource
        - ply_location:
          The reference key associated with this item: plyLocation
        - ply_type:
          The reference key associated with this item: plyType
        - ply_brand:
          The reference key associated with this item: plyBrand
        - ply_size:
          The number (float) for plySize
        - ply_number_system:
          The reference key associated with this item: plyNumberSystem
        - ply_cross_section:
          The reference key associated with this item: plyCrossSection
        - ply_spinning_method:
          The reference key associated with this item: plySpinningMethod
        - ply_filament_count:
          The number (integer) for plyFilamentCount
        - ply_twist:
          The reference key associated with this item: plyTwist
        - ply_luster:
          The reference key associated with this item: plyLuster
        - ply_texture:
          The reference key associated with this item: plyTexture
        - ply_finish_process:
          The reference key associated with this item: plyFinishProcess
        - ply_dye_method:
          The reference key associated with this item: plyDyeMethod
        - ply_visual_effect:
          The reference key associated with this item: plyVisualEffect
        - ply_fixed_color:
          The reference key associated with this item: plyFixedColor
        - ply_usage_percentage:
          The number (float) for plyUsagePercentage
        - fiber_content_percentage:
          The number (float) for fiberContentPercentage
        - fiber_content_type:
          The reference key associated with this item: fiberContentType
        - fiber_content_source:
          The reference key associated with this item: fiberContentSource
        - fiber_size:
          The number (float) for fiberSize
        - fiber_ply_location:
          The reference key associated with this item: fiberPlyLocation
        - fiber_staple_number_system:
          The reference key associated with this item: fiberStapleNumberSystem
        - fiber_staple_length:
          The number (float) for fiberStapleLength
        - fiber_staple_length_min:
          The number (float) for fiberStapleLengthMin
        - fiber_staple_length_max:
          The number (float) for fiberStapleLengthMax
        - fiber_diameter:
          The number (float) for fiberDiameter
        - fiber_diameter_min:
          The number (float) for fiberDiameterMin
        - fiber_diameter_max:
          The number (float) for fiberDiameterMax
        - fiber_diameter_unit:
          The reference key associated with this item: fiberDiameterUnit
        - fiber_preparation:
          The reference key associated with this item: fiberPreparation
        - fiber_cross_section:
          The reference key associated with this item: fiberCrossSection
        - fiber_luster:
          The reference key associated with this item: fiberLuster
        - fiber_finish_process:
          The reference key associated with this item: fiberFinishProcess
        - fiber_dye_method:
          The reference key associated with this item: fiberDyeMethod
        - fiber_usage_percentage:
          The number (float) for fiberUsagePercentage
        - edge_finish:
          The reference key associated with this item: edgeFinish
        - visual_effect:
          The reference key associated with this item: visualEffect
        - visual_effect_location:
          The reference key associated with this item: visualEffectLocation
        - print_code:
          The reference key associated with this item: printCode
        - emboss_code_text:
          Emboss Code Text
        - application_technique:
          The reference key associated with this item: applicationTechnique
        - finish_process:
          The reference key associated with this item: finishProcess
        - finish_location:
          The reference key associated with this item: finishLocation
        - number_of_passes:
          The number (integer) for numberOfPasses
        - material_technologies:
          The reference key associated with this item: materialTechnology
        - release_paper_code:
          The code associated with this item: releasePaperCode
        - release_paper_one:
          The material Id for releasePaperOne
        - release_paper_two:
          The material Id for releasePaperTwo
        - release_paper_side_one:
          The reference key associated with this item: releasePaperSideOne
        - release_paper_side_two:
          The reference key associated with this item: releasePaperSideTwo
        - release_paper_finish_process:
          The reference key associated with this item:
          releasePaperFinishProcess
        - top_layer_material_item:
          The material Id for topLayerMaterialItem
        - middle_layer_1_material_item:
          The material Id for middleLayer1MaterialItem
        - middle_layer_2_material_item:
          The material Id for middleLayer2MaterialItem
        - middle_layer_3_material_item:
          The material Id for middleLayer3MaterialItem
        - bottom_layer_material_item:
          The material Id for bottomLayerMaterialItem
        - non_woven_substrate_type:
          The reference key associated with this item: nonWovenSubstrateType
        - non_woven_web_bonding_method:
          The reference key associated with this item: nonWovenWebBondingMethod
        - color_dominance:
          The reference key associated with this item: colorDominance
        - color_effect:
          The reference key associated with this item: colorEffect
        - color_position:
          The reference key associated with this item: colorPosition
        - color_location:
          The reference key associated with this item: colorLocation
        - color_callout:
          The reference key associated with this item: colorCallout
        - color_fiber:
          The reference key associated with this item: colorFiber
        - dye_method:
          The reference key associated with this item: dyeMethod
        - dye_type:
          The reference key associated with this item: dyeType
        - active_category:
          The reference key associated with this item: activeCategory
        - active_cycle_year:
          The reference key associated with this item: activeCycleYear
        - web_formation:
          The reference key associated with this item: webFormation
        - number_of_colors:
          The reference key associated with this item: numberOfColors
        - last_identifier:
          The last identifier
        - outsourced_process:
          The reference key associated with this item: outsourcedProcess
        - perf_code:
          The coode associated with this item: perfCode
        - animal_source:
          The reference key associated with this item: animalSource
        - dyed_through_crust_indicator:
          The true or false flag associated with this item:
          dyedThroughCrustIndicator
        - oil_content:
          The reference key associated with this item: oilContent
        - re_tannage:
          The reference key associated with this item: reTannage
        - washable_indicator:
          The true or false flag associated with this item: washableIndicator
        - composition_leather_type:
          The reference key associated with this item: compositionLeatherType
        - animal_source_country_of_origin:
          The reference key associated with this item: Animal Source Country of
          Origin
        - satrasumm_qc:
          The reference key associated with this item: Satrasumm QC
        - grain_leather_type:
          The reference key associated with this item: grainLeatherType
        - grain_leather_sub_type:
          The reference key associated with this item: grainLeatherSubType
        - split_leather_type:
          The reference key associated with this item: splitLeatherType
        - average_pu_thickness:
          The number (float) for averagePUThickness
        - coating_thickness_mm:
          The number (float) for coatingThicknessMm
        - moldable:
          The reference key associated with this item: moldable
        - substrate_processing_type:
          The reference key associated with this item: substrateProcessingType
        - substrate_pu_dipped_indicator:
          The true or false flag associated with this item:
          substratePUDippedIndicator
        - substrate_construction:
          The reference key associated with this item: substrateConstruction
        - textile_construction_type:
          The reference key associated with this item: textileConstructionType
        - textile_sub_variation:
          The reference key associated with this item: textileSubVariation
        - textile_sub_variation_two:
          The reference key associated with this item: textileSubVariationTwo
        - textile_variation:
          The reference key associated with this item: textileVariation
        - ends_per_inch_number:
          The number of endsPerInchNumber
        - picks_per_inch_number:
          The number of picksPerInchNumber
        - machinery_type:
          The reference key associated with this item: machineryType
        - warp_count:
          The number of warpCount
        - weft_count:
          The number of weftCount
        - twill_construction_type:
          The reference key associated with this item: twillConstructionType
        - twill_direction:
          The reference key associated with this item: twillDirection
        - fold_indicator:
          The true or false flag associated with this item: foldIndicator
        - rib_construction:
          The reference key associated with this item: ribConstruction
        - height_indicator:
          The reference key associated with this item: heightIndicator
        - rows_of_spandex:
          The number of rowsOfSpandex
        - part_type_orientation:
          The reference key associated with this item: partTypeOrientation
        - initial_development_product_alias:
          The string value associated with this item:
          initialDevelopmentProductAlias
        - pre_twist_yarn:
          The reference key associated with this item: preTwistYarn
        - program:
          The reference key associated with this item: programIdentifier
        - steam_method:
          The reference key associated with this item: steamMethod
        - design_patent_number
        - utility_patent_number
        - development_defect_rate
        - negotiated_defect_rate
        - run_time_minutes
        - gate:
          The reference key associated with this item: Program Gate
        - structure_testing_reference:
          The reference key associated with this item:
          structureTestingReference
        - structure_reference_number:
          The reference key associated with this item: structureReferenceNumber
        - structure_coverage:
          The reference key associated with this item: structureCoverage
        - blanket_number:
          The reference key associated with this item: blanketNumber
        - yarn_size:
          The number (float) of yarnSize
        - yarn_spinning_method:
          The reference key associated with this item: yarnSpinningMethod
        - all_plys_the_same_indicator:
          The true or false flag associated with this item:
          allPlysTheSameIndicator
        - fancy_yarn:
          The reference key associated with this item: fancyYarn
        - fixed_color:
          The reference key associated with this item: fixedColor
        - yarn_brand:
          The reference key associated with this item: yarnBrand
        - yarn_number_system:
          The reference key associated with this item: yarnNumberSystem
        - yarn_twist:
          The reference key associated with this item: yarnTwist
        - yarn_ply_count:
          The number of yarnPlyCount
        - yarn_type:
          The reference key associated with this item: yarnType
        - yarn_luster:
          The reference key associated with this item: yarnLuster
        - yarn_finish_process:
          The reference key associated with this item: yarnFinishProcess
        - yarn_dye_method:
          The reference key associated with this item: yarnDyeMethod
        - yarn_visual_effect:
          The reference key associated with this item: yarnVisualEffect
        - yarn_number_of_ends:
          The number of yarnNumberOfEnds
        - yarn_filament_count:
          The number of yarnFilamentCount
        - yarn_covering_method:
          The reference key associated with this item: yarnCoveringMethod
        - yarn_texture:
          The reference key associated with this item: yarnTexture
        - microfiber_indicator:
          The true or false flag associated with this item: microfiberIndicator
        - yarn_preparation:
          The reference key associated with this item: yarnPreparation
        - yarn_cross_section:
          The reference key associated with this item: yarnCrossSection
        - yarn_location:
          The reference key associated with this item: yarnLocation
        - yarn_supplied_material:
          The reference key associated with this item: yarnSuppliedMaterial
        - yarn_supplied_material_number_of_ends:
          The integer for yarnSuppliedMaterialNumberOfEnds
        - yarn_usage_percentage:
          The number (float) for yarnUsagePercentage
        - base_type:
          The reference key associated with this item: baseType
        - single_component_indicator:
          The reference key associated with this item: singleComponentIndicator
        - flammability_rating:
          The reference key associated with this item: flammabilityRating
        - hotmelt_type:
          The reference key associated with this item: hotmeltType
        - hydrolysis_resistant_indicator:
          The true or false flag associated with this item:
          hydrolysisResistantIndicator
        - method_of_make:
          The reference key associated with this item: methodOfMake
        - chem_poly_form:
          The reference key associated with this item: chemPolyForm
        - film_type:
          The reference key associated with this item: filmType
        - hotmelt_material_item:
          The reference key associated with this item: Hotmelt Material
          Identifier
        - hotmelt_thickness_number_mm:
          The number (float) for hotmeltThicknessNumberMm
        - opacity:
          The reference key associated with this item: opacity
        - stretch_indicator:
          The true or false flag associated with this item: stretchIndicator
        - carrier_paper_statement:
          The reference key associated with this item: carrierPaperStatement
        - foam_type:
          The reference key associated with this item: foamType
        - polyurethane_chemistry:
          The reference key associated with this item: polyurethaneChemistry
        - hardness_asker_c:
          The reference key associated with this item: hardnessAskerC
        - firmness:
          The reference key associated with this item: firmness
        - melting_point_number:
          The number (float) for meltingPointNumber
        - plastic_type:
          The reference key associated with this item: plasticType
        - plastic_sub_type:
          The reference key associated with this item: plasticSubType
        - ultraviolet_inhibitor_indicator:
          The true or false flag associated with this item:
          ultravioletInhibitorIndicator
        - clear_rubber_indicator:
          The true or false flag associated with this item:
          clearRubberIndicator
        - cure_process:
          The reference key associated with this item: cureProcess
        - regrind_content_percentage:
          The number (float) for regrindContentPercentage
        - sport_activity:
          The reference key associated with this item: sportActivity
        - detachable_metal_indicator:
          The true or false flag associated with this item:
          detachableMetalIndicator
        - hard_or_soft_component:
          The reference key associated with this item: hardOrSoftComponent
        - stock_or_custom:
          The reference key associated with this item: stockOrCustom
        - core_construction_type:
          The reference key associated with this item: coreConstructionType
        - component_construction_type:
          The reference key associated with this item:
          componentConstructionType
        - has_core_indicator:
          The true or false flag associated with this item: hasCoreIndicator
        - shape:
          The reference key associated with this item: shape
        - logo_type:
          The reference key associated with this item: logoType
        - logo_name:
          The reference key associated with this item: logoName
        - logo_placement:
          The reference key associated with this item: logoPlacement
        - hotmelt_included_indicator:
          The true or false flag associated with this item:
          hotmeltIncludedIndicator
        - elasticized_indicator:
          The true or false flag associated with this item:
          elasticizedIndicator
        - vendor_color_card_only_indicator:
          The true or false flag associated with this item:
          vendorColorCardOnlyIndicator
        - component_form:
          The reference key associated with this item: componentForm
        - ligne_size_number:
          The number (float) for ligneSizeNumber
        - number_of_holes:
          The number for numberOfHoles
        - adhesive_type:
          The reference key associated with this item: adhesiveType
        - gripper_type:
          The reference key associated with this item: gripperType
        - number_of_gripper_rows:
          The number for numberOfGripperRows
        - end_finish:
          The reference key associated with this item: endFinish
        - for_product_sizes:
          The reference key associated with this item: forProductSizes
        - part_type:
          The reference key associated with this item: partType
        - number_of_rows:
          The number for numberOfRows
        - amount_per_row:
          The number for amountPerRow
        - adjuster_type:
          The reference key associated with this item: adjusterType
        - contains_magnet_indicator:
          The true or false flag associated with this item:
          containsMagnetIndicator
        - button_type:
          The reference key associated with this item: buttonType
        - tape_type:
          The reference key associated with this item: tapeType
        - snap_type:
          The reference key associated with this item: snapType
        - snap_part_type:
          The reference key associated with this item: snapPartType
        - tape_width_mm:
          The number (float) for tapeWidthMm
        - snap_width_mm:
          The number (float) for snapWidthMm
        - snap_repeat_length_mm:
          The number (float) for snapRepeatLengthMm
        - cordlock_toggle_type:
          The reference key associated with this item: cordlockToggleType
        - activation_temperature_number:
          The number (float) for activationTemperatureNumber
        - counter_type:
          The reference key associated with this item: counterType
        - dwell_time:
          The reference key associated with this item: dwellTime
        - general_construction:
          The reference key associated with this item: generalConstruction
        - elastic_type:
          The reference key associated with this item: elasticType
        - crossover_drawcord_indicator:
          The true or false flag associated with this item:
          crossoverDrawcordIndicator
        - elastic_drawcord_content_percentage:
          The number (float) for elasticDrawcordContentPercentage
        - elastic_drawcord_content_type:
          The reference key associated with this item:
          elasticDrawcordContentType
        - elastic_drawcord_content_source:
          The reference key associated with this item:
          elasticDrawcordContentSource
        - elastic_drawcord_aglet_material_item:
          The reference key associated with this item:
          elasticDrawcordAgletMaterialItem
        - elastic_drawcord_has_core_indicator:
          The true or false flag associated with this item:
          elasticDrawcordHasCoreIndicator
        - elastic_drawcord_elasticized_indicator:
          The true or false flag associated with this item:
          elasticDrawcordElasticizedIndicator
        - elastic_drawcord_shape:
          The reference key associated with this item: elasticDrawcordShape
        - elastic_drawcord_logo_name:
          The reference key associated with this item: elasticDrawcordLogoName
        - elastic_drawcord_dimension_width_indicator:
          The reference key associated with this item:
          elasticDrawcordDimensionWidthIndicator
        - elastic_drawcord_gripper_type:
          The reference key associated with this item:
          elasticDrawcordGripperType
        - elastic_drawcord_construction_type:
          The reference key associated with this item:
          elasticDrawcordConstructionType
        - elastic_drawcord_form:
          The reference key associated with this item: elasticDrawcordForm
        - elastic_drawcord_end_finish:
          The reference key associated with this item: elasticDrawcordEndFinish
        - elastic_drawcord_width_mm:
          The number (float) for elasticDrawcordWidthMm
        - elastic_drawcord_finish_process:
          The reference key associated with this item:
          elasticDrawcordFinishProcess
        - elastic_drawcord_dye_method:
          The reference key associated with this item: elasticDrawcordDyeMethod
        - elastic_drawcord_artwork_technique:
          The reference key associated with this item:
          elasticDrawcordArtworkTechnique
        - elastic_drawcord_visual_effect:
          The reference key associated with this item:
          elasticDrawcordVisualEffect
        - elastic_drawcord_number_of_colors:
          he reference key associated with this item:
          elasticDrawcordNumberOfColors
        - elastic_aglet_content_percentage:
          The number (float) for elasticAgletContentPercentage
        - elastic_aglet_content_type:
          The reference key associated with this item: elasticAgletContentType
        - elastic_aglet_content_source:
          The reference key associated with this item:
          elasticAgletContentSource
        - elastic_aglet_logo_name:
          The reference key associated with this item: elasticAgletLogoName
        - elastic_aglet_shape:
          The reference key associated with this item: elasticAgletShape
        - elastic_aglet_construction_type:
          The reference key associated with this item:
          elasticAgletConstructionType
        - elastic_aglet_width_mm:
          The number (float) for elasticAgletWidthMm
        - elastic_aglet_height_mm:
          The number (float) for elasticAgletHeightMm
        - elastic_aglet_internal_diameter_mm:
          The number (float) for elasticAgletInternalDiameterMm
        - elastic_aglet_grams_per_thousand_pieces:
          The number (float) for elasticAgletGramsPerThousandPieces
        - elastic_aglet_finish_process:
          The reference key associated with this item:
          elasticAgletFinishProcess
        - elastic_aglet_dye_method:
          The reference key associated with this item: elasticAgletDyeMethod
        - elastic_aglet_artwork_technique:
          The reference key associated with this item:
          elasticAgletArtworkTechnique
        - elastic_aglet_visual_effect:
          The reference key associated with this item: elasticAgletVisualEffect
        - elastic_aglet_number_of_colors:
          he reference key associated with this item:
          elasticAgletNumberOfColors
        - drawcord_material_item:
          The reference key associated with this item: drawcordMaterialItem
        - drawcord_aglet_material_item:
          The reference key associated with this item:
          drawcordAgletMaterialItem
        - drawcord_aglet_content_percentage:
          The number (float) for drawcordAgletContentPercentage
        - drawcord_aglet_content_type:
          The reference key associated with this item: drawcordAgletContentType
        - drawcord_aglet_content_source:
          The reference key associated with this item:
          drawcordAgletContentSource
        - drawcord_aglet_logo_name:
          The reference key associated with this item: drawcordAgletLogoName
        - drawcord_aglet_shape:
          The reference key associated with this item: drawcordAgletShape
        - drawcord_aglet_construction_type:
          The reference key associated with this item:
          drawcordAgletConstructionType
        - drawcord_aglet_width_mm:
          The number (float) for drawcordAgletWidthMm
        - drawcord_aglet_height_mm:
          The number (float) for drawcordAgletHeightMm
        - drawcord_aglet_internal_diameter_mm:
          The number (float) for drawcordAgletInternalDiameterMm
        - drawcord_aglet_grams_per_thousand_pieces:
          The number (float) for drawcordAgletGramsPerThousandPieces
        - drawcord_aglet_finish_process:
          The reference key associated with this item:
          drawcordAgletFinishProcess
        - drawcord_aglet_dye_method:
          The reference key associated with this item: drawcordAgletDyeMethod
        - drawcord_aglet_artwork_technique:
          The reference key associated with this item:
          drawcordAgletArtworkTechnique
        - drawcord_aglet_visual_effect:
          The reference key associated with this item:
          drawcordAgletVisualEffect
        - drawcord_aglet_number_of_colors:
          he reference key associated with this item:
          drawcordAgletNumberOfColors
        - hook_type:
          The reference key associated with this item: hookType
        - hook_loop_type:
          The reference key associated with this item: hookLoopType
        - label_type:
          The reference key associated with this item: labelType
        - fold_method:
          The reference key associated with this item: foldMethod
        - label_twill_direction:
          The reference key associated with this item: labelTwillDirection
        - backing_type:
          The reference key associated with this item: backingType
        - logo_size:
          The reference key associated with this item: logoSize
        - aglet_material_item:
          The reference key associated with this item: agletMaterialItem
        - has_aglet_indicator:
          The true or false flag associated with this item: hasAgletIndicator
        - number_of_bundles:
          The number for numberOfBundles
        - tip_content:
          The reference key associated with this item: tipContent
        - tip_type:
          The reference key associated with this item: tipType
        - magnet_cover_type:
          The reference key associated with this item: magnetCoverType
        - padding_type:
          The reference key associated with this item: paddingType
        - padding_orientation:
          The reference key associated with this item: paddingOrientation
        - layer_location:
          The reference key associated with this item: layerLocation
        - material_construction:
          The reference key associated with this item: materialConstruction
        - layer_finish_process:
          The reference key associated with this item: layerFinishProcess
        - layer_artwork_technique:
          The reference key associated with this item: layerArtworkTechnique
        - layer_content_percentage:
          The number (float) for layerContentPercentage
        - layer_content_type:
          The reference key associated with this item: layerContentType
        - layer_content_source:
          The reference key associated with this item: layerContentSource
        - pin_badge_type:
          The reference key associated with this item: pinBadgeType
        - plate_orientation:
          The reference key associated with this item: plateOrientation
        - mold_identifier:
          The reference key associated with this item: moldIdentifier
        - ring_type:
          The reference key associated with this item: ringType
        - bonded_indicator:
          The true or false flag associated with this item: bondedIndicator
        - lubricated_indicator:
          The true or false flag associated with this item: lubricatedIndicator
        - thread_ply:
          The number of threadPly
        - thread_size:
          The number (float) for threadSize
        - alternate_thread_size:
          The number (float) for alternateThreadSize
        - thread_type:
          The reference key associated with this item: threadType
        - thread_brand_name:
          The reference key associated with this item: threadBrandName
        - thread_number_system:
          The reference key associated with this item: threadNumberSystem
        - thread_preparation:
          The reference key associated with this item: threadPreparation
        - thread_filament_count:
          The number for threadFilamentCount
        - thread_ply_count:
          The number for threadPlyCount
        - thread_luster:
          The reference key associated with this item: threadLuster
        - thread_statement_content:
          The reference key associated with this item: threadStatementContent
        - zipper_type:
          The reference key associated with this item: zipperType
        - zip_in_compatible_indicator:
          The true or false flag associated with this item:
          zipInCompatibleIndicator
        - zipper_performance:
          The reference key associated with this item: zipperPerformance
        - zipper_brand:
          The reference key associated with this item: zipperBrand
        - slider_pull_logo_name:
          The reference key associated with this item: sliderPullLogoName
        - slider_locking_function:
          The reference key associated with this item: sliderLockingFunction
        - slider_quantity:
          The number for sliderQuantity
        - slider_orientation:
          The reference key associated with this item: sliderOrientation
        - slider_visual_effect:
          The reference key associated with this item: sliderVisualEffect
        - slider_pull_finish_process:
          The reference key associated with this item: sliderPullFinishProcess
        - slider_pull_artwork_technique:
          The reference key associated with this item:
          sliderPullArtworkTechnique
        - zipper_pull_code:
          The reference key associated with this item: zipperPullCode
        - zipper_tape_construction_type:
          The reference key associated with this item:
          zipperTapeConstructionType
        - zipper_tape_logo_name:
          The reference key associated with this item: zipperTapeLogoName
        - zipper_tape_width_mm:
          The number (float) for zipperTapeWidthMm
        - zipper_tape_finish_process:
          The reference key associated with this item: zipperTapeFinishProcess
        - zipper_tape_dye_method:
          The reference key associated with this item: zipperTapeDyeMethod
        - zipper_tape_artwork_technique:
          The reference key associated with this item:
          zipperTapeArtworkTechnique
        - zipper_tape_artwork_graphic:
          The reference key associated with this item: zipperTapeArtworkGraphic
        - zipper_tape_visual_effect:
          The reference key associated with this item: zipperTapeVisualEffect
        - teeth_type:
          The reference key associated with this item: teethType
        - special_zipper_teeth_orientation:
          The reference key associated with this item:
          specialZipperTeethOrientation
        - teeth_size:
          The reference key associated with this item: teethSize
        - teeth_shape:
          The reference key associated with this item: teethShape
        - teeth_repeat_length_mm:
          The number (float) for teethRepeatLengthMm
        - teeth_finish_process:
          The reference key associated with this item: teethFinishProcess
        - teeth_artwork_technique:
          The reference key associated with this item: teethArtworkTechnique
        - teeth_visual_effect:
          The reference key associated with this item: teethVisualEffect
        - contrast_thread_for_coil_indicator:
          The true or false flag associated with this item:
          contrastThreadForCoilIndicator
        - teeth_multi_colored_indicator:
          The true or false flag associated with this item:
          teethMultiColoredIndicator
        - zipper_stop_type:
          The reference key associated with this item: zipperStopType
        - zipper_stop_logo_name:
          The reference key associated with this item: zipperStopLogoName
        - zipper_stop_logo_placement:
          The reference key associated with this item: zipperStopLogoPlacement
        - aglet_construction_type:
          The reference key associated with this item: agletConstructionType
        - airbag_process:
          The reference key associated with this item: airbagProcess
        - airbag_type:
          The reference key associated with this item: airbagType
        - coloration_available:
          The reference key associated with this item: colorationAvailable
        - gas_content:
          The reference key associated with this item: gasContent
        - fill_type:
          The reference key associated with this item: fillType
        - scrim:
          The reference key associated with this item: scrim
        - down_cluster_statement:
          The reference key associated with this item: downClusterStatement
        - fill_power:
          The number for fillPower
        - natural_down_color:
          The reference key associated with this item: naturalDownColor
        - fill_form:
          The reference key associated with this item: fillForm
        - heat_set:
          The reference key associated with this item: heatSet
        - vendor_supplied_indicator:
          The true or false flag associated with this item:
          vendorSuppliedIndicator
        - corporate_designation_indicator:
          The true or false flag associated with this item:
          corporateDesignationIndicator
        - confidential_indicator:
          The true or false flag associated with this item:
          confidentialIndicator
        - country_of_origin_statement_indicator:
          The true or false flag associated with this item:
          countryOfOriginStatementIndicator
        - size_matrix_indicator:
          The true or false flag associated with this item: sizeMatrixIndicator
        - contains_corporate_logo_indicator:
          The true or false flag associated with this item:
          containsCorporateLogoIndicator
        - packaging_intent:
          The reference key associated with this item: packagingIntent
        - packaging_statement:
          The reference key associated with this item: packagingStatement
        - card_type:
          The reference key associated with this item: cardType
        - card_construction_type:
          The reference key associated with this item: cardConstructionType
        - fluting_size:
          The reference key associated with this item: flutingSize
        - inner_linerboard_basis_weight:
          The number innerLinerboardBasisWeight
        - inner_linerboard_type:
          The reference key associated with this item: innerLinerboardType
        - medium_paper_basis_weight:
          The the number for mediumPaperBasisWeight
        - medium_paper_type:
          The reference key associated with this item: mediumPaperType
        - outer_linerboard_basis_weight:
          The number for outerLinerboardBasisWeight
        - outer_linerboard_type:
          The reference key associated with this item: outerLinerboardType
        - fastener_type:
          The reference key associated with this item: fastenerType
        - hanger_type:
          The reference key associated with this item: hangerType
        - hangtag_type:
          The reference key associated with this item: hangtagType
        - partition_type:
          The reference key associated with this item: partitionType
        - shoebag_type:
          The reference key associated with this item: shoebagType
        - shoe_form_type:
          The reference key associated with this item: shoeFormType
        - sticker_type:
          The reference key associated with this item: stickerType
        - tissue_type:
          The reference key associated with this item: tissueType
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/search/suppliedMaterials",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    kwargs.get("x_b_3_trace_id", None),
                    style="form",
                    explode=False,
                ),
            },
            query={
                "count": oapi.client.format_argument_value(
                    "count",
                    kwargs.get("count", None),
                    style="form",
                    explode=False,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    kwargs.get("offset", None),
                    style="form",
                    explode=False,
                ),
                "q": oapi.client.format_argument_value(
                    "q",
                    kwargs.get("q", ""),
                    style="form",
                    explode=False,
                ),
                "material": oapi.client.format_argument_value(
                    "material",
                    kwargs.get("material", None),
                    style="form",
                    explode=False,
                ),
                "supplierLocation": oapi.client.format_argument_value(
                    "supplierLocation",
                    kwargs.get("supplier_location", None),
                    style="form",
                    explode=False,
                ),
                "supplierMaterialNumber": oapi.client.format_argument_value(
                    "supplierMaterialNumber",
                    kwargs.get("supplier_material_number", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialDescription": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialDescription",
                    kwargs.get("supplied_material_description", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialItemName": oapi.client.format_argument_value(
                    "suppliedMaterialItemName",
                    kwargs.get("supplied_material_item_name", None),
                    style="form",
                    explode=False,
                ),
                "supplementalMaterialName": oapi.client.format_argument_value(
                    "supplementalMaterialName",
                    kwargs.get("supplemental_material_name", None),
                    style="form",
                    explode=False,
                ),
                "materialNameVariationWeight": oapi.client.format_argument_value(  # noqa
                    "materialNameVariationWeight",
                    kwargs.get("material_name_variation_weight", None),
                    style="form",
                    explode=False,
                ),
                "materialNameVariationVisual": oapi.client.format_argument_value(  # noqa
                    "materialNameVariationVisual",
                    kwargs.get("material_name_variation_visual", None),
                    style="form",
                    explode=False,
                ),
                "manufacturingCountryofOrigin": oapi.client.format_argument_value(  # noqa
                    "manufacturingCountryofOrigin",
                    kwargs.get("manufacturing_countryof_origin", None),
                    style="form",
                    explode=False,
                ),
                "developmentTeam": oapi.client.format_argument_value(
                    "developmentTeam",
                    kwargs.get("development_team", None),
                    style="form",
                    explode=False,
                ),
                "retirementReasonCode": oapi.client.format_argument_value(
                    "retirementReasonCode",
                    kwargs.get("retirement_reason_code", None),
                    style="form",
                    explode=False,
                ),
                "initialSeasonCycleYear": oapi.client.format_argument_value(
                    "initialSeasonCycleYear",
                    kwargs.get("initial_season_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "targetSeasonCycleYear": oapi.client.format_argument_value(
                    "targetSeasonCycleYear",
                    kwargs.get("target_season_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "legacyCreatedDate": oapi.client.format_argument_value(
                    "legacyCreatedDate",
                    kwargs.get("legacy_created_date", None),
                    style="form",
                    explode=False,
                ),
                "legacySuppliedMaterialNumber": oapi.client.format_argument_value(  # noqa
                    "legacySuppliedMaterialNumber",
                    kwargs.get("legacy_supplied_material_number", None),
                    style="form",
                    explode=False,
                ),
                "materialContentSpecificationNumber": oapi.client.format_argument_value(  # noqa
                    "materialContentSpecificationNumber",
                    kwargs.get("material_content_specification_number", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialState": oapi.client.format_argument_value(
                    "suppliedMaterialState",
                    kwargs.get("supplied_material_state", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialStatusIndicator",
                    kwargs.get("supplied_material_status_indicator", None),
                    style="form",
                    explode=False,
                ),
                "materialLibraryLocatorCode": oapi.client.format_argument_value(  # noqa
                    "materialLibraryLocatorCode",
                    kwargs.get("material_library_locator_code", None),
                    style="form",
                    explode=False,
                ),
                "division": oapi.client.format_argument_value(
                    "division",
                    kwargs.get("division", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialDevelopmentTeam": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialDevelopmentTeam",
                    kwargs.get("supplied_material_development_team", None),
                    style="form",
                    explode=False,
                ),
                "physicalSampleAvailableIndicator": oapi.client.format_argument_value(  # noqa
                    "physicalSampleAvailableIndicator",
                    kwargs.get("physical_sample_available_indicator", None),
                    style="form",
                    explode=False,
                ),
                "physicalSampleDateAdded": oapi.client.format_argument_value(
                    "physicalSampleDateAdded",
                    kwargs.get("physical_sample_date_added", None),
                    style="form",
                    explode=False,
                ),
                "ppsItemNumber": oapi.client.format_argument_value(
                    "ppsItemNumber",
                    kwargs.get("pps_item_number", None),
                    style="form",
                    explode=False,
                ),
                "ppsSubmitNumber": oapi.client.format_argument_value(
                    "ppsSubmitNumber",
                    kwargs.get("pps_submit_number", None),
                    style="form",
                    explode=False,
                ),
                "crossApprovalSuppliedMaterial": oapi.client.format_argument_value(  # noqa
                    "crossApprovalSuppliedMaterial",
                    kwargs.get("cross_approval_supplied_material", None),
                    style="form",
                    explode=False,
                ),
                "approvedVendorArticleNumber": oapi.client.format_argument_value(  # noqa
                    "approvedVendorArticleNumber",
                    kwargs.get("approved_vendor_article_number", None),
                    style="form",
                    explode=False,
                ),
                "buyReadyApprover": oapi.client.format_argument_value(
                    "buyReadyApprover",
                    kwargs.get("buy_ready_approver", None),
                    style="form",
                    explode=False,
                ),
                "buyReadyDate": oapi.client.format_argument_value(
                    "buyReadyDate",
                    kwargs.get("buy_ready_date", None),
                    style="form",
                    explode=False,
                ),
                "expirationDate": oapi.client.format_argument_value(
                    "expirationDate",
                    kwargs.get("expiration_date", None),
                    style="form",
                    explode=False,
                ),
                "dutyAndCompliance": oapi.client.format_argument_value(
                    "dutyAndCompliance",
                    kwargs.get("duty_and_compliance", None),
                    style="form",
                    explode=False,
                ),
                "primarySuppliedMaterialIndicator": oapi.client.format_argument_value(  # noqa
                    "primarySuppliedMaterialIndicator",
                    kwargs.get("primary_supplied_material_indicator", None),
                    style="form",
                    explode=False,
                ),
                "expirationSeasonCycleYear": oapi.client.format_argument_value(
                    "expirationSeasonCycleYear",
                    kwargs.get("expiration_season_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "cuttableLengthNumber": oapi.client.format_argument_value(
                    "cuttableLengthNumber",
                    kwargs.get("cuttable_length_number", None),
                    style="form",
                    explode=False,
                ),
                "cuttableLengthUOM": oapi.client.format_argument_value(
                    "cuttableLengthUOM",
                    kwargs.get("cuttable_length_uom", None),
                    style="form",
                    explode=False,
                ),
                "cuttableWidthNumber": oapi.client.format_argument_value(
                    "cuttableWidthNumber",
                    kwargs.get("cuttable_width_number", None),
                    style="form",
                    explode=False,
                ),
                "cuttableWidthUOM": oapi.client.format_argument_value(
                    "cuttableWidthUOM",
                    kwargs.get("cuttable_width_uom", None),
                    style="form",
                    explode=False,
                ),
                "materialLengthNumber": oapi.client.format_argument_value(
                    "materialLengthNumber",
                    kwargs.get("material_length_number", None),
                    style="form",
                    explode=False,
                ),
                "materialLengthUOM": oapi.client.format_argument_value(
                    "materialLengthUOM",
                    kwargs.get("material_length_uom", None),
                    style="form",
                    explode=False,
                ),
                "materialWidthNumber": oapi.client.format_argument_value(
                    "materialWidthNumber",
                    kwargs.get("material_width_number", None),
                    style="form",
                    explode=False,
                ),
                "materialWidthUOM": oapi.client.format_argument_value(
                    "materialWidthUOM",
                    kwargs.get("material_width_uom", None),
                    style="form",
                    explode=False,
                ),
                "initialPrice": oapi.client.format_argument_value(
                    "initialPrice",
                    kwargs.get("initial_price", None),
                    style="form",
                    explode=False,
                ),
                "initialPriceUOM": oapi.client.format_argument_value(
                    "initialPriceUOM",
                    kwargs.get("initial_price_uom", None),
                    style="form",
                    explode=False,
                ),
                "patent": oapi.client.format_argument_value(
                    "patent",
                    kwargs.get("patent", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorIdentifier": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorIdentifier",
                    kwargs.get("supplied_material_color_identifier", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorGraphicDescription": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorGraphicDescription",
                    kwargs.get("supplied_material_color_graphic_description", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialTeamPlayerGraphicIdentifier": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialTeamPlayerGraphicIdentifier",
                    kwargs.get("supplied_material_team_player_graphic_identifier", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "teamPlayerGraphicIdentifier": oapi.client.format_argument_value(  # noqa
                    "teamPlayerGraphicIdentifier",
                    kwargs.get("team_player_graphic_identifier", None),
                    style="form",
                    explode=False,
                ),
                "color": oapi.client.format_argument_value(
                    "color",
                    kwargs.get("color", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorGraphicPrimaryColor": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorGraphicPrimaryColor",
                    kwargs.get("supplied_material_color_graphic_primary_color", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorGraphicHueIdentifier": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorGraphicHueIdentifier",
                    kwargs.get("supplied_material_color_graphic_hue_identifier", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialMultiColorCode": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialMultiColorCode",
                    kwargs.get("supplied_material_multi_color_code", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorIsMultipleColors": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorIsMultipleColors",
                    kwargs.get("supplied_material_color_is_multiple_colors", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorGraphicInitialCycleYear": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorGraphicInitialCycleYear",
                    kwargs.get("supplied_material_color_graphic_initial_cycle_year", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorGraphicStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorGraphicStatusIndicator",
                    kwargs.get("supplied_material_color_graphic_status_indicator", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorGraphicStateIdentifier": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorGraphicStateIdentifier",
                    kwargs.get("supplied_material_color_graphic_state_identifier", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "createTimestamp": oapi.client.format_argument_value(
                    "createTimestamp",
                    kwargs.get("create_timestamp", None),
                    style="form",
                    explode=False,
                ),
                "changeTimestamp": oapi.client.format_argument_value(
                    "changeTimestamp",
                    kwargs.get("change_timestamp", None),
                    style="form",
                    explode=False,
                ),
                "parentMaterialItemIdentifier": oapi.client.format_argument_value(  # noqa
                    "parentMaterialItemIdentifier",
                    kwargs.get("parent_material_item_identifier", None),
                    style="form",
                    explode=False,
                ),
                "materialType": oapi.client.format_argument_value(
                    "materialType",
                    kwargs.get("material_type", None),
                    style="form",
                    explode=False,
                ),
                "materialItemName": oapi.client.format_argument_value(
                    "materialItemName",
                    kwargs.get("material_item_name", None),
                    style="form",
                    explode=False,
                ),
                "customsDescription": oapi.client.format_argument_value(
                    "customsDescription",
                    kwargs.get("customs_description", None),
                    style="form",
                    explode=False,
                ),
                "coreMaterialNameVariationWeight": oapi.client.format_argument_value(  # noqa
                    "coreMaterialNameVariationWeight",
                    kwargs.get("core_material_name_variation_weight", None),
                    style="form",
                    explode=False,
                ),
                "coreMaterialNameVariationVisual": oapi.client.format_argument_value(  # noqa
                    "coreMaterialNameVariationVisual",
                    kwargs.get("core_material_name_variation_visual", None),
                    style="form",
                    explode=False,
                ),
                "targetPrice": oapi.client.format_argument_value(
                    "targetPrice",
                    kwargs.get("target_price", None),
                    style="form",
                    explode=False,
                ),
                "targetPriceUOM": oapi.client.format_argument_value(
                    "targetPriceUOM",
                    kwargs.get("target_price_uom", None),
                    style="form",
                    explode=False,
                ),
                "materialColorControlMode": oapi.client.format_argument_value(
                    "materialColorControlMode",
                    kwargs.get("material_color_control_mode", None),
                    style="form",
                    explode=False,
                ),
                "materialPricingMode": oapi.client.format_argument_value(
                    "materialPricingMode",
                    kwargs.get("material_pricing_mode", None),
                    style="form",
                    explode=False,
                ),
                "legacyCreatedOnDate": oapi.client.format_argument_value(
                    "legacyCreatedOnDate",
                    kwargs.get("legacy_created_on_date", None),
                    style="form",
                    explode=False,
                ),
                "legacyMaterialNumber": oapi.client.format_argument_value(
                    "legacyMaterialNumber",
                    kwargs.get("legacy_material_number", None),
                    style="form",
                    explode=False,
                ),
                "apparelPDMMaterialNumber": oapi.client.format_argument_value(
                    "apparelPDMMaterialNumber",
                    kwargs.get("apparel_pdm_material_number", None),
                    style="form",
                    explode=False,
                ),
                "materialDevelopmentTeam": oapi.client.format_argument_value(
                    "materialDevelopmentTeam",
                    kwargs.get("material_development_team", None),
                    style="form",
                    explode=False,
                ),
                "materialInitialCategory": oapi.client.format_argument_value(
                    "materialInitialCategory",
                    kwargs.get("material_initial_category", None),
                    style="form",
                    explode=False,
                ),
                "materialInitialCycleYear": oapi.client.format_argument_value(
                    "materialInitialCycleYear",
                    kwargs.get("material_initial_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "materialTargetCycleYear": oapi.client.format_argument_value(
                    "materialTargetCycleYear",
                    kwargs.get("material_target_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "materialItemStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "materialItemStatusIndicator",
                    kwargs.get("material_item_status_indicator", None),
                    style="form",
                    explode=False,
                ),
                "materialBOMIndicator": oapi.client.format_argument_value(
                    "materialBOMIndicator",
                    kwargs.get("material_bom_indicator", None),
                    style="form",
                    explode=False,
                ),
                "coreMaterialContentPercentage": oapi.client.format_argument_value(  # noqa
                    "coreMaterialContentPercentage",
                    kwargs.get("core_material_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "coreMaterialContentType": oapi.client.format_argument_value(
                    "coreMaterialContentType",
                    kwargs.get("core_material_content_type", None),
                    style="form",
                    explode=False,
                ),
                "coreMaterialContentSource": oapi.client.format_argument_value(
                    "coreMaterialContentSource",
                    kwargs.get("core_material_content_source", None),
                    style="form",
                    explode=False,
                ),
                "coreMaterialFamily": oapi.client.format_argument_value(
                    "coreMaterialFamily",
                    kwargs.get("core_material_family", None),
                    style="form",
                    explode=False,
                ),
                "materialContentPercentage": oapi.client.format_argument_value(
                    "materialContentPercentage",
                    kwargs.get("material_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "materialContentType": oapi.client.format_argument_value(
                    "materialContentType",
                    kwargs.get("material_content_type", None),
                    style="form",
                    explode=False,
                ),
                "materialContentSource": oapi.client.format_argument_value(
                    "materialContentSource",
                    kwargs.get("material_content_source", None),
                    style="form",
                    explode=False,
                ),
                "materialLabelContentPercentage": oapi.client.format_argument_value(  # noqa
                    "materialLabelContentPercentage",
                    kwargs.get("material_label_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "materialLabelContentType": oapi.client.format_argument_value(
                    "materialLabelContentType",
                    kwargs.get("material_label_content_type", None),
                    style="form",
                    explode=False,
                ),
                "materialLabelContentSource": oapi.client.format_argument_value(  # noqa
                    "materialLabelContentSource",
                    kwargs.get("material_label_content_source", None),
                    style="form",
                    explode=False,
                ),
                "materialFamily": oapi.client.format_argument_value(
                    "materialFamily",
                    kwargs.get("material_family", None),
                    style="form",
                    explode=False,
                ),
                "materialOwner": oapi.client.format_argument_value(
                    "materialOwner",
                    kwargs.get("material_owner", None),
                    style="form",
                    explode=False,
                ),
                "artworkGraphic": oapi.client.format_argument_value(
                    "artworkGraphic",
                    kwargs.get("artwork_graphic", None),
                    style="form",
                    explode=False,
                ),
                "artworkTechnique": oapi.client.format_argument_value(
                    "artworkTechnique",
                    kwargs.get("artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "secondaryProcessIndicator": oapi.client.format_argument_value(
                    "secondaryProcessIndicator",
                    kwargs.get("secondary_process_indicator", None),
                    style="form",
                    explode=False,
                ),
                "artworkApplicationLocation": oapi.client.format_argument_value(  # noqa
                    "artworkApplicationLocation",
                    kwargs.get("artwork_application_location", None),
                    style="form",
                    explode=False,
                ),
                "artworkRepeatLengthCm": oapi.client.format_argument_value(
                    "artworkRepeatLengthCm",
                    kwargs.get("artwork_repeat_length_cm", None),
                    style="form",
                    explode=False,
                ),
                "directionalPatternIndicator": oapi.client.format_argument_value(  # noqa
                    "directionalPatternIndicator",
                    kwargs.get("directional_pattern_indicator", None),
                    style="form",
                    explode=False,
                ),
                "garmentLocationPlacement": oapi.client.format_argument_value(
                    "garmentLocationPlacement",
                    kwargs.get("garment_location_placement", None),
                    style="form",
                    explode=False,
                ),
                "endUse": oapi.client.format_argument_value(
                    "endUse",
                    kwargs.get("end_use", None),
                    style="form",
                    explode=False,
                ),
                "developmentReason": oapi.client.format_argument_value(
                    "developmentReason",
                    kwargs.get("development_reason", None),
                    style="form",
                    explode=False,
                ),
                "materialBenefits": oapi.client.format_argument_value(
                    "materialBenefits",
                    kwargs.get("material_benefits", None),
                    style="form",
                    explode=False,
                ),
                "fabricFaceDesignation": oapi.client.format_argument_value(
                    "fabricFaceDesignation",
                    kwargs.get("fabric_face_designation", None),
                    style="form",
                    explode=False,
                ),
                "stretchDirection": oapi.client.format_argument_value(
                    "stretchDirection",
                    kwargs.get("stretch_direction", None),
                    style="form",
                    explode=False,
                ),
                "vendorSpecialCareInstructions": oapi.client.format_argument_value(  # noqa
                    "vendorSpecialCareInstructions",
                    kwargs.get("vendor_special_care_instructions", None),
                    style="form",
                    explode=False,
                ),
                "considerationAndRisks": oapi.client.format_argument_value(
                    "considerationAndRisks",
                    kwargs.get("consideration_and_risks", None),
                    style="form",
                    explode=False,
                ),
                "thicknessMm": oapi.client.format_argument_value(
                    "thicknessMm",
                    kwargs.get("thickness_mm", None),
                    style="form",
                    explode=False,
                ),
                "thicknessSelection": oapi.client.format_argument_value(
                    "thicknessSelection",
                    kwargs.get("thickness_selection", None),
                    style="form",
                    explode=False,
                ),
                "maximumThicknessMm": oapi.client.format_argument_value(
                    "maximumThicknessMm",
                    kwargs.get("maximum_thickness_mm", None),
                    style="form",
                    explode=False,
                ),
                "minimumThicknessMm": oapi.client.format_argument_value(
                    "minimumThicknessMm",
                    kwargs.get("minimum_thickness_mm", None),
                    style="form",
                    explode=False,
                ),
                "lengthMm": oapi.client.format_argument_value(
                    "lengthMm",
                    kwargs.get("length_mm", None),
                    style="form",
                    explode=False,
                ),
                "lengthCm": oapi.client.format_argument_value(
                    "lengthCm",
                    kwargs.get("length_cm", None),
                    style="form",
                    explode=False,
                ),
                "dimensionWidthIndicator": oapi.client.format_argument_value(
                    "dimensionWidthIndicator",
                    kwargs.get("dimension_width_indicator", None),
                    style="form",
                    explode=False,
                ),
                "widthMm": oapi.client.format_argument_value(
                    "widthMm",
                    kwargs.get("width_mm", None),
                    style="form",
                    explode=False,
                ),
                "widthCm": oapi.client.format_argument_value(
                    "widthCm",
                    kwargs.get("width_cm", None),
                    style="form",
                    explode=False,
                ),
                "heightMm": oapi.client.format_argument_value(
                    "heightMm",
                    kwargs.get("height_mm", None),
                    style="form",
                    explode=False,
                ),
                "heightCm": oapi.client.format_argument_value(
                    "heightCm",
                    kwargs.get("height_cm", None),
                    style="form",
                    explode=False,
                ),
                "weightGramsPerSquareMeter": oapi.client.format_argument_value(
                    "weightGramsPerSquareMeter",
                    kwargs.get("weight_grams_per_square_meter", None),
                    style="form",
                    explode=False,
                ),
                "externalDiameterMm": oapi.client.format_argument_value(
                    "externalDiameterMm",
                    kwargs.get("external_diameter_mm", None),
                    style="form",
                    explode=False,
                ),
                "externalLengthMm": oapi.client.format_argument_value(
                    "externalLengthMm",
                    kwargs.get("external_length_mm", None),
                    style="form",
                    explode=False,
                ),
                "externalWidthMm": oapi.client.format_argument_value(
                    "externalWidthMm",
                    kwargs.get("external_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "internalDiameterMm": oapi.client.format_argument_value(
                    "internalDiameterMm",
                    kwargs.get("internal_diameter_mm", None),
                    style="form",
                    explode=False,
                ),
                "internalLengthMm": oapi.client.format_argument_value(
                    "internalLengthMm",
                    kwargs.get("internal_length_mm", None),
                    style="form",
                    explode=False,
                ),
                "internalWidthMm": oapi.client.format_argument_value(
                    "internalWidthMm",
                    kwargs.get("internal_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "gaugeInch": oapi.client.format_argument_value(
                    "gaugeInch",
                    kwargs.get("gauge_inch", None),
                    style="form",
                    explode=False,
                ),
                "gramsPerThousandPieces": oapi.client.format_argument_value(
                    "gramsPerThousandPieces",
                    kwargs.get("grams_per_thousand_pieces", None),
                    style="form",
                    explode=False,
                ),
                "weightGramsPerThousandPieces": oapi.client.format_argument_value(  # noqa
                    "weightGramsPerThousandPieces",
                    kwargs.get("weight_grams_per_thousand_pieces", None),
                    style="form",
                    explode=False,
                ),
                "weightGramsPerLinearYard": oapi.client.format_argument_value(
                    "weightGramsPerLinearYard",
                    kwargs.get("weight_grams_per_linear_yard", None),
                    style="form",
                    explode=False,
                ),
                "weightGramsPerLinearMeter": oapi.client.format_argument_value(
                    "weightGramsPerLinearMeter",
                    kwargs.get("weight_grams_per_linear_meter", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionContentPercentage": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionContentPercentage",
                    kwargs.get("yarn_composition_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionContentType": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionContentType",
                    kwargs.get("yarn_composition_content_type", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionContentSource": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionContentSource",
                    kwargs.get("yarn_composition_content_source", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionLocation": oapi.client.format_argument_value(
                    "yarnCompositionLocation",
                    kwargs.get("yarn_composition_location", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionType": oapi.client.format_argument_value(
                    "yarnCompositionType",
                    kwargs.get("yarn_composition_type", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionSize": oapi.client.format_argument_value(
                    "yarnCompositionSize",
                    kwargs.get("yarn_composition_size", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionSpinningMethod": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionSpinningMethod",
                    kwargs.get("yarn_composition_spinning_method", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionCount": oapi.client.format_argument_value(
                    "yarnCompositionCount",
                    kwargs.get("yarn_composition_count", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionPreparation": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionPreparation",
                    kwargs.get("yarn_composition_preparation", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionCrossSection": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionCrossSection",
                    kwargs.get("yarn_composition_cross_section", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionFilamentCount": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionFilamentCount",
                    kwargs.get("yarn_composition_filament_count", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionNumberSystem": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionNumberSystem",
                    kwargs.get("yarn_composition_number_system", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionLuster": oapi.client.format_argument_value(
                    "yarnCompositionLuster",
                    kwargs.get("yarn_composition_luster", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionBrand": oapi.client.format_argument_value(
                    "yarnCompositionBrand",
                    kwargs.get("yarn_composition_brand", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionTexture": oapi.client.format_argument_value(
                    "yarnCompositionTexture",
                    kwargs.get("yarn_composition_texture", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionTwist": oapi.client.format_argument_value(
                    "yarnCompositionTwist",
                    kwargs.get("yarn_composition_twist", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionFinishProcess": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionFinishProcess",
                    kwargs.get("yarn_composition_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionDyeMethod": oapi.client.format_argument_value(
                    "yarnCompositionDyeMethod",
                    kwargs.get("yarn_composition_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionVisualEffect": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionVisualEffect",
                    kwargs.get("yarn_composition_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionFixedColor": oapi.client.format_argument_value(
                    "yarnCompositionFixedColor",
                    kwargs.get("yarn_composition_fixed_color", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionUsagePercentage": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionUsagePercentage",
                    kwargs.get("yarn_composition_usage_percentage", None),
                    style="form",
                    explode=False,
                ),
                "plyContentPercentage": oapi.client.format_argument_value(
                    "plyContentPercentage",
                    kwargs.get("ply_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "plyContentType": oapi.client.format_argument_value(
                    "plyContentType",
                    kwargs.get("ply_content_type", None),
                    style="form",
                    explode=False,
                ),
                "plyContentSource": oapi.client.format_argument_value(
                    "plyContentSource",
                    kwargs.get("ply_content_source", None),
                    style="form",
                    explode=False,
                ),
                "plyLocation": oapi.client.format_argument_value(
                    "plyLocation",
                    kwargs.get("ply_location", None),
                    style="form",
                    explode=False,
                ),
                "plyType": oapi.client.format_argument_value(
                    "plyType",
                    kwargs.get("ply_type", None),
                    style="form",
                    explode=False,
                ),
                "plyBrand": oapi.client.format_argument_value(
                    "plyBrand",
                    kwargs.get("ply_brand", None),
                    style="form",
                    explode=False,
                ),
                "plySize": oapi.client.format_argument_value(
                    "plySize",
                    kwargs.get("ply_size", None),
                    style="form",
                    explode=False,
                ),
                "plyNumberSystem": oapi.client.format_argument_value(
                    "plyNumberSystem",
                    kwargs.get("ply_number_system", None),
                    style="form",
                    explode=False,
                ),
                "plyCrossSection": oapi.client.format_argument_value(
                    "plyCrossSection",
                    kwargs.get("ply_cross_section", None),
                    style="form",
                    explode=False,
                ),
                "plySpinningMethod": oapi.client.format_argument_value(
                    "plySpinningMethod",
                    kwargs.get("ply_spinning_method", None),
                    style="form",
                    explode=False,
                ),
                "plyFilamentCount": oapi.client.format_argument_value(
                    "plyFilamentCount",
                    kwargs.get("ply_filament_count", None),
                    style="form",
                    explode=False,
                ),
                "plyTwist": oapi.client.format_argument_value(
                    "plyTwist",
                    kwargs.get("ply_twist", None),
                    style="form",
                    explode=False,
                ),
                "plyLuster": oapi.client.format_argument_value(
                    "plyLuster",
                    kwargs.get("ply_luster", None),
                    style="form",
                    explode=False,
                ),
                "plyTexture": oapi.client.format_argument_value(
                    "plyTexture",
                    kwargs.get("ply_texture", None),
                    style="form",
                    explode=False,
                ),
                "plyFinishProcess": oapi.client.format_argument_value(
                    "plyFinishProcess",
                    kwargs.get("ply_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "plyDyeMethod": oapi.client.format_argument_value(
                    "plyDyeMethod",
                    kwargs.get("ply_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "plyVisualEffect": oapi.client.format_argument_value(
                    "plyVisualEffect",
                    kwargs.get("ply_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "plyFixedColor": oapi.client.format_argument_value(
                    "plyFixedColor",
                    kwargs.get("ply_fixed_color", None),
                    style="form",
                    explode=False,
                ),
                "plyUsagePercentage": oapi.client.format_argument_value(
                    "plyUsagePercentage",
                    kwargs.get("ply_usage_percentage", None),
                    style="form",
                    explode=False,
                ),
                "fiberContentPercentage": oapi.client.format_argument_value(
                    "fiberContentPercentage",
                    kwargs.get("fiber_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "fiberContentType": oapi.client.format_argument_value(
                    "fiberContentType",
                    kwargs.get("fiber_content_type", None),
                    style="form",
                    explode=False,
                ),
                "fiberContentSource": oapi.client.format_argument_value(
                    "fiberContentSource",
                    kwargs.get("fiber_content_source", None),
                    style="form",
                    explode=False,
                ),
                "fiberSize": oapi.client.format_argument_value(
                    "fiberSize",
                    kwargs.get("fiber_size", None),
                    style="form",
                    explode=False,
                ),
                "fiberPlyLocation": oapi.client.format_argument_value(
                    "fiberPlyLocation",
                    kwargs.get("fiber_ply_location", None),
                    style="form",
                    explode=False,
                ),
                "fiberStapleNumberSystem": oapi.client.format_argument_value(
                    "fiberStapleNumberSystem",
                    kwargs.get("fiber_staple_number_system", None),
                    style="form",
                    explode=False,
                ),
                "fiberStapleLength": oapi.client.format_argument_value(
                    "fiberStapleLength",
                    kwargs.get("fiber_staple_length", None),
                    style="form",
                    explode=False,
                ),
                "fiberStapleLengthMin": oapi.client.format_argument_value(
                    "fiberStapleLengthMin",
                    kwargs.get("fiber_staple_length_min", None),
                    style="form",
                    explode=False,
                ),
                "fiberStapleLengthMax": oapi.client.format_argument_value(
                    "fiberStapleLengthMax",
                    kwargs.get("fiber_staple_length_max", None),
                    style="form",
                    explode=False,
                ),
                "fiberDiameter": oapi.client.format_argument_value(
                    "fiberDiameter",
                    kwargs.get("fiber_diameter", None),
                    style="form",
                    explode=False,
                ),
                "fiberDiameterMin": oapi.client.format_argument_value(
                    "fiberDiameterMin",
                    kwargs.get("fiber_diameter_min", None),
                    style="form",
                    explode=False,
                ),
                "fiberDiameterMax": oapi.client.format_argument_value(
                    "fiberDiameterMax",
                    kwargs.get("fiber_diameter_max", None),
                    style="form",
                    explode=False,
                ),
                "fiberDiameterUnit": oapi.client.format_argument_value(
                    "fiberDiameterUnit",
                    kwargs.get("fiber_diameter_unit", None),
                    style="form",
                    explode=False,
                ),
                "fiberPreparation": oapi.client.format_argument_value(
                    "fiberPreparation",
                    kwargs.get("fiber_preparation", None),
                    style="form",
                    explode=False,
                ),
                "fiberCrossSection": oapi.client.format_argument_value(
                    "fiberCrossSection",
                    kwargs.get("fiber_cross_section", None),
                    style="form",
                    explode=False,
                ),
                "fiberLuster": oapi.client.format_argument_value(
                    "fiberLuster",
                    kwargs.get("fiber_luster", None),
                    style="form",
                    explode=False,
                ),
                "fiberFinishProcess": oapi.client.format_argument_value(
                    "fiberFinishProcess",
                    kwargs.get("fiber_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "fiberDyeMethod": oapi.client.format_argument_value(
                    "fiberDyeMethod",
                    kwargs.get("fiber_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "fiberUsagePercentage": oapi.client.format_argument_value(
                    "fiberUsagePercentage",
                    kwargs.get("fiber_usage_percentage", None),
                    style="form",
                    explode=False,
                ),
                "edgeFinish": oapi.client.format_argument_value(
                    "edgeFinish",
                    kwargs.get("edge_finish", None),
                    style="form",
                    explode=False,
                ),
                "visualEffect": oapi.client.format_argument_value(
                    "visualEffect",
                    kwargs.get("visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "visualEffectLocation": oapi.client.format_argument_value(
                    "visualEffectLocation",
                    kwargs.get("visual_effect_location", None),
                    style="form",
                    explode=False,
                ),
                "printCode": oapi.client.format_argument_value(
                    "printCode",
                    kwargs.get("print_code", None),
                    style="form",
                    explode=False,
                ),
                "embossCodeText": oapi.client.format_argument_value(
                    "embossCodeText",
                    kwargs.get("emboss_code_text", None),
                    style="form",
                    explode=False,
                ),
                "applicationTechnique": oapi.client.format_argument_value(
                    "applicationTechnique",
                    kwargs.get("application_technique", None),
                    style="form",
                    explode=False,
                ),
                "finishProcess": oapi.client.format_argument_value(
                    "finishProcess",
                    kwargs.get("finish_process", None),
                    style="form",
                    explode=False,
                ),
                "finishLocation": oapi.client.format_argument_value(
                    "finishLocation",
                    kwargs.get("finish_location", None),
                    style="form",
                    explode=False,
                ),
                "numberOfPasses": oapi.client.format_argument_value(
                    "numberOfPasses",
                    kwargs.get("number_of_passes", None),
                    style="form",
                    explode=False,
                ),
                "materialTechnologies": oapi.client.format_argument_value(
                    "materialTechnologies",
                    kwargs.get("material_technologies", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperCode": oapi.client.format_argument_value(
                    "releasePaperCode",
                    kwargs.get("release_paper_code", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperOne": oapi.client.format_argument_value(
                    "releasePaperOne",
                    kwargs.get("release_paper_one", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperTwo": oapi.client.format_argument_value(
                    "releasePaperTwo",
                    kwargs.get("release_paper_two", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperSideOne": oapi.client.format_argument_value(
                    "releasePaperSideOne",
                    kwargs.get("release_paper_side_one", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperSideTwo": oapi.client.format_argument_value(
                    "releasePaperSideTwo",
                    kwargs.get("release_paper_side_two", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperFinishProcess": oapi.client.format_argument_value(
                    "releasePaperFinishProcess",
                    kwargs.get("release_paper_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "topLayerMaterialItem": oapi.client.format_argument_value(
                    "topLayerMaterialItem",
                    kwargs.get("top_layer_material_item", None),
                    style="form",
                    explode=False,
                ),
                "middleLayer1MaterialItem": oapi.client.format_argument_value(
                    "middleLayer1MaterialItem",
                    kwargs.get("middle_layer_1_material_item", None),
                    style="form",
                    explode=False,
                ),
                "middleLayer2MaterialItem": oapi.client.format_argument_value(
                    "middleLayer2MaterialItem",
                    kwargs.get("middle_layer_2_material_item", None),
                    style="form",
                    explode=False,
                ),
                "middleLayer3MaterialItem": oapi.client.format_argument_value(
                    "middleLayer3MaterialItem",
                    kwargs.get("middle_layer_3_material_item", None),
                    style="form",
                    explode=False,
                ),
                "bottomLayerMaterialItem": oapi.client.format_argument_value(
                    "bottomLayerMaterialItem",
                    kwargs.get("bottom_layer_material_item", None),
                    style="form",
                    explode=False,
                ),
                "nonWovenSubstrateType": oapi.client.format_argument_value(
                    "nonWovenSubstrateType",
                    kwargs.get("non_woven_substrate_type", None),
                    style="form",
                    explode=False,
                ),
                "nonWovenWebBondingMethod": oapi.client.format_argument_value(
                    "nonWovenWebBondingMethod",
                    kwargs.get("non_woven_web_bonding_method", None),
                    style="form",
                    explode=False,
                ),
                "colorDominance": oapi.client.format_argument_value(
                    "colorDominance",
                    kwargs.get("color_dominance", None),
                    style="form",
                    explode=False,
                ),
                "colorEffect": oapi.client.format_argument_value(
                    "colorEffect",
                    kwargs.get("color_effect", None),
                    style="form",
                    explode=False,
                ),
                "colorPosition": oapi.client.format_argument_value(
                    "colorPosition",
                    kwargs.get("color_position", None),
                    style="form",
                    explode=False,
                ),
                "colorLocation": oapi.client.format_argument_value(
                    "colorLocation",
                    kwargs.get("color_location", None),
                    style="form",
                    explode=False,
                ),
                "colorCallout": oapi.client.format_argument_value(
                    "colorCallout",
                    kwargs.get("color_callout", None),
                    style="form",
                    explode=False,
                ),
                "colorFiber": oapi.client.format_argument_value(
                    "colorFiber",
                    kwargs.get("color_fiber", None),
                    style="form",
                    explode=False,
                ),
                "dyeMethod": oapi.client.format_argument_value(
                    "dyeMethod",
                    kwargs.get("dye_method", None),
                    style="form",
                    explode=False,
                ),
                "dyeType": oapi.client.format_argument_value(
                    "dyeType",
                    kwargs.get("dye_type", None),
                    style="form",
                    explode=False,
                ),
                "activeCategory": oapi.client.format_argument_value(
                    "activeCategory",
                    kwargs.get("active_category", None),
                    style="form",
                    explode=False,
                ),
                "activeCycleYear": oapi.client.format_argument_value(
                    "activeCycleYear",
                    kwargs.get("active_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "webFormation": oapi.client.format_argument_value(
                    "webFormation",
                    kwargs.get("web_formation", None),
                    style="form",
                    explode=False,
                ),
                "numberOfColors": oapi.client.format_argument_value(
                    "numberOfColors",
                    kwargs.get("number_of_colors", None),
                    style="form",
                    explode=False,
                ),
                "lastIdentifier": oapi.client.format_argument_value(
                    "lastIdentifier",
                    kwargs.get("last_identifier", None),
                    style="form",
                    explode=False,
                ),
                "outsourcedProcess": oapi.client.format_argument_value(
                    "outsourcedProcess",
                    kwargs.get("outsourced_process", None),
                    style="form",
                    explode=False,
                ),
                "perfCode": oapi.client.format_argument_value(
                    "perfCode",
                    kwargs.get("perf_code", None),
                    style="form",
                    explode=False,
                ),
                "animalSource": oapi.client.format_argument_value(
                    "animalSource",
                    kwargs.get("animal_source", None),
                    style="form",
                    explode=False,
                ),
                "dyedThroughCrustIndicator": oapi.client.format_argument_value(
                    "dyedThroughCrustIndicator",
                    kwargs.get("dyed_through_crust_indicator", None),
                    style="form",
                    explode=False,
                ),
                "oilContent": oapi.client.format_argument_value(
                    "oilContent",
                    kwargs.get("oil_content", None),
                    style="form",
                    explode=False,
                ),
                "reTannage": oapi.client.format_argument_value(
                    "reTannage",
                    kwargs.get("re_tannage", None),
                    style="form",
                    explode=False,
                ),
                "washableIndicator": oapi.client.format_argument_value(
                    "washableIndicator",
                    kwargs.get("washable_indicator", None),
                    style="form",
                    explode=False,
                ),
                "compositionLeatherType": oapi.client.format_argument_value(
                    "compositionLeatherType",
                    kwargs.get("composition_leather_type", None),
                    style="form",
                    explode=False,
                ),
                "animalSourceCountryOfOrigin": oapi.client.format_argument_value(  # noqa
                    "animalSourceCountryOfOrigin",
                    kwargs.get("animal_source_country_of_origin", None),
                    style="form",
                    explode=False,
                ),
                "satrasummQC": oapi.client.format_argument_value(
                    "satrasummQC",
                    kwargs.get("satrasumm_qc", None),
                    style="form",
                    explode=False,
                ),
                "grainLeatherType": oapi.client.format_argument_value(
                    "grainLeatherType",
                    kwargs.get("grain_leather_type", None),
                    style="form",
                    explode=False,
                ),
                "grainLeatherSubType": oapi.client.format_argument_value(
                    "grainLeatherSubType",
                    kwargs.get("grain_leather_sub_type", None),
                    style="form",
                    explode=False,
                ),
                "splitLeatherType": oapi.client.format_argument_value(
                    "splitLeatherType",
                    kwargs.get("split_leather_type", None),
                    style="form",
                    explode=False,
                ),
                "averagePUThickness": oapi.client.format_argument_value(
                    "averagePUThickness",
                    kwargs.get("average_pu_thickness", None),
                    style="form",
                    explode=False,
                ),
                "coatingThicknessMm": oapi.client.format_argument_value(
                    "coatingThicknessMm",
                    kwargs.get("coating_thickness_mm", None),
                    style="form",
                    explode=False,
                ),
                "moldable": oapi.client.format_argument_value(
                    "moldable",
                    kwargs.get("moldable", None),
                    style="form",
                    explode=False,
                ),
                "substrateProcessingType": oapi.client.format_argument_value(
                    "substrateProcessingType",
                    kwargs.get("substrate_processing_type", None),
                    style="form",
                    explode=False,
                ),
                "substratePUDippedIndicator": oapi.client.format_argument_value(  # noqa
                    "substratePUDippedIndicator",
                    kwargs.get("substrate_pu_dipped_indicator", None),
                    style="form",
                    explode=False,
                ),
                "substrateConstruction": oapi.client.format_argument_value(
                    "substrateConstruction",
                    kwargs.get("substrate_construction", None),
                    style="form",
                    explode=False,
                ),
                "textileConstructionType": oapi.client.format_argument_value(
                    "textileConstructionType",
                    kwargs.get("textile_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "textileSubVariation": oapi.client.format_argument_value(
                    "textileSubVariation",
                    kwargs.get("textile_sub_variation", None),
                    style="form",
                    explode=False,
                ),
                "textileSubVariationTwo": oapi.client.format_argument_value(
                    "textileSubVariationTwo",
                    kwargs.get("textile_sub_variation_two", None),
                    style="form",
                    explode=False,
                ),
                "textileVariation": oapi.client.format_argument_value(
                    "textileVariation",
                    kwargs.get("textile_variation", None),
                    style="form",
                    explode=False,
                ),
                "endsPerInchNumber": oapi.client.format_argument_value(
                    "endsPerInchNumber",
                    kwargs.get("ends_per_inch_number", None),
                    style="form",
                    explode=False,
                ),
                "picksPerInchNumber": oapi.client.format_argument_value(
                    "picksPerInchNumber",
                    kwargs.get("picks_per_inch_number", None),
                    style="form",
                    explode=False,
                ),
                "machineryType": oapi.client.format_argument_value(
                    "machineryType",
                    kwargs.get("machinery_type", None),
                    style="form",
                    explode=False,
                ),
                "warpCount": oapi.client.format_argument_value(
                    "warpCount",
                    kwargs.get("warp_count", None),
                    style="form",
                    explode=False,
                ),
                "weftCount": oapi.client.format_argument_value(
                    "weftCount",
                    kwargs.get("weft_count", None),
                    style="form",
                    explode=False,
                ),
                "twillConstructionType": oapi.client.format_argument_value(
                    "twillConstructionType",
                    kwargs.get("twill_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "twillDirection": oapi.client.format_argument_value(
                    "twillDirection",
                    kwargs.get("twill_direction", None),
                    style="form",
                    explode=False,
                ),
                "foldIndicator": oapi.client.format_argument_value(
                    "foldIndicator",
                    kwargs.get("fold_indicator", None),
                    style="form",
                    explode=False,
                ),
                "ribConstruction": oapi.client.format_argument_value(
                    "ribConstruction",
                    kwargs.get("rib_construction", None),
                    style="form",
                    explode=False,
                ),
                "heightIndicator": oapi.client.format_argument_value(
                    "heightIndicator",
                    kwargs.get("height_indicator", None),
                    style="form",
                    explode=False,
                ),
                "rowsOfSpandex": oapi.client.format_argument_value(
                    "rowsOfSpandex",
                    kwargs.get("rows_of_spandex", None),
                    style="form",
                    explode=False,
                ),
                "partTypeOrientation": oapi.client.format_argument_value(
                    "partTypeOrientation",
                    kwargs.get("part_type_orientation", None),
                    style="form",
                    explode=False,
                ),
                "initialDevelopmentProductAlias": oapi.client.format_argument_value(  # noqa
                    "initialDevelopmentProductAlias",
                    kwargs.get("initial_development_product_alias", None),
                    style="form",
                    explode=False,
                ),
                "preTwistYarn": oapi.client.format_argument_value(
                    "preTwistYarn",
                    kwargs.get("pre_twist_yarn", None),
                    style="form",
                    explode=False,
                ),
                "program": oapi.client.format_argument_value(
                    "program",
                    kwargs.get("program", None),
                    style="form",
                    explode=False,
                ),
                "steamMethod": oapi.client.format_argument_value(
                    "steamMethod",
                    kwargs.get("steam_method", None),
                    style="form",
                    explode=False,
                ),
                "designPatentNumber": oapi.client.format_argument_value(
                    "designPatentNumber",
                    kwargs.get("design_patent_number", None),
                    style="form",
                    explode=False,
                ),
                "utilityPatentNumber": oapi.client.format_argument_value(
                    "utilityPatentNumber",
                    kwargs.get("utility_patent_number", None),
                    style="form",
                    explode=False,
                ),
                "developmentDefectRate": oapi.client.format_argument_value(
                    "developmentDefectRate",
                    kwargs.get("development_defect_rate", None),
                    style="form",
                    explode=False,
                ),
                "negotiatedDefectRate": oapi.client.format_argument_value(
                    "negotiatedDefectRate",
                    kwargs.get("negotiated_defect_rate", None),
                    style="form",
                    explode=False,
                ),
                "runTimeMinutes": oapi.client.format_argument_value(
                    "runTimeMinutes",
                    kwargs.get("run_time_minutes", None),
                    style="form",
                    explode=False,
                ),
                "gate": oapi.client.format_argument_value(
                    "gate",
                    kwargs.get("gate", None),
                    style="form",
                    explode=False,
                ),
                "structureTestingReference": oapi.client.format_argument_value(
                    "structureTestingReference",
                    kwargs.get("structure_testing_reference", None),
                    style="form",
                    explode=False,
                ),
                "structureReferenceNumber": oapi.client.format_argument_value(
                    "structureReferenceNumber",
                    kwargs.get("structure_reference_number", None),
                    style="form",
                    explode=False,
                ),
                "structureCoverage": oapi.client.format_argument_value(
                    "structureCoverage",
                    kwargs.get("structure_coverage", None),
                    style="form",
                    explode=False,
                ),
                "blanketNumber": oapi.client.format_argument_value(
                    "blanketNumber",
                    kwargs.get("blanket_number", None),
                    style="form",
                    explode=False,
                ),
                "yarnSize": oapi.client.format_argument_value(
                    "yarnSize",
                    kwargs.get("yarn_size", None),
                    style="form",
                    explode=False,
                ),
                "yarnSpinningMethod": oapi.client.format_argument_value(
                    "yarnSpinningMethod",
                    kwargs.get("yarn_spinning_method", None),
                    style="form",
                    explode=False,
                ),
                "allPlysTheSameIndicator": oapi.client.format_argument_value(
                    "allPlysTheSameIndicator",
                    kwargs.get("all_plys_the_same_indicator", None),
                    style="form",
                    explode=False,
                ),
                "fancyYarn": oapi.client.format_argument_value(
                    "fancyYarn",
                    kwargs.get("fancy_yarn", None),
                    style="form",
                    explode=False,
                ),
                "fixedColor": oapi.client.format_argument_value(
                    "fixedColor",
                    kwargs.get("fixed_color", None),
                    style="form",
                    explode=False,
                ),
                "yarnBrand": oapi.client.format_argument_value(
                    "yarnBrand",
                    kwargs.get("yarn_brand", None),
                    style="form",
                    explode=False,
                ),
                "yarnNumberSystem": oapi.client.format_argument_value(
                    "yarnNumberSystem",
                    kwargs.get("yarn_number_system", None),
                    style="form",
                    explode=False,
                ),
                "yarnTwist": oapi.client.format_argument_value(
                    "yarnTwist",
                    kwargs.get("yarn_twist", None),
                    style="form",
                    explode=False,
                ),
                "yarnPlyCount": oapi.client.format_argument_value(
                    "yarnPlyCount",
                    kwargs.get("yarn_ply_count", None),
                    style="form",
                    explode=False,
                ),
                "yarnType": oapi.client.format_argument_value(
                    "yarnType",
                    kwargs.get("yarn_type", None),
                    style="form",
                    explode=False,
                ),
                "yarnLuster": oapi.client.format_argument_value(
                    "yarnLuster",
                    kwargs.get("yarn_luster", None),
                    style="form",
                    explode=False,
                ),
                "yarnFinishProcess": oapi.client.format_argument_value(
                    "yarnFinishProcess",
                    kwargs.get("yarn_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "yarnDyeMethod": oapi.client.format_argument_value(
                    "yarnDyeMethod",
                    kwargs.get("yarn_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "yarnVisualEffect": oapi.client.format_argument_value(
                    "yarnVisualEffect",
                    kwargs.get("yarn_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "yarnNumberOfEnds": oapi.client.format_argument_value(
                    "yarnNumberOfEnds",
                    kwargs.get("yarn_number_of_ends", None),
                    style="form",
                    explode=False,
                ),
                "yarnFilamentCount": oapi.client.format_argument_value(
                    "yarnFilamentCount",
                    kwargs.get("yarn_filament_count", None),
                    style="form",
                    explode=False,
                ),
                "yarnCoveringMethod": oapi.client.format_argument_value(
                    "yarnCoveringMethod",
                    kwargs.get("yarn_covering_method", None),
                    style="form",
                    explode=False,
                ),
                "yarnTexture": oapi.client.format_argument_value(
                    "yarnTexture",
                    kwargs.get("yarn_texture", None),
                    style="form",
                    explode=False,
                ),
                "microfiberIndicator": oapi.client.format_argument_value(
                    "microfiberIndicator",
                    kwargs.get("microfiber_indicator", None),
                    style="form",
                    explode=False,
                ),
                "yarnPreparation": oapi.client.format_argument_value(
                    "yarnPreparation",
                    kwargs.get("yarn_preparation", None),
                    style="form",
                    explode=False,
                ),
                "yarnCrossSection": oapi.client.format_argument_value(
                    "yarnCrossSection",
                    kwargs.get("yarn_cross_section", None),
                    style="form",
                    explode=False,
                ),
                "yarnLocation": oapi.client.format_argument_value(
                    "yarnLocation",
                    kwargs.get("yarn_location", None),
                    style="form",
                    explode=False,
                ),
                "yarnSuppliedMaterial": oapi.client.format_argument_value(
                    "yarnSuppliedMaterial",
                    kwargs.get("yarn_supplied_material", None),
                    style="form",
                    explode=False,
                ),
                "yarnSuppliedMaterialNumberOfEnds": oapi.client.format_argument_value(  # noqa
                    "yarnSuppliedMaterialNumberOfEnds",
                    kwargs.get("yarn_supplied_material_number_of_ends", None),
                    style="form",
                    explode=False,
                ),
                "yarnUsagePercentage": oapi.client.format_argument_value(
                    "yarnUsagePercentage",
                    kwargs.get("yarn_usage_percentage", None),
                    style="form",
                    explode=False,
                ),
                "baseType": oapi.client.format_argument_value(
                    "baseType",
                    kwargs.get("base_type", None),
                    style="form",
                    explode=False,
                ),
                "singleComponentIndicator": oapi.client.format_argument_value(
                    "singleComponentIndicator",
                    kwargs.get("single_component_indicator", None),
                    style="form",
                    explode=False,
                ),
                "flammabilityRating": oapi.client.format_argument_value(
                    "flammabilityRating",
                    kwargs.get("flammability_rating", None),
                    style="form",
                    explode=False,
                ),
                "hotmeltType": oapi.client.format_argument_value(
                    "hotmeltType",
                    kwargs.get("hotmelt_type", None),
                    style="form",
                    explode=False,
                ),
                "hydrolysisResistantIndicator": oapi.client.format_argument_value(  # noqa
                    "hydrolysisResistantIndicator",
                    kwargs.get("hydrolysis_resistant_indicator", None),
                    style="form",
                    explode=False,
                ),
                "methodOfMake": oapi.client.format_argument_value(
                    "methodOfMake",
                    kwargs.get("method_of_make", None),
                    style="form",
                    explode=False,
                ),
                "chemPolyForm": oapi.client.format_argument_value(
                    "chemPolyForm",
                    kwargs.get("chem_poly_form", None),
                    style="form",
                    explode=False,
                ),
                "filmType": oapi.client.format_argument_value(
                    "filmType",
                    kwargs.get("film_type", None),
                    style="form",
                    explode=False,
                ),
                "hotmeltMaterialItem": oapi.client.format_argument_value(
                    "hotmeltMaterialItem",
                    kwargs.get("hotmelt_material_item", None),
                    style="form",
                    explode=False,
                ),
                "hotmeltThicknessNumberMm": oapi.client.format_argument_value(
                    "hotmeltThicknessNumberMm",
                    kwargs.get("hotmelt_thickness_number_mm", None),
                    style="form",
                    explode=False,
                ),
                "opacity": oapi.client.format_argument_value(
                    "opacity",
                    kwargs.get("opacity", None),
                    style="form",
                    explode=False,
                ),
                "stretchIndicator": oapi.client.format_argument_value(
                    "stretchIndicator",
                    kwargs.get("stretch_indicator", None),
                    style="form",
                    explode=False,
                ),
                "carrierPaperStatement": oapi.client.format_argument_value(
                    "carrierPaperStatement",
                    kwargs.get("carrier_paper_statement", None),
                    style="form",
                    explode=False,
                ),
                "foamType": oapi.client.format_argument_value(
                    "foamType",
                    kwargs.get("foam_type", None),
                    style="form",
                    explode=False,
                ),
                "polyurethaneChemistry": oapi.client.format_argument_value(
                    "polyurethaneChemistry",
                    kwargs.get("polyurethane_chemistry", None),
                    style="form",
                    explode=False,
                ),
                "hardnessAskerC": oapi.client.format_argument_value(
                    "hardnessAskerC",
                    kwargs.get("hardness_asker_c", None),
                    style="form",
                    explode=False,
                ),
                "firmness": oapi.client.format_argument_value(
                    "firmness",
                    kwargs.get("firmness", None),
                    style="form",
                    explode=False,
                ),
                "meltingPointNumber": oapi.client.format_argument_value(
                    "meltingPointNumber",
                    kwargs.get("melting_point_number", None),
                    style="form",
                    explode=False,
                ),
                "plasticType": oapi.client.format_argument_value(
                    "plasticType",
                    kwargs.get("plastic_type", None),
                    style="form",
                    explode=False,
                ),
                "plasticSubType": oapi.client.format_argument_value(
                    "plasticSubType",
                    kwargs.get("plastic_sub_type", None),
                    style="form",
                    explode=False,
                ),
                "ultravioletInhibitorIndicator": oapi.client.format_argument_value(  # noqa
                    "ultravioletInhibitorIndicator",
                    kwargs.get("ultraviolet_inhibitor_indicator", None),
                    style="form",
                    explode=False,
                ),
                "clearRubberIndicator": oapi.client.format_argument_value(
                    "clearRubberIndicator",
                    kwargs.get("clear_rubber_indicator", None),
                    style="form",
                    explode=False,
                ),
                "cureProcess": oapi.client.format_argument_value(
                    "cureProcess",
                    kwargs.get("cure_process", None),
                    style="form",
                    explode=False,
                ),
                "regrindContentPercentage": oapi.client.format_argument_value(
                    "regrindContentPercentage",
                    kwargs.get("regrind_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "sportActivity": oapi.client.format_argument_value(
                    "sportActivity",
                    kwargs.get("sport_activity", None),
                    style="form",
                    explode=False,
                ),
                "detachableMetalIndicator": oapi.client.format_argument_value(
                    "detachableMetalIndicator",
                    kwargs.get("detachable_metal_indicator", None),
                    style="form",
                    explode=False,
                ),
                "hardOrSoftComponent": oapi.client.format_argument_value(
                    "hardOrSoftComponent",
                    kwargs.get("hard_or_soft_component", None),
                    style="form",
                    explode=False,
                ),
                "stockOrCustom": oapi.client.format_argument_value(
                    "stockOrCustom",
                    kwargs.get("stock_or_custom", None),
                    style="form",
                    explode=False,
                ),
                "coreConstructionType": oapi.client.format_argument_value(
                    "coreConstructionType",
                    kwargs.get("core_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "componentConstructionType": oapi.client.format_argument_value(
                    "componentConstructionType",
                    kwargs.get("component_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "hasCoreIndicator": oapi.client.format_argument_value(
                    "hasCoreIndicator",
                    kwargs.get("has_core_indicator", None),
                    style="form",
                    explode=False,
                ),
                "shape": oapi.client.format_argument_value(
                    "shape",
                    kwargs.get("shape", None),
                    style="form",
                    explode=False,
                ),
                "logoType": oapi.client.format_argument_value(
                    "logoType",
                    kwargs.get("logo_type", None),
                    style="form",
                    explode=False,
                ),
                "logoName": oapi.client.format_argument_value(
                    "logoName",
                    kwargs.get("logo_name", None),
                    style="form",
                    explode=False,
                ),
                "logoPlacement": oapi.client.format_argument_value(
                    "logoPlacement",
                    kwargs.get("logo_placement", None),
                    style="form",
                    explode=False,
                ),
                "hotmeltIncludedIndicator": oapi.client.format_argument_value(
                    "hotmeltIncludedIndicator",
                    kwargs.get("hotmelt_included_indicator", None),
                    style="form",
                    explode=False,
                ),
                "elasticizedIndicator": oapi.client.format_argument_value(
                    "elasticizedIndicator",
                    kwargs.get("elasticized_indicator", None),
                    style="form",
                    explode=False,
                ),
                "vendorColorCardOnlyIndicator": oapi.client.format_argument_value(  # noqa
                    "vendorColorCardOnlyIndicator",
                    kwargs.get("vendor_color_card_only_indicator", None),
                    style="form",
                    explode=False,
                ),
                "componentForm": oapi.client.format_argument_value(
                    "componentForm",
                    kwargs.get("component_form", None),
                    style="form",
                    explode=False,
                ),
                "ligneSizeNumber": oapi.client.format_argument_value(
                    "ligneSizeNumber",
                    kwargs.get("ligne_size_number", None),
                    style="form",
                    explode=False,
                ),
                "numberOfHoles": oapi.client.format_argument_value(
                    "numberOfHoles",
                    kwargs.get("number_of_holes", None),
                    style="form",
                    explode=False,
                ),
                "adhesiveType": oapi.client.format_argument_value(
                    "adhesiveType",
                    kwargs.get("adhesive_type", None),
                    style="form",
                    explode=False,
                ),
                "gripperType": oapi.client.format_argument_value(
                    "gripperType",
                    kwargs.get("gripper_type", None),
                    style="form",
                    explode=False,
                ),
                "numberOfGripperRows": oapi.client.format_argument_value(
                    "numberOfGripperRows",
                    kwargs.get("number_of_gripper_rows", None),
                    style="form",
                    explode=False,
                ),
                "endFinish": oapi.client.format_argument_value(
                    "endFinish",
                    kwargs.get("end_finish", None),
                    style="form",
                    explode=False,
                ),
                "forProductSizes": oapi.client.format_argument_value(
                    "forProductSizes",
                    kwargs.get("for_product_sizes", None),
                    style="form",
                    explode=False,
                ),
                "partType": oapi.client.format_argument_value(
                    "partType",
                    kwargs.get("part_type", None),
                    style="form",
                    explode=False,
                ),
                "numberOfRows": oapi.client.format_argument_value(
                    "numberOfRows",
                    kwargs.get("number_of_rows", None),
                    style="form",
                    explode=False,
                ),
                "amountPerRow": oapi.client.format_argument_value(
                    "amountPerRow",
                    kwargs.get("amount_per_row", None),
                    style="form",
                    explode=False,
                ),
                "adjusterType": oapi.client.format_argument_value(
                    "adjusterType",
                    kwargs.get("adjuster_type", None),
                    style="form",
                    explode=False,
                ),
                "containsMagnetIndicator": oapi.client.format_argument_value(
                    "containsMagnetIndicator",
                    kwargs.get("contains_magnet_indicator", None),
                    style="form",
                    explode=False,
                ),
                "buttonType": oapi.client.format_argument_value(
                    "buttonType",
                    kwargs.get("button_type", None),
                    style="form",
                    explode=False,
                ),
                "tapeType": oapi.client.format_argument_value(
                    "tapeType",
                    kwargs.get("tape_type", None),
                    style="form",
                    explode=False,
                ),
                "snapType": oapi.client.format_argument_value(
                    "snapType",
                    kwargs.get("snap_type", None),
                    style="form",
                    explode=False,
                ),
                "snapPartType": oapi.client.format_argument_value(
                    "snapPartType",
                    kwargs.get("snap_part_type", None),
                    style="form",
                    explode=False,
                ),
                "tapeWidthMm": oapi.client.format_argument_value(
                    "tapeWidthMm",
                    kwargs.get("tape_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "snapWidthMm": oapi.client.format_argument_value(
                    "snapWidthMm",
                    kwargs.get("snap_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "snapRepeatLengthMm": oapi.client.format_argument_value(
                    "snapRepeatLengthMm",
                    kwargs.get("snap_repeat_length_mm", None),
                    style="form",
                    explode=False,
                ),
                "cordlockToggleType": oapi.client.format_argument_value(
                    "cordlockToggleType",
                    kwargs.get("cordlock_toggle_type", None),
                    style="form",
                    explode=False,
                ),
                "activationTemperatureNumber": oapi.client.format_argument_value(  # noqa
                    "activationTemperatureNumber",
                    kwargs.get("activation_temperature_number", None),
                    style="form",
                    explode=False,
                ),
                "counterType": oapi.client.format_argument_value(
                    "counterType",
                    kwargs.get("counter_type", None),
                    style="form",
                    explode=False,
                ),
                "dwellTime": oapi.client.format_argument_value(
                    "dwellTime",
                    kwargs.get("dwell_time", None),
                    style="form",
                    explode=False,
                ),
                "generalConstruction": oapi.client.format_argument_value(
                    "generalConstruction",
                    kwargs.get("general_construction", None),
                    style="form",
                    explode=False,
                ),
                "elasticType": oapi.client.format_argument_value(
                    "elasticType",
                    kwargs.get("elastic_type", None),
                    style="form",
                    explode=False,
                ),
                "crossoverDrawcordIndicator": oapi.client.format_argument_value(  # noqa
                    "crossoverDrawcordIndicator",
                    kwargs.get("crossover_drawcord_indicator", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordContentPercentage": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordContentPercentage",
                    kwargs.get("elastic_drawcord_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordContentType": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordContentType",
                    kwargs.get("elastic_drawcord_content_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordContentSource": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordContentSource",
                    kwargs.get("elastic_drawcord_content_source", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordAgletMaterialItem": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordAgletMaterialItem",
                    kwargs.get("elastic_drawcord_aglet_material_item", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordHasCoreIndicator": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordHasCoreIndicator",
                    kwargs.get("elastic_drawcord_has_core_indicator", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordElasticizedIndicator": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordElasticizedIndicator",
                    kwargs.get("elastic_drawcord_elasticized_indicator", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordShape": oapi.client.format_argument_value(
                    "elasticDrawcordShape",
                    kwargs.get("elastic_drawcord_shape", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordLogoName": oapi.client.format_argument_value(
                    "elasticDrawcordLogoName",
                    kwargs.get("elastic_drawcord_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordDimensionWidthIndicator": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordDimensionWidthIndicator",
                    kwargs.get("elastic_drawcord_dimension_width_indicator", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordGripperType": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordGripperType",
                    kwargs.get("elastic_drawcord_gripper_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordConstructionType": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordConstructionType",
                    kwargs.get("elastic_drawcord_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordForm": oapi.client.format_argument_value(
                    "elasticDrawcordForm",
                    kwargs.get("elastic_drawcord_form", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordEndFinish": oapi.client.format_argument_value(
                    "elasticDrawcordEndFinish",
                    kwargs.get("elastic_drawcord_end_finish", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordWidthMm": oapi.client.format_argument_value(
                    "elasticDrawcordWidthMm",
                    kwargs.get("elastic_drawcord_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordFinishProcess": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordFinishProcess",
                    kwargs.get("elastic_drawcord_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordDyeMethod": oapi.client.format_argument_value(
                    "elasticDrawcordDyeMethod",
                    kwargs.get("elastic_drawcord_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordArtworkTechnique",
                    kwargs.get("elastic_drawcord_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordVisualEffect": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordVisualEffect",
                    kwargs.get("elastic_drawcord_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordNumberOfColors": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordNumberOfColors",
                    kwargs.get("elastic_drawcord_number_of_colors", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletContentPercentage": oapi.client.format_argument_value(  # noqa
                    "elasticAgletContentPercentage",
                    kwargs.get("elastic_aglet_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletContentType": oapi.client.format_argument_value(
                    "elasticAgletContentType",
                    kwargs.get("elastic_aglet_content_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletContentSource": oapi.client.format_argument_value(
                    "elasticAgletContentSource",
                    kwargs.get("elastic_aglet_content_source", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletLogoName": oapi.client.format_argument_value(
                    "elasticAgletLogoName",
                    kwargs.get("elastic_aglet_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletShape": oapi.client.format_argument_value(
                    "elasticAgletShape",
                    kwargs.get("elastic_aglet_shape", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletConstructionType": oapi.client.format_argument_value(  # noqa
                    "elasticAgletConstructionType",
                    kwargs.get("elastic_aglet_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletWidthMm": oapi.client.format_argument_value(
                    "elasticAgletWidthMm",
                    kwargs.get("elastic_aglet_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletHeightMm": oapi.client.format_argument_value(
                    "elasticAgletHeightMm",
                    kwargs.get("elastic_aglet_height_mm", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletInternalDiameterMm": oapi.client.format_argument_value(  # noqa
                    "elasticAgletInternalDiameterMm",
                    kwargs.get("elastic_aglet_internal_diameter_mm", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletGramsPerThousandPieces": oapi.client.format_argument_value(  # noqa
                    "elasticAgletGramsPerThousandPieces",
                    kwargs.get("elastic_aglet_grams_per_thousand_pieces", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "elasticAgletFinishProcess": oapi.client.format_argument_value(
                    "elasticAgletFinishProcess",
                    kwargs.get("elastic_aglet_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletDyeMethod": oapi.client.format_argument_value(
                    "elasticAgletDyeMethod",
                    kwargs.get("elastic_aglet_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "elasticAgletArtworkTechnique",
                    kwargs.get("elastic_aglet_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletVisualEffect": oapi.client.format_argument_value(
                    "elasticAgletVisualEffect",
                    kwargs.get("elastic_aglet_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletNumberOfColors": oapi.client.format_argument_value(  # noqa
                    "elasticAgletNumberOfColors",
                    kwargs.get("elastic_aglet_number_of_colors", None),
                    style="form",
                    explode=False,
                ),
                "drawcordMaterialItem": oapi.client.format_argument_value(
                    "drawcordMaterialItem",
                    kwargs.get("drawcord_material_item", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletMaterialItem": oapi.client.format_argument_value(
                    "drawcordAgletMaterialItem",
                    kwargs.get("drawcord_aglet_material_item", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletContentPercentage": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletContentPercentage",
                    kwargs.get("drawcord_aglet_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletContentType": oapi.client.format_argument_value(
                    "drawcordAgletContentType",
                    kwargs.get("drawcord_aglet_content_type", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletContentSource": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletContentSource",
                    kwargs.get("drawcord_aglet_content_source", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletLogoName": oapi.client.format_argument_value(
                    "drawcordAgletLogoName",
                    kwargs.get("drawcord_aglet_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletShape": oapi.client.format_argument_value(
                    "drawcordAgletShape",
                    kwargs.get("drawcord_aglet_shape", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletConstructionType": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletConstructionType",
                    kwargs.get("drawcord_aglet_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletWidthMm": oapi.client.format_argument_value(
                    "drawcordAgletWidthMm",
                    kwargs.get("drawcord_aglet_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletHeightMm": oapi.client.format_argument_value(
                    "drawcordAgletHeightMm",
                    kwargs.get("drawcord_aglet_height_mm", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletInternalDiameterMm": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletInternalDiameterMm",
                    kwargs.get("drawcord_aglet_internal_diameter_mm", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletGramsPerThousandPieces": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletGramsPerThousandPieces",
                    kwargs.get("drawcord_aglet_grams_per_thousand_pieces", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "drawcordAgletFinishProcess": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletFinishProcess",
                    kwargs.get("drawcord_aglet_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletDyeMethod": oapi.client.format_argument_value(
                    "drawcordAgletDyeMethod",
                    kwargs.get("drawcord_aglet_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletArtworkTechnique",
                    kwargs.get("drawcord_aglet_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletVisualEffect": oapi.client.format_argument_value(
                    "drawcordAgletVisualEffect",
                    kwargs.get("drawcord_aglet_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletNumberOfColors": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletNumberOfColors",
                    kwargs.get("drawcord_aglet_number_of_colors", None),
                    style="form",
                    explode=False,
                ),
                "hookType": oapi.client.format_argument_value(
                    "hookType",
                    kwargs.get("hook_type", None),
                    style="form",
                    explode=False,
                ),
                "hookLoopType": oapi.client.format_argument_value(
                    "hookLoopType",
                    kwargs.get("hook_loop_type", None),
                    style="form",
                    explode=False,
                ),
                "labelType": oapi.client.format_argument_value(
                    "labelType",
                    kwargs.get("label_type", None),
                    style="form",
                    explode=False,
                ),
                "foldMethod": oapi.client.format_argument_value(
                    "foldMethod",
                    kwargs.get("fold_method", None),
                    style="form",
                    explode=False,
                ),
                "labelTwillDirection": oapi.client.format_argument_value(
                    "labelTwillDirection",
                    kwargs.get("label_twill_direction", None),
                    style="form",
                    explode=False,
                ),
                "backingType": oapi.client.format_argument_value(
                    "backingType",
                    kwargs.get("backing_type", None),
                    style="form",
                    explode=False,
                ),
                "logoSize": oapi.client.format_argument_value(
                    "logoSize",
                    kwargs.get("logo_size", None),
                    style="form",
                    explode=False,
                ),
                "agletMaterialItem": oapi.client.format_argument_value(
                    "agletMaterialItem",
                    kwargs.get("aglet_material_item", None),
                    style="form",
                    explode=False,
                ),
                "hasAgletIndicator": oapi.client.format_argument_value(
                    "hasAgletIndicator",
                    kwargs.get("has_aglet_indicator", None),
                    style="form",
                    explode=False,
                ),
                "numberOfBundles": oapi.client.format_argument_value(
                    "numberOfBundles",
                    kwargs.get("number_of_bundles", None),
                    style="form",
                    explode=False,
                ),
                "tipContent": oapi.client.format_argument_value(
                    "tipContent",
                    kwargs.get("tip_content", None),
                    style="form",
                    explode=False,
                ),
                "tipType": oapi.client.format_argument_value(
                    "tipType",
                    kwargs.get("tip_type", None),
                    style="form",
                    explode=False,
                ),
                "magnetCoverType": oapi.client.format_argument_value(
                    "magnetCoverType",
                    kwargs.get("magnet_cover_type", None),
                    style="form",
                    explode=False,
                ),
                "paddingType": oapi.client.format_argument_value(
                    "paddingType",
                    kwargs.get("padding_type", None),
                    style="form",
                    explode=False,
                ),
                "paddingOrientation": oapi.client.format_argument_value(
                    "paddingOrientation",
                    kwargs.get("padding_orientation", None),
                    style="form",
                    explode=False,
                ),
                "layerLocation": oapi.client.format_argument_value(
                    "layerLocation",
                    kwargs.get("layer_location", None),
                    style="form",
                    explode=False,
                ),
                "materialConstruction": oapi.client.format_argument_value(
                    "materialConstruction",
                    kwargs.get("material_construction", None),
                    style="form",
                    explode=False,
                ),
                "layerFinishProcess": oapi.client.format_argument_value(
                    "layerFinishProcess",
                    kwargs.get("layer_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "layerArtworkTechnique": oapi.client.format_argument_value(
                    "layerArtworkTechnique",
                    kwargs.get("layer_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "layerContentPercentage": oapi.client.format_argument_value(
                    "layerContentPercentage",
                    kwargs.get("layer_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "layerContentType": oapi.client.format_argument_value(
                    "layerContentType",
                    kwargs.get("layer_content_type", None),
                    style="form",
                    explode=False,
                ),
                "layerContentSource": oapi.client.format_argument_value(
                    "layerContentSource",
                    kwargs.get("layer_content_source", None),
                    style="form",
                    explode=False,
                ),
                "pinBadgeType": oapi.client.format_argument_value(
                    "pinBadgeType",
                    kwargs.get("pin_badge_type", None),
                    style="form",
                    explode=False,
                ),
                "plateOrientation": oapi.client.format_argument_value(
                    "plateOrientation",
                    kwargs.get("plate_orientation", None),
                    style="form",
                    explode=False,
                ),
                "moldIdentifier": oapi.client.format_argument_value(
                    "moldIdentifier",
                    kwargs.get("mold_identifier", None),
                    style="form",
                    explode=False,
                ),
                "ringType": oapi.client.format_argument_value(
                    "ringType",
                    kwargs.get("ring_type", None),
                    style="form",
                    explode=False,
                ),
                "bondedIndicator": oapi.client.format_argument_value(
                    "bondedIndicator",
                    kwargs.get("bonded_indicator", None),
                    style="form",
                    explode=False,
                ),
                "lubricatedIndicator": oapi.client.format_argument_value(
                    "lubricatedIndicator",
                    kwargs.get("lubricated_indicator", None),
                    style="form",
                    explode=False,
                ),
                "threadPly": oapi.client.format_argument_value(
                    "threadPly",
                    kwargs.get("thread_ply", None),
                    style="form",
                    explode=False,
                ),
                "threadSize": oapi.client.format_argument_value(
                    "threadSize",
                    kwargs.get("thread_size", None),
                    style="form",
                    explode=False,
                ),
                "alternateThreadSize": oapi.client.format_argument_value(
                    "alternateThreadSize",
                    kwargs.get("alternate_thread_size", None),
                    style="form",
                    explode=False,
                ),
                "threadType": oapi.client.format_argument_value(
                    "threadType",
                    kwargs.get("thread_type", None),
                    style="form",
                    explode=False,
                ),
                "threadBrandName": oapi.client.format_argument_value(
                    "threadBrandName",
                    kwargs.get("thread_brand_name", None),
                    style="form",
                    explode=False,
                ),
                "threadNumberSystem": oapi.client.format_argument_value(
                    "threadNumberSystem",
                    kwargs.get("thread_number_system", None),
                    style="form",
                    explode=False,
                ),
                "threadPreparation": oapi.client.format_argument_value(
                    "threadPreparation",
                    kwargs.get("thread_preparation", None),
                    style="form",
                    explode=False,
                ),
                "threadFilamentCount": oapi.client.format_argument_value(
                    "threadFilamentCount",
                    kwargs.get("thread_filament_count", None),
                    style="form",
                    explode=False,
                ),
                "threadPlyCount": oapi.client.format_argument_value(
                    "threadPlyCount",
                    kwargs.get("thread_ply_count", None),
                    style="form",
                    explode=False,
                ),
                "threadLuster": oapi.client.format_argument_value(
                    "threadLuster",
                    kwargs.get("thread_luster", None),
                    style="form",
                    explode=False,
                ),
                "threadStatementContent": oapi.client.format_argument_value(
                    "threadStatementContent",
                    kwargs.get("thread_statement_content", None),
                    style="form",
                    explode=False,
                ),
                "zipperType": oapi.client.format_argument_value(
                    "zipperType",
                    kwargs.get("zipper_type", None),
                    style="form",
                    explode=False,
                ),
                "zipInCompatibleIndicator": oapi.client.format_argument_value(
                    "zipInCompatibleIndicator",
                    kwargs.get("zip_in_compatible_indicator", None),
                    style="form",
                    explode=False,
                ),
                "zipperPerformance": oapi.client.format_argument_value(
                    "zipperPerformance",
                    kwargs.get("zipper_performance", None),
                    style="form",
                    explode=False,
                ),
                "zipperBrand": oapi.client.format_argument_value(
                    "zipperBrand",
                    kwargs.get("zipper_brand", None),
                    style="form",
                    explode=False,
                ),
                "sliderPullLogoName": oapi.client.format_argument_value(
                    "sliderPullLogoName",
                    kwargs.get("slider_pull_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "sliderLockingFunction": oapi.client.format_argument_value(
                    "sliderLockingFunction",
                    kwargs.get("slider_locking_function", None),
                    style="form",
                    explode=False,
                ),
                "sliderQuantity": oapi.client.format_argument_value(
                    "sliderQuantity",
                    kwargs.get("slider_quantity", None),
                    style="form",
                    explode=False,
                ),
                "sliderOrientation": oapi.client.format_argument_value(
                    "sliderOrientation",
                    kwargs.get("slider_orientation", None),
                    style="form",
                    explode=False,
                ),
                "sliderVisualEffect": oapi.client.format_argument_value(
                    "sliderVisualEffect",
                    kwargs.get("slider_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "sliderPullFinishProcess": oapi.client.format_argument_value(
                    "sliderPullFinishProcess",
                    kwargs.get("slider_pull_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "sliderPullArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "sliderPullArtworkTechnique",
                    kwargs.get("slider_pull_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "zipperPullCode": oapi.client.format_argument_value(
                    "zipperPullCode",
                    kwargs.get("zipper_pull_code", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeConstructionType": oapi.client.format_argument_value(  # noqa
                    "zipperTapeConstructionType",
                    kwargs.get("zipper_tape_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeLogoName": oapi.client.format_argument_value(
                    "zipperTapeLogoName",
                    kwargs.get("zipper_tape_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeWidthMm": oapi.client.format_argument_value(
                    "zipperTapeWidthMm",
                    kwargs.get("zipper_tape_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeFinishProcess": oapi.client.format_argument_value(
                    "zipperTapeFinishProcess",
                    kwargs.get("zipper_tape_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeDyeMethod": oapi.client.format_argument_value(
                    "zipperTapeDyeMethod",
                    kwargs.get("zipper_tape_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "zipperTapeArtworkTechnique",
                    kwargs.get("zipper_tape_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeArtworkGraphic": oapi.client.format_argument_value(
                    "zipperTapeArtworkGraphic",
                    kwargs.get("zipper_tape_artwork_graphic", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeVisualEffect": oapi.client.format_argument_value(
                    "zipperTapeVisualEffect",
                    kwargs.get("zipper_tape_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "teethType": oapi.client.format_argument_value(
                    "teethType",
                    kwargs.get("teeth_type", None),
                    style="form",
                    explode=False,
                ),
                "specialZipperTeethOrientation": oapi.client.format_argument_value(  # noqa
                    "specialZipperTeethOrientation",
                    kwargs.get("special_zipper_teeth_orientation", None),
                    style="form",
                    explode=False,
                ),
                "teethSize": oapi.client.format_argument_value(
                    "teethSize",
                    kwargs.get("teeth_size", None),
                    style="form",
                    explode=False,
                ),
                "teethShape": oapi.client.format_argument_value(
                    "teethShape",
                    kwargs.get("teeth_shape", None),
                    style="form",
                    explode=False,
                ),
                "teethRepeatLengthMm": oapi.client.format_argument_value(
                    "teethRepeatLengthMm",
                    kwargs.get("teeth_repeat_length_mm", None),
                    style="form",
                    explode=False,
                ),
                "teethFinishProcess": oapi.client.format_argument_value(
                    "teethFinishProcess",
                    kwargs.get("teeth_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "teethArtworkTechnique": oapi.client.format_argument_value(
                    "teethArtworkTechnique",
                    kwargs.get("teeth_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "teethVisualEffect": oapi.client.format_argument_value(
                    "teethVisualEffect",
                    kwargs.get("teeth_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "contrastThreadForCoilIndicator": oapi.client.format_argument_value(  # noqa
                    "contrastThreadForCoilIndicator",
                    kwargs.get("contrast_thread_for_coil_indicator", None),
                    style="form",
                    explode=False,
                ),
                "teethMultiColoredIndicator": oapi.client.format_argument_value(  # noqa
                    "teethMultiColoredIndicator",
                    kwargs.get("teeth_multi_colored_indicator", None),
                    style="form",
                    explode=False,
                ),
                "zipperStopType": oapi.client.format_argument_value(
                    "zipperStopType",
                    kwargs.get("zipper_stop_type", None),
                    style="form",
                    explode=False,
                ),
                "zipperStopLogoName": oapi.client.format_argument_value(
                    "zipperStopLogoName",
                    kwargs.get("zipper_stop_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "zipperStopLogoPlacement": oapi.client.format_argument_value(
                    "zipperStopLogoPlacement",
                    kwargs.get("zipper_stop_logo_placement", None),
                    style="form",
                    explode=False,
                ),
                "agletConstructionType": oapi.client.format_argument_value(
                    "agletConstructionType",
                    kwargs.get("aglet_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "airbagProcess": oapi.client.format_argument_value(
                    "airbagProcess",
                    kwargs.get("airbag_process", None),
                    style="form",
                    explode=False,
                ),
                "airbagType": oapi.client.format_argument_value(
                    "airbagType",
                    kwargs.get("airbag_type", None),
                    style="form",
                    explode=False,
                ),
                "colorationAvailable": oapi.client.format_argument_value(
                    "colorationAvailable",
                    kwargs.get("coloration_available", None),
                    style="form",
                    explode=False,
                ),
                "gasContent": oapi.client.format_argument_value(
                    "gasContent",
                    kwargs.get("gas_content", None),
                    style="form",
                    explode=False,
                ),
                "fillType": oapi.client.format_argument_value(
                    "fillType",
                    kwargs.get("fill_type", None),
                    style="form",
                    explode=False,
                ),
                "scrim": oapi.client.format_argument_value(
                    "scrim",
                    kwargs.get("scrim", None),
                    style="form",
                    explode=False,
                ),
                "downClusterStatement": oapi.client.format_argument_value(
                    "downClusterStatement",
                    kwargs.get("down_cluster_statement", None),
                    style="form",
                    explode=False,
                ),
                "fillPower": oapi.client.format_argument_value(
                    "fillPower",
                    kwargs.get("fill_power", None),
                    style="form",
                    explode=False,
                ),
                "naturalDownColor": oapi.client.format_argument_value(
                    "naturalDownColor",
                    kwargs.get("natural_down_color", None),
                    style="form",
                    explode=False,
                ),
                "fillForm": oapi.client.format_argument_value(
                    "fillForm",
                    kwargs.get("fill_form", None),
                    style="form",
                    explode=False,
                ),
                "heatSet": oapi.client.format_argument_value(
                    "heatSet",
                    kwargs.get("heat_set", None),
                    style="form",
                    explode=False,
                ),
                "vendorSuppliedIndicator": oapi.client.format_argument_value(
                    "vendorSuppliedIndicator",
                    kwargs.get("vendor_supplied_indicator", None),
                    style="form",
                    explode=False,
                ),
                "corporateDesignationIndicator": oapi.client.format_argument_value(  # noqa
                    "corporateDesignationIndicator",
                    kwargs.get("corporate_designation_indicator", None),
                    style="form",
                    explode=False,
                ),
                "confidentialIndicator": oapi.client.format_argument_value(
                    "confidentialIndicator",
                    kwargs.get("confidential_indicator", None),
                    style="form",
                    explode=False,
                ),
                "countryOfOriginStatementIndicator": oapi.client.format_argument_value(  # noqa
                    "countryOfOriginStatementIndicator",
                    kwargs.get("country_of_origin_statement_indicator", None),
                    style="form",
                    explode=False,
                ),
                "sizeMatrixIndicator": oapi.client.format_argument_value(
                    "sizeMatrixIndicator",
                    kwargs.get("size_matrix_indicator", None),
                    style="form",
                    explode=False,
                ),
                "containsCorporateLogoIndicator": oapi.client.format_argument_value(  # noqa
                    "containsCorporateLogoIndicator",
                    kwargs.get("contains_corporate_logo_indicator", None),
                    style="form",
                    explode=False,
                ),
                "packagingIntent": oapi.client.format_argument_value(
                    "packagingIntent",
                    kwargs.get("packaging_intent", None),
                    style="form",
                    explode=False,
                ),
                "packagingStatement": oapi.client.format_argument_value(
                    "packagingStatement",
                    kwargs.get("packaging_statement", None),
                    style="form",
                    explode=False,
                ),
                "cardType": oapi.client.format_argument_value(
                    "cardType",
                    kwargs.get("card_type", None),
                    style="form",
                    explode=False,
                ),
                "cardConstructionType": oapi.client.format_argument_value(
                    "cardConstructionType",
                    kwargs.get("card_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "flutingSize": oapi.client.format_argument_value(
                    "flutingSize",
                    kwargs.get("fluting_size", None),
                    style="form",
                    explode=False,
                ),
                "innerLinerboardBasisWeight": oapi.client.format_argument_value(  # noqa
                    "innerLinerboardBasisWeight",
                    kwargs.get("inner_linerboard_basis_weight", None),
                    style="form",
                    explode=False,
                ),
                "innerLinerboardType": oapi.client.format_argument_value(
                    "innerLinerboardType",
                    kwargs.get("inner_linerboard_type", None),
                    style="form",
                    explode=False,
                ),
                "mediumPaperBasisWeight": oapi.client.format_argument_value(
                    "mediumPaperBasisWeight",
                    kwargs.get("medium_paper_basis_weight", None),
                    style="form",
                    explode=False,
                ),
                "mediumPaperType": oapi.client.format_argument_value(
                    "mediumPaperType",
                    kwargs.get("medium_paper_type", None),
                    style="form",
                    explode=False,
                ),
                "outerLinerboardBasisWeight": oapi.client.format_argument_value(  # noqa
                    "outerLinerboardBasisWeight",
                    kwargs.get("outer_linerboard_basis_weight", None),
                    style="form",
                    explode=False,
                ),
                "outerLinerboardType": oapi.client.format_argument_value(
                    "outerLinerboardType",
                    kwargs.get("outer_linerboard_type", None),
                    style="form",
                    explode=False,
                ),
                "fastenerType": oapi.client.format_argument_value(
                    "fastenerType",
                    kwargs.get("fastener_type", None),
                    style="form",
                    explode=False,
                ),
                "hangerType": oapi.client.format_argument_value(
                    "hangerType",
                    kwargs.get("hanger_type", None),
                    style="form",
                    explode=False,
                ),
                "hangtagType": oapi.client.format_argument_value(
                    "hangtagType",
                    kwargs.get("hangtag_type", None),
                    style="form",
                    explode=False,
                ),
                "partitionType": oapi.client.format_argument_value(
                    "partitionType",
                    kwargs.get("partition_type", None),
                    style="form",
                    explode=False,
                ),
                "shoebagType": oapi.client.format_argument_value(
                    "shoebagType",
                    kwargs.get("shoebag_type", None),
                    style="form",
                    explode=False,
                ),
                "shoeFormType": oapi.client.format_argument_value(
                    "shoeFormType",
                    kwargs.get("shoe_form_type", None),
                    style="form",
                    explode=False,
                ),
                "stickerType": oapi.client.format_argument_value(
                    "stickerType",
                    kwargs.get("sticker_type", None),
                    style="form",
                    explode=False,
                ),
                "tissueType": oapi.client.format_argument_value(
                    "tissueType",
                    kwargs.get("tissue_type", None),
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SearchResponse,
            )
        )

    def get_material_management_search_supplied_materials_distinct(
        self,
        distinct_fields: model.MaterialManagementSearchSuppliedMaterialsDistinctGetDistinctFields,  # noqa
        **kwargs: typing.Any,
    ) -> model.DistinctResponse:
        """
        How you search against all fields contained within the supplied
        material entity

        Parameters:

        - distinct_fields:
          This is a comma separated list of referenced or Identifier fields
          from the global offering service you wish to get distinct values for
          based on the search paramaters given. NOTE: Only referenced fields or
          Identifier fields are supported
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        - q:
          This parameter is how you pass free text search, if any string is
          passed here it will be searched as free text
        - material:
          The reference key associated with this item: Material Identifier
        - supplier_location:
          The reference key associated with this item: Supplier Location
          Identifier
        - supplier_material_number
        - material_name_variation_weight
        - material_name_variation_visual
        - manufacturing_countryof_origin:
          The reference key associated with this item: Manufacturing Country Of
          Origin
        - initial_season_cycle_year:
          The reference key associated with this item: Supplied Material
          Initial Season
        - target_season_cycle_year:
          The reference key associated with this item: Supplied Material Target
          Season
        - legacy_created_date
        - legacy_supplied_material_number
        - material_content_specification_number
        - supplied_material_state:
          The reference key associated with this item: Supplied Material State
          Identifier
        - supplied_material_status_indicator
        - material_library_locator_code
        - division:
          The reference key associated with this item: Supplied Material
          Division Code
        - supplied_material_development_team:
          The reference key associated with this item:
          suppliedMaterialDevelopmentTeam
        - physical_sample_available_indicator
        - physical_sample_date_added
        - pps_item_number
        - pps_submit_number
        - cross_approval_supplied_material:
          The reference key associated with this item: Cross Approval Supplied
          Material
        - approved_vendor_article_number
        - buy_ready_approver
        - buy_ready_date
        - expiration_date
        - duty_and_compliance:
          The reference key associated with this item: Duty and Compliance
        - primary_supplied_material_indicator
        - expiration_season_cycle_year:
          The reference key associated with this item: Expiration Season Year
        - cuttable_length_number
        - cuttable_length_uom:
          The reference key associated with this item: Supplied Material
          Cuttable Length UOM
        - cuttable_width_number
        - cuttable_width_uom:
          The reference key associated with this item: Supplied Material
          Cuttable Width UOM
        - material_length_number
        - material_length_uom:
          The reference key associated with this item: Supplied Material Length
          UOM
        - material_width_number
        - material_width_uom:
          The reference key associated with this item: Supplied Material Width
          UOM
        - initial_price:
          The number (float) for initialPrice
        - initial_price_uom:
          The reference key associated with this item: Initial Price UOM
        - patent
        - supplied_material_color_identifier
        - supplied_material_color_graphic_description
        - supplied_material_team_player_graphic_identifier
        - team_player_graphic_identifier
        - color:
          The reference key associated with this item: Supplied Material Color
          Identifier - Link to CM
        - supplied_material_color_graphic_primary_color:
          The reference key associated with this item: Supplied Material
          Primary Color Identifier - Link to CM
        - supplied_material_color_graphic_hue_identifier:
          The reference key associated with this item: Supplied Material
          Primary Hue Identifier
        - supplied_material_multi_color_code
        - supplied_material_color_is_multiple_colors
        - supplied_material_color_graphic_initial_cycle_year:
          The reference key associated with this item: Supplied Material Color
          Initial Season
        - supplied_material_color_graphic_status_indicator
        - supplied_material_color_graphic_state_identifier:
          The reference key associated with this item: Supplied Material Color
          State Identifier
        - create_timestamp:
          The reference key associated with this item: Supplied Material
          Created Timestamp
        - change_timestamp:
          The reference key associated with this item: Supplied Material Change
          Timestamp
        - parent_material_item_identifier:
          The reference key associated with this item: Material Level
          parentMaterialItemIdentifier
        - material_type:
          The reference key associated with this item: Material Type
        - material_item_name
        - customs_description:
          The reference key associated with this item: Material Level Customs
          Description
        - development_team:
          Material Level Development Team
        - core_material_name_variation_weight:
          Material Level Material Name Variation Weight
        - core_material_name_variation_visual:
          Material Level Material Name Variation Visual
        - target_price
        - target_price_uom:
          The reference key associated with this item: Material Level Target
          Price UOM
        - material_color_control_mode:
          The reference key associated with this item: Material Level Color
          Control Mode
        - material_pricing_mode:
          The reference key associated with this item: Material Level Pricing
          Mode
        - legacy_created_on_date:
          The reference key associated with this item: legacyCreatedOnDate
        - legacy_material_number:
          The reference key associated with this item: legacyMaterialNumber
        - apparel_pdm_material_number:
          The reference key associated with this item: apparelPDMMaterialNumber
        - material_development_team:
          The reference key associated with this item: Material Level
          Development Team
        - material_initial_category:
          The reference key associated with this item: Material Level Initial
          Category
        - material_initial_cycle_year:
          The reference key associated with this item: Material Level Initial
          Season
        - material_target_cycle_year:
          The reference key associated with this item: Material Level Target
          Season
        - material_item_status_indicator:
          The true or false flag associated with this item:
          materialItemStatusIndicator
        - material_bom_indicator:
          The true or false flag associated with this item:
          materialBOMIndicator
        - core_material_content_percentage:
          The number (float) for Material Level Content Percentage
        - core_material_content_type:
          The reference key associated with this item: Material Level Content
          Type
        - core_material_content_source:
          The reference key associated with this item: Material Level Content
          Source
        - core_material_family:
          The reference key associated with this item: Material Level Family
        - material_content_percentage:
          The number (float) for materialContentPercentage
        - material_content_type:
          The reference key associated with this item: materialContentType
        - material_content_source:
          The reference key associated with this item: materialContentSource
        - material_label_content_percentage:
          The number (float) for materialLabelContentPercentage
        - material_label_content_type:
          The reference key associated with this item: materialLabelContentType
        - material_label_content_source:
          The reference key associated with this item:
          materialLabelContentSource
        - material_family:
          The reference key associated with this item: materialFamily
        - material_owner:
          The reference key associated with this item: materialOwner
        - artwork_graphic:
          The reference key associated with this item: artworkGraphic
        - artwork_technique:
          The reference key associated with this item: artworkTechnique
        - secondary_process_indicator:
          The true or false flag associated with this item:
          secondaryProcessIndicator
        - artwork_application_location:
          The reference key associated with this item:
          artworkApplicationLocation
        - artwork_repeat_length_cm:
          The number (float) for artworkRepeatLengthCm
        - directional_pattern_indicator:
          The true or false flag associated with this item:
          directionalPatternIndicator
        - garment_location_placement:
          The value associated with this item: garmentLocationPlacement
        - end_use:
          The reference key associated with this item: endUse
        - development_reason:
          The reference key associated with this item: developmentReason
        - material_benefits:
          The reference key associated with this item: materialBenefits
        - fabric_face_designation:
          The reference key associated with this item: fabricFaceDesignation
        - stretch_direction:
          The reference key associated with this item: stretchDirection
        - vendor_special_care_instructions:
          The reference key associated with this item:
          vendorSpecialCareInstructions
        - consideration_and_risks:
          The reference key associated with this item: considerationAndRisks
        - thickness_mm:
          The number (float) for thicknessMm
        - thickness_selection:
          The reference key associated with this item: thicknessSelection
        - maximum_thickness_mm:
          The number (float) for maximumThicknessMm
        - minimum_thickness_mm:
          The number (float) for maximumThicknessMm
        - length_mm:
          The number (float) for lengthMm
        - length_cm:
          The number (float) for lengthCm
        - dimension_width_indicator:
          The reference key associated with this item: dimensionWidthIndicator
        - width_mm:
          The number (float) for widthMm
        - width_cm:
          The number (float) for widthCm
        - height_mm:
          The number (float) for heightMm
        - height_cm:
          The number (float) for heightCm
        - weight_grams_per_square_meter:
          The number (float) for weightGramsPerSquareMeter
        - external_diameter_mm:
          The number (float) for externalDiameterMm
        - external_length_mm:
          The number (float) for externalLengthMm
        - external_width_mm:
          The number (float) for externalWidthMm
        - internal_diameter_mm:
          The number (float) for internalDiameterMm
        - internal_length_mm:
          The number (float) for internalLengthMm
        - internal_width_mm:
          The number (float) for internalWidthMm
        - gauge_inch:
          The number (float) for gaugeInch
        - grams_per_thousand_pieces:
          The number (float) for gramsPerThousandPieces
        - weight_grams_per_thousand_pieces:
          Weight (grams per 1000 pieces)
        - weight_grams_per_linear_yard:
          Weight (grams per linear yard)
        - weight_grams_per_linear_meter:
          Weight (grams per linear meter)
        - yarn_composition_content_percentage:
          The number (float) for yarnCompositionContentPercentage
        - yarn_composition_content_type:
          The reference key associated with this item:
          yarnCompositionContentType
        - yarn_composition_content_source:
          The reference key associated with this item:
          yarnCompositionContentSource
        - yarn_composition_location:
          The reference key associated with this item: yarnCompositionLocation
        - yarn_composition_type:
          The reference key associated with this item: yarnCompositionType
        - yarn_composition_size:
          The number (float) for yarnCompositionSize
        - yarn_composition_spinning_method:
          The reference key associated with this item:
          yarnCompositionSpinningMethod
        - yarn_composition_count:
          The The number (integer) for yarnCompositionCount
        - yarn_composition_preparation:
          The reference key associated with this item:
          yarnCompositionPreparation
        - yarn_composition_cross_section:
          The reference key associated with this item:
          yarnCompositionCrossSection
        - yarn_composition_filament_count:
          The number (integer) for yarnCompositionFilamentCount
        - yarn_composition_number_system:
          The reference key associated with this item:
          yarnCompositionNumberSystem
        - yarn_composition_luster:
          The reference key associated with this item: yarnCompositionLuster
        - yarn_composition_brand:
          The reference key associated with this item: yarnCompositionBrand
        - yarn_composition_texture:
          The reference key associated with this item: yarnCompositionTexture
        - yarn_composition_twist:
          The reference key associated with this item: yarnCompositionTwist
        - yarn_composition_finish_process:
          The reference key associated with this item:
          yarnCompositionFinishProcess
        - yarn_composition_dye_method:
          The reference key associated with this item: yarnCompositionDyeMethod
        - yarn_composition_visual_effect:
          The reference key associated with this item:
          yarnCompositionVisualEffect
        - yarn_composition_fixed_color:
          The reference key associated with this item:
          yarnCompositionFixedColor
        - yarn_composition_usage_percentage:
          The number (float) for yarnCompositionUsagePercentage
        - ply_content_percentage:
          The number (float) for plyContentPercentage
        - ply_content_type:
          The reference key associated with this item: plyContentType
        - ply_content_source:
          The reference key associated with this item: plyContentSource
        - ply_location:
          The reference key associated with this item: plyLocation
        - ply_type:
          The reference key associated with this item: plyType
        - ply_brand:
          The reference key associated with this item: plyBrand
        - ply_size:
          The number (float) for plySize
        - ply_number_system:
          The reference key associated with this item: plyNumberSystem
        - ply_cross_section:
          The reference key associated with this item: plyCrossSection
        - ply_spinning_method:
          The reference key associated with this item: plySpinningMethod
        - ply_filament_count:
          The number (integer) for plyFilamentCount
        - ply_twist:
          The reference key associated with this item: plyTwist
        - ply_luster:
          The reference key associated with this item: plyLuster
        - ply_texture:
          The reference key associated with this item: plyTexture
        - ply_finish_process:
          The reference key associated with this item: plyFinishProcess
        - ply_dye_method:
          The reference key associated with this item: plyDyeMethod
        - ply_visual_effect:
          The reference key associated with this item: plyVisualEffect
        - ply_fixed_color:
          The reference key associated with this item: plyFixedColor
        - ply_usage_percentage:
          The number (float) for plyUsagePercentage
        - fiber_content_percentage:
          The number (float) for fiberContentPercentage
        - fiber_content_type:
          The reference key associated with this item: fiberContentType
        - fiber_content_source:
          The reference key associated with this item: fiberContentSource
        - fiber_size:
          The number (float) for fiberSize
        - fiber_ply_location:
          The reference key associated with this item: fiberPlyLocation
        - fiber_staple_number_system:
          The reference key associated with this item: fiberStapleNumberSystem
        - fiber_staple_length:
          The number (float) for fiberStapleLength
        - fiber_staple_length_min:
          The number (float) for fiberStapleLengthMin
        - fiber_staple_length_max:
          The number (float) for fiberStapleLengthMax
        - fiber_diameter:
          The number (float) for fiberDiameter
        - fiber_diameter_min:
          The number (float) for fiberDiameterMin
        - fiber_diameter_max:
          The number (float) for fiberDiameterMax
        - fiber_diameter_unit:
          The reference key associated with this item: fiberDiameterUnit
        - fiber_preparation:
          The reference key associated with this item: fiberPreparation
        - fiber_cross_section:
          The reference key associated with this item: fiberCrossSection
        - fiber_luster:
          The reference key associated with this item: fiberLuster
        - fiber_finish_process:
          The reference key associated with this item: fiberFinishProcess
        - fiber_dye_method:
          The reference key associated with this item: fiberDyeMethod
        - fiber_usage_percentage:
          The number (float) for fiberUsagePercentage
        - edge_finish:
          The reference key associated with this item: edgeFinish
        - visual_effect:
          The reference key associated with this item: visualEffect
        - visual_effect_location:
          The reference key associated with this item: visualEffectLocation
        - print_code:
          The reference key associated with this item: printCode
        - emboss_code_text:
          Emboss Code Text
        - application_technique:
          The reference key associated with this item: applicationTechnique
        - finish_process:
          The reference key associated with this item: finishProcess
        - finish_location:
          The reference key associated with this item: finishLocation
        - number_of_passes:
          The number (integer) for numberOfPasses
        - material_technologies:
          The reference key associated with this item: materialTechnology
        - release_paper_code:
          The code associated with this item: releasePaperCode
        - release_paper_one:
          The material Id for releasePaperOne
        - release_paper_two:
          The material Id for releasePaperTwo
        - release_paper_side_one:
          The reference key associated with this item: releasePaperSideOne
        - release_paper_side_two:
          The reference key associated with this item: releasePaperSideTwo
        - release_paper_finish_process:
          The reference key associated with this item:
          releasePaperFinishProcess
        - top_layer_material_item:
          The material Id for topLayerMaterialItem
        - middle_layer_1_material_item:
          The material Id for middleLayer1MaterialItem
        - middle_layer_2_material_item:
          The material Id for middleLayer2MaterialItem
        - middle_layer_3_material_item:
          The material Id for middleLayer3MaterialItem
        - bottom_layer_material_item:
          The material Id for bottomLayerMaterialItem
        - non_woven_substrate_type:
          The reference key associated with this item: nonWovenSubstrateType
        - non_woven_web_bonding_method:
          The reference key associated with this item: nonWovenWebBondingMethod
        - color_dominance:
          The reference key associated with this item: colorDominance
        - color_effect:
          The reference key associated with this item: colorEffect
        - color_position:
          The reference key associated with this item: colorPosition
        - color_location:
          The reference key associated with this item: colorLocation
        - color_callout:
          The reference key associated with this item: colorCallout
        - color_fiber:
          The reference key associated with this item: colorFiber
        - dye_method:
          The reference key associated with this item: dyeMethod
        - dye_type:
          The reference key associated with this item: dyeType
        - active_category:
          The reference key associated with this item: activeCategory
        - active_cycle_year:
          The reference key associated with this item: activeCycleYear
        - web_formation:
          The reference key associated with this item: webFormation
        - number_of_colors:
          The reference key associated with this item: numberOfColors
        - last_identifier:
          The last identifier
        - outsourced_process:
          The reference key associated with this item: outsourcedProcess
        - perf_code:
          The coode associated with this item: perfCode
        - animal_source:
          The reference key associated with this item: animalSource
        - dyed_through_crust_indicator:
          The true or false flag associated with this item:
          dyedThroughCrustIndicator
        - oil_content:
          The reference key associated with this item: oilContent
        - re_tannage:
          The reference key associated with this item: reTannage
        - washable_indicator:
          The true or false flag associated with this item: washableIndicator
        - composition_leather_type:
          The reference key associated with this item: compositionLeatherType
        - animal_source_country_of_origin:
          The reference key associated with this item: Animal Source Country of
          Origin
        - satrasumm_qc:
          The reference key associated with this item: Satrasumm QC
        - grain_leather_type:
          The reference key associated with this item: grainLeatherType
        - grain_leather_sub_type:
          The reference key associated with this item: grainLeatherSubType
        - split_leather_type:
          The reference key associated with this item: splitLeatherType
        - average_pu_thickness:
          The number (float) for averagePUThickness
        - coating_thickness_mm:
          The number (float) for coatingThicknessMm
        - moldable:
          The reference key associated with this item: moldable
        - substrate_processing_type:
          The reference key associated with this item: substrateProcessingType
        - substrate_pu_dipped_indicator:
          The true or false flag associated with this item:
          substratePUDippedIndicator
        - substrate_construction:
          The reference key associated with this item: substrateConstruction
        - textile_construction_type:
          The reference key associated with this item: textileConstructionType
        - textile_sub_variation:
          The reference key associated with this item: textileSubVariation
        - textile_sub_variation_two:
          The reference key associated with this item: textileSubVariationTwo
        - textile_variation:
          The reference key associated with this item: textileVariation
        - ends_per_inch_number:
          The number of endsPerInchNumber
        - picks_per_inch_number:
          The number of picksPerInchNumber
        - machinery_type:
          The reference key associated with this item: machineryType
        - warp_count:
          The number of warpCount
        - weft_count:
          The number of weftCount
        - twill_construction_type:
          The reference key associated with this item: twillConstructionType
        - twill_direction:
          The reference key associated with this item: twillDirection
        - fold_indicator:
          The true or false flag associated with this item: foldIndicator
        - rib_construction:
          The reference key associated with this item: ribConstruction
        - height_indicator:
          The reference key associated with this item: heightIndicator
        - rows_of_spandex:
          The number of rowsOfSpandex
        - part_type_orientation:
          The reference key associated with this item: partTypeOrientation
        - initial_development_product_alias:
          The string value associated with this item:
          initialDevelopmentProductAlias
        - pre_twist_yarn:
          The reference key associated with this item: preTwistYarn
        - program:
          The reference key associated with this item: programIdentifier
        - steam_method:
          The reference key associated with this item: steamMethod
        - design_patent_number
        - utility_patent_number
        - development_defect_rate
        - negotiated_defect_rate
        - run_time_minutes
        - gate:
          The reference key associated with this item: Program Gate
        - structure_testing_reference:
          The reference key associated with this item:
          structureTestingReference
        - structure_reference_number:
          The reference key associated with this item: structureReferenceNumber
        - structure_coverage:
          The reference key associated with this item: structureCoverage
        - blanket_number:
          The reference key associated with this item: blanketNumber
        - yarn_size:
          The number (float) of yarnSize
        - yarn_spinning_method:
          The reference key associated with this item: yarnSpinningMethod
        - all_plys_the_same_indicator:
          The true or false flag associated with this item:
          allPlysTheSameIndicator
        - fancy_yarn:
          The reference key associated with this item: fancyYarn
        - fixed_color:
          The reference key associated with this item: fixedColor
        - yarn_brand:
          The reference key associated with this item: yarnBrand
        - yarn_number_system:
          The reference key associated with this item: yarnNumberSystem
        - yarn_twist:
          The reference key associated with this item: yarnTwist
        - yarn_ply_count:
          The number of yarnPlyCount
        - yarn_type:
          The reference key associated with this item: yarnType
        - yarn_luster:
          The reference key associated with this item: yarnLuster
        - yarn_finish_process:
          The reference key associated with this item: yarnFinishProcess
        - yarn_dye_method:
          The reference key associated with this item: yarnDyeMethod
        - yarn_visual_effect:
          The reference key associated with this item: yarnVisualEffect
        - yarn_number_of_ends:
          The number of yarnNumberOfEnds
        - yarn_filament_count:
          The number of yarnFilamentCount
        - yarn_covering_method:
          The reference key associated with this item: yarnCoveringMethod
        - yarn_texture:
          The reference key associated with this item: yarnTexture
        - microfiber_indicator:
          The true or false flag associated with this item: microfiberIndicator
        - yarn_preparation:
          The reference key associated with this item: yarnPreparation
        - yarn_cross_section:
          The reference key associated with this item: yarnCrossSection
        - yarn_location:
          The reference key associated with this item: yarnLocation
        - yarn_supplied_material:
          The reference key associated with this item: yarnSuppliedMaterial
        - yarn_supplied_material_number_of_ends:
          The integer for yarnSuppliedMaterialNumberOfEnds
        - yarn_usage_percentage:
          The number (float) for yarnUsagePercentage
        - base_type:
          The reference key associated with this item: baseType
        - single_component_indicator:
          The reference key associated with this item: singleComponentIndicator
        - flammability_rating:
          The reference key associated with this item: flammabilityRating
        - hotmelt_type:
          The reference key associated with this item: hotmeltType
        - hydrolysis_resistant_indicator:
          The true or false flag associated with this item:
          hydrolysisResistantIndicator
        - method_of_make:
          The reference key associated with this item: methodOfMake
        - chem_poly_form:
          The reference key associated with this item: chemPolyForm
        - film_type:
          The reference key associated with this item: filmType
        - hotmelt_material_item:
          The reference key associated with this item: Hotmelt Material
          Identifier
        - hotmelt_thickness_number_mm:
          The number (float) for hotmeltThicknessNumberMm
        - opacity:
          The reference key associated with this item: opacity
        - stretch_indicator:
          The true or false flag associated with this item: stretchIndicator
        - carrier_paper_statement:
          The reference key associated with this item: carrierPaperStatement
        - foam_type:
          The reference key associated with this item: foamType
        - polyurethane_chemistry:
          The reference key associated with this item: polyurethaneChemistry
        - hardness_asker_c:
          The reference key associated with this item: hardnessAskerC
        - firmness:
          The reference key associated with this item: firmness
        - melting_point_number:
          The number (float) for meltingPointNumber
        - plastic_type:
          The reference key associated with this item: plasticType
        - plastic_sub_type:
          The reference key associated with this item: plasticSubType
        - ultraviolet_inhibitor_indicator:
          The true or false flag associated with this item:
          ultravioletInhibitorIndicator
        - clear_rubber_indicator:
          The true or false flag associated with this item:
          clearRubberIndicator
        - cure_process:
          The reference key associated with this item: cureProcess
        - regrind_content_percentage:
          The number (float) for regrindContentPercentage
        - sport_activity:
          The reference key associated with this item: sportActivity
        - detachable_metal_indicator:
          The true or false flag associated with this item:
          detachableMetalIndicator
        - hard_or_soft_component:
          The reference key associated with this item: hardOrSoftComponent
        - stock_or_custom:
          The reference key associated with this item: stockOrCustom
        - core_construction_type:
          The reference key associated with this item: coreConstructionType
        - component_construction_type:
          The reference key associated with this item:
          componentConstructionType
        - has_core_indicator:
          The true or false flag associated with this item: hasCoreIndicator
        - shape:
          The reference key associated with this item: shape
        - logo_type:
          The reference key associated with this item: logoType
        - logo_name:
          The reference key associated with this item: logoName
        - logo_placement:
          The reference key associated with this item: logoPlacement
        - hotmelt_included_indicator:
          The true or false flag associated with this item:
          hotmeltIncludedIndicator
        - elasticized_indicator:
          The true or false flag associated with this item:
          elasticizedIndicator
        - vendor_color_card_only_indicator:
          The true or false flag associated with this item:
          vendorColorCardOnlyIndicator
        - component_form:
          The reference key associated with this item: componentForm
        - ligne_size_number:
          The number (float) for ligneSizeNumber
        - number_of_holes:
          The number for numberOfHoles
        - adhesive_type:
          The reference key associated with this item: adhesiveType
        - gripper_type:
          The reference key associated with this item: gripperType
        - number_of_gripper_rows:
          The number for numberOfGripperRows
        - end_finish:
          The reference key associated with this item: endFinish
        - for_product_sizes:
          The reference key associated with this item: forProductSizes
        - part_type:
          The reference key associated with this item: partType
        - number_of_rows:
          The number for numberOfRows
        - amount_per_row:
          The number for amountPerRow
        - adjuster_type:
          The reference key associated with this item: adjusterType
        - contains_magnet_indicator:
          The true or false flag associated with this item:
          containsMagnetIndicator
        - button_type:
          The reference key associated with this item: buttonType
        - tape_type:
          The reference key associated with this item: tapeType
        - snap_type:
          The reference key associated with this item: snapType
        - snap_part_type:
          The reference key associated with this item: snapPartType
        - tape_width_mm:
          The number (float) for tapeWidthMm
        - snap_width_mm:
          The number (float) for snapWidthMm
        - snap_repeat_length_mm:
          The number (float) for snapRepeatLengthMm
        - cordlock_toggle_type:
          The reference key associated with this item: cordlockToggleType
        - activation_temperature_number:
          The number (float) for activationTemperatureNumber
        - counter_type:
          The reference key associated with this item: counterType
        - dwell_time:
          The reference key associated with this item: dwellTime
        - general_construction:
          The reference key associated with this item: generalConstruction
        - elastic_type:
          The reference key associated with this item: elasticType
        - crossover_drawcord_indicator:
          The true or false flag associated with this item:
          crossoverDrawcordIndicator
        - elastic_drawcord_content_percentage:
          The number (float) for elasticDrawcordContentPercentage
        - elastic_drawcord_content_type:
          The reference key associated with this item:
          elasticDrawcordContentType
        - elastic_drawcord_content_source:
          The reference key associated with this item:
          elasticDrawcordContentSource
        - elastic_drawcord_aglet_material_item:
          The reference key associated with this item:
          elasticDrawcordAgletMaterialItem
        - elastic_drawcord_has_core_indicator:
          The true or false flag associated with this item:
          elasticDrawcordHasCoreIndicator
        - elastic_drawcord_elasticized_indicator:
          The true or false flag associated with this item:
          elasticDrawcordElasticizedIndicator
        - elastic_drawcord_shape:
          The reference key associated with this item: elasticDrawcordShape
        - elastic_drawcord_logo_name:
          The reference key associated with this item: elasticDrawcordLogoName
        - elastic_drawcord_dimension_width_indicator:
          The reference key associated with this item:
          elasticDrawcordDimensionWidthIndicator
        - elastic_drawcord_gripper_type:
          The reference key associated with this item:
          elasticDrawcordGripperType
        - elastic_drawcord_construction_type:
          The reference key associated with this item:
          elasticDrawcordConstructionType
        - elastic_drawcord_form:
          The reference key associated with this item: elasticDrawcordForm
        - elastic_drawcord_end_finish:
          The reference key associated with this item: elasticDrawcordEndFinish
        - elastic_drawcord_width_mm:
          The number (float) for elasticDrawcordWidthMm
        - elastic_drawcord_finish_process:
          The reference key associated with this item:
          elasticDrawcordFinishProcess
        - elastic_drawcord_dye_method:
          The reference key associated with this item: elasticDrawcordDyeMethod
        - elastic_drawcord_artwork_technique:
          The reference key associated with this item:
          elasticDrawcordArtworkTechnique
        - elastic_drawcord_visual_effect:
          The reference key associated with this item:
          elasticDrawcordVisualEffect
        - elastic_drawcord_number_of_colors:
          he reference key associated with this item:
          elasticDrawcordNumberOfColors
        - elastic_aglet_content_percentage:
          The number (float) for elasticAgletContentPercentage
        - elastic_aglet_content_type:
          The reference key associated with this item: elasticAgletContentType
        - elastic_aglet_content_source:
          The reference key associated with this item:
          elasticAgletContentSource
        - elastic_aglet_logo_name:
          The reference key associated with this item: elasticAgletLogoName
        - elastic_aglet_shape:
          The reference key associated with this item: elasticAgletShape
        - elastic_aglet_construction_type:
          The reference key associated with this item:
          elasticAgletConstructionType
        - elastic_aglet_width_mm:
          The number (float) for elasticAgletWidthMm
        - elastic_aglet_height_mm:
          The number (float) for elasticAgletHeightMm
        - elastic_aglet_internal_diameter_mm:
          The number (float) for elasticAgletInternalDiameterMm
        - elastic_aglet_grams_per_thousand_pieces:
          The number (float) for elasticAgletGramsPerThousandPieces
        - elastic_aglet_finish_process:
          The reference key associated with this item:
          elasticAgletFinishProcess
        - elastic_aglet_dye_method:
          The reference key associated with this item: elasticAgletDyeMethod
        - elastic_aglet_artwork_technique:
          The reference key associated with this item:
          elasticAgletArtworkTechnique
        - elastic_aglet_visual_effect:
          The reference key associated with this item: elasticAgletVisualEffect
        - elastic_aglet_number_of_colors:
          he reference key associated with this item:
          elasticAgletNumberOfColors
        - drawcord_material_item:
          The reference key associated with this item: drawcordMaterialItem
        - drawcord_aglet_material_item:
          The reference key associated with this item:
          drawcordAgletMaterialItem
        - drawcord_aglet_content_percentage:
          The number (float) for drawcordAgletContentPercentage
        - drawcord_aglet_content_type:
          The reference key associated with this item: drawcordAgletContentType
        - drawcord_aglet_content_source:
          The reference key associated with this item:
          drawcordAgletContentSource
        - drawcord_aglet_logo_name:
          The reference key associated with this item: drawcordAgletLogoName
        - drawcord_aglet_shape:
          The reference key associated with this item: drawcordAgletShape
        - drawcord_aglet_construction_type:
          The reference key associated with this item:
          drawcordAgletConstructionType
        - drawcord_aglet_width_mm:
          The number (float) for drawcordAgletWidthMm
        - drawcord_aglet_height_mm:
          The number (float) for drawcordAgletHeightMm
        - drawcord_aglet_internal_diameter_mm:
          The number (float) for drawcordAgletInternalDiameterMm
        - drawcord_aglet_grams_per_thousand_pieces:
          The number (float) for drawcordAgletGramsPerThousandPieces
        - drawcord_aglet_finish_process:
          The reference key associated with this item:
          drawcordAgletFinishProcess
        - drawcord_aglet_dye_method:
          The reference key associated with this item: drawcordAgletDyeMethod
        - drawcord_aglet_artwork_technique:
          The reference key associated with this item:
          drawcordAgletArtworkTechnique
        - drawcord_aglet_visual_effect:
          The reference key associated with this item:
          drawcordAgletVisualEffect
        - drawcord_aglet_number_of_colors:
          he reference key associated with this item:
          drawcordAgletNumberOfColors
        - hook_type:
          The reference key associated with this item: hookType
        - hook_loop_type:
          The reference key associated with this item: hookLoopType
        - label_type:
          The reference key associated with this item: labelType
        - fold_method:
          The reference key associated with this item: foldMethod
        - label_twill_direction:
          The reference key associated with this item: labelTwillDirection
        - backing_type:
          The reference key associated with this item: backingType
        - logo_size:
          The reference key associated with this item: logoSize
        - aglet_material_item:
          The reference key associated with this item: agletMaterialItem
        - has_aglet_indicator:
          The true or false flag associated with this item: hasAgletIndicator
        - number_of_bundles:
          The number for numberOfBundles
        - tip_content:
          The reference key associated with this item: tipContent
        - tip_type:
          The reference key associated with this item: tipType
        - magnet_cover_type:
          The reference key associated with this item: magnetCoverType
        - padding_type:
          The reference key associated with this item: paddingType
        - padding_orientation:
          The reference key associated with this item: paddingOrientation
        - layer_location:
          The reference key associated with this item: layerLocation
        - material_construction:
          The reference key associated with this item: materialConstruction
        - layer_finish_process:
          The reference key associated with this item: layerFinishProcess
        - layer_artwork_technique:
          The reference key associated with this item: layerArtworkTechnique
        - layer_content_percentage:
          The number (float) for layerContentPercentage
        - layer_content_type:
          The reference key associated with this item: layerContentType
        - layer_content_source:
          The reference key associated with this item: layerContentSource
        - pin_badge_type:
          The reference key associated with this item: pinBadgeType
        - plate_orientation:
          The reference key associated with this item: plateOrientation
        - mold_identifier:
          The reference key associated with this item: moldIdentifier
        - ring_type:
          The reference key associated with this item: ringType
        - bonded_indicator:
          The true or false flag associated with this item: bondedIndicator
        - lubricated_indicator:
          The true or false flag associated with this item: lubricatedIndicator
        - thread_ply:
          The number of threadPly
        - thread_size:
          The number (float) for threadSize
        - alternate_thread_size:
          The number (float) for alternateThreadSize
        - thread_type:
          The reference key associated with this item: threadType
        - thread_brand_name:
          The reference key associated with this item: threadBrandName
        - thread_number_system:
          The reference key associated with this item: threadNumberSystem
        - thread_preparation:
          The reference key associated with this item: threadPreparation
        - thread_filament_count:
          The number for threadFilamentCount
        - thread_ply_count:
          The number for threadPlyCount
        - thread_luster:
          The reference key associated with this item: threadLuster
        - thread_statement_content:
          The reference key associated with this item: threadStatementContent
        - zipper_type:
          The reference key associated with this item: zipperType
        - zip_in_compatible_indicator:
          The true or false flag associated with this item:
          zipInCompatibleIndicator
        - zipper_performance:
          The reference key associated with this item: zipperPerformance
        - zipper_brand:
          The reference key associated with this item: zipperBrand
        - slider_pull_logo_name:
          The reference key associated with this item: sliderPullLogoName
        - slider_locking_function:
          The reference key associated with this item: sliderLockingFunction
        - slider_quantity:
          The number for sliderQuantity
        - slider_orientation:
          The reference key associated with this item: sliderOrientation
        - slider_visual_effect:
          The reference key associated with this item: sliderVisualEffect
        - slider_pull_finish_process:
          The reference key associated with this item: sliderPullFinishProcess
        - slider_pull_artwork_technique:
          The reference key associated with this item:
          sliderPullArtworkTechnique
        - zipper_pull_code:
          The reference key associated with this item: zipperPullCode
        - zipper_tape_construction_type:
          The reference key associated with this item:
          zipperTapeConstructionType
        - zipper_tape_logo_name:
          The reference key associated with this item: zipperTapeLogoName
        - zipper_tape_width_mm:
          The number (float) for zipperTapeWidthMm
        - zipper_tape_finish_process:
          The reference key associated with this item: zipperTapeFinishProcess
        - zipper_tape_dye_method:
          The reference key associated with this item: zipperTapeDyeMethod
        - zipper_tape_artwork_technique:
          The reference key associated with this item:
          zipperTapeArtworkTechnique
        - zipper_tape_artwork_graphic:
          The reference key associated with this item: zipperTapeArtworkGraphic
        - zipper_tape_visual_effect:
          The reference key associated with this item: zipperTapeVisualEffect
        - teeth_type:
          The reference key associated with this item: teethType
        - special_zipper_teeth_orientation:
          The reference key associated with this item:
          specialZipperTeethOrientation
        - teeth_size:
          The reference key associated with this item: teethSize
        - teeth_shape:
          The reference key associated with this item: teethShape
        - teeth_repeat_length_mm:
          The number (float) for teethRepeatLengthMm
        - teeth_finish_process:
          The reference key associated with this item: teethFinishProcess
        - teeth_artwork_technique:
          The reference key associated with this item: teethArtworkTechnique
        - teeth_visual_effect:
          The reference key associated with this item: teethVisualEffect
        - contrast_thread_for_coil_indicator:
          The true or false flag associated with this item:
          contrastThreadForCoilIndicator
        - teeth_multi_colored_indicator:
          The true or false flag associated with this item:
          teethMultiColoredIndicator
        - zipper_stop_type:
          The reference key associated with this item: zipperStopType
        - zipper_stop_logo_name:
          The reference key associated with this item: zipperStopLogoName
        - zipper_stop_logo_placement:
          The reference key associated with this item: zipperStopLogoPlacement
        - aglet_construction_type:
          The reference key associated with this item: agletConstructionType
        - airbag_process:
          The reference key associated with this item: airbagProcess
        - airbag_type:
          The reference key associated with this item: airbagType
        - coloration_available:
          The reference key associated with this item: colorationAvailable
        - gas_content:
          The reference key associated with this item: gasContent
        - fill_type:
          The reference key associated with this item: fillType
        - scrim:
          The reference key associated with this item: scrim
        - down_cluster_statement:
          The reference key associated with this item: downClusterStatement
        - fill_power:
          The number for fillPower
        - natural_down_color:
          The reference key associated with this item: naturalDownColor
        - fill_form:
          The reference key associated with this item: fillForm
        - heat_set:
          The reference key associated with this item: heatSet
        - vendor_supplied_indicator:
          The true or false flag associated with this item:
          vendorSuppliedIndicator
        - corporate_designation_indicator:
          The true or false flag associated with this item:
          corporateDesignationIndicator
        - confidential_indicator:
          The true or false flag associated with this item:
          confidentialIndicator
        - country_of_origin_statement_indicator:
          The true or false flag associated with this item:
          countryOfOriginStatementIndicator
        - size_matrix_indicator:
          The true or false flag associated with this item: sizeMatrixIndicator
        - contains_corporate_logo_indicator:
          The true or false flag associated with this item:
          containsCorporateLogoIndicator
        - packaging_intent:
          The reference key associated with this item: packagingIntent
        - packaging_statement:
          The reference key associated with this item: packagingStatement
        - card_type:
          The reference key associated with this item: cardType
        - card_construction_type:
          The reference key associated with this item: cardConstructionType
        - fluting_size:
          The reference key associated with this item: flutingSize
        - inner_linerboard_basis_weight:
          The number innerLinerboardBasisWeight
        - inner_linerboard_type:
          The reference key associated with this item: innerLinerboardType
        - medium_paper_basis_weight:
          The the number for mediumPaperBasisWeight
        - medium_paper_type:
          The reference key associated with this item: mediumPaperType
        - outer_linerboard_basis_weight:
          The number for outerLinerboardBasisWeight
        - outer_linerboard_type:
          The reference key associated with this item: outerLinerboardType
        - fastener_type:
          The reference key associated with this item: fastenerType
        - hanger_type:
          The reference key associated with this item: hangerType
        - hangtag_type:
          The reference key associated with this item: hangtagType
        - partition_type:
          The reference key associated with this item: partitionType
        - shoebag_type:
          The reference key associated with this item: shoebagType
        - shoe_form_type:
          The reference key associated with this item: shoeFormType
        - sticker_type:
          The reference key associated with this item: stickerType
        - tissue_type:
          The reference key associated with this item: tissueType
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/search/suppliedMaterials/distinct",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    kwargs.get("x_b_3_trace_id", None),
                    style="form",
                    explode=False,
                ),
            },
            query={
                "distinctFields": oapi.client.format_argument_value(
                    "distinctFields",
                    kwargs.get("distinct_fields", None),
                    style="form",
                    explode=False,
                ),
                "q": oapi.client.format_argument_value(
                    "q",
                    kwargs.get("q", ""),
                    style="form",
                    explode=False,
                ),
                "material": oapi.client.format_argument_value(
                    "material",
                    kwargs.get("material", None),
                    style="form",
                    explode=False,
                ),
                "supplierLocation": oapi.client.format_argument_value(
                    "supplierLocation",
                    kwargs.get("supplier_location", None),
                    style="form",
                    explode=False,
                ),
                "supplierMaterialNumber": oapi.client.format_argument_value(
                    "supplierMaterialNumber",
                    kwargs.get("supplier_material_number", None),
                    style="form",
                    explode=False,
                ),
                "materialNameVariationWeight": oapi.client.format_argument_value(  # noqa
                    "materialNameVariationWeight",
                    kwargs.get("material_name_variation_weight", None),
                    style="form",
                    explode=False,
                ),
                "materialNameVariationVisual": oapi.client.format_argument_value(  # noqa
                    "materialNameVariationVisual",
                    kwargs.get("material_name_variation_visual", None),
                    style="form",
                    explode=False,
                ),
                "manufacturingCountryofOrigin": oapi.client.format_argument_value(  # noqa
                    "manufacturingCountryofOrigin",
                    kwargs.get("manufacturing_countryof_origin", None),
                    style="form",
                    explode=False,
                ),
                "initialSeasonCycleYear": oapi.client.format_argument_value(
                    "initialSeasonCycleYear",
                    kwargs.get("initial_season_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "targetSeasonCycleYear": oapi.client.format_argument_value(
                    "targetSeasonCycleYear",
                    kwargs.get("target_season_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "legacyCreatedDate": oapi.client.format_argument_value(
                    "legacyCreatedDate",
                    kwargs.get("legacy_created_date", None),
                    style="form",
                    explode=False,
                ),
                "legacySuppliedMaterialNumber": oapi.client.format_argument_value(  # noqa
                    "legacySuppliedMaterialNumber",
                    kwargs.get("legacy_supplied_material_number", None),
                    style="form",
                    explode=False,
                ),
                "materialContentSpecificationNumber": oapi.client.format_argument_value(  # noqa
                    "materialContentSpecificationNumber",
                    kwargs.get("material_content_specification_number", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialState": oapi.client.format_argument_value(
                    "suppliedMaterialState",
                    kwargs.get("supplied_material_state", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialStatusIndicator",
                    kwargs.get("supplied_material_status_indicator", None),
                    style="form",
                    explode=False,
                ),
                "materialLibraryLocatorCode": oapi.client.format_argument_value(  # noqa
                    "materialLibraryLocatorCode",
                    kwargs.get("material_library_locator_code", None),
                    style="form",
                    explode=False,
                ),
                "division": oapi.client.format_argument_value(
                    "division",
                    kwargs.get("division", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialDevelopmentTeam": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialDevelopmentTeam",
                    kwargs.get("supplied_material_development_team", None),
                    style="form",
                    explode=False,
                ),
                "physicalSampleAvailableIndicator": oapi.client.format_argument_value(  # noqa
                    "physicalSampleAvailableIndicator",
                    kwargs.get("physical_sample_available_indicator", None),
                    style="form",
                    explode=False,
                ),
                "physicalSampleDateAdded": oapi.client.format_argument_value(
                    "physicalSampleDateAdded",
                    kwargs.get("physical_sample_date_added", None),
                    style="form",
                    explode=False,
                ),
                "ppsItemNumber": oapi.client.format_argument_value(
                    "ppsItemNumber",
                    kwargs.get("pps_item_number", None),
                    style="form",
                    explode=False,
                ),
                "ppsSubmitNumber": oapi.client.format_argument_value(
                    "ppsSubmitNumber",
                    kwargs.get("pps_submit_number", None),
                    style="form",
                    explode=False,
                ),
                "crossApprovalSuppliedMaterial": oapi.client.format_argument_value(  # noqa
                    "crossApprovalSuppliedMaterial",
                    kwargs.get("cross_approval_supplied_material", None),
                    style="form",
                    explode=False,
                ),
                "approvedVendorArticleNumber": oapi.client.format_argument_value(  # noqa
                    "approvedVendorArticleNumber",
                    kwargs.get("approved_vendor_article_number", None),
                    style="form",
                    explode=False,
                ),
                "buyReadyApprover": oapi.client.format_argument_value(
                    "buyReadyApprover",
                    kwargs.get("buy_ready_approver", None),
                    style="form",
                    explode=False,
                ),
                "buyReadyDate": oapi.client.format_argument_value(
                    "buyReadyDate",
                    kwargs.get("buy_ready_date", None),
                    style="form",
                    explode=False,
                ),
                "expirationDate": oapi.client.format_argument_value(
                    "expirationDate",
                    kwargs.get("expiration_date", None),
                    style="form",
                    explode=False,
                ),
                "dutyAndCompliance": oapi.client.format_argument_value(
                    "dutyAndCompliance",
                    kwargs.get("duty_and_compliance", None),
                    style="form",
                    explode=False,
                ),
                "primarySuppliedMaterialIndicator": oapi.client.format_argument_value(  # noqa
                    "primarySuppliedMaterialIndicator",
                    kwargs.get("primary_supplied_material_indicator", None),
                    style="form",
                    explode=False,
                ),
                "expirationSeasonCycleYear": oapi.client.format_argument_value(
                    "expirationSeasonCycleYear",
                    kwargs.get("expiration_season_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "cuttableLengthNumber": oapi.client.format_argument_value(
                    "cuttableLengthNumber",
                    kwargs.get("cuttable_length_number", None),
                    style="form",
                    explode=False,
                ),
                "cuttableLengthUOM": oapi.client.format_argument_value(
                    "cuttableLengthUOM",
                    kwargs.get("cuttable_length_uom", None),
                    style="form",
                    explode=False,
                ),
                "cuttableWidthNumber": oapi.client.format_argument_value(
                    "cuttableWidthNumber",
                    kwargs.get("cuttable_width_number", None),
                    style="form",
                    explode=False,
                ),
                "cuttableWidthUOM": oapi.client.format_argument_value(
                    "cuttableWidthUOM",
                    kwargs.get("cuttable_width_uom", None),
                    style="form",
                    explode=False,
                ),
                "materialLengthNumber": oapi.client.format_argument_value(
                    "materialLengthNumber",
                    kwargs.get("material_length_number", None),
                    style="form",
                    explode=False,
                ),
                "materialLengthUOM": oapi.client.format_argument_value(
                    "materialLengthUOM",
                    kwargs.get("material_length_uom", None),
                    style="form",
                    explode=False,
                ),
                "materialWidthNumber": oapi.client.format_argument_value(
                    "materialWidthNumber",
                    kwargs.get("material_width_number", None),
                    style="form",
                    explode=False,
                ),
                "materialWidthUOM": oapi.client.format_argument_value(
                    "materialWidthUOM",
                    kwargs.get("material_width_uom", None),
                    style="form",
                    explode=False,
                ),
                "initialPrice": oapi.client.format_argument_value(
                    "initialPrice",
                    kwargs.get("initial_price", None),
                    style="form",
                    explode=False,
                ),
                "initialPriceUOM": oapi.client.format_argument_value(
                    "initialPriceUOM",
                    kwargs.get("initial_price_uom", None),
                    style="form",
                    explode=False,
                ),
                "patent": oapi.client.format_argument_value(
                    "patent",
                    kwargs.get("patent", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorIdentifier": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorIdentifier",
                    kwargs.get("supplied_material_color_identifier", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorGraphicDescription": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorGraphicDescription",
                    kwargs.get("supplied_material_color_graphic_description", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialTeamPlayerGraphicIdentifier": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialTeamPlayerGraphicIdentifier",
                    kwargs.get("supplied_material_team_player_graphic_identifier", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "teamPlayerGraphicIdentifier": oapi.client.format_argument_value(  # noqa
                    "teamPlayerGraphicIdentifier",
                    kwargs.get("team_player_graphic_identifier", None),
                    style="form",
                    explode=False,
                ),
                "color": oapi.client.format_argument_value(
                    "color",
                    kwargs.get("color", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorGraphicPrimaryColor": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorGraphicPrimaryColor",
                    kwargs.get("supplied_material_color_graphic_primary_color", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorGraphicHueIdentifier": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorGraphicHueIdentifier",
                    kwargs.get("supplied_material_color_graphic_hue_identifier", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialMultiColorCode": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialMultiColorCode",
                    kwargs.get("supplied_material_multi_color_code", None),
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorIsMultipleColors": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorIsMultipleColors",
                    kwargs.get("supplied_material_color_is_multiple_colors", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorGraphicInitialCycleYear": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorGraphicInitialCycleYear",
                    kwargs.get("supplied_material_color_graphic_initial_cycle_year", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorGraphicStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorGraphicStatusIndicator",
                    kwargs.get("supplied_material_color_graphic_status_indicator", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorGraphicStateIdentifier": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorGraphicStateIdentifier",
                    kwargs.get("supplied_material_color_graphic_state_identifier", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "createTimestamp": oapi.client.format_argument_value(
                    "createTimestamp",
                    kwargs.get("create_timestamp", None),
                    style="form",
                    explode=False,
                ),
                "changeTimestamp": oapi.client.format_argument_value(
                    "changeTimestamp",
                    kwargs.get("change_timestamp", None),
                    style="form",
                    explode=False,
                ),
                "parentMaterialItemIdentifier": oapi.client.format_argument_value(  # noqa
                    "parentMaterialItemIdentifier",
                    kwargs.get("parent_material_item_identifier", None),
                    style="form",
                    explode=False,
                ),
                "materialType": oapi.client.format_argument_value(
                    "materialType",
                    kwargs.get("material_type", None),
                    style="form",
                    explode=False,
                ),
                "materialItemName": oapi.client.format_argument_value(
                    "materialItemName",
                    kwargs.get("material_item_name", None),
                    style="form",
                    explode=False,
                ),
                "customsDescription": oapi.client.format_argument_value(
                    "customsDescription",
                    kwargs.get("customs_description", None),
                    style="form",
                    explode=False,
                ),
                "developmentTeam": oapi.client.format_argument_value(
                    "developmentTeam",
                    kwargs.get("development_team", None),
                    style="form",
                    explode=False,
                ),
                "coreMaterialNameVariationWeight": oapi.client.format_argument_value(  # noqa
                    "coreMaterialNameVariationWeight",
                    kwargs.get("core_material_name_variation_weight", None),
                    style="form",
                    explode=False,
                ),
                "coreMaterialNameVariationVisual": oapi.client.format_argument_value(  # noqa
                    "coreMaterialNameVariationVisual",
                    kwargs.get("core_material_name_variation_visual", None),
                    style="form",
                    explode=False,
                ),
                "targetPrice": oapi.client.format_argument_value(
                    "targetPrice",
                    kwargs.get("target_price", None),
                    style="form",
                    explode=False,
                ),
                "targetPriceUOM": oapi.client.format_argument_value(
                    "targetPriceUOM",
                    kwargs.get("target_price_uom", None),
                    style="form",
                    explode=False,
                ),
                "materialColorControlMode": oapi.client.format_argument_value(
                    "materialColorControlMode",
                    kwargs.get("material_color_control_mode", None),
                    style="form",
                    explode=False,
                ),
                "materialPricingMode": oapi.client.format_argument_value(
                    "materialPricingMode",
                    kwargs.get("material_pricing_mode", None),
                    style="form",
                    explode=False,
                ),
                "legacyCreatedOnDate": oapi.client.format_argument_value(
                    "legacyCreatedOnDate",
                    kwargs.get("legacy_created_on_date", None),
                    style="form",
                    explode=False,
                ),
                "legacyMaterialNumber": oapi.client.format_argument_value(
                    "legacyMaterialNumber",
                    kwargs.get("legacy_material_number", None),
                    style="form",
                    explode=False,
                ),
                "apparelPDMMaterialNumber": oapi.client.format_argument_value(
                    "apparelPDMMaterialNumber",
                    kwargs.get("apparel_pdm_material_number", None),
                    style="form",
                    explode=False,
                ),
                "materialDevelopmentTeam": oapi.client.format_argument_value(
                    "materialDevelopmentTeam",
                    kwargs.get("material_development_team", None),
                    style="form",
                    explode=False,
                ),
                "materialInitialCategory": oapi.client.format_argument_value(
                    "materialInitialCategory",
                    kwargs.get("material_initial_category", None),
                    style="form",
                    explode=False,
                ),
                "materialInitialCycleYear": oapi.client.format_argument_value(
                    "materialInitialCycleYear",
                    kwargs.get("material_initial_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "materialTargetCycleYear": oapi.client.format_argument_value(
                    "materialTargetCycleYear",
                    kwargs.get("material_target_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "materialItemStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "materialItemStatusIndicator",
                    kwargs.get("material_item_status_indicator", None),
                    style="form",
                    explode=False,
                ),
                "materialBOMIndicator": oapi.client.format_argument_value(
                    "materialBOMIndicator",
                    kwargs.get("material_bom_indicator", None),
                    style="form",
                    explode=False,
                ),
                "coreMaterialContentPercentage": oapi.client.format_argument_value(  # noqa
                    "coreMaterialContentPercentage",
                    kwargs.get("core_material_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "coreMaterialContentType": oapi.client.format_argument_value(
                    "coreMaterialContentType",
                    kwargs.get("core_material_content_type", None),
                    style="form",
                    explode=False,
                ),
                "coreMaterialContentSource": oapi.client.format_argument_value(
                    "coreMaterialContentSource",
                    kwargs.get("core_material_content_source", None),
                    style="form",
                    explode=False,
                ),
                "coreMaterialFamily": oapi.client.format_argument_value(
                    "coreMaterialFamily",
                    kwargs.get("core_material_family", None),
                    style="form",
                    explode=False,
                ),
                "materialContentPercentage": oapi.client.format_argument_value(
                    "materialContentPercentage",
                    kwargs.get("material_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "materialContentType": oapi.client.format_argument_value(
                    "materialContentType",
                    kwargs.get("material_content_type", None),
                    style="form",
                    explode=False,
                ),
                "materialContentSource": oapi.client.format_argument_value(
                    "materialContentSource",
                    kwargs.get("material_content_source", None),
                    style="form",
                    explode=False,
                ),
                "materialLabelContentPercentage": oapi.client.format_argument_value(  # noqa
                    "materialLabelContentPercentage",
                    kwargs.get("material_label_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "materialLabelContentType": oapi.client.format_argument_value(
                    "materialLabelContentType",
                    kwargs.get("material_label_content_type", None),
                    style="form",
                    explode=False,
                ),
                "materialLabelContentSource": oapi.client.format_argument_value(  # noqa
                    "materialLabelContentSource",
                    kwargs.get("material_label_content_source", None),
                    style="form",
                    explode=False,
                ),
                "materialFamily": oapi.client.format_argument_value(
                    "materialFamily",
                    kwargs.get("material_family", None),
                    style="form",
                    explode=False,
                ),
                "materialOwner": oapi.client.format_argument_value(
                    "materialOwner",
                    kwargs.get("material_owner", None),
                    style="form",
                    explode=False,
                ),
                "artworkGraphic": oapi.client.format_argument_value(
                    "artworkGraphic",
                    kwargs.get("artwork_graphic", None),
                    style="form",
                    explode=False,
                ),
                "artworkTechnique": oapi.client.format_argument_value(
                    "artworkTechnique",
                    kwargs.get("artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "secondaryProcessIndicator": oapi.client.format_argument_value(
                    "secondaryProcessIndicator",
                    kwargs.get("secondary_process_indicator", None),
                    style="form",
                    explode=False,
                ),
                "artworkApplicationLocation": oapi.client.format_argument_value(  # noqa
                    "artworkApplicationLocation",
                    kwargs.get("artwork_application_location", None),
                    style="form",
                    explode=False,
                ),
                "artworkRepeatLengthCm": oapi.client.format_argument_value(
                    "artworkRepeatLengthCm",
                    kwargs.get("artwork_repeat_length_cm", None),
                    style="form",
                    explode=False,
                ),
                "directionalPatternIndicator": oapi.client.format_argument_value(  # noqa
                    "directionalPatternIndicator",
                    kwargs.get("directional_pattern_indicator", None),
                    style="form",
                    explode=False,
                ),
                "garmentLocationPlacement": oapi.client.format_argument_value(
                    "garmentLocationPlacement",
                    kwargs.get("garment_location_placement", None),
                    style="form",
                    explode=False,
                ),
                "endUse": oapi.client.format_argument_value(
                    "endUse",
                    kwargs.get("end_use", None),
                    style="form",
                    explode=False,
                ),
                "developmentReason": oapi.client.format_argument_value(
                    "developmentReason",
                    kwargs.get("development_reason", None),
                    style="form",
                    explode=False,
                ),
                "materialBenefits": oapi.client.format_argument_value(
                    "materialBenefits",
                    kwargs.get("material_benefits", None),
                    style="form",
                    explode=False,
                ),
                "fabricFaceDesignation": oapi.client.format_argument_value(
                    "fabricFaceDesignation",
                    kwargs.get("fabric_face_designation", None),
                    style="form",
                    explode=False,
                ),
                "stretchDirection": oapi.client.format_argument_value(
                    "stretchDirection",
                    kwargs.get("stretch_direction", None),
                    style="form",
                    explode=False,
                ),
                "vendorSpecialCareInstructions": oapi.client.format_argument_value(  # noqa
                    "vendorSpecialCareInstructions",
                    kwargs.get("vendor_special_care_instructions", None),
                    style="form",
                    explode=False,
                ),
                "considerationAndRisks": oapi.client.format_argument_value(
                    "considerationAndRisks",
                    kwargs.get("consideration_and_risks", None),
                    style="form",
                    explode=False,
                ),
                "thicknessMm": oapi.client.format_argument_value(
                    "thicknessMm",
                    kwargs.get("thickness_mm", None),
                    style="form",
                    explode=False,
                ),
                "thicknessSelection": oapi.client.format_argument_value(
                    "thicknessSelection",
                    kwargs.get("thickness_selection", None),
                    style="form",
                    explode=False,
                ),
                "maximumThicknessMm": oapi.client.format_argument_value(
                    "maximumThicknessMm",
                    kwargs.get("maximum_thickness_mm", None),
                    style="form",
                    explode=False,
                ),
                "minimumThicknessMm": oapi.client.format_argument_value(
                    "minimumThicknessMm",
                    kwargs.get("minimum_thickness_mm", None),
                    style="form",
                    explode=False,
                ),
                "lengthMm": oapi.client.format_argument_value(
                    "lengthMm",
                    kwargs.get("length_mm", None),
                    style="form",
                    explode=False,
                ),
                "lengthCm": oapi.client.format_argument_value(
                    "lengthCm",
                    kwargs.get("length_cm", None),
                    style="form",
                    explode=False,
                ),
                "dimensionWidthIndicator": oapi.client.format_argument_value(
                    "dimensionWidthIndicator",
                    kwargs.get("dimension_width_indicator", None),
                    style="form",
                    explode=False,
                ),
                "widthMm": oapi.client.format_argument_value(
                    "widthMm",
                    kwargs.get("width_mm", None),
                    style="form",
                    explode=False,
                ),
                "widthCm": oapi.client.format_argument_value(
                    "widthCm",
                    kwargs.get("width_cm", None),
                    style="form",
                    explode=False,
                ),
                "heightMm": oapi.client.format_argument_value(
                    "heightMm",
                    kwargs.get("height_mm", None),
                    style="form",
                    explode=False,
                ),
                "heightCm": oapi.client.format_argument_value(
                    "heightCm",
                    kwargs.get("height_cm", None),
                    style="form",
                    explode=False,
                ),
                "weightGramsPerSquareMeter": oapi.client.format_argument_value(
                    "weightGramsPerSquareMeter",
                    kwargs.get("weight_grams_per_square_meter", None),
                    style="form",
                    explode=False,
                ),
                "externalDiameterMm": oapi.client.format_argument_value(
                    "externalDiameterMm",
                    kwargs.get("external_diameter_mm", None),
                    style="form",
                    explode=False,
                ),
                "externalLengthMm": oapi.client.format_argument_value(
                    "externalLengthMm",
                    kwargs.get("external_length_mm", None),
                    style="form",
                    explode=False,
                ),
                "externalWidthMm": oapi.client.format_argument_value(
                    "externalWidthMm",
                    kwargs.get("external_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "internalDiameterMm": oapi.client.format_argument_value(
                    "internalDiameterMm",
                    kwargs.get("internal_diameter_mm", None),
                    style="form",
                    explode=False,
                ),
                "internalLengthMm": oapi.client.format_argument_value(
                    "internalLengthMm",
                    kwargs.get("internal_length_mm", None),
                    style="form",
                    explode=False,
                ),
                "internalWidthMm": oapi.client.format_argument_value(
                    "internalWidthMm",
                    kwargs.get("internal_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "gaugeInch": oapi.client.format_argument_value(
                    "gaugeInch",
                    kwargs.get("gauge_inch", None),
                    style="form",
                    explode=False,
                ),
                "gramsPerThousandPieces": oapi.client.format_argument_value(
                    "gramsPerThousandPieces",
                    kwargs.get("grams_per_thousand_pieces", None),
                    style="form",
                    explode=False,
                ),
                "weightGramsPerThousandPieces": oapi.client.format_argument_value(  # noqa
                    "weightGramsPerThousandPieces",
                    kwargs.get("weight_grams_per_thousand_pieces", None),
                    style="form",
                    explode=False,
                ),
                "weightGramsPerLinearYard": oapi.client.format_argument_value(
                    "weightGramsPerLinearYard",
                    kwargs.get("weight_grams_per_linear_yard", None),
                    style="form",
                    explode=False,
                ),
                "weightGramsPerLinearMeter": oapi.client.format_argument_value(
                    "weightGramsPerLinearMeter",
                    kwargs.get("weight_grams_per_linear_meter", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionContentPercentage": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionContentPercentage",
                    kwargs.get("yarn_composition_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionContentType": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionContentType",
                    kwargs.get("yarn_composition_content_type", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionContentSource": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionContentSource",
                    kwargs.get("yarn_composition_content_source", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionLocation": oapi.client.format_argument_value(
                    "yarnCompositionLocation",
                    kwargs.get("yarn_composition_location", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionType": oapi.client.format_argument_value(
                    "yarnCompositionType",
                    kwargs.get("yarn_composition_type", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionSize": oapi.client.format_argument_value(
                    "yarnCompositionSize",
                    kwargs.get("yarn_composition_size", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionSpinningMethod": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionSpinningMethod",
                    kwargs.get("yarn_composition_spinning_method", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionCount": oapi.client.format_argument_value(
                    "yarnCompositionCount",
                    kwargs.get("yarn_composition_count", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionPreparation": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionPreparation",
                    kwargs.get("yarn_composition_preparation", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionCrossSection": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionCrossSection",
                    kwargs.get("yarn_composition_cross_section", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionFilamentCount": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionFilamentCount",
                    kwargs.get("yarn_composition_filament_count", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionNumberSystem": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionNumberSystem",
                    kwargs.get("yarn_composition_number_system", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionLuster": oapi.client.format_argument_value(
                    "yarnCompositionLuster",
                    kwargs.get("yarn_composition_luster", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionBrand": oapi.client.format_argument_value(
                    "yarnCompositionBrand",
                    kwargs.get("yarn_composition_brand", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionTexture": oapi.client.format_argument_value(
                    "yarnCompositionTexture",
                    kwargs.get("yarn_composition_texture", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionTwist": oapi.client.format_argument_value(
                    "yarnCompositionTwist",
                    kwargs.get("yarn_composition_twist", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionFinishProcess": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionFinishProcess",
                    kwargs.get("yarn_composition_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionDyeMethod": oapi.client.format_argument_value(
                    "yarnCompositionDyeMethod",
                    kwargs.get("yarn_composition_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionVisualEffect": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionVisualEffect",
                    kwargs.get("yarn_composition_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionFixedColor": oapi.client.format_argument_value(
                    "yarnCompositionFixedColor",
                    kwargs.get("yarn_composition_fixed_color", None),
                    style="form",
                    explode=False,
                ),
                "yarnCompositionUsagePercentage": oapi.client.format_argument_value(  # noqa
                    "yarnCompositionUsagePercentage",
                    kwargs.get("yarn_composition_usage_percentage", None),
                    style="form",
                    explode=False,
                ),
                "plyContentPercentage": oapi.client.format_argument_value(
                    "plyContentPercentage",
                    kwargs.get("ply_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "plyContentType": oapi.client.format_argument_value(
                    "plyContentType",
                    kwargs.get("ply_content_type", None),
                    style="form",
                    explode=False,
                ),
                "plyContentSource": oapi.client.format_argument_value(
                    "plyContentSource",
                    kwargs.get("ply_content_source", None),
                    style="form",
                    explode=False,
                ),
                "plyLocation": oapi.client.format_argument_value(
                    "plyLocation",
                    kwargs.get("ply_location", None),
                    style="form",
                    explode=False,
                ),
                "plyType": oapi.client.format_argument_value(
                    "plyType",
                    kwargs.get("ply_type", None),
                    style="form",
                    explode=False,
                ),
                "plyBrand": oapi.client.format_argument_value(
                    "plyBrand",
                    kwargs.get("ply_brand", None),
                    style="form",
                    explode=False,
                ),
                "plySize": oapi.client.format_argument_value(
                    "plySize",
                    kwargs.get("ply_size", None),
                    style="form",
                    explode=False,
                ),
                "plyNumberSystem": oapi.client.format_argument_value(
                    "plyNumberSystem",
                    kwargs.get("ply_number_system", None),
                    style="form",
                    explode=False,
                ),
                "plyCrossSection": oapi.client.format_argument_value(
                    "plyCrossSection",
                    kwargs.get("ply_cross_section", None),
                    style="form",
                    explode=False,
                ),
                "plySpinningMethod": oapi.client.format_argument_value(
                    "plySpinningMethod",
                    kwargs.get("ply_spinning_method", None),
                    style="form",
                    explode=False,
                ),
                "plyFilamentCount": oapi.client.format_argument_value(
                    "plyFilamentCount",
                    kwargs.get("ply_filament_count", None),
                    style="form",
                    explode=False,
                ),
                "plyTwist": oapi.client.format_argument_value(
                    "plyTwist",
                    kwargs.get("ply_twist", None),
                    style="form",
                    explode=False,
                ),
                "plyLuster": oapi.client.format_argument_value(
                    "plyLuster",
                    kwargs.get("ply_luster", None),
                    style="form",
                    explode=False,
                ),
                "plyTexture": oapi.client.format_argument_value(
                    "plyTexture",
                    kwargs.get("ply_texture", None),
                    style="form",
                    explode=False,
                ),
                "plyFinishProcess": oapi.client.format_argument_value(
                    "plyFinishProcess",
                    kwargs.get("ply_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "plyDyeMethod": oapi.client.format_argument_value(
                    "plyDyeMethod",
                    kwargs.get("ply_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "plyVisualEffect": oapi.client.format_argument_value(
                    "plyVisualEffect",
                    kwargs.get("ply_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "plyFixedColor": oapi.client.format_argument_value(
                    "plyFixedColor",
                    kwargs.get("ply_fixed_color", None),
                    style="form",
                    explode=False,
                ),
                "plyUsagePercentage": oapi.client.format_argument_value(
                    "plyUsagePercentage",
                    kwargs.get("ply_usage_percentage", None),
                    style="form",
                    explode=False,
                ),
                "fiberContentPercentage": oapi.client.format_argument_value(
                    "fiberContentPercentage",
                    kwargs.get("fiber_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "fiberContentType": oapi.client.format_argument_value(
                    "fiberContentType",
                    kwargs.get("fiber_content_type", None),
                    style="form",
                    explode=False,
                ),
                "fiberContentSource": oapi.client.format_argument_value(
                    "fiberContentSource",
                    kwargs.get("fiber_content_source", None),
                    style="form",
                    explode=False,
                ),
                "fiberSize": oapi.client.format_argument_value(
                    "fiberSize",
                    kwargs.get("fiber_size", None),
                    style="form",
                    explode=False,
                ),
                "fiberPlyLocation": oapi.client.format_argument_value(
                    "fiberPlyLocation",
                    kwargs.get("fiber_ply_location", None),
                    style="form",
                    explode=False,
                ),
                "fiberStapleNumberSystem": oapi.client.format_argument_value(
                    "fiberStapleNumberSystem",
                    kwargs.get("fiber_staple_number_system", None),
                    style="form",
                    explode=False,
                ),
                "fiberStapleLength": oapi.client.format_argument_value(
                    "fiberStapleLength",
                    kwargs.get("fiber_staple_length", None),
                    style="form",
                    explode=False,
                ),
                "fiberStapleLengthMin": oapi.client.format_argument_value(
                    "fiberStapleLengthMin",
                    kwargs.get("fiber_staple_length_min", None),
                    style="form",
                    explode=False,
                ),
                "fiberStapleLengthMax": oapi.client.format_argument_value(
                    "fiberStapleLengthMax",
                    kwargs.get("fiber_staple_length_max", None),
                    style="form",
                    explode=False,
                ),
                "fiberDiameter": oapi.client.format_argument_value(
                    "fiberDiameter",
                    kwargs.get("fiber_diameter", None),
                    style="form",
                    explode=False,
                ),
                "fiberDiameterMin": oapi.client.format_argument_value(
                    "fiberDiameterMin",
                    kwargs.get("fiber_diameter_min", None),
                    style="form",
                    explode=False,
                ),
                "fiberDiameterMax": oapi.client.format_argument_value(
                    "fiberDiameterMax",
                    kwargs.get("fiber_diameter_max", None),
                    style="form",
                    explode=False,
                ),
                "fiberDiameterUnit": oapi.client.format_argument_value(
                    "fiberDiameterUnit",
                    kwargs.get("fiber_diameter_unit", None),
                    style="form",
                    explode=False,
                ),
                "fiberPreparation": oapi.client.format_argument_value(
                    "fiberPreparation",
                    kwargs.get("fiber_preparation", None),
                    style="form",
                    explode=False,
                ),
                "fiberCrossSection": oapi.client.format_argument_value(
                    "fiberCrossSection",
                    kwargs.get("fiber_cross_section", None),
                    style="form",
                    explode=False,
                ),
                "fiberLuster": oapi.client.format_argument_value(
                    "fiberLuster",
                    kwargs.get("fiber_luster", None),
                    style="form",
                    explode=False,
                ),
                "fiberFinishProcess": oapi.client.format_argument_value(
                    "fiberFinishProcess",
                    kwargs.get("fiber_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "fiberDyeMethod": oapi.client.format_argument_value(
                    "fiberDyeMethod",
                    kwargs.get("fiber_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "fiberUsagePercentage": oapi.client.format_argument_value(
                    "fiberUsagePercentage",
                    kwargs.get("fiber_usage_percentage", None),
                    style="form",
                    explode=False,
                ),
                "edgeFinish": oapi.client.format_argument_value(
                    "edgeFinish",
                    kwargs.get("edge_finish", None),
                    style="form",
                    explode=False,
                ),
                "visualEffect": oapi.client.format_argument_value(
                    "visualEffect",
                    kwargs.get("visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "visualEffectLocation": oapi.client.format_argument_value(
                    "visualEffectLocation",
                    kwargs.get("visual_effect_location", None),
                    style="form",
                    explode=False,
                ),
                "printCode": oapi.client.format_argument_value(
                    "printCode",
                    kwargs.get("print_code", None),
                    style="form",
                    explode=False,
                ),
                "embossCodeText": oapi.client.format_argument_value(
                    "embossCodeText",
                    kwargs.get("emboss_code_text", None),
                    style="form",
                    explode=False,
                ),
                "applicationTechnique": oapi.client.format_argument_value(
                    "applicationTechnique",
                    kwargs.get("application_technique", None),
                    style="form",
                    explode=False,
                ),
                "finishProcess": oapi.client.format_argument_value(
                    "finishProcess",
                    kwargs.get("finish_process", None),
                    style="form",
                    explode=False,
                ),
                "finishLocation": oapi.client.format_argument_value(
                    "finishLocation",
                    kwargs.get("finish_location", None),
                    style="form",
                    explode=False,
                ),
                "numberOfPasses": oapi.client.format_argument_value(
                    "numberOfPasses",
                    kwargs.get("number_of_passes", None),
                    style="form",
                    explode=False,
                ),
                "materialTechnologies": oapi.client.format_argument_value(
                    "materialTechnologies",
                    kwargs.get("material_technologies", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperCode": oapi.client.format_argument_value(
                    "releasePaperCode",
                    kwargs.get("release_paper_code", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperOne": oapi.client.format_argument_value(
                    "releasePaperOne",
                    kwargs.get("release_paper_one", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperTwo": oapi.client.format_argument_value(
                    "releasePaperTwo",
                    kwargs.get("release_paper_two", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperSideOne": oapi.client.format_argument_value(
                    "releasePaperSideOne",
                    kwargs.get("release_paper_side_one", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperSideTwo": oapi.client.format_argument_value(
                    "releasePaperSideTwo",
                    kwargs.get("release_paper_side_two", None),
                    style="form",
                    explode=False,
                ),
                "releasePaperFinishProcess": oapi.client.format_argument_value(
                    "releasePaperFinishProcess",
                    kwargs.get("release_paper_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "topLayerMaterialItem": oapi.client.format_argument_value(
                    "topLayerMaterialItem",
                    kwargs.get("top_layer_material_item", None),
                    style="form",
                    explode=False,
                ),
                "middleLayer1MaterialItem": oapi.client.format_argument_value(
                    "middleLayer1MaterialItem",
                    kwargs.get("middle_layer_1_material_item", None),
                    style="form",
                    explode=False,
                ),
                "middleLayer2MaterialItem": oapi.client.format_argument_value(
                    "middleLayer2MaterialItem",
                    kwargs.get("middle_layer_2_material_item", None),
                    style="form",
                    explode=False,
                ),
                "middleLayer3MaterialItem": oapi.client.format_argument_value(
                    "middleLayer3MaterialItem",
                    kwargs.get("middle_layer_3_material_item", None),
                    style="form",
                    explode=False,
                ),
                "bottomLayerMaterialItem": oapi.client.format_argument_value(
                    "bottomLayerMaterialItem",
                    kwargs.get("bottom_layer_material_item", None),
                    style="form",
                    explode=False,
                ),
                "nonWovenSubstrateType": oapi.client.format_argument_value(
                    "nonWovenSubstrateType",
                    kwargs.get("non_woven_substrate_type", None),
                    style="form",
                    explode=False,
                ),
                "nonWovenWebBondingMethod": oapi.client.format_argument_value(
                    "nonWovenWebBondingMethod",
                    kwargs.get("non_woven_web_bonding_method", None),
                    style="form",
                    explode=False,
                ),
                "colorDominance": oapi.client.format_argument_value(
                    "colorDominance",
                    kwargs.get("color_dominance", None),
                    style="form",
                    explode=False,
                ),
                "colorEffect": oapi.client.format_argument_value(
                    "colorEffect",
                    kwargs.get("color_effect", None),
                    style="form",
                    explode=False,
                ),
                "colorPosition": oapi.client.format_argument_value(
                    "colorPosition",
                    kwargs.get("color_position", None),
                    style="form",
                    explode=False,
                ),
                "colorLocation": oapi.client.format_argument_value(
                    "colorLocation",
                    kwargs.get("color_location", None),
                    style="form",
                    explode=False,
                ),
                "colorCallout": oapi.client.format_argument_value(
                    "colorCallout",
                    kwargs.get("color_callout", None),
                    style="form",
                    explode=False,
                ),
                "colorFiber": oapi.client.format_argument_value(
                    "colorFiber",
                    kwargs.get("color_fiber", None),
                    style="form",
                    explode=False,
                ),
                "dyeMethod": oapi.client.format_argument_value(
                    "dyeMethod",
                    kwargs.get("dye_method", None),
                    style="form",
                    explode=False,
                ),
                "dyeType": oapi.client.format_argument_value(
                    "dyeType",
                    kwargs.get("dye_type", None),
                    style="form",
                    explode=False,
                ),
                "activeCategory": oapi.client.format_argument_value(
                    "activeCategory",
                    kwargs.get("active_category", None),
                    style="form",
                    explode=False,
                ),
                "activeCycleYear": oapi.client.format_argument_value(
                    "activeCycleYear",
                    kwargs.get("active_cycle_year", None),
                    style="form",
                    explode=False,
                ),
                "webFormation": oapi.client.format_argument_value(
                    "webFormation",
                    kwargs.get("web_formation", None),
                    style="form",
                    explode=False,
                ),
                "numberOfColors": oapi.client.format_argument_value(
                    "numberOfColors",
                    kwargs.get("number_of_colors", None),
                    style="form",
                    explode=False,
                ),
                "lastIdentifier": oapi.client.format_argument_value(
                    "lastIdentifier",
                    kwargs.get("last_identifier", None),
                    style="form",
                    explode=False,
                ),
                "outsourcedProcess": oapi.client.format_argument_value(
                    "outsourcedProcess",
                    kwargs.get("outsourced_process", None),
                    style="form",
                    explode=False,
                ),
                "perfCode": oapi.client.format_argument_value(
                    "perfCode",
                    kwargs.get("perf_code", None),
                    style="form",
                    explode=False,
                ),
                "animalSource": oapi.client.format_argument_value(
                    "animalSource",
                    kwargs.get("animal_source", None),
                    style="form",
                    explode=False,
                ),
                "dyedThroughCrustIndicator": oapi.client.format_argument_value(
                    "dyedThroughCrustIndicator",
                    kwargs.get("dyed_through_crust_indicator", None),
                    style="form",
                    explode=False,
                ),
                "oilContent": oapi.client.format_argument_value(
                    "oilContent",
                    kwargs.get("oil_content", None),
                    style="form",
                    explode=False,
                ),
                "reTannage": oapi.client.format_argument_value(
                    "reTannage",
                    kwargs.get("re_tannage", None),
                    style="form",
                    explode=False,
                ),
                "washableIndicator": oapi.client.format_argument_value(
                    "washableIndicator",
                    kwargs.get("washable_indicator", None),
                    style="form",
                    explode=False,
                ),
                "compositionLeatherType": oapi.client.format_argument_value(
                    "compositionLeatherType",
                    kwargs.get("composition_leather_type", None),
                    style="form",
                    explode=False,
                ),
                "animalSourceCountryOfOrigin": oapi.client.format_argument_value(  # noqa
                    "animalSourceCountryOfOrigin",
                    kwargs.get("animal_source_country_of_origin", None),
                    style="form",
                    explode=False,
                ),
                "satrasummQC": oapi.client.format_argument_value(
                    "satrasummQC",
                    kwargs.get("satrasumm_qc", None),
                    style="form",
                    explode=False,
                ),
                "grainLeatherType": oapi.client.format_argument_value(
                    "grainLeatherType",
                    kwargs.get("grain_leather_type", None),
                    style="form",
                    explode=False,
                ),
                "grainLeatherSubType": oapi.client.format_argument_value(
                    "grainLeatherSubType",
                    kwargs.get("grain_leather_sub_type", None),
                    style="form",
                    explode=False,
                ),
                "splitLeatherType": oapi.client.format_argument_value(
                    "splitLeatherType",
                    kwargs.get("split_leather_type", None),
                    style="form",
                    explode=False,
                ),
                "averagePUThickness": oapi.client.format_argument_value(
                    "averagePUThickness",
                    kwargs.get("average_pu_thickness", None),
                    style="form",
                    explode=False,
                ),
                "coatingThicknessMm": oapi.client.format_argument_value(
                    "coatingThicknessMm",
                    kwargs.get("coating_thickness_mm", None),
                    style="form",
                    explode=False,
                ),
                "moldable": oapi.client.format_argument_value(
                    "moldable",
                    kwargs.get("moldable", None),
                    style="form",
                    explode=False,
                ),
                "substrateProcessingType": oapi.client.format_argument_value(
                    "substrateProcessingType",
                    kwargs.get("substrate_processing_type", None),
                    style="form",
                    explode=False,
                ),
                "substratePUDippedIndicator": oapi.client.format_argument_value(  # noqa
                    "substratePUDippedIndicator",
                    kwargs.get("substrate_pu_dipped_indicator", None),
                    style="form",
                    explode=False,
                ),
                "substrateConstruction": oapi.client.format_argument_value(
                    "substrateConstruction",
                    kwargs.get("substrate_construction", None),
                    style="form",
                    explode=False,
                ),
                "textileConstructionType": oapi.client.format_argument_value(
                    "textileConstructionType",
                    kwargs.get("textile_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "textileSubVariation": oapi.client.format_argument_value(
                    "textileSubVariation",
                    kwargs.get("textile_sub_variation", None),
                    style="form",
                    explode=False,
                ),
                "textileSubVariationTwo": oapi.client.format_argument_value(
                    "textileSubVariationTwo",
                    kwargs.get("textile_sub_variation_two", None),
                    style="form",
                    explode=False,
                ),
                "textileVariation": oapi.client.format_argument_value(
                    "textileVariation",
                    kwargs.get("textile_variation", None),
                    style="form",
                    explode=False,
                ),
                "endsPerInchNumber": oapi.client.format_argument_value(
                    "endsPerInchNumber",
                    kwargs.get("ends_per_inch_number", None),
                    style="form",
                    explode=False,
                ),
                "picksPerInchNumber": oapi.client.format_argument_value(
                    "picksPerInchNumber",
                    kwargs.get("picks_per_inch_number", None),
                    style="form",
                    explode=False,
                ),
                "machineryType": oapi.client.format_argument_value(
                    "machineryType",
                    kwargs.get("machinery_type", None),
                    style="form",
                    explode=False,
                ),
                "warpCount": oapi.client.format_argument_value(
                    "warpCount",
                    kwargs.get("warp_count", None),
                    style="form",
                    explode=False,
                ),
                "weftCount": oapi.client.format_argument_value(
                    "weftCount",
                    kwargs.get("weft_count", None),
                    style="form",
                    explode=False,
                ),
                "twillConstructionType": oapi.client.format_argument_value(
                    "twillConstructionType",
                    kwargs.get("twill_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "twillDirection": oapi.client.format_argument_value(
                    "twillDirection",
                    kwargs.get("twill_direction", None),
                    style="form",
                    explode=False,
                ),
                "foldIndicator": oapi.client.format_argument_value(
                    "foldIndicator",
                    kwargs.get("fold_indicator", None),
                    style="form",
                    explode=False,
                ),
                "ribConstruction": oapi.client.format_argument_value(
                    "ribConstruction",
                    kwargs.get("rib_construction", None),
                    style="form",
                    explode=False,
                ),
                "heightIndicator": oapi.client.format_argument_value(
                    "heightIndicator",
                    kwargs.get("height_indicator", None),
                    style="form",
                    explode=False,
                ),
                "rowsOfSpandex": oapi.client.format_argument_value(
                    "rowsOfSpandex",
                    kwargs.get("rows_of_spandex", None),
                    style="form",
                    explode=False,
                ),
                "partTypeOrientation": oapi.client.format_argument_value(
                    "partTypeOrientation",
                    kwargs.get("part_type_orientation", None),
                    style="form",
                    explode=False,
                ),
                "initialDevelopmentProductAlias": oapi.client.format_argument_value(  # noqa
                    "initialDevelopmentProductAlias",
                    kwargs.get("initial_development_product_alias", None),
                    style="form",
                    explode=False,
                ),
                "preTwistYarn": oapi.client.format_argument_value(
                    "preTwistYarn",
                    kwargs.get("pre_twist_yarn", None),
                    style="form",
                    explode=False,
                ),
                "program": oapi.client.format_argument_value(
                    "program",
                    kwargs.get("program", None),
                    style="form",
                    explode=False,
                ),
                "steamMethod": oapi.client.format_argument_value(
                    "steamMethod",
                    kwargs.get("steam_method", None),
                    style="form",
                    explode=False,
                ),
                "designPatentNumber": oapi.client.format_argument_value(
                    "designPatentNumber",
                    kwargs.get("design_patent_number", None),
                    style="form",
                    explode=False,
                ),
                "utilityPatentNumber": oapi.client.format_argument_value(
                    "utilityPatentNumber",
                    kwargs.get("utility_patent_number", None),
                    style="form",
                    explode=False,
                ),
                "developmentDefectRate": oapi.client.format_argument_value(
                    "developmentDefectRate",
                    kwargs.get("development_defect_rate", None),
                    style="form",
                    explode=False,
                ),
                "negotiatedDefectRate": oapi.client.format_argument_value(
                    "negotiatedDefectRate",
                    kwargs.get("negotiated_defect_rate", None),
                    style="form",
                    explode=False,
                ),
                "runTimeMinutes": oapi.client.format_argument_value(
                    "runTimeMinutes",
                    kwargs.get("run_time_minutes", None),
                    style="form",
                    explode=False,
                ),
                "gate": oapi.client.format_argument_value(
                    "gate",
                    kwargs.get("gate", None),
                    style="form",
                    explode=False,
                ),
                "structureTestingReference": oapi.client.format_argument_value(
                    "structureTestingReference",
                    kwargs.get("structure_testing_reference", None),
                    style="form",
                    explode=False,
                ),
                "structureReferenceNumber": oapi.client.format_argument_value(
                    "structureReferenceNumber",
                    kwargs.get("structure_reference_number", None),
                    style="form",
                    explode=False,
                ),
                "structureCoverage": oapi.client.format_argument_value(
                    "structureCoverage",
                    kwargs.get("structure_coverage", None),
                    style="form",
                    explode=False,
                ),
                "blanketNumber": oapi.client.format_argument_value(
                    "blanketNumber",
                    kwargs.get("blanket_number", None),
                    style="form",
                    explode=False,
                ),
                "yarnSize": oapi.client.format_argument_value(
                    "yarnSize",
                    kwargs.get("yarn_size", None),
                    style="form",
                    explode=False,
                ),
                "yarnSpinningMethod": oapi.client.format_argument_value(
                    "yarnSpinningMethod",
                    kwargs.get("yarn_spinning_method", None),
                    style="form",
                    explode=False,
                ),
                "allPlysTheSameIndicator": oapi.client.format_argument_value(
                    "allPlysTheSameIndicator",
                    kwargs.get("all_plys_the_same_indicator", None),
                    style="form",
                    explode=False,
                ),
                "fancyYarn": oapi.client.format_argument_value(
                    "fancyYarn",
                    kwargs.get("fancy_yarn", None),
                    style="form",
                    explode=False,
                ),
                "fixedColor": oapi.client.format_argument_value(
                    "fixedColor",
                    kwargs.get("fixed_color", None),
                    style="form",
                    explode=False,
                ),
                "yarnBrand": oapi.client.format_argument_value(
                    "yarnBrand",
                    kwargs.get("yarn_brand", None),
                    style="form",
                    explode=False,
                ),
                "yarnNumberSystem": oapi.client.format_argument_value(
                    "yarnNumberSystem",
                    kwargs.get("yarn_number_system", None),
                    style="form",
                    explode=False,
                ),
                "yarnTwist": oapi.client.format_argument_value(
                    "yarnTwist",
                    kwargs.get("yarn_twist", None),
                    style="form",
                    explode=False,
                ),
                "yarnPlyCount": oapi.client.format_argument_value(
                    "yarnPlyCount",
                    kwargs.get("yarn_ply_count", None),
                    style="form",
                    explode=False,
                ),
                "yarnType": oapi.client.format_argument_value(
                    "yarnType",
                    kwargs.get("yarn_type", None),
                    style="form",
                    explode=False,
                ),
                "yarnLuster": oapi.client.format_argument_value(
                    "yarnLuster",
                    kwargs.get("yarn_luster", None),
                    style="form",
                    explode=False,
                ),
                "yarnFinishProcess": oapi.client.format_argument_value(
                    "yarnFinishProcess",
                    kwargs.get("yarn_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "yarnDyeMethod": oapi.client.format_argument_value(
                    "yarnDyeMethod",
                    kwargs.get("yarn_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "yarnVisualEffect": oapi.client.format_argument_value(
                    "yarnVisualEffect",
                    kwargs.get("yarn_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "yarnNumberOfEnds": oapi.client.format_argument_value(
                    "yarnNumberOfEnds",
                    kwargs.get("yarn_number_of_ends", None),
                    style="form",
                    explode=False,
                ),
                "yarnFilamentCount": oapi.client.format_argument_value(
                    "yarnFilamentCount",
                    kwargs.get("yarn_filament_count", None),
                    style="form",
                    explode=False,
                ),
                "yarnCoveringMethod": oapi.client.format_argument_value(
                    "yarnCoveringMethod",
                    kwargs.get("yarn_covering_method", None),
                    style="form",
                    explode=False,
                ),
                "yarnTexture": oapi.client.format_argument_value(
                    "yarnTexture",
                    kwargs.get("yarn_texture", None),
                    style="form",
                    explode=False,
                ),
                "microfiberIndicator": oapi.client.format_argument_value(
                    "microfiberIndicator",
                    kwargs.get("microfiber_indicator", None),
                    style="form",
                    explode=False,
                ),
                "yarnPreparation": oapi.client.format_argument_value(
                    "yarnPreparation",
                    kwargs.get("yarn_preparation", None),
                    style="form",
                    explode=False,
                ),
                "yarnCrossSection": oapi.client.format_argument_value(
                    "yarnCrossSection",
                    kwargs.get("yarn_cross_section", None),
                    style="form",
                    explode=False,
                ),
                "yarnLocation": oapi.client.format_argument_value(
                    "yarnLocation",
                    kwargs.get("yarn_location", None),
                    style="form",
                    explode=False,
                ),
                "yarnSuppliedMaterial": oapi.client.format_argument_value(
                    "yarnSuppliedMaterial",
                    kwargs.get("yarn_supplied_material", None),
                    style="form",
                    explode=False,
                ),
                "yarnSuppliedMaterialNumberOfEnds": oapi.client.format_argument_value(  # noqa
                    "yarnSuppliedMaterialNumberOfEnds",
                    kwargs.get("yarn_supplied_material_number_of_ends", None),
                    style="form",
                    explode=False,
                ),
                "yarnUsagePercentage": oapi.client.format_argument_value(
                    "yarnUsagePercentage",
                    kwargs.get("yarn_usage_percentage", None),
                    style="form",
                    explode=False,
                ),
                "baseType": oapi.client.format_argument_value(
                    "baseType",
                    kwargs.get("base_type", None),
                    style="form",
                    explode=False,
                ),
                "singleComponentIndicator": oapi.client.format_argument_value(
                    "singleComponentIndicator",
                    kwargs.get("single_component_indicator", None),
                    style="form",
                    explode=False,
                ),
                "flammabilityRating": oapi.client.format_argument_value(
                    "flammabilityRating",
                    kwargs.get("flammability_rating", None),
                    style="form",
                    explode=False,
                ),
                "hotmeltType": oapi.client.format_argument_value(
                    "hotmeltType",
                    kwargs.get("hotmelt_type", None),
                    style="form",
                    explode=False,
                ),
                "hydrolysisResistantIndicator": oapi.client.format_argument_value(  # noqa
                    "hydrolysisResistantIndicator",
                    kwargs.get("hydrolysis_resistant_indicator", None),
                    style="form",
                    explode=False,
                ),
                "methodOfMake": oapi.client.format_argument_value(
                    "methodOfMake",
                    kwargs.get("method_of_make", None),
                    style="form",
                    explode=False,
                ),
                "chemPolyForm": oapi.client.format_argument_value(
                    "chemPolyForm",
                    kwargs.get("chem_poly_form", None),
                    style="form",
                    explode=False,
                ),
                "filmType": oapi.client.format_argument_value(
                    "filmType",
                    kwargs.get("film_type", None),
                    style="form",
                    explode=False,
                ),
                "hotmeltMaterialItem": oapi.client.format_argument_value(
                    "hotmeltMaterialItem",
                    kwargs.get("hotmelt_material_item", None),
                    style="form",
                    explode=False,
                ),
                "hotmeltThicknessNumberMm": oapi.client.format_argument_value(
                    "hotmeltThicknessNumberMm",
                    kwargs.get("hotmelt_thickness_number_mm", None),
                    style="form",
                    explode=False,
                ),
                "opacity": oapi.client.format_argument_value(
                    "opacity",
                    kwargs.get("opacity", None),
                    style="form",
                    explode=False,
                ),
                "stretchIndicator": oapi.client.format_argument_value(
                    "stretchIndicator",
                    kwargs.get("stretch_indicator", None),
                    style="form",
                    explode=False,
                ),
                "carrierPaperStatement": oapi.client.format_argument_value(
                    "carrierPaperStatement",
                    kwargs.get("carrier_paper_statement", None),
                    style="form",
                    explode=False,
                ),
                "foamType": oapi.client.format_argument_value(
                    "foamType",
                    kwargs.get("foam_type", None),
                    style="form",
                    explode=False,
                ),
                "polyurethaneChemistry": oapi.client.format_argument_value(
                    "polyurethaneChemistry",
                    kwargs.get("polyurethane_chemistry", None),
                    style="form",
                    explode=False,
                ),
                "hardnessAskerC": oapi.client.format_argument_value(
                    "hardnessAskerC",
                    kwargs.get("hardness_asker_c", None),
                    style="form",
                    explode=False,
                ),
                "firmness": oapi.client.format_argument_value(
                    "firmness",
                    kwargs.get("firmness", None),
                    style="form",
                    explode=False,
                ),
                "meltingPointNumber": oapi.client.format_argument_value(
                    "meltingPointNumber",
                    kwargs.get("melting_point_number", None),
                    style="form",
                    explode=False,
                ),
                "plasticType": oapi.client.format_argument_value(
                    "plasticType",
                    kwargs.get("plastic_type", None),
                    style="form",
                    explode=False,
                ),
                "plasticSubType": oapi.client.format_argument_value(
                    "plasticSubType",
                    kwargs.get("plastic_sub_type", None),
                    style="form",
                    explode=False,
                ),
                "ultravioletInhibitorIndicator": oapi.client.format_argument_value(  # noqa
                    "ultravioletInhibitorIndicator",
                    kwargs.get("ultraviolet_inhibitor_indicator", None),
                    style="form",
                    explode=False,
                ),
                "clearRubberIndicator": oapi.client.format_argument_value(
                    "clearRubberIndicator",
                    kwargs.get("clear_rubber_indicator", None),
                    style="form",
                    explode=False,
                ),
                "cureProcess": oapi.client.format_argument_value(
                    "cureProcess",
                    kwargs.get("cure_process", None),
                    style="form",
                    explode=False,
                ),
                "regrindContentPercentage": oapi.client.format_argument_value(
                    "regrindContentPercentage",
                    kwargs.get("regrind_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "sportActivity": oapi.client.format_argument_value(
                    "sportActivity",
                    kwargs.get("sport_activity", None),
                    style="form",
                    explode=False,
                ),
                "detachableMetalIndicator": oapi.client.format_argument_value(
                    "detachableMetalIndicator",
                    kwargs.get("detachable_metal_indicator", None),
                    style="form",
                    explode=False,
                ),
                "hardOrSoftComponent": oapi.client.format_argument_value(
                    "hardOrSoftComponent",
                    kwargs.get("hard_or_soft_component", None),
                    style="form",
                    explode=False,
                ),
                "stockOrCustom": oapi.client.format_argument_value(
                    "stockOrCustom",
                    kwargs.get("stock_or_custom", None),
                    style="form",
                    explode=False,
                ),
                "coreConstructionType": oapi.client.format_argument_value(
                    "coreConstructionType",
                    kwargs.get("core_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "componentConstructionType": oapi.client.format_argument_value(
                    "componentConstructionType",
                    kwargs.get("component_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "hasCoreIndicator": oapi.client.format_argument_value(
                    "hasCoreIndicator",
                    kwargs.get("has_core_indicator", None),
                    style="form",
                    explode=False,
                ),
                "shape": oapi.client.format_argument_value(
                    "shape",
                    kwargs.get("shape", None),
                    style="form",
                    explode=False,
                ),
                "logoType": oapi.client.format_argument_value(
                    "logoType",
                    kwargs.get("logo_type", None),
                    style="form",
                    explode=False,
                ),
                "logoName": oapi.client.format_argument_value(
                    "logoName",
                    kwargs.get("logo_name", None),
                    style="form",
                    explode=False,
                ),
                "logoPlacement": oapi.client.format_argument_value(
                    "logoPlacement",
                    kwargs.get("logo_placement", None),
                    style="form",
                    explode=False,
                ),
                "hotmeltIncludedIndicator": oapi.client.format_argument_value(
                    "hotmeltIncludedIndicator",
                    kwargs.get("hotmelt_included_indicator", None),
                    style="form",
                    explode=False,
                ),
                "elasticizedIndicator": oapi.client.format_argument_value(
                    "elasticizedIndicator",
                    kwargs.get("elasticized_indicator", None),
                    style="form",
                    explode=False,
                ),
                "vendorColorCardOnlyIndicator": oapi.client.format_argument_value(  # noqa
                    "vendorColorCardOnlyIndicator",
                    kwargs.get("vendor_color_card_only_indicator", None),
                    style="form",
                    explode=False,
                ),
                "componentForm": oapi.client.format_argument_value(
                    "componentForm",
                    kwargs.get("component_form", None),
                    style="form",
                    explode=False,
                ),
                "ligneSizeNumber": oapi.client.format_argument_value(
                    "ligneSizeNumber",
                    kwargs.get("ligne_size_number", None),
                    style="form",
                    explode=False,
                ),
                "numberOfHoles": oapi.client.format_argument_value(
                    "numberOfHoles",
                    kwargs.get("number_of_holes", None),
                    style="form",
                    explode=False,
                ),
                "adhesiveType": oapi.client.format_argument_value(
                    "adhesiveType",
                    kwargs.get("adhesive_type", None),
                    style="form",
                    explode=False,
                ),
                "gripperType": oapi.client.format_argument_value(
                    "gripperType",
                    kwargs.get("gripper_type", None),
                    style="form",
                    explode=False,
                ),
                "numberOfGripperRows": oapi.client.format_argument_value(
                    "numberOfGripperRows",
                    kwargs.get("number_of_gripper_rows", None),
                    style="form",
                    explode=False,
                ),
                "endFinish": oapi.client.format_argument_value(
                    "endFinish",
                    kwargs.get("end_finish", None),
                    style="form",
                    explode=False,
                ),
                "forProductSizes": oapi.client.format_argument_value(
                    "forProductSizes",
                    kwargs.get("for_product_sizes", None),
                    style="form",
                    explode=False,
                ),
                "partType": oapi.client.format_argument_value(
                    "partType",
                    kwargs.get("part_type", None),
                    style="form",
                    explode=False,
                ),
                "numberOfRows": oapi.client.format_argument_value(
                    "numberOfRows",
                    kwargs.get("number_of_rows", None),
                    style="form",
                    explode=False,
                ),
                "amountPerRow": oapi.client.format_argument_value(
                    "amountPerRow",
                    kwargs.get("amount_per_row", None),
                    style="form",
                    explode=False,
                ),
                "adjusterType": oapi.client.format_argument_value(
                    "adjusterType",
                    kwargs.get("adjuster_type", None),
                    style="form",
                    explode=False,
                ),
                "containsMagnetIndicator": oapi.client.format_argument_value(
                    "containsMagnetIndicator",
                    kwargs.get("contains_magnet_indicator", None),
                    style="form",
                    explode=False,
                ),
                "buttonType": oapi.client.format_argument_value(
                    "buttonType",
                    kwargs.get("button_type", None),
                    style="form",
                    explode=False,
                ),
                "tapeType": oapi.client.format_argument_value(
                    "tapeType",
                    kwargs.get("tape_type", None),
                    style="form",
                    explode=False,
                ),
                "snapType": oapi.client.format_argument_value(
                    "snapType",
                    kwargs.get("snap_type", None),
                    style="form",
                    explode=False,
                ),
                "snapPartType": oapi.client.format_argument_value(
                    "snapPartType",
                    kwargs.get("snap_part_type", None),
                    style="form",
                    explode=False,
                ),
                "tapeWidthMm": oapi.client.format_argument_value(
                    "tapeWidthMm",
                    kwargs.get("tape_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "snapWidthMm": oapi.client.format_argument_value(
                    "snapWidthMm",
                    kwargs.get("snap_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "snapRepeatLengthMm": oapi.client.format_argument_value(
                    "snapRepeatLengthMm",
                    kwargs.get("snap_repeat_length_mm", None),
                    style="form",
                    explode=False,
                ),
                "cordlockToggleType": oapi.client.format_argument_value(
                    "cordlockToggleType",
                    kwargs.get("cordlock_toggle_type", None),
                    style="form",
                    explode=False,
                ),
                "activationTemperatureNumber": oapi.client.format_argument_value(  # noqa
                    "activationTemperatureNumber",
                    kwargs.get("activation_temperature_number", None),
                    style="form",
                    explode=False,
                ),
                "counterType": oapi.client.format_argument_value(
                    "counterType",
                    kwargs.get("counter_type", None),
                    style="form",
                    explode=False,
                ),
                "dwellTime": oapi.client.format_argument_value(
                    "dwellTime",
                    kwargs.get("dwell_time", None),
                    style="form",
                    explode=False,
                ),
                "generalConstruction": oapi.client.format_argument_value(
                    "generalConstruction",
                    kwargs.get("general_construction", None),
                    style="form",
                    explode=False,
                ),
                "elasticType": oapi.client.format_argument_value(
                    "elasticType",
                    kwargs.get("elastic_type", None),
                    style="form",
                    explode=False,
                ),
                "crossoverDrawcordIndicator": oapi.client.format_argument_value(  # noqa
                    "crossoverDrawcordIndicator",
                    kwargs.get("crossover_drawcord_indicator", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordContentPercentage": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordContentPercentage",
                    kwargs.get("elastic_drawcord_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordContentType": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordContentType",
                    kwargs.get("elastic_drawcord_content_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordContentSource": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordContentSource",
                    kwargs.get("elastic_drawcord_content_source", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordAgletMaterialItem": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordAgletMaterialItem",
                    kwargs.get("elastic_drawcord_aglet_material_item", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordHasCoreIndicator": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordHasCoreIndicator",
                    kwargs.get("elastic_drawcord_has_core_indicator", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordElasticizedIndicator": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordElasticizedIndicator",
                    kwargs.get("elastic_drawcord_elasticized_indicator", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordShape": oapi.client.format_argument_value(
                    "elasticDrawcordShape",
                    kwargs.get("elastic_drawcord_shape", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordLogoName": oapi.client.format_argument_value(
                    "elasticDrawcordLogoName",
                    kwargs.get("elastic_drawcord_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordDimensionWidthIndicator": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordDimensionWidthIndicator",
                    kwargs.get("elastic_drawcord_dimension_width_indicator", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordGripperType": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordGripperType",
                    kwargs.get("elastic_drawcord_gripper_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordConstructionType": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordConstructionType",
                    kwargs.get("elastic_drawcord_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordForm": oapi.client.format_argument_value(
                    "elasticDrawcordForm",
                    kwargs.get("elastic_drawcord_form", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordEndFinish": oapi.client.format_argument_value(
                    "elasticDrawcordEndFinish",
                    kwargs.get("elastic_drawcord_end_finish", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordWidthMm": oapi.client.format_argument_value(
                    "elasticDrawcordWidthMm",
                    kwargs.get("elastic_drawcord_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordFinishProcess": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordFinishProcess",
                    kwargs.get("elastic_drawcord_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordDyeMethod": oapi.client.format_argument_value(
                    "elasticDrawcordDyeMethod",
                    kwargs.get("elastic_drawcord_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordArtworkTechnique",
                    kwargs.get("elastic_drawcord_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordVisualEffect": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordVisualEffect",
                    kwargs.get("elastic_drawcord_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "elasticDrawcordNumberOfColors": oapi.client.format_argument_value(  # noqa
                    "elasticDrawcordNumberOfColors",
                    kwargs.get("elastic_drawcord_number_of_colors", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletContentPercentage": oapi.client.format_argument_value(  # noqa
                    "elasticAgletContentPercentage",
                    kwargs.get("elastic_aglet_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletContentType": oapi.client.format_argument_value(
                    "elasticAgletContentType",
                    kwargs.get("elastic_aglet_content_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletContentSource": oapi.client.format_argument_value(
                    "elasticAgletContentSource",
                    kwargs.get("elastic_aglet_content_source", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletLogoName": oapi.client.format_argument_value(
                    "elasticAgletLogoName",
                    kwargs.get("elastic_aglet_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletShape": oapi.client.format_argument_value(
                    "elasticAgletShape",
                    kwargs.get("elastic_aglet_shape", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletConstructionType": oapi.client.format_argument_value(  # noqa
                    "elasticAgletConstructionType",
                    kwargs.get("elastic_aglet_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletWidthMm": oapi.client.format_argument_value(
                    "elasticAgletWidthMm",
                    kwargs.get("elastic_aglet_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletHeightMm": oapi.client.format_argument_value(
                    "elasticAgletHeightMm",
                    kwargs.get("elastic_aglet_height_mm", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletInternalDiameterMm": oapi.client.format_argument_value(  # noqa
                    "elasticAgletInternalDiameterMm",
                    kwargs.get("elastic_aglet_internal_diameter_mm", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletGramsPerThousandPieces": oapi.client.format_argument_value(  # noqa
                    "elasticAgletGramsPerThousandPieces",
                    kwargs.get("elastic_aglet_grams_per_thousand_pieces", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "elasticAgletFinishProcess": oapi.client.format_argument_value(
                    "elasticAgletFinishProcess",
                    kwargs.get("elastic_aglet_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletDyeMethod": oapi.client.format_argument_value(
                    "elasticAgletDyeMethod",
                    kwargs.get("elastic_aglet_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "elasticAgletArtworkTechnique",
                    kwargs.get("elastic_aglet_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletVisualEffect": oapi.client.format_argument_value(
                    "elasticAgletVisualEffect",
                    kwargs.get("elastic_aglet_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "elasticAgletNumberOfColors": oapi.client.format_argument_value(  # noqa
                    "elasticAgletNumberOfColors",
                    kwargs.get("elastic_aglet_number_of_colors", None),
                    style="form",
                    explode=False,
                ),
                "drawcordMaterialItem": oapi.client.format_argument_value(
                    "drawcordMaterialItem",
                    kwargs.get("drawcord_material_item", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletMaterialItem": oapi.client.format_argument_value(
                    "drawcordAgletMaterialItem",
                    kwargs.get("drawcord_aglet_material_item", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletContentPercentage": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletContentPercentage",
                    kwargs.get("drawcord_aglet_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletContentType": oapi.client.format_argument_value(
                    "drawcordAgletContentType",
                    kwargs.get("drawcord_aglet_content_type", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletContentSource": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletContentSource",
                    kwargs.get("drawcord_aglet_content_source", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletLogoName": oapi.client.format_argument_value(
                    "drawcordAgletLogoName",
                    kwargs.get("drawcord_aglet_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletShape": oapi.client.format_argument_value(
                    "drawcordAgletShape",
                    kwargs.get("drawcord_aglet_shape", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletConstructionType": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletConstructionType",
                    kwargs.get("drawcord_aglet_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletWidthMm": oapi.client.format_argument_value(
                    "drawcordAgletWidthMm",
                    kwargs.get("drawcord_aglet_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletHeightMm": oapi.client.format_argument_value(
                    "drawcordAgletHeightMm",
                    kwargs.get("drawcord_aglet_height_mm", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletInternalDiameterMm": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletInternalDiameterMm",
                    kwargs.get("drawcord_aglet_internal_diameter_mm", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletGramsPerThousandPieces": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletGramsPerThousandPieces",
                    kwargs.get("drawcord_aglet_grams_per_thousand_pieces", None),  # noqa
                    style="form",
                    explode=False,
                ),
                "drawcordAgletFinishProcess": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletFinishProcess",
                    kwargs.get("drawcord_aglet_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletDyeMethod": oapi.client.format_argument_value(
                    "drawcordAgletDyeMethod",
                    kwargs.get("drawcord_aglet_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletArtworkTechnique",
                    kwargs.get("drawcord_aglet_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletVisualEffect": oapi.client.format_argument_value(
                    "drawcordAgletVisualEffect",
                    kwargs.get("drawcord_aglet_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "drawcordAgletNumberOfColors": oapi.client.format_argument_value(  # noqa
                    "drawcordAgletNumberOfColors",
                    kwargs.get("drawcord_aglet_number_of_colors", None),
                    style="form",
                    explode=False,
                ),
                "hookType": oapi.client.format_argument_value(
                    "hookType",
                    kwargs.get("hook_type", None),
                    style="form",
                    explode=False,
                ),
                "hookLoopType": oapi.client.format_argument_value(
                    "hookLoopType",
                    kwargs.get("hook_loop_type", None),
                    style="form",
                    explode=False,
                ),
                "labelType": oapi.client.format_argument_value(
                    "labelType",
                    kwargs.get("label_type", None),
                    style="form",
                    explode=False,
                ),
                "foldMethod": oapi.client.format_argument_value(
                    "foldMethod",
                    kwargs.get("fold_method", None),
                    style="form",
                    explode=False,
                ),
                "labelTwillDirection": oapi.client.format_argument_value(
                    "labelTwillDirection",
                    kwargs.get("label_twill_direction", None),
                    style="form",
                    explode=False,
                ),
                "backingType": oapi.client.format_argument_value(
                    "backingType",
                    kwargs.get("backing_type", None),
                    style="form",
                    explode=False,
                ),
                "logoSize": oapi.client.format_argument_value(
                    "logoSize",
                    kwargs.get("logo_size", None),
                    style="form",
                    explode=False,
                ),
                "agletMaterialItem": oapi.client.format_argument_value(
                    "agletMaterialItem",
                    kwargs.get("aglet_material_item", None),
                    style="form",
                    explode=False,
                ),
                "hasAgletIndicator": oapi.client.format_argument_value(
                    "hasAgletIndicator",
                    kwargs.get("has_aglet_indicator", None),
                    style="form",
                    explode=False,
                ),
                "numberOfBundles": oapi.client.format_argument_value(
                    "numberOfBundles",
                    kwargs.get("number_of_bundles", None),
                    style="form",
                    explode=False,
                ),
                "tipContent": oapi.client.format_argument_value(
                    "tipContent",
                    kwargs.get("tip_content", None),
                    style="form",
                    explode=False,
                ),
                "tipType": oapi.client.format_argument_value(
                    "tipType",
                    kwargs.get("tip_type", None),
                    style="form",
                    explode=False,
                ),
                "magnetCoverType": oapi.client.format_argument_value(
                    "magnetCoverType",
                    kwargs.get("magnet_cover_type", None),
                    style="form",
                    explode=False,
                ),
                "paddingType": oapi.client.format_argument_value(
                    "paddingType",
                    kwargs.get("padding_type", None),
                    style="form",
                    explode=False,
                ),
                "paddingOrientation": oapi.client.format_argument_value(
                    "paddingOrientation",
                    kwargs.get("padding_orientation", None),
                    style="form",
                    explode=False,
                ),
                "layerLocation": oapi.client.format_argument_value(
                    "layerLocation",
                    kwargs.get("layer_location", None),
                    style="form",
                    explode=False,
                ),
                "materialConstruction": oapi.client.format_argument_value(
                    "materialConstruction",
                    kwargs.get("material_construction", None),
                    style="form",
                    explode=False,
                ),
                "layerFinishProcess": oapi.client.format_argument_value(
                    "layerFinishProcess",
                    kwargs.get("layer_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "layerArtworkTechnique": oapi.client.format_argument_value(
                    "layerArtworkTechnique",
                    kwargs.get("layer_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "layerContentPercentage": oapi.client.format_argument_value(
                    "layerContentPercentage",
                    kwargs.get("layer_content_percentage", None),
                    style="form",
                    explode=False,
                ),
                "layerContentType": oapi.client.format_argument_value(
                    "layerContentType",
                    kwargs.get("layer_content_type", None),
                    style="form",
                    explode=False,
                ),
                "layerContentSource": oapi.client.format_argument_value(
                    "layerContentSource",
                    kwargs.get("layer_content_source", None),
                    style="form",
                    explode=False,
                ),
                "pinBadgeType": oapi.client.format_argument_value(
                    "pinBadgeType",
                    kwargs.get("pin_badge_type", None),
                    style="form",
                    explode=False,
                ),
                "plateOrientation": oapi.client.format_argument_value(
                    "plateOrientation",
                    kwargs.get("plate_orientation", None),
                    style="form",
                    explode=False,
                ),
                "moldIdentifier": oapi.client.format_argument_value(
                    "moldIdentifier",
                    kwargs.get("mold_identifier", None),
                    style="form",
                    explode=False,
                ),
                "ringType": oapi.client.format_argument_value(
                    "ringType",
                    kwargs.get("ring_type", None),
                    style="form",
                    explode=False,
                ),
                "bondedIndicator": oapi.client.format_argument_value(
                    "bondedIndicator",
                    kwargs.get("bonded_indicator", None),
                    style="form",
                    explode=False,
                ),
                "lubricatedIndicator": oapi.client.format_argument_value(
                    "lubricatedIndicator",
                    kwargs.get("lubricated_indicator", None),
                    style="form",
                    explode=False,
                ),
                "threadPly": oapi.client.format_argument_value(
                    "threadPly",
                    kwargs.get("thread_ply", None),
                    style="form",
                    explode=False,
                ),
                "threadSize": oapi.client.format_argument_value(
                    "threadSize",
                    kwargs.get("thread_size", None),
                    style="form",
                    explode=False,
                ),
                "alternateThreadSize": oapi.client.format_argument_value(
                    "alternateThreadSize",
                    kwargs.get("alternate_thread_size", None),
                    style="form",
                    explode=False,
                ),
                "threadType": oapi.client.format_argument_value(
                    "threadType",
                    kwargs.get("thread_type", None),
                    style="form",
                    explode=False,
                ),
                "threadBrandName": oapi.client.format_argument_value(
                    "threadBrandName",
                    kwargs.get("thread_brand_name", None),
                    style="form",
                    explode=False,
                ),
                "threadNumberSystem": oapi.client.format_argument_value(
                    "threadNumberSystem",
                    kwargs.get("thread_number_system", None),
                    style="form",
                    explode=False,
                ),
                "threadPreparation": oapi.client.format_argument_value(
                    "threadPreparation",
                    kwargs.get("thread_preparation", None),
                    style="form",
                    explode=False,
                ),
                "threadFilamentCount": oapi.client.format_argument_value(
                    "threadFilamentCount",
                    kwargs.get("thread_filament_count", None),
                    style="form",
                    explode=False,
                ),
                "threadPlyCount": oapi.client.format_argument_value(
                    "threadPlyCount",
                    kwargs.get("thread_ply_count", None),
                    style="form",
                    explode=False,
                ),
                "threadLuster": oapi.client.format_argument_value(
                    "threadLuster",
                    kwargs.get("thread_luster", None),
                    style="form",
                    explode=False,
                ),
                "threadStatementContent": oapi.client.format_argument_value(
                    "threadStatementContent",
                    kwargs.get("thread_statement_content", None),
                    style="form",
                    explode=False,
                ),
                "zipperType": oapi.client.format_argument_value(
                    "zipperType",
                    kwargs.get("zipper_type", None),
                    style="form",
                    explode=False,
                ),
                "zipInCompatibleIndicator": oapi.client.format_argument_value(
                    "zipInCompatibleIndicator",
                    kwargs.get("zip_in_compatible_indicator", None),
                    style="form",
                    explode=False,
                ),
                "zipperPerformance": oapi.client.format_argument_value(
                    "zipperPerformance",
                    kwargs.get("zipper_performance", None),
                    style="form",
                    explode=False,
                ),
                "zipperBrand": oapi.client.format_argument_value(
                    "zipperBrand",
                    kwargs.get("zipper_brand", None),
                    style="form",
                    explode=False,
                ),
                "sliderPullLogoName": oapi.client.format_argument_value(
                    "sliderPullLogoName",
                    kwargs.get("slider_pull_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "sliderLockingFunction": oapi.client.format_argument_value(
                    "sliderLockingFunction",
                    kwargs.get("slider_locking_function", None),
                    style="form",
                    explode=False,
                ),
                "sliderQuantity": oapi.client.format_argument_value(
                    "sliderQuantity",
                    kwargs.get("slider_quantity", None),
                    style="form",
                    explode=False,
                ),
                "sliderOrientation": oapi.client.format_argument_value(
                    "sliderOrientation",
                    kwargs.get("slider_orientation", None),
                    style="form",
                    explode=False,
                ),
                "sliderVisualEffect": oapi.client.format_argument_value(
                    "sliderVisualEffect",
                    kwargs.get("slider_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "sliderPullFinishProcess": oapi.client.format_argument_value(
                    "sliderPullFinishProcess",
                    kwargs.get("slider_pull_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "sliderPullArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "sliderPullArtworkTechnique",
                    kwargs.get("slider_pull_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "zipperPullCode": oapi.client.format_argument_value(
                    "zipperPullCode",
                    kwargs.get("zipper_pull_code", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeConstructionType": oapi.client.format_argument_value(  # noqa
                    "zipperTapeConstructionType",
                    kwargs.get("zipper_tape_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeLogoName": oapi.client.format_argument_value(
                    "zipperTapeLogoName",
                    kwargs.get("zipper_tape_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeWidthMm": oapi.client.format_argument_value(
                    "zipperTapeWidthMm",
                    kwargs.get("zipper_tape_width_mm", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeFinishProcess": oapi.client.format_argument_value(
                    "zipperTapeFinishProcess",
                    kwargs.get("zipper_tape_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeDyeMethod": oapi.client.format_argument_value(
                    "zipperTapeDyeMethod",
                    kwargs.get("zipper_tape_dye_method", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeArtworkTechnique": oapi.client.format_argument_value(  # noqa
                    "zipperTapeArtworkTechnique",
                    kwargs.get("zipper_tape_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeArtworkGraphic": oapi.client.format_argument_value(
                    "zipperTapeArtworkGraphic",
                    kwargs.get("zipper_tape_artwork_graphic", None),
                    style="form",
                    explode=False,
                ),
                "zipperTapeVisualEffect": oapi.client.format_argument_value(
                    "zipperTapeVisualEffect",
                    kwargs.get("zipper_tape_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "teethType": oapi.client.format_argument_value(
                    "teethType",
                    kwargs.get("teeth_type", None),
                    style="form",
                    explode=False,
                ),
                "specialZipperTeethOrientation": oapi.client.format_argument_value(  # noqa
                    "specialZipperTeethOrientation",
                    kwargs.get("special_zipper_teeth_orientation", None),
                    style="form",
                    explode=False,
                ),
                "teethSize": oapi.client.format_argument_value(
                    "teethSize",
                    kwargs.get("teeth_size", None),
                    style="form",
                    explode=False,
                ),
                "teethShape": oapi.client.format_argument_value(
                    "teethShape",
                    kwargs.get("teeth_shape", None),
                    style="form",
                    explode=False,
                ),
                "teethRepeatLengthMm": oapi.client.format_argument_value(
                    "teethRepeatLengthMm",
                    kwargs.get("teeth_repeat_length_mm", None),
                    style="form",
                    explode=False,
                ),
                "teethFinishProcess": oapi.client.format_argument_value(
                    "teethFinishProcess",
                    kwargs.get("teeth_finish_process", None),
                    style="form",
                    explode=False,
                ),
                "teethArtworkTechnique": oapi.client.format_argument_value(
                    "teethArtworkTechnique",
                    kwargs.get("teeth_artwork_technique", None),
                    style="form",
                    explode=False,
                ),
                "teethVisualEffect": oapi.client.format_argument_value(
                    "teethVisualEffect",
                    kwargs.get("teeth_visual_effect", None),
                    style="form",
                    explode=False,
                ),
                "contrastThreadForCoilIndicator": oapi.client.format_argument_value(  # noqa
                    "contrastThreadForCoilIndicator",
                    kwargs.get("contrast_thread_for_coil_indicator", None),
                    style="form",
                    explode=False,
                ),
                "teethMultiColoredIndicator": oapi.client.format_argument_value(  # noqa
                    "teethMultiColoredIndicator",
                    kwargs.get("teeth_multi_colored_indicator", None),
                    style="form",
                    explode=False,
                ),
                "zipperStopType": oapi.client.format_argument_value(
                    "zipperStopType",
                    kwargs.get("zipper_stop_type", None),
                    style="form",
                    explode=False,
                ),
                "zipperStopLogoName": oapi.client.format_argument_value(
                    "zipperStopLogoName",
                    kwargs.get("zipper_stop_logo_name", None),
                    style="form",
                    explode=False,
                ),
                "zipperStopLogoPlacement": oapi.client.format_argument_value(
                    "zipperStopLogoPlacement",
                    kwargs.get("zipper_stop_logo_placement", None),
                    style="form",
                    explode=False,
                ),
                "agletConstructionType": oapi.client.format_argument_value(
                    "agletConstructionType",
                    kwargs.get("aglet_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "airbagProcess": oapi.client.format_argument_value(
                    "airbagProcess",
                    kwargs.get("airbag_process", None),
                    style="form",
                    explode=False,
                ),
                "airbagType": oapi.client.format_argument_value(
                    "airbagType",
                    kwargs.get("airbag_type", None),
                    style="form",
                    explode=False,
                ),
                "colorationAvailable": oapi.client.format_argument_value(
                    "colorationAvailable",
                    kwargs.get("coloration_available", None),
                    style="form",
                    explode=False,
                ),
                "gasContent": oapi.client.format_argument_value(
                    "gasContent",
                    kwargs.get("gas_content", None),
                    style="form",
                    explode=False,
                ),
                "fillType": oapi.client.format_argument_value(
                    "fillType",
                    kwargs.get("fill_type", None),
                    style="form",
                    explode=False,
                ),
                "scrim": oapi.client.format_argument_value(
                    "scrim",
                    kwargs.get("scrim", None),
                    style="form",
                    explode=False,
                ),
                "downClusterStatement": oapi.client.format_argument_value(
                    "downClusterStatement",
                    kwargs.get("down_cluster_statement", None),
                    style="form",
                    explode=False,
                ),
                "fillPower": oapi.client.format_argument_value(
                    "fillPower",
                    kwargs.get("fill_power", None),
                    style="form",
                    explode=False,
                ),
                "naturalDownColor": oapi.client.format_argument_value(
                    "naturalDownColor",
                    kwargs.get("natural_down_color", None),
                    style="form",
                    explode=False,
                ),
                "fillForm": oapi.client.format_argument_value(
                    "fillForm",
                    kwargs.get("fill_form", None),
                    style="form",
                    explode=False,
                ),
                "heatSet": oapi.client.format_argument_value(
                    "heatSet",
                    kwargs.get("heat_set", None),
                    style="form",
                    explode=False,
                ),
                "vendorSuppliedIndicator": oapi.client.format_argument_value(
                    "vendorSuppliedIndicator",
                    kwargs.get("vendor_supplied_indicator", None),
                    style="form",
                    explode=False,
                ),
                "corporateDesignationIndicator": oapi.client.format_argument_value(  # noqa
                    "corporateDesignationIndicator",
                    kwargs.get("corporate_designation_indicator", None),
                    style="form",
                    explode=False,
                ),
                "confidentialIndicator": oapi.client.format_argument_value(
                    "confidentialIndicator",
                    kwargs.get("confidential_indicator", None),
                    style="form",
                    explode=False,
                ),
                "countryOfOriginStatementIndicator": oapi.client.format_argument_value(  # noqa
                    "countryOfOriginStatementIndicator",
                    kwargs.get("country_of_origin_statement_indicator", None),
                    style="form",
                    explode=False,
                ),
                "sizeMatrixIndicator": oapi.client.format_argument_value(
                    "sizeMatrixIndicator",
                    kwargs.get("size_matrix_indicator", None),
                    style="form",
                    explode=False,
                ),
                "containsCorporateLogoIndicator": oapi.client.format_argument_value(  # noqa
                    "containsCorporateLogoIndicator",
                    kwargs.get("contains_corporate_logo_indicator", None),
                    style="form",
                    explode=False,
                ),
                "packagingIntent": oapi.client.format_argument_value(
                    "packagingIntent",
                    kwargs.get("packaging_intent", None),
                    style="form",
                    explode=False,
                ),
                "packagingStatement": oapi.client.format_argument_value(
                    "packagingStatement",
                    kwargs.get("packaging_statement", None),
                    style="form",
                    explode=False,
                ),
                "cardType": oapi.client.format_argument_value(
                    "cardType",
                    kwargs.get("card_type", None),
                    style="form",
                    explode=False,
                ),
                "cardConstructionType": oapi.client.format_argument_value(
                    "cardConstructionType",
                    kwargs.get("card_construction_type", None),
                    style="form",
                    explode=False,
                ),
                "flutingSize": oapi.client.format_argument_value(
                    "flutingSize",
                    kwargs.get("fluting_size", None),
                    style="form",
                    explode=False,
                ),
                "innerLinerboardBasisWeight": oapi.client.format_argument_value(  # noqa
                    "innerLinerboardBasisWeight",
                    kwargs.get("inner_linerboard_basis_weight", None),
                    style="form",
                    explode=False,
                ),
                "innerLinerboardType": oapi.client.format_argument_value(
                    "innerLinerboardType",
                    kwargs.get("inner_linerboard_type", None),
                    style="form",
                    explode=False,
                ),
                "mediumPaperBasisWeight": oapi.client.format_argument_value(
                    "mediumPaperBasisWeight",
                    kwargs.get("medium_paper_basis_weight", None),
                    style="form",
                    explode=False,
                ),
                "mediumPaperType": oapi.client.format_argument_value(
                    "mediumPaperType",
                    kwargs.get("medium_paper_type", None),
                    style="form",
                    explode=False,
                ),
                "outerLinerboardBasisWeight": oapi.client.format_argument_value(  # noqa
                    "outerLinerboardBasisWeight",
                    kwargs.get("outer_linerboard_basis_weight", None),
                    style="form",
                    explode=False,
                ),
                "outerLinerboardType": oapi.client.format_argument_value(
                    "outerLinerboardType",
                    kwargs.get("outer_linerboard_type", None),
                    style="form",
                    explode=False,
                ),
                "fastenerType": oapi.client.format_argument_value(
                    "fastenerType",
                    kwargs.get("fastener_type", None),
                    style="form",
                    explode=False,
                ),
                "hangerType": oapi.client.format_argument_value(
                    "hangerType",
                    kwargs.get("hanger_type", None),
                    style="form",
                    explode=False,
                ),
                "hangtagType": oapi.client.format_argument_value(
                    "hangtagType",
                    kwargs.get("hangtag_type", None),
                    style="form",
                    explode=False,
                ),
                "partitionType": oapi.client.format_argument_value(
                    "partitionType",
                    kwargs.get("partition_type", None),
                    style="form",
                    explode=False,
                ),
                "shoebagType": oapi.client.format_argument_value(
                    "shoebagType",
                    kwargs.get("shoebag_type", None),
                    style="form",
                    explode=False,
                ),
                "shoeFormType": oapi.client.format_argument_value(
                    "shoeFormType",
                    kwargs.get("shoe_form_type", None),
                    style="form",
                    explode=False,
                ),
                "stickerType": oapi.client.format_argument_value(
                    "stickerType",
                    kwargs.get("sticker_type", None),
                    style="form",
                    explode=False,
                ),
                "tissueType": oapi.client.format_argument_value(
                    "tissueType",
                    kwargs.get("tissue_type", None),
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DistinctResponse,
            )
        )

    def get_material_management_data_supplied_materials_object_id_relationships(  # noqa
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.RelationshipResponse:
        """
        How you get all the relationships to the single object requested, in
        other words the children in the hierarchy to the requested entity

        Parameters:

        - object_id:
          The Id of the object (in this case Supplied Material) where the
          relationships are desired
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/suppliedMaterials/{objectId}/relationships".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.RelationshipResponse,
            )
        )

    def get_material_procurement_data_material_prices_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.MaterialProcurementDataMaterialPricesObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.MaterialPricesResponse:
        """
        How you get a single material price.

        Parameters:

        - object_id:
          A single Id of the object (in this case Material Pricing)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/materialPrices/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.MaterialPricesResponse,
            )
        )

    def get_material_procurement_data_material_prices(
        self,
        object_id: model.MaterialProcurementDataMaterialPricesGetObjectId,
        *,
        dataunits: typing.Optional[
            model.MaterialProcurementDataMaterialPricesGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.MaterialPricesBulkResponse:
        """
        How you get material price in a Bulk fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Material
          Pricing)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/materialPrices",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "objectId": oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                ),
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.MaterialPricesBulkResponse,
            )
        )

    def get_material_management_data_material_palettes_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.MaterialManagementDataMaterialPalettesObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.MaterialPaletteResponse:
        """
        How you get a single palette data for material and material color.

        Parameters:

        - object_id:
          A single Id of the object (in this case Palette ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialPalettes/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.MaterialPaletteResponse,
            )
        )

    def get_material_management_data_material_palettes(
        self,
        object_id: model.MaterialManagementDataMaterialPalettesGetObjectId,
        *,
        dataunits: typing.Optional[
            model.MaterialManagementDataMaterialPalettesGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.MaterialPaletteBulkResponse:
        """
        How you get a single palette data for material and material color in a
        Bulk Fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Palette ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialPalettes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "objectId": oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                ),
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.MaterialPaletteBulkResponse,
            )
        )

    def get_material_management_data_material_palettes_object_id_relationships(
        self,
        object_id: int,
        *,
        depth: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.RelationshipResponse:
        """
        How you get all the relationships to the single object requested, in
        other words the children in the hierarchy to the requested entity

        Parameters:

        - object_id:
          The Id of the object (in this case Palette Id) where the
          relationships are desired
        - depth:
          This determines how many levels in the hierarcy you wish to traverse,
          default is 2
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialPalettes/{objectId}/relationships".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "depth": oapi.client.format_argument_value(
                    "depth",
                    depth,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.RelationshipResponse,
            )
        )

    def get_material_management_search_material_palettes(
        self,
        *,
        count: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
        q: typing.Optional[
            str
        ] = "",
        cycle_year: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetCycleYear
        ] = None,
        palette_type: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetPaletteType
        ] = None,
        material: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetMaterial
        ] = None,
        supplied_material: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetSuppliedMaterial
        ] = None,
        palette_material_category: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetPaletteMaterialCategory  # noqa
        ] = None,
        color: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetColor
        ] = None,
        supplied_material_color_identifier: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetSuppliedMaterialColorIdentifier  # noqa
        ] = None,
        supplied_material_multi_color_code: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetSuppliedMaterialMultiColorCode  # noqa
        ] = None,
        supplied_material_color_is_multiple_colors: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetSuppliedMaterialColorIsMultipleColors  # noqa
        ] = None,
        team_player_graphic_identifier: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetTeamPlayerGraphicIdentifier  # noqa
        ] = None,
        supplied_material_team_player_graphic_identifier: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetSuppliedMaterialTeamPlayerGraphicIdentifier  # noqa
        ] = None,
        parent_material_palette_identifier: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetParentMaterialPaletteIdentifier  # noqa
        ] = None,
        division: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetDivision
        ] = None,
        sub_palette_content: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetSubPaletteContent
        ] = None,
        development_team_group: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetDevelopmentTeamGroup  # noqa
        ] = None,
        development_team: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetDevelopmentTeam
        ] = None,
        business_designation: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetBusinessDesignation  # noqa
        ] = None,
        material_palette_state: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetMaterialPaletteState  # noqa
        ] = None,
        material_palette_status_indicator: typing.Optional[
            bool
        ] = None,
        published_date: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesGetPublishedDate
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the Material Palette
        entity

        Parameters:

        - count:
          Number of entries the API should attempt to fetch, default is 10
        - offset:
          Offset of the entries the API should attempt to fetch, default is 0
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        - q:
          This parameter is how you pass free text search, if any string is
          passed here it will be searched as free text
        - cycle_year:
          The reference key associated with this item: No Definition Available
        - palette_type:
          The reference key associated with this item: value: master palette;
          sub-palette
        - material:
          The reference key associated with this item: No Definition Available
        - supplied_material:
          The reference key associated with this item: No Definition Available
        - palette_material_category
        - color:
          The reference key associated with this item: No Definition Available
        - supplied_material_color_identifier:
          The reference key associated with this item: No Definition Available
        - supplied_material_multi_color_code
        - supplied_material_color_is_multiple_colors:
          The reference key associated with this item: No Definition Available
        - team_player_graphic_identifier:
          The reference key associated with this item: No Definition Available
        - supplied_material_team_player_graphic_identifier:
          The reference key associated with this item: No Definition Available
        - parent_material_palette_identifier:
          The reference key associated with this item: No Definition Available
        - division:
          The reference key associated with this item: No Definition Available
        - sub_palette_content:
          The reference key associated with this item: No Definition Available
        - development_team_group:
          The reference key associated with this item: No Definition Available
        - development_team:
          The reference key associated with this item: No Definition Available
        - business_designation:
          The reference key associated with this item: No Definition Available
        - material_palette_state:
          The reference key associated with this item: No Definition Available
        - material_palette_status_indicator:
          The true or false flag associated with this item: No Definition
          Available
        - published_date:
          The reference key associated with this item: No Definition Available
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/search/materialPalettes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "count": oapi.client.format_argument_value(
                    "count",
                    count,
                    style="form",
                    explode=False,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=False,
                ),
                "q": oapi.client.format_argument_value(
                    "q",
                    q,
                    style="form",
                    explode=False,
                ),
                "cycleYear": oapi.client.format_argument_value(
                    "cycleYear",
                    cycle_year,
                    style="form",
                    explode=False,
                ),
                "paletteType": oapi.client.format_argument_value(
                    "paletteType",
                    palette_type,
                    style="form",
                    explode=False,
                ),
                "material": oapi.client.format_argument_value(
                    "material",
                    material,
                    style="form",
                    explode=False,
                ),
                "suppliedMaterial": oapi.client.format_argument_value(
                    "suppliedMaterial",
                    supplied_material,
                    style="form",
                    explode=False,
                ),
                "paletteMaterialCategory": oapi.client.format_argument_value(
                    "paletteMaterialCategory",
                    palette_material_category,
                    style="form",
                    explode=False,
                ),
                "color": oapi.client.format_argument_value(
                    "color",
                    color,
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorIdentifier": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorIdentifier",
                    supplied_material_color_identifier,
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialMultiColorCode": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialMultiColorCode",
                    supplied_material_multi_color_code,
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorIsMultipleColors": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorIsMultipleColors",
                    supplied_material_color_is_multiple_colors,
                    style="form",
                    explode=False,
                ),
                "teamPlayerGraphicIdentifier": oapi.client.format_argument_value(  # noqa
                    "teamPlayerGraphicIdentifier",
                    team_player_graphic_identifier,
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialTeamPlayerGraphicIdentifier": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialTeamPlayerGraphicIdentifier",
                    supplied_material_team_player_graphic_identifier,
                    style="form",
                    explode=False,
                ),
                "parentMaterialPaletteIdentifier": oapi.client.format_argument_value(  # noqa
                    "parentMaterialPaletteIdentifier",
                    parent_material_palette_identifier,
                    style="form",
                    explode=False,
                ),
                "division": oapi.client.format_argument_value(
                    "division",
                    division,
                    style="form",
                    explode=False,
                ),
                "subPaletteContent": oapi.client.format_argument_value(
                    "subPaletteContent",
                    sub_palette_content,
                    style="form",
                    explode=False,
                ),
                "developmentTeamGroup": oapi.client.format_argument_value(
                    "developmentTeamGroup",
                    development_team_group,
                    style="form",
                    explode=False,
                ),
                "developmentTeam": oapi.client.format_argument_value(
                    "developmentTeam",
                    development_team,
                    style="form",
                    explode=False,
                ),
                "businessDesignation": oapi.client.format_argument_value(
                    "businessDesignation",
                    business_designation,
                    style="form",
                    explode=False,
                ),
                "materialPaletteState": oapi.client.format_argument_value(
                    "materialPaletteState",
                    material_palette_state,
                    style="form",
                    explode=False,
                ),
                "materialPaletteStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "materialPaletteStatusIndicator",
                    material_palette_status_indicator,
                    style="form",
                    explode=False,
                ),
                "publishedDate": oapi.client.format_argument_value(
                    "publishedDate",
                    published_date,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SearchResponse,
            )
        )

    def get_material_management_search_material_palettes_distinct_values(
        self,
        node: str,
        *,
        division: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesDistinctValuesGetDivision  # noqa
        ] = None,
        cycle_year: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesDistinctValuesGetCycleYear  # noqa
        ] = None,
        development_team_group: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesDistinctValuesGetDevelopmentTeamGroup  # noqa
        ] = None,
        development_team: typing.Optional[
            model.MaterialManagementSearchMaterialPalettesDistinctValuesGetDevelopmentTeam  # noqa
        ] = None,
    ) -> model.DistinctValuesResponse:
        """
        How you search for distinct values for a specific field/node in the
        material palette

        Parameters:

        - node:
          The node or attribute where you want the distinct possible values
          that would be desired
        - division:
          The reference key associated with this item: No Definition Available
        - cycle_year:
          The reference key associated with this item: No Definition Available
        - development_team_group:
          The reference key associated with this item: No Definition Available
        - development_team:
          The reference key associated with this item: No Definition Available
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/search/materialPalettes/distinctValues",
            method="GET",
            query={
                "node": oapi.client.format_argument_value(
                    "node",
                    node,
                    style="form",
                    explode=False,
                ),
                "division": oapi.client.format_argument_value(
                    "division",
                    division,
                    style="form",
                    explode=False,
                ),
                "cycleYear": oapi.client.format_argument_value(
                    "cycleYear",
                    cycle_year,
                    style="form",
                    explode=False,
                ),
                "developmentTeamGroup": oapi.client.format_argument_value(
                    "developmentTeamGroup",
                    development_team_group,
                    style="form",
                    explode=False,
                ),
                "developmentTeam": oapi.client.format_argument_value(
                    "developmentTeam",
                    development_team,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DistinctValuesResponse,
            )
        )

    def get_material_management_data_material_boms_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.MaterialManagementDataMaterialBOMsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.MaterialBOMResponse:
        """
        How you get a single Material BOM with the line item details

        Parameters:

        - object_id:
          A single Id of the object (in this case Material ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialBOMs/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.MaterialBOMResponse,
            )
        )

    def get_material_management_data_material_boms(
        self,
        object_id: model.MaterialManagementDataMaterialBOMsGetObjectId,
        *,
        dataunits: typing.Optional[
            model.MaterialManagementDataMaterialBOMsGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.MaterialBOMBulkResponse:
        """
        How you get a single Material BOM with the line item details in a Bulk
        Fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Material ID
          )
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialBOMs",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "objectId": oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                ),
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.MaterialBOMBulkResponse,
            )
        )

    def get_material_management_search_material_boms(
        self,
        *,
        count: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
        q: typing.Optional[
            str
        ] = "",
        bom_identifier: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetBomIdentifier
        ] = None,
        bom_name: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetBomName
        ] = None,
        bom_description: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetBomDescription
        ] = None,
        bom_comment: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetBomComment
        ] = None,
        bom_line_item_identifier: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetBomLineItemIdentifier
        ] = None,
        line_item_material: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetLineItemMaterial
        ] = None,
        line_item_supplied_material: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetLineItemSuppliedMaterial  # noqa
        ] = None,
        line_item_color: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetLineItemColor
        ] = None,
        line_item_supplied_material_color: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetLineItemSuppliedMaterialColor  # noqa
        ] = None,
        line_item_supplied_material_multi_color_code: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetLineItemSuppliedMaterialMultiColorCode  # noqa
        ] = None,
        line_item_supplied_material_color_is_multiple_colors: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetLineItemSuppliedMaterialColorIsMultipleColors  # noqa
        ] = None,
        quantity_grams: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetQuantityGrams
        ] = None,
        color_position: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetColorPosition
        ] = None,
        part_name: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetPartName
        ] = None,
        feeder_left: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetFeederLeft
        ] = None,
        feeder_right: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetFeederRight
        ] = None,
        bobbin_position_left: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetBobbinPositionLeft
        ] = None,
        bobbin_position_right: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetBobbinPositionRight
        ] = None,
        placement: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetPlacement
        ] = None,
        bom_status_indicator: typing.Optional[
            model.MaterialManagementSearchMaterialBOMsGetBomStatusIndicator
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the Material BOM
        entity

        Parameters:

        - count:
          Number of entries the API should attempt to fetch, default is 10
        - offset:
          Offset of the entries the API should attempt to fetch, default is 0
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        - q:
          This parameter is how you pass free text search, if any string is
          passed here it will be searched as free text
        - bom_identifier:
          The reference key associated with this item: No Definition Available
        - bom_name:
          The reference key associated with this item: No Definition Available
        - bom_description:
          The reference key associated with this item: No Definition Available
        - bom_comment:
          The reference key associated with this item: No Definition Available
        - bom_line_item_identifier:
          The reference key associated with this item: BOM Line Item Identifier
          in the BOM Line Item Details
        - line_item_material:
          The reference key associated with this item: Material Identifier in
          the BOM Line Item Details
        - line_item_supplied_material:
          The reference key associated with this item: Supplied Material
          Identifier in the BOM Line Item Details
        - line_item_color:
          The reference key associated with this item: Color Identifier in the
          BOM Line Item Details
        - line_item_supplied_material_color:
          The reference key associated with this item: Supplied Material Color
          Identifier in the BOM Line Item Details
        - line_item_supplied_material_multi_color_code:
          The reference key associated with this item: Supplied Material Multi
          Color Name in the BOM Line Item Details
        - line_item_supplied_material_color_is_multiple_colors:
          The reference key associated with this item: Supplied Material Color
          Multi Color Indicator in the BOM Line Item Details
        - quantity_grams:
          The reference key associated with this item: Weight in Grams for the
          particular material in the BOM Line Item Details
        - color_position:
          The reference key associated with this item: No Definition Available
        - part_name:
          The reference key associated with this item: No Definition Available
        - feeder_left:
          The reference key associated with this item: No Definition Available
        - feeder_right:
          The reference key associated with this item: No Definition Available
        - bobbin_position_left:
          The reference key associated with this item: No Definition Available
        - bobbin_position_right:
          The reference key associated with this item: No Definition Available
        - placement:
          The reference key associated with this item: No Definition Available
        - bom_status_indicator:
          The reference key associated with this item: No Definition Available
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/search/materialBOMs",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "count": oapi.client.format_argument_value(
                    "count",
                    count,
                    style="form",
                    explode=False,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=False,
                ),
                "q": oapi.client.format_argument_value(
                    "q",
                    q,
                    style="form",
                    explode=False,
                ),
                "bomIdentifier": oapi.client.format_argument_value(
                    "bomIdentifier",
                    bom_identifier,
                    style="form",
                    explode=False,
                ),
                "bomName": oapi.client.format_argument_value(
                    "bomName",
                    bom_name,
                    style="form",
                    explode=False,
                ),
                "bomDescription": oapi.client.format_argument_value(
                    "bomDescription",
                    bom_description,
                    style="form",
                    explode=False,
                ),
                "bomComment": oapi.client.format_argument_value(
                    "bomComment",
                    bom_comment,
                    style="form",
                    explode=False,
                ),
                "bomLineItemIdentifier": oapi.client.format_argument_value(
                    "bomLineItemIdentifier",
                    bom_line_item_identifier,
                    style="form",
                    explode=False,
                ),
                "lineItemMaterial": oapi.client.format_argument_value(
                    "lineItemMaterial",
                    line_item_material,
                    style="form",
                    explode=False,
                ),
                "lineItemSuppliedMaterial": oapi.client.format_argument_value(
                    "lineItemSuppliedMaterial",
                    line_item_supplied_material,
                    style="form",
                    explode=False,
                ),
                "lineItemColor": oapi.client.format_argument_value(
                    "lineItemColor",
                    line_item_color,
                    style="form",
                    explode=False,
                ),
                "lineItemSuppliedMaterialColor": oapi.client.format_argument_value(  # noqa
                    "lineItemSuppliedMaterialColor",
                    line_item_supplied_material_color,
                    style="form",
                    explode=False,
                ),
                "lineItemSuppliedMaterialMultiColorCode": oapi.client.format_argument_value(  # noqa
                    "lineItemSuppliedMaterialMultiColorCode",
                    line_item_supplied_material_multi_color_code,
                    style="form",
                    explode=False,
                ),
                "lineItemSuppliedMaterialColorIsMultipleColors": oapi.client.format_argument_value(  # noqa
                    "lineItemSuppliedMaterialColorIsMultipleColors",
                    line_item_supplied_material_color_is_multiple_colors,
                    style="form",
                    explode=False,
                ),
                "quantityGrams": oapi.client.format_argument_value(
                    "quantityGrams",
                    quantity_grams,
                    style="form",
                    explode=False,
                ),
                "colorPosition": oapi.client.format_argument_value(
                    "colorPosition",
                    color_position,
                    style="form",
                    explode=False,
                ),
                "partName": oapi.client.format_argument_value(
                    "partName",
                    part_name,
                    style="form",
                    explode=False,
                ),
                "feederLeft": oapi.client.format_argument_value(
                    "feederLeft",
                    feeder_left,
                    style="form",
                    explode=False,
                ),
                "feederRight": oapi.client.format_argument_value(
                    "feederRight",
                    feeder_right,
                    style="form",
                    explode=False,
                ),
                "bobbinPositionLeft": oapi.client.format_argument_value(
                    "bobbinPositionLeft",
                    bobbin_position_left,
                    style="form",
                    explode=False,
                ),
                "bobbinPositionRight": oapi.client.format_argument_value(
                    "bobbinPositionRight",
                    bobbin_position_right,
                    style="form",
                    explode=False,
                ),
                "placement": oapi.client.format_argument_value(
                    "placement",
                    placement,
                    style="form",
                    explode=False,
                ),
                "bomStatusIndicator": oapi.client.format_argument_value(
                    "bomStatusIndicator",
                    bom_status_indicator,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SearchResponse,
            )
        )

    def get_material_management_data_supplied_material_boms_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.MaterialManagementDataSuppliedMaterialBOMsObjectIdGetDataunits  # noqa
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SuppliedMaterialBOMResponse:
        """
        How you get a single Supplied Material BOM with the line item details

        Parameters:

        - object_id:
          A single Id of the object (in this case Supplied Material ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/suppliedMaterialBOMs/{objectId}".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SuppliedMaterialBOMResponse,
            )
        )

    def get_material_management_data_supplied_material_boms(
        self,
        object_id: model.MaterialManagementDataSuppliedMaterialBOMsGetObjectId,
        *,
        dataunits: typing.Optional[
            model.MaterialManagementDataSuppliedMaterialBOMsGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SuppliedMaterialBOMBulkResponse:
        """
        How you get a single Supplied Material BOM with the line item details
        in a Bulk Fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Supplied
          Material ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/suppliedMaterialBOMs",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "objectId": oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                ),
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SuppliedMaterialBOMBulkResponse,
            )
        )

    def get_material_management_search_supplied_material_boms(
        self,
        *,
        count: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
        q: typing.Optional[
            str
        ] = "",
        bom_identifier: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetBomIdentifier
        ] = None,
        bom_name: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetBomName
        ] = None,
        bom_description: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetBomDescription
        ] = None,
        material: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetMaterial
        ] = None,
        bom_comment: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetBomComment
        ] = None,
        bom_line_item_identifier: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetBomLineItemIdentifier  # noqa
        ] = None,
        line_item_material: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetLineItemMaterial  # noqa
        ] = None,
        line_item_supplied_material: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetLineItemSuppliedMaterial  # noqa
        ] = None,
        line_item_color: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetLineItemColor
        ] = None,
        line_item_supplied_material_color: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetLineItemSuppliedMaterialColor  # noqa
        ] = None,
        line_item_supplied_material_multi_color_code: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetLineItemSuppliedMaterialMultiColorCode  # noqa
        ] = None,
        line_item_supplied_material_color_is_multiple_colors: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetLineItemSuppliedMaterialColorIsMultipleColors  # noqa
        ] = None,
        quantity_grams: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetQuantityGrams
        ] = None,
        color_position: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetColorPosition
        ] = None,
        part_name: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetPartName
        ] = None,
        feeder_left: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetFeederLeft
        ] = None,
        feeder_right: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetFeederRight
        ] = None,
        bobbin_position_left: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetBobbinPositionLeft  # noqa
        ] = None,
        bobbin_position_right: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetBobbinPositionRight  # noqa
        ] = None,
        placement: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetPlacement
        ] = None,
        bom_status_indicator: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialBOMsGetBomStatusIndicator  # noqa
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the Supplied
        Material BOM entity

        Parameters:

        - count:
          Number of entries the API should attempt to fetch, default is 10
        - offset:
          Offset of the entries the API should attempt to fetch, default is 0
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        - q:
          This parameter is how you pass free text search, if any string is
          passed here it will be searched as free text
        - bom_identifier:
          The reference key associated with this item: No Definition Available
        - bom_name:
          The reference key associated with this item: No Definition Available
        - bom_description:
          The reference key associated with this item: No Definition Available
        - material:
          The reference key associated with this item: Material Identifier in
          the BOM Header
        - bom_comment:
          The reference key associated with this item: No Definition Available
        - bom_line_item_identifier:
          The reference key associated with this item: BOM Line Item Identifier
          in the BOM Line Item Details
        - line_item_material:
          The reference key associated with this item: Material Identifier in
          the BOM Line Item Details
        - line_item_supplied_material:
          The reference key associated with this item: Supplied Material
          Identifier in the BOM Line Item Details
        - line_item_color:
          The reference key associated with this item: Color Identifier in the
          BOM Line Item Details
        - line_item_supplied_material_color:
          The reference key associated with this item: Supplied Material Color
          Identifier in the BOM Line Item Details
        - line_item_supplied_material_multi_color_code:
          The reference key associated with this item: Supplied Material Multi
          Color Name in the BOM Line Item Details
        - line_item_supplied_material_color_is_multiple_colors:
          The reference key associated with this item: Supplied Material Color
          Multi Color Indicator in the BOM Line Item Details
        - quantity_grams:
          The reference key associated with this item: Weight in Grams for the
          particular material in the BOM Line Item Details
        - color_position:
          The reference key associated with this item: No Definition Available
        - part_name:
          The reference key associated with this item: No Definition Available
        - feeder_left:
          The reference key associated with this item: No Definition Available
        - feeder_right:
          The reference key associated with this item: No Definition Available
        - bobbin_position_left:
          The reference key associated with this item: No Definition Available
        - bobbin_position_right:
          The reference key associated with this item: No Definition Available
        - placement:
          The reference key associated with this item: No Definition Available
        - bom_status_indicator:
          The reference key associated with this item: No Definition Available
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/search/suppliedMaterialBOMs",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "count": oapi.client.format_argument_value(
                    "count",
                    count,
                    style="form",
                    explode=False,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=False,
                ),
                "q": oapi.client.format_argument_value(
                    "q",
                    q,
                    style="form",
                    explode=False,
                ),
                "bomIdentifier": oapi.client.format_argument_value(
                    "bomIdentifier",
                    bom_identifier,
                    style="form",
                    explode=False,
                ),
                "bomName": oapi.client.format_argument_value(
                    "bomName",
                    bom_name,
                    style="form",
                    explode=False,
                ),
                "bomDescription": oapi.client.format_argument_value(
                    "bomDescription",
                    bom_description,
                    style="form",
                    explode=False,
                ),
                "material": oapi.client.format_argument_value(
                    "material",
                    material,
                    style="form",
                    explode=False,
                ),
                "bomComment": oapi.client.format_argument_value(
                    "bomComment",
                    bom_comment,
                    style="form",
                    explode=False,
                ),
                "bomLineItemIdentifier": oapi.client.format_argument_value(
                    "bomLineItemIdentifier",
                    bom_line_item_identifier,
                    style="form",
                    explode=False,
                ),
                "lineItemMaterial": oapi.client.format_argument_value(
                    "lineItemMaterial",
                    line_item_material,
                    style="form",
                    explode=False,
                ),
                "lineItemSuppliedMaterial": oapi.client.format_argument_value(
                    "lineItemSuppliedMaterial",
                    line_item_supplied_material,
                    style="form",
                    explode=False,
                ),
                "lineItemColor": oapi.client.format_argument_value(
                    "lineItemColor",
                    line_item_color,
                    style="form",
                    explode=False,
                ),
                "lineItemSuppliedMaterialColor": oapi.client.format_argument_value(  # noqa
                    "lineItemSuppliedMaterialColor",
                    line_item_supplied_material_color,
                    style="form",
                    explode=False,
                ),
                "lineItemSuppliedMaterialMultiColorCode": oapi.client.format_argument_value(  # noqa
                    "lineItemSuppliedMaterialMultiColorCode",
                    line_item_supplied_material_multi_color_code,
                    style="form",
                    explode=False,
                ),
                "lineItemSuppliedMaterialColorIsMultipleColors": oapi.client.format_argument_value(  # noqa
                    "lineItemSuppliedMaterialColorIsMultipleColors",
                    line_item_supplied_material_color_is_multiple_colors,
                    style="form",
                    explode=False,
                ),
                "quantityGrams": oapi.client.format_argument_value(
                    "quantityGrams",
                    quantity_grams,
                    style="form",
                    explode=False,
                ),
                "colorPosition": oapi.client.format_argument_value(
                    "colorPosition",
                    color_position,
                    style="form",
                    explode=False,
                ),
                "partName": oapi.client.format_argument_value(
                    "partName",
                    part_name,
                    style="form",
                    explode=False,
                ),
                "feederLeft": oapi.client.format_argument_value(
                    "feederLeft",
                    feeder_left,
                    style="form",
                    explode=False,
                ),
                "feederRight": oapi.client.format_argument_value(
                    "feederRight",
                    feeder_right,
                    style="form",
                    explode=False,
                ),
                "bobbinPositionLeft": oapi.client.format_argument_value(
                    "bobbinPositionLeft",
                    bobbin_position_left,
                    style="form",
                    explode=False,
                ),
                "bobbinPositionRight": oapi.client.format_argument_value(
                    "bobbinPositionRight",
                    bobbin_position_right,
                    style="form",
                    explode=False,
                ),
                "placement": oapi.client.format_argument_value(
                    "placement",
                    placement,
                    style="form",
                    explode=False,
                ),
                "bomStatusIndicator": oapi.client.format_argument_value(
                    "bomStatusIndicator",
                    bom_status_indicator,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SearchResponse,
            )
        )

    def get_material_management_data_supplied_material_color_boms_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.MaterialManagementDataSuppliedMaterialColorBOMsObjectIdGetDataunits  # noqa
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SuppliedMaterialColorBOMResponse:
        """
        How you get a single Supplied Material Color BOM with the line item
        details

        Parameters:

        - object_id:
          A single Id of the object (in this case Supplied Material Color ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/suppliedMaterialColorBOMs/{objectId}".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SuppliedMaterialColorBOMResponse,
            )
        )

    def get_material_management_data_supplied_material_color_boms(
        self,
        object_id: model.MaterialManagementDataSuppliedMaterialColorBOMsGetObjectId,  # noqa
        *,
        dataunits: typing.Optional[
            model.MaterialManagementDataSuppliedMaterialColorBOMsGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SuppliedMaterialColorBOMBulkResponse:
        """
        How you get a single Supplied Material Color BOM with the line item
        details in a Bulk Fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Supplied
          Material Color ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/suppliedMaterialColorBOMs",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "objectId": oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                ),
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SuppliedMaterialColorBOMBulkResponse,
            )
        )

    def get_material_management_search_supplied_material_color_boms(
        self,
        *,
        count: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
        q: typing.Optional[
            str
        ] = "",
        bom_identifier: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetBomIdentifier  # noqa
        ] = None,
        bom_name: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetBomName
        ] = None,
        bom_description: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetBomDescription  # noqa
        ] = None,
        material: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetMaterial
        ] = None,
        supplied_material: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetSuppliedMaterial  # noqa
        ] = None,
        color: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetColor
        ] = None,
        supplied_material_color_identifier: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetSuppliedMaterialColorIdentifier  # noqa
        ] = None,
        bom_comment: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetBomComment  # noqa
        ] = None,
        bom_line_item_identifier: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetBomLineItemIdentifier  # noqa
        ] = None,
        line_item_material: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetLineItemMaterial  # noqa
        ] = None,
        line_item_supplied_material: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetLineItemSuppliedMaterial  # noqa
        ] = None,
        line_item_color: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetLineItemColor  # noqa
        ] = None,
        line_item_supplied_material_color: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetLineItemSuppliedMaterialColor  # noqa
        ] = None,
        line_item_supplied_material_multi_color_code: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetLineItemSuppliedMaterialMultiColorCode  # noqa
        ] = None,
        line_item_supplied_material_color_is_multiple_colors: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetLineItemSuppliedMaterialColorIsMultipleColors  # noqa
        ] = None,
        quantity_grams: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetQuantityGrams  # noqa
        ] = None,
        color_position: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetColorPosition  # noqa
        ] = None,
        part_name: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetPartName
        ] = None,
        feeder_left: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetFeederLeft  # noqa
        ] = None,
        feeder_right: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetFeederRight  # noqa
        ] = None,
        bobbin_position_left: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetBobbinPositionLeft  # noqa
        ] = None,
        bobbin_position_right: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetBobbinPositionRight  # noqa
        ] = None,
        placement: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetPlacement
        ] = None,
        bom_status_indicator: typing.Optional[
            model.MaterialManagementSearchSuppliedMaterialColorBOMsGetBomStatusIndicator  # noqa
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the Supplied
        Material Color BOM entity

        Parameters:

        - count:
          Number of entries the API should attempt to fetch, default is 10
        - offset:
          Offset of the entries the API should attempt to fetch, default is 0
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        - q:
          This parameter is how you pass free text search, if any string is
          passed here it will be searched as free text
        - bom_identifier:
          The reference key associated with this item: No Definition Available
        - bom_name:
          The reference key associated with this item: No Definition Available
        - bom_description:
          The reference key associated with this item: No Definition Available
        - material:
          The reference key associated with this item: Material Identifier in
          the BOM Header
        - supplied_material:
          The reference key associated with this item: Material Identifier in
          the BOM Header
        - color:
          The reference key associated with this item: Color Identifier in the
          BOM Header
        - supplied_material_color_identifier:
          The reference key associated with this item: Supplied Material Color
          Identifier in the BOM Header
        - bom_comment:
          The reference key associated with this item: No Definition Available
        - bom_line_item_identifier:
          The reference key associated with this item: BOM Line Item Identifier
          in the BOM Line Item Details
        - line_item_material:
          The reference key associated with this item: Material Identifier in
          the BOM Line Item Details
        - line_item_supplied_material:
          The reference key associated with this item: Supplied Material
          Identifier in the BOM Line Item Details
        - line_item_color:
          The reference key associated with this item: Color Identifier in the
          BOM Line Item Details
        - line_item_supplied_material_color:
          The reference key associated with this item: Supplied Material Color
          Identifier in the BOM Line Item Details
        - line_item_supplied_material_multi_color_code:
          The reference key associated with this item: Supplied Material Multi
          Color Name in the BOM Line Item Details
        - line_item_supplied_material_color_is_multiple_colors:
          The reference key associated with this item: Supplied Material Color
          Multi Color Indicator in the BOM Line Item Details
        - quantity_grams:
          The reference key associated with this item: Weight in Grams for the
          particular material in the BOM Line Item Details
        - color_position:
          The reference key associated with this item: No Definition Available
        - part_name:
          The reference key associated with this item: No Definition Available
        - feeder_left:
          The reference key associated with this item: No Definition Available
        - feeder_right:
          The reference key associated with this item: No Definition Available
        - bobbin_position_left:
          The reference key associated with this item: No Definition Available
        - bobbin_position_right:
          The reference key associated with this item: No Definition Available
        - placement:
          The reference key associated with this item: No Definition Available
        - bom_status_indicator:
          The reference key associated with this item: No Definition Available
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/search/suppliedMaterialColorBOMs",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "count": oapi.client.format_argument_value(
                    "count",
                    count,
                    style="form",
                    explode=False,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=False,
                ),
                "q": oapi.client.format_argument_value(
                    "q",
                    q,
                    style="form",
                    explode=False,
                ),
                "bomIdentifier": oapi.client.format_argument_value(
                    "bomIdentifier",
                    bom_identifier,
                    style="form",
                    explode=False,
                ),
                "bomName": oapi.client.format_argument_value(
                    "bomName",
                    bom_name,
                    style="form",
                    explode=False,
                ),
                "bomDescription": oapi.client.format_argument_value(
                    "bomDescription",
                    bom_description,
                    style="form",
                    explode=False,
                ),
                "material": oapi.client.format_argument_value(
                    "material",
                    material,
                    style="form",
                    explode=False,
                ),
                "suppliedMaterial": oapi.client.format_argument_value(
                    "suppliedMaterial",
                    supplied_material,
                    style="form",
                    explode=False,
                ),
                "color": oapi.client.format_argument_value(
                    "color",
                    color,
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorIdentifier": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorIdentifier",
                    supplied_material_color_identifier,
                    style="form",
                    explode=False,
                ),
                "bomComment": oapi.client.format_argument_value(
                    "bomComment",
                    bom_comment,
                    style="form",
                    explode=False,
                ),
                "bomLineItemIdentifier": oapi.client.format_argument_value(
                    "bomLineItemIdentifier",
                    bom_line_item_identifier,
                    style="form",
                    explode=False,
                ),
                "lineItemMaterial": oapi.client.format_argument_value(
                    "lineItemMaterial",
                    line_item_material,
                    style="form",
                    explode=False,
                ),
                "lineItemSuppliedMaterial": oapi.client.format_argument_value(
                    "lineItemSuppliedMaterial",
                    line_item_supplied_material,
                    style="form",
                    explode=False,
                ),
                "lineItemColor": oapi.client.format_argument_value(
                    "lineItemColor",
                    line_item_color,
                    style="form",
                    explode=False,
                ),
                "lineItemSuppliedMaterialColor": oapi.client.format_argument_value(  # noqa
                    "lineItemSuppliedMaterialColor",
                    line_item_supplied_material_color,
                    style="form",
                    explode=False,
                ),
                "lineItemSuppliedMaterialMultiColorCode": oapi.client.format_argument_value(  # noqa
                    "lineItemSuppliedMaterialMultiColorCode",
                    line_item_supplied_material_multi_color_code,
                    style="form",
                    explode=False,
                ),
                "lineItemSuppliedMaterialColorIsMultipleColors": oapi.client.format_argument_value(  # noqa
                    "lineItemSuppliedMaterialColorIsMultipleColors",
                    line_item_supplied_material_color_is_multiple_colors,
                    style="form",
                    explode=False,
                ),
                "quantityGrams": oapi.client.format_argument_value(
                    "quantityGrams",
                    quantity_grams,
                    style="form",
                    explode=False,
                ),
                "colorPosition": oapi.client.format_argument_value(
                    "colorPosition",
                    color_position,
                    style="form",
                    explode=False,
                ),
                "partName": oapi.client.format_argument_value(
                    "partName",
                    part_name,
                    style="form",
                    explode=False,
                ),
                "feederLeft": oapi.client.format_argument_value(
                    "feederLeft",
                    feeder_left,
                    style="form",
                    explode=False,
                ),
                "feederRight": oapi.client.format_argument_value(
                    "feederRight",
                    feeder_right,
                    style="form",
                    explode=False,
                ),
                "bobbinPositionLeft": oapi.client.format_argument_value(
                    "bobbinPositionLeft",
                    bobbin_position_left,
                    style="form",
                    explode=False,
                ),
                "bobbinPositionRight": oapi.client.format_argument_value(
                    "bobbinPositionRight",
                    bobbin_position_right,
                    style="form",
                    explode=False,
                ),
                "placement": oapi.client.format_argument_value(
                    "placement",
                    placement,
                    style="form",
                    explode=False,
                ),
                "bomStatusIndicator": oapi.client.format_argument_value(
                    "bomStatusIndicator",
                    bom_status_indicator,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SearchResponse,
            )
        )

    def get_material_management_data_artwork_graphics_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.MaterialManagementDataArtworkGraphicsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ArtworkGraphicResponse:
        """
        How you get a single Artwork Graphic which indicates what artwork or
        graphic is printed on a given material

        Parameters:

        - object_id:
          A single Id of the object (in this case Artwork Graphic ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/artworkGraphics/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.ArtworkGraphicResponse,
            )
        )

    def get_material_management_data_artwork_graphics(
        self,
        object_id: model.MaterialManagementDataArtworkGraphicsGetObjectId,
        *,
        dataunits: typing.Optional[
            model.MaterialManagementDataArtworkGraphicsGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ArtworkGraphicBulkResponse:
        """
        How you get Artwork Graphic which indicates what artwork or graphic is
        printed on a given material in a Bulk fashion

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Arwork
          Graphic Ids)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/artworkGraphics",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "objectId": oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                ),
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.ArtworkGraphicBulkResponse,
            )
        )

    def get_material_management_data_material_families_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.MaterialFamilyResponse:
        """
        How you get a single Material Family resource

        Parameters:

        - object_id:
          A single Id of the object (in this case Material Family ID)
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialFamilies/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.MaterialFamilyResponse,
            )
        )

    def get_material_management_data_material_families(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.MaterialFamilyBulkResponse:
        """
        How you get all the Material Family data

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialFamilies",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.MaterialFamilyBulkResponse,
            )
        )

    def get_material_procurement_data_pricing_effectivities_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.MaterialProcurementDataPricingEffectivitiesObjectIdGetDataunits  # noqa
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.PricingEffectivityResponse:
        """
        How you get a single Pricing Effectivity (Effectivity Context) which
        indicates the time range a price is effecitve

        Parameters:

        - object_id:
          A single Id of the object (in this case Effectivity Context ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/pricingEffectivities/{objectId}".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.PricingEffectivityResponse,
            )
        )

    def get_material_procurement_data_pricing_effectivities(
        self,
        object_id: model.MaterialProcurementDataPricingEffectivitiesGetObjectId,  # noqa
        *,
        dataunits: typing.Optional[
            model.MaterialProcurementDataPricingEffectivitiesGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.PricingEffectivityBulkResponse:
        """
        Getting the Pricing Effectivity (Effectivity Context) data which
        indicates the time range a price is effecitve, in Bulk

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Supplied
          Materials)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/pricingEffectivities",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "objectId": oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                ),
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.PricingEffectivityBulkResponse,
            )
        )

    def get_material_management_data_products_information_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.MaterialManagementDataProductsInformationObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ProductInformationResponse:
        """
        How you get a single product information data.

        Parameters:

        - object_id:
          A single Id of the object (in this case Product Information
          Identifier - PCX Material or Supplied Material Number)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/productsInformation/{objectId}".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.ProductInformationResponse,
            )
        )

    def get_material_management_search_products_information(
        self,
        *,
        count: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
        q: typing.Optional[
            str
        ] = "",
        primary_product_information_identifier: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetPrimaryProductInformationIdentifier  # noqa
        ] = None,
        supplier_location: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetSupplierLocation  # noqa
        ] = None,
        parent_product_information_identifier: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetParentProductInformationIdentifier  # noqa
        ] = None,
        product_information_type: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetProductInformationType  # noqa
        ] = None,
        product_information_name: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetProductInformationName  # noqa
        ] = None,
        product_information_description: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetProductInformationDescription  # noqa
        ] = None,
        supplemental_product_information_name: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetSupplementalProductInformationName  # noqa
        ] = None,
        pdm_material_number: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetPdmMaterialNumber  # noqa
        ] = None,
        pps_item_number: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetPpsItemNumber
        ] = None,
        division: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetDivision
        ] = None,
        material_development_team: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetMaterialDevelopmentTeam  # noqa
        ] = None,
        target_style: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetTargetStyle
        ] = None,
        material_family: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetMaterialFamily
        ] = None,
        target_season_cycle_year: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetTargetSeasonCycleYear  # noqa
        ] = None,
        development_reason: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetDevelopmentReason  # noqa
        ] = None,
        end_use: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetEndUse
        ] = None,
        material_benefits: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetMaterialBenefits  # noqa
        ] = None,
        nav_indicator: typing.Optional[
            bool
        ] = None,
        corporate_designation_indicator: typing.Optional[
            bool
        ] = None,
        primary_supplier_indicator: typing.Optional[
            bool
        ] = None,
        vendor_special_care_instructions: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetVendorSpecialCareInstructions  # noqa
        ] = None,
        consideration_and_risks: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetConsiderationAndRisks  # noqa
        ] = None,
        product_information_owner: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetProductInformationOwner  # noqa
        ] = None,
        approved_vendor_article_number: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetApprovedVendorArticleNumber  # noqa
        ] = None,
        product_information_state: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetProductInformationState  # noqa
        ] = None,
        product_information_status_indicator: typing.Optional[
            bool
        ] = None,
        wash_instructions: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetWashInstructions  # noqa
        ] = None,
        wash_additional_instructions: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetWashAdditionalInstructions  # noqa
        ] = None,
        bleach_instructions: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetBleachInstructions  # noqa
        ] = None,
        bleach_additional_instructions: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetBleachAdditionalInstructions  # noqa
        ] = None,
        drying_instructions: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetDryingInstructions  # noqa
        ] = None,
        drying_additional_instructions: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetDryingAdditionalInstructions  # noqa
        ] = None,
        ironing_instructions: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetIroningInstructions  # noqa
        ] = None,
        ironing_additional_instructions: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetIroningAdditionalInstructions  # noqa
        ] = None,
        dry_clean_instructions: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetDryCleanInstructions  # noqa
        ] = None,
        dry_clean_additional_instructions: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetDryCleanAdditionalInstructions  # noqa
        ] = None,
        special_care_instructions: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetSpecialCareInstructions  # noqa
        ] = None,
        special_care_additional_instructions: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetSpecialCareAdditionalInstructions  # noqa
        ] = None,
        required_phrases: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetRequiredPhrases
        ] = None,
        statement_content: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetStatementContent  # noqa
        ] = None,
        product_part: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetProductPart
        ] = None,
        alternate_product_part_content_statement: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetAlternateProductPartContentStatement  # noqa
        ] = None,
        product_part_content_percentage: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetProductPartContentPercentage  # noqa
        ] = None,
        product_part_content: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetProductPartContent  # noqa
        ] = None,
        process_type: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetProcessType
        ] = None,
        statement_used_on: typing.Optional[
            model.MaterialManagementSearchProductsInformationGetStatementUsedOn
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the Product
        Information entity

        Parameters:

        - count:
          Number of entries the API should attempt to fetch, default is 10
        - offset:
          Offset of the entries the API should attempt to fetch, default is 0
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        - q:
          This parameter is how you pass free text search, if any string is
          passed here it will be searched as free text
        - primary_product_information_identifier:
          The reference key associated with this item: Primary Product
          Information ID
        - supplier_location:
          The reference key associated with this item: Supplier Location ID
        - parent_product_information_identifier:
          The reference key associated with this item: Parent Product
          Information ID
        - product_information_type:
          The reference key associated with this item: Product Information Type
        - product_information_name:
          The value associated with this item: Product Information Name
        - product_information_description:
          The value associated with this item: Product Information Description
        - supplemental_product_information_name:
          The value associated with this item: Supplemental Product Information
          Name
        - pdm_material_number:
          The value associated with this item: PDM Material Number
        - pps_item_number:
          The value associated with this item: PPS Item Number
        - division:
          The reference key associated with this item: Division Code
        - material_development_team:
          The reference key associated with this item: Material Development
          Team
        - target_style:
          The value associated with this item: targetStyle
        - material_family:
          The reference key associated with this item: Material Family
        - target_season_cycle_year:
          The reference key associated with this item: Target Season Cycle Year
        - development_reason:
          The reference key associated with this item: Development Reason
        - end_use:
          The reference key associated with this item: End Use
        - material_benefits:
          The reference key associated with this item: Material Benefits
        - nav_indicator:
          The true or false flag associated with this item: NAV Indicator
        - corporate_designation_indicator:
          The true or false flag associated with this item: Corporate
          Designtation Indicator
        - primary_supplier_indicator:
          The true or false flag associated with this item: Primary Supplier
          Indicator
        - vendor_special_care_instructions:
          The reference key associate with this item: Vendor Special Care
          Indicator
        - consideration_and_risks:
          The reference key associated with this item: Consideration And Risk
        - product_information_owner:
          The value associated with this item: Product Information Owner
        - approved_vendor_article_number:
          The value associated with this item: Approved Vendor Article Number
        - product_information_state:
          The reference key associated with this item: Product Information
          State
        - product_information_status_indicator:
          The true or false flag associated with this item: Product Information
          Status Indicator
        - wash_instructions:
          The reference key associated with this item: Wash Instructions
        - wash_additional_instructions:
          The reference key associated with this item: Wash Additional
          Instructions
        - bleach_instructions:
          The reference key associated with this item: Bleach Instructions
        - bleach_additional_instructions:
          The reference key associated with this item: Bleach Additional
          Instructions
        - drying_instructions:
          The reference key associated with this item: Drying Instructions
        - drying_additional_instructions:
          The reference key associated with this item: Drying Additional
          Instructions
        - ironing_instructions:
          The reference key associated with this item: Ironing Instructions
        - ironing_additional_instructions:
          The reference key associated with this item: Ironing Additional
          Instructions
        - dry_clean_instructions:
          The reference key associated with this item: Dry Clean Instructions
        - dry_clean_additional_instructions:
          The reference key associated with this item: Dry Clean Additional
          Instructions
        - special_care_instructions:
          The reference key associated with this item: Special Care
          Instructions
        - special_care_additional_instructions:
          The reference key associated with this item: Special Care Additional
          Instructions
        - required_phrases:
          The reference key associated with this item: Required Phrases
        - statement_content:
          The reference key associated with this item: Statement Content
        - product_part:
          The reference key associated with this item: Product Part
        - alternate_product_part_content_statement:
          The reference key associated with this item: Alternate Product Part
          Statement
        - product_part_content_percentage:
          The number (float) for Product Part Content Percentage
        - product_part_content:
          The reference key associated with this item: Product Part Content
        - process_type:
          The reference key associated with this item: Process Type
        - statement_used_on:
          The reference key associated with this item: Statement Used On
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/search/productsInformation",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "count": oapi.client.format_argument_value(
                    "count",
                    count,
                    style="form",
                    explode=False,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=False,
                ),
                "q": oapi.client.format_argument_value(
                    "q",
                    q,
                    style="form",
                    explode=False,
                ),
                "primaryProductInformationIdentifier": oapi.client.format_argument_value(  # noqa
                    "primaryProductInformationIdentifier",
                    primary_product_information_identifier,
                    style="form",
                    explode=False,
                ),
                "supplierLocation": oapi.client.format_argument_value(
                    "supplierLocation",
                    supplier_location,
                    style="form",
                    explode=False,
                ),
                "parentProductInformationIdentifier": oapi.client.format_argument_value(  # noqa
                    "parentProductInformationIdentifier",
                    parent_product_information_identifier,
                    style="form",
                    explode=False,
                ),
                "productInformationType": oapi.client.format_argument_value(
                    "productInformationType",
                    product_information_type,
                    style="form",
                    explode=False,
                ),
                "productInformationName": oapi.client.format_argument_value(
                    "productInformationName",
                    product_information_name,
                    style="form",
                    explode=False,
                ),
                "productInformationDescription": oapi.client.format_argument_value(  # noqa
                    "productInformationDescription",
                    product_information_description,
                    style="form",
                    explode=False,
                ),
                "supplementalProductInformationName": oapi.client.format_argument_value(  # noqa
                    "supplementalProductInformationName",
                    supplemental_product_information_name,
                    style="form",
                    explode=False,
                ),
                "pdmMaterialNumber": oapi.client.format_argument_value(
                    "pdmMaterialNumber",
                    pdm_material_number,
                    style="form",
                    explode=False,
                ),
                "ppsItemNumber": oapi.client.format_argument_value(
                    "ppsItemNumber",
                    pps_item_number,
                    style="form",
                    explode=False,
                ),
                "division": oapi.client.format_argument_value(
                    "division",
                    division,
                    style="form",
                    explode=False,
                ),
                "materialDevelopmentTeam": oapi.client.format_argument_value(
                    "materialDevelopmentTeam",
                    material_development_team,
                    style="form",
                    explode=False,
                ),
                "targetStyle": oapi.client.format_argument_value(
                    "targetStyle",
                    target_style,
                    style="form",
                    explode=False,
                ),
                "materialFamily": oapi.client.format_argument_value(
                    "materialFamily",
                    material_family,
                    style="form",
                    explode=False,
                ),
                "targetSeasonCycleYear": oapi.client.format_argument_value(
                    "targetSeasonCycleYear",
                    target_season_cycle_year,
                    style="form",
                    explode=False,
                ),
                "developmentReason": oapi.client.format_argument_value(
                    "developmentReason",
                    development_reason,
                    style="form",
                    explode=False,
                ),
                "endUse": oapi.client.format_argument_value(
                    "endUse",
                    end_use,
                    style="form",
                    explode=False,
                ),
                "materialBenefits": oapi.client.format_argument_value(
                    "materialBenefits",
                    material_benefits,
                    style="form",
                    explode=False,
                ),
                "navIndicator": oapi.client.format_argument_value(
                    "navIndicator",
                    nav_indicator,
                    style="form",
                    explode=False,
                ),
                "corporateDesignationIndicator": oapi.client.format_argument_value(  # noqa
                    "corporateDesignationIndicator",
                    corporate_designation_indicator,
                    style="form",
                    explode=False,
                ),
                "primarySupplierIndicator": oapi.client.format_argument_value(
                    "primarySupplierIndicator",
                    primary_supplier_indicator,
                    style="form",
                    explode=False,
                ),
                "vendorSpecialCareInstructions": oapi.client.format_argument_value(  # noqa
                    "vendorSpecialCareInstructions",
                    vendor_special_care_instructions,
                    style="form",
                    explode=False,
                ),
                "considerationAndRisks": oapi.client.format_argument_value(
                    "considerationAndRisks",
                    consideration_and_risks,
                    style="form",
                    explode=False,
                ),
                "productInformationOwner": oapi.client.format_argument_value(
                    "productInformationOwner",
                    product_information_owner,
                    style="form",
                    explode=False,
                ),
                "approvedVendorArticleNumber": oapi.client.format_argument_value(  # noqa
                    "approvedVendorArticleNumber",
                    approved_vendor_article_number,
                    style="form",
                    explode=False,
                ),
                "productInformationState": oapi.client.format_argument_value(
                    "productInformationState",
                    product_information_state,
                    style="form",
                    explode=False,
                ),
                "productInformationStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "productInformationStatusIndicator",
                    product_information_status_indicator,
                    style="form",
                    explode=False,
                ),
                "washInstructions": oapi.client.format_argument_value(
                    "washInstructions",
                    wash_instructions,
                    style="form",
                    explode=False,
                ),
                "washAdditionalInstructions": oapi.client.format_argument_value(  # noqa
                    "washAdditionalInstructions",
                    wash_additional_instructions,
                    style="form",
                    explode=False,
                ),
                "bleachInstructions": oapi.client.format_argument_value(
                    "bleachInstructions",
                    bleach_instructions,
                    style="form",
                    explode=False,
                ),
                "bleachAdditionalInstructions": oapi.client.format_argument_value(  # noqa
                    "bleachAdditionalInstructions",
                    bleach_additional_instructions,
                    style="form",
                    explode=False,
                ),
                "dryingInstructions": oapi.client.format_argument_value(
                    "dryingInstructions",
                    drying_instructions,
                    style="form",
                    explode=False,
                ),
                "dryingAdditionalInstructions": oapi.client.format_argument_value(  # noqa
                    "dryingAdditionalInstructions",
                    drying_additional_instructions,
                    style="form",
                    explode=False,
                ),
                "ironingInstructions": oapi.client.format_argument_value(
                    "ironingInstructions",
                    ironing_instructions,
                    style="form",
                    explode=False,
                ),
                "ironingAdditionalInstructions": oapi.client.format_argument_value(  # noqa
                    "ironingAdditionalInstructions",
                    ironing_additional_instructions,
                    style="form",
                    explode=False,
                ),
                "dryCleanInstructions": oapi.client.format_argument_value(
                    "dryCleanInstructions",
                    dry_clean_instructions,
                    style="form",
                    explode=False,
                ),
                "dryCleanAdditionalInstructions": oapi.client.format_argument_value(  # noqa
                    "dryCleanAdditionalInstructions",
                    dry_clean_additional_instructions,
                    style="form",
                    explode=False,
                ),
                "specialCareInstructions": oapi.client.format_argument_value(
                    "specialCareInstructions",
                    special_care_instructions,
                    style="form",
                    explode=False,
                ),
                "specialCareAdditionalInstructions": oapi.client.format_argument_value(  # noqa
                    "specialCareAdditionalInstructions",
                    special_care_additional_instructions,
                    style="form",
                    explode=False,
                ),
                "requiredPhrases": oapi.client.format_argument_value(
                    "requiredPhrases",
                    required_phrases,
                    style="form",
                    explode=False,
                ),
                "statementContent": oapi.client.format_argument_value(
                    "statementContent",
                    statement_content,
                    style="form",
                    explode=False,
                ),
                "productPart": oapi.client.format_argument_value(
                    "productPart",
                    product_part,
                    style="form",
                    explode=False,
                ),
                "alternateProductPartContentStatement": oapi.client.format_argument_value(  # noqa
                    "alternateProductPartContentStatement",
                    alternate_product_part_content_statement,
                    style="form",
                    explode=False,
                ),
                "productPartContentPercentage": oapi.client.format_argument_value(  # noqa
                    "productPartContentPercentage",
                    product_part_content_percentage,
                    style="form",
                    explode=False,
                ),
                "productPartContent": oapi.client.format_argument_value(
                    "productPartContent",
                    product_part_content,
                    style="form",
                    explode=False,
                ),
                "processType": oapi.client.format_argument_value(
                    "processType",
                    process_type,
                    style="form",
                    explode=False,
                ),
                "statementUsedOn": oapi.client.format_argument_value(
                    "statementUsedOn",
                    statement_used_on,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SearchResponse,
            )
        )
