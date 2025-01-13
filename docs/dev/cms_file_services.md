# CMS File Services

## Tag Management

### Overview
The CMS supports tagging capabilities for files, allowing for better organization and searchability. Tags can be added, removed, and used to filter files.

### Features
- Add/remove tags from files
- View all tags in the system
- Filter files by tags
- Tag validation and error handling
- Cached tag operations for performance

### Implementation
- JSONField storage for flexible tag lists
- Tag validation rules:
  - Non-empty string
  - Max 50 characters
  - Alphanumeric with hyphens and underscores
- Atomic operations for data consistency
- Cache invalidation on updates

### Security
- User authentication required
- Input validation
- CSRF protection
- Error handling for all operations

### UI Components
- Tag display in file browser
- Tag management modal
- Add/remove tag interface
- Tag filtering options

## Move Operation

### Overview
The move operation allows users to relocate files and folders within the CMS directory structure. The implementation follows established security patterns and error handling approaches.

### Components

#### Backend
- URL endpoint: `/move/`
- View function: `move_item`
- Security measures:
  - Path traversal prevention
  - Permission validation
  - CSRF protection
  - Input sanitization

#### Frontend
- Move button in file/folder actions
- Modal dialog with directory tree
- Interactive directory selection
- Error feedback display
- Full item click area for navigation

### Error Handling

#### Validation Checks
- Invalid source/destination paths
- Name conflicts at destination
- Moving folder into itself
- Permission issues
- Path traversal attempts

#### User Feedback
- Clear error messages in modal
- Loading states during operation
- Success/failure notifications

### Security Considerations

#### Path Validation
- Normalization of paths
- Prevention of directory traversal
- Validation of source/destination

#### Permission Checks
- User authentication required
- CSRF protection on all operations
- Proper error handling for unauthorized actions

### Implementation Details

#### Directory Tree
- Dynamic loading of directories
- Visual selection feedback
- Current path highlighting
- Root directory access
- New folder creation at any level

#### Move Operation Flow
1. User clicks move button
2. Modal opens with directory tree
3. User selects destination
4. Validation occurs
5. Move executes if valid
6. Feedback provided to user

#### UI Improvements
- Full item click area for better UX
- Proper button group interaction
- Consistent behavior in list/grid views
- Visual feedback for clickable areas

### Future Considerations
- Bulk move operations
- Drag and drop interface
- Progress tracking for large moves
- Conflict resolution options
