# NetCtrl Project Structure

For a comprehensive overview of the system architecture, please see [architecture.md](architecture.md).

## Directory Structure
```
netctrl/
├── config/               # Project configuration
│   ├── settings.py      # Django settings
│   ├── urls.py          # Main URL routing
│   ├── asgi.py          # ASGI configuration
│   └── wsgi.py          # WSGI configuration
│
├── netdash/             # Core dashboard app
│   ├── migrations/      # Database migrations
│   ├── templates/       # Dashboard templates
│   ├── admin.py         # Admin interface
│   ├── apps.py         # App configuration
│   ├── forms.py        # Form definitions
│   ├── models.py       # Data models
│   ├── urls.py         # URL patterns
│   └── views.py        # View logic
│
├── netdevices/          # Device management app
│   ├── migrations/      # Database migrations
│   ├── templates/       # Device templates
│   ├── admin.py        # Admin interface
│   ├── apps.py         # App configuration
│   ├── models.py       # Device models
│   ├── urls.py         # URL patterns
│   └── views.py        # View logic
│
├── netconfig/          # Configuration management app
│   ├── migrations/     # Database migrations
│   ├── templates/      # Config templates
│   ├── admin.py       # Admin interface
│   ├── apps.py        # App configuration
│   ├── models.py      # Config models
│   ├── urls.py        # URL patterns
│   └── views.py       # View logic
│
├── static/             # Static files
│   ├── css/           # Stylesheets
│   ├── js/            # JavaScript files
│   └── vendor/        # Third-party assets
│
├── templates/          # Global templates
│   └── base/          # Base template files
│
├── media/             # User-uploaded files
│   ├── configs/       # Device configurations
│   └── backups/       # Configuration backups
│
├── docs/              # Project documentation
│   └── dev/          # Developer documentation
│
└── manage.py          # Django management script
```

## Key Components

### Authentication System
- Custom User model with approval workflow
- Staff-based user approval system
- Login and registration views
- Middleware for approval enforcement

### Templates
- Base template with Bootstrap styling
- Navigation with dynamic notifications
- Responsive dashboard layout
- Device management interfaces

### Static Files
- Bootstrap CSS framework
- Custom stylesheets
- Bootstrap Icons
- HTMX for dynamic updates

### Configuration
- SQLite database (development)
- Static/media file handling
- Custom middleware configuration
- Authentication settings

## Development Guidelines

### MCP Server Integration
- Use MCP tools for file operations
- Monitor file changes during development
- Use batch operations for related changes
- Perform regex-based code analysis

### Documentation
- Store all documentation in /docs/dev
- Document system dependencies
- Maintain current examples
- Track system changes

### Testing
- Write tests before implementation
- Cover all edge cases
- Document test cases
- Full test coverage required

### Error Handling
- Comprehensive error handling
- Proper validation of all inputs
- Clear error messages
- Recovery procedures

## Future Enhancements
1. PostgreSQL database migration
2. Device configuration templates
3. Automated network discovery
4. Configuration version control
5. Backup and restore functionality
