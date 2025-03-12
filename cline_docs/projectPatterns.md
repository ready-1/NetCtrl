# Project Patterns Details

## Project-Specific Patterns:

## Code Patterns:

## Tool Usage Patterns:

- **Docker Standards:**
    - **Docker Compose Format:**
        - Use modern Docker Compose specification (no "version" key in docker-compose.yml)
        - Use "name:" to explicitly name the project
        - Group related services using labels
        - Use JSON file logging with size limits for all containers
        - Implement proper health checks for critical services
        - Use "depends_on" with conditions to ensure proper startup order
        
    - **Docker Commands:**
        - Use "docker compose" (no hyphen) instead of "docker-compose" for all commands
        - Examples: "docker compose up -d", "docker compose down", "docker compose ps"
        - For Docker run commands, prefer using the compose file over direct docker run
        - Use "--remove-orphans" when bringing down services to clean up
        
    - **Docker Build:**
        - Use multi-stage builds where appropriate to minimize image size
        - Set explicit container names for critical services
        - Properly handle environment variable defaults
        - Design for resilience to temporary internet outages

- **Memory Bank Files:**
    - `projectbrief.md`: Defines project scope and core requirements (source of truth).
    - `productContext.md`: Explains project purpose, problems solved, and user experience goals.
    - `activeContext.md`: Tracks current work focus, recent changes, and next steps.
    - `systemPatterns.md`: Documents system architecture, design patterns, and component relationships.
    - `techContext.md`:  Specifies technologies, development setup, and technical constraints.
    - `progress.md`:  Tracks what works, what's left to build, and current project status.
    - `userProfile.md`: Contains a dynamic user profile to personalize assistance.
    - `changelog.md`: Contains a log of changes to the project.
    
- **Code Files:**

- **Tools:**
