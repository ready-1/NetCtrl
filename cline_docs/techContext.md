# Technologies Used
- Git for version control
  - .gitignore configured for Python/Django projects
  - TLS certificate directories maintained with .gitkeep files

# Development Setup
- Git repository initialized and configured
- Version control ignores:
  - Python bytecode and cache
  - Django database and media files
  - Environment files
  - IDE configs
  - System files
  - TLS/certificates
  - Test artifacts

# Technical Constraints
- TLS certificates must be managed separately (ignored by git)
- Sensitive environment variables stored in .env (ignored by git)
