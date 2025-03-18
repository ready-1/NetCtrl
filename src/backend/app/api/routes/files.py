"""API routes for file management"""
from typing import Optional, Dict, Any, List
from fastapi import APIRouter, Depends, HTTPException, Query, Path, Body, UploadFile, File, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.db.session import get_async_session as get_db
from app.auth.users import current_active_user, current_active_user_with_role
from app.models.role import UserRole
from app.models.user import User
from app.models.content import ContentFile
from app.services.file import FileService
from app.schemas.content import ContentFileRead, ContentFileListResponse

router = APIRouter(prefix="/files", tags=["files"])

@router.post("/", response_model=ContentFileRead, status_code=status.HTTP_201_CREATED)
async def upload_file(
    file: UploadFile = File(...),
    content_id: Optional[int] = Query(None, description="Content ID to associate with the file"),
    db: Session = Depends(get_db),
    current_user: User = Depends(current_active_user_with_role)
):
    """
    Upload a new file.
    
    Requires an authenticated user. If content_id is provided, the user must have permission to edit the content.
    """
    content_file = await FileService.create_file(
        db=db,
        file=file,
        content_id=content_id,
        user_id=current_user.id
    )
    return content_file

@router.get("/{file_id}", response_model=ContentFileRead)
async def get_file_metadata(
    file_id: int = Path(..., title="The ID of the file to get metadata for"),
    db: Session = Depends(get_db),
    current_user: User = Depends(current_active_user_with_role)
):
    """
    Get metadata for a specific file.
    
    Requires an authenticated user with appropriate permissions.
    """
    file = await FileService.get_file_by_id(
        db=db,
        file_id=file_id,
        user_id=current_user.id,
        user_role=current_user.role
    )
    return file

@router.get("/{file_id}/download")
async def download_file(
    file_id: int = Path(..., title="The ID of the file to download"),
    db: Session = Depends(get_db),
    current_user: User = Depends(current_active_user_with_role)
):
    """
    Download a file.
    
    Requires an authenticated user with appropriate permissions.
    """
    file = await FileService.get_file_by_id(
        db=db,
        file_id=file_id,
        user_id=current_user.id,
        user_role=current_user.role
    )
    
    try:
        return FileResponse(
            path=file.file_path,
            filename=file.filename,
            media_type=file.mime_type
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"File not found on disk: {str(e)}"
        )

@router.patch("/{file_id}", response_model=ContentFileRead)
async def update_file_metadata(
    metadata: Dict[str, Any] = Body(..., description="File metadata to update"),
    file_id: int = Path(..., title="The ID of the file to update metadata for"),
    db: Session = Depends(get_db),
    current_user: User = Depends(current_active_user_with_role)
):
    """
    Update metadata for a file.
    
    Requires an authenticated user with appropriate permissions.
    """
    file = await FileService.update_file_metadata(
        db=db,
        file_id=file_id,
        metadata=metadata,
        user_id=current_user.id,
        user_role=current_user.role
    )
    return file

@router.delete("/{file_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_file(
    file_id: int = Path(..., title="The ID of the file to delete"),
    db: Session = Depends(get_db),
    current_user: User = Depends(current_active_user_with_role)
):
    """
    Delete a file.
    
    Requires an authenticated user with appropriate permissions.
    """
    await FileService.delete_file(
        db=db,
        file_id=file_id,
        user_id=current_user.id,
        user_role=current_user.role
    )
    return None

@router.get("/", response_model=ContentFileListResponse)
async def list_files(
    content_id: Optional[int] = Query(None, description="Filter files by content ID"),
    skip: int = Query(0, title="Skip items", ge=0),
    limit: int = Query(100, title="Limit items", ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(current_active_user_with_role)
):
    """
    List files with filtering and pagination.
    
    Requires an authenticated user. Results are filtered by user's permissions.
    """
    files, total_count = await FileService.list_files(
        db=db,
        user_id=current_user.id,
        user_role=current_user.role,
        content_id=content_id,
        skip=skip,
        limit=limit
    )
    
    return {
        "items": files,
        "total": total_count,
        "page": skip // limit + 1,
        "size": limit,
        "pages": (total_count + limit - 1) // limit
    }
