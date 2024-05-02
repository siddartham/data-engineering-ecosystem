#!/usr/bin/env python3
"""
This script creates and/or updates the data model for
material-management-client.

*Please note that any class names which are altered manually in the generated
model will be retained when this script is run subsequently, so long as the
JSON pointer in the OpenAPI document has remained the same*
"""
import json
import os
import re
from collections import deque
from copy import copy
from typing import IO, TYPE_CHECKING, Callable, Dict, List, Tuple, Union

import oapi  # type: ignore
import yaml
from daves_dev_tools.clean import delete_empty_directories
from daves_dev_tools.git.download import download
from cerberus_assistant.get import get_secret
from sob.abc import JSONTypes
from sob.model import serialize

from product_data_hub_client.abc.client import Client

GITHUB_USER: str = "a-bmx-sustainability_nike"
GITHUB_PASSWORD_CERBERUS_PATH: str = f"app/sustainability/github/{GITHUB_USER}"
PROJECT_PATH: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OPENAPI_SOURCE_DIRECTORY: str = os.path.join(PROJECT_PATH, "openapi", "source")
OPENAPI_FIXED_DIRECTORY: str = os.path.join(PROJECT_PATH, "openapi", "fixed")
ROOT_PACKAGE_PATH: str = f"{PROJECT_PATH}/nike/product_data_hub_client/"
_INTEGER_SCHEMA: oapi.oas.model.Schema = oapi.oas.model.Schema(
    type_="integer",
)
_FLOAT_SCHEMA: oapi.oas.model.Schema = oapi.oas.model.Schema(
    type_="number",
    format_="float",
)
_BOOLEAN_SCHEMA: oapi.oas.model.Schema = oapi.oas.model.Schema(
    type_="boolean",
)
_STRING_SCHEMA: oapi.oas.model.Schema = oapi.oas.model.Schema(
    type_="string",
)
_DATETIME_SCHEMA: oapi.oas.model.Schema = oapi.oas.model.Schema(
    type_="string",
    format_="date-time",
)
_LINK_SCHEMA: oapi.oas.model.Schema = oapi.oas.model.Schema(
    type_="object",
    properties=oapi.oas.model.Properties(
        {
            "rel": _STRING_SCHEMA,
            "href": _STRING_SCHEMA,
        }
    ),
)
_LINK_SCHEMA_REFERENCE: oapi.oas.model.Reference = oapi.oas.model.Reference(
    ref="#/definitions/_links"
)
_REFERENCE_SCHEMA: oapi.oas.model.Schema = oapi.oas.model.Schema(
    type_="object",
    properties=oapi.oas.model.Properties(
        {
            "link": _LINK_SCHEMA,
            "referenceKey": _STRING_SCHEMA,
        }
    ),
)

_ARRAY_REFERENCE_SCHEMA: oapi.oas.model.Schema = oapi.oas.model.Schema(
    type_="array", items=_REFERENCE_SCHEMA
)

_REFERENCE_SCHEMA_REFERENCE: oapi.oas.model.Reference = (
    oapi.oas.model.Reference(ref="#/definitions/_reference")
)
_OBJECT_SCHEMA: oapi.oas.model.Schema = oapi.oas.model.Schema(
    type_="object",
)


def get_open_api(schema_path: str) -> oapi.oas.model.OpenAPI:
    """
    This function parses the OpenAPI doc
    """
    schema_io: IO[str]
    schema: Dict[str, JSONTypes]
    with open(schema_path, "r") as schema_io:
        if schema_path.endswith(".yaml") or schema_path.endswith(".yml"):
            schema = yaml.safe_load(
                re.sub(
                    (
                        r"\n[ ][ ][ ][ ]"
                        r"/materialManagement/data/forBallTypeAndSizes\:"
                    ),
                    "\n  /materialManagement/data/forBallTypeAndSizes:",
                    re.sub(
                        r"\btype\:\s*float\b", "type: number", schema_io.read()
                    ),
                )
                .replace(
                    "$ref: '#/definitions/forBallTypeAndSizeResponse'",
                    "type: object",
                )
                .replace(
                    "$ref: '#/definitions/forBallTypeAndSizeBulkResponse'",
                    "type: object",
                )
            )
        else:
            schema = json.load(schema_io)
    return oapi.oas.model.OpenAPI(schema)


