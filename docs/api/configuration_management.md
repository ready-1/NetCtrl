# Configuration Management

## Overview

API endpoints for managing switch configurations, including backups, templates, and version control.

## Endpoints

### List Configurations

```http
GET /api/v1/switches/{switch_id}/configurations/
```

Returns a list of configuration backups for a switch.

### Get Configuration

```http
GET /api/v1/switches/{switch_id}/configurations/{config_id}/
```

Returns a specific configuration backup.

### Create Configuration Backup

```http
POST /api/v1/switches/{switch_id}/configurations/
```

Creates a new configuration backup.

### Apply Configuration

```http
POST /api/v1/switches/{switch_id}/configurations/{config_id}/apply/
```

Applies a configuration backup to the switch.

### List Templates

```http
GET /api/v1/templates/
```

Returns a list of configuration templates.

### Create Template

```http
POST /api/v1/templates/
Content-Type: application/json

{
    "name": "string",
    "description": "string",
    "content": "string"
}
```

### Apply Template

```http
POST /api/v1/switches/{switch_id}/templates/{template_id}/apply/
```

Applies a configuration template to the switch.

### Compare Configurations

```http
POST /api/v1/configurations/compare/
Content-Type: application/json

{
    "config1_id": "integer",
    "config2_id": "integer"
}
```

Returns a diff of two configurations.

## Error Responses

- **400 Bad Request**: Invalid configuration
- **404 Not Found**: Configuration not found
- **409 Conflict**: Configuration conflict
- **503 Service Unavailable**: Switch unreachable
