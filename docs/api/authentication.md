# Authentication

## Overview

NetCtrl uses Django's built-in authentication system with token-based authentication for API access.

## User Roles

- **Non-Privileged**: Read-only access to switch status and configurations
- **Privileged**: Can modify switch configurations and port settings
- **Superuser**: Full administrative access

## Authentication Methods

### Session Authentication (Web Interface)

Standard Django session-based authentication used for the web interface.

```http
POST /api/auth/login/
Content-Type: application/json

{
    "username": "string",
    "password": "string"
}
```

### Token Authentication (API)

Used for programmatic API access.

1. Obtain token:
```http
POST /api/auth/token/
Content-Type: application/json

{
    "username": "string",
    "password": "string"
}
```

2. Use token in requests:
```http
GET /api/v1/switches/
Authorization: Token <your-token>
```

## Error Responses

- **401 Unauthorized**: Invalid or missing credentials
- **403 Forbidden**: Insufficient permissions for the requested operation
