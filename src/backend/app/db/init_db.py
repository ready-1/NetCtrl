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
from app.schemas.user import UserCreate

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
            # Check if any users exist - use the correct table name "user"
            result = await session.execute(select(User))
            existing_user = result.scalars().first()
            
            if existing_user:
                logger.info("Users already exist, skipping superuser creation")
                return
            
            logger.info("Creating initial superuser")
            
            # Create user manager
            async for user_manager in get_user_manager(session):
                # Use a proper UserCreate instance
                from fastapi_users.schemas import CreateUserProtocol
                from app.schemas.user import UserCreate
                
                # Create a user with our custom UserCreate model
                user_create = UserCreate(
                    username=settings.FIRST_SUPERUSER_USERNAME,
                    email=settings.FIRST_SUPERUSER_EMAIL,
                    password=settings.FIRST_SUPERUSER_PASSWORD,
                    is_active=True,
                    is_verified=True,
                    is_superuser=True,
                    role=UserRole.ADMIN
                )
                
                try:
                    # Manually create the user to bypass the model validation issues
                    hashed_password = await user_manager.password_helper.hash(settings.FIRST_SUPERUSER_PASSWORD)
                    user_dict = {
                        "username": settings.FIRST_SUPERUSER_USERNAME,
                        "email": settings.FIRST_SUPERUSER_EMAIL,
                        "hashed_password": hashed_password,
                        "is_active": True,
                        "is_verified": True,
                        "is_superuser": True,
                        "role": UserRole.ADMIN,
                    }
                    
                    # Create the user directly in the database
                    user = User(**user_dict)
                    session.add(user)
                    await session.commit()
                    await session.refresh(user)
                    
                    logger.info(f"Superuser created with ID: {user.id}")
                except Exception as e:
                    logger.error(f"Error in user creation: {e}", exc_info=True)
                    raise
                
            logger.info("Superuser created successfully")
            
    except Exception as e:
        logger.error(f"Error creating superuser: {e}")
