import React, { useState } from 'react';
import { Container, Form, Button, Alert, Card } from 'react-bootstrap';
import { useParams, Link, useNavigate } from 'react-router-dom';

/**
 * ContentEdit Component
 * 
 * Form for creating new or editing existing CMS content.
 * This is a placeholder component for future implementation.
 */
const ContentEdit = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const isNewContent = !id;
  
  // Placeholder form state
  const [formData, setFormData] = useState({
    title: '',
    content: '',
    category: '',
  });

  // Placeholder submit handler
  const handleSubmit = (e) => {
    e.preventDefault();
    // For now, just navigate back to content list
    navigate('/content');
  };

  return (
    <Container className="py-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1>{isNewContent ? 'Create New Content' : 'Edit Content'}</h1>
        <Button as={Link} to={isNewContent ? '/content' : `/content/${id}`} variant="outline-secondary">
          <i className="bi bi-x-circle me-2"></i>
          Cancel
        </Button>
      </div>
      
      <Alert variant="info">
        <Alert.Heading>Under Development</Alert.Heading>
        <p>The Content {isNewContent ? 'Creation' : 'Edit'} UI is currently being implemented.</p>
        <p>This component will provide a form for {isNewContent ? 'creating new' : 'editing'} CMS content with rich text editing capabilities.</p>
      </Alert>
      
      <Card className="mt-4">
        <Card.Body>
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3">
              <Form.Label>Title</Form.Label>
              <Form.Control 
                type="text" 
                placeholder="Enter content title" 
                value={formData.title}
                onChange={(e) => setFormData({...formData, title: e.target.value})}
              />
            </Form.Group>
            
            <Form.Group className="mb-3">
              <Form.Label>Category</Form.Label>
              <Form.Select 
                value={formData.category}
                onChange={(e) => setFormData({...formData, category: e.target.value})}
              >
                <option value="">Select category</option>
                <option value="documentation">Documentation</option>
                <option value="guidelines">Guidelines</option>
                <option value="troubleshooting">Troubleshooting</option>
              </Form.Select>
            </Form.Group>
            
            <Form.Group className="mb-3">
              <Form.Label>Content</Form.Label>
              <Form.Control 
                as="textarea" 
                rows={6} 
                placeholder="Enter content body"
                value={formData.content}
                onChange={(e) => setFormData({...formData, content: e.target.value})}
              />
              <Form.Text className="text-muted">
                Markdown formatting is supported.
              </Form.Text>
            </Form.Group>
            
            <div className="d-flex justify-content-end">
              <Button variant="primary" type="submit">
                {isNewContent ? 'Create Content' : 'Save Changes'}
              </Button>
            </div>
          </Form>
        </Card.Body>
      </Card>
    </Container>
  );
};

export default ContentEdit;
