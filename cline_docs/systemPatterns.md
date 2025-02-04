# System Patterns

## Authentication System

### Switch Authentication
1. Token-Based Authentication:
   - Uses JWT tokens from switch API
   - Tokens stored in Switch model with expiration time
   - Automatic refresh before expiration (15-minute buffer)
   - Background thread for token maintenance

2. SSL/TLS Configuration:
   - Uses SSLv23 protocol for backward compatibility
   - Minimal SSL restrictions for legacy switch support
   - Custom SSL context with all ciphers enabled
   - Certificate verification disabled for self-signed certs

3. Error Handling:
   - Handles both JSON and plain text responses
   - Detailed logging of all authentication steps
   - Graceful handling of connection issues
   - Status tracking in Switch model

4. Background Tasks:
   - TokenRefreshThread for automatic token management
   - Runs only in production environment
   - 5-minute check interval
   - Daemon thread for clean shutdown

### API Communication
1. Request Format:
   ```json
   {
     "login": {
       "username": "admin",
       "password": "password"
     }
   }
   ```

2. Response Format:
   ```json
   {
     "login": {
       "token": "...",
       "expire": "86400"
     },
     "resp": {
       "status": "success",
       "respCode": 0,
       "respMsg": "Operation success"
     }
   }
   ```

3. Error Handling:
   - HTTP 200 with error message for auth failures
   - JSON response validation
   - Required field verification
   - SSL/TLS error recovery

## Database Models

### Switch Model
- Authentication fields:
  - auth_token: Current JWT token
  - token_expires: Token expiration timestamp
  - auth_status: Current authentication state
  - username/password: Switch credentials

### Status Tracking
- AUTH_STATUS_AUTHENTICATED: Successfully logged in
- AUTH_STATUS_UNAUTHENTICATED: No active session
- AUTH_STATUS_ERROR: Authentication failed

## Background Tasks
- Daemon threads for maintenance tasks
- Production-only execution
- Error logging and recovery
- Clean shutdown handling
