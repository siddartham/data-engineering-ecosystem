from typing import Dict

CERBERUS_URL: str = "https://prod.cerberus.companycloud.com"
BMX_USER: str = "a.BMX.teamName"
BMX_CERBERUS_PATH: str = "app/teamName/bmx"
REGIONS_BIN_BUCKET_NAMES: Dict[str, str] = {
    "us-west-2": "company-emr-bin-west",
    "us-east-1": "company-emr-bin",
}
teamName_ENGINEERING_ARN: str = (
    "arn:aws:iam::456234896345:role/teamNameEngineering"
)
teamName_ENGINEERING_NON_PROD_ARN: str = (
    "arn:aws:iam::456234896345:role/teamNameEngineeringNonProd"
)
BMX_teamName_ENGINEERING_ARN: str = (
    "arn:aws:iam::456234896345:role/BMX-teamNameEngineering"
)
BMX_teamName_ENGINEERING_NON_PROD_ARN: str = (
    "arn:aws:iam::456234896345:role/BMX-teamNameEngineeringNonProd"
)
