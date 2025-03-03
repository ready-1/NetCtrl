import React, { useState, useEffect } from 'react';
import { 
  Container, 
  Row, 
  Col, 
  Card, 
  Button, 
  Badge, 
  Alert, 
  Spinner, 
  Tab, 
  Nav, 
  Table,
  Modal,
  ListGroup,
  Dropdown
} from 'react-bootstrap';
import { useParams, Link, useNavigate } from 'react-router-dom';
import apiService from '../../services/api';

/**
 * ContentDetail Component
 * 
 * Displays detailed information about a specific CMS content item,
 * including content body, metadata, revision history, and related files.
 */
const ContentDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [content, setContent] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('content');
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [showPublishModal, setShowPublishModal] = useState(false);

  // Fetch content data on component mount
  useEffect(() => {
    fetchContent();
  }, [id]);

  // Function to fetch content from API
  const fetchContent = async () => {
    setLoading(true);
    try {
      const response = await apiService.content.getById(id);
      setContent(response.data);
      setError(null);
    } catch (err) {
      console.error('Error fetching content:', err);
      setError('Failed to load content. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  // Function to handle content deletion
  const handleDelete = async () => {
    try {
      await apiService.content.delete(id);
      navigate('/content');
    } catch (err) {
      console.error('Error deleting content:', err);
      setError('Failed to delete content. Please try again later.');
      setShowDeleteModal(false);
    }
  };

  // Function to handle status change
  const handleStatusChange = async (newStatus) => {
    try {
      await apiService.content.update(id, { ...content, status: newStatus });
      setContent({ ...content, status: newStatus });
      setShowPublishModal(false);
    } catch (err) {
      console.error('Error updating content status:', err);
      setError('Failed to update content status. Please try again later.');
    }
  };

  // Function to get formatted date
  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  // Get status badge
  const getStatusBadge = (status) => {
    switch (status) {
      case 'published':
        return <Badge bg="success">Published</Badge>;
      case 'draft':
        return <Badge bg="secondary">Draft</Badge>;
      case 'archived':
        return <Badge bg="warning">Archived</Badge>;
      default:
        return <Badge bg="info">{status}</Badge>;
    }
  };

  // Render loading spinner
  if (loading) {
    return (
      <Container className="py-4 text-center">
        <Spinner animation="border" role="status">
          <span className="visually-hidden">Loading...</span>
        </Spinner>
      </Container>
    );
  }

  // Render error message
  if (error) {
    return (
      <Container className="py-4">
        <Alert variant="danger">
          <Alert.Heading>Error</Alert.Heading>
          <p>{error}</p>
          <div className="d-flex justify-content-end">
            <Button onClick={() => navigate('/content')} variant="outline-danger">
              Back to Content
            </Button>
          </div>
        </Alert>
      </Container>
    );
  }

  return (
    <Container className="py-4">
      {/* Header */}
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1>
          {content?.title || 'Content Details'}
          <span className="ms-3">{content?.status && getStatusBadge(content.status)}</span>
        </h1>
        <div>
          <Dropdown className="d-inline-block me-2">
            <Dropdown.Toggle variant="outline-primary" id="content-actions">
              <i className="bi bi-gear me-2"></i>
              Actions
            </Dropdown.Toggle>
            <Dropdown.Menu>
              {content?.status !== 'published' && (
                <Dropdown.Item onClick={() => setShowPublishModal(true)}>
                  <i className="bi bi-check-circle me-2"></i>
                  Publish
                </Dropdown.Item>
              )}
              {content?.status !== 'draft' && (
                <Dropdown.Item onClick={() => handleStatusChange('draft')}>
                  <i className="bi bi-file-earmark me-2"></i>
                  Save as Draft
                </Dropdown.Item>
              )}
              {content?.status !== 'archived' && (
                <Dropdown.Item onClick={() => handleStatusChange('archived')}>
                  <i className="bi bi-archive me-2"></i>
                  Archive
                </Dropdown.Item>
              )}
              <Dropdown.Divider />
              <Dropdown.Item className="text-danger" onClick={() => setShowDeleteModal(true)}>
                <i className="bi bi-trash me-2"></i>
                Delete
              </Dropdown.Item>
            </Dropdown.Menu>
          </Dropdown>
          <Button as={Link} to={`/content/${id}/edit`} variant="primary" className="me-2">
            <i className="bi bi-pencil me-2"></i>
            Edit
          </Button>
          <Button as={Link} to="/content" variant="outline-secondary">
            <i className="bi bi-arrow-left me-2"></i>
            Back
          </Button>
        </div>
      </div>

      {/* Content Metadata */}
      <Card className="mb-4">
        <Card.Body>
          <Row>
            <Col md={3} className="border-end">
              <div className="text-center mb-3">
                <h5>Category</h5>
                <div className="fw-bold my-2">
                  {content?.category || 'Uncategorized'}
                </div>
              </div>
            </Col>
            <Col md={3} className="border-end">
              <div className="text-center mb-3">
                <h5>Author</h5>
                <div className="fw-bold my-2">
                  {content?.author || 'Unknown'}
                </div>
              </div>
            </Col>
            <Col md={3} className="border-end">
              <div className="text-center mb-3">
                <h5>Created</h5>
                <div className="text-muted small my-2">
                  {formatDate(content?.created_at)}
                </div>
              </div>
            </Col>
            <Col md={3}>
              <div className="text-center mb-3">
                <h5>Last Updated</h5>
                <div className="text-muted small my-2">
                  {formatDate(content?.updated_at)}
                </div>
              </div>
            </Col>
          </Row>
        </Card.Body>
      </Card>

      {/* Tabs */}
      <Tab.Container id="content-tabs" activeKey={activeTab} onSelect={setActiveTab}>
        <Card>
          <Card.Header>
            <Nav variant="tabs">
              <Nav.Item>
                <Nav.Link eventKey="content">Content</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link eventKey="revisions">Revisions</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link eventKey="files">Files</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link eventKey="metadata">Metadata</Nav.Link>
              </Nav.Item>
            </Nav>
          </Card.Header>
          <Card.Body>
            <Tab.Content>
              {/* Content Tab */}
              <Tab.Pane eventKey="content">
                <Card className="mb-3">
                  <Card.Header>
                    <div className="d-flex justify-content-between align-items-center">
                      <h5 className="mb-0">{content?.title}</h5>
                      <div>
                        {content?.tags && content.tags.map((tag) => (
                          <Badge 
                            key={tag} 
                            bg="light" 
                            text="dark" 
                            className="me-1"
                          >
                            {tag}
                          </Badge>
                        ))}
                      </div>
                    </div>
                  </Card.Header>
                  <Card.Body>
                    {content?.description && (
                      <Card.Subtitle className="mb-3 text-muted">
                        {content.description}
                      </Card.Subtitle>
                    )}
                    <div 
                      className="content-body"
                      dangerouslySetInnerHTML={{ __html: content?.body || 'No content available.' }}
                    />
                  </Card.Body>
                  <Card.Footer className="text-muted">
                    <div className="d-flex justify-content-between">
                      <span>Version: {content?.version || '1.0'}</span>
                      <span>Last updated by: {content?.last_modified_by || content?.author || 'Unknown'}</span>
                    </div>
                  </Card.Footer>
                </Card>
              </Tab.Pane>

              {/* Revisions Tab */}
              <Tab.Pane eventKey="revisions">
                {!content?.revisions || content.revisions.length === 0 ? (
                  <Alert variant="info">
                    No revision history available for this content.
                  </Alert>
                ) : (
                  <Table responsive hover>
                    <thead>
                      <tr>
                        <th>Version</th>
                        <th>Date</th>
                        <th>Author</th>
                        <th>Comments</th>
                        <th>Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      {content.revisions.map((revision) => (
                        <tr key={revision.version}>
                          <td>{revision.version}</td>
                          <td>{formatDate(revision.date)}</td>
                          <td>{revision.author}</td>
                          <td>{revision.comments || 'No comments'}</td>
                          <td>
                            <Button 
                              variant="outline-primary" 
                              size="sm"
                              className="me-2"
                            >
                              <i className="bi bi-eye"></i>
                            </Button>
                            <Button 
                              variant="outline-secondary" 
                              size="sm"
                            >
                              <i className="bi bi-arrow-counterclockwise"></i>
                            </Button>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </Table>
                )}
              </Tab.Pane>

              {/* Files Tab */}
              <Tab.Pane eventKey="files">
                {!content?.files || content.files.length === 0 ? (
                  <Alert variant="info">
                    No files attached to this content.
                  </Alert>
                ) : (
                  <ListGroup>
                    {content.files.map((file, index) => (
                      <ListGroup.Item key={index} className="d-flex justify-content-between align-items-center">
                        <div>
                          <i className={`bi bi-file-${getFileIcon(file.type)} me-2`}></i>
                          {file.name}
                          <span className="text-muted ms-2">({file.size})</span>
                        </div>
                        <div>
                          <Button 
                            variant="link" 
                            className="p-0 me-3"
                          >
                            <i className="bi bi-download"></i>
                          </Button>
                          <Button 
                            variant="link" 
                            className="p-0 text-danger"
                          >
                            <i className="bi bi-trash"></i>
                          </Button>
                        </div>
                      </ListGroup.Item>
                    ))}
                  </ListGroup>
                )}
                <div className="mt-3">
                  <Button variant="outline-primary">
                    <i className="bi bi-upload me-2"></i>
                    Upload New File
                  </Button>
                </div>
              </Tab.Pane>

              {/* Metadata Tab */}
              <Tab.Pane eventKey="metadata">
                <Table bordered>
                  <tbody>
                    <tr>
                      <th style={{ width: '30%' }}>ID</th>
                      <td>{content?.id}</td>
                    </tr>
                    <tr>
                      <th>Title</th>
                      <td>{content?.title}</td>
                    </tr>
                    <tr>
                      <th>Slug</th>
                      <td>{content?.slug || `content-${content?.id}`}</td>
                    </tr>
                    <tr>
                      <th>Category</th>
                      <td>{content?.category || 'Uncategorized'}</td>
                    </tr>
                    <tr>
                      <th>Tags</th>
                      <td>
                        {content?.tags && content.tags.length > 0
                          ? content.tags.map(tag => (
                              <Badge 
                                key={tag} 
                                bg="light" 
                                text="dark" 
                                className="me-1"
                              >
                                {tag}
                              </Badge>
                            ))
                          : 'None'}
                      </td>
                    </tr>
                    <tr>
                      <th>Status</th>
                      <td>{getStatusBadge(content?.status || 'unknown')}</td>
                    </tr>
                    <tr>
                      <th>Author</th>
                      <td>{content?.author || 'Unknown'}</td>
                    </tr>
                    <tr>
                      <th>Created Date</th>
                      <td>{formatDate(content?.created_at)}</td>
                    </tr>
                    <tr>
                      <th>Last Updated</th>
                      <td>{formatDate(content?.updated_at)}</td>
                    </tr>
                    <tr>
                      <th>Last Modified By</th>
                      <td>{content?.last_modified_by || content?.author || 'Unknown'}</td>
                    </tr>
                    <tr>
                      <th>Version</th>
                      <td>{content?.version || '1.0'}</td>
                    </tr>
                    <tr>
                      <th>Featured Image</th>
                      <td>{content?.featured_image ? 'Yes' : 'None'}</td>
                    </tr>
                  </tbody>
                </Table>
              </Tab.Pane>
            </Tab.Content>
          </Card.Body>
        </Card>
      </Tab.Container>

      {/* Delete Confirmation Modal */}
      <Modal show={showDeleteModal} onHide={() => setShowDeleteModal(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Confirm Deletion</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          Are you sure you want to delete "{content?.title}"? 
          This action cannot be undone.
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={() => setShowDeleteModal(false)}>
            Cancel
          </Button>
          <Button variant="danger" onClick={handleDelete}>
            Delete
          </Button>
        </Modal.Footer>
      </Modal>

      {/* Publish Confirmation Modal */}
      <Modal show={showPublishModal} onHide={() => setShowPublishModal(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Publish Content</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          Are you ready to publish "{content?.title}"? 
          Once published, it will be visible to all users with appropriate permissions.
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={() => setShowPublishModal(false)}>
            Cancel
          </Button>
          <Button variant="success" onClick={() => handleStatusChange('published')}>
            Publish
          </Button>
        </Modal.Footer>
      </Modal>
    </Container>
  );
};

// Helper function to determine file icon based on type
const getFileIcon = (type) => {
  if (!type) return 'earmark';
  
  const fileType = type.toLowerCase();
  
  if (fileType.includes('image')) return 'image';
  if (fileType.includes('pdf')) return 'pdf';
  if (fileType.includes('word') || fileType.includes('doc')) return 'word';
  if (fileType.includes('excel') || fileType.includes('sheet') || fileType.includes('csv')) return 'excel';
  if (fileType.includes('powerpoint') || fileType.includes('presentation')) return 'ppt';
  if (fileType.includes('zip') || fileType.includes('compressed')) return 'zip';
  if (fileType.includes('text')) return 'text';
  if (fileType.includes('code') || fileType.includes('javascript') || fileType.includes('html') || fileType.includes('css')) return 'code';
  
  return 'earmark';
};

export default ContentDetail;
