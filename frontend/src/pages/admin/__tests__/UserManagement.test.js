import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import UserManagement from '../UserManagement';
import apiService from '../../../services/api';
import { AuthProvider } from '../../../store/AuthContext';

// Mock the API service
jest.mock('../../../services/api', () => ({
  users: {
    getAll: jest.fn(),
    getRoles: jest.fn(),
    create: jest.fn(),
    update: jest.fn(),
    delete: jest.fn(),
    updateRole: jest.fn()
  }
}));

// Mock the AuthContext
jest.mock('../../../store/AuthContext', () => {
  const originalModule = jest.requireActual('../../../store/AuthContext');
  
  // Return a modified AuthProvider that includes a mock user
  return {
    ...originalModule,
    useAuth: () => ({
      user: {
        id: 999,
        username: 'admin',
        email: 'admin@example.com',
        roles: ['Admin']
      },
      isAuthenticated: true
    }),
    AuthProvider: ({ children }) => children
  };
});

// Mock data
const mockUsers = [
  {
    id: 1,
    username: 'user1',
    email: 'user1@example.com',
    first_name: 'John',
    last_name: 'Doe',
    roles: [1],
    is_active: true,
    created_at: '2023-01-01T10:00:00Z',
    updated_at: '2023-01-02T10:00:00Z'
  },
  {
    id: 2,
    username: 'user2',
    email: 'user2@example.com',
    first_name: 'Jane',
    last_name: 'Smith',
    roles: [2, 3],
    is_active: false,
    created_at: '2023-02-01T10:00:00Z',
    updated_at: '2023-02-02T10:00:00Z'
  }
];

const mockRoles = [
  { id: 1, name: 'Admin', description: 'Full access to all features' },
  { id: 2, name: 'Manager', description: 'Can manage content and switches' },
  { id: 3, name: 'User', description: 'Standard user access' },
  { id: 4, name: 'ReadOnly', description: 'Can only view content' }
];

