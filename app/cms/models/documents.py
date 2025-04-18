"""
Document models for the NetCtrl CMS.

This module defines models for content management:
- Category: For organizing documents in a hierarchy
- Tag: For tagging and filtering documents
- Document: The main content type with publishing workflow
- DocumentVersion: For tracking document version history
- DocumentFile: Junction model to associate files with documents
"""

from django.db import models, transaction
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
import uuid
import logging
from .files import File

logger = logging.getLogger(__name__)

class Category(models.Model):
    """
    Category model for organizing documents.
    
    Categories can be nested to create a hierarchy.
    
    Attributes:
        name (CharField): The category name
        slug (SlugField): URL-friendly version of the name
        description (TextField): Optional description of the category
        parent (ForeignKey): Optional parent category creating a hierarchy
        created_at (DateTimeField): When the category was created
    """
    name = models.CharField("Name", max_length=100)
    slug = models.SlugField("Slug", max_length=100, unique=True)
    description = models.TextField("Description", blank=True)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='children',
        verbose_name="Parent Category"
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Auto-generate slug if not provided."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        logger.info(f"Category saved: {self.name}")
    
    def get_absolute_url(self):
        """Get URL for category detail page."""
        return reverse('cms:category_detail', kwargs={'slug': self.slug})


class Tag(models.Model):
    """
    Tag model for categorizing documents.
    
    Attributes:
        name (CharField): The tag name
        slug (SlugField): URL-friendly version of the name
    """
    name = models.CharField("Name", max_length=50)
    slug = models.SlugField("Slug", max_length=50, unique=True)
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Auto-generate slug if not provided."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        logger.info(f"Tag saved: {self.name}")
    
    def get_absolute_url(self):
        """Get URL for tag detail page."""
        return reverse('cms:tag_detail', kwargs={'slug': self.slug})


