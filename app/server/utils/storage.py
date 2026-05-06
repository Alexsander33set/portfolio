import logging
import os
from copy import deepcopy
from typing import Any, Dict, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin, urlparse
from urllib.request import urlopen


logger = logging.getLogger(__name__)


class PublicStorageConnector:
    """Resolves public asset references stored in the database."""

    def __init__(
        self,
        base_url: Optional[str] = None,
        timeout: int = 5,
        max_text_bytes: int = 262144,
    ):
        self.base_url = (base_url or os.getenv('PUBLIC_STORAGE_BASE_URL', '')).strip()
        self.timeout = timeout
        self.max_text_bytes = max_text_bytes

    def build_public_url(self, reference: Any) -> Optional[str]:
        asset = self.normalize_reference(reference)
        if not asset:
            return None

        direct_url = asset.get('url')
        if self._is_public_url(direct_url):
            return direct_url

        storage_key = asset.get('storage_key')
        if not storage_key or not self.base_url:
            return None

        encoded_key = quote(str(storage_key).lstrip('/'), safe='/')
        return urljoin(f"{self.base_url.rstrip('/')}/", encoded_key)

    def resolve_asset(self, reference: Any) -> Optional[Dict[str, Any]]:
        asset = self.normalize_reference(reference)
        if not asset:
            return None

        resolved_url = self.build_public_url(asset)
        if not resolved_url:
            return None

        resolved_asset = deepcopy(asset)
        resolved_asset['url'] = resolved_url
        return resolved_asset

    def read_text(self, reference: Any) -> Optional[str]:
        public_url = self.build_public_url(reference)
        if not public_url:
            return None

        try:
            with urlopen(public_url, timeout=self.timeout) as response:
                content_type = response.headers.get_content_type()
                if content_type and not content_type.startswith('text/'):
                    logger.warning("Skipping non-text asset from public storage: %s", public_url)
                    return None

                raw_content = response.read(self.max_text_bytes + 1)
                if len(raw_content) > self.max_text_bytes:
                    logger.warning("Skipping oversized text asset from public storage: %s", public_url)
                    return None

                charset = response.headers.get_content_charset() or 'utf-8'
                return raw_content.decode(charset)
        except (HTTPError, URLError, UnicodeDecodeError) as error:
            logger.warning("Failed to read public storage asset %s: %s", public_url, error)
            return None

    @staticmethod
    def normalize_reference(reference: Any) -> Optional[Dict[str, Any]]:
        if not reference:
            return None

        if isinstance(reference, str):
            if PublicStorageConnector._is_public_url(reference):
                return {'url': reference}

            return {'storage_key': reference}

        if isinstance(reference, dict):
            normalized_reference = deepcopy(reference)
            if 'key' in normalized_reference and 'storage_key' not in normalized_reference:
                normalized_reference['storage_key'] = normalized_reference['key']
            return normalized_reference

        return None

    @staticmethod
    def _is_public_url(value: Optional[str]) -> bool:
        if not value or not isinstance(value, str):
            return False

        parsed_value = urlparse(value)
        return parsed_value.scheme in {'http', 'https'} and bool(parsed_value.netloc)
