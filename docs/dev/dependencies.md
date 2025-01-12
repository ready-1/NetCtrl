# System Dependencies

## Python Environment
- Python 3.9+
- Poetry for dependency management

## Core Dependencies
```toml
[tool.poetry.dependencies]
python = "^3.9"
django = "^5.1.4"
```

## Development Dependencies
```toml
[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
black = "^23.7.0"
isort = "^5.12.0"
mypy = "^1.5.0"
pylint = "^2.17.5"
```

## Frontend Dependencies
- Bootstrap CSS framework
- Bootstrap Icons
- HTMX for dynamic updates

## Database
- SQLite (Development)
- PostgreSQL (Production - planned)

## MCP Server Dependencies
- Node.js 18+
- TypeScript
- MCP SDK

## System Requirements
- macOS/Linux/Windows
- Git for version control
- VSCode (recommended)
  - Python extension
  - Django extension
  - GitLens
  - ESLint

## Installation

1. Clone Repository
```bash
git clone <repository-url>
cd netctrl
```

2. Install Poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install Dependencies
```bash
poetry install
```

4. Install Node.js Dependencies
```bash
cd mcp/netctrl-context
npm install
```

5. Setup Development Environment
```bash
poetry shell
python manage.py migrate
python manage.py createsuperuser
```

## Environment Variables
```bash
# Development
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3

# Production
DEBUG=False
SECRET_KEY=your-secure-secret-key
DATABASE_URL=postgres://user:password@localhost:5432/netctrl
ALLOWED_HOSTS=your-domain.com
```

## Development Tools Configuration

### Poetry Configuration
```toml
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.black]
line-length = 88
target-version = ['py39']
include = '\.pyi?$'

[tool.isort]
profile = "black"
multi_line_output = 3

[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pylint.messages_control]
disable = [
    "C0111",  # missing-docstring
    "C0103",  # invalid-name
    "C0330",  # bad-continuation
]
```

### VSCode Settings
```json
{
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

## Maintenance
- Keep dependencies updated using `poetry update`
- Monitor security advisories
- Regular database backups
- Log rotation setup
