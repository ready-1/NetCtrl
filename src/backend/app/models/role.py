"""
Role model for RBAC functionality
"""
from enum import Enum

class UserRole(str, Enum):
    """
    Enumeration of user roles in the system
    """
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"
