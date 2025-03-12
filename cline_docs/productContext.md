# Product Context:

## Why This Project Exists:

This Content Management System (CMS) with Role-Based Access Control (RBAC) is being developed to provide organizations with a secure, flexible solution for managing content while maintaining strict access controls. The system fills the need for a modern CMS that properly segregates user permissions based on organizational roles and responsibilities, even in air-gapped environments without internet access.

## Problems It Solves:

1. **Access Control Challenges**: Many existing CMS solutions have limited or overly complex permission systems. This project implements a clear RBAC model with predefined roles (superuser, admin, editor, viewer) to easily control who can access, create, edit, or delete content.

2. **Large File Management**: The system supports uploads of large binary files (up to 2GB), addressing limitations in many current CMS platforms that restrict file sizes.

3. **User Approval Workflow**: By implementing an "approved" flag for new users and an "inactive" flag for temporary access suspension, the system provides administrators with granular control over the user lifecycle.

4. **Modern Deployment**: The Docker-based implementation ensures consistent deployment across environments and proper isolation of components.

5. **Issue Tracking Integration**: The GitHub issue submission feature enables authenticated users to report problems or request features directly from within the CMS.

6. **Air-Gapped Operation**: The system can function in environments without internet access, with all dependencies, frameworks, and libraries served locally.

7. **Consistent UI**: By using Material UI components, the system provides a cohesive, responsive user interface that works across devices while being completely served from local resources.

## How It Should Work:

1. **User Registration and Authentication**:
   - New users register through the registration screen.
   - Admin users approve new accounts by setting the "approved" flag to true.
   - Users login with valid credentials, requiring "approved" = true and "inactive" = false.

2. **Role-Based Permissions**:
   - Superusers have complete system access.
   - Admins can manage users and have full content control.
   - Editors can create and modify content but have limited administrative capabilities.
   - Viewers can only view content without modification rights.

3. **Content Management**:
   - Authorized users can create, read, update, and delete content based on their role.
   - Large file uploads (up to 2GB) are supported through properly configured NGINX and API endpoints.

4. **Administrative Functions**:
   - User management interface for approving new users or marking accounts as inactive.
   - Role assignment and modification.

5. **GitHub Issue Submission**:
   - Authenticated users can submit issues directly to GitHub through a dedicated interface.
   - In air-gapped environments, issues are queued locally for later synchronization.

6. **Offline Operation**:
   - All dependencies, frameworks, and libraries are served locally.
   - No external API calls or CDN dependencies.
   - System functions completely within the internal network.

## User Experience Goals:

1. **Simplicity**: Intuitive interfaces for all user roles, with clear navigation and contextual actions using Material UI components.

2. **Responsiveness**: Mobile-first design with Material UI ensures usability across devices of various sizes.

3. **Feedback**: Clear error messages and status updates (e.g., "Account not approved," "Account is inactive").

4. **Efficiency**: Streamlined workflows for common tasks to minimize clicks and user friction.

5. **Security**: Robust authentication while maintaining a smooth user experience.

6. **Offline Functionality**: Complete functionality in air-gapped environments with no dependency on external resources.

## Value Proposition / Key Benefits:

1. **Enhanced Security**: Granular RBAC system prevents unauthorized access to sensitive content and administrative functions.

2. **Operational Efficiency**: Clear separation of roles ensures users only see and access what they need for their job functions.

3. **Scalable Content Management**: Support for large files accommodates diverse content needs, from documents to media files.

4. **Deployment Simplicity**: Docker containerization simplifies deployment and environment consistency.

5. **Adaptable Framework**: The system can be extended to accommodate additional features and workflows as organizational needs evolve.

6. **Air-Gapped Operation**: The ability to function in environments without internet access expands usability to high-security, isolated networks.

7. **Consistent Design Language**: Material UI provides a professional, cohesive interface that is both intuitive and visually appealing while being served entirely from local resources.
