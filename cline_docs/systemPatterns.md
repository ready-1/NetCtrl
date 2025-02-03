# System Patterns

## Architecture Overview
1. Backend Framework
   - Django 5.0+ for core application
   - Django REST Framework for API endpoints
   - Channels for async tasks
   - PostgreSQL (production) / SQLite (development)

2. Frontend Architecture
   - Server-side rendered templates
   - Bootstrap 5 for responsive layout
   - HTMX for dynamic updates
   - Chart.js for metrics visualization

3. Authentication & Authorization
   - Django's built-in authentication
   - Custom User model with role-based permissions
   - JWT tokens for API authentication
   - Session-based auth for web interface

## Key Design Patterns
1. Model-View-Template (MVT)
   - Models: Django ORM for data structure
   - Views: Class-based views for logic
   - Templates: Django templates for presentation

2. Service Layer
   - Switch management services
   - Configuration management services
   - Port management services
   - Monitoring services

3. Repository Pattern
   - Switch repository
   - Configuration repository
   - Port profile repository
   - Audit log repository

## Code Organization
1. Core Apps
   - core: Base functionality and shared components
   - authentication: User management and auth
   - switches: Switch management
   - netctrl: Network control features

2. Directory Structure
   ```
   ├── core/
   │   ├── models.py      # Base models
   │   ├── views.py       # Core views
   │   └── utils/         # Shared utilities
   ├── switches/
   │   ├── models.py      # Switch models
   │   ├── views.py       # Switch views
   │   └── templates/     # Switch templates
   └── templates/
       ├── base.html      # Base template
       └── components/    # Shared components
   ```

## Implementation Patterns
1. View Patterns
   - Class-based views for consistency
   - Mixins for shared functionality
   - Permission mixins for access control

2. Model Patterns
   - Abstract base classes for common fields
   - Model managers for complex queries
   - Custom model methods for business logic

3. Template Patterns
   - Base template inheritance
   - Component-based structure
   - Consistent naming conventions

## Security Patterns
1. Authentication
   - Token-based API auth
   - Session-based web auth
   - Role-based access control

2. Data Protection
   - Form validation
   - Input sanitization
   - CSRF protection

3. Audit Trail
   - Comprehensive logging
   - Action tracking
   - User activity monitoring

## Testing Patterns
1. Test Organization
   - Unit tests per app
   - Integration tests
   - End-to-end tests

2. Test Types
   - Model tests
   - View tests
   - Form tests
   - API tests

3. Test Data
   - Factories for test data
   - Fixtures for common scenarios
   - Mock objects for external services
