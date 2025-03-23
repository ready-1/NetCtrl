import React from 'react';
import { useParams, Navigate } from 'react-router-dom';
import { Container } from '@mui/material';
import ContentDetail from '../../components/content/ContentDetail';
import { useDocumentTitle } from '../../hooks/useDocumentTitle';
import routes from '../../config/routes';

const ContentDetailPage: React.FC = () => {
  // Get the content ID from URL params
  const { id } = useParams<{ id: string }>();
  
  // Convert the ID to a number
  const contentId = id ? parseInt(id, 10) : undefined;
  
  // Set document title
  useDocumentTitle('Content Details');
  
  // If ID is invalid, redirect to list page
  if (!contentId || isNaN(contentId)) {
    return <Navigate to={routes.content.list} replace />;
  }
  
  return (
    <Container maxWidth="lg">
      <ContentDetail contentId={contentId} />
    </Container>
  );
};

export default ContentDetailPage;
