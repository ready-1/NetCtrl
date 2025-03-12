"""
FastAPI-Users configuration and user management
"""
from typing import Optional, Dict, Any
from fastapi import Depends, Request, HTTPException, status
from fastapi_users import BaseUserManager, FastAPIUsers, IntegerIDMixin
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.db.session import get_async_session
from app.models.user import User
from app.models.role import UserRole

# User database adapter
async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    """
    FastAPI dependency that provides a SQLAlchemy user database
    """
    yield SQLAlchemyUserDatabase(session, User)

# User manager for handling user operations
class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """
    Custom user manager for handling user operations
    """
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY
    
    # Override to handle user creation
    async def on_after_register(self, user: User, request: Optional[Request] = None):
        """
        Hook that runs after successful user registration
        """
        # Auto-verify users since we don't have email
        user.is_verified = True
        print(f"User {user.id} has registered with username {user.username}")
    
    # Override to handle password reset (minimal without email)
    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        """
        Hook that runs after user requests password reset
        """
        # In a real system, you would send an email here
        print(f"User {user.id} has requested password reset. Token: {token}")
    
    # Custom method to check if user has specific role
    async def has_role(self, user: User, role: UserRole) -> bool:
        """
        Check if user has a specific role or is an admin
        """
        return user.role == role or user.role == UserRole.ADMIN
    
    # Override create to set admin role for first user
    async def create(self, user_create: Dict[str, Any], safe: bool = False, request: Optional[Request] = None) -> User:
        """
        Create a new user and make first user an admin
        """
        # Check if this is first user to be created
        user_db = self.user_db
        if isinstance(user_db, SQLAlchemyUserDatabase):
            session = user_db.session
            first_user = await session.execute("SELECT COUNT(*) FROM users")
            is_first_user = (await first_user.scalar()) == 0
            
            if is_first_user:
                user_create["role"] = UserRole.ADMIN
                user_create["is_superuser"] = True
        
        return await super().create(user_create, safe, request)

async def get_user_manager(user_db=Depends(get_user_db)):
    """
    FastAPI dependency that provides a user manager
    """
    yield UserManager(user_db)

# JWT authentication
bearer_transport = BearerTransport(tokenUrl=f"{settings.API_V1_STR}/auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    """
    Get JWT strategy for token generation
    """
    return JWTStrategy(
        secret=settings.SECRET_KEY,
        lifetime_seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )

# Authentication backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

# FastAPIUsers instance
fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

# Export current user dependencies
current_active_user = fastapi_users.current_user(active=True)
current_verified_user = fastapi_users.current_user(active=True, verified=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

# Role-based dependencies
def current_user_with_role(role: UserRole):
    """
    Creates a dependency for role-based access control
    """
    async def current_user_with_role_dependency(
        user_manager=Depends(get_user_manager),
        user=Depends(current_active_user),
    ):
        """
        Check if current user has required role
        """
        if await user_manager.has_role(user, role):
            return user
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Role {role} required",
        )
    return current_user_with_role_dependency

# Export role-based dependencies
current_admin = current_user_with_role(UserRole.ADMIN)
current_manager = current_user_with_role(UserRole.MANAGER)
