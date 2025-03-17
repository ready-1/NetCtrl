"""
FastAPI-Users configuration with role-based authentication
"""
import logging
from typing import Optional, Dict, Any, List, Tuple
from fastapi import Depends, Request, HTTPException, status, Response
from fastapi_users import BaseUserManager, FastAPIUsers, IntegerIDMixin, models, schemas
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, Strategy
from fastapi_users.authentication.strategy.base import StrategyDestroyNotSupportedError
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import text
import jwt
from datetime import datetime, timedelta

from app.core.config import settings
from app.db.session import get_async_session
from app.models.user import User
from app.models.role import UserRole
from app.auth.custom_jwt import CustomJWTStrategy

# Configure logger
logger = logging.getLogger(__name__)

# User database adapter
async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    """Provides SQLAlchemy user database adapter"""
    yield SQLAlchemyUserDatabase(session, User)

# User manager
class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """Custom user manager with username-based login and role-based access control"""
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY
    
    async def get_by_username(self, username: str) -> Optional[User]:
        """Get user by username"""
        user_db = self.user_db
        if isinstance(user_db, SQLAlchemyUserDatabase):
            statement = select(User).where(User.username == username)
            result = await user_db.session.execute(statement)
            user = result.scalars().first()
            
            if user is None:
                raise self.not_exists_exception
                
            return user
        return None
    
    async def on_after_register(self, user: User, request: Optional[Request] = None):
        """Auto-verify users on registration"""
        user.is_verified = True
        logger.info("User %s registered successfully", user.id)
    
    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        """Handle password reset requests"""
        logger.info("User %s requested password reset", user.id)
    
    async def has_role(self, user: User, role: UserRole) -> bool:
        """Check if user has specific role or is admin"""
        return user.role == role or user.role == UserRole.ADMIN
    
    async def create(self, user_create: Dict[str, Any], safe: bool = False, request: Optional[Request] = None) -> User:
        """Create user and make first user an admin"""
        user_db = self.user_db
        if isinstance(user_db, SQLAlchemyUserDatabase):
            session = user_db.session
            # Fixed async query
            result = await session.execute(select(User))
            is_first_user = result.scalars().first() is None
            
            if is_first_user:
                user_create["role"] = UserRole.ADMIN
                user_create["is_superuser"] = True
                logger.info("Creating first user as admin")
        
        return await super().create(user_create, safe, request)

# User manager dependency
async def get_user_manager(user_db=Depends(get_user_db)):
    """Provides user manager dependency"""
    yield UserManager(user_db)

# JWT authentication configuration
bearer_transport = BearerTransport(tokenUrl=f"{settings.API_V1_STR}/jwt/login")

# JWT strategy factory function
def get_jwt_strategy() -> Strategy:
    """Get JWT strategy for token generation"""
    # Get token expire minutes as integer
    expire_minutes = int(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    lifetime_seconds = expire_minutes * 60
    
    return CustomJWTStrategy(
        secret=settings.SECRET_KEY,
        lifetime_seconds=lifetime_seconds,
    )

# Auth backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

# Create FastAPIUsers instance
fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

# User dependencies
current_active_user = fastapi_users.current_user(active=True)
current_verified_user = fastapi_users.current_user(active=True, verified=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

# Role-based access control
def current_user_with_role(role: UserRole):
    """Creates a dependency for role-based access control"""
    async def dependency(
        user_manager=Depends(get_user_manager),
        user=Depends(current_active_user),
    ):
        if await user_manager.has_role(user, role):
            return user
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Role {role} required",
        )
    return dependency

# Role-based dependencies
current_admin = current_user_with_role(UserRole.ADMIN)
current_manager = current_user_with_role(UserRole.MANAGER)