def fix_sustainability_schema(
    open_api: oapi.oas.model.OpenAPI,
) -> None:
    assert open_api.definitions
    open_api.definitions["suppliedMaterialIndexResponse"].properties[
        "objectId"
    ] = _STRING_SCHEMA
    open_api.definitions["suppliedMaterialIndexResponse"].properties[
        "objectType"
    ] = _STRING_SCHEMA
    open_api.definitions["sustnbltySuppliedMaterialScoreCore"].properties[
        "nikeSustainabilityRankingDescription"
    ] = _STRING_SCHEMA
    open_api.definitions["sustnbltySuppliedMaterialScoreCore"].properties[
        "nikeSustainabilityRanking"
    ] = _STRING_SCHEMA
    open_api.definitions["sustnbltySuppliedMaterialScoreCore"].properties[
        "carbonFootprintKgCO2ePerKg"
    ] = _FLOAT_SCHEMA
    open_api.definitions["PDHStreamAdaptorItems"] = oapi.oas.model.Schema(
        properties=oapi.oas.model.Properties(
            [
                (
                    "domain",
                    oapi.oas.model.Schema(
                        description="Specifies the domain related to the data",
                        type_="string",
                    ),
                ),
                (
                    "eventType",
                    oapi.oas.model.Schema(
                        description=(
                            "Type of events responsible for the"
                            " message e.g. CREATE, UPDATE"
                        ),
                        type_="string",
                    ),
                ),
                (
                    "sourceSystem",
                    oapi.oas.model.Schema(
                        description=(
                            "Specifies the system from there the"
                            " data is sourced from"
                        ),
                        type_="string",
                    ),
                ),
                (
                    "objectId",
                    oapi.oas.model.Schema(
                        description="Unique identifier for the data",
                        type_="string",
                    ),
                ),
                (
                    "objectType",
                    oapi.oas.model.Schema(
                        description="Type of the data", type_="string"
                    ),
                ),
                (
                    "objectVersion",
                    oapi.oas.model.Schema(
                        description=(
                            "Version of object data resultant to change. This"
                            " information will be used to expose the latest "
                            "data to a consumer. The older versions will be "
                            "saved in the cold and warm storage areas."
                        ),
                        type_="integer",
                    ),
                ),
                (
                    "apiVersion",
                    oapi.oas.model.Schema(
                        description=(
                            "Version of the splitting required for aligning "
                            "to the exposed canonical form of data. the "
                            "expectation if this will help us to version "
                            "changes to data as defined by the source system"
                            " / integration services"
                        ),
                        type_="integer",
                    ),
                ),
                (
                    "correlationId",
                    oapi.oas.model.Schema(
                        description=(
                            "id for tracking the data produced by source "
                            "system, logging, monitoring and alerts"
                            " - UUID is recommended for this field"
                        ),
                        type_="string",
                    ),
                ),
                (
                    "entitlements",
                    oapi.oas.model.Schema(
                        description=(
                            "Who can see this data or confidential"
                            " group information"
                        ),
                        items=oapi.oas.model.Schema(type_="string"),
                        type_="array",
                        default=(),
                    ),
                ),
                (
                    "changes",
                    oapi.oas.model.Schema(
                        description=(
                            "What are the changes to data in case there is a "
                            "field level event is required, but encrypted"
                            " using AES 256"
                        ),
                        items=oapi.oas.model.Schema(
                            properties=oapi.oas.model.Properties(
                                [
                                    (
                                        "fieldName",
                                        oapi.oas.model.Schema(
                                            type_="string",
                                        ),
                                    ),
                                    (
                                        "fromValue",
                                        oapi.oas.model.Schema(
                                            type_="string",
                                        ),
                                    ),
                                    (
                                        "toValue",
                                        oapi.oas.model.Schema(
                                            type_="string",
                                        ),
                                    ),
                                ]
                            ),
                            type_="object",
                        ),
                        type_="array",
                        default=(),
                    ),
                ),
                (
                    "fullObject",
                    oapi.oas.model.Schema(
                        description="The data itself in JSON format encrypted",
                        type_="string",
                    ),
                ),
            ]
        ),
        type_="object",
        required=[
            "eventType",
            "sourceSystem",
            "objectId",
            "objectType",
            "objectVersion",
            "fullObject",
            "correlationId",
            "domain",
            "apiVersion",
        ],
    )

    # Define the PUT endpoint operation
    operation = oapi.oas.model.Operation(
        description="Update a pdhStreamAdaptor resource by objectId",
        parameters=[
            oapi.oas.model.Parameter(
                name="Events",
                in_="body",
                description="The request body",
                required=True,
                schema=oapi.oas.model.Schema(
                    items=oapi.oas.model.Reference(
                        ref="#/definitions/PDHStreamAdaptorItems"
                    ),
                    type_="array",
                ),
            )
        ],
        responses=None,
        tags=["PDHStreamAdaptor"],
    )
    assert open_api.paths
    open_api.paths["/pdhStreamsAdaptor/data"] = oapi.oas.model.PathItem(
        put=operation
    )


