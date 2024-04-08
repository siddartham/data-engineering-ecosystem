import warnings

from sqlalchemy.exc import SAWarning  # type: ignore

OKTA_URL: str = "https://org.okta.com"
LDAP_HOST: str = "ldap://ad.org.com"

# Turn off warnings for table arguments with unknown dialect prefixes
warnings.filterwarnings(
    "ignore",
    message=(
        r"^Can't validate argument .* "
        r"can't locate any SQLAlchemy dialect named .*"
    ),
    category=SAWarning,
)
