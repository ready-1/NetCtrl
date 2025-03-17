"""
Database initialization and superuser creation
"""
import logging
from sqlalchemy.future import select
from sqlalchemy.sql import text
from fastapi_users.password import PasswordHelper

from app.core.config import settings
from app.db.session import AsyncSessionLocal
from app.db.base import Base
from app.models.user import User
from app.models.role import UserRole

logger = logging.getLogger(__name__)

async def create_tables(engine):
    """Create database tables"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database tables created")

async def create_first_superuser():
    """Create first superuser if no users exist"""
    if not settings.FIRST_SUPERUSER_PASSWORD:
        logger.warning("Superuser password not set, skipping creation")
        return
    
    try:
        async with AsyncSessionLocal() as session:
            # Check if any users exist - fixed async query
            result = await session.execute(select(User))
            user_exists = result.scalars().first() is not None
            
            if user_exists:
                logger.info("Users already exist, skipping superuser creation")
                return
            
            # Create superuser
            password_hash = PasswordHelper().hash(settings.FIRST_SUPERUSER_PASSWORD)
            
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
            
            logger.info("Superuser created with username: %s", settings.FIRST_SUPERUSER_USERNAME)
            
    except Exception as e:
        logger.error("Failed to create superuser: %s", e)
        raise
