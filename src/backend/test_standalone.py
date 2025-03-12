"""
Standalone test with direct async client 
"""
import asyncio
import pytest
from fastapi import status
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport

from app.main import app

@pytest.mark.asyncio
async def test_root_endpoint():
    """Test the root endpoint directly."""
    # Create the client inside the test
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://testserver"
    ) as client:
        response = await client.get("/")
        assert response.status_code == status.HTTP_200_OK
        print(f"Root endpoint response: {response.json()}")

@pytest.mark.asyncio
async def test_health_endpoint():
    """Test the health endpoint directly."""
    # Create the client inside the test
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://testserver"
    ) as client:
        response = await client.get("/health")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"status": "ok"}
        print(f"Health check response: {response.json()}")
