# Product Context

## Purpose
NetCtrl is a Django-based web application designed for managing M4300 network switches in an airgapped environment. It provides a centralized interface for switch monitoring, configuration management, and port profile management through a responsive, dark-themed interface.

## Problems Solved
1. Switch Management Complexity
   - Simplifies management of multiple M4300 switches
   - Provides unified interface for both in-band and out-band management
   - Centralizes configuration and monitoring

2. Airgapped Environment Support
   - Works in environments without internet connectivity
   - All assets served locally
   - Self-contained deployment

3. Configuration Management
   - Version control for switch configurations
   - Configuration comparison and rollback
   - Template-based configuration management

4. Security & Audit
   - Role-based access control
   - Comprehensive audit logging
   - Secure authentication system

## Core Functionality
1. Switch Management
   - Add/Remove switches
   - Monitor switch status
   - In-band and out-band access (port 49151)
   - Port profile management

2. User Roles
   - Non-Privileged: View status, change port profiles
   - Privileged: Add/remove switches, manage configurations
   - Superuser: Full system administration

3. Monitoring
   - Real-time status monitoring
   - Configuration status tracking
   - Port status monitoring
   - System health metrics

4. Configuration
   - Version-controlled configurations
   - Configuration templates
   - Backup and restore
   - Configuration comparison

## Target Users
1. Network Administrators
   - Primary users managing switch infrastructure
   - Need full control over switch configurations
   - Require audit capabilities

2. Network Operators
   - Day-to-day switch operations
   - Port profile management
   - Status monitoring

3. Security Teams
   - Audit log review
   - Security configuration verification
   - Access control management
