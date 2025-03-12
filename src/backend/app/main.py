"""
Main application entry point for FastAPI
"""
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes import auth, roles
from app.db.init_db import create_first_superuser

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
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
@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "ok"}

# Include API routers
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}")
app.include_router(roles.router, prefix=f"{settings.API_V1_STR}")

# Startup event
@app.on_event("startup")
async def startup_event():
    """
    Startup event that initializes the database
    """
    logger.info("Starting up application")
    # Database migrations are handled by Alembic via the start script
    # First superuser creation is handled in the start script via app.initial_setup
    logger.info("Application startup completed")

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """
    Shutdown event
    """
    logger.info("Application shutting down")
