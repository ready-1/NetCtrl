"""
Application configuration using environment variables and type validation
"""
from typing import List, Optional, Union
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings
import logging

logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    """
    Application settings with environment variable loading and validation
    """
    # API settings
    PROJECT_NAME: str = "NetCtrl CMS"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "development_secret_key"  # Override in production with NETCTRL_SECRET_KEY
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    # Database settings
    POSTGRES_SERVER: str = "database"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "netctrl"
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    # CORS settings
    BACKEND_CORS_ORIGINS: List[Union[str, AnyHttpUrl]] = ["http://localhost:3000"]

    # Superuser settings - can be overridden with environment variables
    # NETCTRL_FIRST_SUPERUSER_USERNAME - default is "admin"
    # NETCTRL_FIRST_SUPERUSER_PASSWORD - default is "admin123"
    # NETCTRL_FIRST_SUPERUSER_EMAIL - optional, no default
    FIRST_SUPERUSER_USERNAME: str = "admin"
    FIRST_SUPERUSER_PASSWORD: str = "admin123"  # Override in production with NETCTRL_FIRST_SUPERUSER_PASSWORD
    FIRST_SUPERUSER_EMAIL: Optional[str] = None  # Email is optional in our setup

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: dict) -> str:
        """
        Build the database connection string from individual components if not provided
        """
        if isinstance(v, str):
            return v

        return f"postgresql+asyncpg://{values['POSTGRES_USER']}:{values['POSTGRES_PASSWORD']}@{values['POSTGRES_SERVER']}/{values['POSTGRES_DB']}"

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        """
        Parse CORS origins from string or list
        """
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    @validator("FIRST_SUPERUSER_PASSWORD")
    def validate_admin_password(cls, v: str) -> str:
        """
        Validate that the admin password is strong enough
        """
        if v == "admin123" and not cls._detect_test_environment():
            logger.warning(
                "Using default admin password. This is insecure and should "
                "only be used in development environments. Set the "
                "NETCTRL_FIRST_SUPERUSER_PASSWORD environment variable "
                "to override it in production."
            )
        
        if len(v) < 8:
            logger.warning(
                "Admin password is less than 8 characters. "
                "This is potentially insecure."
            )
        
        return v
    
    @classmethod
    def _detect_test_environment(cls) -> bool:
        """
        Helper method to detect if we're running in a test environment
        """
        import sys
        return "pytest" in sys.modules

    class Config:
        """
        Pydantic settings configuration
        """
        case_sensitive = True
        env_file = ".env"
        env_prefix = "NETCTRL_"  # Use NETCTRL_ as prefix for environment variables

# Create global settings instance
settings = Settings()

# Log important settings on import
if settings.FIRST_SUPERUSER_PASSWORD == "admin123":
    logger.warning(
        "Using default admin password. Set NETCTRL_FIRST_SUPERUSER_PASSWORD "
        "environment variable to use a custom secure password."
    )

if settings.SECRET_KEY == "development_secret_key":
    logger.warning(
        "Using default SECRET_KEY. This is insecure and should only be used "
        "in development. Set the NETCTRL_SECRET_KEY environment variable "
        "in production."
    )