def fix_material_management_schema(open_api: oapi.oas.model.OpenAPI) -> None:
    """
    This function fixes errors in the OpenAPI doc
    """
    assert open_api.definitions
    open_api.definitions["materialTypeBulkResponse"].properties[
        "totalCount"
    ] = _INTEGER_SCHEMA
    # Add self, count, objectId, and objectType properties to all (non-bulk)
    # response schemas
    deque(
        map(
            _definition_item_schema_add_count_property,
            map(
                _definition_item_schema_add_object_type_property,
                map(
                    _definition_item_schema_add_object_id_property,
                    filter(
                        _definition_item_is_non_bulk_response,
                        open_api.definitions.items(),
                    ),
                ),
            ),
        ),
        maxlen=0,
    )
    # Add unprocessedObjects property to all bulk response schemas
    deque(
        map(
            _definition_item_schema_add_unprocessed_objects_property,
            filter(
                _definition_item_is_bulk_response, open_api.definitions.items()
            ),
        ),
        maxlen=0,
    )
    # The relationship response items *are* references, they aren't
    # objects with a `relationships` property containing the reference
    relationship_response: oapi.oas.model.Schema = open_api.definitions[
        "relationshipResponse"
    ]
    assert relationship_response.properties
    relationship_response.properties[
        "content"
    ].items = relationship_response.properties["content"].items.properties[
        "relationships"
    ]
    # Missing properties
    open_api.definitions["Dimension"].properties[
        "weightGramsPerPiece"
    ] = _INTEGER_SCHEMA
    open_api.definitions["Cushioning"].properties[
        "initialPressure"
    ] = _INTEGER_SCHEMA
    # remove supmatCore from the list of required fields
    open_api.definitions["suppliedMaterialPrice_dataunits"].required.remove(
        "supmatCore"
    )
    # The retirement reason code is a reference object, not an integer
    open_api.definitions["supmatCore"].properties[
        "retirementReasonCode"
    ] = _REFERENCE_SCHEMA_REFERENCE
    # Capitalization typo:
    # "availableforUseIndicator" -> "availableForUseIndicator"
    material_type_properties: oapi.oas.model.Properties = open_api.definitions[
        "materialType"
    ].properties
    material_type_properties[
        "availableForUseIndicator"
    ] = material_type_properties.pop("availableforUseIndicator")
    # The division property should be a reference, not an array of
    # references
    open_api.definitions["pricingEffectivityClassification"].properties[
        "division"
    ] = _REFERENCE_SCHEMA_REFERENCE
    # The material core development team attribute is a reference, not an int
    open_api.definitions["matCore"].properties[
        "developmentTeam"
    ] = _REFERENCE_SCHEMA_REFERENCE
    # The supmatcore development team attribute is a reference, not an int
    open_api.definitions["supmatCore"].properties[
        "developmentTeam"
    ] = _REFERENCE_SCHEMA_REFERENCE
    open_api.definitions["ComponentZipper"].properties[
        "sliderSize"
    ] = _REFERENCE_SCHEMA
    open_api.definitions["ComponentZipper"].properties[
        "sliderType"
    ] = _REFERENCE_SCHEMA
    open_api.definitions["ComponentZipper"].properties[
        "zipperPartType"
    ] = _REFERENCE_SCHEMA
    open_api.definitions["ComponentZipper"].properties[
        "teethSizeWidth"
    ] = _INTEGER_SCHEMA
    open_api.definitions["suppliedMaterial_dataunits"].properties[
        "matComponentBladder"
    ] = _OBJECT_SCHEMA
    open_api.definitions["suppliedMaterial_dataunits"].properties[
        "matComponentSpecialty"
    ] = open_api.definitions["suppliedMaterial_dataunits"].properties.get(
        "matComponentSpecialty", _OBJECT_SCHEMA
    )
    open_api.definitions["material_dataunits"].properties[
        "matComponentSpecialty"
    ] = open_api.definitions["material_dataunits"].properties.get(
        "matComponentSpecialty",
        open_api.definitions["suppliedMaterial_dataunits"].properties[
            "matComponentSpecialty"
        ],
    )
    open_api.definitions["supmatCore"].properties[
        "suppliedMaterialUUID"
    ] = _STRING_SCHEMA
    open_api.definitions["matCore"].properties["materialUUID"] = _STRING_SCHEMA
    component_zipper: oapi.oas.model.Schema = open_api.definitions[
        "ComponentZipper"
    ]
    assert component_zipper.properties
    component_zipper.properties["intendedUseOn"] = _ARRAY_REFERENCE_SCHEMA


def _definition_item_is_response(
    item: Tuple[str, oapi.oas.model.Schema]
) -> bool:
    return item[0].endswith("Response")


