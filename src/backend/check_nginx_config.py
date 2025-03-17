#!/usr/bin/env python
"""
NGINX Configuration Checker for NetCtrl CMS

This script examines the NGINX configuration to identify potential issues
with how login requests are routed to the backend service.
"""
import os
import re
import sys
import subprocess
import textwrap

def print_section(title):
    """Print a section header"""
    print("\n" + "="*80)
    print(f" {title}")
    print("="*80)

def parse_nginx_conf(file_path):
    """
    Parse an NGINX config file and extract relevant information
    """
    if not os.path.exists(file_path):
        print(f"ERROR: NGINX config file not found at {file_path}")
        return None
        
    with open(file_path, 'r') as f:
        content = f.read()
    
    print(f"Examining NGINX config file: {file_path}")
    
    # Look for proxy_pass directives
    proxy_pass_pattern = re.compile(r'location\s+([^{]+)\s*{[^}]*proxy_pass\s+([^;]+);', re.DOTALL)
    proxy_matches = proxy_pass_pattern.findall(content)
    
    # Find API-related location blocks
    api_pattern = re.compile(r'location\s+([^{]*api[^{]*)\s*{([^}]*)}', re.DOTALL)
    api_matches = api_pattern.findall(content)
    
    results = {
        "proxy_routes": proxy_matches,
        "api_locations": api_matches,
        "raw_content": content
    }
    
    return results

def analyze_nginx_routes(parsed_config):
    """
    Analyze parsed NGINX config for login related routes
    """
    if not parsed_config:
        return
    
    print_section("PROXY ROUTES")
    if parsed_config["proxy_routes"]:
        print(f"Found {len(parsed_config['proxy_routes'])} proxy_pass directives:")
        for location, destination in parsed_config["proxy_routes"]:
            location = location.strip()
            print(f"• Location: {location:<30} → Destination: {destination}")
            
            # Check for potential issues
            if "api" in location and "backend" not in destination and "127.0.0.1" not in destination:
                print(f"  ⚠️  WARNING: API location doesn't route to backend service")
            
            if location.startswith("~ ") and "/api/" in location:
                print(f"  ℹ️  INFO: Using regex match for API routes")
    else:
        print("No proxy_pass directives found. This might indicate a configuration issue.")
    
    print_section("API LOCATIONS")
    if parsed_config["api_locations"]:
        print(f"Found {len(parsed_config['api_locations'])} API-related location blocks:")
        for location, block in parsed_config["api_locations"]:
            location = location.strip()
            print(f"• API Location: {location}")
            print(f"  Configuration:")
            for line in textwrap.wrap(block.strip(), width=70):
                print(f"  {line}")
            
            # Check for potential issues
            if "proxy_pass" not in block:
                print(f"  ⚠️  WARNING: No proxy_pass found in API location block")
            if "/api/v1/jwt/login" in location or "/api/v1/auth" in location:
                print(f"  🔍 Found login-related API route")
    else:
        print("No API-related location blocks found. This might indicate a configuration issue.")

def check_docker_network():
    """
    Check Docker networking configuration
    """
    print_section("DOCKER NETWORK CHECK")
    
    try:
        # Run docker compose ps
        compose_result = subprocess.run(
            ["docker", "compose", "ps"], 
            capture_output=True, 
            text=True
        )
        
        if compose_result.returncode != 0:
            print(f"Error running docker compose ps: {compose_result.stderr}")
            return
        
        print("Docker compose services:")
        print(compose_result.stdout)
        
        # Check if backend and nginx services are running
        if "backend" not in compose_result.stdout:
            print("⚠️  WARNING: Backend service doesn't appear to be running")
        if "nginx" not in compose_result.stdout:
            print("⚠️  WARNING: NGINX service doesn't appear to be running")
        
        # Get backend IP address
        backend_ip_result = subprocess.run(
            ["docker", "compose", "exec", "-T", "backend", "hostname", "-i"],
            capture_output=True,
            text=True
        )
        
        if backend_ip_result.returncode == 0:
            backend_ip = backend_ip_result.stdout.strip()
            print(f"Backend service IP: {backend_ip}")
        else:
            print(f"Could not determine backend IP: {backend_ip_result.stderr}")
        
        # Get NGINX configuration for upstream servers
        nginx_conf_result = subprocess.run(
            ["docker", "compose", "exec", "-T", "nginx", "cat", "/etc/nginx/conf.d/default.conf"],
            capture_output=True,
            text=True
        )
        
        if nginx_conf_result.returncode == 0:
            # Look for backend upstream configuration
            backend_upstream = re.search(r'upstream\s+backend\s*{([^}]*)}', nginx_conf_result.stdout, re.DOTALL)
            if backend_upstream:
                upstream_config = backend_upstream.group(1)
                print("Backend upstream configuration:")
                print(upstream_config)
                
                # Check if there's a server directive
                if "server" not in upstream_config:
                    print("⚠️  WARNING: No server directive found in backend upstream")
                    
                # Check if the server matches the backend IP or hostname
                server_match = re.search(r'server\s+([^:]+)(:\d+)?', upstream_config)
                if server_match:
                    server_host = server_match.group(1)
                    print(f"Backend server host: {server_host}")
                    
                    # Check if it's using hostname or IP
                    if server_host == "backend" or server_host == "localhost" or server_host.startswith("127."):
                        print("✓ Backend referenced by hostname or localhost")
                    else:
                        print(f"ℹ️  Backend referenced by IP: {server_host}")
        else:
            print(f"Could not retrieve NGINX configuration: {nginx_conf_result.stderr}")
            
    except Exception as e:
        print(f"Error checking Docker network: {e}")