describe('UserManagement Component', () => {
  beforeEach(() => {
    // Reset mocks
    jest.clearAllMocks();
    
    // Setup default mocks
    apiService.users.getAll.mockResolvedValue({ 
      data: mockUsers
    });
    apiService.users.getRoles.mockResolvedValue({ 
      data: mockRoles
    });
    apiService.users.create.mockImplementation(userData => 
      Promise.resolve({ 
        data: { 
          id: 3, 
          ...userData,
          created_at: new Date().toISOString(),
          updated_at: new Date().toISOString()
        } 
      })
    );
    apiService.users.update.mockImplementation((id, userData) => 
      Promise.resolve({ 
        data: { 
          ...mockUsers.find(u => u.id === id),
          ...userData,
          updated_at: new Date().toISOString()
        } 
      })
    );
  });

  test('renders loading spinner initially', () => {
    render(
      <BrowserRouter>
        <UserManagement />
      </BrowserRouter>
    );
    
    expect(screen.getByRole('status')).toBeInTheDocument();
  });

  test('fetches users and roles on mount', async () => {
    render(
      <BrowserRouter>
        <UserManagement />
      </BrowserRouter>
    );
    
    // Should call the API methods
    expect(apiService.users.getAll).toHaveBeenCalledTimes(1);
    expect(apiService.users.getRoles).toHaveBeenCalledTimes(1);
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Should render user info
    expect(screen.getByText('user1')).toBeInTheDocument();
    expect(screen.getByText('user2')).toBeInTheDocument();
  });

  test('renders roles badge correctly', async () => {
    render(
      <BrowserRouter>
        <UserManagement />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Should render role badges
    const adminBadge = screen.getByText('Admin');
    expect(adminBadge).toBeInTheDocument();
    
    // User 2 has multiple roles (Manager and User)
    const managerBadge = screen.getByText('Manager');
    const userBadge = screen.getByText('User');
    expect(managerBadge).toBeInTheDocument();
    expect(userBadge).toBeInTheDocument();
  });

  test('search filter works properly', async () => {
    render(
      <BrowserRouter>
        <UserManagement />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Search for "user1"
    const searchInput = screen.getByPlaceholderText('Search users...');
    fireEvent.change(searchInput, { target: { value: 'user1' } });
    
    // Should show user1 but not user2
    expect(screen.getByText('user1')).toBeInTheDocument();
    expect(screen.queryByText('user2')).not.toBeInTheDocument();
    
    // Search for "Jane" (user2's first name)
    fireEvent.change(searchInput, { target: { value: 'Jane' } });
    
    // Should show user2 but not user1
    expect(screen.queryByText('user1')).not.toBeInTheDocument();
    expect(screen.getByText('user2')).toBeInTheDocument();
  });

  test('role filter works properly', async () => {
    render(
      <BrowserRouter>
        <UserManagement />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Filter by Manager role (id: 2)
    const roleFilter = screen.getByDisplayValue('All Roles');
    fireEvent.change(roleFilter, { target: { value: '2' } });
    
    // Should show user2 (has Manager role) but not user1
    expect(screen.queryByText('user1')).not.toBeInTheDocument();
    expect(screen.getByText('user2')).toBeInTheDocument();
  });

  test('add user modal opens and creates user', async () => {
    render(
      <BrowserRouter>
        <UserManagement />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Click the "Add User" button
    fireEvent.click(screen.getByText('Add User'));
    
    // Modal should be visible with form fields
    expect(screen.getByText('Create New User')).toBeInTheDocument();
    
    // Fill out form
    fireEvent.change(screen.getByLabelText('Username'), { 
      target: { value: 'newuser' } 
    });
    fireEvent.change(screen.getByLabelText('Email'), { 
      target: { value: 'newuser@example.com' } 
    });
    fireEvent.change(screen.getByLabelText('Password'), { 
      target: { value: 'password123' } 
    });
    fireEvent.change(screen.getByLabelText('Confirm Password'), { 
      target: { value: 'password123' } 
    });
    
    // Click on the Admin role checkbox
    const adminCheckbox = screen.getByLabelText(/Admin/);
    fireEvent.click(adminCheckbox);
    
    // Click the Create User button
    fireEvent.click(screen.getByText('Create User'));
    
    // Should call the API to create user
    await waitFor(() => {
      expect(apiService.users.create).toHaveBeenCalledWith(
        expect.objectContaining({
          username: 'newuser',
          email: 'newuser@example.com',
          password: 'password123',
          roles: [1] // Admin role
        })
      );
    });
  });

  test('edit user modal opens and updates user', async () => {
    render(
      <BrowserRouter>
        <UserManagement />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Find the edit button for the first user
    const editButtons = screen.getAllByRole('button', { name: '' });
    
    // Click the first edit button
    fireEvent.click(editButtons[0]);
    
    // Modal should show with user data pre-filled
    expect(screen.getByText('Edit User')).toBeInTheDocument();
    
    // Check if username is pre-filled
    const usernameInput = screen.getByLabelText('Username');
    expect(usernameInput.value).toBe('user1');
    
    // Update email
    fireEvent.change(screen.getByLabelText('Email'), { 
      target: { value: 'updated@example.com' } 
    });
    
    // Click the Update User button
    fireEvent.click(screen.getByText('Update User'));
    
    // Should call the API to update user
    await waitFor(() => {
      expect(apiService.users.update).toHaveBeenCalledWith(
        1, // first user id
        expect.objectContaining({
          username: 'user1',
          email: 'updated@example.com'
        })
      );
    });
  });

  test('delete modal shows and confirms deletion', async () => {
    // Mock delete to resolve successfully
    apiService.users.delete.mockResolvedValue({});
    
    render(
      <BrowserRouter>
        <UserManagement />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Find delete buttons (the trashcan icons)
    const deleteButtons = screen.getAllByRole('button', { name: '' });
    
    // Click the delete button for user1
    fireEvent.click(deleteButtons[2]); // The third button should be the delete button for the first user
    
    // Confirm modal is showing
    expect(screen.getByText(/Are you sure you want to delete the user/)).toBeInTheDocument();
    
    // Click the confirm delete button
    const confirmButton = screen.getByText('Delete', { selector: 'button.btn-danger' });
    fireEvent.click(confirmButton);
    
    // Should call delete with the correct ID
    expect(apiService.users.delete).toHaveBeenCalledWith(1);
    
    // Wait for deletion to process
    await waitFor(() => {
      // Should only show one user now
      expect(screen.queryByText('user1')).not.toBeInTheDocument();
      expect(screen.getByText('user2')).toBeInTheDocument();
    });
  });

  test('role edit modal shows and updates roles', async () => {
    // Mock updateRole to resolve successfully
    apiService.users.updateRole.mockResolvedValue({});
    
    render(
      <BrowserRouter>
        <UserManagement />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Find role edit buttons (the shield icons)
    const roleButtons = screen.getAllByRole('button', { name: '' });
    
    // Click the role edit button for user1
    fireEvent.click(roleButtons[1]); // The second button should be the role edit button for the first user
    
    // Confirm modal is showing
    expect(screen.getByText(/Edit User Roles/)).toBeInTheDocument();
    
    // Check if correct user is being edited
    expect(screen.getByText(/Editing roles for user: user1/)).toBeInTheDocument();
    
    // Select the Manager role checkbox
    const managerCheckbox = screen.getByLabelText(/Manager/);
    fireEvent.click(managerCheckbox);
    
    // Click the Update Roles button
    fireEvent.click(screen.getByText('Update Roles'));
    
    // Should call updateRole with the correct ID and roles
    expect(apiService.users.updateRole).toHaveBeenCalledWith(
      1, // user1 id
      [1, 2] // Admin and Manager roles
    );
  });

  test('tabs switch correctly between users and roles views', async () => {
    render(
      <BrowserRouter>
        <UserManagement />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Default tab should be "Users"
    expect(screen.getByText('user1')).toBeInTheDocument();
    
    // Switch to "Roles" tab
    fireEvent.click(screen.getByText('Roles'));
    
    // Should show roles information
    expect(screen.getByText('System Roles')).toBeInTheDocument();
    expect(screen.getByText('Full access to all features')).toBeInTheDocument();
  });
});
