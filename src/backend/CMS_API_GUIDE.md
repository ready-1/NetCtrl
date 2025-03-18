# NetCtrl CMS API Guide

This guide documents the Content Management System (CMS) API for the NetCtrl application. The CMS provides comprehensive functionality for creating, retrieving, updating, and deleting content, along with file management and role-based permissions.

## Authentication

All CMS API endpoints require authentication. You need to include a valid JWT token in the Authorization header:

```
Authorization: Bearer your-jwt-token
```

See the [AUTHENTICATION_GUIDE.md](./AUTHENTICATION_GUIDE.md) for details on how to obtain a token.

## Content Management API

### Create Content

**Endpoint:** `POST /api/v1/content/`

Creates a new content item in the CMS.

**Request Body:**
```json
{
  "title": "Example Content",
  "description": "This is a description of the content",
  "body": "This is the main content body with details.",
  "content_type": "text",
  "status": "draft"
}
```

**Content Types:**
- `text`: Plain text content
- `html`: HTML formatted content
- `markdown`: Markdown formatted content
- `file`: File-based content

**Content Status:**
- `draft`: Not yet published
- `published`: Publicly available
- `archived`: No longer actively shown

**Response:**
```json
{
  "id": 1,
  "title": "Example Content",
  "description": "This is a description of the content",
  "body": "This is the main content body with details.",
  "content_type": "text",
  "status": "draft",
  "created_by": 1,
  "updated_by": 1,
  "created_at": "2025-03-18T12:30:00",
  "updated_at": "2025-03-18T12:30:00"
}
```

### Get Content by ID

**Endpoint:** `GET /api/v1/content/{content_id}`

Retrieves detailed information for a specific content item including associated files and permissions.

**Response:**
```json
{
  "id": 1,
  "title": "Example Content",
  "description": "This is a description of the content",
  "body": "This is the main content body with details.",
  "content_type": "text",
  "status": "draft",
  "created_by": 1,
  "updated_by": 1,
  "created_at": "2025-03-18T12:30:00",
  "updated_at": "2025-03-18T12:30:00",
  "files": [
    {
      "id": 1,
      "content_id": 1,
      "filename": "document.pdf",
      "file_path": "/app/uploads/1/document.pdf",
      "file_size": 1024567,
      "mime_type": "application/pdf",
      "uploaded_at": "2025-03-18T12:35:00",
      "uploaded_by": 1
    }
  ],
  "permissions": [
    {
      "id": 1,
      "content_id": 1,
      "role": "admin",
      "can_view": true,
      "can_edit": true,
      "can_delete": true
    },
    {
      "id": 2,
      "content_id": 1,
      "role": "user",
      "can_view": true,
      "can_edit": false,
      "can_delete": false
    }
  ]
}
```

### List Content

**Endpoint:** `GET /api/v1/content/`

Lists content items with filtering and pagination.

**Query Parameters:**
- `skip`: Number of items to skip (default: 0)
- `limit`: Maximum number of items to return (default: 100, max: 100)
- `status_filter`: Filter by content status (`draft`, `published`, `archived`)
- `content_type_filter`: Filter by content type (`text`, `html`, `markdown`, `file`)
- `search`: Search in title, description, and body text

**Response:**
```json
{
  "items": [
    {
      "id": 1,
      "title": "Example Content",
      "description": "This is a description of the content",
      "body": "This is the main content body with details.",
      "content_type": "text",
      "status": "draft",
      "created_by": 1,
      "updated_by": 1,
      "created_at": "2025-03-18T12:30:00",
      "updated_at": "2025-03-18T12:30:00"
    },
    {
      "id": 2,
      "title": "Another Content Item",
      "description": "Description for the second item",
      "body": "Main content for the second item.",
      "content_type": "html",
      "status": "published",
      "created_by": 1,
      "updated_by": 1,
      "created_at": "2025-03-18T12:40:00",
      "updated_at": "2025-03-18T12:40:00"
    }
  ],
  "total": 2,
  "page": 1,
  "size": 100,
  "pages": 1
}
```

### Update Content

**Endpoint:** `PUT /api/v1/content/{content_id}`

Updates a content item.

**Request Body:**
```json
{
  "title": "Updated Content Title",
  "description": "Updated description",
  "body": "Updated content body",
  "status": "published"
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Updated Content Title",
  "description": "Updated description",
  "body": "Updated content body",
  "content_type": "text",
  "status": "published",
  "created_by": 1,
  "updated_by": 1,
  "created_at": "2025-03-18T12:30:00",
  "updated_at": "2025-03-18T12:45:00"
}
```

### Delete Content

**Endpoint:** `DELETE /api/v1/content/{content_id}`

Deletes a content item and all associated files and permissions.

**Response:** `204 No Content`

### Set Content Permissions

**Endpoint:** `POST /api/v1/content/{content_id}/permissions`

Sets permissions for a content item.

**Request Body:**
```json
{
  "permissions": {
    "admin": {
      "can_view": true,
      "can_edit": true,
      "can_delete": true
    },
    "editor": {
      "can_view": true,
      "can_edit": true,
      "can_delete": false
    },
    "user": {
      "can_view": true,
      "can_edit": false,
      "can_delete": false
    }
  }
}
```

