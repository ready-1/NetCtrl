import pytest
import asyncio
from httpx import AsyncClient
from fastapi import FastAPI
from httpx._transports.asgi import ASGITransport

from app.main import app

@pytest.mark.asyncio
async def test_simple_client():
    """
    Verify we can create and use an AsyncClient directly
    """
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        assert response.status_code == 200
