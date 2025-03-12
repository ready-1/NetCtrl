"""
Basic tests to ensure the test infrastructure works properly
"""
import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_basic_endpoint(client: AsyncClient):
    """Test a simple endpoint to ensure fixture setup works."""
    # Verify that the client fixture works with the ASGI transport
    response = await client.get("/")
    assert response.status_code == status.HTTP_200_OK
    # Print debug info
    print(f"Root endpoint response: {response.json()}")
    
    # Also try health check
    health_response = await client.get("/health")
    assert health_response.status_code == status.HTTP_200_OK
    assert health_response.json() == {"status": "ok"}
