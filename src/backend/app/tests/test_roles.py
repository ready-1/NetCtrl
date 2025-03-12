"""
Tests for role-based access control functionality
"""
import pytest
from httpx import AsyncClient
from fastapi import status

from app.models.role import UserRole

@pytest.mark.asyncio
async def test_list_roles(client: AsyncClient):
    """
    Test listing all available roles (public endpoint)
    """
    response = await client.get("/api/v1/roles/")
    assert response.status_code == status.HTTP_200_OK
    roles = response.json()
    assert "admin" in roles
    assert "manager" in roles
    assert "user" in roles

@pytest.mark.asyncio
async def test_list_users_by_role_as_admin(client: AsyncClient, test_admin_token, test_user):
    """
    Test listing users by role as admin
    """
    response = await client.get(
        f"/api/v1/roles/{UserRole.USER}/users",
        headers={"Authorization": f"Bearer {test_admin_token}"},
    )
    assert response.status_code == status.HTTP_200_OK
    users = response.json()
    assert len(users) > 0
    assert users[0]["role"] == "user"

@pytest.mark.asyncio
async def test_list_users_by_role_as_user(client: AsyncClient, test_user_token):
    """
    Test listing users by role as regular user (forbidden)
    """
    response = await client.get(
        f"/api/v1/roles/{UserRole.USER}/users",
        headers={"Authorization": f"Bearer {test_user_token}"},
    )
    # Regular users should not be able to list users by role
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.asyncio
async def test_list_users_by_role_unauthorized(client: AsyncClient):
    """
    Test listing users by role without authentication
    """
    response = await client.get(f"/api/v1/roles/{UserRole.USER}/users")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
