"""
Custom JWT authentication strategy implementation
"""
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, Tuple
import logging
import jwt
from fastapi_users import models
from fastapi_users.authentication.strategy.base import Strategy

# Configure logger
logger = logging.getLogger(__name__)

class CustomJWTStrategy(Strategy):
    """Custom JWT authentication strategy that supports username-based authentication"""
    
    def __init__(
        self,
        secret: str,
        lifetime_seconds: int,
        token_audience: Optional[str] = None,
        algorithm: str = "HS256",
    ):
        self.secret = secret
        self.lifetime_seconds = int(lifetime_seconds)  # Ensure it's an integer
        self.token_audience = token_audience
        self.algorithm = algorithm
        logger.info(f"Initializing CustomJWTStrategy with lifetime_seconds: {self.lifetime_seconds}")

    async def read_token(
        self, token: Optional[str], user_manager=None
    ) -> Optional[models.UP]:
        """Read and validate a token."""
        if token is None:
            return None

        try:
            payload = jwt.decode(
                token,
                self.secret,
                audience=self.token_audience,
                algorithms=[self.algorithm],
            )
            user_id = payload.get("sub")
            if user_id is None:
                return None

            # Convert user_id from string back to integer since that's what the database expects
            user_id = int(user_id)
            
            user = await user_manager.get(user_id)
            return user
        except (jwt.PyJWTError, ValueError):
            return None

    async def write_token(self, user: models.UP) -> str:
        """Generate a new token for a user."""
        payload = {
            "sub": str(user.id),  # Convert user.id to string for JWT
            "aud": self.token_audience,
            "exp": datetime.utcnow() + timedelta(seconds=self.lifetime_seconds),
        }
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)

    async def authenticate(
        self, credentials: Dict[str, Any], user_manager, strategy_state=None
    ) -> Tuple[Optional[models.UP], Optional[str]]:
        """Authenticate with username and password"""
        try:
            username = credentials.get("username")
            password = credentials.get("password")
            
            if username is None or password is None:
                return None, None
            
            # Get user by username
            user = await user_manager.get_by_username(username)
            
            # Verify password
            verified, updated_password_hash = user_manager.password_helper.verify_and_update(
                password, user.hashed_password
            )
            
            if not verified:
                return None, None
                
            # Update password hash if needed
            if updated_password_hash is not None:
                await user_manager.user_db.update(user, {"hashed_password": updated_password_hash})
            
            # Generate token
            token = await self.write_token(user)
            
            return user, token
        except Exception as e:
            logger.error(f"Error in authentication: {e}")
            return None, None
