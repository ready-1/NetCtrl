import React from 'react';
import { Container } from '@mui/material';
import ContentList from '../../components/content/ContentList';
import { useDocumentTitle } from '../../hooks/useDocumentTitle';

const ContentListPage: React.FC = () => {
  // Set document title
  useDocumentTitle('Content Management');
  
  return (
    <Container maxWidth="lg">
      <ContentList />
    </Container>
  );
};

export default ContentListPage;
