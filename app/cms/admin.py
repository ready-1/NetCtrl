"""
Admin interface configuration for the CMS app.

This module registers models from the CMS app with Django's admin site
and customizes their appearance and functionality in the admin interface.
"""

from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.text import Truncator

from cms.models import (
    UserProfile, Category, Tag, Document, DocumentVersion, DocumentFile,
    FileCategory, FileTag, File, FileChunkedUpload
)

import logging

logger = logging.getLogger(__name__)


class UserProfileAdmin(admin.ModelAdmin):
    """Admin interface for UserProfile model."""
    list_display = ('user', 'get_email', 'get_date_joined', 'dark_mode')
    search_fields = ('user__username', 'user__email', 'bio')
    readonly_fields = ('get_date_joined', 'get_last_login')
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'get_email', 'get_date_joined', 'get_last_login')
        }),
        ('Profile', {
            'fields': ('profile_picture', 'bio', 'dark_mode')
        }),
    )

    def get_email(self, obj):
        """Get user's email address."""
        return obj.user.email
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'

    def get_date_joined(self, obj):
        """Get user's join date."""
        return obj.date_joined
    get_date_joined.short_description = 'Date Joined'
    get_date_joined.admin_order_field = 'user__date_joined'

    def get_last_login(self, obj):
        """Get user's last login date."""
        return obj.last_login
    get_last_login.short_description = 'Last Login'
    get_last_login.admin_order_field = 'user__last_login'


