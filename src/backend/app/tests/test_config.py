"""
Test configuration with support for both SQLite and PostgreSQL
"""
import os
from typing import Dict, Any

# Default SQLite configuration for quick tests
SQLITE_TEST_CONFIG = {
    "DB_URL": "sqlite+aiosqlite:///:memory:",
    "DB_CONNECT_ARGS": {"check_same_thread": False},
    "REQUIRES_CREATE_ALL": True,
}

# PostgreSQL configuration for production-like tests
POSTGRES_TEST_CONFIG = {
    "DB_URL": "postgresql+asyncpg://postgres:postgres@{server}:{port}/{db}",
    "DB_CONNECT_ARGS": {},
    "REQUIRES_CREATE_ALL": True,
}

def get_test_config() -> Dict[str, Any]:
    """
    Get test configuration based on environment
    
    Returns SQLite config by default, but PostgreSQL if TEST_WITH_POSTGRES=1 
    environment variable is set.
    """
    if os.environ.get("TEST_WITH_POSTGRES", "0") == "1":
        # Get PostgreSQL connection details from environment
        server = os.environ.get("POSTGRES_SERVER", "database")
        port = os.environ.get("POSTGRES_PORT", "5432")
        user = os.environ.get("POSTGRES_USER", "postgres")
        password = os.environ.get("POSTGRES_PASSWORD", "postgres")
        db = os.environ.get("POSTGRES_DB", "test_netctrl")
        
        # Format the connection URL
        db_url = POSTGRES_TEST_CONFIG["DB_URL"].format(
            server=server,
            port=port,
            db=db
        )
        
        # Return the modified config
        return {
            "DB_URL": db_url.replace("{user}", user).replace("{password}", password),
            "DB_CONNECT_ARGS": POSTGRES_TEST_CONFIG["DB_CONNECT_ARGS"],
            "REQUIRES_CREATE_ALL": POSTGRES_TEST_CONFIG["REQUIRES_CREATE_ALL"],
        }
    return SQLITE_TEST_CONFIG

# For Docker-specific PostgreSQL test settings
DOCKER_POSTGRES_TEST_CONFIG = {
    "DB_URL": "postgresql+asyncpg://{user}:{password}@{server}:{port}/{db}",
    "DB_CONNECT_ARGS": {},
    "REQUIRES_CREATE_ALL": True,
}

def get_docker_test_config() -> Dict[str, Any]:
    """
    Get Docker-specific test configuration
    
    Used when testing from within the Docker container against external PostgreSQL.
    """
    # Get PostgreSQL connection details from environment
    server = os.environ.get("POSTGRES_SERVER", "test_db")
    port = os.environ.get("POSTGRES_PORT", "5432")
    user = os.environ.get("POSTGRES_USER", "postgres")
    password = os.environ.get("POSTGRES_PASSWORD", "postgres")
    db = os.environ.get("POSTGRES_DB", "test_netctrl")
    
    # Format the connection URL
    db_url = DOCKER_POSTGRES_TEST_CONFIG["DB_URL"].format(
        server=server,
        port=port,
        db=db,
        user=user,
        password=password
    )
    
    return {
        "DB_URL": db_url,
        "DB_CONNECT_ARGS": DOCKER_POSTGRES_TEST_CONFIG["DB_CONNECT_ARGS"],
        "REQUIRES_CREATE_ALL": DOCKER_POSTGRES_TEST_CONFIG["REQUIRES_CREATE_ALL"],
    }
