# User CRUD Implementation Plan

## Overview
This document outlines the implementation plan for user management CRUD (Create, Read, Update, Delete) operations with role-based access control (RBAC) for the NetCtrl CMS backend.

## Goals
1. Complete the superuser creation functionality
2. Implement user management REST API endpoints
3. Add role management functionality 
4. Ensure proper RBAC is applied to all endpoints
5. Create comprehensive tests for all user operations

## Components

### 1. User Schema Refinement
- Create complete Pydantic schemas for user operations:
  - `UserRead`: Schema for reading user data (excludes password)
  - `UserCreate`: Schema for creating new users
  - `UserUpdate`: Schema for updating existing users
  - `UserWithRoles`: Extended schema that includes role information

### 2. User API Routes
- Implement the following endpoints:
  - `GET /api/users`: List all users (admin only)
  - `GET /api/users/{user_id}`: Get a specific user
  - `POST /api/users`: Create a new user
  - `PUT /api/users/{user_id}`: Update a user
  - `DELETE /api/users/{user_id}`: Delete a user
  - `GET /api/users/me`: Get current user profile

### 3. Role Management
- Implement the following endpoints:
  - `GET /api/roles`: List all available roles
  - `PUT /api/users/{user_id}/role`: Update a user's role (admin only)

### 4. Superuser Creation Fix
- Fix the remaining issue with superuser creation
- Ensure first admin user can be created during initialization
- Add environment variable configuration for initial admin credentials

### 5. RBAC Implementation
- Ensure access to endpoints is restricted based on user role:
  - Admin: Full access to all endpoints
  - Manager: Access to most endpoints except role management and user deletion
  - User: Access only to their own user information

### 6. Testing
- Create unit tests for all user management operations
- Implement integration tests to verify RBAC functionality
- Add tests for edge cases and error handling

## Implementation Steps

1. **Fix Superuser Creation**
   - Update the superuser creation flow to properly handle user creation
   - Test the fix to ensure superusers can be created

2. **Implement User Schemas**
   - Create or update Pydantic schemas in `app/schemas/user.py`
   - Ensure proper validation and field definitions

3. **Create API Routes**
   - Implement user routes in `app/api/routes/users.py`
   - Add role management endpoints to the same file or a separate `app/api/routes/roles.py`

4. **Implement RBAC**
   - Update the authentication system to properly check roles for each endpoint
   - Use FastAPI dependencies to enforce role-based access

5. **Testing**
   - Create test files for each component
   - Implement comprehensive test coverage

## Dependencies
- FastAPI-Users library (already set up)
- JWT authentication system (already implemented)
- Database models for User and Role (already created)

## Estimated Timeline
- Superuser creation fix: 1-2 hours
- User schemas and API routes: 3-4 hours
- Role management: 2-3 hours
- RBAC implementation: 2-3 hours
- Testing: 3-4 hours

## Success Criteria
- All user management endpoints are accessible and working correctly
- Role-based access control properly restricts unauthorized access
- Superuser creation works during system initialization
- All tests pass
