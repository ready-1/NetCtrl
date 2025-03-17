#!/usr/bin/env python
"""
Login Test Script for NetCtrl CMS

This script tests the authentication system by making login requests
to both the direct backend endpoint and through NGINX.
"""
import asyncio
import sys
import os
import httpx
import json
import argparse

# Add parent directory to Python path to find app package
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.insert(0, parent_dir)

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

async def test_login(username, password):
    """Test login with provided credentials"""
    section(f"Testing login with username: {username}")
    
    # Login data
    login_data = {
        "username": username,
        "password": password,
        "grant_type": "password"
    }
    
    # Test direct backend login (inside container)
    section("1. Testing login directly to backend (localhost:8000)")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8000/api/v1/jwt/login",
                data=login_data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=5.0
            )
            
            info(f"Status code: {response.status_code}")
            
            try:
                response_json = response.json()
                info(f"Response: {json.dumps(response_json, indent=2)}")
                
                if response.status_code == 200 and "access_token" in response_json:
                    success("Login successful to backend directly")
                    token = response_json["access_token"]
                else:
                    error(f"Login failed: {response_json.get('detail', 'Unknown error')}")
                    token = None
            except Exception as e:
                error(f"Failed to parse response as JSON: {e}")
                info(f"Raw response: {response.text}")
                token = None
    except Exception as e:
        error(f"HTTP request failed: {e}")
        token = None
    
    # Test NGINX proxied login
    section("2. Testing login through NGINX (localhost:80)")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost/api/v1/jwt/login",
                data=login_data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=5.0
            )
            
            info(f"Status code: {response.status_code}")
            
            try:
                response_json = response.json()
                info(f"Response: {json.dumps(response_json, indent=2)}")
                
                if response.status_code == 200 and "access_token" in response_json:
                    success("Login successful through NGINX")
                    token = response_json["access_token"]
                    
                    # Test user info endpoint with token
                    section("3. Testing /users/me endpoint with token")
                    me_response = await client.get(
                        "http://localhost/api/v1/users/me",
                        headers={"Authorization": f"Bearer {token}"}
                    )
                    
                    if me_response.status_code == 200:
                        success("Successfully retrieved user info")
                        info(f"User info: {json.dumps(me_response.json(), indent=2)}")
                    else:
                        error(f"Failed to get user info: {me_response.status_code}")
                else:
                    error(f"Login failed: {response_json.get('detail', 'Unknown error')}")
            except Exception as e:
                error(f"Failed to parse response as JSON: {e}")
                info(f"Raw response: {response.text}")
    except Exception as e:
        error(f"HTTP request failed: {e}")

    # Print curl command for manual testing
    section("Manual testing commands")
    print(f"""
# Test login with curl:
curl -X POST "http://localhost/api/v1/jwt/login" \\
  -H "Content-Type: application/x-www-form-urlencoded" \\
  -d "username={username}&password={password}&grant_type=password"
    """)

async def main():
    parser = argparse.ArgumentParser(description="Test authentication system")
    parser.add_argument("username", help="Username to test")
    parser.add_argument("password", help="Password to test")
    
    # Check if running with arguments or use defaults
    if len(sys.argv) >= 3:
        args = parser.parse_args()
        username = args.username
        password = args.password
    else:
        # Default to admin credentials from settings
        from app.core.config import settings
        username = settings.FIRST_SUPERUSER_USERNAME
        password = settings.FIRST_SUPERUSER_PASSWORD
        print(f"Using default credentials: {username}/{password}")
    
    await test_login(username, password)

if __name__ == "__main__":
    asyncio.run(main())
