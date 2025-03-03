import React, { useState, useEffect } from 'react';
import { 
  Container, 
  Row, 
  Col, 
  Card, 
  Table, 
  Badge, 
  Button, 
  Spinner, 
  Form, 
  InputGroup, 
  Dropdown, 
  Alert,
  Modal,
  Tabs,
  Tab
} from 'react-bootstrap';
import { Link } from 'react-router-dom';
import apiService from '../../services/api';

/**
 * ContentList Component
 * 
 * Lists all CMS content in the system with filtering, sorting,
 * and management options.
 */
const ContentList = () => {
  const [content, setContent] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterCategory, setFilterCategory] = useState('all');
  const [filterTag, setFilterTag] = useState('all');
  const [sortField, setSortField] = useState('updated_at');
  const [sortDirection, setSortDirection] = useState('desc');
  const [categories, setCategories] = useState([]);
  const [tags, setTags] = useState([]);
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [contentToDelete, setContentToDelete] = useState(null);
  const [activeTab, setActiveTab] = useState('published');

  // Fetch content, categories, and tags on component mount
  useEffect(() => {
    fetchContent();
    fetchCategories();
    fetchTags();
  }, []);

  // Function to fetch content from API
  const fetchContent = async () => {
    setLoading(true);
    try {
      const response = await apiService.content.getAll();
      setContent(response.data);
      setError(null);
    } catch (err) {
      console.error('Error fetching content:', err);
      setError('Failed to load content. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  // Function to fetch categories
  const fetchCategories = async () => {
    try {
      const response = await apiService.content.getCategories();
      setCategories(response.data);
    } catch (err) {
      console.error('Error fetching categories:', err);
      // Don't show error for categories to avoid UI clutter
    }
  };

  // Function to fetch tags
  const fetchTags = async () => {
    try {
      const response = await apiService.content.getTags();
      setTags(response.data);
    } catch (err) {
      console.error('Error fetching tags:', err);
      // Don't show error for tags to avoid UI clutter
    }
  };

  // Function to handle content deletion
  const handleDelete = async () => {
    if (!contentToDelete) return;
    
    try {
      await apiService.content.delete(contentToDelete.id);
      setContent(content.filter(c => c.id !== contentToDelete.id));
      setShowDeleteModal(false);
      setContentToDelete(null);
    } catch (err) {
      console.error('Error deleting content:', err);
      setError('Failed to delete content. Please try again later.');
    }
  };

  // Function to confirm deletion
  const confirmDelete = (contentItem) => {
    setContentToDelete(contentItem);
    setShowDeleteModal(true);
  };

  // Function to get formatted date
  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
    });
  };

  // Function to handle sort change
  const handleSortChange = (field) => {
    if (sortField === field) {
      // Toggle direction if same field
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc');
    } else {
      // Set new field and default to descending
      setSortField(field);
      setSortDirection('desc');
    }
  };

  // Function to sort content
  const sortContent = (items) => {
    return [...items].sort((a, b) => {
      let aValue = a[sortField];
      let bValue = b[sortField];
      
      // Handle null values
      if (aValue === null) return 1;
      if (bValue === null) return -1;
      
      // Handle dates
      if (sortField === 'created_at' || sortField === 'updated_at') {
        aValue = new Date(aValue).getTime();
        bValue = new Date(bValue).getTime();
      }
      
      // Handle strings
      if (typeof aValue === 'string' && typeof bValue === 'string') {
        aValue = aValue.toLowerCase();
        bValue = bValue.toLowerCase();
      }
      
      // Sort direction
      if (sortDirection === 'asc') {
        return aValue > bValue ? 1 : -1;
      } else {
        return aValue < bValue ? 1 : -1;
      }
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

  // Filter content based on search term, category, tag, and status
  const filteredContent = content.filter(item => {
    // Filter by search term
    const searchMatch = 
      item.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      (item.description && item.description.toLowerCase().includes(searchTerm.toLowerCase()));
    
    // Filter by category
    const categoryMatch = 
      filterCategory === 'all' || 
      item.category === filterCategory;
    
    // Filter by tag
    const tagMatch = 
      filterTag === 'all' || 
      (item.tags && item.tags.includes(filterTag));
    
    // Filter by status (tab)
    const statusMatch = 
      activeTab === 'all' || 
      item.status === activeTab;
    
    return searchMatch && categoryMatch && tagMatch && statusMatch;
  });

  // Sort the filtered content
  const sortedContent = sortContent(filteredContent);

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

  return (
    <Container className="py-4">
      <Row className="mb-4 align-items-center">
        <Col>
          <h1>Content Management</h1>
        </Col>
        <Col xs="auto">
          <Button 
            as={Link} 
            to="/content/new" 
            variant="primary"
          >
            <i className="bi bi-plus-circle me-2"></i>
            Create New
          </Button>
        </Col>
      </Row>

      {error && (
        <Alert variant="danger" dismissible onClose={() => setError(null)}>
          {error}
        </Alert>
      )}

      <Card className="mb-4">
        <Card.Body>
          <Row className="mb-3 g-3">
            <Col md={6}>
              <Form.Group controlId="contentSearch">
                <InputGroup>
                  <InputGroup.Text>
                    <i className="bi bi-search"></i>
                  </InputGroup.Text>
                  <Form.Control
                    type="text"
                    placeholder="Search by title or description..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                  />
                </InputGroup>
              </Form.Group>
            </Col>
            <Col md={3}>
              <Form.Group controlId="categoryFilter">
                <Form.Select
                  value={filterCategory}
                  onChange={(e) => setFilterCategory(e.target.value)}
                >
                  <option value="all">All Categories</option>
                  {categories.map((category) => (
                    <option key={category.id} value={category.id}>
                      {category.name}
                    </option>
                  ))}
                </Form.Select>
              </Form.Group>
            </Col>
            <Col md={3}>
              <Form.Group controlId="tagFilter">
                <Form.Select
                  value={filterTag}
                  onChange={(e) => setFilterTag(e.target.value)}
                >
                  <option value="all">All Tags</option>
                  {tags.map((tag) => (
                    <option key={tag.id} value={tag.id}>
                      {tag.name}
                    </option>
                  ))}
                </Form.Select>
              </Form.Group>
            </Col>
          </Row>

          <Tabs
            activeKey={activeTab}
            onSelect={(k) => setActiveTab(k)}
            className="mb-3"
          >
            <Tab eventKey="all" title="All Content" />
            <Tab eventKey="published" title="Published" />
            <Tab eventKey="draft" title="Drafts" />
            <Tab eventKey="archived" title="Archived" />
          </Tabs>

          {content.length === 0 ? (
            <Alert variant="info">
              No content found. Create new content to get started.
            </Alert>
          ) : sortedContent.length === 0 ? (
            <Alert variant="info">
              No content matches your search criteria.
            </Alert>
          ) : (
            <Table responsive hover>
              <thead>
                <tr>
                  <th>
                    <Button 
                      variant="link" 
                      className="p-0 text-decoration-none text-black"
                      onClick={() => handleSortChange('title')}
                    >
                      Title
                      {sortField === 'title' && (
                        <i className={`bi bi-caret-${sortDirection === 'asc' ? 'up' : 'down'}-fill ms-1`}></i>
                      )}
                    </Button>
                  </th>
                  <th>
                    <Button 
                      variant="link" 
                      className="p-0 text-decoration-none text-black"
                      onClick={() => handleSortChange('category')}
                    >
                      Category
                      {sortField === 'category' && (
                        <i className={`bi bi-caret-${sortDirection === 'asc' ? 'up' : 'down'}-fill ms-1`}></i>
                      )}
                    </Button>
                  </th>
                  <th>Status</th>
                  <th>
                    <Button 
                      variant="link" 
                      className="p-0 text-decoration-none text-black"
                      onClick={() => handleSortChange('author')}
                    >
                      Author
                      {sortField === 'author' && (
                        <i className={`bi bi-caret-${sortDirection === 'asc' ? 'up' : 'down'}-fill ms-1`}></i>
                      )}
                    </Button>
                  </th>
                  <th>
                    <Button 
                      variant="link" 
                      className="p-0 text-decoration-none text-black"
                      onClick={() => handleSortChange('updated_at')}
                    >
                      Last Updated
                      {sortField === 'updated_at' && (
                        <i className={`bi bi-caret-${sortDirection === 'asc' ? 'up' : 'down'}-fill ms-1`}></i>
                      )}
                    </Button>
                  </th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {sortedContent.map((contentItem) => (
                  <tr key={contentItem.id}>
                    <td>
                      <Link to={`/content/${contentItem.id}`}>
                        {contentItem.title}
                      </Link>
                      {contentItem.tags && contentItem.tags.length > 0 && (
                        <div className="mt-1">
                          {contentItem.tags.map((tag) => (
                            <Badge 
                              key={tag} 
                              bg="light" 
                              text="dark" 
                              className="me-1 small"
                            >
                              {tag}
                            </Badge>
                          ))}
                        </div>
                      )}
                    </td>
                    <td>{contentItem.category}</td>
                    <td>{getStatusBadge(contentItem.status)}</td>
                    <td>{contentItem.author}</td>
                    <td>{formatDate(contentItem.updated_at)}</td>
                    <td>
                      <Button
                        as={Link}
                        to={`/content/${contentItem.id}`}
                        variant="outline-primary"
                        size="sm"
                        className="me-2"
                      >
                        <i className="bi bi-eye"></i>
                      </Button>
                      <Button
                        as={Link}
                        to={`/content/${contentItem.id}/edit`}
                        variant="outline-secondary"
                        size="sm"
                        className="me-2"
                      >
                        <i className="bi bi-pencil"></i>
                      </Button>
                      <Dropdown as="span">
                        <Dropdown.Toggle 
                          variant="outline-secondary" 
                          size="sm" 
                          id={`dropdown-${contentItem.id}`}
                        >
                          <i className="bi bi-three-dots"></i>
                        </Dropdown.Toggle>
                        <Dropdown.Menu>
                          {contentItem.status !== 'published' && (
                            <Dropdown.Item>
                              <i className="bi bi-check-circle me-2"></i>
                              Publish
                            </Dropdown.Item>
                          )}
                          {contentItem.status !== 'draft' && (
                            <Dropdown.Item>
                              <i className="bi bi-file-earmark me-2"></i>
                              Save as Draft
                            </Dropdown.Item>
                          )}
                          {contentItem.status !== 'archived' && (
                            <Dropdown.Item>
                              <i className="bi bi-archive me-2"></i>
                              Archive
                            </Dropdown.Item>
                          )}
                          <Dropdown.Divider />
                          <Dropdown.Item 
                            className="text-danger"
                            onClick={() => confirmDelete(contentItem)}
                          >
                            <i className="bi bi-trash me-2"></i>
                            Delete
                          </Dropdown.Item>
                        </Dropdown.Menu>
                      </Dropdown>
                    </td>
                  </tr>
                ))}
              </tbody>
            </Table>
          )}
        </Card.Body>
      </Card>

      {/* Delete Confirmation Modal */}
      <Modal show={showDeleteModal} onHide={() => setShowDeleteModal(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Confirm Deletion</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          Are you sure you want to delete "{contentToDelete?.title}"? 
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
    </Container>
  );
};

export default ContentList;
