"""
Pydantic schemas for user data validation and serialization
"""
from typing import Optional
from datetime import datetime
from pydantic import Field, validator, EmailStr
from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate

from app.models.role import UserRole

class UserRead(BaseUser[int]):
    """
    Schema for reading user data
    """
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: UserRole
    
    class Config:
        """
        Pydantic configuration for ORM mode
        """
        from_attributes = True

class UserCreate(BaseUserCreate):
    """
    Schema for creating a new user
    """
    username: str = Field(..., min_length=3, max_length=50)
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    email: Optional[EmailStr] = None  # Make email optional
    role: UserRole = UserRole.USER
    
    @validator('username')
    def username_alphanumeric(cls, v):
        """
        Validate username contains only alphanumeric characters
        """
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v

class UserUpdate(BaseUserUpdate):
    """
    Schema for updating user data
    """
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    email: Optional[EmailStr] = None
    role: Optional[UserRole] = None
    
    @validator('username')
    def username_alphanumeric(cls, v):
        """
        Validate username contains only alphanumeric characters
        """
        if v is not None and not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v

class UserWithRoles(UserRead):
    """
    Extended user schema that includes detailed role information
    """
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    last_login: Optional[datetime] = None
    
    class Config:
        """
        Pydantic configuration for ORM mode
        """
        from_attributes = True
