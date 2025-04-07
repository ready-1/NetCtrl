# Product Context

This document explains the purpose of the NetCtrl project and user needs.

## Purpose

NetCtrl serves two primary purposes:

1. **Content Management and File Storage**: Provides a lightweight CMS with file management capabilities in an air-gapped environment, allowing users to store, organize, and share documents and files up to 5GB in size.

2. **Network Device Management**: Enables monitoring and configuration of Netgear M4300 switches through a centralized web interface, simplifying network administration in environments where direct internet access is unavailable.

The application is designed to operate in secure, air-gapped environments where reliability and self-contained operation are critical.

## User Needs

### Primary User Groups

1. **Content Managers**:
   - Need to create, edit, and organize textual content
   - Upload and manage large files up to 5GB
   - Access content on mobile devices
   - Work efficiently in various lighting conditions (dark/light mode)

2. **Network Administrators**:
   - Need to monitor Netgear M4300 switch status
   - Configure network settings without direct internet access
   - Maintain network configuration history
   - Access network management features from mobile devices

3. **System Administrators**:
   - Require containerized deployment for simplified management
   - Need centralized logging through syslog
   - Require secure, local-only authentication
   - Access to comprehensive documentation for maintenance

### Common User Requirements
- Mobile-first interface that works across devices
- Dark mode toggle for improved visibility in different environments
- Simple authentication mechanism
- Reliable operation in air-gapped environments
- Fast and efficient handling of large files

## Integration Points

### Internal Component Integration

1. **Django App ↔ PostgreSQL**:
   - Database connection for storing CMS content, file metadata, user accounts, and network configuration

2. **Django App ↔ Syslog**:
   - Logging integration for centralized monitoring and troubleshooting

3. **Nginx ↔ Django App**:
   - Reverse proxy connection for serving the application
   - Handling of large file uploads through chunked upload mechanism

4. **Django App ↔ File System**:
   - Storage and retrieval of files up to 5GB

### External System Integration

1. **NetCtrl ↔ Netgear M4300 Switches**:
   - Integration through OpenAPI client (Phase 2)
   - Configuration management and status monitoring
   - The OpenAPI specification will be used to generate a Python client library
