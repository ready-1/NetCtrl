"""API routes for content management"""
from typing import Optional, Dict, Any, List
from fastapi import APIRouter, Depends, HTTPException, Query, Path, Body
from fastapi import status
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.db.session import get_async_session as get_db
from app.auth.users import current_active_user, current_active_user_with_role
from app.models.role import UserRole
from app.models.content import Content, ContentType, ContentStatus, ContentPermission
from app.models.user import User
from app.services.content import ContentService
from app.schemas.content import (
    ContentCreate, ContentRead, ContentDetailRead, ContentUpdate,
    ContentListResponse, ContentPermissionsUpdate, PermissionSettings
)

router = APIRouter(prefix="/content", tags=["content"])

@router.post("/", response_model=ContentRead, status_code=status.HTTP_201_CREATED)
async def create_content(
    content_data: ContentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(current_active_user)
):
    """
    Create a new content item.
    
    Requires an authenticated user.
    """
    content = await ContentService.create_content(
        db=db,
        content_data=content_data,
        user_id=current_user.id
    )
    return content

@router.get("/{content_id}", response_model=ContentDetailRead)
async def get_content(
    content_id: int = Path(..., title="The ID of the content to get"),
    db: Session = Depends(get_db),
    current_user: User = Depends(current_active_user_with_role)
):
    """
    Get a specific content item by ID.
    
    Requires an authenticated user with appropriate view permissions.
    """
    content = await ContentService.get_content_by_id(
        db=db,
        content_id=content_id,
        user_id=current_user.id,
        user_role=current_user.role
    )
    return content

@router.get("/", response_model=ContentListResponse)
async def list_content(
    skip: int = Query(0, title="Skip items", ge=0),
    limit: int = Query(100, title="Limit items", ge=1, le=100),
    status_filter: Optional[ContentStatus] = Query(None, title="Filter by status"),
    content_type_filter: Optional[ContentType] = Query(None, title="Filter by content type"),
    search: Optional[str] = Query(None, title="Search in title, description, and body"),
    db: Session = Depends(get_db),
    current_user: User = Depends(current_active_user_with_role)
):
    """
    List content items with filtering and pagination.
    
    Requires an authenticated user. Results are filtered by user's permissions.
    """
    content_items, total_count = await ContentService.list_content(
        db=db,
        user_id=current_user.id,
        user_role=current_user.role,
        skip=skip,
        limit=limit,
        status_filter=status_filter,
        content_type_filter=content_type_filter,
        search=search
    )
    
    return {
        "items": content_items,
        "total": total_count,
        "page": skip // limit + 1,
        "size": limit,
        "pages": (total_count + limit - 1) // limit
    }

@router.put("/{content_id}", response_model=ContentRead)
async def update_content(
    content_data: ContentUpdate,
    content_id: int = Path(..., title="The ID of the content to update"),
    db: Session = Depends(get_db),
    current_user: User = Depends(current_active_user_with_role)
):
    """
    Update a content item.
    
    Requires an authenticated user with appropriate edit permissions.
    """
    content = await ContentService.update_content(
        db=db,
        content_id=content_id,
        content_data=content_data,
        user_id=current_user.id,
        user_role=current_user.role
    )
    return content

@router.delete("/{content_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_content(
    content_id: int = Path(..., title="The ID of the content to delete"),
    db: Session = Depends(get_db),
    current_user: User = Depends(current_active_user_with_role)
):
    """
    Delete a content item.
    
    Requires an authenticated user with appropriate delete permissions.
    """
    await ContentService.delete_content(
        db=db,
        content_id=content_id,
        user_id=current_user.id,
        user_role=current_user.role
    )
    return None

@router.post("/{content_id}/permissions", response_model=Dict[str, bool])
async def set_content_permissions(
    permissions_data: ContentPermissionsUpdate,
    content_id: int = Path(..., title="The ID of the content to set permissions for"),
    db: Session = Depends(get_db),
    current_user: User = Depends(current_active_user_with_role)
):
    """
    Set permissions for a content item.
    
    Requires an authenticated user with admin role or content creator.
    """
    await ContentService.set_permissions(
        db=db,
        content_id=content_id,
        permissions=permissions_data.permissions,
        user_id=current_user.id,
        user_role=current_user.role
    )
    return {"success": True}

@router.get("/{content_id}/permissions", response_model=Dict[str, PermissionSettings])
async def get_content_permissions(
    content_id: int = Path(..., title="The ID of the content to get permissions for"),
    db: Session = Depends(get_db),
    current_user: User = Depends(current_active_user_with_role)
):
    """
    Get permissions for a content item.
    
    Requires an authenticated user with view permissions for the content.
    """
    # First check if user can view the content
    can_view = await ContentService.check_permission(
        db=db,
        content_id=content_id,
        user_id=current_user.id,
        user_role=current_user.role,
        permission_type="view"
    )
    
    if not can_view:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to view this content's permissions"
        )
    
    # Get content with permissions
    query = (
        select(Content)
        .options(joinedload(Content.permissions))
        .where(Content.id == content_id)
    )
    
    result = await db.execute(query)
    content = result.scalar_one_or_none()
    
    if content is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Content with id {content_id} not found"
        )
    
    # Convert permissions to dictionary
    permissions_dict = {}
    for permission in content.permissions:
        permissions_dict[permission.role.value] = PermissionSettings(
            can_view=permission.can_view,
            can_edit=permission.can_edit,
            can_delete=permission.can_delete
        )
    
    return permissions_dict
