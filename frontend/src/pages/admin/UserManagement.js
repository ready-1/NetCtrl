import React from 'react';
import { Container, Alert, Card, Table, Button, Badge } from 'react-bootstrap';

/**
 * UserManagement Component
 * 
 * Admin-only page for managing users and their roles.
 * This is a placeholder component for future implementation.
 */
const UserManagement = () => {
  // Placeholder mock data
  const mockUsers = [
    { id: 1, username: 'admin', email: 'admin@example.com', roles: ['admin'] },
    { id: 2, username: 'manager', email: 'manager@example.com', roles: ['manager'] },
    { id: 3, username: 'user', email: 'user@example.com', roles: ['user'] },
  ];

  return (
    <Container className="py-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1>User Management</h1>
        <Button variant="primary">
          <i className="bi bi-person-plus me-2"></i>
          Add User
        </Button>
      </div>
      
      <Alert variant="info">
        <Alert.Heading>Under Development</Alert.Heading>
        <p>The User Management UI is currently being implemented.</p>
        <p>This component will provide tools for creating, editing, and managing user accounts and permissions.</p>
      </Alert>
      
      <Card className="mt-4">
        <Card.Header>
          <h5>Users</h5>
        </Card.Header>
        <Card.Body>
          <Table responsive hover>
            <thead>
              <tr>
                <th>ID</th>
                <th>Username</th>
                <th>Email</th>
                <th>Roles</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {mockUsers.map(user => (
                <tr key={user.id}>
                  <td>{user.id}</td>
                  <td>{user.username}</td>
                  <td>{user.email}</td>
                  <td>
                    {user.roles.map(role => (
                      <Badge key={role} bg="primary" className="me-1">{role}</Badge>
                    ))}
                  </td>
                  <td>
                    <Button variant="outline-primary" size="sm" className="me-2">
                      <i className="bi bi-pencil"></i>
                    </Button>
                    <Button variant="outline-danger" size="sm">
                      <i className="bi bi-trash"></i>
                    </Button>
                  </td>
                </tr>
              ))}
            </tbody>
          </Table>
        </Card.Body>
      </Card>
    </Container>
  );
};

export default UserManagement;
