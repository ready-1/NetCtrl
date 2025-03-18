# CMS Backend Testing Plan

## Testing Philosophy

The CMS backend testing suite follows these key principles:

1. **Clean isolation** - Each test runs with a fresh database state to prevent test interdependence
2. **Proper async handling** - Correctly awaiting fixtures and using AsyncClient for all tests
3. **Composable fixtures** - Small, focused fixtures that can be combined for different test scenarios
4. **Clear organization** - Tests grouped by functionality (auth, content, files, permissions)
5. **Comprehensive coverage** - Testing happy paths and error cases
6. **Real-world scenarios** - Integration tests that mirror actual user workflows

## Test Structure

```
tests/
├── conftest.py               # Core fixtures (DB, client, users, auth tokens)
├── test_auth.py              # Authentication tests
├── test_user_management.py   # User CRUD operations
├── test_content_crud.py      # Content CRUD operations
├── test_file_upload.py       # File operations
├── test_permissions.py       # RBAC permission tests
└── test_integration.py       # Complex workflows
```

## Key Fixtures

1. **Database fixtures**:
   - `test_db_session` - Creates a clean async SQLite DB for each test
   - `apply_migrations` - Ensures schema is applied

2. **Authentication fixtures**:
   - `admin_user`, `editor_user`, `regular_user` - Pre-created users with different roles
   - `admin_token`, `editor_token`, `user_token` - Authentication tokens

3. **Content fixtures**:
   - `create_content` - Factory fixture to create content with specified attributes
   - `sample_contents` - Pre-populated content for listing/filtering tests

4. **File fixtures**:
   - `temp_file` - Creates temporary test files of different types
   - `uploaded_file` - Pre-uploaded file with metadata

## Test Categories

1. **Authentication Tests**:
   - Login with valid/invalid credentials
   - Token validation
   - Permission checks

2. **Content Tests**:
   - Create content (validating all fields)
   - Read content (by ID, pagination, filtering, search)
   - Update content (full and partial updates)
   - Delete content (with permission checks)
   - Content versioning (create, retrieve, compare)

3. **File Tests**:
   - Upload files (different types and sizes)
   - Associate files with content
   - List files (pagination, filtering)
   - Download files
   - Delete files (with permission checks)

4. **Permission Tests**:
   - Role-based access to content
   - Object-level permissions
   - Permission templates
   - Permission inheritance

5. **Integration Tests**:
   - Content workflow (create → update → publish)
   - Content with files (create content with attachments)
   - Version management workflow

## Implementation Approach

1. Fix the `conftest.py` to properly handle async fixtures
2. Implement the base test fixtures for authentication
3. Create content and file fixtures
4. Implement the test cases starting with authentication and permissions
5. Add content CRUD tests
6. Add file upload tests
7. Finish with integration tests

## Docker Considerations

- Tests are designed to run both locally and within Docker containers
- Environment-specific configurations are handled via environment variables
- Test database is isolated from production database

## Test Data Management

- Test data is generated programmatically for consistency
- Test files use standardized formats and reasonable sizes
- All test data is cleaned up after tests complete

## Performance Considerations

- Tests are optimized to run efficiently in CI/CD pipelines
- Parameterized tests are used for testing multiple scenarios
- Heavy tests are marked for optional execution in quick test runs
