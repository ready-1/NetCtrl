#!/usr/bin/env python
"""
Admin Password Reset Tool for NetCtrl CMS
"""
import asyncio
import sys
import os
from sqlalchemy.future import select
from fastapi_users.password import PasswordHelper

# Add parent directory to path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.insert(0, parent_dir)

# Import app modules
from app.db.session import AsyncSessionLocal
from app.models.user import User
from app.models.role import UserRole
from app.core.config import settings

async def reset_admin_password(new_password: str = None):
    """Reset admin password or create admin if not exists"""
    print("Admin Password Reset Tool")
    print("========================")
    
    # Use provided password or default
    new_password = new_password or settings.FIRST_SUPERUSER_PASSWORD
    print(f"Using password: {new_password}")
    
    # Generate password hash
    hashed_password = PasswordHelper().hash(new_password)
    
    async with AsyncSessionLocal() as session:
        # Find admin user
        result = await session.execute(
            select(User).where(User.username == settings.FIRST_SUPERUSER_USERNAME)
        )
        admin_user = result.scalars().first()
        
        if not admin_user:
            # Create new admin user
            admin_user = User(
                username=settings.FIRST_SUPERUSER_USERNAME,
                hashed_password=hashed_password,
                role=UserRole.ADMIN,
                is_active=True,
                is_verified=True,
                is_superuser=True
            )
            session.add(admin_user)
            print(f"Created new admin user: {settings.FIRST_SUPERUSER_USERNAME}")
        else:
            # Update existing admin
            admin_user.hashed_password = hashed_password
            print(f"Updated existing admin user: {admin_user.username}")
        
        # Commit changes
        await session.commit()
        
        print("\nAdmin credentials:")
        print(f"Username: {settings.FIRST_SUPERUSER_USERNAME}")
        print(f"Password: {new_password}")
        print(f"Role: ADMIN")

def main():
    # Use first argument as password if provided
    password = sys.argv[1] if len(sys.argv) > 1 else None
    asyncio.run(reset_admin_password(password))

if __name__ == "__main__":
    main()
