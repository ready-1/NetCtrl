"""
Extensions to SQLAlchemyUserDatabase to support username-based queries
"""
from typing import Optional, Type, TypeVar
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from app.models.user import User

UP = TypeVar("UP", bound=User)

class SQLAlchemyUserDatabaseWithUsername(SQLAlchemyUserDatabase):
    """
    Extension of SQLAlchemyUserDatabase that supports username-based queries.
    """
    
    async def get_by_username(self, username: str) -> Optional[UP]:
        """
        Get a user by username.
        
        Args:
            username: The username of the user to get.
            
        Returns:
            The user with the given username, or None if no such user exists.
        """
        statement = select(self.user_table).where(self.user_table.username == username)
        
        # Get the session (handle possible async generator)
        session = self.session
        session_value = session
        
        if hasattr(session, "__anext__"):
            try:
                session_value = await session.__anext__()
            except StopAsyncIteration:
                return None
                
        # Execute the query
        result = await session_value.execute(statement)
        user = result.scalars().first()
        
        return user

# Factory function to create a database adapter with username support
def get_user_db_with_username(session: AsyncSession) -> SQLAlchemyUserDatabaseWithUsername:
    """
    Create a SQLAlchemyUserDatabaseWithUsername instance.
    
    Args:
        session: The SQLAlchemy session to use.
        
    Returns:
        A SQLAlchemyUserDatabaseWithUsername instance.
    """
    return SQLAlchemyUserDatabaseWithUsername(session, User)
