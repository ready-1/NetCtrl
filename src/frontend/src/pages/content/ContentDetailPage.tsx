import React, { useEffect, useState } from 'react';
import { useParams, useNavigate, Link as RouterLink } from 'react-router-dom';
import {
  Box,
  Breadcrumbs,
  Button,
  Container,
  Divider,
  Grid,
  Link,
  Paper,
  Tab,
  Tabs,
  Typography,
  useTheme,
} from '@mui/material';
import {
  ArrowBack as ArrowBackIcon,
  Edit as EditIcon,
  Delete as DeleteIcon,
  History as HistoryIcon,
  Visibility as VisibilityIcon,
} from '@mui/icons-material';
import { useAuth } from '../../context/AuthContext';
import routes from '../../config/routes';

/**
 * ContentDetailPage component
 * 
 * Displays detailed information about a content item including:
 * - Content metadata (title, type, status, etc.)
 * - Content body/details
 * - Associated files
 * - Version history
 * - Edit/Delete actions (based on permissions)
 */
const ContentDetailPage: React.FC = () => {
  const theme = useTheme();
  const navigate = useNavigate();
  const { contentId } = useParams<{ contentId: string }>();
  const { hasPermission } = useAuth();
  
  // Tab state
  const [currentTab, setCurrentTab] = useState(0);
  
  // Permissions
  const canEdit = hasPermission('content:edit');
  const canDelete = hasPermission('content:delete');
  
  // Mock content data
  const [content, setContent] = useState({
    id: contentId || '1',
    title: 'Sample Content Item',
    type: 'Page',
    status: 'published',
    createdBy: 'admin',
    createdAt: '2025-03-01',
    updatedAt: '2025-03-15',
    body: 'This is a sample content item for demonstration purposes. In a real application, this would contain the actual content data retrieved from the API.',
    version: 3,
    files: [
      { id: '1', name: 'image.jpg', type: 'image/jpeg', size: 1024 * 1024 * 2 },
      { id: '4', name: 'document.pdf', type: 'application/pdf', size: 1024 * 1024 * 5 },
    ],
    versions: [
      { id: 3, updatedAt: '2025-03-15', updatedBy: 'admin' },
      { id: 2, updatedAt: '2025-03-10', updatedBy: 'editor' },
      { id: 1, updatedAt: '2025-03-01', updatedBy: 'admin' },
    ],
  });
  
  // Handle tab change
  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setCurrentTab(newValue);
  };
  
  // Handle delete
  const handleDelete = () => {
    // In a real application, this would make an API call to delete the content
    alert('Content deleted successfully');
    navigate(routes.content.list);
  };
  
  // Load content data
  useEffect(() => {
    // In a real application, this would make an API call to fetch the content
    // For now, we'll use the mock data
  }, [contentId]);

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      {/* Breadcrumbs navigation */}
      <Breadcrumbs sx={{ mb: 2 }}>
        <Link component={RouterLink} to="/" color="inherit">
          Dashboard
        </Link>
        <Link component={RouterLink} to={routes.content.list} color="inherit">
          Content
        </Link>
        <Typography color="text.primary">View Content</Typography>
      </Breadcrumbs>
      
      {/* Page header */}
      <Box sx={{ mb: 4, display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
        <Box>
          <Button
            startIcon={<ArrowBackIcon />}
            component={RouterLink}
            to={routes.content.list}
            sx={{ mb: 2 }}
          >
            Back to Content List
          </Button>
          <Typography variant="h4" component="h1" gutterBottom>
            {content.title}
          </Typography>
          <Typography variant="subtitle1" color="text.secondary">
            {content.type} • Last updated {content.updatedAt} by {content.createdBy} • Version {content.version}
          </Typography>
        </Box>
        
        {/* Action buttons */}
        <Box>
          {canEdit && (
            <Button
              variant="contained"
              color="primary"
              startIcon={<EditIcon />}
              component={RouterLink}
              to={routes.content.edit(content.id)}
              sx={{ mr: 1 }}
            >
              Edit
            </Button>
          )}
          
          {canDelete && (
            <Button
              variant="outlined"
              color="error"
              startIcon={<DeleteIcon />}
              onClick={handleDelete}
            >
              Delete
            </Button>
          )}
        </Box>
      </Box>
      
      {/* Content tabs */}
      <Paper sx={{ mb: 4 }}>
        <Tabs value={currentTab} onChange={handleTabChange}>
          <Tab label="Content" />
          <Tab label="Files" />
          <Tab label="Version History" />
        </Tabs>
        
        <Divider />
        
        {/* Content tab panel */}
        {currentTab === 0 && (
          <Box sx={{ p: 3 }}>
            <Typography variant="body1" paragraph>
              {content.body}
            </Typography>
          </Box>
        )}
        
        {/* Files tab panel */}
        {currentTab === 1 && (
          <Box sx={{ p: 3 }}>
            {content.files.length > 0 ? (
              <Grid container spacing={2}>
                {content.files.map((file) => (
                  <Grid item xs={12} key={file.id}>
                    <Paper sx={{ p: 2, display: 'flex', alignItems: 'center' }}>
                      <Box sx={{ flexGrow: 1 }}>
                        <Typography variant="subtitle1">{file.name}</Typography>
                        <Typography variant="body2" color="text.secondary">
                          {file.type.split('/')[1].toUpperCase()} • {(file.size / (1024 * 1024)).toFixed(2)} MB
                        </Typography>
                      </Box>
                      <Button
                        component={RouterLink}
                        to={routes.files.detail(file.id)}
                        startIcon={<VisibilityIcon />}
                      >
                        View
                      </Button>
                    </Paper>
                  </Grid>
                ))}
              </Grid>
            ) : (
              <Typography variant="body1" color="text.secondary">
                No files associated with this content.
              </Typography>
            )}
          </Box>
        )}
        
        {/* Version history tab panel */}
        {currentTab === 2 && (
          <Box sx={{ p: 3 }}>
            {content.versions.map((version) => (
              <Box key={version.id} sx={{ mb: 2, display: 'flex', alignItems: 'center' }}>
                <HistoryIcon sx={{ mr: 2, color: 'text.secondary' }} />
                <Box sx={{ flexGrow: 1 }}>
                  <Typography variant="subtitle1">
                    Version {version.id}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    Updated on {version.updatedAt} by {version.updatedBy}
                  </Typography>
                </Box>
                <Button variant="outlined" size="small">
                  View Version
                </Button>
              </Box>
            ))}
          </Box>
        )}
      </Paper>
    </Container>
  );
};

export default ContentDetailPage;