def _definition_item_is_non_bulk_response(
    item: Tuple[str, oapi.oas.model.Schema]
) -> bool:
    return _definition_item_is_response(
        item
    ) and not _definition_item_is_bulk_response(item)


def _definition_item_is_bulk_response(
    item: Tuple[str, oapi.oas.model.Schema]
) -> bool:
    return item[0].endswith("BulkResponse")


def _definition_item_schema_add_self_property(
    item: Tuple[str, oapi.oas.model.Schema]
) -> Tuple[str, oapi.oas.model.Schema]:
    schema: oapi.oas.model.Schema = item[1]
    assert schema.properties
    if "self" not in schema.properties:
        print(
            'Adding a "self" property to the schema definition for '
            f'"{item[0]}"'
        )
        schema.properties["self"] = _LINK_SCHEMA_REFERENCE
    return item


def _definition_item_schema_add_object_id_property(
    item: Tuple[str, oapi.oas.model.Schema]
) -> Tuple[str, oapi.oas.model.Schema]:
    schema: oapi.oas.model.Schema = item[1]
    assert schema.properties
    if (
        ("content" in schema.properties)
        and ("objectId" not in schema.properties)
        and ("objectId" in (schema.properties["content"].properties or ()))
    ):
        print(
            'Adding an "objectId" property to the schema definition for '
            f'"{item[0]}"'
        )
        schema.properties["objectId"] = schema.properties[
            "content"
        ].properties["objectId"]
    return item


def _definition_item_schema_add_count_property(
    item: Tuple[str, oapi.oas.model.Schema]
) -> Tuple[str, oapi.oas.model.Schema]:
    schema: oapi.oas.model.Schema = item[1]
    assert schema.properties
    if "count" not in schema.properties:
        print(
            'Adding a "count" property to the schema definition for '
            f'"{item[0]}"'
        )
        schema.properties["count"] = _INTEGER_SCHEMA
    return item


def _definition_item_schema_add_unprocessed_objects_property(
    item: Tuple[str, oapi.oas.model.Schema]
) -> Tuple[str, oapi.oas.model.Schema]:
    schema: oapi.oas.model.Schema = item[1]
    assert schema.properties
    if "unprocessedObjects" not in schema.properties:
        print(
            'Adding an "unprocessedObjects" property to the schema '
            f'definition for "{item[0]}"'
        )
        schema.properties["unprocessedObjects"] = _STRING_SCHEMA
    return item


def _definition_item_schema_add_object_type_property(
    item: Tuple[str, oapi.oas.model.Schema]
) -> Tuple[str, oapi.oas.model.Schema]:
    schema: oapi.oas.model.Schema = item[1]
    assert schema.properties
    if (
        ("content" in schema.properties)
        and ("objectType" not in schema.properties)
        and ("objectType" in (schema.properties["content"].properties or ()))
    ):
        print(
            'Adding an "objectType" property to the schema definition for '
            f'"{item[0]}"'
        )
        schema.properties["objectType"] = schema.properties[
            "content"
        ].properties["objectType"]
    return item


def _accommodate_available_for_use_indicator_typo(
    schema: oapi.oas.model.Schema,
) -> None:
    assert schema.properties
    schema.properties["availableforUseIndicator"] = schema.properties[
        "availableForUseIndicator"
    ]


def fix_material_management_reference_schema(
    open_api: oapi.oas.model.OpenAPI,
) -> None:
    assert open_api.definitions
    open_api.definitions["_links"] = _LINK_SCHEMA
    open_api.definitions["_reference"] = _REFERENCE_SCHEMA
    # Add missing attributes
    open_api.definitions["materialTechnology"].properties[
        "materialTechnologiesIdentifier"
    ] = _INTEGER_SCHEMA
    open_api.definitions["materialTechnology"].properties[
        "materialTechnologiesName"
    ] = _STRING_SCHEMA
    open_api.definitions["referencePriceUnitOfMeasurement"].properties[
        "referencePriceUnitOfMeasurementCode"
    ].any_of = [_INTEGER_SCHEMA, _STRING_SCHEMA]
    open_api.definitions["referencePriceUnitOfMeasurement"].properties[
        "referencePriceUnitOfMeasurementCode"
    ].type_ = None
    # add a "self" link-property to all bulk response objects
    deque(
        map(
            _definition_item_schema_add_self_property,
            filter(_definition_item_is_response, open_api.definitions.items()),
        ),
        maxlen=0,
    )
    # Apply typo...
    deque(
        map(
            _accommodate_available_for_use_indicator_typo,
            (
                open_api.definitions["dyeMethod"],
                open_api.definitions["dyeType"],
                open_api.definitions["methodOfMake"],
                open_api.definitions["nonWovenWebBondingMethod"],
                open_api.definitions["scrim"],
                open_api.definitions["substrateConstruction"],
                open_api.definitions["textileConstructionType"],
                open_api.definitions["webFormation"],
                open_api.definitions["yarnPlyTexture"],
                open_api.definitions["yarnPlyType"],
            ),
        ),
        maxlen=0,
    )
    assert open_api.paths
    parameter: oapi.oas.model.Parameter
    for parameter in open_api.paths[
        "/materialManagement/data/weightMaterialNameVariations/{objectId}"
    ].get.parameters:
        if isinstance(parameter, oapi.oas.model.Parameter):
            if parameter.name == "objectId":
                parameter.type_ = "integer"
    open_api.paths[
        "/materialManagement/data/cushioningTypes"
    ] = open_api.paths.pop("/materialManagement/data/cushioningType")
    open_api.paths[
        "/materialManagement/data/cushioningTypes/{objectId}"
    ].get.responses["200"].schema.ref = "#/definitions/cushioningTypeResponse"


