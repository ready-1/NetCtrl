"""
Category management service for CMS content organization.

This module provides hierarchical category operations for device firmware and media content,
with efficient tree traversal and path management.
"""

from typing import List, Optional, Dict, Any, Set
from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.db.models import Q, QuerySet
from ..models import Device, FirmwareVersion, Category

class CategoryValidationError(ValidationError):
    """Custom exception for category validation errors."""
    pass

class CategoryService:
    """Service class for managing content categories."""

    def __init__(self):
        """Initialize the category service."""
        self._path_cache: Dict[str, str] = {}
        self._hierarchy_cache: Dict[int, List[Category]] = {}

    @transaction.atomic
    def create_category(self, name: str, parent_id: Optional[int] = None) -> Category:
        """
        Create a new category.

        Args:
            name: Name of the category
            parent_id: Optional ID of parent category

        Returns:
            Created category instance

        Raises:
            CategoryValidationError: If validation fails
        """
        try:
            self._validate_category_name(name)
            path = self._generate_path(name, parent_id)
            category = Category.objects.create(
                name=name,
                parent_id=parent_id,
                path=path
            )
            self._invalidate_cache()
            return category
        except Exception as e:
            raise CategoryValidationError(f"Failed to create category: {str(e)}")

    @transaction.atomic
    def update_category(self, category_id: int, name: str, parent_id: Optional[int] = None) -> Category:
        """
        Update an existing category.

        Args:
            category_id: ID of category to update
            name: New name for category
            parent_id: Optional new parent ID

        Returns:
            Updated category instance

        Raises:
            CategoryValidationError: If validation fails
        """
        try:
            category = Category.objects.get(id=category_id)
            if name != category.name:
                self._validate_category_name(name)
                category.name = name
            if parent_id != category.parent_id:
                self._validate_parent(parent_id, category_id)
                category.parent_id = parent_id
                category.path = self._generate_path(name, parent_id)
            category.save()
            self._invalidate_cache()
            return category
        except Exception as e:
            raise CategoryValidationError(f"Failed to update category: {str(e)}")

    @transaction.atomic
    def delete_category(self, category_id: int) -> None:
        """
        Delete a category and optionally move children.

        Args:
            category_id: ID of category to delete

        Raises:
            CategoryValidationError: If validation fails
        """
        try:
            category = Category.objects.get(id=category_id)
            if Category.objects.filter(parent_id=category_id).exists():
                raise CategoryValidationError("Cannot delete category with children")
            category.delete()
            self._invalidate_cache()
        except Exception as e:
            raise CategoryValidationError(f"Failed to delete category: {str(e)}")

    def get_hierarchy(self) -> List[Dict[str, Any]]:
        """
        Get complete category hierarchy.

        Returns:
            List of category dictionaries with children
        """
        categories = Category.objects.all().order_by('path')
        hierarchy: List[Dict[str, Any]] = []
        category_map: Dict[int, Dict[str, Any]] = {}

        for category in categories:
            node = {
                'id': category.id,
                'name': category.name,
                'children': []
            }
            category_map[category.id] = node
            if category.parent_id is None:
                hierarchy.append(node)
            else:
                parent = category_map.get(category.parent_id)
                if parent:
                    parent['children'].append(node)

        return hierarchy

    def get_path(self, category_id: int) -> str:
        """
        Get full path for category.

        Args:
            category_id: ID of category

        Returns:
            Full path string

        Raises:
            CategoryValidationError: If category not found
        """
        if category_id in self._path_cache:
            return self._path_cache[category_id]

        try:
            category = Category.objects.get(id=category_id)
            path = category.path
            self._path_cache[category_id] = path
            return path
        except Category.DoesNotExist:
            raise CategoryValidationError(f"Category not found: {category_id}")

    def find_by_path(self, path: str) -> Optional[Category]:
        """
        Find category by path.

        Args:
            path: Category path to search for

        Returns:
            Category instance if found, None otherwise
        """
        return Category.objects.filter(path=path).first()

    def get_children(self, category_id: int) -> QuerySet:
        """
        Get direct children of category.

        Args:
            category_id: ID of parent category

        Returns:
            QuerySet of child categories
        """
        return Category.objects.filter(parent_id=category_id)

    def get_descendants(self, category_id: int) -> QuerySet:
        """
        Get all descendants of category.

        Args:
            category_id: ID of ancestor category

        Returns:
            QuerySet of descendant categories
        """
        category = Category.objects.get(id=category_id)
        return Category.objects.filter(path__startswith=f"{category.path}/")

    def _validate_category_name(self, name: str) -> None:
        """Validate category name."""
        if not name or not isinstance(name, str):
            raise CategoryValidationError("Category name must be a non-empty string")
        if len(name) > 100:
            raise CategoryValidationError("Category name must be 100 characters or less")
        if not name.replace(" ", "").replace("-", "").replace("_", "").isalnum():
            raise CategoryValidationError("Category name must contain only letters, numbers, spaces, hyphens and underscores")

    def _validate_parent(self, parent_id: Optional[int], category_id: int) -> None:
        """Validate parent category."""
        if parent_id is None:
            return
        if parent_id == category_id:
            raise CategoryValidationError("Category cannot be its own parent")
        parent = Category.objects.get(id=parent_id)
        if parent.path.startswith(f"{self.get_path(category_id)}/"):
            raise CategoryValidationError("Category cannot be a descendant of itself")

    def _generate_path(self, name: str, parent_id: Optional[int]) -> str:
        """Generate path for category."""
        if parent_id is None:
            return name
        parent = Category.objects.get(id=parent_id)
        return f"{parent.path}/{name}"

    def _invalidate_cache(self) -> None:
        """Invalidate all caches."""
        self._path_cache.clear()
        self._hierarchy_cache.clear()
