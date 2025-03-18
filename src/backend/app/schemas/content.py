"""
Pydantic schemas for content data validation and serialization
"""
from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field, validator

from app.models.content import ContentType, ContentStatus
from app.models.role import UserRole

# Base schemas

class ContentPermissionBase(BaseModel):
    """Base schema for content permission data"""
    role: UserRole
    can_view: bool = False
    can_edit: bool = False
    can_delete: bool = False

class ContentFileBase(BaseModel):
    """Base schema for content file data"""
    filename: str
    file_size: int
    mime_type: str

# Create schemas

class ContentPermissionCreate(ContentPermissionBase):
    """Schema for creating a new content permission"""
    pass

class ContentFileCreate(ContentFileBase):
    """Schema for creating a new content file"""
    content_id: Optional[int] = None

class ContentCreate(BaseModel):
    """Schema for creating a new content item"""
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    body: Optional[str] = None
    content_type: ContentType = ContentType.TEXT
    status: ContentStatus = ContentStatus.DRAFT
    
    @validator('title')
    def title_not_empty(cls, v):
        """Validate title is not empty"""
        if not v.strip():
            raise ValueError('Title cannot be empty')
        return v

# Read schemas

class ContentPermissionRead(ContentPermissionBase):
    """Schema for reading content permission data"""
    id: int
    content_id: int
    
    class Config:
        """Pydantic configuration"""
        from_attributes = True

class ContentFileRead(ContentFileBase):
    """Schema for reading content file data"""
    id: int
    content_id: int
    file_path: str
    uploaded_at: datetime
    uploaded_by: int
    
    class Config:
        """Pydantic configuration"""
        from_attributes = True

class ContentRead(BaseModel):
    """Schema for reading content data"""
    id: int
    title: str
    description: Optional[str] = None
    body: Optional[str] = None
    content_type: ContentType
    status: ContentStatus
    created_by: int
    updated_by: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        """Pydantic configuration"""
        from_attributes = True

class ContentDetailRead(ContentRead):
    """Schema for reading detailed content data with permissions and files"""
    files: List[ContentFileRead] = []
    permissions: List[ContentPermissionRead] = []
    
    class Config:
        """Pydantic configuration"""
        from_attributes = True

# Update schemas

class ContentPermissionUpdate(BaseModel):
    """Schema for updating content permission data"""
    can_view: Optional[bool] = None
    can_edit: Optional[bool] = None
    can_delete: Optional[bool] = None

class ContentUpdate(BaseModel):
    """Schema for updating content data"""
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    body: Optional[str] = None
    status: Optional[ContentStatus] = None
    
    @validator('title')
    def title_not_empty(cls, v):
        """Validate title is not empty if provided"""
        if v is not None and not v.strip():
            raise ValueError('Title cannot be empty')
        return v

# Permission template schemas

class PermissionSettings(BaseModel):
    """Schema for permission settings"""
    can_view: bool = False
    can_edit: bool = False
    can_delete: bool = False

class PermissionTemplate(BaseModel):
    """Schema for permission template"""
    permissions: Dict[UserRole, PermissionSettings]

class ContentPermissionsUpdate(BaseModel):
    """Schema for updating content permissions"""
    permissions: Dict[UserRole, PermissionSettings]

# List response schemas

class ContentListResponse(BaseModel):
    """Schema for content list response"""
    items: List[ContentRead]
    total: int
    page: int
    size: int
    pages: int

class ContentFileListResponse(BaseModel):
    """Schema for content file list response"""
    items: List[ContentFileRead]
    total: int
    page: int
    size: int
    pages: int
