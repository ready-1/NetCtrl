# NetCtrl CMS Authentication Guide

## Overview

The NetCtrl CMS uses a username-based authentication system with JWT tokens and role-based access control (RBAC). This guide covers authentication concepts, API endpoints, and common usage patterns.

## Authentication Endpoints

| Endpoint                    | Method | Description                               | Authentication |
|-----------------------------|--------|-------------------------------------------|----------------|
| `/api/v1/jwt/login`         | POST   | Login to get JWT token                    | None           |
| `/api/v1/users/me`          | GET    | Get current user information              | JWT Token      |
| `/api/v1/register/register` | POST   | Register a new user                       | None           |

## Authentication Flow Examples

### 1. Login to Get JWT Token

**Request:**
```bash
curl -X POST "http://localhost/api/v1/jwt/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin123&grant_type=password"
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 2. Retrieve Current User Information

**Request:**
```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  http://localhost/api/v1/users/me
```

**Response:**
```json
{
  "id": 1,
  "email": null,
  "is_active": true,
  "is_superuser": true,
  "is_verified": true,
  "username": "admin",
  "first_name": null,
  "last_name": null,
  "role": "admin"
}
```

### 3. Register a New User

**Request:**
```bash
curl -X POST "http://localhost/api/v1/register/register" \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpassword123", "role": "user"}'
```

**Response:**
```json
{
  "id": 2,
  "email": null,
  "is_active": true,
  "is_superuser": false,
  "is_verified": true,
  "username": "testuser",
  "first_name": null,
  "last_name": null,
  "role": "user"
}
```

## Role-Based Access Control (RBAC)

Users have one of the following roles:
- `admin`: Full system access including user management
- `manager`: Content management access and limited admin functions
- `user`: Regular user access with restricted permissions

Role-specific endpoints verify the user's role before providing access.

## Default Credentials

The system is initialized with a default admin user:
- Username: `admin`
- Password: `admin123`

It is recommended to change the default password in production.

## Security Considerations

1. Always include the `Authorization` header with the format `Bearer {token}` when accessing protected endpoints.

2. JWT tokens expire after 7 days by default (configurable in settings).

3. If you receive a 401 Unauthorized error, your token may have expired. Login again to get a fresh token.

4. Passwords are stored using secure bcrypt hashing.

## Troubleshooting

### Common Issues

1. **LOGIN_BAD_CREDENTIALS**: This error means either the username or password is incorrect.

2. **TOKEN_EXPIRED**: The JWT token has expired. Get a new token by logging in again.

### Resetting Admin Password

If you need to reset the admin password:

```bash
docker compose exec backend python scripts/reset_admin_password.py newpassword
