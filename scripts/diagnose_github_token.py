#!/usr/bin/env python
"""
Simplified diagnostic tool for GitHub token recognition issues.

This script directly tests GitHub tokens against the placeholder detection patterns
without relying on importing application modules.
"""
import os
import re
import sys
from pathlib import Path

def directly_test_placeholder(value):
    """
    Direct implementation of placeholder detection logic from env_config.py
    to check GitHub tokens without importing modules.
    """
    if not value or not isinstance(value, str):
        return False, []
        
    # Common legitimate values (not placeholders)
    common_values = [
        "True", "False", 
        "true", "false", 
        "yes", "no", 
        "on", "off",
        "INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL",
        "development", "production", "staging", "testing"
    ]
    
    # If the value exactly matches a common legitimate value, it's not a placeholder
    if value in common_values:
        return False, []
        
    # Patterns that indicate placeholders
    patterns = [
        r"your[-_].*[-_]here",  # e.g., "your-token-here"
        r"replace[-_]with[-_]",  # e.g., "replace_with_secret_key"
        r"<.*>",                # Values in angle brackets, e.g., "<token>"
        r"\[.*\]",              # Values in square brackets, e.g., "[insert_key]"
        r"example[-_.]*",       # e.g., "example.com", "example_key"
        r"change[-_]?me",       # e.g., "change-me", "change_me", "changeme"
        r"xxx+",                # Multiple x characters, e.g., "xxxxx"
        r"CHANGEME",            # Uppercase "CHANGEME"
        r"TODO",                # "TODO" placeholder
        # More specific all-caps pattern to avoid matching legitimate values
        r"^(?!INFO$|DEBUG$|ERROR$|WARNING$|CRITICAL$)[A-Z_]{3,}$"
    ]
    
    pattern_names = [
        "your-*-here pattern",
        "replace-with pattern",
        "angle brackets pattern",
        "square brackets pattern",
        "example pattern",
        "change-me pattern",
        "multiple x's pattern",
        "CHANGEME pattern",
        "TODO pattern",
        "uppercase pattern"
    ]
    
    matching_patterns = []
    for i, pattern in enumerate(patterns):
        if re.search(pattern, value, re.IGNORECASE):
            matching_patterns.append({
                "pattern": pattern,
                "name": pattern_names[i]
            })
    
    return bool(matching_patterns), matching_patterns

def read_env_file():
    """Read the .env file directly to check for GitHub token"""
    project_root = Path(__file__).resolve().parent.parent
    env_path = project_root / '.env'
    
    if not env_path.exists():
        print(f"ERROR: .env file not found at {env_path}")
        return {}
    
    env_vars = {}
    with open(env_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            if '=' in line:
                key, value = line.split('=', 1)
                env_vars[key.strip()] = value.strip()
    
    return env_vars

def test_github_token():
    """Test GitHub token from .env file against placeholder detection"""
    print("GitHub Token Diagnostic Tool")
    print("===========================")
    
    # Get token from .env file
    env_vars = read_env_file()
    github_token = env_vars.get('GITHUB_TOKEN')
    
    if not github_token:
        # Check if it's commented out
        with open(Path(__file__).resolve().parent.parent / '.env', 'r') as f:
            for line in f:
                if line.strip().startswith('# GITHUB_TOKEN='):
                    print("NOTE: GITHUB_TOKEN is commented out in .env file.")
                    print("Uncomment this line to enable GitHub integration.")
                    # Extract the token for testing anyway
                    github_token = line.strip().split('=', 1)[1] if '=' in line else None
                    break
    
    print(f"\n=== GitHub Token Analysis ===")
    if github_token:
        print(f"GitHub token found in .env file: {github_token[:4]}...{github_token[-4:]}")
        is_placeholder, matching_patterns = directly_test_placeholder(github_token)
        
        print(f"Token treated as placeholder: {is_placeholder}")
        
        if matching_patterns:
            print("Matching placeholder patterns:")
            for p in matching_patterns:
                print(f" - {p['name']}: {p['pattern']}")
            
            print("\nISSUE DETECTED: Your GitHub token is being incorrectly identified")
            print("as a placeholder value. This causes it to be removed from the environment")
            print("variables during validation.")
            
            print("\nRECOMMENDED FIX:")
            print("Modify app/netctrl/env_config.py's is_placeholder() function to whitelist GitHub tokens:")
            print("\n# Whitelist known token formats")
            print("if isinstance(value, str) and value.startswith(('github_pat_', 'ghp_')):")
            print("    return False")
            
        else:
            # If not a placeholder but still having issues
            print("Token is not detected as a placeholder. Check if it's being loaded correctly.")
    else:
        print("GitHub token not found in .env file.")
        print("If you need GitHub integration, add GITHUB_TOKEN=your_token to .env file.")
    
    # Check if token is available in environment
    env_token = os.environ.get('GITHUB_TOKEN')
    print(f"\nGitHub token in current environment: {'Present' if env_token else 'Not present'}")
    
    if not env_token and github_token:
        print("\nISSUE DETECTED: Token exists in .env file but is not loaded into environment.")
        print("This could be due to several reasons:")
        print("1. The .env file is not being loaded correctly")
        print("2. The token is being identified as a placeholder and removed during validation")
        print("3. Another part of the code is removing the token from the environment")

def main():
    """Run all diagnostic tests"""
    test_github_token()

if __name__ == "__main__":
    main()
