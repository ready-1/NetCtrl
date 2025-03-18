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
  Typography,
  useTheme,
} from '@mui/material';
import {
  ArrowBack as ArrowBackIcon,
  Delete as DeleteIcon,
  Download as DownloadIcon,
  Edit as EditIcon,
} from '@mui/icons-material';
import { useAuth } from '../../context/AuthContext';
import routes from '../../config/routes';

// File type definition
interface FileDetails {
  id: string;
  name: string;
  type: string;
  size: number;
  uploadDate: string;
  uploadedBy: string;
  url: string;
  contentId?: string;
  metadata: {
    width?: number;
    height?: number;
    duration?: number;
    pages?: number;
    [key: string]: any;
  };
}

/**
 * FileDetailPage component
 * 
 * Displays detailed information about a file:
 * - File metadata (name, type, size, etc.)
 * - File preview when possible
 * - Associated content
 * - Download/delete actions
 */
const FileDetailPage: React.FC = () => {
  const theme = useTheme();
  const navigate = useNavigate();
  const { fileId } = useParams<{ fileId: string }>();
  const { hasPermission } = useAuth();
  
  // Permissions
  const canEdit = hasPermission('file:edit');
  const canDelete = hasPermission('file:delete');
  
  // File state
  const [file, setFile] = useState<FileDetails | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  
  // Load file data
  useEffect(() => {
    // In a real app, this would be an API call
    // For demo purposes, using mock data
    setLoading(true);
    
    // Simulate API call
    setTimeout(() => {
      if (fileId === '999') {
        setError('File not found');
        setLoading(false);
        return;
      }
      
      // Mock data
      setFile({
        id: fileId || '1',
        name: 'sample-image.jpg',
        type: 'image/jpeg',
        size: 1024 * 1024 * 2.5, // 2.5 MB
        uploadDate: '2025-03-15',
        uploadedBy: 'admin',
        url: 'https://via.placeholder.com/800x600',
        contentId: '4',
        metadata: {
          width: 800,
          height: 600,
          description: 'Sample image for demonstration purposes',
        },
      });
      
      setLoading(false);
    }, 500);
  }, [fileId]);
  
  // Handle delete
  const handleDelete = () => {
    // In a real app, this would be an API call
    // For demo purposes, just showing an alert
    if (window.confirm('Are you sure you want to delete this file?')) {
      alert('File deleted successfully');
      navigate(routes.files.list);
    }
  };
  
  // Handle download
  const handleDownload = () => {
    // In a real app, this would trigger a file download
    // For demo purposes, just showing an alert
    alert('Downloading file...');
  };
  
  if (loading) {
    return (
      <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
        <Typography>Loading file details...</Typography>
      </Container>
    );
  }
  
  if (error) {
    return (
      <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
        <Typography color="error">{error}</Typography>
        <Button
          component={RouterLink}
          to={routes.files.list}
          sx={{ mt: 2 }}
        >
          Return to File List
        </Button>
      </Container>
    );
  }
  
  if (!file) {
    return null;
  }

  // Determine file preview component based on type
  const renderFilePreview = () => {
    if (file.type.startsWith('image/')) {
      return (
        <Box
          component="img"
          src={file.url}
          alt={file.name}
          sx={{
            maxWidth: '100%',
            maxHeight: 500,
            objectFit: 'contain',
            display: 'block',
            margin: '0 auto',
          }}
        />
      );
    }
    
    if (file.type.startsWith('video/')) {
      return (
        <Box
          component="video"
          controls
          sx={{
            width: '100%',
            maxHeight: 500,
          }}
        >
          <source src={file.url} type={file.type} />
          Your browser does not support the video tag.
        </Box>
      );
    }
    
    if (file.type === 'application/pdf') {
      return (
        <Box
          component="iframe"
          src={file.url}
          sx={{
            width: '100%',
            height: 500,
            border: 'none',
          }}
        />
      );
    }
    
    // Default preview (file icon)
    return (
      <Box sx={{ textAlign: 'center', py: 4 }}>
        <Typography variant="body1">
          Preview not available for this file type. Please download the file to view it.
        </Typography>
      </Box>
    );
  };

  // Format file size
  const formatFileSize = (bytes: number): string => {
    if (bytes === 0) return '0 Bytes';
    
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      {/* Breadcrumbs navigation */}
      <Breadcrumbs sx={{ mb: 2 }}>
        <Link component={RouterLink} to="/" color="inherit">
          Dashboard
        </Link>
        <Link component={RouterLink} to={routes.files.list} color="inherit">
          Files
        </Link>
        <Typography color="text.primary">View File</Typography>
      </Breadcrumbs>
      
      {/* Page header */}
      <Box sx={{ mb: 4, display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
        <Box>
          <Button
            startIcon={<ArrowBackIcon />}
            component={RouterLink}
            to={routes.files.list}
            sx={{ mb: 2 }}
          >
            Back to File List
          </Button>
          <Typography variant="h4" component="h1" gutterBottom>
            {file.name}
          </Typography>
          <Typography variant="subtitle1" color="text.secondary">
            {file.type} • {formatFileSize(file.size)} • Uploaded on {file.uploadDate} by {file.uploadedBy}
          </Typography>
        </Box>
        
        {/* Action buttons */}
        <Box>
          <Button
            variant="outlined"
            startIcon={<DownloadIcon />}
            onClick={handleDownload}
            sx={{ mr: 1 }}
          >
            Download
          </Button>
          
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
      
      {/* File preview */}
      <Paper sx={{ mb: 4, p: 2 }}>
        <Typography variant="h6" gutterBottom>
          File Preview
        </Typography>
        <Divider sx={{ mb: 2 }} />
        {renderFilePreview()}
      </Paper>
      
      {/* File metadata */}
      <Paper sx={{ mb: 4, p: 3 }}>
        <Typography variant="h6" gutterBottom>
          File Details
        </Typography>
        <Divider sx={{ mb: 2 }} />
        
        <Grid container spacing={2}>
          <Grid item xs={12} sm={4}>
            <Typography variant="subtitle2" color="text.secondary">
              File Name
            </Typography>
            <Typography variant="body1">
              {file.name}
            </Typography>
          </Grid>
          
          <Grid item xs={12} sm={4}>
            <Typography variant="subtitle2" color="text.secondary">
              File Type
            </Typography>
            <Typography variant="body1">
              {file.type}
            </Typography>
          </Grid>
          
          <Grid item xs={12} sm={4}>
            <Typography variant="subtitle2" color="text.secondary">
              File Size
            </Typography>
            <Typography variant="body1">
              {formatFileSize(file.size)}
            </Typography>
          </Grid>
          
          <Grid item xs={12} sm={4}>
            <Typography variant="subtitle2" color="text.secondary">
              Upload Date
            </Typography>
            <Typography variant="body1">
              {file.uploadDate}
            </Typography>
          </Grid>
          
          <Grid item xs={12} sm={4}>
            <Typography variant="subtitle2" color="text.secondary">
              Uploaded By
            </Typography>
            <Typography variant="body1">
              {file.uploadedBy}
            </Typography>
          </Grid>
          
          {file.contentId && (
            <Grid item xs={12} sm={4}>
              <Typography variant="subtitle2" color="text.secondary">
                Associated Content
              </Typography>
              <Link component={RouterLink} to={routes.content.detail(file.contentId)}>
                View Associated Content
              </Link>
            </Grid>
          )}
          
          {/* Additional metadata */}
          {file.metadata.width && (
            <Grid item xs={12} sm={4}>
              <Typography variant="subtitle2" color="text.secondary">
                Dimensions
              </Typography>
              <Typography variant="body1">
                {file.metadata.width} × {file.metadata.height} pixels
              </Typography>
            </Grid>
          )}
          
          {file.metadata.duration && (
            <Grid item xs={12} sm={4}>
              <Typography variant="subtitle2" color="text.secondary">
                Duration
              </Typography>
              <Typography variant="body1">
                {file.metadata.duration} seconds
              </Typography>
            </Grid>
          )}
          
          {file.metadata.pages && (
            <Grid item xs={12} sm={4}>
              <Typography variant="subtitle2" color="text.secondary">
                Pages
              </Typography>
              <Typography variant="body1">
                {file.metadata.pages}
              </Typography>
            </Grid>
          )}
          
          {file.metadata.description && (
            <Grid item xs={12}>
              <Typography variant="subtitle2" color="text.secondary">
                Description
              </Typography>
              <Typography variant="body1">
                {file.metadata.description}
              </Typography>
            </Grid>
          )}
        </Grid>
      </Paper>
    </Container>
  );
};

export default FileDetailPage;
