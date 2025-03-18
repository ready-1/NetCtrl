"""
Main application entry point for FastAPI
"""
import logging
import yaml
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from app.core.config import settings
from app.api.routes import auth, roles, users, content, files
from app.db.init_db import init_db

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="API for the NetCtrl CMS with role-based access control",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
)

# Set up CORS middleware
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Root API router
@app.get("/")
async def root():
    """
    Root endpoint that returns API information
    """
    return {
        "name": settings.PROJECT_NAME,
        "docs": f"{settings.API_V1_STR}/docs",
        "version": "0.1.0"
    }

# Health check endpoint
@app.get(f"{settings.API_V1_STR}/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "ok"}

# Include API routers
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}")
app.include_router(roles.router, prefix=f"{settings.API_V1_STR}")
app.include_router(users.router, prefix=f"{settings.API_V1_STR}")
app.include_router(content.router, prefix=f"{settings.API_V1_STR}")
app.include_router(files.router, prefix=f"{settings.API_V1_STR}")

# Startup event
@app.on_event("startup")
async def startup_event():
    """
    Startup event that initializes the database and generates OpenAPI schema
    """
    logger.info("Starting up application")
    
    # Initialize database and create superuser if needed
    try:
        await init_db()
        logger.info("Database initialization completed successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
    
    # Generate OpenAPI schema on startup
    try:
        openapi_schema = app.openapi()
        openapi_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                  "openapi.yaml")
        
        with open(openapi_path, 'w') as f:
            yaml.dump(openapi_schema, f, default_flow_style=False, sort_keys=False)
        logger.info(f"OpenAPI schema exported to {openapi_path}")
    except Exception as e:
        logger.error(f"Failed to generate OpenAPI schema: {e}")
    
    logger.info("Application startup completed")

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """
    Shutdown event
    """
    logger.info("Application shutting down")
