# NetCtrl CMS API Examples Using cURL

This document provides examples of how to interact with the NetCtrl CMS API using cURL commands.

## Authentication

### Login

To authenticate and obtain a JWT token:

```bash
curl -X POST "http://localhost/api/v1/jwt/login" \
  -d "username=admin&password=admin123&grant_type=password" \
  -H "Content-Type: application/x-www-form-urlencoded"
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiYXVkIjpudWxsLCJleHAiOjE3NDIyNDMwNjB9.Jy6Th6qnqaLByhB3Az77IBawKMAn6cCj6GWQ7_z2UOQ",
  "token_type": "bearer"
}
```

### Get Current User

Retrieve the current authenticated user's details:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost/api/v1/users/me"
```

Replace `YOUR_TOKEN` with the access token obtained from login.

## User Management

### List All Users (Admin Only)

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost/api/v1/users?limit=10&skip=0"
```

### Create a New User

```bash
curl -X POST "http://localhost/api/v1/users/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "password": "StrongP@ssw0rd",
    "email": "user@example.com",
    "first_name": "New",
    "last_name": "User",
    "role": "user"
  }'
```

### Get User by ID

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost/api/v1/users/2"
```

### Update User

```bash
curl -X PUT "http://localhost/api/v1/users/2" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Updated",
    "last_name": "User"
  }'
```

### Delete User

```bash
curl -X DELETE "http://localhost/api/v1/users/2" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Role Management

### List All Roles

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost/api/v1/roles/"
```

### List Users by Role

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost/api/v1/roles/manager/users"
```

### Assign Role to User

```bash
curl -X PUT "http://localhost/api/v1/roles/assign/2" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '"manager"'
```

### Get Current User Permissions

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost/api/v1/roles/my-permissions"
```

## Notes

- All API endpoints require authentication except for login and register.
- Different endpoints have different permission requirements based on roles.
- Replace `YOUR_TOKEN` with the actual JWT token obtained during login.
- Replace URLs with the appropriate host if not running on localhost.