class Document(models.Model):
    """
    Document model - the primary content type for the CMS.
    
    Documents have a publishing workflow with draft and published states.
    
    Attributes:
        title (CharField): The document title
        slug (SlugField): URL-friendly version of the title
        content (TextField): The main document content (HTML or Markdown)
        content_format (CharField): Format of the content (HTML or Markdown)
        excerpt (TextField): Short summary or teaser
        author (ForeignKey): User who created the document
        category (ForeignKey): Primary category for the document
        tags (ManyToManyField): Associated tags
        featured_image (ImageField): Main image for the document
        status (CharField): Document status (draft or published)
        created_at (DateTimeField): When the document was created
        updated_at (DateTimeField): When the document was last updated
        published_at (DateTimeField): When the document was published
        uuid (UUIDField): Unique identifier for the document
    """
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    CONTENT_FORMAT_CHOICES = (
        ('markdown', 'Markdown'),
        ('plaintext', 'Plain Text'),
    )
    
    title = models.CharField("Title", max_length=255)
    slug = models.SlugField("Slug", max_length=255, unique=True)
    content = models.TextField("Content")
    excerpt = models.TextField("Excerpt", blank=True)
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='documents',
        verbose_name="Author"
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='documents',
        verbose_name="Category"
    )
    tags = models.ManyToManyField(
        Tag, 
        blank=True, 
        related_name='documents',
        verbose_name="Tags"
    )
    featured_image = models.ImageField(
        "Featured Image",
        upload_to='documents/featured_images/%Y/%m/', 
        null=True, 
        blank=True
    )
    content_format = models.CharField(
        "Content Format",
        max_length=10,
        choices=CONTENT_FORMAT_CHOICES,
        default='markdown'
    )
    status = models.CharField(
        "Status",
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='draft'
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    published_at = models.DateTimeField("Published at", null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """Auto-generate slug if not provided."""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        logger.info(f"Document saved: {self.title} by {self.author.username}")
    
    def get_absolute_url(self):
        """Get URL for document detail page."""
        return reverse('cms:document_detail', kwargs={'slug': self.slug})
    
    @property
    def is_published(self):
        """Check if document is published."""
        return self.status == 'published'
    
    def publish(self):
        """Publish the document."""
        self.status = 'published'
        self.published_at = timezone.now()
        self.save()
        logger.info(f"Document published: {self.title} by {self.author.username}")
    
    def unpublish(self):
        """Unpublish the document."""
        self.status = 'draft'
        self.published_at = None
        self.save()
        logger.info(f"Document unpublished: {self.title} by {self.author.username}")
    
    def create_version(self, created_by, changelog=""):
        """
        Create a new version of this document.
        
        Args:
            created_by (User): User creating the version
            changelog (str): Description of changes in this version
            
        Returns:
            DocumentVersion: The new version object
        """
        version_number = self.versions.count() + 1
        version = DocumentVersion.objects.create(
            document=self,
            version_number=version_number,
            content=self.content,
            content_format=self.content_format,
            excerpt=self.excerpt,
            created_by=created_by,
            changelog=changelog
        )
        logger.info(f"Document version {version_number} created for {self.title} by {created_by.username}")
        return version


class DocumentVersion(models.Model):
    """
    Document version model for tracking document history.
    
    Attributes:
        document (ForeignKey): The document this version belongs to
        version_number (PositiveIntegerField): Sequential version number
        content (TextField): Version-specific content
        content_format (CharField): Format of the content (HTML or Markdown)
        excerpt (TextField): Version-specific excerpt
        created_at (DateTimeField): When this version was created
        created_by (ForeignKey): User who created this version
        changelog (TextField): Description of changes made in this version
    """
    document = models.ForeignKey(
        Document, 
        on_delete=models.CASCADE, 
        related_name='versions',
        verbose_name="Document"
    )
    version_number = models.PositiveIntegerField("Version Number")
    content = models.TextField("Content")
    excerpt = models.TextField("Excerpt", blank=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    content_format = models.CharField(
        "Content Format",
        max_length=10,
        choices=Document.CONTENT_FORMAT_CHOICES,
        default='markdown'
    )
    created_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='created_versions',
        verbose_name="Created by"
    )
    changelog = models.TextField("Change Description", blank=True)
    
    class Meta:
        verbose_name = "Document Version"
        verbose_name_plural = "Document Versions"
        ordering = ['-version_number']
        unique_together = ['document', 'version_number']
    
    def __str__(self):
        return f"{self.document.title} - v{self.version_number}"
        
    def promote_to_current(self):
        """
        Promote this version to be the current document content.
        
        Returns:
            Document: The updated document
        """
        with transaction.atomic():
            self.document.content = self.content
            self.document.content_format = self.content_format
            self.document.excerpt = self.excerpt
            self.document.updated_at = timezone.now()
            self.document.save(update_fields=['content', 'content_format', 'excerpt', 'updated_at'])
            logger.info(f"Version {self.version_number} promoted to current for document {self.document.id}")
        return self.document


class DocumentFile(models.Model):
    """
    Junction model to track files associated with documents.
    
    Attributes:
        document (ForeignKey): The document this file is associated with
        file (ForeignKey): The associated file
        order (PositiveIntegerField): Display order within the document
        added_at (DateTimeField): When the file was added to the document
        added_by (ForeignKey): User who added the file
    """
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name='document_files',
        verbose_name="Document"
    )
    file = models.ForeignKey(
        File,
        on_delete=models.CASCADE,
        related_name='used_in_documents',
        verbose_name="File"
    )
    order = models.PositiveIntegerField("Order", default=0)
    added_at = models.DateTimeField("Added at", auto_now_add=True)
    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='added_document_files',
        verbose_name="Added by"
    )
    
    class Meta:
        verbose_name = "Document File"
        verbose_name_plural = "Document Files"
        ordering = ['order', 'added_at']
        unique_together = ['document', 'file']
        
    def __str__(self):
        return f"{self.document.title} - {self.file.name}"
