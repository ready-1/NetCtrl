# Active Context:

**Purpose:** This file provides a concise overview of the current work focus, immediate next steps, and active decisions for the CMS with RBAC project. It is intended to be a frequently referenced, high-level summary to maintain project momentum and team alignment.

**Use Guidelines:**
- **Current Work Focus:**  List the 2-3 *most critical* tasks currently being actively worked on. Keep descriptions concise and action-oriented.
- **Next Steps:**  List the immediate next steps required to advance the project. Prioritize and order these steps for clarity.
- **Active Decisions and Considerations:** Document key decisions currently being considered or actively debated. Capture the essence of the decision and any open questions.
- **Do NOT include:** Detailed task breakdowns, historical changes, long-term plans (these belong in other memory bank files like `progress.md` or dedicated documentation).
- **Maintain Brevity:** Keep this file concise and focused on the *current* state of the project. Regularly review and prune outdated information.

## Current Work Focus:

- Initializing the CRCT system for the CMS with RBAC project
- Setting up core files and dependency trackers
- Preparing for MVP1 development with air-gapped environment requirements

## Next Steps:

1. Complete CRCT system initialization
2. Plan Docker environment setup for air-gapped operation (MVP1)
3. Design frontend architecture with Material UI components
4. Develop approach for bundling dependencies for offline use

## Active Decisions and Considerations:

- Determining the optimal Docker container structure for the CMS system in air-gapped environments
- Planning strategy for bundling all dependencies locally (no CDNs or external package repositories)
- Considering specific RBAC implementation details with FastAPI Users in offline environments
- Evaluating Material UI component structure for responsive design
- Planning approach for large file uploads (up to 2GB) in an air-gapped environment
