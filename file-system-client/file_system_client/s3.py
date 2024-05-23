import copyreg
import json
import logging
import os
import re
from abc import ABC, ABCMeta, abstractmethod
from copy import copy
from datetime import datetime
from inspect import Parameter, signature
from itertools import chain
from typing import (
    IO,
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Tuple,
    Type,
    Union,
)
from urllib.parse import ParseResult, quote_plus, urlparse

import boto3  # type: ignore
import boto3.session  # type: ignore
import botocore  # type: ignore
import botocore.client  # type: ignore
import botocore.config  # type: ignore
import botocore.exceptions  # type: ignore
from boto3.resources.base import ResourceMeta, ServiceResource  # type: ignore
from boto3.resources.collection import (  # type: ignore
    CollectionManager,
    ResourceCollection,
)
from boto3.s3.transfer import TransferConfig  # type: ignore
from botocore.credentials import ReadOnlyCredentials  # type: ignore
from botocore.exceptions import ClientError  # type: ignore
from botocore.response import StreamingBody  # type: ignore

from ._utilities import FileBytesIO
from .base import FileSystem
from .errors import append_exception_text, get_exception_text
from .utilities import (
    SUCCESS_FILE_NAME,
    FileSortKey,
    camel,
    get_qualified_name,
    lru_cache,
    url_is_local,
)

if TYPE_CHECKING:
    IO.register(StreamingBody)

log: logging.Logger = logging.getLogger(__name__)
DEFAULT_CONFIG: botocore.config.Config = botocore.config.Config(
    retries={"total_max_attempts": 4, "mode": "adaptive"}
)
DEFAULT_LOCAL_CONFIG: botocore.config.Config = botocore.config.Config(
    retries={"total_max_attempts": 1}
)


