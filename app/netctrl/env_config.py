"""
Environment variable management for NetCtrl.

This module provides centralized handling of environment variables with type validation,
default values, and comprehensive error handling for the NetCtrl application.
"""

import os
import typing
from dotenv import load_dotenv

# Load environment variables once at module level
load_dotenv()


def get_env_var(
    name: str, 
    default: typing.Optional[typing.Any] = None,
    required: bool = False,
    var_type: typing.Type = str
) -> typing.Any:
    """
    Get environment variable with type conversion and validation.
    
    Args:
        name: Environment variable name
        default: Default value if variable is not set
        required: Whether the variable is required
        var_type: Type to convert the variable to
    
    Returns:
        The environment variable value with appropriate type conversion
    
    Raises:
        RuntimeError: If a required variable is missing
        ValueError: If variable cannot be converted to the specified type
    """
    value = os.environ.get(name)
    
    # Handle missing variables
    if value is None:
        if required:
            raise RuntimeError(
                f"Required environment variable '{name}' is not set. "
                f"Please add it to your .env file."
            )
        return default
    
    # Handle type conversion
    try:
        if var_type == bool:
            return value.lower() in ('true', 'yes', '1', 'y')
        elif var_type == list:
            return value.split(',')
        else:
            return var_type(value)
    except (ValueError, TypeError):
        if default is not None:
            return default
        raise ValueError(
            f"Environment variable '{name}' value '{value}' "
            f"could not be converted to {var_type.__name__}."
        )
