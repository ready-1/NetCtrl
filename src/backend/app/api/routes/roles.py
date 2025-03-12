"""
Role management routes for RBAC functionality
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.session import get_async_session
from app.models.user import User
from app.models.role import UserRole
from app.schemas.user import UserRead
from app.auth.users import current_admin

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
