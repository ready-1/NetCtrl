# Port Management

## Overview

API endpoints for managing switch ports, including configuration, status monitoring, and bulk operations.

## Endpoints

### List Ports

```http
GET /api/v1/switches/{switch_id}/ports/
```

Returns a list of all ports on a switch.

### Get Port Details

```http
GET /api/v1/switches/{switch_id}/ports/{port_id}/
```

### Update Port Configuration

```http
PUT /api/v1/switches/{switch_id}/ports/{port_id}/
Content-Type: application/json

{
    "admin_status": "up|down",
    "description": "string",
    "vlan": "integer",
    "speed": "string",
    "duplex": "full|half|auto"
}
```

### Get Port Statistics

```http
GET /api/v1/switches/{switch_id}/ports/{port_id}/stats/
```

Returns port statistics including:
- Bytes in/out
- Packets in/out
- Errors
- Discards

### Bulk Port Update

```http
POST /api/v1/switches/{switch_id}/ports/bulk/
Content-Type: application/json

{
    "ports": ["1/0/1", "1/0/2"],
    "config": {
        "admin_status": "up|down",
        "vlan": "integer"
    }
}
```

### Apply Port Profile

```http
POST /api/v1/switches/{switch_id}/ports/{port_id}/profile/
Content-Type: application/json

{
    "profile_id": "integer"
}
```

## Error Responses

- **400 Bad Request**: Invalid configuration
- **404 Not Found**: Port not found
- **409 Conflict**: Port in use or operation not allowed
