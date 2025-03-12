"""
Authentication routes for login, registration, and user management
"""
from fastapi import APIRouter

from app.auth.users import auth_backend, fastapi_users
from app.schemas.user import UserRead, UserCreate, UserUpdate

# Create the main auth router
router = APIRouter(tags=["auth"])

# Include FastAPI-Users routers
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/register",
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
)
