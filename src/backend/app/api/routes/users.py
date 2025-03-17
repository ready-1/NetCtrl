"""
Extended user management routes beyond the basic FastAPI-Users functionality
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query, Body, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.session import get_async_session
from app.models.user import User
from app.models.role import UserRole
from app.schemas.user import UserRead, UserCreate, UserUpdate, UserWithRoles
from app.auth.users import (
    current_active_user,
    current_admin,
    current_manager,
    fastapi_users,
    get_user_manager,
    UserManager
)

# Create the users router
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserRead])
async def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    role: Optional[UserRole] = None,
    db: AsyncSession = Depends(get_async_session),
    _: User = Depends(current_admin)  # Admin only
):
    """
    List all users with optional filtering by role
    
    This endpoint allows administrators to list all users in the system,
    optionally filtered by role. Supports pagination.
    Requires admin privileges.
    """
    query = select(User)
    if role is not None:
        query = query.filter(User.role == role)
    
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    users = result.scalars().all()
    
    return users

@router.get("/me", response_model=UserWithRoles)
async def get_current_user(
    user: User = Depends(current_active_user)
):
    """
    Get the current authenticated user's details
    
    This endpoint returns details about the currently authenticated user,
    including their role information. Requires authentication.
    """
    return user

@router.get("/{user_id}", response_model=UserWithRoles)
async def get_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(current_active_user)
):
    """
    Get a specific user by ID
    
    This endpoint returns details about a specific user. Regular users can only
    access their own information. Managers and admins can access any user.
    """
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Regular users can only access their own information
    if (current_user.role == UserRole.USER and current_user.id != user_id) and \
       not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    return user

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    current_user: User = Depends(current_active_user),
    user_manager: UserManager = Depends(get_user_manager)
):
    """
    Create a new user
    
    This endpoint allows administrators and managers to create new users.
    Managers cannot create admin users. Regular users cannot create users.
    """
    # Check if current user has permission to create users
    if current_user.role == UserRole.USER and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions to create users"
        )
    
    # Check if current user has permission to create users with specified role
    if user_data.role == UserRole.ADMIN and current_user.role != UserRole.ADMIN and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions to create admin users"
        )
    
    # Convert to dict for user creation
    user_dict = user_data.dict()
    
    try:
        created_user = await user_manager.create(user_dict)
        return created_user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error creating user: {str(e)}"
        )

@router.put("/{user_id}", response_model=UserWithRoles)
async def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(current_active_user),
    user_manager: UserManager = Depends(get_user_manager)
):
    """
    Update a user
    
    This endpoint allows users to update their own information, and allows
    administrators and managers to update other users. Managers cannot update
    admin users or change user roles to admin.
    """
    # Get the user to update
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Check permissions for updating user
    is_self = current_user.id == user_id
    is_admin = current_user.role == UserRole.ADMIN or current_user.is_superuser
    is_manager = current_user.role == UserRole.MANAGER or is_admin
    
    if not (is_self or is_admin or is_manager):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions to update this user"
        )
    
    # Additional role-based restrictions
    if user_data.role is not None:
        # Only admins can change roles
        if not is_admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only administrators can change user roles"
            )
        
        # Prevent downgrading own admin role
        if is_self and current_user.role == UserRole.ADMIN and user_data.role != UserRole.ADMIN:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Administrators cannot downgrade their own role"
            )
    
    # Get only the fields that were actually provided
    update_data = user_data.dict(exclude_unset=True)
    
    # If no fields to update, return the current user
    if not update_data:
        return user
    
    # Update the user
    try:
        updated_user = await user_manager.update(update_data, user)
        return updated_user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error updating user: {str(e)}"
        )

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(current_active_user)
):
    """
    Delete a user
    
    This endpoint allows administrators to delete users, or users to delete
    their own accounts. Requires appropriate permissions.
    """
    # Check if the user exists
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Check permissions - admins can delete any user, users can only delete themselves
    if current_user.id != user_id and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    # Delete the user
    await db.delete(user)
    await db.commit()
    
    return None
