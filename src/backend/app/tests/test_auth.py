"""
Tests for authentication functionality
"""
import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_login(client: AsyncClient, test_user):
    """
    Test user login with valid credentials
    """
    response = await client.post(
        "/api/v1/jwt/login",
        data={
            "username": "testuser",
            "password": "password123",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_login_invalid_credentials(client: AsyncClient, test_user):
    """
    Test login with invalid credentials
    """
    response = await client.post(
        "/api/v1/jwt/login",
        data={
            "username": "testuser",
            "password": "wrongpassword",
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.asyncio
async def test_me_endpoint(client: AsyncClient, test_user_token):
    """
    Test getting current user information
    """
    response = await client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {test_user_token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == "testuser"
    assert response.json()["role"] == "user"

@pytest.mark.asyncio
async def test_me_unauthorized(client: AsyncClient):
    """
    Test accessing protected endpoint without token
    """
    response = await client.get("/api/v1/users/me")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.asyncio
async def test_invalid_token(client: AsyncClient):
    """
    Test using an invalid token
    """
    response = await client.get(
        "/api/v1/users/me",
        headers={"Authorization": "Bearer invalidtoken"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.asyncio
async def test_register_endpoint(client: AsyncClient):
    """
    Test user registration
    """
    response = await client.post(
        "/api/v1/register",
        json={
            "username": "newuser",
            "password": "newpassword123",
            "role": "user",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["username"] == "newuser"
    assert response.json()["role"] == "user"

@pytest.mark.asyncio
async def test_register_duplicate_username(client: AsyncClient, test_user):
    """
    Test registration with duplicate username
    """
    response = await client.post(
        "/api/v1/register",
        json={
            "username": "testuser",  # Already exists
            "password": "newpassword123",
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
