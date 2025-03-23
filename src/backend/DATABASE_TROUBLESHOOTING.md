# Database Troubleshooting Guide

This document provides solutions for common database issues in the NetCtrl CMS.

## Fixing "relation 'user' does not exist" Error

If you're seeing the error `relation "user" does not exist` during startup or database operations, follow these steps to resolve it:

### Solution 1: Wait for Retry Logic to Complete

The application includes retry logic for database operations during startup. If you see warnings like:

```
WARNING:app.db.init_db:Database error on attempt 1/5: (sqlalchemy.dialects.postgresql.asyncpg.ProgrammingError) <class 'asyncpg.exceptions.UndefinedTableError'>: relation "user" does not exist
```

Simply wait for the retry process to complete. The system will attempt 5 retries by default, which is often sufficient for the migrations to finish creating the tables.

### Solution 2: Reset the Database and Rerun Migrations

If retries don't resolve the issue, you can reset the database:

1. Stop all containers:
   ```bash
   docker compose down
   ```

2. Remove the database volume to start fresh:
   ```bash
   docker volume rm netctrl_postgres_data
   ```

3. Restart the services:
   ```bash
   docker compose up
   ```

4. If the issue persists, you may need to manually trigger migrations:
   ```bash
   docker compose exec backend alembic upgrade head
   ```

### Solution 3: Check Alembic Migration Chain

If the above solutions don't work, the issue may be with the Alembic migration chain:

1. Ensure all migration files in `src/backend/alembic/versions` have proper dependencies:
   - Check that each migration file has a valid `down_revision` pointing to the previous migration
   - Verify that there are no duplicate revision IDs

2. Validate the migration history:
   ```bash
   docker compose exec backend alembic history
   ```

3. If you see "Multiple head revisions", you need to create a merge migration:
   ```bash
   docker compose exec backend alembic merge heads -m "merge_heads"
   ```

### Solution 4: Inspect Database Schema

If the issue persists, inspect the actual database schema:

1. Connect to the database:
   ```bash
   docker compose exec database psql -U postgres -d cms_db
   ```

2. List all tables:
   ```sql
   \dt
   ```

3. Check if the table exists with a different name:
   ```sql
   \dt *user*
   ```

4. If you find a table with a similar name (like `users` instead of `user`), you may need to update your code or migrations to use the correct table name.

## Frontend and Navigation Issues

### Frontend Troubleshooting

If the frontend is not building or running properly:

1. Check dependency installation:
   ```bash
   docker compose exec frontend npm install
   ```

2. Install specific missing dependencies:
   ```bash
   docker compose exec frontend npm install dompurify react-quill @tanstack/react-query
   ```

3. Restart the frontend container:
   ```bash
   docker compose restart frontend
   ```

### NGINX Configuration

If you're experiencing routing or proxy issues:

1. Check the NGINX configuration:
   ```bash
   docker compose exec nginx cat /etc/nginx/conf.d/default.conf
   ```

2. Ensure the location blocks are correctly defined with proper priorities:
   - Exact matches (using `=`) have highest priority
   - Prefix matches with `^~` have higher priority than regex matches
   - Regular expression matches (using `~*` or `~`) are evaluated in order
   - Prefix matches without `^~` have lowest priority

3. Test if NGINX is functioning properly:
   ```bash
   docker compose exec nginx curl -i localhost/health
   ```

4. If needed, update the NGINX configuration and reload:
   ```bash
   docker compose cp your-config.conf nginx:/etc/nginx/conf.d/default.conf
   docker compose exec nginx nginx -s reload
   ```

### Accessing the CMS

The NetCtrl CMS provides different URLs for accessing different parts of the system:

- **System Status Page**: http://localhost/status
  - Shows the current status of all system components
  - Quick view of system health

- **CMS Frontend**: http://localhost/app/
  - Access the React frontend UI
  - Requires user login with proper credentials

- **API Documentation**: http://localhost/api/v1/docs
  - Swagger UI for API endpoints
  - Test API endpoints directly

- **Default Login Credentials**:
  - Username: `admin`
  - Password: `admin123`

## Additional Issues

### Superuser Creation Failures

If the superuser creation is failing after database initialization:

1. Check the retry logic in `app/db/init_db.py`
2. Ensure the superuser creation code matches the current user model schema
3. Manually create a superuser if needed:
   ```bash
   docker compose exec backend python -c "
   from app.core.security import get_password_hash
   from app.db.session import get_db
   from app.models.user import User
   from fastapi.encoders import jsonable_encoder
   from sqlalchemy.ext.asyncio import AsyncSession
   import asyncio

   async def create_superuser():
       async for db in get_db():
           db_obj = User(
               username='admin',
               email='admin@example.com',
               hashed_password=get_password_hash('admin123'),
               is_superuser=True,
               is_active=True,
               role='admin'
           )
           db.add(db_obj)
           await db.commit()
           print('Superuser created successfully')

   asyncio.run(create_superuser())
   "
   ```

### Database Connection Issues

If you're experiencing database connection problems:

1. Verify the database container is running:
   ```bash
   docker compose ps database
   ```

2. Check the database logs:
   ```bash
   docker compose logs database
   ```

3. Ensure the connection string in `alembic.ini` and environment variables match the database container settings.

## Schema Reference

For reference, here's the expected schema for the main tables:

### User Table
```sql
CREATE TABLE "user" (
    id UUID PRIMARY KEY,
    email VARCHAR(255),
    username VARCHAR(255) NOT NULL UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_superuser BOOLEAN DEFAULT FALSE,
    is_verified BOOLEAN DEFAULT FALSE,
    role VARCHAR(50) NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_login TIMESTAMP WITH TIME ZONE
);
```

### Content Table
```sql
CREATE TABLE content (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    body TEXT,
    content_type VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_by UUID REFERENCES "user"(id),
    updated_by UUID REFERENCES "user"(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### Content Permissions Table
```sql
CREATE TABLE content_permission (
    id SERIAL PRIMARY KEY,
    content_id INTEGER REFERENCES content(id) ON DELETE CASCADE,
    role VARCHAR(50) NOT NULL,
    can_view BOOLEAN DEFAULT FALSE,
    can_edit BOOLEAN DEFAULT FALSE,
    can_delete BOOLEAN DEFAULT FALSE
);
