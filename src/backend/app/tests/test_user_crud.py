"""
Tests for user CRUD operations and role-based access control
"""
from typing import Dict, List, Tuple, Optional, Any
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from app.db.base import Base
from app.core.config import settings
from app.models.user import User
from app.models.role import UserRole
from app.db.session import get_async_session
from app.auth.users import get_user_manager, UserManager, fastapi_users
from app.main import app

# Test database URL
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

# Create async test engine
engine = create_async_engine(TEST_DATABASE_URL, poolclass=NullPool)
TestAsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Override the get_async_session dependency
async def override_get_async_session() -> AsyncSession:
    async with TestAsyncSessionLocal() as session:
        yield session

# Override dependency in app
app.dependency_overrides[get_async_session] = override_get_async_session

# Create test client
client = TestClient(app)

# Test users
test_admin = {
    "username": "testadmin",
    "password": "Admin123!",
    "email": "admin@example.com",
    "role": "admin",
    "is_superuser": True,
    "is_active": True,
    "is_verified": True,
}

test_manager = {
    "username": "testmanager",
    "password": "Manager123!",
    "email": "manager@example.com",
    "role": "manager",
    "is_superuser": False,
    "is_active": True,
    "is_verified": True,
}

test_user = {
    "username": "testuser",
    "password": "User123!",
    "email": "user@example.com",
    "role": "user",
    "is_superuser": False,
    "is_active": True,
    "is_verified": True,
}

@pytest.fixture
async def setup_test_db():
    """Create tables and test users in the test database"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async def _create_test_user(user_data: dict, user_manager: UserManager) -> User:
        """Helper to create a test user"""
        try:
            user = await user_manager.create(user_data)
            return user
        except Exception as e:
            pytest.fail(f"Failed to create test user: {e}")
    
    async with TestAsyncSessionLocal() as session:
        # Get user manager
        user_manager = UserManager(
            fastapi_users.user_db_model(session, User),
            fastapi_users.frontend_context,
        )
        
        # Create test users
        await _create_test_user(test_admin, user_manager)
        await _create_test_user(test_manager, user_manager)
        await _create_test_user(test_user, user_manager)
    
    yield
    
    # Teardown
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.mark.asyncio
async def test_get_users_admin(setup_test_db):
    """Test listing users as admin"""
    # Login as admin
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": test_admin["username"],
            "password": test_admin["password"],
            "grant_type": "password",
        },
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    
    # Get users
    response = client.get(
        f"{settings.API_V1_STR}/users/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 3  # admin, manager, user

@pytest.mark.asyncio
async def test_get_users_manager(setup_test_db):
    """Test listing users as manager (should be forbidden)"""
    # Login as manager
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": test_manager["username"],
            "password": test_manager["password"],
            "grant_type": "password",
        },
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    
    # Get users (should be forbidden)
    response = client.get(
        f"{settings.API_V1_STR}/users/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 403

@pytest.mark.asyncio
async def test_get_me(setup_test_db):
    """Test getting current user profile"""
    # Login as user
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": test_user["username"],
            "password": test_user["password"],
            "grant_type": "password",
        },
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    
    # Get own profile
    response = client.get(
        f"{settings.API_V1_STR}/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["username"] == test_user["username"]
    assert user_data["role"] == test_user["role"]

@pytest.mark.asyncio
async def test_create_user_admin(setup_test_db):
    """Test creating a user as admin"""
    # Login as admin
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": test_admin["username"],
            "password": test_admin["password"],
            "grant_type": "password",
        },
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    
    # Create new user
    new_user = {
        "username": "newuser",
        "password": "NewUser123!",
        "email": "newuser@example.com",
        "role": "user",
    }
    
    response = client.post(
        f"{settings.API_V1_STR}/users/",
        json=new_user,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    created_user = response.json()
    assert created_user["username"] == new_user["username"]
    assert created_user["role"] == new_user["role"]

@pytest.mark.asyncio
async def test_create_admin_as_manager(setup_test_db):
    """Test creating an admin user as manager (should be forbidden)"""
    # Login as manager
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": test_manager["username"],
            "password": test_manager["password"],
            "grant_type": "password",
        },
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    
    # Attempt to create admin user (should be forbidden)
    new_admin = {
        "username": "newadmin",
        "password": "Admin123!",
        "email": "newadmin@example.com",
        "role": "admin",
    }
    
    response = client.post(
        f"{settings.API_V1_STR}/users/",
        json=new_admin,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 403

@pytest.mark.asyncio
async def test_update_own_profile(setup_test_db):
    """Test updating own profile"""
    # Login as user
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": test_user["username"],
            "password": test_user["password"],
            "grant_type": "password",
        },
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    user_id = 3  # Assuming user ID is 3 (after admin and manager)
    
    # Update own profile
    profile_update = {
        "first_name": "Updated",
        "last_name": "User"
    }
    
    response = client.put(
        f"{settings.API_V1_STR}/users/{user_id}",
        json=profile_update,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    updated_user = response.json()
    assert updated_user["first_name"] == profile_update["first_name"]
    assert updated_user["last_name"] == profile_update["last_name"]

@pytest.mark.asyncio
async def test_user_cannot_change_role(setup_test_db):
    """Test regular user cannot change their role"""
    # Login as user
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": test_user["username"],
            "password": test_user["password"],
            "grant_type": "password",
        },
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    user_id = 3  # Assuming user ID is 3 (after admin and manager)
    
    # Attempt to change role (should be forbidden)
    role_update = {
        "role": "admin"
    }
    
    response = client.put(
        f"{settings.API_V1_STR}/users/{user_id}",
        json=role_update,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 403

@pytest.mark.asyncio
async def test_admin_assign_role(setup_test_db):
    """Test admin assigning role"""
    # Login as admin
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": test_admin["username"],
            "password": test_admin["password"],
            "grant_type": "password",
        },
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    user_id = 3  # Assuming user ID is 3 (user)
    
    # Assign manager role to user
    response = client.put(
        f"{settings.API_V1_STR}/roles/assign/{user_id}",
        json="manager",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    updated_user = response.json()
    assert updated_user["role"] == "manager"

@pytest.mark.asyncio
async def test_delete_user(setup_test_db):
    """Test admin deleting a user"""
    # Login as admin
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": test_admin["username"],
            "password": test_admin["password"],
            "grant_type": "password",
        },
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    user_id = 3  # Assuming user ID is 3 (user)
    
    # Delete user
    response = client.delete(
        f"{settings.API_V1_STR}/users/{user_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 204
    
    # Verify user is deleted
    response = client.get(
        f"{settings.API_V1_STR}/users/{user_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 404
