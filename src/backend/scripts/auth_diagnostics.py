#!/usr/bin/env python
"""
Authentication Diagnostics Tool for NetCtrl CMS
"""
import asyncio
import sys
import os
import json
import httpx
from typing import Dict, Any, Optional
from sqlalchemy.future import select
from fastapi_users.password import PasswordHelper
from datetime import datetime, timedelta
from jose import jwt

# Add parent directory to path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.insert(0, parent_dir)

# Import app modules
from app.db.session import AsyncSessionLocal
from app.models.user import User
from app.core.config import settings

# Terminal colors
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
ENDC = '\033[0m'
BOLD = '\033[1m'

def success(text): print(f"{GREEN}✓ {text}{ENDC}")
def error(text): print(f"{RED}✗ {text}{ENDC}")
def info(text): print(f"{BLUE}ℹ {text}{ENDC}")
def section(text): print(f"\n{BOLD}{text}{ENDC}\n{'-' * 40}")

async def check_user(username: str = None) -> bool:
    """Check if user exists in database"""
    username = username or settings.FIRST_SUPERUSER_USERNAME
    section(f"Checking User: {username}")
    
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(User).where(User.username == username)
        )
        user = result.scalars().first()
        
        if not user:
            error(f"User not found: {username}")
            return False
        
        success(f"Found user: {username} (ID: {user.id})")
        info(f"Role: {user.role}, Active: {user.is_active}, Superuser: {user.is_superuser}")
        return True

async def verify_password(username: str, password: str) -> bool:
    """Verify password for user"""
    section(f"Verifying Password")
    
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(User).where(User.username == username)
        )
        user = result.scalars().first()
        
        if not user:
            error(f"User not found: {username}")
            return False
        
        if not user.is_active:
            error(f"User is not active")
            return False
        
        is_valid = PasswordHelper().verify_and_update(
            password, user.hashed_password
        )[0]
        
        if is_valid:
            success(f"Password verification successful")
            return True
        else:
            error(f"Password verification failed")
            return False

async def generate_token(username: str) -> Optional[str]:
    """Generate JWT token for user"""
    section("Generating JWT Token")
    
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(User).where(User.username == username)
        )
        user = result.scalars().first()
        
        if not user:
            error(f"User not found")
            return None
            
        # Create token data
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        expire = datetime.utcnow() + expires_delta
        token_data = {
            "sub": str(user.id),
            "exp": expire.timestamp(),
            "aud": "fastapi-users:auth"
        }
        
        try:
            token = jwt.encode(token_data, settings.SECRET_KEY, algorithm="HS256")
            success("JWT token generated successfully")
            return token
        except Exception as e:
            error(f"Failed to generate token: {e}")
            return None

async def test_request(url: str, headers: Dict[str, str] = None, data: Dict[str, Any] = None) -> None:
    """Test HTTP request"""
    method = "POST" if data else "GET"
    section(f"Testing {method} Request to {url}")
    
    headers = headers or {}
    
    try:
        async with httpx.AsyncClient() as client:
            if data:
                response = await client.post(url, headers=headers, data=data)
            else:
                response = await client.get(url, headers=headers)
            
            info(f"Status: {response.status_code}")
            
            try:
                response_json = response.json()
                if response.status_code < 400:
                    success(f"Request successful")
                else:
                    error(f"Request failed: {response_json.get('detail', 'Unknown error')}")
            except Exception:
                info(f"Raw response: {response.text[:100]}...")
    except Exception as e:
        error(f"Request failed: {e}")

async def print_examples() -> None:
    """Print example commands"""
    section("Example Commands")
    
    username = settings.FIRST_SUPERUSER_USERNAME
    password = settings.FIRST_SUPERUSER_PASSWORD
    
    print(f"{BOLD}1. Login:{ENDC}")
    print(f"curl -X POST 'http://localhost/api/v1/jwt/login' \\")
    print(f"  -H 'Content-Type: application/x-www-form-urlencoded' \\")
    print(f"  -d 'username={username}&password={password}&grant_type=password'")
    
    print(f"\n{BOLD}2. Use token:{ENDC}")
    print(f"TOKEN=$(curl -s -X POST 'http://localhost/api/v1/jwt/login' \\")
    print(f"  -H 'Content-Type: application/x-www-form-urlencoded' \\")
    print(f"  -d 'username={username}&password={password}&grant_type=password' | jq -r '.access_token')")
    print(f"curl -H 'Authorization: Bearer $TOKEN' http://localhost/api/v1/users/me")

async def system_health() -> None:
    """Perform system health check"""
    section("Authentication System Health Check")
    
    # Check admin user
    admin_exists = await check_user(settings.FIRST_SUPERUSER_USERNAME)
    
    # Check password if admin exists
    password_valid = False
    if admin_exists:
        password_valid = await verify_password(
            settings.FIRST_SUPERUSER_USERNAME, 
            settings.FIRST_SUPERUSER_PASSWORD
        )
    
    # Check token generation if password is valid
    token_valid = False
    if password_valid:
        token = await generate_token(settings.FIRST_SUPERUSER_USERNAME)
        token_valid = token is not None
    
    # Print summary
    section("Health Check Summary")
    if admin_exists:
        success("Admin user exists")
    else:
        error("Admin user missing")
    
    if password_valid:
        success("Password validation works")
    else:
        error("Password validation failed")
    
    if token_valid:
        success("JWT token generation works")
    else:
        error("JWT token generation failed")
    
    # Next steps
    if not admin_exists or not password_valid:
        info("Run: docker compose exec backend python scripts/reset_admin_password.py")

async def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python auth_diagnostics.py COMMAND [args]")
        print("\nCommands:")
        print("  check-user [username]           - Check if user exists")
        print("  verify-pass USER PASS           - Verify password")
        print("  generate-token USER             - Generate JWT token")
        print("  test-login USER PASS            - Test login endpoint")
        print("  examples                        - Show example commands")
        print("  health-check                    - Run system health check")
        return
    
    command = sys.argv[1]
    
    if command == "check-user":
        username = sys.argv[2] if len(sys.argv) > 2 else None
        await check_user(username)
    
    elif command == "verify-pass":
        if len(sys.argv) < 4:
            error("Missing arguments: username and password required")
            return
        await verify_password(sys.argv[2], sys.argv[3])
    
    elif command == "generate-token":
        if len(sys.argv) < 3:
            error("Missing argument: username required")
            return
        await generate_token(sys.argv[2])
    
    elif command == "test-login":
        if len(sys.argv) < 4:
            error("Missing arguments: username and password required")
            return
        await test_request(
            "http://localhost/api/v1/jwt/login",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "username": sys.argv[2],
                "password": sys.argv[3],
                "grant_type": "password"
            }
        )
    
    elif command == "examples":
        await print_examples()
    
    elif command == "health-check":
        await system_health()
    
    else:
        error(f"Unknown command: {command}")

if __name__ == "__main__":
    asyncio.run(main())
