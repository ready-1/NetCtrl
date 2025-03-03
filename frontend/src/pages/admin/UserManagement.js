import React, { useState, useEffect } from 'react';
import { 
  Container, 
  Row, 
  Col, 
  Card, 
  Table, 
  Button, 
  Badge, 
  Spinner, 
  Form, 
  InputGroup, 
  Alert,
  Modal,
  Tab,
  Nav,
  Dropdown
} from 'react-bootstrap';
import apiService from '../../services/api';
import { useAuth } from '../../store/AuthContext';

/**
 * UserManagement Component
 * 
 * Admin-only page for managing users and their roles.
 * Provides functionality for creating, editing, and deleting users,
 * as well as managing their role assignments.
 */
const UserManagement = () => {
  const { user: currentUser } = useAuth();
  const [users, setUsers] = useState([]);
  const [roles, setRoles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterRole, setFilterRole] = useState('all');
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [userToDelete, setUserToDelete] = useState(null);
  const [showUserModal, setShowUserModal] = useState(false);
  const [currentUserEdit, setCurrentUserEdit] = useState(null);
  const [showRoleModal, setShowRoleModal] = useState(false);
  const [userForRoleEdit, setUserForRoleEdit] = useState(null);
  const [selectedRoles, setSelectedRoles] = useState([]);
  const [formError, setFormError] = useState('');
  const [activeTab, setActiveTab] = useState('users');

  // Form state for user creation/editing
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
    firstName: '',
    lastName: '',
    roles: [],
    active: true
  });

  // Fetch users and roles on component mount
  useEffect(() => {
    fetchUsers();
    fetchRoles();
  }, []);

  // Function to fetch users from API
  const fetchUsers = async () => {
    setLoading(true);
    try {
      const response = await apiService.users.getAll();
      setUsers(response.data);
      setError(null);
    } catch (err) {
      console.error('Error fetching users:', err);
      setError('Failed to load users. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  // Function to fetch roles from API
  const fetchRoles = async () => {
    try {
      const response = await apiService.users.getRoles();
      setRoles(response.data);
    } catch (err) {
      console.error('Error fetching roles:', err);
      // Don't show error for roles to avoid UI clutter
    }
  };

  // Function to handle form field changes
  const handleFormChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value
    });
  };

  // Function to handle role checkbox changes
  const handleRoleChange = (roleId) => {
    const updatedRoles = [...formData.roles];
    if (updatedRoles.includes(roleId)) {
      // Remove role if already selected
      const index = updatedRoles.indexOf(roleId);
      updatedRoles.splice(index, 1);
    } else {
      // Add role if not selected
      updatedRoles.push(roleId);
    }
    setFormData({ ...formData, roles: updatedRoles });
  };

  // Function to handle role edit checkbox changes
  const handleRoleEditChange = (roleId) => {
    const updatedRoles = [...selectedRoles];
    if (updatedRoles.includes(roleId)) {
      // Remove role if already selected
      const index = updatedRoles.indexOf(roleId);
      updatedRoles.splice(index, 1);
    } else {
      // Add role if not selected
      updatedRoles.push(roleId);
    }
    setSelectedRoles(updatedRoles);
  };

  // Function to open user modal for creating a new user
  const handleAddUser = () => {
    setFormData({
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
      firstName: '',
      lastName: '',
      roles: [],
      active: true
    });
    setCurrentUserEdit(null);
    setFormError('');
    setShowUserModal(true);
  };

  // Function to open user modal for editing an existing user
  const handleEditUser = (user) => {
    setFormData({
      username: user.username,
      email: user.email,
      password: '',
      confirmPassword: '',
      firstName: user.firstName || '',
      lastName: user.lastName || '',
      roles: user.roles.map(role => typeof role === 'object' ? role.id : role),
      active: user.active !== false
    });
    setCurrentUserEdit(user);
    setFormError('');
    setShowUserModal(true);
  };

  // Function to open role edit modal
  const handleEditRoles = (user) => {
    setUserForRoleEdit(user);
    setSelectedRoles(user.roles.map(role => typeof role === 'object' ? role.id : role));
    setShowRoleModal(true);
  };

  // Function to handle saving the user form
  const handleSaveUser = async () => {
    // Validate form
    if (!formData.username) {
      setFormError('Username is required');
      return;
    }
    if (!formData.email) {
      setFormError('Email is required');
      return;
    }
    if (!currentUserEdit && !formData.password) {
      setFormError('Password is required for new users');
      return;
    }
    if (formData.password && formData.password !== formData.confirmPassword) {
      setFormError('Passwords do not match');
      return;
    }

    try {
      let response;
      if (currentUserEdit) {
        // Update existing user
        const userData = { ...formData };
        // Don't send password if it's empty (no change)
        if (!userData.password) {
          delete userData.password;
          delete userData.confirmPassword;
        }
        response = await apiService.users.update(currentUserEdit.id, userData);
      } else {
        // Create new user
        response = await apiService.users.create(formData);
      }
      
      // Update users list
      if (currentUserEdit) {
        setUsers(users.map(u => u.id === currentUserEdit.id ? response.data : u));
      } else {
        setUsers([...users, response.data]);
      }
      
      // Close modal
      setShowUserModal(false);
      setCurrentUserEdit(null);
      setFormError('');
    } catch (err) {
      console.error('Error saving user:', err);
      setFormError(err.message || 'Failed to save user. Please try again.');
    }
  };

  // Function to handle updating user roles
  const handleUpdateRoles = async () => {
    if (!userForRoleEdit) return;
    
    try {
      await apiService.users.updateRole(userForRoleEdit.id, selectedRoles);
      
      // Update user in the state
      setUsers(users.map(u => {
        if (u.id === userForRoleEdit.id) {
          return {
            ...u,
            roles: selectedRoles
          };
        }
        return u;
      }));
      
      setShowRoleModal(false);
      setUserForRoleEdit(null);
    } catch (err) {
      console.error('Error updating roles:', err);
      setError('Failed to update roles. Please try again later.');
    }
  };

  // Function to confirm user deletion
  const confirmDelete = (user) => {
    setUserToDelete(user);
    setShowDeleteModal(true);
  };

  // Function to handle user deletion
  const handleDelete = async () => {
    if (!userToDelete) return;
    
    try {
      await apiService.users.delete(userToDelete.id);
      setUsers(users.filter(u => u.id !== userToDelete.id));
      setShowDeleteModal(false);
      setUserToDelete(null);
    } catch (err) {
      console.error('Error deleting user:', err);
      setError('Failed to delete user. Please try again later.');
    }
  };

  // Filter users based on search term and role filter
  const filteredUsers = users.filter(user => {
    // Filter by search term
    const searchMatch = 
      user.username.toLowerCase().includes(searchTerm.toLowerCase()) ||
      user.email.toLowerCase().includes(searchTerm.toLowerCase()) ||
      (user.firstName && user.firstName.toLowerCase().includes(searchTerm.toLowerCase())) ||
      (user.lastName && user.lastName.toLowerCase().includes(searchTerm.toLowerCase()));
    
    // Filter by role
    const roleMatch = 
      filterRole === 'all' || 
      user.roles.some(role => {
        const roleId = typeof role === 'object' ? role.id : role;
        return roleId === filterRole;
      });
    
    return searchMatch && roleMatch;
  });

  // Get role badge color
  const getRoleBadgeColor = (roleName) => {
    switch (roleName.toLowerCase()) {
      case 'admin':
        return 'danger';
      case 'manager':
        return 'warning';
      case 'user':
        return 'primary';
      case 'readonly':
        return 'info';
      default:
        return 'secondary';
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

  // Helper function to get role name by ID
  const getRoleName = (roleId) => {
    const role = roles.find(r => r.id === roleId);
    return role ? role.name : 'Unknown';
  };

  return (
    <Container className="py-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1>User Management</h1>
        <Button 
          variant="primary" 
          onClick={handleAddUser}
        >
          <i className="bi bi-person-plus me-2"></i>
          Add User
        </Button>
      </div>

      {error && (
        <Alert variant="danger" dismissible onClose={() => setError(null)}>
          {error}
        </Alert>
      )}

      <Tab.Container id="user-management-tabs" activeKey={activeTab} onSelect={setActiveTab}>
        <Card className="mb-4">
          <Card.Header>
            <Nav variant="tabs">
              <Nav.Item>
                <Nav.Link eventKey="users">Users</Nav.Link>
              </Nav.Item>
              <Nav.Item>
                <Nav.Link eventKey="roles">Roles</Nav.Link>
              </Nav.Item>
            </Nav>
          </Card.Header>
          <Card.Body>
            <Tab.Content>
              {/* Users Tab */}
              <Tab.Pane eventKey="users">
                <Row className="mb-3 g-3">
                  <Col md={6}>
                    <Form.Group controlId="userSearch">
                      <InputGroup>
                        <InputGroup.Text>
                          <i className="bi bi-search"></i>
                        </InputGroup.Text>
                        <Form.Control
                          type="text"
                          placeholder="Search users..."
                          value={searchTerm}
                          onChange={(e) => setSearchTerm(e.target.value)}
                        />
                      </InputGroup>
                    </Form.Group>
                  </Col>
                  <Col md={6}>
                    <Form.Group controlId="roleFilter">
                      <Form.Select
                        value={filterRole}
                        onChange={(e) => setFilterRole(e.target.value)}
                      >
                        <option value="all">All Roles</option>
                        {roles.map((role) => (
                          <option key={role.id} value={role.id}>
                            {role.name}
                          </option>
                        ))}
                      </Form.Select>
                    </Form.Group>
                  </Col>
                </Row>

                {users.length === 0 ? (
                  <Alert variant="info">
                    No users found. Use the "Add User" button to create a new user.
                  </Alert>
                ) : filteredUsers.length === 0 ? (
                  <Alert variant="info">
                    No users match your search criteria.
                  </Alert>
                ) : (
                  <Table responsive hover>
                    <thead>
                      <tr>
                        <th>Username</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Roles</th>
                        <th>Status</th>
                        <th>Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      {filteredUsers.map((user) => (
                        <tr key={user.id}>
                          <td>{user.username}</td>
                          <td>
                            {user.firstName || user.lastName
                              ? `${user.firstName || ''} ${user.lastName || ''}`
                              : 'N/A'}
                          </td>
                          <td>{user.email}</td>
                          <td>
                            {user.roles.map((role) => {
                              const roleName = typeof role === 'object' ? role.name : getRoleName(role);
                              return (
                                <Badge 
                                  key={typeof role === 'object' ? role.id : role} 
                                  bg={getRoleBadgeColor(roleName)}
                                  className="me-1"
                                >
                                  {roleName}
                                </Badge>
                              );
                            })}
                          </td>
                          <td>
                            <Badge bg={user.active !== false ? 'success' : 'secondary'}>
                              {user.active !== false ? 'Active' : 'Inactive'}
                            </Badge>
                          </td>
                          <td>
                            <Button
                              variant="outline-primary"
                              size="sm"
                              className="me-2"
                              onClick={() => handleEditUser(user)}
                            >
                              <i className="bi bi-pencil"></i>
                            </Button>
                            <Button
                              variant="outline-secondary"
                              size="sm"
                              className="me-2"
                              onClick={() => handleEditRoles(user)}
                            >
                              <i className="bi bi-shield"></i>
                            </Button>
                            {/* Don't allow deleting yourself */}
                            {currentUser.id !== user.id && (
                              <Button
                                variant="outline-danger"
                                size="sm"
                                onClick={() => confirmDelete(user)}
                              >
                                <i className="bi bi-trash"></i>
                              </Button>
                            )}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </Table>
                )}
              </Tab.Pane>

              {/* Roles Tab */}
              <Tab.Pane eventKey="roles">
                <div className="d-flex justify-content-between align-items-center mb-3">
                  <h4>System Roles</h4>
                </div>

                {roles.length === 0 ? (
                  <Alert variant="info">
                    No roles defined in the system.
                  </Alert>
                ) : (
                  <Table responsive hover>
                    <thead>
                      <tr>
                        <th>Role</th>
                        <th>Description</th>
                        <th>Users</th>
                        <th>Permissions</th>
                      </tr>
                    </thead>
                    <tbody>
                      {roles.map((role) => (
                        <tr key={role.id}>
                          <td>
                            <Badge bg={getRoleBadgeColor(role.name)} className="fs-6 py-2 px-3">
                              {role.name}
                            </Badge>
                          </td>
                          <td>{role.description || 'No description'}</td>
                          <td>
                            {users.filter(u => 
                              u.roles.some(r => 
                                (typeof r === 'object' ? r.id === role.id : r === role.id)
                              )
                            ).length}
                          </td>
                          <td>
                            {role.permissions ? (
                              <ul className="mb-0 ps-3">
                                {role.permissions.map((permission, index) => (
                                  <li key={index}>{permission}</li>
                                ))}
                              </ul>
                            ) : (
                              'No specific permissions'
                            )}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </Table>
                )}

                <Alert variant="info" className="mt-3">
                  <Alert.Heading>Role Information</Alert.Heading>
                  <p>User roles determine permissions and access within the system:</p>
                  <ul>
                    <li><strong>Admin:</strong> Full system access and configuration</li>
                    <li><strong>Manager:</strong> Can manage switches, content, and view user information</li>
                    <li><strong>User:</strong> Basic access to view switches and content</li>
                    <li><strong>ReadOnly:</strong> View-only access with no editing capabilities</li>
                  </ul>
                </Alert>
              </Tab.Pane>
            </Tab.Content>
          </Card.Body>
        </Card>
      </Tab.Container>

      {/* User Create/Edit Modal */}
      <Modal
        show={showUserModal}
        onHide={() => setShowUserModal(false)}
        backdrop="static"
        size="lg"
      >
        <Modal.Header closeButton>
          <Modal.Title>{currentUserEdit ? 'Edit User' : 'Create New User'}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {formError && (
            <Alert variant="danger">{formError}</Alert>
          )}
          <Form>
            <Row className="mb-3">
              <Col md={6}>
                <Form.Group controlId="formUsername">
                  <Form.Label>Username</Form.Label>
                  <Form.Control
                    type="text"
                    name="username"
                    value={formData.username}
                    onChange={handleFormChange}
                    required
                  />
                </Form.Group>
              </Col>
              <Col md={6}>
                <Form.Group controlId="formEmail">
                  <Form.Label>Email</Form.Label>
                  <Form.Control
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleFormChange}
                    required
                  />
                </Form.Group>
              </Col>
            </Row>

            <Row className="mb-3">
              <Col md={6}>
                <Form.Group controlId="formPassword">
                  <Form.Label>{currentUserEdit ? 'New Password (leave blank to keep current)' : 'Password'}</Form.Label>
                  <Form.Control
                    type="password"
                    name="password"
                    value={formData.password}
                    onChange={handleFormChange}
                    required={!currentUserEdit}
                  />
                </Form.Group>
              </Col>
              <Col md={6}>
                <Form.Group controlId="formConfirmPassword">
                  <Form.Label>Confirm Password</Form.Label>
                  <Form.Control
                    type="password"
                    name="confirmPassword"
                    value={formData.confirmPassword}
                    onChange={handleFormChange}
                    required={!currentUserEdit || formData.password !== ''}
                  />
                </Form.Group>
              </Col>
            </Row>

            <Row className="mb-3">
              <Col md={6}>
                <Form.Group controlId="formFirstName">
                  <Form.Label>First Name</Form.Label>
                  <Form.Control
                    type="text"
                    name="firstName"
                    value={formData.firstName}
                    onChange={handleFormChange}
                  />
                </Form.Group>
              </Col>
              <Col md={6}>
                <Form.Group controlId="formLastName">
                  <Form.Label>Last Name</Form.Label>
                  <Form.Control
                    type="text"
                    name="lastName"
                    value={formData.lastName}
                    onChange={handleFormChange}
                  />
                </Form.Group>
              </Col>
            </Row>

            <Form.Group className="mb-3">
              <Form.Label>Roles</Form.Label>
              <div>
                {roles.map((role) => (
                  <Form.Check
                    key={role.id}
                    type="checkbox"
                    id={`role-${role.id}`}
                    label={<span><Badge bg={getRoleBadgeColor(role.name)} className="me-2">{role.name}</Badge>{role.description}</span>}
                    checked={formData.roles.includes(role.id)}
                    onChange={() => handleRoleChange(role.id)}
                    className="mb-2"
                  />
                ))}
              </div>
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Check
                type="checkbox"
                id="formActive"
                label="User is active"
                name="active"
                checked={formData.active}
                onChange={handleFormChange}
              />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={() => setShowUserModal(false)}>
            Cancel
          </Button>
          <Button variant="primary" onClick={handleSaveUser}>
            {currentUserEdit ? 'Update User' : 'Create User'}
          </Button>
        </Modal.Footer>
      </Modal>

      {/* Role Edit Modal */}
      <Modal
        show={showRoleModal}
        onHide={() => setShowRoleModal(false)}
        backdrop="static"
      >
        <Modal.Header closeButton>
          <Modal.Title>Edit User Roles</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>Editing roles for user: <strong>{userForRoleEdit?.username}</strong></p>
          <Form>
            <Form.Group>
              <div>
                {roles.map((role) => (
                  <Form.Check
                    key={role.id}
                    type="checkbox"
                    id={`role-edit-${role.id}`}
                    label={<span><Badge bg={getRoleBadgeColor(role.name)} className="me-2">{role.name}</Badge>{role.description}</span>}
                    checked={selectedRoles.includes(role.id)}
                    onChange={() => handleRoleEditChange(role.id)}
                    className="mb-2"
                  />
                ))}
              </div>
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={() => setShowRoleModal(false)}>
            Cancel
          </Button>
          <Button variant="primary" onClick={handleUpdateRoles}>
            Update Roles
          </Button>
        </Modal.Footer>
      </Modal>

      {/* Delete Confirmation Modal */}
      <Modal show={showDeleteModal} onHide={() => setShowDeleteModal(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Confirm Deletion</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          Are you sure you want to delete the user "{userToDelete?.username}"? 
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

export default UserManagement;
