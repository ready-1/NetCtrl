# NetCtrl CMS Database Troubleshooting Guide

## Common Database Issues

### 1. "Relation Does Not Exist" Error

**Symptom:** Error message in logs: `relation "user" does not exist` despite migrations appearing to complete successfully.

**Cause:** This is typically caused by one of the following:
- Alembic migration chain issues (incorrect revision IDs or dependencies)
- Table name mismatch between models and migrations
- Schema changes not properly reflected in migration files

**Solution:**
1. Check Alembic migration files for proper revision ID format (should be UUID-like strings, not plain text)
2. Verify migration dependencies (`down_revision` value in migration files)
3. Reset the database completely using the database reset script:
   ```bash
   docker compose exec backend bash -c "cd /app && ./scripts/reset_database.sh"
   ```

### 2. Multiple Head Revisions Error

**Symptom:** Alembic shows "Multiple head revisions" error during migration.

**Cause:** Multiple migration files claiming to be the latest revision (no `down_revision` or conflicting chain).

**Solution:**
1. Check all migration files to ensure proper `down_revision` values creating a single chain
2. Run a merge migration if appropriate:
   ```bash
   docker compose exec backend alembic merge heads
   ```

### 3. Type Already Exists Error

**Symptom:** Error like "type `user_role` already exists" during migration.

**Cause:** Migration tries to create a PostgreSQL ENUM type that already exists.

**Solution:** Modify migration file to handle existing types:
```python
# Check if enum exists before creating
op.execute("CREATE TYPE user_role AS ENUM ('admin', 'manager', 'user') IF NOT EXISTS")
# Or use try/except
try:
    op.execute("CREATE TYPE user_role AS ENUM ('admin', 'manager', 'user')")
except Exception:
    pass  # Type already exists
```

## Database Reset

If you need to completely reset the database and recreate all tables:

```bash
docker compose exec backend bash -c "cd /app && ./scripts/reset_database.sh"
```

This script will:
1. Drop all tables
2. Create new tables based on the application models
3. Create a default superuser account

The default superuser credentials after reset are:
- Username: `admin`
- Password: `admin123`

## Fixing Alembic Migration Chain Issues

If you need to correct the Alembic migration chain:

1. Fix any incorrect revision IDs (they should use UUID format, e.g., `'bce38eb0d123'`)
2. Ensure proper `down_revision` values to create a single chain
3. Restart the backend service:
   ```bash
   docker compose restart backend
   ```
4. If problems persist, reset the database using the reset script

## Checking Database State

To check the current state of the database:

```bash
# View Alembic migration history
docker compose exec backend alembic history

# Check current revision
docker compose exec backend alembic current

# Show pending migrations
docker compose exec backend alembic heads
```

## Advanced Troubleshooting: Manual Database Connection

For direct database access:

```bash
docker compose exec database psql -U postgres -d cms_db
```

Useful PostgreSQL commands:
```sql
-- List all tables
\dt

-- Check if a specific table exists
\dt user

-- View table schema
\d user

-- Check Alembic version table
SELECT * FROM alembic_version;
