# Comprehensive User CRUD Implementation Plan

## Overview
This document outlines the implementation plan for user management CRUD (Create, Read, Update, Delete) operations with role-based access control (RBAC) for the NetCtrl CMS backend, with detailed integration aspects.

## Goals
1. Complete the superuser creation functionality
2. Implement user management REST API endpoints
3. Add role management functionality 
4. Ensure proper RBAC is applied to all endpoints
5. Create comprehensive tests for all user operations

## Integration Considerations

### Data Schema Integration

#### User Schemas (Existing with Enhancements Needed)
- **UserRead**: 
  - Types: `username` (str), `first_name` (Optional[str]), `last_name` (Optional[str]), `role` (UserRole enum), `email` (Optional[EmailStr])
  - Format: JSON response objects
  - Usage: For GET responses, excluding sensitive data

- **UserCreate**:
  - Types: `username` (str, min_length=3, max_length=50), `password` (str, with complexity validation), `email` (Optional[EmailStr]), `role` (UserRole, default=USER), `first_name` (Optional[str]), `last_name` (Optional[str])
  - Validation: Username must be alphanumeric, password needs complexity rules
  - Required: `username`, `password`
  - Optional: `email`, `first_name`, `last_name`, `role` (admin can set, others default to USER)

- **UserUpdate**:
  - All fields optional to support partial updates
  - Same validation rules as UserCreate
  - Role updates restricted by permission

- **UserWithRoles**:
  - Extended from UserRead
  - Additional audit fields: `created_at`, `updated_at`, `last_login`
  - Format: Detailed JSON for admin views

#### Database Model Synchronization
- Ensure model fields match schema fields
- Type conversion between SQLAlchemy types and Pydantic types
- Default values synchronized

### API Endpoint Integration

#### User Endpoints
| Endpoint | Method | Input | Output | Authorization | Status |
|----------|--------|-------|--------|--------------|--------|
| `/api/v1/users` | GET | Pagination params, role filter | List[UserRead] | Admin only | ✅ Implemented |
| `/api/v1/users/{user_id}` | GET | Path param | UserWithRoles | Admin, Manager, Owner | ✅ Implemented |
| `/api/v1/users` | POST | UserCreate body | UserRead | Admin, Manager | ❌ Needed |
| `/api/v1/users/{user_id}` | PUT | UserUpdate body | UserRead | Admin, Manager, Owner | ❌ Needed |
| `/api/v1/users/{user_id}` | DELETE | Path param | None | Admin, Owner | ✅ Implemented |
| `/api/v1/users/me` | GET | None | UserWithRoles | Any authenticated | ✅ Implemented |

#### Role Endpoints
| Endpoint | Method | Input | Output | Authorization | Status |
|----------|--------|-------|--------|--------------|--------|
| `/api/v1/roles` | GET | None | List[str] | Any | ✅ Implemented |
| `/api/v1/roles/{role}/users` | GET | Path param | List[UserRead] | Admin only | ✅ Implemented |
| `/api/v1/roles/assign/{user_id}` | PUT | Role body | UserWithRoles | Admin only | ✅ Implemented |
| `/api/v1/roles/my-permissions` | GET | None | Dict[str, bool] | Any authenticated | ✅ Implemented |

### Role-Based Access Control Integration

#### Permission Matrix
| Action | Admin | Manager | User |
|--------|-------|---------|------|
| View all users | ✅ | ❌ | ❌ |
| View specific user | ✅ | ✅ | Self only |
| Create user | ✅ | ✅ | ❌ |
| Update user | ✅ | ✅ | Self only |
| Delete user | ✅ | ❌ | Self only |
| Assign roles | ✅ | ❌ | ❌ |
| Set user as admin | ✅ | ❌ | ❌ |
| View permissions | ✅ | ✅ | ✅ |

### Error Handling & Status Codes

| Scenario | Status Code | Response Format |
|----------|-------------|-----------------|
| Success (GET) | 200 | JSON object(s) |
| Success (POST) | 201 | Created object |
| Success (PUT) | 200 | Updated object |
| Success (DELETE) | 204 | No content |
| Validation Error | 422 | `{"detail": [validation errors]}` |
| Not Found | 404 | `{"detail": "Resource not found"}` |
| Permission Denied | 403 | `{"detail": "Not enough permissions"}` |
| Authentication Error | 401 | `{"detail": "Not authenticated"}` |

## Components

### 1. User Schema Refinement
- **Status**: ✅ Mostly Complete
- **Tasks**:
  - ✅ Create UserRead schema
  - ✅ Create UserCreate schema
  - ✅ Create UserUpdate schema
  - ✅ Create UserWithRoles schema
  - ❌ Add password complexity validation

### 2. User API Routes
- **Status**: ⚠️ Partially Complete
- **Tasks**:
  - ✅ `GET /api/users`: List all users (admin only)
  - ✅ `GET /api/users/{user_id}`: Get a specific user
  - ❌ `POST /api/users`: Create a new user
  - ❌ `PUT /api/users/{user_id}`: Update a user
  - ✅ `DELETE /api/users/{user_id}`: Delete a user
  - ✅ `GET /api/users/me`: Get current user profile

### 3. Role Management
- **Status**: ✅ Complete
- **Tasks**:
  - ✅ `GET /api/roles`: List all available roles
  - ✅ `GET /api/roles/{role}/users`: List users with specific role
  - ✅ `PUT /api/roles/assign/{user_id}`: Update a user's role (admin only)
  - ✅ `GET /api/roles/my-permissions`: Get current user permissions

### 4. Superuser Creation
- **Status**: ⚠️ Needs Review
- **Tasks**:
  - ❌ Review superuser creation during initialization
  - ❌ Add environment variable configuration for initial admin credentials
  - ❌ Add documentation for superuser setup

### 5. RBAC Implementation
- **Status**: ⚠️ Partially Complete
- **Tasks**:
  - ✅ Implement role-based dependencies
  - ✅ Add role checking to existing endpoints
  - ❌ Add role validation to new endpoints
  - ❌ Add comprehensive error messages

### 6. Testing
- **Status**: ❌ Not Started
- **Tasks**:
  - ❌ Create unit tests for all user management operations
  - ❌ Implement integration tests to verify RBAC functionality
  - ❌ Add tests for edge cases and error handling

## Implementation Steps

### Phase 1: Complete User Management Endpoints
1. Implement `POST /api/users` endpoint for user creation
2. Implement `PUT /api/users/{user_id}` endpoint for user updates
3. Add password complexity validation to UserCreate schema
4. Add proper permissions checks for all endpoints

### Phase 2: Fix Superuser Creation
1. Review current initialization flow
2. Add environment variables for initial admin credentials
3. Test superuser creation workflow

### Phase 3: Testing and Documentation
1. Implement unit tests for all endpoints
2. Create integration tests for RBAC
3. Document all endpoints and permission requirements
4. Add examples for endpoint usage

## Dependencies
- FastAPI-Users library (already set up)
- JWT authentication system (already implemented)
- Database models for User and Role (already created)

## Success Criteria
- All user management endpoints are accessible and working correctly
- Role-based access control properly restricts unauthorized access
- Superuser creation works during system initialization
- All tests pass
- Documentation is complete and accurate