**Response:**
```json
{
  "success": true
}
```

### Get Content Permissions

**Endpoint:** `GET /api/v1/content/{content_id}/permissions`

Gets permissions for a content item.

**Response:**
```json
{
  "admin": {
    "can_view": true,
    "can_edit": true,
    "can_delete": true
  },
  "editor": {
    "can_view": true,
    "can_edit": true,
    "can_delete": false
  },
  "user": {
    "can_view": true,
    "can_edit": false,
    "can_delete": false
  }
}
```

## File Management API

### Upload File

**Endpoint:** `POST /api/v1/files/`

Uploads a file to the server.

**Form Data:**
- `file`: The file to upload
- `content_id`: (Optional) The ID of the content to associate the file with

**Response:**
```json
{
  "id": 1,
  "content_id": 1,
  "filename": "document.pdf",
  "file_path": "/app/uploads/1/document.pdf",
  "file_size": 1024567,
  "mime_type": "application/pdf",
  "uploaded_at": "2025-03-18T12:35:00",
  "uploaded_by": 1
}
```

### List Files

**Endpoint:** `GET /api/v1/files/`

Lists files with optional filtering by content ID.

**Query Parameters:**
- `content_id`: (Optional) Filter files by content ID
- `skip`: Number of items to skip (default: 0)
- `limit`: Maximum number of items to return (default: 100, max: 100)

**Response:**
```json
{
  "items": [
    {
      "id": 1,
      "content_id": 1,
      "filename": "document.pdf",
      "file_path": "/app/uploads/1/document.pdf",
      "file_size": 1024567,
      "mime_type": "application/pdf",
      "uploaded_at": "2025-03-18T12:35:00",
      "uploaded_by": 1
    },
    {
      "id": 2,
      "content_id": 2,
      "filename": "image.jpg",
      "file_path": "/app/uploads/2/image.jpg",
      "file_size": 256789,
      "mime_type": "image/jpeg",
      "uploaded_at": "2025-03-18T12:50:00",
      "uploaded_by": 1
    }
  ],
  "total": 2,
  "page": 1,
  "size": 100,
  "pages": 1
}
```

### Get File Metadata

**Endpoint:** `GET /api/v1/files/{file_id}`

Gets metadata for a specific file.

**Response:**
```json
{
  "id": 1,
  "content_id": 1,
  "filename": "document.pdf",
  "file_path": "/app/uploads/1/document.pdf",
  "file_size": 1024567,
  "mime_type": "application/pdf",
  "uploaded_at": "2025-03-18T12:35:00",
  "uploaded_by": 1
}
```

### Download File

**Endpoint:** `GET /api/v1/files/{file_id}/download`

Downloads a file.

**Response:** The file as a binary response with appropriate Content-Type header.

### Update File Metadata

**Endpoint:** `PATCH /api/v1/files/{file_id}`

Updates metadata for a file.

**Request Body:**
```json
{
  "filename": "renamed-document.pdf",
  "content_id": 2
}
```

**Response:**
```json
{
  "id": 1,
  "content_id": 2,
  "filename": "renamed-document.pdf",
  "file_path": "/app/uploads/1/document.pdf",
  "file_size": 1024567,
  "mime_type": "application/pdf",
  "uploaded_at": "2025-03-18T12:35:00",
  "uploaded_by": 1
}
```

### Delete File

**Endpoint:** `DELETE /api/v1/files/{file_id}`

Deletes a file from both the database and disk.

**Response:** `204 No Content`

## Permissions System

The CMS uses a role-based permission system for content access:

- **Admin**: Full access to all content and files
- **Editor**: Can create and edit content but may have restricted deletion rights
- **User**: Default role with limited permissions (typically only view access)

Each content item has specific permissions per role, controlling:

- `can_view`: Whether the role can view the content
- `can_edit`: Whether the role can edit the content
- `can_delete`: Whether the role can delete the content

Additionally:
- Content creators automatically have view and edit permissions to their own content
- Files inherit permissions from their associated content
- Unassociated files can only be accessed by their uploader or admins

## Example cURL Commands

### Login (to get token)

```bash
curl -X POST "http://localhost/api/v1/jwt/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin123&grant_type=password"
```

### Create Content

```bash
curl -X POST "http://localhost/api/v1/content/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "API Documentation",
    "description": "Comprehensive guide to using the API",
    "body": "# API Documentation\n\nThis document explains how to use our API...",
    "content_type": "markdown",
    "status": "published"
  }'
```

### Upload File

```bash
curl -X POST "http://localhost/api/v1/files/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "file=@/path/to/local/file.pdf" \
  -F "content_id=1"
```

### List Content with Search

```bash
curl -X GET "http://localhost/api/v1/content/?search=documentation&status_filter=published" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Set Content Permissions

```bash
curl -X POST "http://localhost/api/v1/content/1/permissions" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "permissions": {
      "admin": {
        "can_view": true,
        "can_edit": true,
        "can_delete": true
      },
      "editor": {
        "can_view": true,
        "can_edit": true,
        "can_delete": false
      },
      "user": {
        "can_view": true,
        "can_edit": false,
        "can_delete": false
      }
    }
  }'
