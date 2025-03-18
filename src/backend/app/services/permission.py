"""
Permission service for content-related operations with role-based access control
"""
from typing import Dict, Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from fastapi import HTTPException, status

from app.models.content import Content, ContentPermission
from app.models.user import User
from app.models.role import UserRole
from app.schemas.content import PermissionSettings, ContentPermissionsUpdate

# Default permission templates for different content visibility levels
DEFAULT_PERMISSION_TEMPLATES = {
    # Public content viewable by anyone
    "public": {
        UserRole.ADMIN: {"can_view": True, "can_edit": True, "can_delete": True},
        UserRole.MANAGER: {"can_view": True, "can_edit": True, "can_delete": False},
        UserRole.USER: {"can_view": True, "can_edit": False, "can_delete": False},
    },
    # Internal content for staff only
    "internal": {
        UserRole.ADMIN: {"can_view": True, "can_edit": True, "can_delete": True},
        UserRole.MANAGER: {"can_view": True, "can_edit": True, "can_delete": False},
        UserRole.USER: {"can_view": False, "can_edit": False, "can_delete": False},
    },
    # Private content for admins only
    "private": {
        UserRole.ADMIN: {"can_view": True, "can_edit": True, "can_delete": True},
        UserRole.MANAGER: {"can_view": False, "can_edit": False, "can_delete": False},
        UserRole.USER: {"can_view": False, "can_edit": False, "can_delete": False},
    },
}

class PermissionService:
    """Service for managing content permissions"""
    
    @staticmethod
    async def get_content_permissions(content_id: int, db: AsyncSession) -> List[ContentPermission]:
        """Get all permissions for a content item"""
        result = await db.execute(
            select(ContentPermission).where(ContentPermission.content_id == content_id)
        )
        return result.scalars().all()
    
    @staticmethod
    async def get_available_templates() -> Dict[str, Dict]:
        """Get available permission templates"""
        return DEFAULT_PERMISSION_TEMPLATES
    
    @staticmethod
    async def apply_permission_template(
        content_id: int, 
        template_name: str, 
        db: AsyncSession
    ) -> List[ContentPermission]:
        """Apply a predefined permission template to content"""
        if template_name not in DEFAULT_PERMISSION_TEMPLATES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unknown permission template: {template_name}"
            )
        
        # Delete existing permissions
        await db.execute(
            delete(ContentPermission).where(ContentPermission.content_id == content_id)
        )
        
        # Create new permissions based on template
        template = DEFAULT_PERMISSION_TEMPLATES[template_name]
        permissions = []
        
        for role, settings in template.items():
            permission = ContentPermission(
                content_id=content_id,
                role=role,
                can_view=settings.get("can_view", False),
                can_edit=settings.get("can_edit", False),
                can_delete=settings.get("can_delete", False)
            )
            db.add(permission)
            permissions.append(permission)
        
        await db.commit()
        
        # Refresh permissions to get their IDs
        for permission in permissions:
            await db.refresh(permission)
        
        return permissions
    
    @staticmethod
    async def update_permissions(
        content_id: int,
        permissions_update: ContentPermissionsUpdate,
        db: AsyncSession
    ) -> List[ContentPermission]:
        """Update permissions for content"""
        # Get existing permissions
        result = await db.execute(
            select(ContentPermission).where(ContentPermission.content_id == content_id)
        )
        existing_permissions = {p.role: p for p in result.scalars().all()}
        
        updated_permissions = []
        
        # Update permissions for each role
        for role, settings in permissions_update.permissions.items():
            if role in existing_permissions:
                # Update existing permission
                permission = existing_permissions[role]
                permission.can_view = settings.can_view
                permission.can_edit = settings.can_edit
                permission.can_delete = settings.can_delete
                updated_permissions.append(permission)
            else:
                # Create new permission
                permission = ContentPermission(
                    content_id=content_id,
                    role=role,
                    can_view=settings.can_view,
                    can_edit=settings.can_edit,
                    can_delete=settings.can_delete
                )
                db.add(permission)
                updated_permissions.append(permission)
        
        await db.commit()
        
        # Refresh permissions to get their updated state
        for permission in updated_permissions:
            await db.refresh(permission)
        
        return updated_permissions
    
    @staticmethod
    async def check_user_permission(
        user: User,
        content_id: int,
        permission_type: str,
        db: AsyncSession
    ) -> bool:
        """Check if a user has a specific permission for content"""
        # Superusers always have permission
        if user.is_superuser:
            return True
        
        # Get the content to check if user is the creator
        content_result = await db.execute(
            select(Content).where(Content.id == content_id)
        )
        content = content_result.scalar_one_or_none()
        
        if not content:
            return False
        
        # Creators always have view access to their own content
        if content.created_by == user.id and permission_type == "view":
            return True
        
        # Check if user has permission based on their role
        result = await db.execute(
            select(ContentPermission).where(
                ContentPermission.content_id == content_id,
                ContentPermission.role == user.role
            )
        )
        permission = result.scalar_one_or_none()
        
        if not permission:
            return False
        
        if permission_type == "view":
            return permission.can_view
        elif permission_type == "edit":
            return permission.can_edit
        elif permission_type == "delete":
            return permission.can_delete
        
        return False
