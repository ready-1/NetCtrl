import React from 'react';
import { useParams, Navigate } from 'react-router-dom';
import { Container, CircularProgress, Alert, Box } from '@mui/material';
import ContentForm from '../../components/content/ContentForm';
import { useContent } from '../../hooks/useContentQuery';
import { useDocumentTitle } from '../../hooks/useDocumentTitle';
import routes from '../../config/routes';

const ContentEditPage: React.FC = () => {
  // Get the content ID from URL params (will be undefined for new content)
  const { id } = useParams<{ id?: string }>();
  
  // Determine if we're editing (has ID) or creating (no ID)
  const isEditing = !!id;
  
  // Convert the ID to a number if it exists
  const contentId = id ? parseInt(id, 10) : undefined;
  
  // Set document title based on mode
  useDocumentTitle(isEditing ? 'Edit Content' : 'Create Content');
  
  // If we're editing, fetch the content
  const {
    data: content,
    isLoading,
    isError,
    error,
  } = useContent(contentId || 0, {
    enabled: isEditing, // Only run the query if we're editing
  });
  
  // If ID is provided but invalid, redirect to list page
  if (isEditing && (!contentId || isNaN(contentId))) {
    return <Navigate to={routes.content.list} replace />;
  }
  
  // Show loading state if we're fetching content
  if (isEditing && isLoading) {
    return (
      <Container maxWidth="lg">
        <Box display="flex" justifyContent="center" alignItems="center" minHeight="300px">
          <CircularProgress />
        </Box>
      </Container>
    );
  }
  
  // Show error state if content fetch failed
  if (isEditing && isError) {
    return (
      <Container maxWidth="lg">
        <Alert severity="error">
          {error instanceof Error 
            ? `Error loading content: ${error.message}` 
            : 'Error loading content. Please try again.'}
        </Alert>
      </Container>
    );
  }
  
  return (
    <Container maxWidth="lg">
      <ContentForm 
        initialContent={isEditing ? content : undefined}
        isEditing={isEditing}
      />
    </Container>
  );
};

export default ContentEditPage;
