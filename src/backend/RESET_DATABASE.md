# Database Reset Tool for NetCtrl CMS

This utility allows you to completely reset the database, recreating all tables and setting up the default admin user. This is useful for:

- Initial setup
- Recovering from database corruption
- Testing with a clean database
- Resolving authentication or data issues

## What This Script Does

1. Drops all tables in the database
2. Creates new tables based on the application models
3. Creates a default superuser account with credentials:
   - Username: `admin`
   - Password: `admin`

## Usage Instructions

We provide two scripts for database reset:

### 1. Shell Script (Recommended)

The shell script automatically detects your environment and runs the appropriate command:

```bash
# From the project root directory
./src/backend/scripts/reset_database.sh

# OR from the backend directory
./scripts/reset_database.sh
```

This script will:
- Detect if you're running inside Docker
- Use Docker Compose if available
- Fall back to direct Docker commands if needed
- Execute locally if not in a containerized environment

### 2. Python Script (Direct)

If you prefer to run the Python script directly:

#### Inside Docker Container
```bash
# If inside the running container
python scripts/reset_db.py

# If outside the container
docker exec -it netctrl-backend python scripts/reset_db.py

# Or with Docker Compose
docker compose exec backend python scripts/reset_db.py
```

#### Direct Local Execution
```bash
# If connecting to a local database
python src/backend/scripts/reset_db.py

# If connecting to a database in Docker
POSTGRES_SERVER=localhost python src/backend/scripts/reset_db.py
```

## Troubleshooting

1. **Database connection error**: Ensure the database container is running and properly configured in `app/core/config.py`

2. **Permission errors**: Ensure your database user has privileges to drop and create tables

3. **Import errors**: Make sure you're executing the script from the correct directory context so Python can find the app modules

4. **Container not found**: If using Docker, ensure the backend container is running before executing the reset command

## After Reset

After a successful reset, you should be able to login using:
- Username: `admin`
- Password: `admin`

Remember to change the default password in a production environment!