def check_login_endpoint():
    """
    Check if login endpoint is accessible from NGINX
    """
    print_section("LOGIN ENDPOINT CHECK")
    
    try:
        # Try to curl the login endpoint from the NGINX container
        curl_result = subprocess.run(
            [
                "docker", "compose", "exec", "-T", "nginx",
                "curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", 
                "http://backend:8000/api/v1/jwt/login"
            ],
            capture_output=True,
            text=True
        )
        
        if curl_result.returncode == 0:
            status_code = curl_result.stdout.strip()
            print(f"Login endpoint status from NGINX container: {status_code}")
            
            if status_code.startswith("2") or status_code.startswith("4"):
                print("✓ NGINX can reach backend login endpoint")
            elif status_code.startswith("5"):
                print("⚠️  WARNING: Backend returned server error")
            else:
                print(f"⚠️  WARNING: Unexpected status code: {status_code}")
        else:
            print(f"Error connecting to login endpoint from NGINX: {curl_result.stderr}")
            
        # Try to curl from backend to itself
        backend_curl_result = subprocess.run(
            [
                "docker", "compose", "exec", "-T", "backend",
                "curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", 
                "http://localhost:8000/api/v1/jwt/login"
            ],
            capture_output=True,
            text=True
        )
        
        if backend_curl_result.returncode == 0:
            status_code = backend_curl_result.stdout.strip()
            print(f"Login endpoint status from backend container: {status_code}")
            
            if status_code.startswith("2") or status_code.startswith("4"):
                print("✓ Backend can reach its own login endpoint")
            elif status_code.startswith("5"):
                print("⚠️  WARNING: Backend returned server error when accessing itself")
            else:
                print(f"⚠️  WARNING: Unexpected status code from backend self-check: {status_code}")
        else:
            print(f"Error connecting from backend to itself: {backend_curl_result.stderr}")
            
    except Exception as e:
        print(f"Error checking login endpoint: {e}")

def main():
    """
    Main function to check NGINX configuration
    """
    print_section("NGINX CONFIGURATION CHECKER")
    
    # First check local nginx config file
    print("Checking local NGINX configuration files...")
    
    # Check src/nginx/conf/default.conf
    default_conf_path = os.path.join('src', 'nginx', 'conf', 'default.conf')
    if os.path.exists(default_conf_path):
        parsed_config = parse_nginx_conf(default_conf_path)
        analyze_nginx_routes(parsed_config)
    else:
        print(f"NGINX config not found at {default_conf_path}")
    
    # Check template file
    template_path = os.path.join('src', 'nginx', 'templates', 'default.template')
    if os.path.exists(template_path):
        print("\nFound NGINX template file, analyzing...")
        parsed_template = parse_nginx_conf(template_path)
        analyze_nginx_routes(parsed_template)
    
    # Check Docker networking
    check_docker_network()
    
    # Check login endpoint
    check_login_endpoint()
    
    print_section("RECOMMENDATIONS")
    print("""
1. Make sure NGINX is properly configured to route API requests to the backend:
   - Check the location directive for /api/v1/jwt/login
   - Verify the proxy_pass destination is correct (backend:8000)

2. Verify that the backend service is properly exposing its endpoints:
   - Check that FastAPI is running on 0.0.0.0:8000 (not just 127.0.0.1:8000)
   - Check backend logs for any errors related to the auth endpoints

3. Check Docker networking:
   - Verify that nginx and backend containers can communicate
   - Ensure backend hostname resolves correctly from the nginx container

4. Confirm the exact URL you're using in Postman:
   - It should be http://localhost/api/v1/jwt/login (or your server's hostname)
   - Check you're using form-urlencoded with these fields:
     username: admin
     password: admin
     grant_type: password
    """)

if __name__ == "__main__":
    main()
