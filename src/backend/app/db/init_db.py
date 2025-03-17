"""
Database initialization and superuser creation
"""
import logging
import asyncio
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from fastapi_users.password import PasswordHelper

from app.core.config import settings
from app.db.session import AsyncSessionLocal, get_engine
from app.db.base import Base
from app.models.user import User
from app.models.role import UserRole

logger = logging.getLogger(__name__)

MAX_RETRIES = 5
RETRY_DELAY = 2  # seconds

async def create_tables(engine):
    """Create database tables"""
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Database tables created successfully")
    except SQLAlchemyError as e:
        logger.error(f"Error creating database tables: {e}")
        raise

async def create_first_superuser(retries=MAX_RETRIES):
    """
    Create first superuser if no users exist
    
    This function will create an admin user if no users exist in the database.
    The admin credentials are configured in app.core.config settings:
        - FIRST_SUPERUSER_USERNAME: Username (default: "admin")
        - FIRST_SUPERUSER_PASSWORD: Password (default: "admin123")
        - FIRST_SUPERUSER_EMAIL: Email (optional)
    
    Override these defaults in production using environment variables:
        - NETCTRL_FIRST_SUPERUSER_USERNAME
        - NETCTRL_FIRST_SUPERUSER_PASSWORD
        - NETCTRL_FIRST_SUPERUSER_EMAIL
    """
    logger.info("Checking if superuser needs to be created")
    
    # Retry logic for database connections
    for attempt in range(retries):
        try:
            async with AsyncSessionLocal() as session:
                # Check if any users exist - using async query pattern
                result = await session.execute(select(User))
                user = result.scalars().first()
                
                if user:
                    logger.info("Users already exist, skipping superuser creation")
                    return
                
                # Create superuser if no users exist
                logger.info("No users found, creating first superuser")
                password_helper = PasswordHelper()
                password_hash = password_helper.hash(settings.FIRST_SUPERUSER_PASSWORD)
                
                # Create user directly
                user = User(
                    username=settings.FIRST_SUPERUSER_USERNAME,
                    email=settings.FIRST_SUPERUSER_EMAIL,
                    hashed_password=password_hash,
                    is_active=True,
                    is_verified=True,
                    is_superuser=True,
                    role=UserRole.ADMIN,
                )
                
                session.add(user)
                await session.commit()
                
                logger.info(f"Superuser created successfully with username: {settings.FIRST_SUPERUSER_USERNAME}")
                return
                
        except SQLAlchemyError as e:
            logger.warning(f"Database error on attempt {attempt + 1}/{retries}: {e}")
            if attempt < retries - 1:
                await asyncio.sleep(RETRY_DELAY)
            else:
                logger.error(f"Failed to create superuser after {retries} attempts")
                raise
        except Exception as e:
            logger.error(f"Unexpected error creating superuser: {e}")
            raise

async def init_db():
    """
    Initialize database with tables and superuser
    
    This function is called during application startup to ensure:
    1. All database tables are created
    2. A superuser exists for admin access
    """
    engine = await get_engine()
    await create_tables(engine)
    await create_first_superuser()
    logger.info("Database initialization completed")
