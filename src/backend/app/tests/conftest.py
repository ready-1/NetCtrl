"""
Pytest fixtures for testing
"""
import asyncio
import pytest
from typing import AsyncGenerator, Dict, Any
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.db.base import Base
from app.db.session import get_async_session
from app.main import app
from app.models.user import User
from app.models.role import UserRole
from app.auth.users import get_user_manager, UserManager, auth_backend

from app.tests.test_config import get_test_config

# Get test configuration (SQLite or PostgreSQL based on environment)
test_config = get_test_config()

@pytest.fixture(scope="session")
def event_loop():
    """
    Create a new event loop for the test session
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def test_engine():
    """
    Create a test database engine
    """
    engine = create_async_engine(
        test_config["DB_URL"],
        connect_args=test_config["DB_CONNECT_ARGS"]
    )
    
    # Create all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield engine
    
    # Drop all tables after tests
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    
    await engine.dispose()

@pytest.fixture
async def test_db_session(test_engine) -> AsyncGenerator[AsyncSession, None]:
    """
    Create a test database session with transaction rollback
    """
    # Create a connection and begin a transaction
    connection = await test_engine.connect()
    transaction = await connection.begin()
    
    # Create a session factory bound to this connection
    TestingSessionLocal = sessionmaker(
        connection, 
        class_=AsyncSession, 
        expire_on_commit=False,
    )
    
    # Get a session
    session = TestingSessionLocal()
    
    try:
        yield session
    finally:
        # Close and rollback the session after the test
        await session.close()
        await transaction.rollback()
        await connection.close()

@pytest.fixture
async def client(test_db_session) -> AsyncClient:
    """
    Create a test client with overridden dependencies
    """
    # Override the dependency for database session
    async def override_get_db():
        yield test_db_session
    
    app.dependency_overrides[get_async_session] = override_get_db
    
    # Create a test client
    client = AsyncClient(app=app, base_url="http://test")
    
    try:
        yield client
    finally:
        await client.aclose()
        # Clear overrides
        app.dependency_overrides.clear()

@pytest.fixture
async def user_manager(test_db_session) -> UserManager:
    """
    Create a user manager for tests
    """
    return UserManager(test_db_session)

@pytest.fixture
async def test_user(user_manager) -> User:
    """
    Create a test user
    """
    user_data = {
        "username": "testuser",
        "email": None,
        "password": "password123",
        "is_active": True,
        "is_verified": True,
        "role": UserRole.USER,
    }
    
    return await user_manager.create(user_data)

@pytest.fixture
async def test_admin(user_manager) -> User:
    """
    Create a test admin user
    """
    admin_data = {
        "username": "testadmin",
        "email": None,
        "password": "password123",
        "is_active": True,
        "is_verified": True,
        "is_superuser": True,
        "role": UserRole.ADMIN,
    }
    
    return await user_manager.create(admin_data)

@pytest.fixture
async def test_user_token(client: AsyncClient, test_user) -> str:
    """
    Get an authentication token for the test user
    """
    response = await client.post(
        "/api/v1/jwt/login",
        data={
            "username": "testuser",
            "password": "password123",
        },
    )
    return response.json()["access_token"]

@pytest.fixture
async def test_admin_token(client: AsyncClient, test_admin) -> str:
    """
    Get an authentication token for the test admin
    """
    response = await client.post(
        "/api/v1/jwt/login",
        data={
            "username": "testadmin",
            "password": "password123",
        },
    )
    return response.json()["access_token"]
