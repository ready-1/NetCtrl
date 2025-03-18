"""
Pytest fixtures for testing
"""
import asyncio
import os
import tempfile
from io import BytesIO
import pytest
from typing import AsyncGenerator, Dict, Any, List, Optional, Callable
from fastapi import FastAPI
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.db.base import Base
from app.db.session import get_async_session
from app.main import app
from app.models.user import User
from app.models.role import UserRole
from app.models.content import Content, ContentType, ContentStatus
from app.schemas.content import ContentCreate
from app.services.content import ContentService
from app.services.file import FileService
from app.auth.users import get_user_manager, UserManager, auth_backend

from app.tests.test_config import get_test_config

# Get test configuration (SQLite or PostgreSQL based on environment)
test_config = get_test_config()

# Helper function to fix coroutine awaiting issues
async def get_client_and_tokens():
    """
    Helper function to get client and all tokens properly awaited
    Returns a tuple of (client, admin_token, editor_token, user_token)
    """
    # This is a patched version that properly awaits all coroutines
    # to fix the 'coroutine was never awaited' warnings
    from app.tests.conftest import client, test_admin_token, test_editor_token, test_user_token
    
    client_instance = await client
    admin_token = await test_admin_token
    editor_token = await test_editor_token
    user_token = await test_user_token
    
    return client_instance, admin_token, editor_token, user_token

# Helper function to properly await any fixture
async def await_fixture(fixture):
    """
    Helper to properly await a fixture that might be a coroutine
    """
    if hasattr(fixture, "__await__"):
        return await fixture
    return fixture

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
async def test_db_session(test_engine):
    """
    Create a test database session with transaction rollback
    """
    # Handle async generator for test_engine
    engine = test_engine
    if hasattr(test_engine, "__anext__"):
        try:
            engine = await test_engine.__anext__()
        except StopAsyncIteration:
            pass
            
    # Create a connection and begin a transaction
    connection = await engine.connect()
    transaction = await connection.begin()
    
    # Create a session factory bound to this connection
    TestingSessionLocal = sessionmaker(
        connection, 
        class_=AsyncSession, 
        expire_on_commit=False,
    )
    
    # Get a session
    session = TestingSessionLocal()
    
    # Return the session for the test to use
    yield session
    
    # Cleanup after the test is done
    await session.close()
    await transaction.rollback()
    await connection.close()

@pytest.fixture
async def client(test_db_session):
    """
    Create a test client with overridden dependencies
    
    This fixture returns an AsyncClient for testing FastAPI endpoints.
    It overrides the database session dependency with the test session.
    """
    # Handle async generator for test_db_session
    session = test_db_session
    if hasattr(test_db_session, "__anext__"):
        try:
            session = await test_db_session.__anext__()
        except StopAsyncIteration:
            pass
            
    # Override the dependency for database session
    async def override_get_db():
        # Return the actual session, not a generator
        yield session
    
    app.dependency_overrides[get_async_session] = override_get_db
    
    # Create the client with ASGI transport to avoid network calls
    async_client = AsyncClient(
        transport=ASGITransport(app=app), 
        base_url="http://test"
    )
    
    # Yield the client to work with pytest's async fixtures
    yield async_client
    
    # Clear dependency overrides after test
    app.dependency_overrides.clear()

@pytest.fixture
async def user_db(test_db_session):
    """
    Get a SQLAlchemy user database adapter for tests with username support
    """
    from app.db.user_db import SQLAlchemyUserDatabaseWithUsername
    
    # Create and return the user database with the session and username support
    return SQLAlchemyUserDatabaseWithUsername(test_db_session, User)

@pytest.fixture
async def user_manager(user_db):
    """
    Create a user manager for tests
    """
    # Await the user_db fixture
    user_db_instance = await user_db
    
    # Return the user manager directly
    return UserManager(user_db_instance)

@pytest.fixture
async def test_user(user_manager):
    """
    Create a test user
    """
    # Await the user_manager fixture
    user_manager_instance = await user_manager
    
    try:
        # Check if user already exists
        user = await user_manager_instance.get_by_username("testuser")
        if user:
            return user
    except Exception:
        pass
        
    # Create user using proper Pydantic model
    from app.schemas.user import UserCreate
    
    user_create = UserCreate(
        username="testuser",
        email=None,
        password="Password123!",  # Match password complexity requirements
        is_active=True,
        is_verified=True,
        role=UserRole.USER
    )
    
    # Create the user
    user = await user_manager_instance.create(user_create)
    return user

@pytest.fixture
async def test_editor(user_manager):
    """
    Create a test editor user
    """
    # Await the user_manager fixture
    user_manager_instance = await user_manager
    
    try:
        # Check if editor already exists
        user = await user_manager_instance.get_by_username("testeditor")
        if user:
            return user
    except Exception:
        pass

    # Create editor using proper Pydantic model
    from app.schemas.user import UserCreate
    
    editor_create = UserCreate(
        username="testeditor",
        email=None,
        password="Editor123!",  # Match password complexity requirements
        is_active=True,
        is_verified=True,
        is_superuser=False,
        role=UserRole.EDITOR
    )
    
    # Create the editor user
    editor = await user_manager_instance.create(editor_create)
    return editor

