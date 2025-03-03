import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ContentDetail from '../ContentDetail';
import apiService from '../../../services/api';

// Mock the API service
jest.mock('../../../services/api', () => ({
  content: {
    getById: jest.fn(),
    delete: jest.fn(),
    update: jest.fn()
  }
}));

// Mock react-router-dom's useParams hook
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useParams: () => ({ id: '123' }),
  useNavigate: () => jest.fn()
}));

// Mock data
const mockContent = {
  id: '123',
  title: 'Test Article',
  slug: 'test-article',
  description: 'This is a test article description',
  body: '<p>This is the body of the test article.</p><p>It has multiple paragraphs.</p>',
  status: 'published',
  author: 'John Doe',
  category: 'Documentation',
  tags: ['Network', 'Guide'],
  version: '1.2',
  created_at: '2023-01-01T10:00:00Z',
  updated_at: '2023-02-01T10:00:00Z',
  last_modified_by: 'Jane Smith',
  revisions: [
    {
      version: '1.2',
      date: '2023-02-01T10:00:00Z',
      author: 'Jane Smith',
      comments: 'Updated content formatting'
    },
    {
      version: '1.1',
      date: '2023-01-15T10:00:00Z',
      author: 'John Doe',
      comments: 'Fixed typos'
    },
    {
      version: '1.0',
      date: '2023-01-01T10:00:00Z',
      author: 'John Doe',
      comments: 'Initial version'
    }
  ],
  files: [
    {
      name: 'document.pdf',
      type: 'application/pdf',
      size: '2.5 MB'
    },
    {
      name: 'screenshot.png',
      type: 'image/png',
      size: '350 KB'
    }
  ]
};

describe('ContentDetail Component', () => {
  beforeEach(() => {
    // Reset mocks
    jest.clearAllMocks();
    
    // Setup default mocks
    apiService.content.getById.mockResolvedValue({ 
      data: mockContent
    });
    apiService.content.update.mockResolvedValue({
      data: {
        ...mockContent,
        status: 'draft' // for status change test
      }
    });
    apiService.content.delete.mockResolvedValue({});
  });

  test('renders loading spinner initially', () => {
    render(
      <BrowserRouter>
        <ContentDetail />
      </BrowserRouter>
    );
    
    expect(screen.getByRole('status')).toBeInTheDocument();
  });

  test('fetches content on mount and displays it', async () => {
    render(
      <BrowserRouter>
        <ContentDetail />
      </BrowserRouter>
    );
    
    // Should call the API method
    expect(apiService.content.getById).toHaveBeenCalledWith('123');
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Should render content info
    expect(screen.getByText('Test Article')).toBeInTheDocument();
    expect(screen.getByText('This is a test article description')).toBeInTheDocument();
    expect(screen.getByText('Published')).toBeInTheDocument();
    expect(screen.getByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('Documentation')).toBeInTheDocument();
    
    // Check if the body content is rendered
    const contentBody = screen.getByText('This is the body of the test article.');
    expect(contentBody).toBeInTheDocument();
    
    // Check for tags
    const networkTag = screen.getByText('Network');
    const guideTag = screen.getByText('Guide');
    expect(networkTag).toBeInTheDocument();
    expect(guideTag).toBeInTheDocument();
  });

  test('shows revisions when clicking the revisions tab', async () => {
    render(
      <BrowserRouter>
        <ContentDetail />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Click on the Revisions tab
    fireEvent.click(screen.getByText('Revisions'));
    
    // Check if revision data is shown
    expect(screen.getByText('Updated content formatting')).toBeInTheDocument();
    expect(screen.getByText('Fixed typos')).toBeInTheDocument();
    expect(screen.getByText('Initial version')).toBeInTheDocument();
  });

  test('shows files when clicking the files tab', async () => {
    render(
      <BrowserRouter>
        <ContentDetail />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Click on the Files tab
    fireEvent.click(screen.getByText('Files'));
    
    // Check if files are listed
    expect(screen.getByText('document.pdf')).toBeInTheDocument();
    expect(screen.getByText('screenshot.png')).toBeInTheDocument();
    expect(screen.getByText('(2.5 MB)')).toBeInTheDocument();
    expect(screen.getByText('(350 KB)')).toBeInTheDocument();
  });

  test('shows metadata when clicking the metadata tab', async () => {
    render(
      <BrowserRouter>
        <ContentDetail />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Click on the Metadata tab
    fireEvent.click(screen.getByText('Metadata'));
    
    // Check if metadata is displayed
    expect(screen.getByText('test-article')).toBeInTheDocument(); // slug
    expect(screen.getByText('1.2')).toBeInTheDocument(); // version
    expect(screen.getByText('Jane Smith')).toBeInTheDocument(); // last_modified_by
  });

  test('opens and confirms delete modal', async () => {
    render(
      <BrowserRouter>
        <ContentDetail />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Open the actions dropdown
    fireEvent.click(screen.getByText('Actions'));
    
    // Click delete option
    fireEvent.click(screen.getByText('Delete'));
    
    // Check if confirmation modal appears
    expect(screen.getByText(/Are you sure you want to delete "Test Article"/)).toBeInTheDocument();
    
    // Click the confirm delete button
    fireEvent.click(screen.getByText('Delete', { selector: 'button.btn-danger' }));
    
    // Should call delete with the correct ID
    expect(apiService.content.delete).toHaveBeenCalledWith('123');
  });

  test('changes content status when action is selected', async () => {
    render(
      <BrowserRouter>
        <ContentDetail />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Open the actions dropdown
    fireEvent.click(screen.getByText('Actions'));
    
    // Click "Save as Draft" option
    fireEvent.click(screen.getByText('Save as Draft'));
    
    // Should call update with the correct data
    expect(apiService.content.update).toHaveBeenCalledWith('123', expect.objectContaining({
      ...mockContent,
      status: 'draft'
    }));
  });

  test('opens and confirms publish modal', async () => {
    // Change mock content to draft for this test
    apiService.content.getById.mockResolvedValue({
      data: {
        ...mockContent,
        status: 'draft'
      }
    });
    
    render(
      <BrowserRouter>
        <ContentDetail />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Open the actions dropdown
    fireEvent.click(screen.getByText('Actions'));
    
    // Click publish option
    fireEvent.click(screen.getByText('Publish'));
    
    // Check if confirmation modal appears
    expect(screen.getByText(/Are you ready to publish "Test Article"/)).toBeInTheDocument();
    
    // Click the confirm publish button
    fireEvent.click(screen.getByText('Publish'));
    
    // Should call update with the correct data
    expect(apiService.content.update).toHaveBeenCalledWith('123', expect.objectContaining({
      status: 'published'
    }));
  });

  test('shows error message when content loading fails', async () => {
    // Mock API to throw an error
    apiService.content.getById.mockRejectedValue(new Error('Failed to load'));
    
    render(
      <BrowserRouter>
        <ContentDetail />
      </BrowserRouter>
    );
    
    // Wait for error to display
    await waitFor(() => {
      expect(screen.getByText('Failed to load content. Please try again later.')).toBeInTheDocument();
    });
    
    // Check if back button is shown
    expect(screen.getByText('Back to Content')).toBeInTheDocument();
  });
});
