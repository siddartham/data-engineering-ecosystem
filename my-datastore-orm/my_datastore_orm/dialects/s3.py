from typing import Dict

_ROOT_URL: str = (
    "s3://my-s3-bucket"
)
# Root S3 URLs for each environment
ENVIRONMENTS_URLS: Dict[str, str] = {
    "dev": f"{_ROOT_URL}dev/",
    "qa": f"{_ROOT_URL}qa/",
    "prod": f"{_ROOT_URL}prod/",
}
