# Status Monitoring

## Overview

API endpoints for real-time monitoring of switch status and statistics.

## WebSocket Endpoint

```
ws://<host>/ws/status/
```

Provides real-time status updates for all monitored switches.

### Message Format

```json
{
    "type": "status_update",
    "switches": {
        "switch_id": {
            "status": "up|down|degraded",
            "cpu_usage": "float",
            "memory_usage": "float",
            "temperature": "float",
            "fans": [
                {
                    "id": "string",
                    "status": "ok|failed",
                    "speed": "integer"
                }
            ],
            "ports": {
                "port_id": {
                    "status": "up|down",
                    "speed": "string",
                    "errors": "integer"
                }
            }
        }
    }
}
```

## REST Endpoints

### Get Current Status

```http
GET /api/v1/status/
```

Returns current status of all switches.

### Get Historical Status

```http
GET /api/v1/status/history/
```

Query Parameters:
- `start_time`: Start of time range
- `end_time`: End of time range
- `switch`: Filter by switch ID
- `interval`: Aggregation interval (1m, 5m, 1h)

### Get Switch Health

```http
GET /api/v1/switches/{switch_id}/health/
```

Returns health metrics for a specific switch.

### Get Port Statistics

```http
GET /api/v1/switches/{switch_id}/ports/{port_id}/stats/
```

Returns detailed statistics for a specific port.

## Error Responses

- **400 Bad Request**: Invalid query parameters
- **404 Not Found**: Switch or port not found
- **503 Service Unavailable**: Switch unreachable
