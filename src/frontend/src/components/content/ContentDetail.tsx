import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Box,
  Button,
  Card,
  CardContent,
  Chip,
  Divider,
  Grid,
  IconButton,
  Paper,
  Tooltip,
  Typography,
  useTheme,
  Alert,
  CircularProgress,
} from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import HistoryIcon from '@mui/icons-material/History';
import SecurityIcon from '@mui/icons-material/Security';
import DOMPurify from 'dompurify';
import { Content, ContentStatus, ContentType } from '../../types/content';
import { useContent, useDeleteContent } from '../../hooks/useContentQuery';
import { useAuth } from '../../context/AuthContext';
import routes from '../../config/routes';

// Status chip colors
const statusColorMap: Record<ContentStatus, 'default' | 'primary' | 'success' | 'error'> = {
  [ContentStatus.DRAFT]: 'default',
  [ContentStatus.PUBLISHED]: 'success',
  [ContentStatus.ARCHIVED]: 'error',
};

// Content type display names
const contentTypeDisplayMap: Record<ContentType, string> = {
  [ContentType.TEXT]: 'Plain Text',
  [ContentType.HTML]: 'Rich Text (HTML)',
  [ContentType.MARKDOWN]: 'Markdown',
  [ContentType.FILE]: 'File',
};

// Helper to format dates
const formatDate = (dateString: string) => {
  const date = new Date(dateString);
  return new Intl.DateTimeFormat('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  }).format(date);
};

interface ContentDetailProps {
  contentId: number;
}

const ContentDetail: React.FC<ContentDetailProps> = ({ contentId }) => {
  const navigate = useNavigate();
  const theme = useTheme();
  const { hasRole } = useAuth();
  
  // Fetch content data
  const { 
    data: content, 
    isLoading, 
    isError,
    error,
  } = useContent(contentId);
  
  // Delete mutation
  const { mutate: deleteContent, isLoading: isDeleting } = useDeleteContent();
  
  // Function to render the content body
  const renderContentBody = (content: Content) => {
    if (!content.body) {
      return <Typography color="text.secondary">No content available</Typography>;
    }
    
    switch (content.content_type) {
      case ContentType.HTML:
        return (
          <Box 
            dangerouslySetInnerHTML={{ 
              __html: DOMPurify.sanitize(content.body) 
            }}
            sx={{
              'h1, h2, h3, h4, h5, h6': {
                mt: 2,
                mb: 1,
              },
              p: {
                mb: 1,
              },
              img: {
                maxWidth: '100%',
                height: 'auto',
              },
            }}
          />
        );
      case ContentType.MARKDOWN:
        // In real implementation, you'd use a Markdown renderer here
        return <Typography component="pre">{content.body}</Typography>;
      case ContentType.TEXT:
        return <Typography whiteSpace="pre-wrap">{content.body}</Typography>;
      case ContentType.FILE:
        return <Typography color="text.secondary">File content type</Typography>;
      default:
        return <Typography color="text.secondary">Unknown content type</Typography>;
    }
  };
  
  // Action handlers
  const handleEdit = () => {
    navigate(routes.content.edit(contentId.toString()));
  };
  
  const handleDelete = () => {
    if (window.confirm('Are you sure you want to delete this content? This action cannot be undone.')) {
      deleteContent(contentId, {
        onSuccess: () => {
          navigate(routes.content.list);
        },
      });
    }
  };
  
  const handleBack = () => {
    navigate(routes.content.list);
  };
  
  // Permission check
  const canEdit = hasRole('admin') || hasRole('manager');
  const canDelete = hasRole('admin');
  
  // Loading state
  if (isLoading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="200px">
        <CircularProgress />
      </Box>
    );
  }
  
  // Error state
  if (isError || !content) {
    return (
      <Alert severity="error" sx={{ mb: 2 }}>
        {error instanceof Error 
          ? `Error loading content: ${error.message}` 
          : 'Error loading content. Please try again.'}
      </Alert>
    );
  }
  
  return (
    <Box>
      <Paper sx={{ p: 2, mb: 2 }}>
        {/* Header with actions */}
        <Box display="flex" justifyContent="space-between" alignItems="center" mb={2}>
          <Button
            startIcon={<ArrowBackIcon />}
            onClick={handleBack}
            sx={{ mr: 2 }}
          >
            Back to List
          </Button>
          
          <Box>
            {canEdit && (
              <Tooltip title="Edit">
                <IconButton
                  color="primary"
                  onClick={handleEdit}
                  sx={{ mr: 1 }}
                  disabled={isDeleting}
                >
                  <EditIcon />
                </IconButton>
              </Tooltip>
            )}
            
            {canDelete && (
              <Tooltip title="Delete">
                <IconButton
                  color="error"
                  onClick={handleDelete}
                  disabled={isDeleting}
                >
                  <DeleteIcon />
                </IconButton>
              </Tooltip>
            )}
          </Box>
        </Box>
        
        {/* Title and status */}
        <Box mb={3}>
          <Box display="flex" justifyContent="space-between" alignItems="center">
            <Typography variant="h4" component="h1" gutterBottom>
              {content.title}
            </Typography>
            
            <Chip 
              label={content.status.charAt(0).toUpperCase() + content.status.slice(1)} 
              color={statusColorMap[content.status]}
              sx={{ ml: 2 }}
            />
          </Box>
          
          {content.description && (
            <Typography variant="body1" color="text.secondary" gutterBottom>
              {content.description}
            </Typography>
          )}
        </Box>
        
        <Divider sx={{ mb: 3 }} />
        
        {/* Content metadata */}
        <Grid container spacing={2} sx={{ mb: 3 }}>
          <Grid item xs={12} sm={6} md={3}>
            <Typography variant="body2" color="text.secondary">
              Content Type
            </Typography>
            <Typography variant="body1">
              {contentTypeDisplayMap[content.content_type]}
            </Typography>
          </Grid>
          
          <Grid item xs={12} sm={6} md={3}>
            <Typography variant="body2" color="text.secondary">
              Created by
            </Typography>
            <Typography variant="body1">
              {content.creator?.username || `User ID: ${content.created_by}`}
            </Typography>
          </Grid>
          
          <Grid item xs={12} sm={6} md={3}>
            <Typography variant="body2" color="text.secondary">
              Created at
            </Typography>
            <Typography variant="body1">
              {formatDate(content.created_at)}
            </Typography>
          </Grid>
          
          <Grid item xs={12} sm={6} md={3}>
            <Typography variant="body2" color="text.secondary">
              Last updated
            </Typography>
            <Typography variant="body1">
              {formatDate(content.updated_at)}
            </Typography>
          </Grid>
        </Grid>
        
        <Divider sx={{ mb: 3 }} />
        
        {/* Content body */}
        <Box mb={3}>
          <Typography variant="h6" gutterBottom>
            Content
          </Typography>
          
          <Card variant="outlined">
            <CardContent>
              {renderContentBody(content)}
            </CardContent>
          </Card>
        </Box>
        
        {/* File attachments, if any */}
        {content.files && content.files.length > 0 && (
          <Box mb={3}>
            <Typography variant="h6" gutterBottom>
              Attached Files
            </Typography>
            
            <Card variant="outlined">
              <CardContent>
                {content.files.map((file) => (
                  <Box key={file.id} mb={1}>
                    <Typography variant="body1">
                      {file.filename} ({Math.round(file.file_size / 1024)} KB)
                    </Typography>
                  </Box>
                ))}
              </CardContent>
            </Card>
          </Box>
        )}
      </Paper>
    </Box>
  );
};

export default ContentDetail;
