# Audit Logging

## Overview

API endpoints for accessing and managing audit logs of all system actions.

## Endpoints

### List Audit Logs

```http
GET /api/v1/audit-logs/
```

Query Parameters:
- `start_date`: Filter logs from this date
- `end_date`: Filter logs until this date
- `user`: Filter by username
- `action`: Filter by action type
- `switch`: Filter by switch ID

### Get Audit Log Entry

```http
GET /api/v1/audit-logs/{id}/
```

Returns details of a specific audit log entry.

### Export Audit Logs

```http
GET /api/v1/audit-logs/export/
Accept: application/csv
```

Exports audit logs in CSV format.

## Log Entry Fields

- `timestamp`: When the action occurred
- `user`: Username who performed the action
- `action`: Type of action performed
- `target`: Object affected by the action
- `details`: Additional context about the action
- `status`: Success or failure of the action
- `ip_address`: IP address of the user
- `user_agent`: User agent of the client

## Action Types

- `LOGIN`: User login
- `LOGOUT`: User logout
- `CREATE`: Resource creation
- `UPDATE`: Resource modification
- `DELETE`: Resource deletion
- `BACKUP`: Configuration backup
- `RESTORE`: Configuration restore
- `APPLY`: Template application

## Error Responses

- **400 Bad Request**: Invalid query parameters
- **404 Not Found**: Log entry not found
