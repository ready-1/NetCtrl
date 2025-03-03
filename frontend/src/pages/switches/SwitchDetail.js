import React from 'react';
import { Container, Alert, Button } from 'react-bootstrap';
import { useParams, Link } from 'react-router-dom';

/**
 * SwitchDetail Component
 * 
 * Displays detailed information about a specific network switch.
 * This is a placeholder component for future implementation.
 */
const SwitchDetail = () => {
  const { id } = useParams();

  return (
    <Container className="py-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1>Switch Details</h1>
        <Button as={Link} to="/switches" variant="outline-secondary">
          <i className="bi bi-arrow-left me-2"></i>
          Back to Switches
        </Button>
      </div>
      
      <Alert variant="info">
        <Alert.Heading>Under Development</Alert.Heading>
        <p>The Switch Detail UI for switch ID: {id} is currently being implemented.</p>
        <p>This component will show detailed configuration and metrics for the selected switch.</p>
      </Alert>
    </Container>
  );
};

export default SwitchDetail;
