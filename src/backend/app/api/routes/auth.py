"""
Authentication routes for login, registration, and user management
"""
from typing import Optional, Dict, Any
from fastapi import APIRouter, Depends, Response, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_users.router.common import ErrorCode

from app.auth.users import auth_backend, fastapi_users, get_user_manager, UserManager
from app.schemas.user import UserRead, UserCreate, UserUpdate

# Create the main auth router
router = APIRouter(tags=["auth"])

# Custom login route that uses username
@router.post("/jwt/login")
async def login(
    request: Request,
    credentials: OAuth2PasswordRequestForm = Depends(),
    user_manager: UserManager = Depends(get_user_manager)
):
    """Custom login route that authenticates with username"""
    try:
        # Get user by username instead of email
        user = await user_manager.get_by_username(credentials.username)
        
        # Create a credentials dict manually since OAuth2PasswordRequestForm doesn't have dict()
        creds_dict = {
            "username": credentials.username,
            "password": credentials.password,
        }
        
        # Authenticate the user
        authenticated_user, token = await auth_backend.get_strategy().authenticate(
            creds_dict, user_manager, request.state
        )
        
        if authenticated_user is None or token is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorCode.LOGIN_BAD_CREDENTIALS,
            )
            
        # Return the token
        return {
            "access_token": token,
            "token_type": "bearer",
        }  # Added comma here
    except Exception as e:
        # Log the error but don't expose details
        print(f"Login error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorCode.LOGIN_BAD_CREDENTIALS,
        )

# Include standard FastAPI-Users routers
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/register",
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
)

# Include other FastAPI-Users auth endpoints except login
for route in fastapi_users.get_auth_router(auth_backend).routes:
    # Skip the login route as we've implemented our own
    if "login" not in route.path:
        router.routes.append(route)
