# CMS with RBAC

A Content Management System with Role-Based Access Control (RBAC), deployed using Docker containers.

## Docker Environment Setup

This project uses Docker Compose to orchestrate containers for the following services:
- FastAPI Backend
- Postgres Database
- React Frontend with Material UI
- NGINX Reverse Proxy
- Syslog for Centralized Logging
- Local Package Repositories for Air-gapped Operation

## Environment Variables

Environment variables are managed through a structured system:

```
env-config/
├── .env.example            # Master template with all variables
├── .env                    # Local development variables (gitignored)
├── services/
│   ├── backend/            # FastAPI-specific variables
│   ├── database/           # Postgres-specific variables
│   ├── frontend/           # React-specific variables
│   ├── nginx/              # NGINX-specific variables
│   └── syslog/             # Syslog-specific variables
└── scripts/
    └── validate-env.sh     # Script to verify all required env vars
    └── init-env.sh         # Script to initialize .env files from templates
```

## Getting Started

1. Initialize environment variables:
   ```bash
   chmod +x env-config/scripts/init-env.sh
   ./env-config/scripts/init-env.sh
   ```

2. Edit the generated `.env` files with your specific configuration values.

3. Validate environment variables:
   ```bash
   cd env-config/scripts
   ./validate-env.sh
   ```

4. Start the containers:
   ```bash
   docker compose up -d
   ```

5. Access the application at http://localhost

## Air-gapped Operation

This project is designed to work in air-gapped environments with no internet access:

- Local PyPI mirror (devpi) for Python dependencies
- Local NPM registry (verdaccio) for JavaScript dependencies
- All Material UI components served locally
- No CDN dependencies

## Development

For development, you can use the following commands:

- Start individual services:
  ```bash
  docker compose up backend database -d
  ```

- View logs:
  ```bash
  docker compose logs -f
  ```

- Access specific container:
  ```bash
  docker compose exec backend bash
  ```

## Configuration

See the `.env.example` file for all available configuration options.
