from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
import uuid
import os
from django.conf import settings

class Category(models.Model):
    """
    Hierarchical category system for organizing files.
    Supports nested categories for flexible organization.
    """
    name = models.CharField(
        max_length=255,
        unique=True,
        help_text=_("Category name - must be unique")
    )
    description = models.TextField(
        blank=True,
        help_text=_("Optional description of the category")
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children',
        help_text=_("Parent category if this is a subcategory")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_full_path(self):
        """Returns the full category path."""
        if self.parent:
            return f"{self.parent.get_full_path()} / {self.name}"
        return self.name

class File(models.Model):
    """
    Core file model for storing file metadata and path information.
    Handles various file types including firmware, documentation, and configs.
    """
    FILE_TYPES = [
        ('FIRMWARE', 'Firmware'),
        ('DOC', 'Documentation'),
        ('CONFIG', 'Configuration'),
        ('OTHER', 'Other'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=255,
        help_text=_("File name with extension")
    )
    path = models.CharField(
        max_length=1024,
        help_text=_("Relative path to file in storage")
    )
    type = models.CharField(
        max_length=10,
        choices=FILE_TYPES,
        default='OTHER',
        help_text=_("Type of file content")
    )
    size = models.BigIntegerField(
        help_text=_("File size in bytes")
    )
    checksum = models.CharField(
        max_length=64,
        help_text=_("SHA-256 checksum of file content")
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='files'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        unique_together = ['name', 'category']

    def __str__(self):
        return self.name

    def get_absolute_path(self):
        """Returns absolute path in storage."""
        return os.path.join(settings.MEDIA_ROOT, self.path)

class FileVersion(models.Model):
    """
    Tracks different versions of files.
    Enables version control and history tracking.
    """
    file = models.ForeignKey(
        File,
        on_delete=models.CASCADE,
        related_name='versions'
    )
    version = models.CharField(
        max_length=50,
        help_text=_("Version identifier")
    )
    upload_date = models.DateTimeField(auto_now_add=True)
    checksum = models.CharField(
        max_length=64,
        help_text=_("SHA-256 checksum of this version")
    )
    changelog = models.TextField(
        blank=True,
        help_text=_("Description of changes in this version")
    )
    
    class Meta:
        ordering = ['-upload_date']
        unique_together = ['file', 'version']

    def __str__(self):
        return f"{self.file.name} - {self.version}"

class Metadata(models.Model):
    """
    Flexible key-value metadata storage for files.
    Allows custom attributes and tagging.
    """
    file = models.ForeignKey(
        File,
        on_delete=models.CASCADE,
        related_name='metadata'
    )
    key = models.CharField(
        max_length=255,
        help_text=_("Metadata key name")
    )
    value = models.JSONField(
        help_text=_("Metadata value - supports JSON structure")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['key']
        unique_together = ['file', 'key']
        verbose_name_plural = "metadata"

    def __str__(self):
        return f"{self.file.name} - {self.key}"
