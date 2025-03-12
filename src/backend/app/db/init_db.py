"""
Database initialization and first superuser creation
"""
import logging
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.config import settings
from app.db.session import AsyncSessionLocal
from app.db.base import Base
from app.models.user import User
from app.models.role import UserRole
from app.auth.users import get_user_manager

logger = logging.getLogger(__name__)

async def create_tables(engine):
    """
    Create database tables if they don't exist
    """
    from sqlalchemy.ext.asyncio import AsyncEngine
    
    logger.info("Creating database tables")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database tables created")

async def create_first_superuser():
    """
    Create first superuser if it doesn't exist
    """
    if not settings.FIRST_SUPERUSER_PASSWORD:
        logger.warning("Superuser password not set, skipping superuser creation")
        return
    
    try:
        async with AsyncSessionLocal() as session:
            # Check if any users exist
            result = await session.execute(select(User))
            user = result.scalars().first()
            
            if user:
                logger.info("Users already exist, skipping superuser creation")
                return
            
            logger.info("Creating initial superuser")
            
            # Create user manager
            async for user_manager in get_user_manager(session):
                # Directly create a user with raw dict instead of using models
                # The base manager expects different attribute names
                user_data = {
                    "username": settings.FIRST_SUPERUSER_USERNAME,
                    "email": None,  # Email is optional in our setup
                    "hashed_password": None,  # Will be hashed by the manager
                    "password": settings.FIRST_SUPERUSER_PASSWORD,  # This is what's required
                    "is_active": True,
                    "is_verified": True,
                    "is_superuser": True,
                    "role": UserRole.ADMIN,
                }
                
                # Use create with safe=False to allow creating admin user
                await user_manager.create(user_data, safe=False)
                
            logger.info("Superuser created successfully")
            
    except Exception as e:
        logger.error(f"Error creating superuser: {e}")
