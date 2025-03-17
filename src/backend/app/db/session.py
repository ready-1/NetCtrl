"""
Database session setup and dependencies
"""
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Create async engine for PostgreSQL
engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True,
    echo=False  # Set to True for SQL query logging during development
)

# Create async session factory
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

async def get_async_session() -> AsyncSession:
    """
    FastAPI dependency that provides an async database session
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

async def get_engine():
    """
    Get the SQLAlchemy engine instance.
    
    This function is used for direct engine access when needed,
    primarily for database initialization and testing.
    """
    return engine
