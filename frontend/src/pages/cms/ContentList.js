import React from 'react';
import { Container, Alert, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

/**
 * ContentList Component
 * 
 * Lists all CMS content in the system.
 * This is a placeholder component for future implementation.
 */
const ContentList = () => {
  return (
    <Container className="py-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1>Content Management</h1>
        <Button as={Link} to="/content/new" variant="primary">
          <i className="bi bi-plus-circle me-2"></i>
          Create New
        </Button>
      </div>
      
      <Alert variant="info">
        <Alert.Heading>Under Development</Alert.Heading>
        <p>The Content Management UI is currently being implemented.</p>
        <p>This component will list all CMS content with filtering and sorting options.</p>
      </Alert>
    </Container>
  );
};

export default ContentList;
