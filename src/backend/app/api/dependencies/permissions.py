"""
Permission check dependencies for API routes
"""
from typing import Optional
from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.session import get_async_session
from app.models.user import User
from app.models.content import Content
from app.auth.users import current_active_user, current_admin, current_manager
from app.services.permission import PermissionService

async def get_content_or_404(
    content_id: int = Path(..., description="The ID of the content item"),
    db: AsyncSession = Depends(get_async_session)
):
    """Get content by ID or raise 404"""
    result = await db.execute(
        select(Content).where(Content.id == content_id)
    )
    content = result.scalar_one_or_none()
    
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Content not found"
        )
    
    return content

def require_content_permission(permission_type: str):
    """
    Dependency for checking content permissions
    
    Usage:
    ```
    @router.get("/{content_id}")
    async def get_content(
        content_id: int,
        current_user: User = Depends(require_content_permission("view"))
    ):
        # Implementation
    ```
    """
    async def dependency(
        content_id: int = Path(..., description="The ID of the content item"),
        current_user: User = Depends(current_active_user),
        db: AsyncSession = Depends(get_async_session),
    ):
        # Superusers always have permission
        if current_user.is_superuser:
            return current_user
            
        # Get the content
        content = await get_content_or_404(content_id, db)
            
        # Check if user is the creator (special case)
        if content.created_by == current_user.id:
            # Creators always have view access
            if permission_type == "view":
                return current_user
        
        # Check role-based permissions
        has_permission = await PermissionService.check_user_permission(
            user=current_user,
            content_id=content_id,
            permission_type=permission_type,
            db=db
        )
        
        if not has_permission:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Not enough permissions to {permission_type} this content"
            )
            
        return current_user
    
    return dependency

# Specific permission dependencies
require_view_permission = require_content_permission("view")
require_edit_permission = require_content_permission("edit")
require_delete_permission = require_content_permission("delete")

# Common role-based dependencies from the auth system
# These are used for operations that don't involve specific content items
current_content_creator = current_active_user  # Any active user can create content
current_content_admin = current_admin  # Admins can manage all content
current_content_manager = current_manager  # Managers have elevated privileges
