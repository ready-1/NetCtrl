"""
Tag management service for CMS content organization.

This module provides tag operations for device firmware and media content,
with optimized query performance and scale considerations.
"""

from typing import List, Optional, Set, Dict, Any
from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.db.models import Q, QuerySet
from ..models import Device, FirmwareVersion

class TagValidationError(ValidationError):
    """Custom exception for tag validation errors."""
    pass

class TagService:
    """Service class for managing content tags."""
    
    def __init__(self):
        """Initialize the tag service."""
        self._tag_cache: Dict[str, Set[str]] = {}

    @transaction.atomic
    def add_tag(self, content_id: int, tag: str, content_type: str) -> None:
        """
        Add a tag to a content item.

        Args:
            content_id: ID of the content item
            tag: Tag to add
            content_type: Type of content ('device' or 'firmware')

        Raises:
            TagValidationError: If validation fails
        """
        try:
            self._validate_tag(tag)
            self._add_tag_to_content(content_id, tag, content_type)
            self._invalidate_cache(content_id, content_type)
        except Exception as e:
            raise TagValidationError(f"Failed to add tag: {str(e)}")

    @transaction.atomic
    def remove_tag(self, content_id: int, tag: str, content_type: str) -> None:
        """
        Remove a tag from a content item.

        Args:
            content_id: ID of the content item
            tag: Tag to remove
            content_type: Type of content ('device' or 'firmware')

        Raises:
            TagValidationError: If validation fails
        """
        try:
            self._remove_tag_from_content(content_id, tag, content_type)
            self._invalidate_cache(content_id, content_type)
        except Exception as e:
            raise TagValidationError(f"Failed to remove tag: {str(e)}")

    def get_tags(self, content_id: int, content_type: str) -> Set[str]:
        """
        Get all tags for a content item.

        Args:
            content_id: ID of the content item
            content_type: Type of content ('device' or 'firmware')

        Returns:
            Set of tags associated with the content
        """
        cache_key = f"{content_type}_{content_id}"
        if cache_key in self._tag_cache:
            return self._tag_cache[cache_key]

        tags = self._get_content_tags(content_id, content_type)
        self._tag_cache[cache_key] = tags
        return tags

    def find_by_tag(self, tag: str, content_type: str) -> QuerySet:
        """
        Find content items by tag.

        Args:
            tag: Tag to search for
            content_type: Type of content ('device' or 'firmware')

        Returns:
            QuerySet of matching content items
        """
        if content_type == 'device':
            return Device.objects.filter(tags__contains=[tag])
        elif content_type == 'firmware':
            return FirmwareVersion.objects.filter(tags__contains=[tag])
        else:
            raise TagValidationError(f"Invalid content type: {content_type}")

    def _validate_tag(self, tag: str) -> None:
        """
        Validate a tag string.

        Args:
            tag: Tag to validate

        Raises:
            TagValidationError: If validation fails
        """
        if not tag or not isinstance(tag, str):
            raise TagValidationError("Tag must be a non-empty string")
        if len(tag) > 50:
            raise TagValidationError("Tag must be 50 characters or less")
        if not tag.replace("-", "").replace("_", "").isalnum():
            raise TagValidationError("Tag must contain only letters, numbers, hyphens and underscores")

    def _add_tag_to_content(self, content_id: int, tag: str, content_type: str) -> None:
        """Add tag to content in database."""
        model = self._get_model(content_type)
        content = model.objects.get(id=content_id)
        tags = set(content.tags or [])
        tags.add(tag)
        content.tags = list(tags)
        content.save()

    def _remove_tag_from_content(self, content_id: int, tag: str, content_type: str) -> None:
        """Remove tag from content in database."""
        model = self._get_model(content_type)
        content = model.objects.get(id=content_id)
        tags = set(content.tags or [])
        tags.discard(tag)
        content.tags = list(tags)
        content.save()

    def _get_content_tags(self, content_id: int, content_type: str) -> Set[str]:
        """Get tags from database."""
        model = self._get_model(content_type)
        content = model.objects.get(id=content_id)
        return set(content.tags or [])

    def _get_model(self, content_type: str) -> models.Model:
        """Get model class for content type."""
        if content_type == 'device':
            return Device
        elif content_type == 'firmware':
            return FirmwareVersion
        else:
            raise TagValidationError(f"Invalid content type: {content_type}")

    def _invalidate_cache(self, content_id: int, content_type: str) -> None:
        """Invalidate cache for content item."""
        cache_key = f"{content_type}_{content_id}"
        self._tag_cache.pop(cache_key, None)
