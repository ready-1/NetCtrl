"""
User model for authentication and authorization
"""
from typing import Optional, List
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String, Enum, Boolean, Integer, DateTime
from sqlalchemy.sql import func

from app.db.base import Base
from app.models.role import UserRole

class User(SQLAlchemyBaseUserTable[int], Base):
    """
    Core user model that extends the FastAPI Users base model
    """
    __tablename__ = "user"
    
    # Override id from SQLAlchemyBaseUserTable to explicitly set primary key
    id = Column(Integer, primary_key=True)
    
    # Make email optional and add username as the primary identifier
    email = Column(String(length=320), unique=True, index=True, nullable=True)
    username = Column(String(length=50), unique=True, index=True, nullable=False)
    
    # Authentication fields
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=True, nullable=False)  # Default true since we skip verification
    is_superuser = Column(Boolean, default=False, nullable=False)
    
    # Role field - single role per user for simplicity
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)
    
    # Profile fields
    first_name = Column(String(length=50), nullable=True)
    last_name = Column(String(length=50), nullable=True)
    
    # Audit fields
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login = Column(DateTime(timezone=True), nullable=True)
