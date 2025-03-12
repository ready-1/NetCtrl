import asyncio
import os
import sys
from logging.config import fileConfig
from typing import Dict, Any

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import AsyncEngine

from alembic import context

# Import our models and configuration
# Add the parent directory to sys.path to allow importing from the app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db.base import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Use the connection string from alembic.ini - we'll override it at runtime
# but keep the one in the config for autogeneration without DB connection
sqlalchemy_url = config.get_main_option("sqlalchemy.url")

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata

# Get revision environment setting
revision_environment = config.get_main_option("revision_environment", "false").lower() in ("true", "1", "t")

# other values from the config, defined by the needs of env.py,
# can be acquired:
revision_environment = config.get_main_option("revision_environment", "false") == "true"
cmd_opts = context.get_x_argument(as_dictionary=True)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    """Run migrations in 'online' mode with a connection."""
    context.configure(
        connection=connection, 
        target_metadata=target_metadata,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.
    
    Support async engine.
    """
    # For revision generation, don't actually try to connect to the database
    if context.get_tag_argument() == 'autogenerate' and not revision_environment:
        # Just run the migration with the metadata and let Alembic figure out the changes
        # without connecting to a database
        context.configure(
            url=sqlalchemy_url,
            target_metadata=target_metadata,
            literal_binds=True,
            dialect_opts={"paramstyle": "named"},
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()
        return

    # Import settings here to avoid import errors when running offline
    from app.core.config import settings
    
    # Override the URL with the one from settings
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = settings.SQLALCHEMY_DATABASE_URI
    
    try:
        # Create async engine
        connectable = AsyncEngine(
            engine_from_config(
                configuration,
                prefix="sqlalchemy.",
                poolclass=pool.NullPool,
                future=True,
            )
        )

        # Use async connection for migrations
        async with connectable.connect() as connection:
            await connection.run_sync(do_run_migrations)

        # Close the connection once migrations are done
        await connectable.dispose()
    except Exception as e:
        print(f"Error during migration: {e}")
        # If running migrations fails (e.g., during revision), fallback to offline mode
        run_migrations_offline()


# Choose the appropriate migration function
if context.is_offline_mode():
    run_migrations_offline()
else:
    # If we're generating a revision, don't run in asyncio
    if context.get_tag_argument() == 'autogenerate' and not revision_environment:
        run_migrations_offline()
    else:
        # Run async migrations in event loop
        asyncio.run(run_migrations_online())
