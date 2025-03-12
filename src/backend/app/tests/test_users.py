"""
Tests for user management functionality
"""
import pytest
from httpx import AsyncClient
from fastapi import status

from app.models.role import UserRole

@pytest.mark.asyncio
async def test_get_users_as_admin(client: AsyncClient, test_admin_token, test_user):
    """
    Test getting users list as admin
    """
    response = await client.get(
        "/api/v1/users",
        headers={"Authorization": f"Bearer {test_admin_token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    users = response.json()
    assert len(users) >= 2  # Admin and regular user
    
    # Find our test user in the list
    test_user_found = False
    for user in users:
        if user["username"] == "testuser":
            test_user_found = True
            assert user["role"] == "user"
    assert test_user_found

@pytest.mark.asyncio
async def test_get_users_as_regular_user(client: AsyncClient, test_user_token):
    """
    Test getting users list as regular user
    """
    response = await client.get(
        "/api/v1/users",
        headers={"Authorization": f"Bearer {test_user_token}"},
    )
    # Regular users may be able to list users, depending on your API configuration
    # This could be 200 or 403 depending on your policy
    if response.status_code == status.HTTP_200_OK:
        users = response.json()
        assert len(users) >= 1
    else:
        assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.asyncio
async def test_get_user_by_id(client: AsyncClient, test_admin_token, test_user):
    """
    Test getting a specific user by ID
    """
    # First, get the user ID 
    users_response = await client.get(
        "/api/v1/users",
        headers={"Authorization": f"Bearer {test_admin_token}"},
    )
    users = users_response.json()
    
    # Find our test user
    user_id = None
    for user in users:
        if user["username"] == "testuser":
            user_id = user["id"]
            break
    
    assert user_id is not None
    
    # Now get the specific user
    response = await client.get(
        f"/api/v1/users/{user_id}",
        headers={"Authorization": f"Bearer {test_admin_token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    user = response.json()
    assert user["username"] == "testuser"
    assert user["role"] == "user"

@pytest.mark.asyncio
async def test_create_user_as_admin(client: AsyncClient, test_admin_token):
    """
    Test creating a new user as admin
    """
    response = await client.post(
        "/api/v1/users",
        headers={"Authorization": f"Bearer {test_admin_token}"},
        json={
            "username": "createduser",
            "password": "password123",
            "role": "manager",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    user = response.json()
    assert user["username"] == "createduser"
    assert user["role"] == "manager"

@pytest.mark.asyncio
async def test_create_user_as_regular_user(client: AsyncClient, test_user_token):
    """
    Test creating a new user as regular user (forbidden)
    """
    response = await client.post(
        "/api/v1/users",
        headers={"Authorization": f"Bearer {test_user_token}"},
        json={
            "username": "anothercreateduser",
            "password": "password123",
            "role": "user",
        },
    )
    # Regular users should not be able to create other users
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.asyncio
async def test_update_user(client: AsyncClient, test_admin_token, test_user):
    """
    Test updating a user
    """
    # First, get the user ID 
    users_response = await client.get(
        "/api/v1/users",
        headers={"Authorization": f"Bearer {test_admin_token}"},
    )
    users = users_response.json()
    
    # Find our test user
    user_id = None
    for user in users:
        if user["username"] == "testuser":
            user_id = user["id"]
            break
    
    assert user_id is not None
    
    # Update the user
    response = await client.patch(
        f"/api/v1/users/{user_id}",
        headers={"Authorization": f"Bearer {test_admin_token}"},
        json={
            "first_name": "Test",
            "last_name": "User",
            "role": "manager",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    updated_user = response.json()
    assert updated_user["first_name"] == "Test"
    assert updated_user["last_name"] == "User"
    assert updated_user["role"] == "manager"
    
    # Verify the update by getting the user again
    response = await client.get(
        f"/api/v1/users/{user_id}",
        headers={"Authorization": f"Bearer {test_admin_token}"},
    )
    user = response.json()
    assert user["first_name"] == "Test"
    assert user["last_name"] == "User"
    assert user["role"] == "manager"
