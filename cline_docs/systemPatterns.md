# System Patterns

## Core Patterns

### Deployment Pattern
The system uses a robust deployment pattern with data persistence:

1. Environment Handling:
   - .env.example as template
   - Local file preservation
   - Environment validation
   - Secure secret generation

2. Database Management:
   - Persistent volume storage
   - Automatic initialization
   - Migration handling
   - Data preservation

3. File Structure:
   ```
   /opt/netctrl/
   ├── app/          # Application code
   ├── static/       # Static files
   ├── media/        # User uploads
   ├── certs/        # SSL certificates
   └── logs/         # Application logs
   ```

### Authentication Pattern
The system uses Django's authentication with fixed credentials:

1. User Management:
   - Custom User model
   - Fixed superuser credentials
   - Role-based access
   - Simplified permissions

2. Default Superuser:
   ```
   Username: admin
   Email: admin@example.com
   Password: FuseFuse123!
   ```

### URL Pattern
The system uses a consistent URL structure:

1. Base Configuration:
   - FORCE_SCRIPT_NAME = '/netctrl'
   - All URLs prefixed
   - Static/media URLs adjusted

2. Nginx Configuration:
   - Proxy pass stripping
   - Static file serving
   - URL rewriting

## Data Patterns

### Switch Management Pattern
The system uses a simplified switch management pattern:

1. Data Model:
   - Basic switch properties
   - IP address validation
   - Status tracking
   - Description field

2. Operations:
   - CRUD operations
   - CSV import
   - Batch updates
   - Data validation

### File Handling Pattern
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

### Data Persistence Pattern
The system ensures data persistence across deployments:

1. Volume Management:
   - Named volumes for databases
   - Preserved during updates
   - Backup support
   - Data integrity

2. Deployment Safety:
   - Database volume preserved
   - Configuration preserved
   - Credentials maintained
   - Migration handling
