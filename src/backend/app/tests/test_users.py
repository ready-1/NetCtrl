"""
Tests for user management functionality
"""
import pytest
from httpx import AsyncClient
from fastapi import status

from app.core.config import settings
from app.models.role import UserRole
from app.schemas.user import UserCreate

# Constants for testing
TEST_USERNAME = "testuser"
TEST_PASSWORD = "testpassword123"

@pytest.mark.asyncio
async def test_create_user(client: AsyncClient, test_admin_token: str):
    """Test creating a new user as admin"""
    # Create a user
    response = await client.post(
        f"{settings.API_V1_STR}/auth/register",
        json={
            "username": TEST_USERNAME,
            "password": TEST_PASSWORD,
            "role": UserRole.USER.value,
            "is_active": True,
            "is_verified": True
        },
        headers={"Authorization": f"Bearer {test_admin_token}"}
    )
    
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["username"] == TEST_USERNAME
    assert "id" in data
    assert data["role"] == UserRole.USER.value
    assert "password" not in data
    
    return data

@pytest.mark.asyncio
async def test_get_user_by_id(client: AsyncClient, test_admin_token: str):
    """Test retrieving a user by ID"""
    # First create a user
    created_user = await test_create_user(client, test_admin_token)
    user_id = created_user["id"]
    
    # Get the user by ID
    response = await client.get(
        f"{settings.API_V1_STR}/users/{user_id}",
        headers={"Authorization": f"Bearer {test_admin_token}"}
    )
    
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == user_id
    assert data["username"] == TEST_USERNAME
    assert data["role"] == UserRole.USER.value

@pytest.mark.asyncio
async def test_list_users(client: AsyncClient, test_admin_token: str):
    """Test listing all users"""
    # Get users list
    response = await client.get(
        f"{settings.API_V1_STR}/users/",
        headers={"Authorization": f"Bearer {test_admin_token}"}
    )
    
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    # Should include at least the admin user and our test user
    assert len(data) >= 2
    
    # Verify the test user is in the list
    test_user = next((user for user in data if user["username"] == TEST_USERNAME), None)
    assert test_user is not None
    assert test_user["role"] == UserRole.USER.value

@pytest.mark.asyncio
async def test_update_user_role(client: AsyncClient, test_admin_token: str):
    """Test updating a user's role"""
    # First create a user
    created_user = await test_create_user(client, test_admin_token)
    user_id = created_user["id"]
    
    # Update the user's role
    response = await client.put(
        f"{settings.API_V1_STR}/roles/assign/{user_id}",
        json=UserRole.MANAGER.value,
        headers={"Authorization": f"Bearer {test_admin_token}"}
    )
    
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == user_id
    assert data["role"] == UserRole.MANAGER.value

@pytest.mark.asyncio
async def test_permissions(client: AsyncClient, test_admin_token: str):
    """Test getting user permissions"""
    response = await client.get(
        f"{settings.API_V1_STR}/roles/my-permissions",
        headers={"Authorization": f"Bearer {test_admin_token}"}
    )
    
    assert response.status_code == status.HTTP_200_OK
    permissions = response.json()
    assert permissions["can_view_all_users"] is True
    assert permissions["can_create_users"] is True
    assert permissions["can_update_users"] is True
    assert permissions["can_delete_users"] is True
    assert permissions["can_assign_roles"] is True

@pytest.mark.asyncio
async def test_delete_user(client: AsyncClient, test_admin_token: str):
    """Test deleting a user"""
    # First create a user
    created_user = await test_create_user(client, test_admin_token)
    user_id = created_user["id"]
    
    # Delete the user
    response = await client.delete(
        f"{settings.API_V1_STR}/users/{user_id}",
        headers={"Authorization": f"Bearer {test_admin_token}"}
    )
    
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
    # Try to get the deleted user (should return 404)
    response = await client.get(
        f"{settings.API_V1_STR}/users/{user_id}",
        headers={"Authorization": f"Bearer {test_admin_token}"}
    )
    
    assert response.status_code == status.HTTP_404_NOT_FOUND
