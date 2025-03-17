"""
Application configuration using environment variables and type validation
"""
from typing import List, Optional, Union
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application settings with environment variable loading and validation
    """
    # API settings
    PROJECT_NAME: str = "NetCtrl CMS"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "development_secret_key"  # Override in production
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    # Database settings
    POSTGRES_SERVER: str = "database"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "netctrl"
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    # CORS settings
    BACKEND_CORS_ORIGINS: List[Union[str, AnyHttpUrl]] = ["http://localhost:3000"]

    # Superuser settings
    FIRST_SUPERUSER_USERNAME: str = "admin"
    FIRST_SUPERUSER_PASSWORD: Optional[str] = "admin"  # Override in production
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

    class Config:
        """
        Pydantic settings configuration
        """
        case_sensitive = True
        env_file = ".env"

# Create global settings instance
settings = Settings()
