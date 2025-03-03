import React from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

/**
 * NotFound Component
 * 
 * Displayed when a user navigates to a non-existent route.
 * Provides a user-friendly 404 page with a link back to the dashboard.
 */
const NotFound = () => {
  return (
    <Container className="text-center py-5">
      <Row className="justify-content-center">
        <Col md={8} lg={6}>
          <div className="mb-4">
            <i className="bi bi-exclamation-triangle" style={{ fontSize: '4rem' }}></i>
          </div>
          <h1 className="mb-4">404 - Page Not Found</h1>
          <p className="mb-4">
            The page you are looking for does not exist or has been moved.
          </p>
          <Button as={Link} to="/" variant="primary">
            <i className="bi bi-house me-2"></i>
            Return to Dashboard
          </Button>
        </Col>
      </Row>
    </Container>
  );
};

export default NotFound;
