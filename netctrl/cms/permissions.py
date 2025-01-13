from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from rest_framework import permissions

class CMSBasePermission(permissions.BasePermission):
    """
    Base permission class for CMS operations.
    Implements core permission checking logic.
    """
    
    def has_permission(self, request, view):
        """
        Global permission check for CMS access.
        Verifies user authentication and basic CMS access rights.
        """
        if not request.user.is_authenticated:
            return False
            
        # Check if user has any CMS permissions
        return request.user.has_perm('cms.view_file') or \
               request.user.has_perm('cms.view_category')

class FileTypePermission(CMSBasePermission):
    """
    Permission class for file type specific operations.
    Controls access based on file type (firmware, documentation, config).
    """
    
    def has_object_permission(self, request, view, obj):
        """
        Object-level permission check based on file type.
        
        Args:
            request: The request being made
            view: The view handling the request
            obj: The file object being accessed
            
        Returns:
            bool: Whether the user has permission
        """
        # Admin always has access
        if request.user.is_superuser:
            return True
            
        # Get required permission based on method
        if request.method in permissions.SAFE_METHODS:
            required_perm = f'cms.view_{obj.type.lower()}'
        elif request.method == 'DELETE':
            required_perm = f'cms.delete_{obj.type.lower()}'
        else:
            required_perm = f'cms.change_{obj.type.lower()}'
            
        return request.user.has_perm(required_perm)

class CategoryPermission(CMSBasePermission):
    """
    Permission class for category operations.
    Implements hierarchical permission checking.
    """
    
    def has_object_permission(self, request, view, obj):
        """
        Object-level permission check for categories.
        Considers category hierarchy in permission checks.
        """
        # Admin always has access
        if request.user.is_superuser:
            return True
            
        # Get required permission based on method
        if request.method in permissions.SAFE_METHODS:
            required_perm = 'cms.view_category'
        elif request.method == 'DELETE':
            required_perm = 'cms.delete_category'
        else:
            required_perm = 'cms.change_category'
            
        # Check basic permission
        if not request.user.has_perm(required_perm):
            return False
            
        # For hierarchical categories, check parent permissions
        current = obj
        while current.parent:
            if not self.has_parent_permission(request.user, current.parent):
                return False
            current = current.parent
            
        return True
        
    def has_parent_permission(self, user, category):
        """Check if user has permission for parent category."""
        return user.has_perm('cms.view_category')

class MetadataPermission(CMSBasePermission):
    """
    Permission class for metadata operations.
    Controls access to file metadata.
    """
    
    def has_object_permission(self, request, view, obj):
        """
        Object-level permission check for metadata.
        Links metadata permissions to file permissions.
        """
        # Admin always has access
        if request.user.is_superuser:
            return True
            
        # Metadata access requires file access
        file_perm = FileTypePermission()
        return file_perm.has_object_permission(request, view, obj.file)

def setup_cms_permissions():
    """
    Initialize CMS permission structure.
    Creates necessary permissions and groups.
    
    This should be run during initial setup or migrations.
    """
    # Create basic CMS groups
    groups = {
        'CMS_Admin': ['*'],
        'CMS_Editor': ['add', 'change', 'view'],
        'CMS_Viewer': ['view'],
    }
    
    # Get content types
    file_ct = ContentType.objects.get(app_label='cms', model='file')
    category_ct = ContentType.objects.get(app_label='cms', model='category')
    metadata_ct = ContentType.objects.get(app_label='cms', model='metadata')
    
    # Create permissions for each group
    for group_name, actions in groups.items():
        group, _ = Group.objects.get_or_create(name=group_name)
        
        # Skip permission assignment for existing groups
        if group.permissions.exists():
            continue
            
        # Determine permissions based on actions
        if '*' in actions:
            permissions = Permission.objects.filter(
                Q(content_type=file_ct) |
                Q(content_type=category_ct) |
                Q(content_type=metadata_ct)
            )
        else:
            permissions = Permission.objects.filter(
                content_type__in=[file_ct, category_ct, metadata_ct],
                codename__regex=r'^(' + '|'.join(actions) + ')_'
            )
        
        # Assign permissions to group
        group.permissions.add(*permissions)
