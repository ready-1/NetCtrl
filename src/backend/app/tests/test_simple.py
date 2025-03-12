"""
Simple auth test to confirm fixture setup
"""
import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_simple_auth(client: AsyncClient):
    """
    Simple test to check if the client fixture works properly
    """
    # Test the root endpoint first
    root_response = await client.get("/")
    assert root_response.status_code == status.HTTP_200_OK
    
    # Try to access a protected endpoint (should fail without auth)
    protected_response = await client.get("/api/v1/users/me")
    assert protected_response.status_code == status.HTTP_401_UNAUTHORIZED
