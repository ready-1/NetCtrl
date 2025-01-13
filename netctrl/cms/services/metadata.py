"""
Metadata management service for CMS content organization.

This module provides metadata operations for device firmware and media content,
with support for device compatibility and version tracking.
"""

from typing import List, Optional, Dict, Any, Set
from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.db.models import Q, QuerySet
from ..models import Device, FirmwareVersion

class MetadataValidationError(ValidationError):
    """Custom exception for metadata validation errors."""
    pass

class MetadataService:
    """Service class for managing content metadata."""

    def __init__(self):
        """Initialize the metadata service."""
        self._metadata_cache: Dict[str, Dict[str, Any]] = {}

    @transaction.atomic
    def set_metadata(self, content_id: int, metadata: Dict[str, Any], content_type: str) -> None:
        """
        Set metadata for a content item.

        Args:
            content_id: ID of the content item
            metadata: Dictionary of metadata values
            content_type: Type of content ('device' or 'firmware')

        Raises:
            MetadataValidationError: If validation fails
        """
        try:
            self._validate_metadata(metadata, content_type)
            self._set_content_metadata(content_id, metadata, content_type)
            self._invalidate_cache(content_id, content_type)
        except Exception as e:
            raise MetadataValidationError(f"Failed to set metadata: {str(e)}")

    def get_metadata(self, content_id: int, content_type: str) -> Dict[str, Any]:
        """
        Get metadata for a content item.

        Args:
            content_id: ID of the content item
            content_type: Type of content ('device' or 'firmware')

        Returns:
            Dictionary of metadata values
        """
        cache_key = f"{content_type}_{content_id}"
        if cache_key in self._metadata_cache:
            return self._metadata_cache[cache_key]

        metadata = self._get_content_metadata(content_id, content_type)
        self._metadata_cache[cache_key] = metadata
        return metadata

    def check_compatibility(self, device_id: int, firmware_id: int) -> bool:
        """
        Check if firmware is compatible with device.

        Args:
            device_id: ID of device
            firmware_id: ID of firmware version

        Returns:
            True if compatible, False otherwise
        """
        try:
            device = Device.objects.get(id=device_id)
            firmware = FirmwareVersion.objects.get(id=firmware_id)
            
            device_meta = self.get_metadata(device_id, 'device')
            firmware_meta = self.get_metadata(firmware_id, 'firmware')
            
            return self._check_version_compatibility(
                device_meta.get('version_requirements', {}),
                firmware_meta.get('version_info', {})
            )
        except Exception:
            return False

    def find_compatible_firmware(self, device_id: int) -> QuerySet:
        """
        Find all firmware versions compatible with device.

        Args:
            device_id: ID of device

        Returns:
            QuerySet of compatible firmware versions
        """
        device_meta = self.get_metadata(device_id, 'device')
        requirements = device_meta.get('version_requirements', {})
        
        query = Q()
        for key, value in requirements.items():
            query &= Q(metadata__version_info__contains={key: value})
            
        return FirmwareVersion.objects.filter(query)

    def track_version(self, content_id: int, version_info: Dict[str, Any], content_type: str) -> None:
        """
        Track version information for content.

        Args:
            content_id: ID of the content item
            version_info: Dictionary of version information
            content_type: Type of content ('device' or 'firmware')

        Raises:
            MetadataValidationError: If validation fails
        """
        try:
            metadata = self.get_metadata(content_id, content_type)
            metadata['version_info'] = version_info
            self.set_metadata(content_id, metadata, content_type)
        except Exception as e:
            raise MetadataValidationError(f"Failed to track version: {str(e)}")

    def _validate_metadata(self, metadata: Dict[str, Any], content_type: str) -> None:
        """Validate metadata structure."""
        if not isinstance(metadata, dict):
            raise MetadataValidationError("Metadata must be a dictionary")
            
        required_fields = self._get_required_fields(content_type)
        for field in required_fields:
            if field not in metadata:
                raise MetadataValidationError(f"Missing required field: {field}")

    def _get_required_fields(self, content_type: str) -> Set[str]:
        """Get required metadata fields for content type."""
        if content_type == 'device':
            return {'model', 'manufacturer', 'version_requirements'}
        elif content_type == 'firmware':
            return {'version_info', 'release_date', 'checksum'}
        else:
            raise MetadataValidationError(f"Invalid content type: {content_type}")

    def _set_content_metadata(self, content_id: int, metadata: Dict[str, Any], content_type: str) -> None:
        """Set metadata in database."""
        model = self._get_model(content_type)
        content = model.objects.get(id=content_id)
        content.metadata = metadata
        content.save()

    def _get_content_metadata(self, content_id: int, content_type: str) -> Dict[str, Any]:
        """Get metadata from database."""
        model = self._get_model(content_type)
        content = model.objects.get(id=content_id)
        return content.metadata or {}

    def _get_model(self, content_type: str) -> models.Model:
        """Get model class for content type."""
        if content_type == 'device':
            return Device
        elif content_type == 'firmware':
            return FirmwareVersion
        else:
            raise MetadataValidationError(f"Invalid content type: {content_type}")

    def _check_version_compatibility(
        self,
        requirements: Dict[str, Any],
        version_info: Dict[str, Any]
    ) -> bool:
        """Check version compatibility."""
        for key, required in requirements.items():
            if key not in version_info:
                return False
            if not self._compare_versions(required, version_info[key]):
                return False
        return True

    def _compare_versions(self, required: Any, actual: Any) -> bool:
        """Compare version values."""
        if isinstance(required, dict) and isinstance(actual, dict):
            return all(
                k in actual and self._compare_versions(v, actual[k])
                for k, v in required.items()
            )
        return required == actual

    def _invalidate_cache(self, content_id: int, content_type: str) -> None:
        """Invalidate cache for content item."""
        cache_key = f"{content_type}_{content_id}"
        self._metadata_cache.pop(cache_key, None)
