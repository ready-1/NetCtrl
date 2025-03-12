# FastAPI Backend Authentication Implementation Plan

This document outlines the implementation plan for the backend authentication system using FastAPI-Users with Role-Based Access Control (RBAC).

## Table of Contents
- [FastAPI Backend Authentication Implementation Plan](#fastapi-backend-authentication-implementation-plan)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Core Implementation Components](#core-implementation-components)
    - [User Model with Role Field](#user-model-with-role-field)
    - [User Schemas](#user-schemas)
    - [FastAPI-Users Setup](#fastapi-users-setup)
    - [API Routes](#api-routes)
    - [Main Application](#main-application)
  - [Configuration](#configuration)
  - [Database Setup](#database-setup)
  - [Testing Framework](#testing-framework)
    - [Test Examples](#test-examples)
  - [Docker Setup](#docker-setup)
  - [Implementation Steps](#implementation-steps)

## Project Structure

```
src/backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py           # Application configuration
│   │   ├── security.py         # Security utilities
│   │   └── dependencies.py     # Common dependencies
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py             # Base SQLAlchemy model
│   │   ├── session.py          # Database session setup
│   │   └── init_db.py          # Database initialization script
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py             # User model with role field
│   │   └── role.py             # Role enum and constants
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py             # User Pydantic schemas
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── users.py            # FastAPI-Users configuration
│   │   └── permissions.py      # Role-based permission system
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py             # API dependencies
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py         # Authentication routes
│   │   │   ├── users.py        # User management routes
│   │   │   └── roles.py        # Role management routes
│   └── tests/
│       ├── __init__.py
│       ├── conftest.py         # Test fixtures
│       ├── test_auth.py        # Authentication tests
│       ├── test_users.py       # User management tests
│       └── test_roles.py       # Role management tests
├── scripts/
│   └── init_db.py              # Initial database setup script
└── alembic/                    # Database migration files
```

## Core Implementation Components

### User Model with Role Field

```python
# app/models/role.py
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"

# app/models/user.py
from typing import Optional, List
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String, Enum, Boolean, Integer

from app.db.base import Base
from app.models.role import UserRole

class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String(length=320), unique=True, index=True, nullable=True)
    username = Column(String(length=50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(length=1024), nullable=False)
    
    # Profile fields
    first_name = Column(String(length=50), nullable=True)
    last_name = Column(String(length=50), nullable=True)
    
    # Role field - single role per user for simplicity
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)
    
    # FastAPI-Users fields
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=True, nullable=False)  # Default to true since we skip verification
    is_superuser = Column(Boolean, default=False, nullable=False)
```

### User Schemas

```python
# app/schemas/user.py
from typing import Optional
from pydantic import Field, validator
from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate

from app.models.role import UserRole

class UserRead(BaseUser[int]):
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: UserRole
    
    class Config:
        orm_mode = True

class UserCreate(BaseUserCreate):
    username: str = Field(..., min_length=3, max_length=50)
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    role: UserRole = UserRole.USER
    
    @validator('username')
    def username_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v

class UserUpdate(BaseUserUpdate):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    role: Optional[UserRole] = None
    
    @validator('username')
    def username_alphanumeric(cls, v):
        if v is not None and not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v
```

### FastAPI-Users Setup

```python
# app/auth/users.py
from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, IntegerIDMixin
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport
from fastapi_users.db import SQLAlchemyUserDatabase

from app.core.config import settings
from app.db.session import get_async_session
from app.models.user import User
from app.models.role import UserRole
from sqlalchemy.ext.asyncio import AsyncSession

# User database adapter
async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

# User manager for handling user operations
class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY
    
    # Override to handle user creation
    async def on_after_register(self, user: User, request: Optional[Request] = None):
        # Auto-verify users since we don't have email
        user.is_verified = True
        print(f"User {user.id} has registered.")
    
    # Override to handle user login
    async def on_after_login(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} logged in.")
    
    # Check if user has specific role
    async def has_role(self, user: User, role: UserRole) -> bool:
        return user.role == role or user.role == UserRole.ADMIN

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

# JWT authentication
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.SECRET_KEY,
        lifetime_seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )

# Authentication backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

# FastAPIUsers instance
fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

# Export current user dependencies
current_active_user = fastapi_users.current_user(active=True)
current_verified_user = fastapi_users.current_user(active=True, verified=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

# Role-based dependencies
def current_user_with_role(role: UserRole):
    async def current_user_with_role_dependency(
        user_manager=Depends(get_user_manager),
        user=Depends(current_active_user),
    ):
        if await user_manager.has_role(user, role):
            return user
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Role {role} required",
        )
    return current_user_with_role_dependency

# Export role-based dependencies
current_admin = current_user_with_role(UserRole.ADMIN)
current_manager = current_user_with_role(UserRole.MANAGER)
```

### API Routes

```python
# app/api/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException

from app.auth.users import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()

# Include FastAPI-Users routes
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/register",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

# app/api/routes/roles.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.auth.users import current_admin
from app.models.user import User
from app.models.role import UserRole
from app.schemas.user import UserRead

router = APIRouter(prefix="/roles", tags=["roles"])

@router.get("/", response_model=List[str])
async def list_roles():
    """List all available roles"""
    return [role.value for role in UserRole]

@router.get("/{role}/users", response_model=List[UserRead])
async def list_users_by_role(
    role: UserRole,
    current_user: User = Depends(current_admin)
):
    """List all users with a specific role (admin only)"""
    # Implementation would query users with specific role
    # This would depend on the database session
    pass
```

### Main Application

```python
# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes import auth, users, roles
from app.db.init_db import create_first_superuser

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set up CORS
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Include routers
app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(roles.router, prefix=settings.API_V1_STR)

@app.on_event("startup")
async def startup_event():
    await create_first_superuser()

@app.get("/health")
def health_check():
    return {"status": "ok"}
```

## Configuration

```python
# app/core/config.py
from typing import List, Union
from pydantic import AnyHttpUrl, BaseSettings, validator

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    # Database settings
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: str = None
    
    # CORS settings
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    # Superuser settings
    FIRST_SUPERUSER_USERNAME: str = "admin"
    FIRST_SUPERUSER_PASSWORD: str = None
    
    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: str, values: dict) -> str:
        if v:
            return v
        return f"postgresql+asyncpg://{values['POSTGRES_USER']}:{values['POSTGRES_PASSWORD']}@{values['POSTGRES_SERVER']}/{values['POSTGRES_DB']}"
    
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
```

## Database Setup

```python
# app/db/session.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session():
    async with SessionLocal() as session:
        yield session

# app/db/init_db.py
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.config import settings
from app.db.session import SessionLocal
from app.models.user import User
from app.models.role import UserRole
from app.auth.users import get_user_manager, UserManager

logger = logging.getLogger(__name__)

async def create_first_superuser():
    """Create first superuser if it doesn't exist"""
    if not settings.FIRST_SUPERUSER_PASSWORD:
        logger.warning("Superuser password not set, skipping initial superuser creation")
        return
    
    try:
        async with SessionLocal() as session:
            # Check if any users exist
            result = await session.execute(select(User))
            user = result.scalars().first()
            
            if user:
                logger.info("Users already exist, skipping superuser creation")
                return
            
            logger.info("Creating initial superuser")
            
            async for user_manager in get_user_manager(session):
                user_manager: UserManager
                
                # Create admin user
                await user_manager.create(
                    {
                        "username": settings.FIRST_SUPERUSER_USERNAME,
                        "email": None,  # Email is optional in our setup
                        "password": settings.FIRST_SUPERUSER_PASSWORD,
                        "is_active": True,
                        "is_verified": True,
                        "is_superuser": True,
                        "role": UserRole.ADMIN,
                    }
                )
                
            logger.info("Superuser created successfully")
            
    except Exception as e:
        logger.error(f"Error creating superuser: {e}")
```

## Testing Framework

```python
# app/tests/conftest.py
import asyncio
import pytest
from typing import AsyncGenerator, Generator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.db.base import Base
from app.db.session import get_async_session
from app.main import app
from app.models.user import User
from app.models.role import UserRole
from app.auth.users import get_user_manager, UserManager

# Use SQLite for tests
TEST_SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def test_engine():
    engine = create_async_engine(TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield engine
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    
    await engine.dispose()

@pytest.fixture
async def db_session(test_engine) -> AsyncGenerator[AsyncSession, None]:
    """Get a testing session with rollback after test."""
    connection = await test_engine.connect()
    transaction = await connection.begin()
    
    async_session = sessionmaker(connection, expire_on_commit=False, class_=AsyncSession)
    session = async_session()
    
    yield session
    
    await session.close()
    await transaction.rollback()
    await connection.close()

@pytest.fixture
async def client(db_session) -> AsyncGenerator[AsyncClient, None]:
    """Get a test client with overridden dependencies."""
    
    async def override_get_db():
        yield db_session
    
    app.dependency_overrides[get_async_session] = override_get_db
    
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
    
    app.dependency_overrides.clear()

@pytest.fixture
async def test_user_manager(db_session) -> AsyncGenerator[UserManager, None]:
    """Get a user manager for tests."""
    yield UserManager(db_session)

@pytest.fixture
async def test_user(test_user_manager) -> User:
    """Create a test user."""
    user_data = {
        "username": "testuser",
        "email": None,
        "password": "password123",
        "is_active": True,
        "is_verified": True,
        "role": UserRole.USER,
    }
    return await test_user_manager.create(user_data)

@pytest.fixture
async def test_admin(test_user_manager) -> User:
    """Create a test admin user."""
    admin_data = {
        "username": "testadmin",
        "email": None,
        "password": "password123",
        "is_active": True,
        "is_verified": True,
        "is_superuser": True,
        "role": UserRole.ADMIN,
    }
    return await test_user_manager.create(admin_data)

@pytest.fixture
async def test_user_token(client, test_user) -> str:
    """Get a token for the test user."""
    response = await client.post(
        "/api/v1/auth/jwt/login",
        data={
            "username": "testuser",
            "password": "password123",
        },
    )
    return response.json()["access_token"]

@pytest.fixture
async def test_admin_token(client, test_admin) -> str:
    """Get a token for the test admin."""
    response = await client.post(
        "/api/v1/auth/jwt/login",
        data={
            "username": "testadmin",
            "password": "password123",
        },
    )
    return response.json()["access_token"]
```

### Test Examples

```python
# app/tests/test_auth.py
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_login(client: AsyncClient, test_user):
    """Test user login."""
    response = await client.post(
        "/api/v1/auth/jwt/login",
        data={
            "username": "testuser",
            "password": "password123",
        },
    )
    assert response.status_code == 200
    assert "access_token" in response.json()

@pytest.mark.asyncio
async def test_me(client: AsyncClient, test_user_token):
    """Test getting current user information."""
    response = await client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {test_user_token}"},
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["role"] == "user"

# app/tests/test_users.py
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_user(client: AsyncClient, test_admin_token):
    """Test creating a new user (admin only)."""
    response = await client.post(
        "/api/v1/users",
        headers={"Authorization": f"Bearer {test_admin_token}"},
        json={
            "username": "newuser",
            "password": "password123",
            "role": "user",
        },
    )
    assert response.status_code == 201
    assert response.json()["username"] == "newuser"
    assert response.json()["role"] == "user"

@pytest.mark.asyncio
async def test_create_user_unauthorized(client: AsyncClient, test_user_token):
    """Test that regular users cannot create users."""
    response = await client.post(
        "/api/v1/users",
        headers={"Authorization": f"Bearer {test_user_token}"},
        json={
            "username": "newuser2",
            "password": "password123",
            "role": "user",
        },
    )
    assert response.status_code == 403

# app/tests/test_roles.py
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_list_roles(client: AsyncClient):
    """Test listing all available roles."""
    response = await client.get("/api/v1/roles/")
    assert response.status_code == 200
    assert "admin" in response.json()
    assert "manager" in response.json()
    assert "user" in response.json()

@pytest.mark.asyncio
async def test_list_users_by_role(client: AsyncClient, test_admin_token):
    """Test listing users by role (admin only)."""
    response = await client.get(
        "/api/v1/roles/user/users",
        headers={"Authorization": f"Bearer {test_admin_token}"},
    )
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["role"] == "user"
```

## Docker Setup

Ensure your `Dockerfile` properly handles installing dependencies and setting up the environment variables:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create a non-root user
RUN useradd -m appuser
USER appuser

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

For running tests in the container:

```bash
# Container test command
pytest -xvs app/tests/
```

## Implementation Steps

1. **Setup Project Structure**:
   - Create directories and files
   - Set up core configuration

2. **Implement User Models and Authentication**:
   - Implement user model with role field
   - Set up FastAPI-Users with JWT authentication
   - Configure role-based permission system

3. **Create API Routes and Business Logic**:
   - Implement authentication routes
   - Set up user management routes
   - Add role management functionality

4. **Database Setup and Initialization**:
   - Configure database connection
   - Implement initial data setup for first admin

5. **Testing**:
   - Write unit tests for auth, users, and roles
   - Set up test fixtures for database and HTTP client

6. **Documentation and Deployment**:
   - Document API endpoints with OpenAPI
   - Set up Docker configuration
   - Configure environment variables
