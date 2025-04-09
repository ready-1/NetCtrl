"""
Environment variable management for NetCtrl.

This module provides centralized handling of environment variables with type validation,
default values, comprehensive error handling, and placeholder detection for the NetCtrl application.
"""

import os
import re
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

# Configure module logging
logger = logging.getLogger("netctrl.config")

# Initialize logging handler if not already configured
if not logger.handlers and not logging.getLogger().handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

def is_placeholder(value):
    """
    Detect if a value is a placeholder using pattern matching.
    
    This function identifies common placeholder patterns in configuration values.
    
    Args:
        value: The value to check
        
    Returns:
        bool: True if the value is likely a placeholder, False otherwise
    """
    if not value or not isinstance(value, str):
        return False
    
    # Whitelist known token formats from major services
    # GitHub PATs (github_pat_* or ghp_*)
    if isinstance(value, str) and value.startswith(('github_pat_', 'ghp_')):
        return False
        
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
        return False
        
    # Patterns that indicate placeholders
    placeholder_patterns = [
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
    
    # Check if the value matches any placeholder pattern
    for pattern in placeholder_patterns:
        if re.search(pattern, value, re.IGNORECASE):
            return True
    
    return False

def load_environment():
    """
    Load environment variables with smart .env file detection and validation.
    
    Attempts to locate and load an .env file from the most likely locations.
    Falls back to system environment variables if no .env file is found.
    
    Returns:
        bool: True if environment variables were loaded successfully, False otherwise
    """
    # Try to find the .env file in common locations
    dotenv_path = find_dotenv(usecwd=True)
    
    if not dotenv_path:
        # Fall back to manual search in likely locations
        project_root = Path(__file__).resolve().parent.parent.parent
        potential_paths = [
            os.path.join(os.getcwd(), '.env'),
            os.path.join(project_root, '.env'),
            os.path.join(project_root.parent, '.env'),
        ]
        
        for path in potential_paths:
            if os.path.isfile(path):
                dotenv_path = path
                break
    
    if dotenv_path:
        load_result = load_dotenv(dotenv_path, override=True)
        if load_result:
            logger.info(f"Loaded environment variables from {dotenv_path}")
            validate_environment()
            return True
        else:
            logger.warning(f"Found .env file at {dotenv_path} but failed to load variables")
    else:
        logger.warning("No .env file found. Using system environment variables only.")
    
    # Even without a .env file, validate the environment
    validate_environment()
    return False

def validate_environment():
    """
    Validate that critical environment variables are properly set.
    
    Checks for common issues like missing variables and placeholder values.
    """
    # Critical variables with appropriate defaults
    critical_vars = {
        'DJANGO_SECRET_KEY': {'required_in_prod': True, 'has_sensitive_default': True},
        'GITHUB_TOKEN': {'required_in_prod': False, 'has_sensitive_default': False},
        'DJANGO_DEBUG': {'required_in_prod': False, 'has_sensitive_default': False},
    }
    
    # Get the current environment
    environment = os.environ.get('ENVIRONMENT', 'development')
    is_production = environment.lower() == 'production'
    
    # Validate each critical variable
    for var_name, config in critical_vars.items():
        value = os.environ.get(var_name)
        
        # Check if missing
        if not value:
            if is_production and config['required_in_prod']:
                logger.error(f"Critical environment variable {var_name} missing in production")
            else:
                logger.warning(f"Environment variable {var_name} not set")
            continue
            
        # Check if it's a placeholder
        if is_placeholder(value):
            logger.warning(f"Environment variable {var_name} contains placeholder value: {value}")
            # Remove the placeholder value to force fallback to defaults
            os.environ.pop(var_name)

def get_env_var(
    name, 
    default=None,
    required=False,
    var_type=str
):
    """
    Get environment variable with enhanced validation and type conversion.
    
    Args:
        name: Environment variable name
        default: Default value if variable is not set or contains a placeholder
        required: Whether the variable is required
        var_type: Type to convert the variable to
    
    Returns:
        The environment variable value with appropriate type conversion
    
    Raises:
        ValueError: If a required variable is missing or cannot be converted
    """
    value = os.environ.get(name)
    
    # Handle missing variables
    if not value:
        if required:
            error_msg = f"Required environment variable '{name}' is not set."
            logger.error(error_msg)
            raise ValueError(error_msg)
        return default
    
    # Handle placeholder values - treat them as missing
    if is_placeholder(value):
        logger.warning(f"Environment variable '{name}' contains a placeholder value")
        if required:
            error_msg = f"Required environment variable '{name}' contains a placeholder value."
            logger.error(error_msg)
            raise ValueError(error_msg)
        return default
    
    # Handle type conversion with robust error handling
    try:
        if var_type == bool:
            if isinstance(value, str):
                return value.lower() in ('true', 'yes', '1', 'y', 'on')
            return bool(value)
        elif var_type == list:
            if isinstance(value, str):
                return [item.strip() for item in value.split(',') if item.strip()]
            if isinstance(value, list):
                return value
            return [value]
        elif var_type == int:
            if isinstance(value, str):
                return int(value)
            return value
        else:
            return var_type(value)
    except (ValueError, TypeError) as e:
        logger.warning(f"Failed to convert '{name}' value to {var_type.__name__}: {e}")
        if default is not None:
            return default
        if required:
            raise
        return None

# Initialize at module level
load_environment()