@pytest.fixture
async def test_admin(user_manager):
    """
    Create a test admin user
    """
    # Await the user_manager fixture
    user_manager_instance = await user_manager
    
    try:
        # Check if admin already exists
        user = await user_manager_instance.get_by_username("testadmin")
        if user:
            return user
    except Exception:
        pass

    # Create admin using proper Pydantic model
    from app.schemas.user import UserCreate
    
    admin_create = UserCreate(
        username="testadmin",
        email=None,
        password="Admin123!",  # Match password complexity requirements
        is_active=True,
        is_verified=True,
        is_superuser=True,
        role=UserRole.ADMIN
    )
    
    # Create the admin user
    admin = await user_manager_instance.create(admin_create)
    return admin

@pytest.fixture
async def test_user_token(client, test_user):
    """
    Get an authentication token for the test user
    """
    # Get the test user and client
    user = await test_user
    client_instance = await client
    
    # Prepare form data for OAuth2 login
    form_data = {
        "username": "testuser",
        "password": "Password123!",  # Match the password used in test_user creation
        "grant_type": "password"  # Required parameter
    }
    
    # Get token
    response = await client_instance.post(
        "/api/v1/jwt/login",
        data=form_data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    return response.json()["access_token"]

@pytest.fixture
async def test_editor_token(client, test_editor):
    """
    Get an authentication token for the test editor
    """
    # Get the test editor and client
    editor = await test_editor
    client_instance = await client
    
    # Prepare form data for OAuth2 login
    form_data = {
        "username": "testeditor",
        "password": "Editor123!",  # Match the password used in test_editor creation
        "grant_type": "password"  # Required parameter
    }
    
    # Get token
    response = await client_instance.post(
        "/api/v1/jwt/login",
        data=form_data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    return response.json()["access_token"]

@pytest.fixture
async def test_admin_token(client, test_admin):
    """
    Get an authentication token for the test admin
    """
    # Get the test admin and client
    admin = await test_admin
    client_instance = await client
    
    # Prepare form data for OAuth2 login
    form_data = {
        "username": "testadmin",
        "password": "Admin123!",  # Match the password used in test_admin creation
        "grant_type": "password"  # Required parameter
    }
    
    # Get token
    response = await client_instance.post(
        "/api/v1/jwt/login",
        data=form_data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    return response.json()["access_token"]

@pytest.fixture
async def create_content(test_db_session, test_admin):
    """
    Factory fixture to create test content with specified attributes
    
    Returns a function that creates content with given parameters
    """
    # Await the admin user
    admin = await test_admin
    
    async def _create_content(**kwargs):
        """
        Inner function that creates a content item with given parameters
        
        Args:
            **kwargs: Content attributes to override defaults
            
        Returns:
            Content: Created content object
        """
        # Default content data
        content_data = {
            "title": "Test Content",
            "content_type": ContentType.PAGE.value,
            "body": "This is test content",
            "status": ContentStatus.DRAFT.value,
            "metadata": {"tags": ["test"]},
        }
        
        # Override with provided kwargs
        content_data.update(kwargs)
        
        # Create the content in the database directly
        content_service = ContentService(test_db_session)
        
        content_create = ContentCreate(**content_data)
        content = await content_service.create_content(content_create, user_id=admin.id)
        
        return content
    
    return _create_content

@pytest.fixture
async def sample_contents(create_content):
    """
    Create a set of sample content items for testing
    """
    # Get the create_content function
    create_content_func = await create_content
    
    contents = []
    # Create a page
    contents.append(await create_content_func(
        title="Sample Page",
        content_type=ContentType.PAGE.value,
        status=ContentStatus.PUBLISHED.value
    ))
    
    # Create a post
    contents.append(await create_content_func(
        title="Sample Post",
        content_type=ContentType.POST.value,
        status=ContentStatus.PUBLISHED.value
    ))
    
    # Create a draft document
    contents.append(await create_content_func(
        title="Draft Document",
        content_type=ContentType.DOCUMENT.value,
        status=ContentStatus.DRAFT.value
    ))
    
    return contents

@pytest.fixture
async def temp_file() -> AsyncGenerator[Dict[str, Any], None]:
    """
    Create a temporary test file for upload testing
    
    Yields a dictionary with file info and cleans up after test
    """
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp:
        temp.write(b"This is test file content")
        temp_path = temp.name
    
    # Yield file info
    yield {
        "path": temp_path,
        "name": os.path.basename(temp_path),
        "content_type": "text/plain",
        "size": os.path.getsize(temp_path)
    }
    
    # Clean up the file
    if os.path.exists(temp_path):
        os.unlink(temp_path)

@pytest.fixture
async def uploaded_file(client, test_admin_token, temp_file):
    """
    Create an uploaded file in the system
    
    Returns the file metadata after upload
    """
    # Get the temp file, client, and token
    file_info = await temp_file
    client_instance = await client
    token = await test_admin_token
    
    # Create file data for upload
    with open(file_info["path"], "rb") as f:
        file_content = f.read()
    
    files = {"file": (file_info["name"], BytesIO(file_content), file_info["content_type"])}
    
    # Upload the file
    response = await client_instance.post(
        "/api/v1/files/",
        files=files,
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 201
    return response.json()
