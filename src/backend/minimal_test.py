"""
Minimal test with inline fixtures
"""
import pytest
import asyncio
from fastapi import status
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport

from app.main import app

@pytest.fixture
def event_loop():
    """Create a new event loop for each test."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
async def test_client():
    """Create a test client with ASGI transport."""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://testserver"
    ) as client:
        yield client

@pytest.mark.asyncio
async def test_root_endpoint(test_client):
    """Test the root endpoint."""
    response = await test_client.get("/")
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.asyncio
async def test_health_endpoint(test_client):
    """Test the health endpoint."""
    response = await test_client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok"}