def fix_line_management_reference_schema(
    open_api: oapi.oas.model.OpenAPI,
) -> None:
    # Fix data types
    assert open_api.definitions
    open_api.definitions["currency"].properties[
        "precisionIndicator"
    ].type_ = "integer"
    cycle_year_properties: oapi.oas.model.Properties = open_api.definitions[
        "cycleYear"
    ].properties
    cycle_year_properties["yearLongDescription"].type_ = "integer"
    cycle_year_properties["byDivision"].items.properties[
        "SAPSeasonCode"
    ].any_of = [_INTEGER_SCHEMA, _STRING_SCHEMA]
    iso_measurement: oapi.oas.model.Schema = open_api.definitions[
        "ISOMeasurement"
    ]
    assert iso_measurement.properties
    iso_measurement.properties[
        "measurementConversionFactorNumber"
    ].type_ = "number"
    legacy_unit_of_measure_code: oapi.oas.model.Schema = (
        iso_measurement.properties["byDivision"].items.properties[
            "legacyUnitOfMeasureCode"
        ]
    )
    legacy_unit_of_measure_code.any_of = [
        oapi.oas.model.Schema(type_=legacy_unit_of_measure_code.type_),
        oapi.oas.model.Schema(type_="integer"),
    ]
    legacy_unit_of_measure_code.type_ = None
    assert iso_measurement.properties
    legacy_special_feature_code: oapi.oas.model.Schema = (
        iso_measurement.properties["byDivision"].items.properties[
            "legacySpecialFeatureCode"
        ]
    )
    legacy_special_feature_code.any_of = [
        oapi.oas.model.Schema(type_=legacy_special_feature_code.type_),
        oapi.oas.model.Schema(type_="integer"),
    ]
    legacy_special_feature_code.type_ = None


def fix_product_development_reference_schema(
    open_api: oapi.oas.model.OpenAPI,
) -> None:
    if TYPE_CHECKING:
        assert open_api.paths and open_api.definitions
    # Replace an invalid JSON pointer
    schema: Union[oapi.oas.model.Schema, oapi.oas.model.Reference] = (
        open_api.paths["/developmentSampleEvaluationStates/{objectId}"]
        .get.responses["200"]
        .schema
    )
    if isinstance(schema, oapi.oas.model.Reference) and schema.ref == (
        "#/definitions/developmentSampleEvaluationStateReasonResponse"
    ):
        schema.ref = "#/definitions/developmentSampleEvaluationStateResponse"
    # Correct the data type for the development team group's status indicator
    open_api.definitions["developmentTeamGroup"].properties[
        "statusIndicator"
    ].type_ = "boolean"
    open_api.definitions["billOfMaterialsSectionResponse"].properties[
        "self"
    ] = oapi.oas.model.Reference(ref="#/definitions/_links")
    open_api.definitions["billOfMaterialsSectionBulkResponse"].properties[
        "self"
    ] = oapi.oas.model.Reference(ref="#/definitions/_links")
    open_api.definitions["billOfMaterialsSection"].properties[
        "availableforUseIndicator"
    ] = _BOOLEAN_SCHEMA
    open_api.definitions[
        "billOfMaterialsUnitOfMeasurementResponse"
    ].properties["self"] = oapi.oas.model.Reference(ref="#/definitions/_links")
    open_api.definitions["billOfMaterialsUnitOfMeasurement"].properties[
        "bomUnitOfMeasurementIdentifier"
    ].type_ = "string"
    open_api.definitions["partNameResponse"].properties[
        "self"
    ] = oapi.oas.model.Reference(ref="#/definitions/_links")
    open_api.definitions["partName"].properties["division"] = _STRING_SCHEMA


