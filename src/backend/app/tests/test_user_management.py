"""
Tests for user management functions and role-based access control
"""
import pytest
from fastapi.testclient import TestClient

from app.core.config import settings
from app.main import app

# Create a test client that interacts directly with the app (no real HTTP requests)
client = TestClient(app)

def test_login_admin():
    """Test login as admin"""
    login_response = client.post(
        f"{settings.API_V1_STR}/jwt/login",
        data={
            "username": "admin",
            "password": "admin123",
            "grant_type": "password",
        },
    )
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
    return login_response.json()["access_token"]

def test_get_current_user():
    """Test getting current user profile"""
    token = test_login_admin()
    
    response = client.get(
        f"{settings.API_V1_STR}/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["username"] == "admin"
    assert user_data["role"] == "admin"

def test_create_and_get_user():
    """Test creating a user and then retrieving it"""
    token = test_login_admin()
    
    # Create new user
    new_user = {
        "username": "testuser",
        "password": "TestUser123!",
        "email": "test@example.com",
        "role": "user",
        "first_name": "Test",
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
    return user_id

def test_update_user():
    """Test updating a user"""
    token = test_login_admin()
    user_id = test_create_and_get_user()
    
    # Update user
    update_data = {
        "first_name": "Updated",
        "last_name": "Name"
    }
    
    update_response = client.put(
        f"{settings.API_V1_STR}/users/{user_id}",
        json=update_data,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert update_response.status_code == 200
    updated_user = update_response.json()
    assert updated_user["first_name"] == update_data["first_name"]
    assert updated_user["last_name"] == update_data["last_name"]

def test_password_complexity():
    """Test password complexity validation"""
    token = test_login_admin()
    
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

def test_role_permissions():
    """Test role-based permissions"""
    token = test_login_admin()
    
    # Get permissions for admin
    response = client.get(
        f"{settings.API_V1_STR}/roles/my-permissions",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    permissions = response.json()
    assert permissions["can_view_all_users"] == True
    assert permissions["can_assign_roles"] == True
