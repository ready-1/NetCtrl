#!/usr/bin/env python
"""
Database reset script for NetCtrl CMS
"""
import asyncio
import logging
import sys
import os
from sqlalchemy.ext.asyncio import create_async_engine

# Add parent directory to path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.insert(0, parent_dir)

# Import app modules
from app.core.config import settings
from app.db.base import Base
from app.db.init_db import create_first_superuser

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("db_reset")

async def reset_database():
    """Reset database by dropping and recreating all tables"""
    logger.info("Connecting to database at %s", settings.POSTGRES_SERVER)
    engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI)
    
    try:
        # Drop all tables
        logger.info("Dropping all tables...")
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
        
        # Create tables
        logger.info("Creating new tables...")
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        
        # Create superuser
        logger.info("Creating initial superuser...")
        await create_first_superuser()
        logger.info("Admin user created: %s", settings.FIRST_SUPERUSER_USERNAME)
        
    except Exception as e:
        logger.error("Error: %s", e)
        raise
    finally:
        await engine.dispose()

if __name__ == "__main__":
    logger.info("Starting database reset")
    asyncio.run(reset_database())
    logger.info("Database reset completed")
