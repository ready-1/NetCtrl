# NetCtrl CMS User Management Guide

## Overview

This guide provides comprehensive information about user management operations in the NetCtrl CMS system, including CRUD (Create, Read, Update, Delete) operations and role-based access control (RBAC).

## Authentication

Before using any of the user management endpoints, you must be authenticated. See the `AUTHENTICATION_GUIDE.md` for details on how to authenticate.

## Role-Based Access Control (RBAC)

The NetCtrl CMS implements a role-based access control system with three roles:

- **Admin**: Full access to all features and endpoints
- **Manager**: Access to content management and limited user management
- **User**: Limited access to own profile and content

## User Endpoints

### List All Users

**Endpoint**: `GET /api/v1/users/`  
**Permission**: Admin only  
**Description**: Returns a list of all users in the system with pagination.

**Query Parameters**:
- `skip` (int, optional): Number of records to skip (default: 0)
- `limit` (int, optional): Maximum number of records to return (default: 100)
- `role` (string, optional): Filter users by role (admin, manager, user)

**Example Request**:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost/api/v1/users?limit=10&skip=0&role=manager"
```

**Example Response**:
```json
[
  {
    "id": 1,
    "email": null,
    "is_active": true,
    "is_verified": true,
    "is_superuser": true,
    "username": "admin",
    "first_name": "Admin",
    "last_name": "User",
    "role": "admin"
  },
  {
    "id": 2,
    "email": "manager@example.com",
    "is_active": true,
    "is_verified": true,
    "is_superuser": false,
    "username": "manager1",
    "first_name": "Manager",
    "last_name": "One",
    "role": "manager"
  }
]
```

### Get Current User

**Endpoint**: `GET /api/v1/users/me`  
**Permission**: Any authenticated user  
**Description**: Returns the profile of the currently authenticated user.

**Example Request**:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost/api/v1/users/me"
```

**Example Response**:
```json
{
  "id": 1,
  "email": null,
  "is_active": true,
  "is_verified": true,
  "is_superuser": true,
  "username": "admin",
  "first_name": "Admin",
  "last_name": "User",
  "role": "admin",
  "created_at": "2025-03-17T10:30:00",
  "updated_at": "2025-03-17T10:30:00",
  "last_login": "2025-03-17T10:30:00"
}
```

### Get User by ID

**Endpoint**: `GET /api/v1/users/{user_id}`  
**Permission**: 
- Admin/Manager: Can access any user
- Regular user: Can only access their own profile

**Example Request**:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost/api/v1/users/2"
```

**Example Response**:
```json
{
  "id": 2,
  "email": "manager@example.com",
  "is_active": true,
  "is_verified": true,
  "is_superuser": false,
  "username": "manager1",
  "first_name": "Manager",
  "last_name": "One",
  "role": "manager",
  "created_at": "2025-03-17T10:30:00",
  "updated_at": "2025-03-17T10:30:00",
  "last_login": "2025-03-17T10:30:00"
}
```

### Create User

**Endpoint**: `POST /api/v1/users/`  
**Permission**: Admin/Manager  
**Description**: Creates a new user. Managers cannot create admin users.

**Request Body**:
```json
{
  "username": "newuser",
  "password": "StrongP@ssw0rd",
  "email": "user@example.com",
  "first_name": "New",
  "last_name": "User",
  "role": "user"
}
```

**Notes**:
- `username` is required and must be alphanumeric, between 3 and 50 characters
- `password` is required and must meet complexity requirements:
  - At least 8 characters
  - At least 1 uppercase letter
  - At least 1 lowercase letter
  - At least 1 digit
  - At least 1 special character
- `email` is optional
- `role` defaults to "user" if not specified

**Example Request**:
```bash
curl -X POST "http://localhost/api/v1/users/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"username": "newuser", "password": "StrongP@ssw0rd", "email": "user@example.com", "first_name": "New", "last_name": "User", "role": "user"}'
```

**Example Response**:
```json
{
  "id": 3,
  "email": "user@example.com",
  "is_active": true,
  "is_verified": true,
  "is_superuser": false,
  "username": "newuser",
  "first_name": "New",
  "last_name": "User",
  "role": "user"
}
```

### Update User

**Endpoint**: `PUT /api/v1/users/{user_id}`  
**Permission**: 
- Admin: Can update any user
- Manager: Can update users except admins, cannot change roles
- Regular user: Can only update their own profile, cannot change role

**Request Body** (all fields optional):
```json
{
  "username": "updateduser",
  "password": "NewStrongP@ssw0rd",
  "email": "updated@example.com",
  "first_name": "Updated",
  "last_name": "User",
  "role": "manager"
}
```

**Example Request**:
```bash
curl -X PUT "http://localhost/api/v1/users/3" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"first_name": "Updated", "last_name": "User"}'
```

**Example Response**:
```json
{
  "id": 3,
  "email": "user@example.com",
  "is_active": true,
  "is_verified": true,
  "is_superuser": false,
  "username": "newuser",
  "first_name": "Updated",
  "last_name": "User",
  "role": "user",
  "created_at": "2025-03-17T10:30:00",
  "updated_at": "2025-03-17T10:35:00",
  "last_login": "2025-03-17T10:30:00"
}
```

### Delete User

**Endpoint**: `DELETE /api/v1/users/{user_id}`  
**Permission**:
- Admin: Can delete any user
- Regular user: Can only delete their own account

**Example Request**:
```bash
curl -X DELETE "http://localhost/api/v1/users/3" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Response**: HTTP 204 No Content (Success, no body)

