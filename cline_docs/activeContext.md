# Active Context:

**Purpose:** This file provides a concise overview of the current work focus, immediate next steps, and active decisions for the CMS with RBAC project. It is intended to be a frequently referenced, high-level summary to maintain project momentum and team alignment.

**Use Guidelines:**
- **Current Work Focus:**  List the 2-3 *most critical* tasks currently being actively worked on. Keep descriptions concise and action-oriented.
- **Next Steps:**  List the immediate next steps required to advance the project. Prioritize and order these steps for clarity.
- **Active Decisions and Considerations:** Document key decisions currently being considered or actively debated. Capture the essence of the decision and any open questions.
- **Do NOT include:** Detailed task breakdowns, historical changes, long-term plans (these belong in other memory bank files like `progress.md` or dedicated documentation).
- **Maintain Brevity:** Keep this file concise and focused on the *current* state of the project. Regularly review and prune outdated information.

## Current Work Focus:

- Standardized Docker command syntax and configuration format
- Fixed Docker container DNS resolution and logging issues
- Implementing Docker environment setup for MVP1

## Next Steps:

1. Implement the FastAPI backend with authentication
2. Resolve backend and frontend container startup issues 
3. Test the system's resilience during temporary internet outages
4. Leverage the Docker helper script for container management

## Active Decisions and Considerations:

- Standardized on "docker compose" command syntax (without hyphen) for all operations
- Created Docker helper script to ensure consistent use of modern Docker syntax
- Using direct connections to public package repositories (PyPI, NPM) as system will be online for installations
- Designing Docker container structure that handles periodic internet outages gracefully
- Creating a comprehensive environment variable management strategy for all containers
- Using simplified network architecture (single shared network) for reliable DNS resolution
- Using file-based logging instead of syslog logging to avoid dependency on DNS resolution
- Caching required dependencies when online to maintain functionality during outages
- Structuring volume mounts for persistent data in the containerized environment
- Determining the best approach for container health checks and startup order
- Configuring NGINX for handling large file uploads (up to 2GB)