def fix_product_development_schema(
    open_api: oapi.oas.model.OpenAPI,
) -> None:
    if TYPE_CHECKING:
        assert open_api.definitions
        assert open_api.paths
    open_api.definitions["billOfMaterialsResponse"].properties[
        "objectId"
    ] = _STRING_SCHEMA
    open_api.definitions["billOfMaterialsResponse"].properties[
        "objectType"
    ] = _STRING_SCHEMA
    open_api.definitions["billOfMaterialsSourceResponse"].properties[
        "objectId"
    ] = _STRING_SCHEMA
    open_api.definitions["billOfMaterialsSource_dataunits"].properties[
        "bomSeason"
    ] = open_api.definitions["billOfMaterialsSource_dataunits"].properties.pop(
        "bomSeason:"
    )
    open_api.definitions["billOfMaterialsSourceResponse"].properties[
        "objectType"
    ] = _STRING_SCHEMA
    open_api.definitions["bomCore"].properties["bomConverted"] = _STRING_SCHEMA
    open_api.definitions["bomSourcingConfiguration"].properties[
        "sourcingConfigurationIdentifier"
    ] = oapi.oas.model.Schema(type_="array", items=_INTEGER_SCHEMA)
    open_api.definitions["bomLineItemDetailSource"].items.properties[
        "lineItemQuantity"
    ].type_ = "number"
    open_api.definitions["bomLineItemDetailSource"].items.properties[
        "bomLineItemGUID"
    ] = _STRING_SCHEMA
    open_api.definitions["bomCore"].properties["bomGUID"] = _STRING_SCHEMA
    open_api.definitions["bomLineItemDetailSource"].items.properties[
        "partPattern"
    ] = _REFERENCE_SCHEMA_REFERENCE
    open_api.definitions["bomLineItemDetailSource"].items.properties[
        "partPrefix"
    ] = _REFERENCE_SCHEMA_REFERENCE
    open_api.definitions["bomLineItemDetail"].items.properties[
        "partPattern"
    ] = _REFERENCE_SCHEMA_REFERENCE
    open_api.definitions["bomLineItemDetail"].items.properties[
        "partPrefix"
    ] = _REFERENCE_SCHEMA_REFERENCE
    open_api.definitions["bomLineItemDetail"].items.properties[
        "bomLineItemGUID"
    ] = _STRING_SCHEMA
    # Allow searching by BOM UUID
    bom_guid_parameter: oapi.oas.model.Parameter = oapi.oas.model.Parameter(
        name="bomGUID",
        in_="query",
        required=False,
        type_="array",
        items=oapi.oas.model.Items(type_="string"),
        collection_format="csv",
        description="The Bill of Material's Universally Unique Identifier",
    )
    open_api.paths["/search/billOfMaterials"].get.parameters.append(
        bom_guid_parameter
    )
    open_api.paths["/search/billOfMaterials/sources"].get.parameters.append(
        copy(bom_guid_parameter)
    )


def fix_line_management_schema(open_api: oapi.oas.model.OpenAPI) -> None:
    assert open_api.definitions
    open_api.definitions["globalOfferingResponse"].properties[
        "objectId"
    ] = _STRING_SCHEMA
    open_api.definitions["sCore"].properties[
        "baseStyleNumber"
    ] = _STRING_SCHEMA
    open_api.definitions["globalOfferingResponse"].properties[
        "objectType"
    ] = _STRING_SCHEMA


def fix_material_vendor_management_schema(
    open_api: oapi.oas.model.OpenAPI,
) -> None:
    # Add objectId and objectType properties to all (non-bulk)
    # response schemas
    assert open_api.definitions
    deque(
        map(
            _definition_item_schema_add_object_type_property,
            map(
                _definition_item_schema_add_object_id_property,
                filter(
                    _definition_item_is_non_bulk_response,
                    open_api.definitions.items(),
                ),
            ),
        ),
        maxlen=0,
    )
    # Fix data types
    open_api.definitions["suplocCore"].properties[
        "supplierLocationIdentifier"
    ].type_ = "integer"
    sup_core: oapi.oas.model.Schema = open_api.definitions["supCore"]
    assert sup_core.properties
    supplier_identifier: oapi.oas.model.Schema = sup_core.properties[
        "supplierIdentifier"
    ]
    supplier_identifier.any_of = [
        oapi.oas.model.Schema(type_=supplier_identifier.type_),
        oapi.oas.model.Schema(type_="integer"),
    ]
    supplier_identifier.type_ = None
    # Add missing properties
    open_api.definitions["suplocGeneral"].properties[
        "confidentialityAgreementIndicator"
    ] = _BOOLEAN_SCHEMA


def fix_material_vendor_management_reference_schema(
    open_api: oapi.oas.model.OpenAPI,
) -> None:
    pass


