# System Patterns

## Deployment Pattern
The system uses a robust deployment pattern:

1. Environment Handling:
   - .env.example as template
   - Local file preservation
   - Environment validation
   - Secure secret generation

2. Database Management:
   - Automatic initialization
   - Migration handling
   - Superuser creation
   - Connection validation

3. File Structure:
   ```
   /opt/netctrl/
   ├── app/          # Application code
   ├── static/       # Static files
   ├── media/        # User uploads
   ├── certs/        # SSL certificates
   └── logs/         # Application logs
   ```

## Authentication Pattern
The system uses Django's authentication with customizations:

1. User Management:
   - Custom User model
   - Superuser creation during deployment
   - Fixed admin credentials
   - Role-based access

2. Default Superuser:
   ```
   Username: admin
   Email: admin@example.com
   Password: FuseFuse123!
   ```

## URL Pattern
The system uses a prefixed URL pattern:

1. Base Configuration:
   - FORCE_SCRIPT_NAME = '/netctrl'
   - All URLs prefixed
   - Static/media URLs adjusted

2. Nginx Configuration:
   - Proxy pass stripping
   - Static file serving
   - URL rewriting

## File Handling Pattern
The system uses a consistent file handling pattern:

1. Static Files:
   - Collected to /opt/static
   - Served through Nginx
   - Prefixed URLs

2. Media Files:
   - Stored in /opt/media
   - Served through Nginx
   - Prefixed URLs

3. Local Changes:
   - Preserved during deployment
   - Backed up before updates
   - Restored after updates
