"""
Role management routes for RBAC functionality
"""
from typing import List, Dict
from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.session import get_async_session
from app.models.user import User
from app.models.role import UserRole
from app.schemas.user import UserRead, UserWithRoles
from app.auth.users import current_admin, current_manager, current_active_user

# Create the roles router
router = APIRouter(prefix="/roles", tags=["roles"])

@router.get("/", response_model=List[str])
async def list_roles():
    """
    List all available roles
    
    Returns a list of all role names in the system.
    This endpoint is accessible to everyone.
    """
    return [role.value for role in UserRole]

@router.get("/{role}/users", response_model=List[UserRead])
async def list_users_by_role(
    role: UserRole,
    db: AsyncSession = Depends(get_async_session),
    _: User = Depends(current_admin)  # Admin only
):
    """
    List all users with a specific role
    
    This endpoint allows administrators to list all users with a specific role.
    Requires admin privileges.
    """
    result = await db.execute(
        select(User).filter(User.role == role)
    )
    users = result.scalars().all()
    return users

@router.get("/my-permissions", response_model=Dict[str, bool])
async def get_current_user_permissions(
    current_user: User = Depends(current_active_user)
):
    """
    Get the current user's role-based permissions
    
    This endpoint returns a dictionary of permission flags for the current user
    based on their role. This can be used by the frontend to show/hide UI elements.
    """
    is_admin = current_user.role == UserRole.ADMIN or current_user.is_superuser
    is_manager = current_user.role == UserRole.MANAGER or is_admin
    
    return {
        "can_view_all_users": is_admin,
        "can_create_users": is_manager,
        "can_update_users": is_manager,
        "can_delete_users": is_admin,
        "can_assign_roles": is_admin,
        "can_view_roles": True,
        "can_manage_content": is_manager
    }

@router.put("/assign/{user_id}", response_model=UserWithRoles)
async def assign_role_to_user(
    user_id: int, 
    role: UserRole = Body(...),
    db: AsyncSession = Depends(get_async_session),
    _: User = Depends(current_admin)  # Admin only
):
    """
    Assign a role to a user
    
    This endpoint allows administrators to assign a new role to a user.
    Requires admin privileges.
    """
    # Find the user
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Update the role
    user.role = role
    await db.commit()
    await db.refresh(user)
    
    return user