SCHEMA_URL_MODEL_PATHS_FIXES: Tuple[
    Tuple[
        str, str, str, str, Callable[[oapi.oas.model.OpenAPI], None], str, str
    ],
    ...,
] = (
    (
        "https://github.com/nike-pdh/sc-material-management.git",
        "material-management/Sustainability/sustainability-swagger.yaml",
        "material_sustainability/model.py",
        "material_sustainability/client.py",
        fix_sustainability_schema,
        "https://materialmanagement.api-product.pes-prod.my.com/v1",
        "https://materialmanagement.api-product.pes-prod.my.com/v1",
        "Client",
    ),
    (
        "https://github.com/nike-pdh/sc-material-management.git",
        "material-management/materialManagement-V3-swagger.yaml",
        "material_management/model.py",
        "material_management/client.py",
        fix_material_management_schema,
        "https://materialmanagement.api-product.pes-prod.my.com/v3",
        "https://materialmanagement.api-product.pes-prod.my.com/v3",
        "Client",
    ),
    (
        "https://github.com/nike-pdh/sc-material-management.git",
        "material-management/reference-MM-V3-swagger.yaml",
        "material_management/reference_model.py",
        "material_management/reference_client.py",
        fix_material_management_reference_schema,
        "https://materialmanagement.api-product.pes-prod.my.com/v3",
        "https://materialmanagement.api-product.pes-prod.my.com/v3",
        "ReferenceClient",
    ),
    (
        "https://github.com/nike-pdh/sc-line-management.git",
        "line-management/globalOffering-swagger.yaml",
        "line_management/model.py",
        "line_management/client.py",
        fix_line_management_schema,
        "https://linemanagement.api-product.pes-prod.my.com/v1",
        "https://linemanagement.api-product.pes-prod.my.com/v1",
        "Client",
    ),
    (
        "https://github.com/nike-pdh/sc-line-management.git",
        "line-management/reference-linemgmt-swagger.yaml",
        "line_management/reference_model.py",
        "line_management/reference_client.py",
        fix_line_management_reference_schema,
        "https://linemanagement.api-product.pes-prod.my.com/v1",
        "https://linemanagement.api-product.pes-prod.my.com/v1",
        "ReferenceClient",
    ),
    (
        "https://github.com/nike-pdh/sc-product-development.git",
        "product-development/productDevelopment-swagger.yaml",
        "product_development/model.py",
        "product_development/client.py",
        fix_product_development_schema,
        (
            "https://productdevelopment.api-product.pes-prod.my.com"
            "https://productdevelopment.api-product.pes-prod.my.com"
            "/v1/productDevelopment"
        ),
        "Client",
    ),
    (
        "https://github.com/nike-pdh/sc-product-development.git",
        "product-development/reference-PD-swagger.yaml",
        "product_development/reference_model.py",
        "product_development/reference_client.py",
        fix_product_development_reference_schema,
        (
            "https://productdevelopment.api-product.pes-prod.my.com"
            "https://productdevelopment.api-product.pes-prod.my.com"
            "/v1/productDevelopment/data"
        ),
        "ReferenceClient",
    ),
    (
        "https://github.com/nike-pdh/sc-vendor-management.git",
        "supplier-swagger.yaml",
        "material_vendor_management/model.py",
        "material_vendor_management/client.py",
        fix_material_vendor_management_schema,
        (
            "https://vendormanagement.api-product.pes-prod.my.com/v1/"
            "https://vendormanagement.api-product.pes-prod.my.com/v1/"
            "materialVendorManagement"
        ),
        "Client",
    ),
    (
        "https://github.com/nike-pdh/sc-vendor-management.git",
        "reference-mvm-swagger.yaml",
        "material_vendor_management/reference_model.py",
        "material_vendor_management/reference_client.py",
        fix_material_vendor_management_reference_schema,
        (
            "https://vendormanagement.api-product.pes-prod.my.com/v1/"
            "https://vendormanagement.api-product.pes-prod.my.com/v1/"
            "materialVendorManagement"
        ),
        "ReferenceClient",
    ),
)


