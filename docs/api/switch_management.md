# Switch Management

## Overview

API endpoints for managing M4300 network switches, including adding new switches, retrieving status, and managing configurations.

## Endpoints

### List Switches

```http
GET /api/v1/switches/
```

Returns a list of all managed switches.

### Add Switch

```http
POST /api/v1/switches/
Content-Type: application/json

{
    "name": "string",
    "ip_address": "string",
    "username": "string",
    "password": "string",
    "description": "string"
}
```

### Get Switch Details

```http
GET /api/v1/switches/{id}/
```

### Update Switch

```http
PUT /api/v1/switches/{id}/
Content-Type: application/json

{
    "name": "string",
    "description": "string"
}
```

### Delete Switch

```http
DELETE /api/v1/switches/{id}/
```

### Get Switch Status

```http
GET /api/v1/switches/{id}/status/
```

Returns current switch status including:
- Connection state
- CPU usage
- Memory usage
- Temperature
- Fan status
- Port status

### Backup Configuration

```http
POST /api/v1/switches/{id}/backup/
```

Creates a backup of the switch configuration.

## Error Responses

- **400 Bad Request**: Invalid request data
- **404 Not Found**: Switch not found
- **503 Service Unavailable**: Switch unreachable