class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for Category model."""
    list_display = ('name', 'slug', 'parent', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'parent', 'description')
        }),
    )


class TagAdmin(admin.ModelAdmin):
    """Admin interface for Tag model."""
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class DocumentAdmin(admin.ModelAdmin):
    """Admin interface for Document model."""
    list_display = ('title', 'slug', 'author', 'category', 'status', 'created_at', 'published_at')
    list_filter = ('status', 'created_at', 'published_at', 'category', 'tags')
    search_fields = ('title', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    filter_horizontal = ('tags',)
    readonly_fields = ('created_at', 'updated_at', 'uuid')
    actions = ['publish_documents', 'unpublish_documents']
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'category', 'tags')
        }),
        ('Content', {
            'fields': ('content', 'excerpt', 'featured_image')
        }),
        ('Publishing', {
            'fields': ('status', 'published_at')
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at', 'uuid')
        }),
    )

    def publish_documents(self, request, queryset):
        """Publish selected documents."""
        count = 0
        for document in queryset:
            if document.status != 'published':
                document.publish()
                count += 1
        if count == 1:
            message = '1 document was'
        else:
            message = f'{count} documents were'
        self.message_user(request, f'{message} successfully published.')
        logger.info(f"Admin user {request.user.username} published {count} documents")
    publish_documents.short_description = 'Publish selected documents'

    def unpublish_documents(self, request, queryset):
        """Unpublish selected documents."""
        count = 0
        for document in queryset:
            if document.status != 'draft':
                document.unpublish()
                count += 1
        if count == 1:
            message = '1 document was'
        else:
            message = f'{count} documents were'
        self.message_user(request, f'{message} successfully unpublished.')
        logger.info(f"Admin user {request.user.username} unpublished {count} documents")
    unpublish_documents.short_description = 'Unpublish selected documents'


class FileCategoryAdmin(admin.ModelAdmin):
    """Admin interface for FileCategory model."""
    list_display = ('name', 'slug')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


class FileTagAdmin(admin.ModelAdmin):
    """Admin interface for FileTag model."""
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class FileAdmin(admin.ModelAdmin):
    """Admin interface for File model."""
    list_display = ('name', 'original_filename', 'file_size_display', 'mime_type', 'uploaded_by', 'uploaded_at', 'download_count')
    list_filter = ('uploaded_at', 'mime_type', 'category', 'tags')
    search_fields = ('name', 'description', 'original_filename', 'uploaded_by__username')
    filter_horizontal = ('tags',)
    readonly_fields = ('file_size_display', 'mime_type', 'original_filename', 'download_count', 'last_accessed', 'uuid')
    fieldsets = (
        (None, {
            'fields': ('name', 'file', 'description')
        }),
        ('Organization', {
            'fields': ('category', 'tags')
        }),
        ('Upload Details', {
            'fields': ('uploaded_by', 'uploaded_at', 'original_filename', 'mime_type', 'file_size_display')
        }),
        ('Statistics', {
            'fields': ('download_count', 'last_accessed')
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('uuid',)
        }),
    )

    def file_size_display(self, obj):
        """Format file size for display."""
        bytes_value = obj.file_size
        if bytes_value < 1024:
            return f"{bytes_value} bytes"
        elif bytes_value < 1024 ** 2:
            return f"{bytes_value / 1024:.1f} KB"
        elif bytes_value < 1024 ** 3:
            return f"{bytes_value / (1024 ** 2):.1f} MB"
        else:
            return f"{bytes_value / (1024 ** 3):.2f} GB"
    file_size_display.short_description = 'File Size'


class FileChunkedUploadAdmin(admin.ModelAdmin):
    """Admin interface for FileChunkedUpload model."""
    list_display = ('filename', 'upload_id', 'status', 'created_on', 'completed_on', 'user')
    list_filter = ('status', 'created_on')
    search_fields = ('filename', 'upload_id', 'user__username')
    readonly_fields = ('upload_id', 'created_on', 'completed_on', 'offset')
    fieldsets = (
        (None, {
            'fields': ('filename', 'upload_id', 'user', 'file')
        }),
        ('Upload Details', {
            'fields': ('offset', 'created_on', 'completed_on', 'status')
        }),
        ('File Details', {
            'fields': ('category_id', 'description', 'tags')
        }),
    )


class DocumentVersionAdmin(admin.ModelAdmin):
    """Admin interface for DocumentVersion model."""
    list_display = ('document', 'version_number', 'created_by', 'created_at')
    list_filter = ('created_at', 'created_by')
    search_fields = ('document__title', 'changelog', 'content')
    readonly_fields = ('document', 'version_number', 'created_at', 'created_by')
    fieldsets = (
        (None, {
            'fields': ('document', 'version_number', 'created_by', 'created_at')
        }),
        ('Content', {
            'fields': ('content', 'excerpt')
        }),
        ('Changes', {
            'fields': ('changelog',)
        }),
    )
    
    def has_add_permission(self, request):
        """Disable manual addition of versions."""
        return False
    
    actions = ['promote_to_current']
    
    def promote_to_current(self, request, queryset):
        """Promote selected version to be current document content."""
        if queryset.count() > 1:
            self.message_user(request, 'Please select only one version to promote.', level='error')
            return
            
        version = queryset.first()
        if version:
            version.promote_to_current()
            self.message_user(request, f'Version {version.version_number} promoted to current for document "{version.document.title}".')
            logger.info(f"Admin user {request.user.username} promoted version {version.version_number} for document {version.document.id}")
    promote_to_current.short_description = 'Promote selected version to current'


class DocumentFileAdmin(admin.ModelAdmin):
    """Admin interface for DocumentFile model."""
    list_display = ('document', 'file', 'order', 'added_by', 'added_at')
    list_filter = ('added_at', 'added_by', 'document')
    search_fields = ('document__title', 'file__name')
    readonly_fields = ('added_at',)
    fieldsets = (
        (None, {
            'fields': ('document', 'file', 'order')
        }),
        ('Details', {
            'fields': ('added_by', 'added_at')
        }),
    )
    
    def get_file_link(self, obj):
        """Get link to file detail page."""
        url = reverse('admin:cms_file_change', args=[obj.file.id])
        return format_html('<a href="{}">{}</a>', url, obj.file.name)
    get_file_link.short_description = 'File'
    get_file_link.admin_order_field = 'file__name'
    
    def get_document_link(self, obj):
        """Get link to document detail page."""
        url = reverse('admin:cms_document_change', args=[obj.document.id])
        return format_html('<a href="{}">{}</a>', url, obj.document.title)
    get_document_link.short_description = 'Document'
    get_document_link.admin_order_field = 'document__title'


# Register models with admin site
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentVersion, DocumentVersionAdmin)
admin.site.register(DocumentFile, DocumentFileAdmin)
admin.site.register(FileCategory, FileCategoryAdmin)
admin.site.register(FileTag, FileTagAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(FileChunkedUpload, FileChunkedUploadAdmin)
