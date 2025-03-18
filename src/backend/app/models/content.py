"""
Content models for the CMS system
"""
from enum import Enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum as SQLEnum, Boolean, UniqueConstraint, BigInteger
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.role import UserRole

class ContentType(str, Enum):
    """
    Enumeration of content types in the system
    """
    TEXT = "text"
    HTML = "html"
    MARKDOWN = "markdown"
    FILE = "file"

class ContentStatus(str, Enum):
    """
    Enumeration of content status values in the system
    """
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"

class Content(Base):
    """
    Core content model representing all content items in the CMS
    """
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(String(1000), nullable=True)
    body = Column(Text, nullable=True)
    content_type = Column(SQLEnum(ContentType), nullable=False)
    status = Column(SQLEnum(ContentStatus), nullable=False, default=ContentStatus.DRAFT)
    
    # Ownership and audit
    created_by = Column(Integer, ForeignKey("user.id"), nullable=False)
    updated_by = Column(Integer, ForeignKey("user.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)
    
    # Relationships
    creator = relationship("User", foreign_keys=[created_by], backref="created_content")
    updater = relationship("User", foreign_keys=[updated_by], backref="updated_content")
    files = relationship("ContentFile", back_populates="content", cascade="all, delete-orphan")
    permissions = relationship("ContentPermission", back_populates="content", cascade="all, delete-orphan")

class ContentFile(Base):
    """
    Model for files attached to content items
    """
    __tablename__ = "content_file"

    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(Integer, ForeignKey("content.id"), nullable=False)
    filename = Column(String(255), nullable=False)
    file_path = Column(String(1000), nullable=False)
    file_size = Column(BigInteger, nullable=False)
    mime_type = Column(String(127), nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    uploaded_by = Column(Integer, ForeignKey("user.id"), nullable=False)
    
    # Relationships
    content = relationship("Content", back_populates="files")
    uploader = relationship("User", backref="uploaded_files")

class ContentPermission(Base):
    """
    Model for role-based content permissions
    """
    __tablename__ = "content_permission"

    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(Integer, ForeignKey("content.id"), nullable=False)
    role = Column(SQLEnum(UserRole), nullable=False)
    can_view = Column(Boolean, default=False, nullable=False)
    can_edit = Column(Boolean, default=False, nullable=False)
    can_delete = Column(Boolean, default=False, nullable=False)
    
    # Relationships
    content = relationship("Content", back_populates="permissions")
    
    # Composite unique constraint
    __table_args__ = (
        UniqueConstraint('content_id', 'role', name='uq_content_role'),
    )