class Object(ABC):
    """
    This class is an abstract base class for the the dynamically created
    `s3.Object` class which can be used to test whether an object
    is an instance of the dynamically created `s3.Object` class.
    """

    __metaclass__ = ABCMeta
    Acl: Callable[[], Any]
    Bucket: Callable[[], "Bucket"]
    MultipartUpload: Callable[[], Any]
    Version: Callable[[str], Any]
    bucket_name: str
    key: str
    accept_ranges: str
    archive_status: str
    bucket_key_enabled: str
    cache_control: str
    content_disposition: str
    content_encoding: str
    content_language: str
    content_length: int
    content_type: str
    delete_marker: bool
    e_tag: str
    expiration: str
    expires: datetime
    last_modified: datetime
    metadata: Dict[str, str]
    missing_meta: int
    object_lock_legal_hold_status: str
    object_lock_mode: str
    object_lock_retain_until_date: datetime
    parts_count: int
    replication_status: str
    request_charged: str
    restore: str
    server_side_encryption: str
    sse_customer_algorithm: str
    sse_customer_key_md5: str
    ssekms_key_id: str
    storage_class: str
    version_id: str
    website_redirect_location: str

    @classmethod
    def __subclasshook__(cls, sub_class: type) -> bool:
        if (
            issubclass(sub_class, ServiceResource)
            and sub_class.__name__ == "s3.Object"
        ):
            return True
        else:
            return False

    @abstractmethod
    def copy(
        self,
        CopySource: Dict[str, str],
        ExtraArgs: Optional[Dict[str, str]] = None,
        Callback: Optional[Callable[[bytes], None]] = None,
        SourceClient: Optional[botocore.client.BaseClient] = None,
        Config: Optional[botocore.config.Config] = None,
    ) -> None:
        pass

    @abstractmethod
    def copy_from(
        self,
        ACL: Optional[str] = None,
        CacheControl: Optional[str] = None,
        ContentDisposition: Optional[str] = None,
        ContentEncoding: Optional[str] = None,
        ContentLanguage: Optional[str] = None,
        ContentType: Optional[str] = None,
        CopySource: Union[str, Dict[str, str], None] = None,
        CopySourceIfMatch: Optional[str] = None,
        CopySourceIfModifiedSince: Optional[datetime] = None,
        CopySourceIfNoneMatch: Optional[str] = None,
        CopySourceIfUnmodifiedSince: Optional[datetime] = None,
        Expires: Optional[datetime] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
        Metadata: Optional[Dict[str, str]] = None,
        MetadataDirective: Optional[str] = None,
        TaggingDirective: Optional[str] = None,
        ServerSideEncryption: Optional[str] = None,
        StorageClass: Optional[str] = None,
        WebsiteRedirectLocation: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        SSEKMSKeyId: Optional[str] = None,
        SSEKMSEncryptionContext: Optional[str] = None,
        BucketKeyEnabled: Optional[bool] = None,
        CopySourceSSECustomerAlgorithm: Optional[str] = None,
        CopySourceSSECustomerKey: Optional[str] = None,
        CopySourceSSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        Tagging: Optional[str] = None,
        ObjectLockMode: Optional[str] = None,
        ObjectLockRetainUntilDate: Optional[datetime] = None,
        ObjectLockLegalHoldStatus: Optional[str] = None,
        ExpectedBucketOwner: Optional[str] = None,
        ExpectedSourceBucketOwner: Optional[str] = None,
    ) -> None:
        pass

    @abstractmethod
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def download_file(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def download_fileobj(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def get(
        self,
        IfMatch: Optional[str] = None,
        IfModifiedSince: Optional[datetime] = None,
        IfNoneMatch: Optional[str] = None,
        IfUnmodifiedSince: Optional[datetime] = None,
        Range: Optional[str] = None,
        ResponseCacheControl: Optional[str] = None,
        ResponseContentDisposition: Optional[str] = None,
        ResponseContentEncoding: Optional[str] = None,
        ResponseContentLanguage: Optional[str] = None,
        ResponseContentType: Optional[str] = None,
        ResponseExpires: Optional[datetime] = None,
        VersionId: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        PartNumber: Optional[int] = None,
        ExpectedBucketOwner: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        https://bit.ly/3qYtSkw
        """
        pass

    @abstractmethod
    def get_available_subresources(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def initiate_multipart_upload(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def put(
        self,
        ACL: Optional[str] = None,
        Body: Union[bytes, IO[bytes], None] = None,
        CacheControl: Optional[str] = None,
        ContentDisposition: Optional[str] = None,
        ContentEncoding: Optional[str] = None,
        ContentLanguage: Optional[str] = None,
        ContentLength: Optional[int] = None,
        ContentMD5: Optional[str] = None,
        ContentType: Optional[str] = None,
        Expires: Optional[datetime] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
        Metadata: Optional[Dict[str, Any]] = None,
        ServerSideEncryption: Optional[str] = None,
        StorageClass: Optional[str] = None,
        WebsiteRedirectLocation: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSEKMSKeyId: Optional[str] = None,
        SSEKMSEncryptionContext: Optional[str] = None,
        BucketKeyEnabled: Optional[bool] = None,
        RequestPayer: Optional[str] = None,
        Tagging: Optional[str] = None,
        ObjectLockMode: Optional[str] = None,
        ObjectLockRetainUntilDate: Optional[datetime] = None,
        ObjectLockLegalHoldStatus: Optional[str] = None,
        ExpectedBucketOwner: Optional[str] = None,
    ) -> None:
        """
        https://bit.ly/3r2uaa3
        """
        pass

    @abstractmethod
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def restore_object(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def upload_file(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def upload_fileobj(self, *args: Any, **kwargs: Any) -> None:
        pass


class Bucket(ABC):
    """
    This class is an abstract base class for the the dynamically created
    `s3.Bucket` class which can be used to test whether an object
    is an instance of the dynamically created `s3.Bucket` class.
    """

    __metaclass__ = ABCMeta
    name: str
    objects: CollectionManager
    creation_date: datetime
    meta: ResourceMeta
    Acl: Callable[[], Any]
    Cors: Callable[[], Any]
    Lifecycle: Callable[[], Any]
    LifecycleConfiguration: Callable[[], Any]
    Logging: Callable[[], Any]
    Notification: Callable[[], Any]
    Object: Callable[..., Object]
    Policy: Callable[[], Any]
    RequestPayment: Callable[[], Any]
    Tagging: Callable[[], Any]
    Versioning: Callable[[], Any]
    Website: Callable[[], Any]

    @classmethod
    def __subclasshook__(cls, sub_class: type) -> bool:
        if (
            issubclass(sub_class, ServiceResource)
            and sub_class.__name__ == "s3.Bucket"
        ):
            return True
        else:
            return False

    @abstractmethod
    def create(self) -> Any:
        pass

    @abstractmethod
    def delete_objects(self, **kwargs: Any) -> Dict[str, Any]:
        pass

    @abstractmethod
    def upload_fileobj(
        self, file_object: Union[str, IO[bytes]], path: str
    ) -> Dict[str, Any]:
        pass

    @abstractmethod
    def download_fileobj(
        self,
        Key: str,
        Fileobj: IO[bytes],
        *,
        ExtraArgs: Optional[Dict[str, Any]] = None,
        Callback: Optional[Callable[[bytes], None]] = None,
        Config: Optional[TransferConfig] = None,
    ) -> Dict[str, Any]:
        pass

    @abstractmethod
    def put_object(
        self,
        ACL: Optional[str] = None,
        Body: Union[bytes, IO[bytes], None] = None,
        CacheControl: Optional[str] = None,
        ContentDisposition: Optional[str] = None,
        ContentEncoding: Optional[str] = None,
        ContentLanguage: Optional[str] = None,
        ContentLength: Optional[int] = None,
        ContentMD5: Optional[str] = None,
        ContentType: Optional[str] = None,
        Expires: Optional[datetime] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
        Key: Optional[str] = None,
        Metadata: Optional[Dict[str, Any]] = None,
        ServerSideEncryption: Optional[str] = None,
        StorageClass: Optional[str] = None,
        WebsiteRedirectLocation: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSEKMSKeyId: Optional[str] = None,
        SSEKMSEncryptionContext: Optional[str] = None,
        BucketKeyEnabled: Optional[bool] = None,
        RequestPayer: Optional[str] = None,
        Tagging: Optional[str] = None,
        ObjectLockMode: Optional[str] = None,
        ObjectLockRetainUntilDate: Optional[datetime] = None,
        ObjectLockLegalHoldStatus: Optional[str] = None,
        ExpectedBucketOwner: Optional[str] = None,
    ) -> None:
        """
        https://bit.ly/30Te9Ig
        """
        pass


def _get_session_redux(
    self: boto3.session.Session,  # type: ignore
) -> Tuple[type, Tuple[None, None, None, Optional[str], None, Optional[str]]]:
    return (
        boto3.session.Session,
        (
            None,
            None,
            None,
            self._session.get_config_variable("region"),
            None,
            self._session.get_config_variable("profile"),
        ),
    )


# This makes `boto3.session.Session` instances pickle-able
copyreg.pickle(boto3.session.Session, _get_session_redux)  # type: ignore


def _get_s3_client_arguments(
    self: botocore.client.BaseClient,
) -> Tuple[
    str,
    str,
    Optional[str],
    bool,
    Union[str, bool, None],
    str,
    Optional[str],
    Optional[str],
    Optional[str],
    botocore.config.Config,
]:
    return (
        "s3",
        self.meta.region_name,
        self.meta.service_model.api_version,
        self.meta.endpoint_url.startswith("https://"),  # use_ssl
        self.meta.config.client_cert,  # verify
        self.meta.endpoint_url,
        None,
        None,
        None,
        self.meta.config,
    )


def _get_bucket(
    name: str,
    client_args: Tuple[
        str,
        str,
        Optional[str],
        bool,
        Union[str, bool, None],
        str,
        Optional[str],
        Optional[str],
        Optional[str],
        botocore.config.Config,
    ],
) -> Bucket:
    return boto3.resource(*client_args).Bucket(name)


def _get_bucket_redux(
    bucket: Bucket,
) -> Tuple[
    Callable,
    Tuple[
        str,
        Tuple[
            str,
            str,
            Optional[str],
            bool,
            Union[str, bool, None],
            str,
            Optional[str],
            Optional[str],
            Optional[str],
            botocore.config.Config,
        ],
    ],
]:
    return (
        _get_bucket,  # noqa
        (bucket.name, _get_s3_client_arguments(bucket.meta.client)),
    )


def _get_s3_resource_redux(
    resource: ServiceResource,
) -> Tuple[
    Callable,
    Tuple[
        str,
        str,
        Optional[str],
        bool,
        Union[str, bool, None],
        str,
        Optional[str],
        Optional[str],
        Optional[str],
        botocore.config.Config,
    ],
]:
    copyreg.pickle(
        type(resource.meta.client), _get_s3_client_redux  # type: ignore
    )
    return boto3.resource, _get_s3_client_arguments(resource.meta.client)


def _get_s3_client_redux(
    resource: ServiceResource,
) -> Tuple[
    Callable,
    Tuple[
        str,
        str,
        Optional[str],
        bool,
        Union[str, bool, None],
        str,
        Optional[str],
        Optional[str],
        Optional[str],
        botocore.config.Config,
    ],
]:
    return boto3.client, _get_s3_client_arguments(resource)


@lru_cache()
def _get_profile_arn(profile_name: str) -> str:
    try:
        return (
            boto3.session.Session(
                profile_name=profile_name or None,
            )
            .client("sts")
            .get_caller_identity()["Arn"]
        )
    except botocore.exceptions.NoCredentialsError:
        return ""


@lru_cache()
def _get_default_endpoint_url() -> str:
    return boto3.session.Session().client("s3").meta.endpoint_url


class ObjectSummary(ABC):
    """
    This class is an abstract base class for the the dynamically created
    `s3.ObjectSummary` class which can be used to test whether an object
    is an instance of the dynamically created `s3.ObjectSummary` class.
    """

    __metaclass__ = ABCMeta
    key: str
    last_modified: datetime
    bucket_name: str
    size: int
    storage_class: str
    e_tag: str

    @classmethod
    def __subclasshook__(cls, sub_class: type) -> bool:
        if (
            issubclass(sub_class, ServiceResource)
            and sub_class.__name__ == "s3.ObjectSummary"
        ):
            return True
        else:
            return False


def _get_path_sub_directories(directory: str, path: str) -> Iterable[str]:
    while (path != directory) and path.startswith(directory):
        path = "{}/".format("/".join(path.rstrip("/").split("/")[:-1]))
        if path != directory:
            yield path


def _cannot_list_objects_in_bucket_prefix(bucket: Bucket, prefix: str) -> str:
    try:
        next(iter(bucket.objects.filter(Prefix=prefix)))
        return ""
    except StopIteration:
        return ""
    except Exception:
        return get_exception_text()


def _cannot_put_in_bucket_prefix(bucket: Bucket, prefix: str) -> str:
    timestamp: str = re.sub(
        r"[^\d\-]+", "-", datetime.now().isoformat(sep="-")
    ).strip("-")
    success_file_path: str = (
        f"{prefix}_bucket-put-test-{timestamp}/{SUCCESS_FILE_NAME}"
    )
    error_message: str = ""
    try:
        bucket.upload_fileobj(FileBytesIO(), success_file_path)
    except Exception:
        error_message = get_exception_text()
    finally:
        bucket.delete_objects(
            Delete=dict(Objects=[dict(Key=success_file_path)])
        )
    return error_message


def _case_insensitive_dictionary_update(
    dictionary: Dict[str, Any], **kwargs: Any
) -> None:
    key: str
    value: Any
    lower_case_keys: Dict[str, str] = {
        key.lower(): key for key in dictionary.keys()
    }
    for key, value in kwargs.items():
        dictionary[lower_case_keys.get(key.lower(), key)] = value


def _get_function_metadata_kwargs(
    function: Callable[..., Any],
    metadata: Optional[Dict[str, Any]] = None,
    kwargs: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    if kwargs:
        kwargs = copy(kwargs)
    else:
        kwargs = {}
    if metadata:
        metadata = copy(metadata)
        parameters: Mapping[str, Parameter] = signature(function).parameters
        key: str
        parameter_name: str
        for key in tuple(metadata.keys()):
            if (key == "self") or (key in kwargs):
                continue
            parameter_name = camel(key, capitalize=True)
            if (parameter_name in parameters) and parameters[
                parameter_name
            ].kind in (
                Parameter.KEYWORD_ONLY,
                Parameter.POSITIONAL_OR_KEYWORD,
            ):
                kwargs[parameter_name] = metadata.pop(key)
        if metadata:
            kwargs["Metadata"] = metadata
    return kwargs


def _get_aws_role_arn() -> str:
    return os.environ.get("AWS_ROLE_ARN", "")


def _get_common_prefix(item: Dict[str, str]) -> str:
    prefix: str = item.get("Prefix", "")
    assert not prefix.endswith("//"), prefix
    return prefix


def get_assume_role_session_name() -> str:
    return os.environ.get(
        "AWS_ROLE_SESSION_NAME",
        (
            datetime.now()
            .replace(microsecond=0, tzinfo=None)
            .isoformat()
            .replace(":", "-")
            .replace(".", "-")
        ),
    )


def get_web_identity_token() -> str:
    web_identity_token: str = ""
    web_identity_token_file: str = os.environ.get(
        "AWS_WEB_IDENTITY_TOKEN_FILE", ""
    )
    if web_identity_token_file:
        with open(web_identity_token_file, "r") as web_identity_token_file_io:
            web_identity_token = web_identity_token_file_io.read().strip()
    return web_identity_token


class _GetBoto3SessionAndExpiration:
    def __init__(
        self, profile_name: str = "", arn: str = "", region_name: str = ""
    ) -> None:
        self.profile_name = profile_name
        self.arn = arn
        self.region_name = region_name
        self.session_name: str = get_assume_role_session_name()
        self.web_identity_token = get_web_identity_token()
        self.aws_role_arn = _get_aws_role_arn()
        self.credentials: Dict[str, Any] = {}
        self.session: boto3.session.Session = boto3.session.Session(
            profile_name=profile_name or None,
            region_name=region_name or None,
        )

    def set_credentials(self, credentials: Dict[str, Any]) -> None:
        self.session = boto3.session.Session(
            region_name=self.region_name or None,
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"],
        )
        self.credentials = credentials

    def web_identity_assume_role(self) -> bool:
        """
        Attempt to assume the role `self.arn`, and return `True` if
        successful
        """
        if self.web_identity_token:
            if self.arn:
                try:
                    self.set_credentials(
                        self.session.client(
                            "sts", region_name=self.region_name or None
                        ).assume_role_with_web_identity(
                            RoleArn=self.arn,
                            RoleSessionName=self.session_name,
                            WebIdentityToken=self.web_identity_token,
                        )[
                            "Credentials"
                        ]
                    )
                    return True
                except ClientError:
                    pass
            if self.aws_role_arn:
                try:
                    self.set_credentials(
                        self.session.client(
                            "sts", region_name=self.region_name or None
                        ).assume_role_with_web_identity(
                            RoleArn=self.aws_role_arn,
                            RoleSessionName=self.session_name,
                            WebIdentityToken=self.web_identity_token,
                        )[
                            "Credentials"
                        ]
                    )
                    if not self.arn:
                        # Only return `True` if no more needs done
                        return True
                except ClientError:
                    pass
        return False

    def assume_role(self) -> bool:
        """
        Try to assume the role `self.arn`, and return `True` if
        this was accomplished (if we don't need to do any more role
        chaining)
        """
        if self.arn:
            try:
                self.set_credentials(
                    self.session.client(
                        "sts", region_name=self.region_name or None
                    ).assume_role(
                        RoleArn=self.arn,
                        RoleSessionName=self.session_name,
                    )[
                        "Credentials"
                    ]
                )
                return True
            except ClientError:
                pass
        return False

    def assume_environment_role(self) -> bool:
        """
        Try to assume the environment-inferred role, `self.aws_role_arn`,
        and return `True` if there was an environment variable specifying a
        role, and we were able to assume that role
        """
        if self.aws_role_arn:
            try:
                self.set_credentials(
                    self.session.client(
                        "sts", region_name=self.region_name or None
                    ).assume_role(
                        RoleArn=self.aws_role_arn,
                        RoleSessionName=self.session_name,
                    )[
                        "Credentials"
                    ]
                )
                return True
            except ClientError:
                pass
        return False

    def __call__(self) -> Tuple[boto3.session.Session, Optional[datetime]]:
        if not self.web_identity_assume_role():
            if not self.assume_role():
                if self.assume_environment_role():
                    self.assume_role()
        return self.session, self.credentials.get("Expiration", None)


def get_boto3_session_and_expiration(
    profile_name: str = "", arn: str = "", region_name: str = ""
) -> Tuple[boto3.session.Session, Optional[datetime]]:
    return _GetBoto3SessionAndExpiration(
        profile_name=profile_name,
        arn=arn,
        region_name=region_name,
    )()


def get_boto3_session(
    profile_name: str = "", arn: str = "", region_name: str = ""
) -> boto3.session.Session:
    return get_boto3_session(
        profile_name=profile_name, arn=arn, region_name=region_name
    )


class SimpleStorageService(FileSystem):
    """
    This class provides an interface with an Amazon S3 bucket suitable for use
    in parallel-processing (pyspark, multiprocessing, etc.).

    Parameters/Properties:

    - bucket_name (str)
    - root (str): A root object prefix ("directory") to use in resolving
      relative paths
    - profile_name (str): This is the profile name to use in retrieving
      stored credentials. If not provided, the profile will be inferred
      to be the first one encountered which has access to the specified bucket.
    - arn (str): An ARN to assume
    - endpoint_url (str): The AWS endpoint URL to use
    - config (botocore.config.Config): An (optional) botocore
      [configuration object](https://bit.ly/3cUHEwy).
    """

    __slots__: Tuple[str, ...] = FileSystem.__slots__ + (
        "_endpoint_url",
        "_bucket",
        "assumed_role_arn",
        "_assumed_role_expires",
        "_profile_name",
        "bucket_name",
        "config",
        "region_name",
    )

    def __init__(
        self,
        bucket_name: str = "",
        root: str = "",
        profile_name: str = "",
        arn: str = "",
        endpoint_url: str = "",
        config: Optional[botocore.config.Config] = None,
        region_name: str = "",
    ) -> None:
        self._endpoint_url: str = endpoint_url
        self._bucket: Optional[Bucket] = None
        self.assumed_role_arn: str = arn
        self._assumed_role_expires: datetime = datetime.now()
        self._profile_name = profile_name
        self.bucket_name = bucket_name
        self.config = config
        self.region_name = region_name
        super().__init__(root=root)

    def __getstate__(self) -> Dict[str, Any]:
        """
        Get a dictionary of attributes for pickling
        """
        # Attempt to obtain and cache these properties, prior to
        # parallelization, so they only need to be created once, but
        # don't raise an error if we can't obtain them quite yet
        cached_properties: Tuple[str, ...] = (
            "endpoint_url",
            "profile_name",
        )
        property_name: str
        for property_name in cached_properties:
            try:
                getattr(self, property_name)
            except Exception:
                pass
        slot: str
        return dict(
            map(
                lambda slot: (slot, getattr(self, slot)),
                chain(
                    filter(
                        lambda slot: (
                            (slot in FileSystem.__slots__)
                            or (not slot.startswith("_"))
                        ),
                        self.__slots__,
                    ),
                    cached_properties,
                ),
            )
        )

    @property
    def endpoint_url(self) -> str:
        if not self._endpoint_url:
            self._endpoint_url = _get_default_endpoint_url()
        return self._endpoint_url

    @property
    def profile_name(self) -> str:
        assert isinstance(self.bucket, Bucket)
        assert isinstance(self._profile_name, str)
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name: str) -> None:
        assert isinstance(profile_name, str)
        if profile_name:
            os.environ["AWS_PROFILE"] = profile_name
        elif "AWS_PROFILE" in os.environ:
            del os.environ["AWS_PROFILE"]
        self._profile_name = profile_name

    def __copy__(self) -> "SimpleStorageService":
        cls: Type["SimpleStorageService"] = type(self)
        state: Dict[str, Any] = self.__getstate__()
        instance: SimpleStorageService = cls()
        instance.__setstate__(state)
        return instance

    def __deepcopy__(
        self, memo: Optional[dict] = None
    ) -> "SimpleStorageService":
        return copy(self)

    def _get_resource_bucket(self, resource: ServiceResource) -> Bucket:
        bucket: Bucket = resource.Bucket(self.bucket_name)  # type: ignore
        copyreg.pickle(type(bucket), _get_bucket_redux)  # type: ignore
        return bucket

    @property  # type: ignore
    @lru_cache()
    def _absolute_root(self) -> str:
        return f"{self.get_absolute_path(self.root)}"

    def _get_session(self) -> boto3.session.Session:
        return self._get_profile_session(self.profile_name)

    def _get_profile_session(
        self, profile_name: str = ""
    ) -> boto3.session.Session:
        assert (profile_name is None) or isinstance(profile_name, str)
        is_local: bool = url_is_local(self.endpoint_url)
        if is_local:
            return boto3.session.Session(
                profile_name=profile_name or None,
                aws_access_key_id="test",
                aws_secret_access_key="test",
                aws_session_token="test",
            )
        session: boto3.session.Session
        expiration: Optional[datetime]
        session, expiration = get_boto3_session_and_expiration(
            profile_name=profile_name or "",
            arn=self.assumed_role_arn,
            region_name=self.region_name,
        )
        if expiration:
            self._assumed_role_expires = expiration
        return session

    def _get_profile_bucket(self, profile_name: str) -> Bucket:
        """
        Retrieve the AWS S3 resource bucket
        """
        is_local: bool = url_is_local(self.endpoint_url)
        local_is_default: bool = (
            is_local and _get_default_endpoint_url() == self.endpoint_url
        )
        if is_local and not local_is_default:
            from localstack_client.patch import (  # type: ignore
                enable_local_endpoints,
            )

            enable_local_endpoints()
        try:
            session: boto3.session.Session = self._get_profile_session(
                profile_name
            )
            s3_resource: ServiceResource = session.resource(
                "s3",
                config=(
                    self.config
                    or (DEFAULT_LOCAL_CONFIG if is_local else DEFAULT_CONFIG)
                ),
                aws_access_key_id=("test" if is_local else None),
                aws_secret_access_key=("test" if is_local else None),
            )
            # Ensure this dynamically created type is pickleable
            copyreg.pickle(  # type: ignore
                type(s3_resource), _get_s3_resource_redux
            )
            bucket = self._get_resource_bucket(s3_resource)
            # Ensure this dynamically created type is pickleable
            copyreg.pickle(type(bucket), _get_bucket_redux)  # type: ignore
            if is_local:
                try:
                    creation_date: Optional[datetime]
                    try:
                        creation_date = bucket.creation_date
                    except Exception:
                        creation_date = None
                    # If using `localstack`, the bucket might have to be
                    # created
                    if not creation_date:
                        bucket.create()
                except botocore.exceptions.ClientError as client_error:
                    message: str = (
                        f"boto3.client.__module__ = "
                        f"{repr(boto3.client.__module__)}\n"
                        f"boto3.resource.__module__ = "
                        f"{repr(boto3.resource.__module__)}\n"
                        f"boto3.session.Session.__module__ = "
                        f"{repr(boto3.session.Session.__module__)}\n"
                        f"self = {repr(self)}\n"
                        f"self.credentials = {repr(self.credentials)}"
                    )
                    # Provide a little more debugging info in the error
                    append_exception_text(
                        client_error,
                        message,
                    )
                    raise client_error
        finally:
            if is_local and not local_is_default:
                from localstack_client.patch import (  # type: ignore
                    disable_local_endpoints,
                )

                disable_local_endpoints()
        return bucket

    def get_url(self, path: str = "", protocol: str = "s3") -> str:
        """
        Get an absolute URL from an object key (`prefix`)
        """
        assert protocol in ("s3", "s3a")
        absolute_path: str = quote_plus(
            self.get_absolute_path(path), safe="/="
        )
        separator: str = "" if absolute_path.startswith("/") else "/"
        return f"{protocol}://{self.bucket_name}{separator}{absolute_path}"

    def get_absolute_path(self, path: str) -> str:
        """
        Get an absolute object key (`prefix`) from a prefix or URL
        """
        parse_result: ParseResult = urlparse(path)
        if parse_result.scheme:
            # If this is a URL, make sure the file is from *this*
            # S3 bucket
            if parse_result.netloc != self.bucket_name:
                raise ValueError(
                    "You may only access objects from the "
                    f"`{self.bucket_name}` bucket, "
                    f"not from `{parse_result.netloc}`."
                )
            path = parse_result.path
        return super().get_absolute_path(path)

    def iter_object_summaries(
        self, directory: str = "", delimiter: str = ""
    ) -> ResourceCollection:
        kwargs: Dict[str, str] = {}
        if directory or self.root:
            kwargs.update(Prefix=self.get_absolute_path(directory))
        if delimiter:
            kwargs.update(Delimiter=delimiter)
        resource_collection: ResourceCollection
        if kwargs:
            return self.bucket.objects.filter(**kwargs)
        return self.bucket.objects.all()

    def iter_file_paths(
        self,
        directory: str = "",
        recursive: bool = True,
        sort_key: FileSortKey = FileSortKey.DEFAULT,
        sort_reverse: bool = False,
    ) -> Iterable[str]:
        """
        Parameters:

        - directory (str): For S3, this parameter actually indicates a
          *prefix* (to be appended to the client's `root` prefix), so keep in
          mind that this prefix can be arbitrary, it does not need to end
          with "/". If no value is provided, *all* objects are included.
        - recursive (bool): This is `True` by default. If `False`, the "/"
          character is treated as a directory indicator to determine nesting.
        - sort_key (..base.FileSortKey):
          This is an enumerated value which can indicate files should be sorted
          by the date on which they were last modified
          (`FileSortKey.MODIFIED`), their name (`FileSortKey.NAME`), or
          just in the default order in which the file system returns them
          (`FileSortKey.DEFAULT`).
        - sort_reverse (bool): This is `False` by default. If `True`,
          files are returned in reverse order.

        Returns: An iterable of all (relative) object paths starting with the
        `directory` prefix.
        """
        object_summaries: Iterable[ObjectSummary] = self.iter_object_summaries(
            directory, delimiter="" if recursive else "/"
        )
        if sort_key is FileSortKey.MODIFIED:

            def get_object_summary_sort_key(
                object_summary: ObjectSummary,
            ) -> datetime:
                return object_summary.last_modified

            object_summaries = sorted(
                object_summaries,
                key=get_object_summary_sort_key,
                reverse=sort_reverse,
            )

        def get_object_summary_key(object_summary: ObjectSummary) -> str:
            return object_summary.key

        object_keys: Iterable[str] = map(
            self.get_relative_path,
            map(get_object_summary_key, object_summaries),
        )
        if sort_key is FileSortKey.NAME:
            object_keys = sorted(object_keys, reverse=sort_reverse)
        elif sort_reverse and sort_key is FileSortKey.DEFAULT:
            object_keys = reversed(tuple(object_keys))
        yield from filter(
            lambda object_key: not object_key.endswith("/"), object_keys
        )

    # For compatibility
    get_file_paths = iter_file_paths

    def _list_objects_v2_prefixes(
        self, prefix: str, start_after: str = ""
    ) -> Iterable[str]:
        response: Dict[str, Any] = self.bucket.meta.client.list_objects_v2(
            Bucket=self.bucket.name,
            Prefix=prefix,
            Delimiter="/",
            **(dict(StartAfter=start_after) if start_after else {}),
        )
        yield from map(
            _get_common_prefix,
            response.get("CommonPrefixes", ()),
        )
        # Chain paginated responses if necessary
        if response.get("IsTruncated", False):
            yield from self._list_objects_v2_prefixes(
                prefix=prefix,
                start_after=response["CommonPrefixes"][-1]["Prefix"],
            )

    def iter_sub_directories(
        self, directory: str = "/", recursive: bool = False
    ) -> Iterable[str]:
        """
        Yield all sub-directories under a `directory` prefix.

        Parameters:

        - directory (str)
        - recursive (bool) = False
        """

        sub_directory: str
        sub_sub_directory: str
        for sub_directory in self._list_objects_v2_prefixes(
            prefix=self.get_absolute_path(directory)
        ):
            sub_directory = self.get_relative_path(sub_directory)
            yield sub_directory
            if recursive:
                for sub_sub_directory in self.iter_sub_directories(
                    sub_directory, recursive=recursive
                ):
                    yield sub_sub_directory

    # For backwards compatibility
    get_sub_directories = iter_sub_directories

    def _is_token_expired(self) -> bool:
        if self.assumed_role_arn:
            # We only need to check to see if our token has
            # expired if we are using an assumed role
            now: datetime = datetime.now()
            # If the assumed role expiration has a timezone, we need to
            # convert `now` to use that timezone as well
            if self._assumed_role_expires.tzinfo:
                now = now.astimezone(self._assumed_role_expires.tzinfo)
            return self._assumed_role_expires <= now
        return False

    def _get_bucket(self) -> Bucket:
        bucket: Optional[Bucket] = None
        bucket_candidate: Bucket
        profile_name_candidates: List[str] = [""]
        if not url_is_local(self.endpoint_url):
            profile_name_candidates = (
                boto3.session.Session().available_profiles
                + profile_name_candidates
            )
        profile_name: str
        indented_error_message: str
        error_message: str
        failed_profile_error_messages: List[str] = []
        arn: str = self.assumed_role_arn or _get_aws_role_arn()
        for profile_name in profile_name_candidates:
            try:
                profile_arn: str = arn or _get_profile_arn(profile_name)
                bucket_candidate = self._get_profile_bucket(profile_name)
                error_message = _cannot_list_objects_in_bucket_prefix(
                    bucket_candidate, self._absolute_root
                )
                if error_message:
                    indented_error_message = "\n  ".join(
                        error_message.split("\n")
                    )
                    failed_profile_error_messages.append(
                        f"- {profile_name or 'default profile'} "
                        f"(ARN: {profile_arn}): "
                        "Cannot list objects in "
                        f"s3://{bucket_candidate.name}/"
                        f"{self._absolute_root}\n"
                        f"  {indented_error_message}"
                    )
                else:
                    bucket = bucket_candidate
                    self._profile_name = profile_name
                    error_message = _cannot_put_in_bucket_prefix(
                        bucket_candidate, self._absolute_root
                    )
                    if error_message:
                        failed_profile_error_messages.append(
                            f"{profile_name or 'default profile'} "
                            f"(ARN: {profile_arn}): "
                            " Cannot put objects in "
                            f"s3://{bucket_candidate.name}/"
                            f"{self._absolute_root}\n"
                            f"{error_message}"
                        )
                    else:
                        # If we have read+write privileges, that's good
                        # enough, look no further
                        break
            except (
                botocore.exceptions.NoCredentialsError,
                botocore.exceptions.ClientError,
                botocore.exceptions.HTTPClientError,
            ):
                indented_error_message = "\n  ".join(
                    get_exception_text().split("\n")
                )
                failed_profile_error_messages.append(
                    f"- {profile_name or '(default profile)'}:\n"
                    f"  {indented_error_message}"
                )
        if bucket is None:
            error_message = (
                f"No profile with access to "
                f"s3://{self.bucket_name}/{self._absolute_root} could be "
                "found."
            )
            if failed_profile_error_messages:
                error_message = (
                    "{} An attempt was made to use each of the "
                    "following profiles:\n{}".format(
                        error_message,
                        "\n".join(failed_profile_error_messages),
                    )
                )
            raise PermissionError(error_message)
        log.info(
            f"Using profile: {self._profile_name}"
            if self._profile_name
            else "Using the default profile"
        )
        return bucket

    @property  # type: ignore
    def bucket(self) -> Bucket:
        """
        An instance of the dynamically created class `s3.Bucket`, a sub-class
        of `boto3.resources.base.ServiceResource`.
        """
        if self._is_token_expired():
            self._bucket = None
        if self._bucket is None:
            self._bucket = self._get_bucket()
        return self._bucket

    @property
    def credentials(self) -> ReadOnlyCredentials:
        return self._get_session().get_credentials().get_frozen_credentials()

    @property  # type: ignore
    def arn(self) -> str:
        return (
            self.assumed_role_arn
            or _get_aws_role_arn()
            or _get_profile_arn(self.profile_name)
        )

    @arn.setter
    def arn(self, arn: str) -> None:
        self.assumed_role_arn = arn

    def clear(self, directory: str = "") -> None:
        """
        Delete all files in a directory.

        Parameters:

        - directory (str): A directory path, relative to the file system root.
        """
        log.info(f'Deleting objects with prefix: "{directory}"')
        self.iter_object_summaries(directory).delete()

    def copy(self, source: str, target: str) -> None:
        """
        Copy a file from a `source` path (relative to the root directory) to a
        `target` path (relative to the root directory).

        Parameters:
        - source (str): The path of the file to copy.
        - target (str): The path to which the file should be copied.
        """

        copy_source: Dict[str, str] = {
            "Bucket": self.bucket.name,
            "Key": source,
        }

        target_key: str = self.get_absolute_path(target)

        target_object: Object = self.bucket.Object(
            target_key,
        )

        try:
            log.info(f"Attempting to copy file: {source}...")
            target_object.copy_from(CopySource=copy_source)
            log.info(f"...copy complete: {target_key}")
        except Exception as error:
            append_exception_text(error, f"\nFailed to copy: {source}")
            raise error

    def delete_directory(self, directory: str) -> None:
        """
        Delete all files in a directory.

        Parameters:

        - directory (str): A directory path, relative to the file system root.
        """
        self.clear(directory)

    def delete(self, path: str, version: str = "") -> None:
        """
        Delete a file.

        Parameters:

        - path (str)
        - version (str) = "": If provided, delete only the specified version
          of a versioned file.
        """
        response: Dict[str, Any] = self.bucket.delete_objects(
            Delete=dict(
                Objects=[
                    dict(
                        Key=self.get_absolute_path(path),
                        **(dict(VersionId=version) if version else {}),
                    ),
                ],
                Quiet=False,
            )
        )
        if "Errors" in response and response["Errors"]:
            message: str = json.dumps(response, indent=4)
            if response["Errors"][0]["Code"] == "AccessDenied":
                raise PermissionError(message)
            else:
                raise RuntimeError(message)

    def put(
        self,
        file: Union[bytes, IO[bytes]],
        path: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
        Save a file to the specified path (relative to `self.root`).

        Parameters:

        - file (typing.IO[bytes]|bytes): Either a file-like object from which
          the `.read()` method returns `bytes`, or an instance of `bytes`.
        - path (str): A path, relative to `self.root`, to which the file object
          will be saved.
        - metadata ({str:typing.Any}|None) = None
        """
        if not isinstance(file, bytes):
            try:
                file.seek(0)
            except (AttributeError, NotImplementedError):
                pass
        # Where a metadata key matches system-defined metadata, they need
        # to be passed as keyword arguments
        kwargs = _get_function_metadata_kwargs(
            Object.put,
            metadata,
            dict(Body=file, Key=self.get_absolute_path(path)),
        )
        try:
            log.info(f"Attempting to put file: {path}...")
            self.bucket.put_object(**kwargs)
            log.info(f"...put complete: {path}")
        except Exception as error:
            append_exception_text(error, f"\nFailed to put in: {path}")
            raise error
        return self.get_relative_path(path)

    def get(self, path: str, version: str = "") -> StreamingBody:
        """
        Retrieve a file.

        Parameters:

        - path (str): The path of a file relative to the root directory.
        - version (str): A specific version of the file to retrieve (optional).
        """
        assert path and isinstance(path, str)
        key: str = self.get_absolute_path(path)
        object_: Object = self.bucket.Object(
            key, **({"VersionId": version} if version else {})
        )
        try:
            return object_.get()["Body"]
        except Exception as error:
            append_exception_text(error, f"\nUnable to get file: {path}")
            raise error

    def update_metadata(self, path: str, metadata: Dict[str, str]) -> None:
        """
        Update metadata for an S3 object found at `path`.

        Parameters:

        - path (str): The path of a file relative to the root directory.
        - metadata ({str: typing.Any}): A dictionary containing
          metadata which should be associated with the file. See
          [the AWS metadata documentation](https://go.aws/3Xm7CxM) for a list
          of system-defined metadata. Note: All keys which do not match
          system-defined metadata fields will be interpreted as user-defined
          metadata.
        - clear (bool) = False: If `True`, all pre-existing metadata will
          be cleared prior to applying the new metadata.
        """
        key: str = self.get_absolute_path(path)
        s3_object: Object = self.bucket.Object(key)
        # Copy the metadata, so that we don't alter the referenced object
        metadata = copy(metadata)
        # Where a metadata key matches system-defined metadata, they need
        # to be passed as keyword arguments
        kwargs: Dict[str, Any] = _get_function_metadata_kwargs(
            Object.copy_from,
            metadata,
            dict(
                CopySource={"Bucket": self.bucket.name, "Key": key},
                Metadata=metadata,
                MetadataDirective="REPLACE",
            ),
        )
        # A case-insensitive update is needed in order to avoid
        # signature errors
        _case_insensitive_dictionary_update(
            s3_object.metadata, **kwargs["Metadata"]
        )
        kwargs["Metadata"] = s3_object.metadata
        s3_object.copy_from(**kwargs)

    def __repr__(self) -> str:
        return (
            f"{get_qualified_name(self.__class__)}(\n"
            f"    bucket_name={repr(self.bucket_name)},\n"
            f"    root={repr(self.root)},\n"
            f"    profile_name={repr(self.profile_name)},\n"
            f"    arn={repr(self.assumed_role_arn)},\n"
            f"    endpoint_url={repr(self.endpoint_url)}\n"
            ")"
        )

    def is_file(self, path: str) -> bool:
        """
        Return `True` if a *file* exists at the specified `path`.

        Parameters:

        - path (str): A path, relative to the file system root, at which to
          look for a file.
        """
        try:
            self.bucket.Object(self.get_absolute_path(path)).load()
            return True
        except botocore.exceptions.ClientError:
            return False

    def is_directory(self, path: str) -> bool:
        """
        Return `True` if a directory exists at the specified `path`.

        Parameters:

        - path (str): A path, relative to the file system root, at which to
          look for a directory.
        """
        try:
            # A "directory" exists if there are any files having that prefix
            next(iter(self.iter_file_paths(path)))
            return True
        except StopIteration:
            return False


def from_url(
    url: str,
    arn: str = "",
    profile_name: str = "",
    endpoint_url: str = "",
    config: Optional[botocore.config.Config] = None,
    region_name: str = "",
) -> SimpleStorageService:
    """
    Create an instance of `SimpleStorageService` from a URL

    Parameters:

    - url (str)
    - arn (str) = "": Only applicable for S3
    - profile_name (str) = "": Only applicable for S3
    - endpoint_url (str) = "": Only applicable for S3
    - config (botocore.config.Config|None) = None: Only applicable for S3
    - region_name (str) = "": Only applicable for S3
    """
    parse_result: ParseResult = urlparse(url)
    assert parse_result.scheme.lower() in ("s3", "s3a")
    return SimpleStorageService(
        bucket_name=parse_result.netloc,
        root=parse_result.path.lstrip("/ "),
        arn=arn,
        endpoint_url=endpoint_url,
        profile_name=profile_name,
        config=config,
        region_name=region_name,
    )


def use_localstack() -> None:
    """
    This function patches boto3 to use localstack
    """
    try:
        from localstack_client.patch import (  # type: ignore
            enable_local_endpoints,
            patch_expand_host_prefix,
        )

        enable_local_endpoints()
        patch_expand_host_prefix()
    except ImportError:
        # isort: split
        from localstack_client import (  # type: ignore # isort: skip
            session as localstack_client_session,
        )

        # isort: split

        localstack_session: localstack_client_session.Session = (
            localstack_client_session.Session()  # type: ignore
        )
        setattr(boto3, "client", localstack_session.client)
        setattr(boto3, "resource", localstack_session.resource)
        setattr(
            boto3.session,
            "Session",
            localstack_client_session.Session,  # type: ignore
        )


# Alias
S3: Type[FileSystem] = SimpleStorageService
