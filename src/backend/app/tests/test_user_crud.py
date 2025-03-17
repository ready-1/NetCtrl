"""
Tests for user CRUD operations and role-based access control
"""
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.core.config import settings
from app.models.user import User
from app.models.role import UserRole
from app.main import app

# Test users data
test_admin_data = {
    "username": "testadmin",
    "password": "Admin123!",
    "email": "admin@example.com",
    "role": "admin",
    "is_superuser": True,
    "is_active": True,
    "is_verified": True,
}

test_manager_data = {
    "username": "testmanager",
    "password": "Manager123!",
    "email": "manager@example.com",
    "role": "manager",
    "is_superuser": False,
    "is_active": True,
    "is_verified": True,
}

test_user_data = {
    "username": "testuser",
    "password": "User123!",
    "email": "user@example.com",
    "role": "user",
    "is_superuser": False,
    "is_active": True,
    "is_verified": True,
}

# Create test client
client = TestClient(app, base_url="http://localhost")

@pytest.mark.asyncio
async def test_get_users_admin():
    """Test listing users as admin"""
    # Login as admin
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": "admin",
            "password": "admin123",
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
    assert len(users) >= 1  # At least the admin user should exist

@pytest.mark.asyncio
async def test_create_user_admin():
    """Test creating a user as admin"""
    # Login as admin
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": "admin",
            "password": "admin123",
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
async def test_get_me():
    """Test getting current user profile"""
    # Login as admin (using default admin)
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": "admin",
            "password": "admin123",
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
    assert user_data["username"] == "admin"
    assert user_data["role"] == "admin"

@pytest.mark.asyncio
async def test_password_complexity():
    """Test password complexity validation"""
    # Login as admin
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": "admin",
            "password": "admin123",
            "grant_type": "password",
        },
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    
    # Try to create user with weak password
    weak_password_user = {
        "username": "weakpassuser",
        "password": "password",  # No uppercase, digits or special chars
        "email": "weak@example.com",
        "role": "user",
    }
    
    response = client.post(
        f"{settings.API_V1_STR}/users/",
        json=weak_password_user,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 422  # Validation error
    assert "password" in response.text.lower()  # Error should mention password

@pytest.mark.asyncio
async def test_create_and_get_user():
    """Test creating a user and then retrieving it"""
    # Login as admin
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": "admin",
            "password": "admin123",
            "grant_type": "password",
        },
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    
    # Create new user
    new_user = {
        "username": "retrieveuser",
        "password": "Retrieve123!",
        "email": "retrieve@example.com",
        "role": "user",
        "first_name": "Retrieve",
        "last_name": "User",
    }
    
    create_response = client.post(
        f"{settings.API_V1_STR}/users/",
        json=new_user,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert create_response.status_code == 201
    created_user = create_response.json()
    user_id = created_user["id"]
    
    # Get the created user
    get_response = client.get(
        f"{settings.API_V1_STR}/users/{user_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert get_response.status_code == 200
    retrieved_user = get_response.json()
    assert retrieved_user["username"] == new_user["username"]
    assert retrieved_user["first_name"] == new_user["first_name"]
    assert retrieved_user["last_name"] == new_user["last_name"]
