import React, { useState, useEffect, useRef } from 'react';
import { 
  Container, 
  Form, 
  Button, 
  Alert, 
  Card, 
  Row, 
  Col, 
  Tab, 
  Nav, 
  Badge, 
  Spinner,
  ListGroup,
  Modal,
  InputGroup,
  Dropdown
} from 'react-bootstrap';
import { useParams, Link, useNavigate } from 'react-router-dom';
import apiService from '../../services/api';

/**
 * ContentEdit Component
 * 
 * Form for creating new or editing existing CMS content.
 * Provides rich text editing, file attachments, and content metadata management.
 */
const ContentEdit = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const isNewContent = !id;
  const editorRef = useRef(null);
  
  // State for form data
  const [formData, setFormData] = useState({
    title: '',
    slug: '',
    description: '',
    body: '',
    category: '',
    tags: [],
    status: 'draft',
    featured_image: null
  });
  
  // State for UI
  const [loading, setLoading] = useState(!isNewContent);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);
  const [validationErrors, setValidationErrors] = useState({});
  const [activeTab, setActiveTab] = useState('content');
  const [categories, setCategories] = useState([]);
  const [availableTags, setAvailableTags] = useState([]);
  const [newTag, setNewTag] = useState('');
  const [files, setFiles] = useState([]);
  const [showFileModal, setShowFileModal] = useState(false);
  const [fileUploading, setFileUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [showUnsavedModal, setShowUnsavedModal] = useState(false);
  const [isDirty, setIsDirty] = useState(false);
  const [redirectPath, setRedirectPath] = useState('/content');

  // Fetch data on component mount
  useEffect(() => {
    fetchCategories();
    fetchTags();
    
    if (!isNewContent) {
      fetchContent();
    }
  }, [id]);

  // Function to fetch content for editing
  const fetchContent = async () => {
    try {
      const response = await apiService.content.getById(id);
      const contentData = response.data;
      
      setFormData({
        title: contentData.title || '',
        slug: contentData.slug || '',
        description: contentData.description || '',
        body: contentData.body || '',
        category: contentData.category || '',
        tags: contentData.tags || [],
        status: contentData.status || 'draft',
        featured_image: contentData.featured_image || null
      });
      
      // Set files if available
      if (contentData.files && contentData.files.length > 0) {
        setFiles(contentData.files);
      }
      
      setLoading(false);
    } catch (err) {
      console.error('Error fetching content:', err);
      setError('Failed to load content. Please try again later.');
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
      setAvailableTags(response.data);
    } catch (err) {
      console.error('Error fetching tags:', err);
      // Don't show error for tags to avoid UI clutter
    }
  };

  // Function to handle form field changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    setIsDirty(true);
    
    // Clear validation error when field is changed
    if (validationErrors[name]) {
      setValidationErrors(prev => ({ ...prev, [name]: null }));
    }
    
    // Generate slug from title if slug is empty
    if (name === 'title' && (!formData.slug || formData.slug === '')) {
      const slug = value
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/(^-|-$)/g, '');
      setFormData(prev => ({ ...prev, slug }));
    }
  };

  // Function to handle rich text editor content changes
  const handleEditorChange = (content) => {
    setFormData(prev => ({ ...prev, body: content }));
    setIsDirty(true);
  };

  // Function to handle tag addition
  const handleAddTag = () => {
    if (newTag && !formData.tags.includes(newTag)) {
      setFormData(prev => ({
        ...prev,
        tags: [...prev.tags, newTag]
      }));
      setNewTag('');
      setIsDirty(true);
    }
  };

  // Function to handle tag removal
  const handleRemoveTag = (tag) => {
    setFormData(prev => ({
      ...prev,
      tags: prev.tags.filter(t => t !== tag)
    }));
    setIsDirty(true);
  };

  // Function to add existing tag from dropdown
  const handleSelectTag = (tag) => {
    if (!formData.tags.includes(tag)) {
      setFormData(prev => ({
        ...prev,
        tags: [...prev.tags, tag]
      }));
      setIsDirty(true);
    }
  };

  // Function to handle file upload
  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    
    // Create form data for file upload
    const formData = new FormData();
    formData.append('file', file);
    
    setFileUploading(true);
    setUploadProgress(0);
    
    try {
      // Setup progress tracking
      const uploadProgressInterval = setInterval(() => {
        setUploadProgress(prev => {
          const newProgress = prev + Math.random() * 8;
          return newProgress > 90 ? 90 : newProgress;
        });
      }, 300);
      
      // Upload file through API service
      const response = await apiService.content.uploadAttachment(
        id || 'temp', // For new content, use temp ID until content is created
        formData
      );
      
      clearInterval(uploadProgressInterval);
      setUploadProgress(100);
      
      // Process the response and add file to list
      const fileData = response.data;
      const newFile = {
        id: fileData.id || Date.now().toString(),
        name: fileData.name || file.name,
        size: fileData.size || `${(file.size / 1024).toFixed(2)} KB`,
        type: fileData.mime_type || file.type,
        uploaded_at: fileData.uploaded_at || new Date().toISOString(),
        url: fileData.url || ''
      };
      
      setFiles(prev => [...prev, newFile]);
      setFileUploading(false);
      setShowFileModal(false);
      setIsDirty(true);
      
      // Reset file input
      e.target.value = null;
    } catch (err) {
      console.error('Error uploading file:', err);
      setError('Failed to upload file. Please try again.');
      setFileUploading(false);
      
      // Reset file input
      e.target.value = null;
    }
  };

  // Function to handle file deletion
  const handleDeleteFile = (fileId) => {
    setFiles(prev => prev.filter(file => file.id !== fileId));
    setIsDirty(true);
  };

  // Function to validate form
  const validateForm = () => {
    const errors = {};
    
    if (!formData.title.trim()) {
      errors.title = 'Title is required';
    }
    
    if (!formData.category) {
      errors.category = 'Category is required';
    }
    
    if (!formData.body.trim()) {
      errors.body = 'Content body is required';
    }
    
    setValidationErrors(errors);
    return Object.keys(errors).length === 0;
  };

  // Function to handle form submission
  const handleSubmit = async (e, saveAsStatus = null) => {
    e.preventDefault();
    
    if (!validateForm()) {
      setActiveTab('content');
      return;
    }
    
    setSaving(true);
    
    // Set status if provided
    const dataToSubmit = {
      ...formData,
      status: saveAsStatus || formData.status
    };
    
    try {
      let response;
      
      if (isNewContent) {
        // Create new content
        response = await apiService.content.create(dataToSubmit);
      } else {
        // Update existing content
        response = await apiService.content.update(id, dataToSubmit);
      }
      
      setSaving(false);
      setIsDirty(false);
      
      // Navigate to content detail or list
      if (saveAsStatus === 'draft') {
        navigate('/content'); // Go to list for drafts
      } else {
        navigate(`/content/${response.data.id}`); // Go to detail view
      }
    } catch (err) {
      console.error('Error saving content:', err);
      setError('Failed to save content. Please try again later.');
      setSaving(false);
    }
  };

  // Function to handle cancel
  const handleCancel = (targetPath = '/content') => {
    if (isDirty) {
      setRedirectPath(targetPath);
      setShowUnsavedModal(true);
    } else {
      navigate(targetPath);
    }
  };

  // Function to handle confirmation of unsaved changes
  const confirmNavigateAway = () => {
    setShowUnsavedModal(false);
    navigate(redirectPath);
  };

  // Function to get file icon based on type
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
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1>{isNewContent ? 'Create New Content' : 'Edit Content'}</h1>
        <div>
          {!isNewContent && (
            <Button 
              as={Link} 
              to={`/content/${id}`} 
              variant="outline-primary" 
              className="me-2"
              onClick={(e) => {
                if (isDirty) {
                  e.preventDefault();
                  handleCancel(`/content/${id}`);
                }
              }}
            >
              <i className="bi bi-eye me-2"></i>
              View
            </Button>
          )}
          <Button 
            variant="outline-secondary" 
            onClick={() => handleCancel()}
          >
            <i className="bi bi-x-circle me-2"></i>
            Cancel
          </Button>
        </div>
      </div>

      {error && (
        <Alert variant="danger" dismissible onClose={() => setError(null)}>
          {error}
        </Alert>
      )}

      <Form onSubmit={handleSubmit}>
        <Tab.Container id="content-edit-tabs" activeKey={activeTab} onSelect={setActiveTab}>
          <Card className="mb-4">
            <Card.Header>
              <Nav variant="tabs">
                <Nav.Item>
                  <Nav.Link eventKey="content">Content</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                  <Nav.Link eventKey="metadata">Metadata</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                  <Nav.Link eventKey="files">Files</Nav.Link>
                </Nav.Item>
              </Nav>
            </Card.Header>
            <Card.Body>
              <Tab.Content>
                {/* Content Tab */}
                <Tab.Pane eventKey="content">
                  <Form.Group className="mb-3">
                    <Form.Label>Title <span className="text-danger">*</span></Form.Label>
                    <Form.Control 
                      type="text" 
                      name="title"
                      placeholder="Enter content title" 
                      value={formData.title}
                      onChange={handleChange}
                      isInvalid={!!validationErrors.title}
                    />
                    <Form.Control.Feedback type="invalid">
                      {validationErrors.title}
                    </Form.Control.Feedback>
                  </Form.Group>
                  
                  <Form.Group className="mb-3">
                    <Form.Label>Description</Form.Label>
                    <Form.Control 
                      as="textarea"
                      rows={2}
                      name="description"
                      placeholder="Brief description or summary" 
                      value={formData.description}
                      onChange={handleChange}
                    />
                  </Form.Group>
                  
                  <Form.Group className="mb-4">
                    <Form.Label>Content <span className="text-danger">*</span></Form.Label>
                    <Form.Control 
                      as="textarea" 
                      rows={12} 
                      name="body"
                      placeholder="Enter content body"
                      value={formData.body}
                      onChange={(e) => handleChange(e)}
                      isInvalid={!!validationErrors.body}
                      className="font-monospace"
                    />
                    <Form.Control.Feedback type="invalid">
                      {validationErrors.body}
                    </Form.Control.Feedback>
                    <Form.Text className="text-muted">
                      <i className="bi bi-markdown me-1"></i>
                      Markdown formatting is supported
                    </Form.Text>
                  </Form.Group>
                </Tab.Pane>

                {/* Metadata Tab */}
                <Tab.Pane eventKey="metadata">
                  <Row>
                    <Col md={6}>
                      <Form.Group className="mb-3">
                        <Form.Label>Slug</Form.Label>
                        <Form.Control 
                          type="text" 
                          name="slug"
                          placeholder="URL-friendly identifier" 
                          value={formData.slug}
                          onChange={handleChange}
                        />
                        <Form.Text className="text-muted">
                          Leave empty to auto-generate from title
                        </Form.Text>
                      </Form.Group>
                      
                      <Form.Group className="mb-3">
                        <Form.Label>Category <span className="text-danger">*</span></Form.Label>
                        <Form.Select 
                          name="category"
                          value={formData.category}
                          onChange={handleChange}
                          isInvalid={!!validationErrors.category}
                        >
                          <option value="">Select category</option>
                          {categories.map((category) => (
                            <option key={category.id} value={category.id}>
                              {category.name}
                            </option>
                          ))}
                        </Form.Select>
                        <Form.Control.Feedback type="invalid">
                          {validationErrors.category}
                        </Form.Control.Feedback>
                      </Form.Group>
                      
                      <Form.Group className="mb-3">
                        <Form.Label>Status</Form.Label>
                        <Form.Select 
                          name="status"
                          value={formData.status}
                          onChange={handleChange}
                        >
                          <option value="draft">Draft</option>
                          <option value="published">Published</option>
                          <option value="archived">Archived</option>
                        </Form.Select>
                      </Form.Group>
                    </Col>
                    
                    <Col md={6}>
                      <Form.Group className="mb-3">
                        <Form.Label>Tags</Form.Label>
                        <InputGroup className="mb-2">
                          <Form.Control 
                            type="text" 
                            placeholder="Add a tag" 
                            value={newTag}
                            onChange={(e) => setNewTag(e.target.value)}
                            onKeyPress={(e) => {
                              if (e.key === 'Enter') {
                                e.preventDefault();
                                handleAddTag();
                              }
                            }}
                          />
                          <Button 
                            variant="outline-secondary" 
                            onClick={handleAddTag}
                          >
                            Add
                          </Button>
                          <Dropdown>
                            <Dropdown.Toggle variant="outline-secondary" id="tag-dropdown">
                              <i className="bi bi-tag"></i>
                            </Dropdown.Toggle>
                            <Dropdown.Menu>
                              {availableTags
                                .filter(tag => !formData.tags.includes(tag.name))
                                .map(tag => (
                                  <Dropdown.Item 
                                    key={tag.id} 
                                    onClick={() => handleSelectTag(tag.name)}
                                  >
                                    {tag.name}
                                  </Dropdown.Item>
                                ))
                              }
                              {availableTags
                                .filter(tag => !formData.tags.includes(tag.name))
                                .length === 0 && (
                                  <Dropdown.Item disabled>No more tags available</Dropdown.Item>
                                )
                              }
                            </Dropdown.Menu>
                          </Dropdown>
                        </InputGroup>
                        
                        <div className="mt-2">
                          {formData.tags.map((tag) => (
                            <Badge 
                              key={tag} 
                              bg="light" 
                              text="dark" 
                              className="me-2 mb-2 p-2"
                            >
                              {tag}
                              <Button 
                                variant="link" 
                                size="sm" 
                                className="p-0 ms-2 text-danger"
                                onClick={() => handleRemoveTag(tag)}
                              >
                                <i className="bi bi-x"></i>
                              </Button>
                            </Badge>
                          ))}
                          {formData.tags.length === 0 && (
                            <span className="text-muted">No tags added</span>
                          )}
                        </div>
                      </Form.Group>
                      
                      <Form.Group className="mb-3">
                        <Form.Label>Featured Image</Form.Label>
                        <div className="d-flex align-items-center">
                          {formData.featured_image ? (
                            <div className="position-relative me-3">
                              <img 
                                src={formData.featured_image} 
                                alt="Featured" 
                                style={{ height: '100px', width: 'auto', objectFit: 'cover' }}
                                className="border"
                              />
                              <Button 
                                variant="danger" 
                                size="sm" 
                                className="position-absolute top-0 end-0"
                                onClick={() => setFormData({...formData, featured_image: null})}
                              >
                                <i className="bi bi-x"></i>
                              </Button>
                            </div>
                          ) : (
                            <div className="border rounded p-4 text-center me-3" style={{ width: '150px' }}>
                              <i className="bi bi-card-image fs-3 text-muted"></i>
                              <p className="mb-0 small text-muted">No image selected</p>
                            </div>
                          )}
                          <Button variant="outline-secondary">
                            Choose Image
                          </Button>
                        </div>
                      </Form.Group>
                    </Col>
                  </Row>
                </Tab.Pane>

                {/* Files Tab */}
                <Tab.Pane eventKey="files">
                  <div className="d-flex justify-content-between align-items-center mb-3">
                    <h5 className="mb-0">Attached Files</h5>
                    <Button 
                      variant="outline-primary"
                      onClick={() => setShowFileModal(true)}
                    >
                      <i className="bi bi-upload me-2"></i>
                      Upload File
                    </Button>
                  </div>
                  
                  {files.length === 0 ? (
                    <Alert variant="info">
                      No files attached to this content. Upload files to include them in your content.
                    </Alert>
                  ) : (
                    <ListGroup>
                      {files.map((file) => (
                        <ListGroup.Item key={file.id} className="d-flex justify-content-between align-items-center">
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
                              onClick={() => handleDeleteFile(file.id)}
                            >
                              <i className="bi bi-trash"></i>
                            </Button>
                          </div>
                        </ListGroup.Item>
                      ))}
                    </ListGroup>
                  )}
                  
                  <Alert variant="info" className="mt-3">
                    <i className="bi bi-info-circle me-2"></i>
                    Attached files can be linked in the content using markdown syntax: <code>[file name](file:filename.ext)</code>
                  </Alert>
                </Tab.Pane>
              </Tab.Content>
            </Card.Body>
            <Card.Footer>
              <div className="d-flex justify-content-between align-items-center">
                <div>
                  {activeTab === 'content' && (
                    <Button 
                      variant="outline-secondary" 
                      onClick={() => setActiveTab('metadata')}
                      className="me-2"
                    >
                      Next: Metadata 
                      <i className="bi bi-arrow-right ms-2"></i>
                    </Button>
                  )}
                  {activeTab === 'metadata' && (
                    <>
                      <Button 
                        variant="outline-secondary" 
                        onClick={() => setActiveTab('content')}
                        className="me-2"
                      >
                        <i className="bi bi-arrow-left me-2"></i>
                        Back to Content
                      </Button>
                      <Button 
                        variant="outline-secondary" 
                        onClick={() => setActiveTab('files')}
                        className="me-2"
                      >
                        Next: Files
                        <i className="bi bi-arrow-right ms-2"></i>
                      </Button>
                    </>
                  )}
                  {activeTab === 'files' && (
                    <Button 
                      variant="outline-secondary" 
                      onClick={() => setActiveTab('metadata')}
                      className="me-2"
                    >
                      <i className="bi bi-arrow-left me-2"></i>
                      Back to Metadata
                    </Button>
                  )}
                </div>
                <div>
                  <Dropdown as="span" className="me-2">
                    <Dropdown.Toggle variant="success" id="save-options">
                      Save As
                    </Dropdown.Toggle>
                    <Dropdown.Menu>
                      <Dropdown.Item onClick={(e) => handleSubmit(e, 'published')}>
                        <i className="bi bi-check-circle me-2"></i>
                        Publish
                      </Dropdown.Item>
                      <Dropdown.Item onClick={(e) => handleSubmit(e, 'draft')}>
                        <i className="bi bi-file-earmark me-2"></i>
                        Draft
                      </Dropdown.Item>
                      <Dropdown.Item onClick={(e) => handleSubmit(e, 'archived')}>
                        <i className="bi bi-archive me-2"></i>
                        Archive
                      </Dropdown.Item>
                    </Dropdown.Menu>
                  </Dropdown>
                  
                  <Button 
                    variant="primary" 
                    type="submit"
                    disabled={saving}
                  >
                    {saving ? (
                      <>
                        <Spinner
                          as="span"
                          animation="border"
                          size="sm"
                          role="status"
                          aria-hidden="true"
                          className="me-2"
                        />
                        Saving...
                      </>
                    ) : (
                      <>
                        <i className="bi bi-save me-2"></i>
                        {isNewContent ? 'Create Content' : 'Save Changes'}
                      </>
                    )}
                  </Button>
                </div>
              </div>
            </Card.Footer>
          </Card>
        </Tab.Container>
      </Form>

      {/* File Upload Modal */}
      <Modal
        show={showFileModal}
        onHide={() => setShowFileModal(false)}
        backdrop="static"
        centered
      >
        <Modal.Header closeButton>
          <Modal.Title>Upload File</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {fileUploading ? (
            <div className="text-center">
              <Spinner animation="border" role="status" className="mb-3">
                <span className="visually-hidden">Uploading...</span>
              </Spinner>
              <h5>Uploading file...</h5>
              <div className="progress mt-3">
                <div 
                  className="progress-bar progress-bar-striped progress-bar-animated" 
                  role="progressbar" 
                  style={{ width: `${uploadProgress}%` }} 
                  aria-valuenow={uploadProgress} 
                  aria-valuemin="0" 
                  aria-valuemax="100"
                >
                  {Math.round(uploadProgress)}%
                </div>
              </div>
            </div>
          ) : (
            <div>
              <p>Select a file to upload and attach to this content.</p>
              <Form.Group controlId="fileUpload">
                <Form.Label>Choose File</Form.Label>
                <Form.Control 
                  type="file" 
                  onChange={handleFileUpload}
                />
                <Form.Text className="text-muted">
                  Maximum file size: 10MB
                </Form.Text>
              </Form.Group>
            </div>
          )}
        </Modal.Body>
        {!fileUploading && (
          <Modal.Footer>
            <Button variant="secondary" onClick={() => setShowFileModal(false)}>
              Cancel
            </Button>
          </Modal.Footer>
        )}
      </Modal>

      {/* Unsaved Changes Modal */}
      <Modal
        show={showUnsavedModal}
        onHide={() => setShowUnsavedModal(false)}
        backdrop="static"
        centered
      >
        <Modal.Header closeButton>
          <Modal.Title>Unsaved Changes</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          You have unsaved changes. Are you sure you want to leave this page? Your changes will be lost.
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={() => setShowUnsavedModal(false)}>
            Stay on Page
          </Button>
          <Button variant="danger" onClick={confirmNavigateAway}>
            Discard Changes
          </Button>
        </Modal.Footer>
      </Modal>
    </Container>
  );
};

export default ContentEdit;
