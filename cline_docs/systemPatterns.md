# System Patterns

## Architecture Patterns
- Django-based web application
- Real-time monitoring with WebSocket updates
- Threaded status checking for parallel interface monitoring
- Role-based access control

## Error Handling Patterns
- Standardized error messages across the system:
  - Connection errors: "No response"
  - Authentication errors: "Auth failed", "SSL"
  - System errors: "Error", "Timeout"
- Error messages are kept concise for UI clarity
- Detailed logging for debugging while keeping UI messages simple
- Status levels: UP, DOWN, DEGRADED

## Code Organization
- Django apps for distinct functionality
- Management commands for background tasks
- Separate thread handling for status monitoring
- WebSocket consumers for real-time updates

## Testing Patterns
- Unit tests for core functionality
- Integration tests for API endpoints
- Frontend integration tests
- Pre-commit hooks for code quality

## UI Patterns
- Real-time status updates
- Color-coded status indicators
- Tooltips for error details
- Consistent error message display
- 5-second refresh interval for status updates

## Security Patterns
- SSL certificate validation
- Authentication required for all operations
- Separate in-band and out-band management
- Connection timeouts for reliability
