"""
Tag management service for CMS content organization.

This module provides tag operations for device firmware and media content,
with optimized query performance and scale considerations.
"""

from typing import List, Optional, Set, Dict, Any
from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.db.models import Q, QuerySet
from ..models import File

class TagValidationError(ValidationError):
    """Custom exception for tag validation errors."""
    pass

class TagService:
    """Service class for managing file tags."""
    
    def __init__(self):
        """Initialize the tag service."""
        self._tag_cache: Dict[str, Set[str]] = {}

    @transaction.atomic
    def add_tag(self, file_id: str, tag: str, content_type: str = 'file') -> None:
        """
        Add a tag to a file.

        Args:
            file_id: ID of the file
            tag: Tag to add
            content_type: Must be 'file'

        Raises:
            TagValidationError: If validation fails
        """
        if content_type != 'file':
            raise TagValidationError("Only file content type is supported")
            
        try:
            self._validate_tag(tag)
            file = File.objects.get(id=file_id)
            tags = set(file.tags or [])
            tags.add(tag)
            file.tags = list(tags)
            file.save()
            self._invalidate_cache(file_id)
        except File.DoesNotExist:
            raise TagValidationError("File not found")
        except Exception as e:
            raise TagValidationError(f"Failed to add tag: {str(e)}")

    @transaction.atomic
    def remove_tag(self, file_id: str, tag: str, content_type: str = 'file') -> None:
        """
        Remove a tag from a file.

        Args:
            file_id: ID of the file
            tag: Tag to remove
            content_type: Must be 'file'

        Raises:
            TagValidationError: If validation fails
        """
        if content_type != 'file':
            raise TagValidationError("Only file content type is supported")
            
        try:
            file = File.objects.get(id=file_id)
            tags = set(file.tags or [])
            tags.discard(tag)
            file.tags = list(tags)
            file.save()
            self._invalidate_cache(file_id)
        except File.DoesNotExist:
            raise TagValidationError("File not found")
        except Exception as e:
            raise TagValidationError(f"Failed to remove tag: {str(e)}")

    def get_tags(self, file_id: str, content_type: str = 'file') -> Set[str]:
        """
        Get all tags for a file.

        Args:
            file_id: ID of the file
            content_type: Must be 'file'

        Returns:
            Set of tags associated with the file
        """
        if content_type != 'file':
            raise TagValidationError("Only file content type is supported")
            
        cache_key = f"file_{file_id}"
        if cache_key in self._tag_cache:
            return self._tag_cache[cache_key]

        try:
            file = File.objects.get(id=file_id)
            tags = set(file.tags or [])
            self._tag_cache[cache_key] = tags
            return tags
        except File.DoesNotExist:
            raise TagValidationError("File not found")

    def get_all_tags(self, content_type: str = 'file') -> Set[str]:
        """
        Get all unique tags in the system.

        Args:
            content_type: Must be 'file'

        Returns:
            Set of all unique tags
        """
        if content_type != 'file':
            raise TagValidationError("Only file content type is supported")
            
        all_tags = set()
        files = File.objects.exclude(tags=[]).values_list('tags', flat=True)
        for tags in files:
            all_tags.update(tags)
        return all_tags

    def filter_by_tags(self, tags: List[str], content_type: str = 'file') -> QuerySet:
        """
        Find files that have all specified tags.

        Args:
            tags: List of tags to filter by
            content_type: Must be 'file'

        Returns:
            QuerySet of matching files
        """
        if content_type != 'file':
            raise TagValidationError("Only file content type is supported")
            
        # Start with all files
        query = File.objects.all()
        
        # Filter files that have all the specified tags
        for tag in tags:
            # Use list comprehension to filter in memory
            files = [file for file in query if tag in (file.tags or [])]
            # Convert back to queryset
            query = File.objects.filter(id__in=[file.id for file in files])
            
        return query

    def _validate_tag(self, tag: str) -> None:
        """Validate a tag string."""
        if not tag or not isinstance(tag, str):
            raise TagValidationError("Tag must be a non-empty string")
        if len(tag) > 50:
            raise TagValidationError("Tag must be 50 characters or less")
        if not tag.replace("-", "").replace("_", "").isalnum():
            raise TagValidationError("Tag must contain only letters, numbers, hyphens and underscores")

    def _invalidate_cache(self, file_id: str) -> None:
        """Invalidate cache for file."""
        cache_key = f"file_{file_id}"
        self._tag_cache.pop(cache_key, None)