def main() -> None:
    """
    This function constructs or updates our data model from the OpenAPI schemas
    """
    os.makedirs(OPENAPI_SOURCE_DIRECTORY, exist_ok=True)
    os.makedirs(OPENAPI_FIXED_DIRECTORY, exist_ok=True)
    open_api: oapi.oas.model.OpenAPI
    url: str
    model_path: str
    client_path: str
    schema_path: str
    api_url: str
    fix_open_api: Callable[[oapi.oas.model.OpenAPI], None]
    for (
        url,
        schema_path,
        model_path,
        client_path,
        fix_open_api,
        api_url,
        class_name,
    ) in SCHEMA_URL_MODEL_PATHS_FIXES:
        files: List[str] = download(
            url,
            files=(schema_path,),
            directory=OPENAPI_SOURCE_DIRECTORY,
            user=GITHUB_USER,
            password=get_secret(GITHUB_PASSWORD_CERBERUS_PATH),
        )
        assert files, f'Could not download "{schema_path}" from {url}'
        if "/" in schema_path:
            schema_path = os.path.join(
                OPENAPI_SOURCE_DIRECTORY, os.path.basename(schema_path)
            )
            os.rename(files[0], schema_path)
        else:
            schema_path = os.path.join(OPENAPI_SOURCE_DIRECTORY, schema_path)
            assert os.path.isfile(schema_path)
        deque(map(print, files), maxlen=0)
        open_api = get_open_api(schema_path)
        fix_open_api(open_api)
        fixed_io: IO[str]
        with open(
            os.path.join(
                OPENAPI_FIXED_DIRECTORY,
                os.path.basename(schema_path).replace(".yaml", ".json"),
            ),
            "w",
        ) as fixed_io:
            fixed_io.write(serialize(open_api, indent=4))
        model_module: oapi.model.Module = oapi.model.Module(open_api)
        model_path = os.path.join(ROOT_PACKAGE_PATH, model_path)
        model_module.save(model_path)
        if client_path:
            client_path = os.path.join(ROOT_PACKAGE_PATH, client_path)
            client_module: oapi.client.Module = oapi.client.Module(
                open_api,
                class_name=class_name,
                base_class=Client,
                model_path=model_path,
                imports=(
                    (
                        "from nike.cerberus_assistant.decorate "
                        "import apply_cerberus_path_arguments"
                    ),
                    (
                        "from nike.cerberus_assistant.config "
                        "import CERBERUS_URL"
                    ),
                    ("from ..config import TOKEN_URL_PROD"),
                ),
                init_decorator=(
                    "@apply_cerberus_path_arguments(\n"
                    '    api_key="api_key_cerberus_path",\n'
                    '    cerberus_url_parameter_name="cerberus_url",\n'
                    "    oauth2_client_id="
                    '"oauth2_client_id_cerberus_path",\n'
                    "    oauth2_client_secret="
                    '"oauth2_client_secret_cerberus_path",\n'
                    ")"
                ),
                include_init_parameters=(
                    "url",
                    "api_key",
                    "api_key_name",
                    "oauth2_client_id",
                    "oauth2_client_secret",
                    "oauth2_token_url",
                    "timeout",
                    "retry_number_of_attempts",
                    "retry_for_errors",
                    "retry_hook",
                    "logger",
                    "echo",
                ),
                add_init_parameters=(
                    "cerberus_url: str = CERBERUS_URL",
                    'api_key_cerberus_path: str = ""',
                    'oauth2_client_id_cerberus_path: str = ""',
                    'oauth2_client_secret_cerberus_path: str = ""',
                ),
                add_init_parameter_docs=(
                    (
                        "cerberus_url (str): The root URL for the Cerberus "
                        "API where\nyour secrets are stored."
                    ),
                    (
                        'api_key_cerberus_path (str) = "": '
                        "A Cerberus secure data path (including /key) wherein "
                        "an API key with which to authenticate can be found."
                    ),
                    (
                        'oauth2_client_id_cerberus_path (str) = "": '
                        "A Cerberus secure data path (including /key) wherein "
                        "an OAuth2 client ID with which to authenticate "
                        "can be found."
                    ),
                    (
                        'oauth2_client_secret_cerberus_path (str) = "": '
                        "A Cerberus secure data path (including /key) wherein "
                        "an OAuth2 client secret with which to authenticate "
                        "can be found."
                    ),
                ),
                init_parameter_defaults={
                    "url": api_url,
                    "retry_number_of_attempts": 3,
                },
                init_parameter_defaults_source={
                    "oauth2_token_url": "TOKEN_URL_PROD",
                },
            )
            # We can't' just do `client_module.save(client_path)` here
            # because we have to set the default value for `q`
            # parameters to an empty string instead of `None`,
            # since PDH searches don't work without `q=` in the query string
            with open(client_path, "w") as client_io:
                client_io.write(
                    re.sub(
                        r'(\n\s*?kwargs.get\("q",\s*)None(\s*\)\s*,)',
                        r'\1""\2',
                        re.sub(
                            (
                                r"(\n\s*q: typing.Optional\[(?:\n|.)*?\]"
                                r"(?:\n|\s)*?=\s*)(?:\n|.)*?,"
                            ),
                            r'\1"",',
                            client_module.get_source(path=client_path),
                        ),
                    )
                )

    delete_empty_directories(OPENAPI_SOURCE_DIRECTORY)


if __name__ == "__main__":
    main()
