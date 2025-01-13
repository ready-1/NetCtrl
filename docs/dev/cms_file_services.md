# CMS File Services

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
