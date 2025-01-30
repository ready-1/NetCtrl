# M4300 Switch Management System - Project Brief


## 1. Project Overview
A Django-based web application for managing M4300 network switches in an airgapped environment. The system will provide switch monitoring, configuration management, and port profile management through a responsive, dark-themed interface.

## 2. Technical Stack

### Backend
- Django 5.0+
- Django REST Framework
- Channels (for async tasks)
- M4300 API Client (custom)
- PostgreSQL (production) / SQLite (development)
- Redis (for caching and async tasks)

### Frontend
- Bootstrap 5 (locally served)
- Chart.js (for metrics)
- htmx (for dynamic updates)
- Font Awesome (locally served)

### Deployment
- Docker
- Gunicorn
- Nginx

## 3. Core Features

### 3.1 Authentication & Authorization

#### User Roles
- Non-Privileged Users:
  - View switch status
  - View configurations
  - Change port profiles
  - View audit logs
- Privileged Users (Django Staff):
  - All non-privileged actions
  - Add/remove switches
  - Create/modify configurations
  - Push configurations
  - Manage users
- Superuser (Django Admin):
  - All system administration tasks

#### Audit Logging
- User actions
- Configuration changes
- Switch status changes
- System events

### 3.2 Switch Management

#### Switch Operations
- Add/Remove switches
- View switch status
- Configure switch settings
- Backup configurations
- Push configurations
- Port profile management

#### Configuration Management
- Version control for configurations
- Multiple default configurations
- Export/Import configurations (JSON format)
- Configuration comparison
- Flat network configuration push
- Configuration templates
- Configuration rollback support

### 3.3 Dashboard & Monitoring

#### Status Dashboard
- Switch status overview
- Ping status monitoring (5-second intervals, configurable)
- Quick links to switch management
- Status history graphs
- Alert indicators
- Real-time notifications

#### Metrics
- Switch uptime
- Port status
- Configuration status
- Recent changes
- System health

## 4. Database Schema

### 4.1 Core Models

\`\`\`python
class Switch(models.Model):
    name = models.CharField()
    ip_address = models.GenericIPAddressField()
    credentials = models.ForeignKey(SwitchCredentials)
    status = models.CharField()
    last_seen = models.DateTimeField()
    config = models.ForeignKey(Configuration)

class Configuration(models.Model):
    name = models.CharField()
    version = models.CharField()
    content = models.JSONField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(User)
    is_default = models.BooleanField()

class PortProfile(models.Model):
    name = models.CharField()
    settings = models.JSONField()
    switch = models.ForeignKey(Switch)
    port_number = models.IntegerField()

class AuditLog(models.Model):
    user = models.ForeignKey(User)
    action = models.CharField()
    details = models.JSONField()
    timestamp = models.DateTimeField()
    switch = models.ForeignKey(Switch, null=True)

class StatusHistory(models.Model):
    switch = models.ForeignKey(Switch)
    status = models.CharField()
    timestamp = models.DateTimeField()
    metrics = models.JSONField()
\`\`\`

### 4.2 Additional Models

\`\`\`python
class ConfigurationTemplate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    template = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User)

    class Meta:
        ordering = ['-updated_at']

class ConfigurationVersion(models.Model):
    configuration = models.ForeignKey(Configuration)
    version_number = models.IntegerField()
    content = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    comment = models.TextField()

    class Meta:
        unique_together = ['configuration', 'version_number']

class BulkPortOperation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ]

    switches = models.ManyToManyField(Switch)
    port_profile = models.ForeignKey(PortProfile)
    port_numbers = ArrayField(models.IntegerField())
    status = models.CharField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User)
    results = models.JSONField(default=dict)

class Notification(models.Model):
    LEVEL_CHOICES = [
        ('info', 'Information'),
        ('warning', 'Warning'),
        ('error', 'Error'),
        ('success', 'Success')
    ]

    user = models.ForeignKey(User)
    level = models.CharField(choices=LEVEL_CHOICES)
    message = models.TextField()
    switch = models.ForeignKey(Switch, null=True)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class ConfigurationRollback(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ]

    switch = models.ForeignKey(Switch)
    from_version = models.ForeignKey(ConfigurationVersion, related_name='rollback_from')
    to_version = models.ForeignKey(ConfigurationVersion, related_name='rollback_to')
    status = models.CharField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
\`\`\`

## 5. UI/UX Design

### 5.1 Design Principles
- Dark mode by default
- Responsive design (iPhone minimum)
- Collapsible navigation
- Quick access to common tasks
- Clear status indicators
- Consistent layout across pages

### 5.2 Key Interfaces
- Dashboard:
  - Switch status grid
  - Quick actions
  - Alert panel
  - Metrics graphs
- Switch Management:
  - Switch details
  - Port configuration
  - Status monitoring
  - Configuration management
- Configuration:
  - Version history
  - Diff viewer
  - Template management
  - Import/Export tools
- User Management:
  - User list
  - Role management
  - Audit log viewer

## 6. Development Workflow

### 6.1 Environment Setup
- Development:
  - SQLite database
  - Debug mode enabled
  - Local asset serving
  - Docker development container
- Production:
  - PostgreSQL database
  - Redis cache
  - Nginx for static files
  - Docker Compose deployment

### 6.2 Testing Strategy
- Unit Tests:
  - Model validation
  - Business logic
  - API endpoints
- Integration Tests:
  - Switch communication
  - Configuration management
  - User workflows
- UI Tests:
  - Responsive design
  - Browser compatibility
  - User interactions

## 7. Future Enhancements
- TFTP/SSH support for firmware updates
- Advanced metric collection
- Configuration templates
- Batch operations
- API documentation

## 8. Configuration Settings

### 8.1 Status Monitoring
\`\`\`python
# settings.py
SWITCH_MONITORING = {
    'polling_interval': 5,  # seconds
    'retry_attempts': 3,
    'retry_delay': 1,  # seconds
    'notification_channels': ['web', 'email'],
    'status_history_retention': 30,  # days
}
\`\`\`

## 9. Browser Support
- Primary Support:
  - Chrome-based browsers (Chrome, Edge, Brave)
  - Safari
- Mobile Support:
  - iOS Safari
  - Android Chrome

## 10. Security Considerations
- Standard Django security practices
- Token-based API authentication
- CSRF protection
- XSS prevention
- SQL injection protection
- Regular security updates
