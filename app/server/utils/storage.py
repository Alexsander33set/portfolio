import logging
import os
from copy import deepcopy
from typing import Any, Dict, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import urlopen

import boto3
from botocore.client import Config
from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)

DEFAULT_SIGNED_URL_TTL = 3600
MAX_TEXT_BYTES = 256 * 1024


def _parse_signed_url_ttl(raw_value: Any) -> int:
    try:
        return int(raw_value)
    except (TypeError, ValueError):
        logger.warning(
            "Invalid STORAGE_SIGNED_URL_TTL value %r. Falling back to %s seconds.",
            raw_value,
            DEFAULT_SIGNED_URL_TTL,
        )
        return DEFAULT_SIGNED_URL_TTL


class StorageConfigurationError(EnvironmentError):
    """Raised when object storage credentials are required but missing."""


class ObjectStorageConnector:
    """Generic S3-compatible object storage connector."""

    def __init__(
        self,
        bucket_name: Optional[str] = None,
        endpoint_url: Optional[str] = None,
        access_key_id: Optional[str] = None,
        secret_access_key: Optional[str] = None,
        region_name: Optional[str] = None,
        signed_url_ttl: Optional[int] = None,
        timeout: int = 5,
        max_text_bytes: int = MAX_TEXT_BYTES,
        client: Any = None,
    ):
        self.bucket_name = (bucket_name or os.getenv('STORAGE_BUCKET_NAME', '')).strip()
        self.endpoint_url = (endpoint_url or os.getenv('STORAGE_ENDPOINT_URL', '')).strip()
        self.access_key_id = (access_key_id or os.getenv('STORAGE_ACCESS_KEY_ID', '')).strip()
        self.secret_access_key = (secret_access_key or os.getenv('STORAGE_SECRET_ACCESS_KEY', '')).strip()
        self.region_name = (region_name or os.getenv('STORAGE_REGION', 'auto')).strip() or 'auto'
        self.signed_url_ttl = _parse_signed_url_ttl(
            os.getenv('STORAGE_SIGNED_URL_TTL', signed_url_ttl or DEFAULT_SIGNED_URL_TTL)
        )
        self.timeout = timeout
        self.max_text_bytes = max_text_bytes
        self._client = client

    @property
    def client(self):
        if self._client is None and self.is_configured():
            self._client = boto3.client(
                's3',
                endpoint_url=self.endpoint_url,
                aws_access_key_id=self.access_key_id,
                aws_secret_access_key=self.secret_access_key,
                region_name=self.region_name,
                config=Config(signature_version='s3v4'),
            )
        return self._client

    def is_configured(self) -> bool:
        return all([
            self.bucket_name,
            self.endpoint_url,
            self.access_key_id,
            self.secret_access_key,
        ])

    def build_download_url(self, reference: Any, expires_in: Optional[int] = None) -> Optional[str]:
        asset = self.normalize_reference(reference)
        if not asset:
            return None

        direct_url = asset.get('url')
        if self._is_url(direct_url):
            return direct_url

        storage_key = self.get_storage_key(asset)
        if not storage_key or not self.is_configured():
            return None

        return self.client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': self.bucket_name,
                'Key': storage_key,
            },
            ExpiresIn=expires_in or self.signed_url_ttl,
        )

    def resolve_asset(self, reference: Any, expires_in: Optional[int] = None) -> Optional[Dict[str, Any]]:
        asset = self.normalize_reference(reference)
        if not asset:
            return None

        resolved_asset = deepcopy(asset)
        resolved_url = self.build_download_url(resolved_asset, expires_in=expires_in)
        if resolved_url:
            resolved_asset['url'] = resolved_url
        return resolved_asset

    def read_text(self, reference: Any) -> Optional[str]:
        asset = self.normalize_reference(reference)
        if not asset:
            return None

        storage_key = self.get_storage_key(asset)
        if storage_key and self.is_configured():
            try:
                response = self.client.get_object(Bucket=self.bucket_name, Key=storage_key)
                content_type = response.get('ContentType', '')
                if content_type and not content_type.startswith('text/'):
                    logger.warning("Skipping non-text storage asset: %s", storage_key)
                    return None

                raw_content = response['Body'].read(self.max_text_bytes + 1)
                if len(raw_content) > self.max_text_bytes:
                    logger.warning("Skipping oversized text asset from storage: %s", storage_key)
                    return None

                return raw_content.decode('utf-8')
            except (ClientError, UnicodeDecodeError) as error:
                logger.warning("Failed to read private storage asset %s: %s", storage_key, error)
                return None

        direct_url = asset.get('url')
        if self._is_url(direct_url):
            return self._read_text_from_url(direct_url)

        return None

    def upload_object(
        self,
        storage_key: str,
        body: bytes,
        content_type: str = 'application/octet-stream',
        metadata: Optional[Dict[str, str]] = None,
        cache_control: Optional[str] = None,
    ) -> Dict[str, Any]:
        normalized_key = self._normalize_storage_key(storage_key)
        self._require_client()

        payload = {
            'Bucket': self.bucket_name,
            'Key': normalized_key,
            'Body': body,
            'ContentType': content_type,
        }
        if metadata:
            payload['Metadata'] = metadata
        if cache_control:
            payload['CacheControl'] = cache_control

        self.client.put_object(**payload)
        return self.resolve_asset({
            'storage_key': normalized_key,
            'content_type': content_type,
            'metadata': metadata or {},
        })

    def upload_text(
        self,
        storage_key: str,
        content: str,
        content_type: str = 'text/markdown; charset=utf-8',
        metadata: Optional[Dict[str, str]] = None,
        cache_control: Optional[str] = None,
    ) -> Dict[str, Any]:
        return self.upload_object(
            storage_key=storage_key,
            body=content.encode('utf-8'),
            content_type=content_type,
            metadata=metadata,
            cache_control=cache_control,
        )

    def update_object(
        self,
        storage_key: str,
        body: bytes,
        content_type: str = 'application/octet-stream',
        metadata: Optional[Dict[str, str]] = None,
        cache_control: Optional[str] = None,
    ) -> Dict[str, Any]:
        normalized_key = self._normalize_storage_key(storage_key)
        self._require_client()
        if not self.object_exists(normalized_key):
            raise FileNotFoundError(f"Storage object not found: {normalized_key}")

        return self.upload_object(
            storage_key=normalized_key,
            body=body,
            content_type=content_type,
            metadata=metadata,
            cache_control=cache_control,
        )

    def delete_object(self, reference: Any) -> bool:
        storage_key = self.get_storage_key(reference)
        if not storage_key:
            return False

        self._require_client()
        self.client.delete_object(Bucket=self.bucket_name, Key=storage_key)
        return True

    def object_exists(self, reference: Any) -> bool:
        storage_key = self.get_storage_key(reference)
        if not storage_key:
            return False

        self._require_client()
        try:
            self.client.head_object(Bucket=self.bucket_name, Key=storage_key)
            return True
        except ClientError as error:
            error_code = str(error.response.get('Error', {}).get('Code', ''))
            if error_code in {'404', 'NoSuchKey', 'NotFound'}:
                return False
            raise

    def _require_client(self):
        if not self.is_configured():
            raise StorageConfigurationError(
                'Private object storage is not configured. '
                'Set STORAGE_BUCKET_NAME, STORAGE_ENDPOINT_URL, '
                'STORAGE_ACCESS_KEY_ID, and STORAGE_SECRET_ACCESS_KEY.'
            )
        return self.client

    def _read_text_from_url(self, url: str) -> Optional[str]:
        try:
            with urlopen(url, timeout=self.timeout) as response:
                content_type = response.headers.get_content_type()
                if content_type and not content_type.startswith('text/'):
                    logger.warning("Skipping non-text storage asset URL: %s", url)
                    return None

                raw_content = response.read(self.max_text_bytes + 1)
                if len(raw_content) > self.max_text_bytes:
                    logger.warning("Skipping oversized text asset URL: %s", url)
                    return None

                charset = response.headers.get_content_charset() or 'utf-8'
                return raw_content.decode(charset)
        except (HTTPError, URLError, UnicodeDecodeError) as error:
            logger.warning("Failed to read storage asset URL %s: %s", url, error)
            return None

    @staticmethod
    def normalize_reference(reference: Any) -> Optional[Dict[str, Any]]:
        if not reference:
            return None

        if isinstance(reference, str):
            if ObjectStorageConnector._is_url(reference):
                return {'url': reference}
            return {'storage_key': ObjectStorageConnector._normalize_storage_key(reference)}

        if isinstance(reference, dict):
            normalized_reference = deepcopy(reference)
            if 'key' in normalized_reference and 'storage_key' not in normalized_reference:
                normalized_reference['storage_key'] = normalized_reference['key']

            if normalized_reference.get('storage_key'):
                normalized_reference['storage_key'] = ObjectStorageConnector._normalize_storage_key(
                    normalized_reference['storage_key']
                )
            return normalized_reference

        return None

    @staticmethod
    def get_storage_key(reference: Any) -> Optional[str]:
        normalized_reference = ObjectStorageConnector.normalize_reference(reference)
        if not normalized_reference:
            return None
        return normalized_reference.get('storage_key')

    @staticmethod
    def _normalize_storage_key(storage_key: str) -> str:
        return str(storage_key).lstrip('/')

    @staticmethod
    def _is_url(value: Optional[str]) -> bool:
        if not value or not isinstance(value, str):
            return False

        parsed_value = urlparse(value)
        return parsed_value.scheme in {'http', 'https'} and bool(parsed_value.netloc)
