# Content Management System Implementation Plan

## Overview
This plan outlines a comprehensive approach for implementing the CMS backend with role-based access control (RBAC). The system will be built on FastAPI and will handle content creation, storage, retrieval, versioning, and permissions. All components are designed to work within Docker containers for seamless deployment.

## Core Components

### 1. Data Models

#### Content Model
- `id`: Unique identifier for content
- `title`: Title of the content
- `content_type`: Type of content (PAGE, POST, DOCUMENT, etc.)
- `body`: Main content body (HTML, Markdown, or plain text)
- `status`: Current state (DRAFT, PUBLISHED, ARCHIVED)
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `author_id`: Reference to the user who created the content
- `metadata`: JSON field for flexible metadata storage (tags, categories, etc.)

#### ContentVersion Model
- `id`: Unique identifier for the version
- `content_id`: Reference to the parent content
- `version_number`: Sequential version number
- `changes`: Description of changes
- `created_at`: Version creation timestamp
- `created_by_id`: User who created this version
- `content_data`: JSON snapshot of the content at this version

#### File Model
- `id`: Unique identifier for the file
- `filename`: Original filename
- `filepath`: Storage path
- `mimetype`: File MIME type
- `size`: File size in bytes
- `uploaded_at`: Upload timestamp
- `uploaded_by_id`: User who uploaded the file
- `metadata`: Additional file metadata (dimensions for images, etc.)

### 2. API Endpoints

#### Content Management
- `GET /api/v1/content/` - List content with filtering and pagination
- `POST /api/v1/content/` - Create new content
- `GET /api/v1/content/{id}` - Get content by ID
- `PATCH /api/v1/content/{id}` - Update content
- `DELETE /api/v1/content/{id}` - Delete content
- `GET /api/v1/content/{id}/versions` - List content versions
- `GET /api/v1/content/{id}/versions/{version_id}` - Get specific content version
- `POST /api/v1/content/{id}/restore/{version_id}` - Restore content to specific version

#### File Management
- `POST /api/v1/files/` - Upload file
- `GET /api/v1/files/{id}` - Get file metadata
- `GET /api/v1/files/{id}/download` - Download file
- `DELETE /api/v1/files/{id}` - Delete file
- `GET /api/v1/files/` - List files with filtering

### 3. Permission System

The system will use role-based access control with the following roles:
- `ADMIN`: Full access to all content and system settings
- `EDITOR`: Can create, edit, and publish content
- `AUTHOR`: Can create and edit their own content, but not publish
- `VIEWER`: Can only view published content

Permission checks will be implemented as FastAPI dependencies that can be applied to API routes.

#### Implementation Strategy
1. Create a `permissions.py` module with permission check functions
2. Implement permission decorators for routes
3. Include object-level permissions (e.g., authors can edit their own content)

```python
# Example permission dependency
async def can_edit_content(
    content_id: int,
    current_user = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> bool:
    content = await get_content_by_id(content_id, session)
    
    # Admin can edit any content
    if current_user.role == UserRole.ADMIN:
        return True
        
    # Editors can edit any content
    if current_user.role == UserRole.EDITOR:
        return True
        
    # Authors can only edit their own content
    if current_user.role == UserRole.AUTHOR and content.author_id == current_user.id:
        return True
        
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You don't have permission to edit this content"
    )
```

### 4. Content Versioning

Each update to content will create a new version record, allowing for:
- Version history tracking
- Rollback to previous versions
- Audit trail of changes

Implementation:
1. Use SQLAlchemy event listeners to capture content changes
2. Store complete content snapshots for each version
3. Provide API endpoints for version management

### 5. File Handling

The system will support file uploads with:
- Secure file storage
- Efficient retrieval
- Support for various file types
- Proper permissions for access

Implementation:
1. Use FastAPI's `UploadFile` for handling uploads
2. Store files in a structured directory or use object storage
3. Track file metadata in the database
4. Implement proper access controls

### 6. Search and Filtering

Implement robust search and filtering capabilities:
- Full-text search for content
- Filtering by content type, status, author, etc.
- Sorting options
- Pagination support

Implementation:
1. Use SQLAlchemy queries with filter parameters
2. Add full-text search capabilities using PostgreSQL features
3. Implement pagination with limit/offset parameters

### 7. Docker Deployment

The CMS will be deployed using Docker, with:
- Separate containers for the backend, database, and file storage
- Volume mapping for persistent storage
- Environment variables for configuration
- Health checks and proper container dependencies

#### Docker Considerations
- Use environment variables for all configuration
- Implement proper volume mapping for file storage
- Configure database connections properly
- Set up proper logging and monitoring

### 8. Testing Strategy

Comprehensive testing will include:
- Unit tests for all business logic
- Integration tests for database operations
- API tests for all endpoints
- Authentication and permission tests
- File upload and download tests
- Content versioning tests

Test implementation:
1. Use pytest for test framework
2. Create test fixtures for database setup and teardown
3. Implement async test client for API testing
4. Use test database for integration tests

## Implementation Phases

### Phase 1: Core Models and Database
- Define all SQLAlchemy models
- Set up database migrations
- Implement database access patterns

### Phase 2: Basic API Endpoints
- Create basic CRUD endpoints for content
- Implement user authentication integration
- Add basic permission checks

### Phase 3: File Management
- Implement file upload and storage
- Add file metadata tracking
- Create file access APIs

### Phase 4: Advanced Features
- Implement content versioning
- Add full-text search
- Enhance permission system

### Phase 5: Testing and Deployment
- Create comprehensive test suite
- Set up Docker deployment
- Document API and usage

## Testing

Tests will be organized as follows:

1. **Unit Tests**
   - Test individual functions and methods
   - Focus on business logic and validation

2. **Integration Tests**
   - Test database operations
   - Test service layer interactions

3. **API Tests**
   - Test all API endpoints
   - Verify correct responses
   - Test authentication and permissions

4. **End-to-End Tests**
   - Test complete workflows
   - Simulate real user scenarios

## Performance Considerations

- Use pagination for list endpoints
- Implement caching for frequently accessed content
- Optimize database queries
- Consider async processing for file uploads

## Security Considerations

- Validate all input data
- Implement proper authentication checks
- Apply principle of least privilege for permissions
- Sanitize content to prevent XSS attacks
- Validate file uploads for security

## Docker Deployment Diagram

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  FastAPI        │     │  PostgreSQL     │     │  File Storage   │
│  Backend        │────▶│  Database       │     │  Volume         │
│                 │     │                 │     │                 │
└────────┬────────┘     └─────────────────┘     └────────▲────────┘
         │                                              │
         └──────────────────────────────────────────────┘
```

## Conclusion

This implementation plan provides a structured approach to building a robust CMS backend with RBAC. By focusing on clean architecture, proper testing, and secure design, we'll create a maintainable and scalable system that meets all the requirements.
