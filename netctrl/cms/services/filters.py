"""
Filter service for CMS content organization.

This module provides filtering operations across tags, categories, and metadata
for device firmware and media content.
"""

from typing import List, Optional, Dict, Any, Set
from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.db.models import Q, QuerySet
from ..models import Device, FirmwareVersion, Category

class FilterValidationError(ValidationError):
    """Custom exception for filter validation errors."""
    pass

class FilterService:
    """Service class for content filtering."""

    def __init__(self):
        """Initialize the filter service."""
        self._query_cache: Dict[str, QuerySet] = {}

    def filter_by_tags(
        self,
        tags: List[str],
        content_type: str,
        match_all: bool = True
    ) -> QuerySet:
        """
        Filter content by tags.

        Args:
            tags: List of tags to filter by
            content_type: Type of content ('device' or 'firmware')
            match_all: If True, content must have all tags

        Returns:
            QuerySet of matching content items
        """
        if not tags:
            return self._get_model(content_type).objects.none()

        query = Q()
        for tag in tags:
            tag_query = Q(tags__contains=[tag])
            if match_all:
                query &= tag_query
            else:
                query |= tag_query

        return self._get_model(content_type).objects.filter(query)

    def filter_by_category(
        self,
        category_id: int,
        content_type: str,
        include_subcategories: bool = True
    ) -> QuerySet:
        """
        Filter content by category.

        Args:
            category_id: ID of category to filter by
            content_type: Type of content ('device' or 'firmware')
            include_subcategories: If True, include content in subcategories

        Returns:
            QuerySet of matching content items
        """
        try:
            category = Category.objects.get(id=category_id)
            if include_subcategories:
                categories = Category.objects.filter(
                    path__startswith=f"{category.path}/"
                ).values_list('id', flat=True)
                return self._get_model(content_type).objects.filter(
                    Q(category_id=category_id) | Q(category_id__in=categories)
                )
            return self._get_model(content_type).objects.filter(
                category_id=category_id
            )
        except Category.DoesNotExist:
            raise FilterValidationError(f"Category not found: {category_id}")

    def filter_by_metadata(
        self,
        criteria: Dict[str, Any],
        content_type: str
    ) -> QuerySet:
        """
        Filter content by metadata criteria.

        Args:
            criteria: Dictionary of metadata field criteria
            content_type: Type of content ('device' or 'firmware')

        Returns:
            QuerySet of matching content items
        """
        query = Q()
        for field, value in criteria.items():
            if isinstance(value, dict):
                for subfield, subvalue in value.items():
                    query &= Q(**{f"metadata__{field}__{subfield}": subvalue})
            else:
                query &= Q(**{f"metadata__{field}": value})

        return self._get_model(content_type).objects.filter(query)

    def combine_filters(
        self,
        tags: Optional[List[str]] = None,
        category_id: Optional[int] = None,
        metadata: Optional[Dict[str, Any]] = None,
        content_type: str = 'device'
    ) -> QuerySet:
        """
        Combine multiple filter criteria.

        Args:
            tags: Optional list of tags
            category_id: Optional category ID
            metadata: Optional metadata criteria
            content_type: Type of content ('device' or 'firmware')

        Returns:
            QuerySet of matching content items
        """
        query = self._get_model(content_type).objects.all()

        if tags:
            query = query.filter(
                id__in=self.filter_by_tags(tags, content_type).values('id')
            )

        if category_id is not None:
            query = query.filter(
                id__in=self.filter_by_category(category_id, content_type).values('id')
            )

        if metadata:
            query = query.filter(
                id__in=self.filter_by_metadata(metadata, content_type).values('id')
            )

        return query

    def search_content(
        self,
        query_string: str,
        content_type: str,
        fields: Optional[List[str]] = None
    ) -> QuerySet:
        """
        Search content across specified fields.

        Args:
            query_string: Search query string
            content_type: Type of content ('device' or 'firmware')
            fields: Optional list of fields to search

        Returns:
            QuerySet of matching content items
        """
        if not fields:
            fields = ['name', 'description', 'metadata']

        query = Q()
        for field in fields:
            if field == 'metadata':
                query |= Q(metadata__icontains=query_string)
            else:
                query |= Q(**{f"{field}__icontains": query_string})

        return self._get_model(content_type).objects.filter(query)

    def _get_model(self, content_type: str) -> models.Model:
        """Get model class for content type."""
        if content_type == 'device':
            return Device
        elif content_type == 'firmware':
            return FirmwareVersion
        else:
            raise FilterValidationError(f"Invalid content type: {content_type}")

    def _get_cache_key(self, **kwargs: Any) -> str:
        """Generate cache key from filter parameters."""
        return '_'.join(f"{k}:{str(v)}" for k, v in sorted(kwargs.items()))

    def _invalidate_cache(self) -> None:
        """Invalidate query cache."""
        self._query_cache.clear()