## Role Management

### List All Roles

**Endpoint**: `GET /api/v1/roles/`  
**Permission**: Any authenticated user  
**Description**: Returns a list of all available roles in the system.

**Example Request**:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost/api/v1/roles/"
```

**Example Response**:
```json
[
  "admin",
  "manager",
  "user"
]
```

### List Users by Role

**Endpoint**: `GET /api/v1/roles/{role}/users`  
**Permission**: Admin only  
**Description**: Returns a list of all users with a specific role.

**Example Request**:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost/api/v1/roles/manager/users"
```

**Example Response**:
```json
[
  {
    "id": 2,
    "email": "manager@example.com",
    "is_active": true,
    "is_verified": true,
    "is_superuser": false,
    "username": "manager1",
    "first_name": "Manager",
    "last_name": "One",
    "role": "manager"
  }
]
```

### Assign Role to User

**Endpoint**: `PUT /api/v1/roles/assign/{user_id}`  
**Permission**: Admin only  
**Description**: Assigns a new role to a user.

**Request Body**:
```json
"admin"  // or "manager" or "user"
```

**Example Request**:
```bash
curl -X PUT "http://localhost/api/v1/roles/assign/2" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '"manager"'
```

**Example Response**:
```json
{
  "id": 2,
  "email": "manager@example.com",
  "is_active": true,
  "is_verified": true,
  "is_superuser": false,
  "username": "manager1",
  "first_name": "Manager",
  "last_name": "One",
  "role": "manager",
  "created_at": "2025-03-17T10:30:00",
  "updated_at": "2025-03-17T10:40:00",
  "last_login": "2025-03-17T10:30:00"
}
```

### Get Current User Permissions

**Endpoint**: `GET /api/v1/roles/my-permissions`  
**Permission**: Any authenticated user  
**Description**: Returns the permissions of the current user based on their role.

**Example Request**:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost/api/v1/roles/my-permissions"
```

**Example Response**:
```json
{
  "can_view_all_users": true,
  "can_create_users": true,
  "can_update_users": true,
  "can_delete_users": true,
  "can_assign_roles": true,
  "can_view_roles": true,
  "can_manage_content": true
}
```

## Error Handling

| Status Code | Description | Example |
|-------------|-------------|---------|
| 400 | Bad Request - Invalid input | `{"detail": "Error creating user: Username must be alphanumeric"}` |
| 401 | Unauthorized - Missing or invalid token | `{"detail": "Not authenticated"}` |
| 403 | Forbidden - Insufficient permissions | `{"detail": "Not enough permissions to create admin users"}` |
| 404 | Not Found - Resource not found | `{"detail": "User not found"}` |
| 422 | Validation Error - Input validation failed | `{"detail": [{"loc": ["body", "password"], "msg": "Password must be at least 8 characters long", "type": "value_error"}]}` |

## Superuser Setup

The system is initially configured with a default superuser:
- Username: `admin`
- Password: `admin123`

In production, you should override these defaults by setting the following environment variables:
- `NETCTRL_FIRST_SUPERUSER_USERNAME`
- `NETCTRL_FIRST_SUPERUSER_PASSWORD`
- `NETCTRL_FIRST_SUPERUSER_EMAIL` (optional)

For security reasons, it's strongly recommended to change the default admin password in production environments.
