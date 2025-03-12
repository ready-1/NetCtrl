"""
Initial database setup script

This script is called from start.sh to initialize the database with
the first superuser if no users exist yet.
"""

import asyncio
import logging
from app.db.init_db import create_first_superuser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def init() -> None:
    """Create first superuser if it doesn't exist"""
    logger.info("Creating first superuser if needed")
    await create_first_superuser()
    logger.info("Superuser check completed")


def main() -> None:
    """Entry point for script execution"""
    asyncio.run(init())


if __name__ == "__main__":
    main()
