"""Content management service layer"""
from typing import Optional, List, Dict, Any, Tuple
from datetime import datetime
from sqlalchemy import select, or_, and_, desc, update, delete
from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, status

from app.models.content import Content, ContentType, ContentStatus, ContentFile, ContentPermission
from app.models.role import UserRole
from app.schemas.content import (
    ContentCreate, ContentUpdate, ContentPermissionCreate, 
    ContentPermissionUpdate, PermissionSettings
)

class ContentService:
    """Service for managing content items"""

    @staticmethod
    async def create_content(
        db: Session, 
        content_data: ContentCreate, 
        user_id: int
    ) -> Content:
        """Create a new content item"""
        content = Content(
            **content_data.model_dump(),
            created_by=user_id,
            updated_by=user_id,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.add(content)
        await db.commit()
        await db.refresh(content)
        
        # Add default permissions for the creator (admin)
        admin_permission = ContentPermission(
            content_id=content.id,
            role=UserRole.ADMIN,
            can_view=True,
            can_edit=True,
            can_delete=True
        )
        db.add(admin_permission)
        
        # Add default permissions for the creator's role
        # If creator is not admin, also add their role permissions
        if user_id != 1:  # Assuming 1 is admin user ID
            user_role_permission = ContentPermission(
                content_id=content.id,
                role=UserRole.USER,  # Default to user role
                can_view=True,
                can_edit=True,
                can_delete=False
            )
            db.add(user_role_permission)
        
        await db.commit()
        return content

    @staticmethod
    async def get_content_by_id(
        db: Session, 
        content_id: int,
        user_id: int,
        user_role: UserRole
    ) -> Optional[Content]:
        """Get a content item by ID"""
        # Check if user has permission first
        can_view = await ContentService.check_permission(
            db, content_id, user_id, user_role, "view"
        )
        
        if not can_view:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to view this content"
            )
        
        # Get content with joined data
        query = (
            select(Content)
            .options(
                joinedload(Content.files),
                joinedload(Content.permissions)
            )
            .where(Content.id == content_id)
        )
        
        result = await db.execute(query)
        content = result.unique().scalar_one_or_none()
        
        if content is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Content with id {content_id} not found"
            )
            
        return content

    @staticmethod
    async def list_content(
        db: Session,
        user_id: int,
        user_role: UserRole,
        skip: int = 0,
        limit: int = 100,
        status_filter: Optional[ContentStatus] = None,
        content_type_filter: Optional[ContentType] = None,
        search: Optional[str] = None
    ) -> Tuple[List[Content], int]:
        """List content items with filtering and pagination"""
        # Base query
        query = select(Content)
        count_query = select(Content)
        
        # Apply filters
        filters = []
        
        # Apply status filter
        if status_filter:
            filters.append(Content.status == status_filter)
            
        # Apply content type filter
        if content_type_filter:
            filters.append(Content.content_type == content_type_filter)
            
        # Apply search filter
        if search:
            search_filter = or_(
                Content.title.ilike(f"%{search}%"),
                Content.description.ilike(f"%{search}%"),
                Content.body.ilike(f"%{search}%")
            )
            filters.append(search_filter)
            
        # If not admin, filter for content the user has permission to view
        if user_role != UserRole.ADMIN:
            # Get content IDs where user has view permission
            permission_query = (
                select(ContentPermission.content_id)
                .where(
                    and_(
                        ContentPermission.role == user_role,
                        ContentPermission.can_view == True
                    )
                )
            )
            permission_result = await db.execute(permission_query)
            viewable_content_ids = [r[0] for r in permission_result]
            
            # Include content created by user
            filters.append(
                or_(
                    Content.id.in_(viewable_content_ids),
                    Content.created_by == user_id
                )
            )
            
        # Apply all filters
        if filters:
            query = query.where(and_(*filters))
            count_query = count_query.where(and_(*filters))
            
        # Get total count
        count_result = await db.execute(count_query)
        total_count = len(count_result.all())
        
        # Apply pagination and get results
        query = query.order_by(desc(Content.updated_at)).offset(skip).limit(limit)
        result = await db.execute(query)
        content_items = result.scalars().all()
        
        return content_items, total_count

    @staticmethod
    async def update_content(
        db: Session,
        content_id: int,
        content_data: ContentUpdate,
        user_id: int,
        user_role: UserRole
    ) -> Content:
        """Update a content item"""
        # Check if user has permission
        can_edit = await ContentService.check_permission(
            db, content_id, user_id, user_role, "edit"
        )
        
        if not can_edit:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to edit this content"
            )
        
        # Get existing content
        query = select(Content).where(Content.id == content_id)
        result = await db.execute(query)
        content = result.scalar_one_or_none()
        
        if content is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Content with id {content_id} not found"
            )
        
        # Update content fields
        content_data_dict = content_data.model_dump(exclude_unset=True)
        for field, value in content_data_dict.items():
            setattr(content, field, value)
            
        # Update updated_by and updated_at
        content.updated_by = user_id
        content.updated_at = datetime.now()
        
        await db.commit()
        await db.refresh(content)
        return content

    @staticmethod
    async def delete_content(
        db: Session,
        content_id: int,
        user_id: int,
        user_role: UserRole
    ) -> bool:
        """Delete a content item"""
        # Check if user has permission
        can_delete = await ContentService.check_permission(
            db, content_id, user_id, user_role, "delete"
        )
        
        if not can_delete:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to delete this content"
            )
        
        # Get existing content
        query = select(Content).where(Content.id == content_id)
        result = await db.execute(query)
        content = result.scalar_one_or_none()
        
        if content is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Content with id {content_id} not found"
            )
        
        # Delete content
        delete_stmt = delete(Content).where(Content.id == content_id)
        await db.execute(delete_stmt)
        await db.commit()
        
        return True

    @staticmethod
    async def check_permission(
        db: Session,
        content_id: int,
        user_id: int,
        user_role: UserRole,
        permission_type: str
    ) -> bool:
        """Check if user has permission for an action on content"""
        # Admins always have permission
        if user_role == UserRole.ADMIN:
            return True
            
        # Check if user is the content creator
        query = select(Content).where(
            and_(
                Content.id == content_id,
                Content.created_by == user_id
            )
        )
        result = await db.execute(query)
        content = result.scalar_one_or_none()
        
        # Content creators have view and edit permissions
        if content and permission_type in ["view", "edit"]:
            return True
            
        # Check role-based permission
        permission_field = f"can_{permission_type}"
        permission_query = select(ContentPermission).where(
            and_(
                ContentPermission.content_id == content_id,
                ContentPermission.role == user_role,
                getattr(ContentPermission, permission_field) == True
            )
        )
        permission_result = await db.execute(permission_query)
        permission = permission_result.scalar_one_or_none()
        
        return permission is not None

    @staticmethod
    async def set_permissions(
        db: Session,
        content_id: int,
        permissions: Dict[UserRole, PermissionSettings],
        user_id: int,
        user_role: UserRole
    ) -> List[ContentPermission]:
        """Set permissions for a content item"""
        # Check if user has permission to change permissions
        # Only admins and content creators can change permissions
        if user_role != UserRole.ADMIN:
            query = select(Content).where(
                and_(
                    Content.id == content_id,
                    Content.created_by == user_id
                )
            )
            result = await db.execute(query)
            content = result.scalar_one_or_none()
            
            if not content:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Only admins and content creators can set permissions"
                )
        
        # Get existing content
        query = select(Content).where(Content.id == content_id)
        result = await db.execute(query)
        content = result.scalar_one_or_none()
        
        if content is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Content with id {content_id} not found"
            )
        
        # Delete existing permissions
        delete_stmt = delete(ContentPermission).where(ContentPermission.content_id == content_id)
        await db.execute(delete_stmt)
        
        # Create new permissions
        new_permissions = []
        for role, settings in permissions.items():
            permission = ContentPermission(
                content_id=content_id,
                role=role,
                can_view=settings.can_view,
                can_edit=settings.can_edit,
                can_delete=settings.can_delete
            )
            db.add(permission)
            new_permissions.append(permission)
        
        await db.commit()
        
        return new_permissions
