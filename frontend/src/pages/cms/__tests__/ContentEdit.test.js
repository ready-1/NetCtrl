import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import ContentEdit from '../ContentEdit';
import apiService from '../../../services/api';

// Mock the API service
jest.mock('../../../services/api', () => ({
  content: {
    getById: jest.fn(),
    create: jest.fn(),
    update: jest.fn(),
    getCategories: jest.fn(),
    getTags: jest.fn()
  }
}));

// Mock react-router-dom's useParams and useNavigate hooks
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
  body: 'This is the body of the test article.',
  category: '1',
  tags: ['Network', 'Guide'],
  status: 'published',
  featured_image: null,
  files: [
    {
      id: 'file1',
      name: 'document.pdf',
      type: 'application/pdf',
      size: '2.5 MB'
    }
  ]
};

const mockCategories = [
  { id: '1', name: 'Documentation' },
  { id: '2', name: 'Tutorials' },
  { id: '3', name: 'News' }
];

const mockTags = [
  { id: '1', name: 'Network' },
  { id: '2', name: 'Guide' },
  { id: '3', name: 'Setup' }
];

describe('ContentEdit Component', () => {
  beforeEach(() => {
    // Reset mocks
    jest.clearAllMocks();
    
    // Setup default mocks
    apiService.content.getById.mockResolvedValue({ 
      data: mockContent
    });
    apiService.content.getCategories.mockResolvedValue({ 
      data: mockCategories
    });
    apiService.content.getTags.mockResolvedValue({ 
      data: mockTags
    });
    apiService.content.create.mockResolvedValue({
      data: { id: 'new-content-id', ...mockContent }
    });
    apiService.content.update.mockResolvedValue({
      data: mockContent
    });
    
    // Mock file reading
    global.FileReader = function() {
      this.readAsDataURL = function() {
        this.onload({
          target: {
            result: 'data:image/png;base64,fakeimagedatafakeimagedata'
          }
        });
      };
    };
    
    // Mock URL methods
    global.URL.createObjectURL = jest.fn(() => 'blob:test-url');
  });

  test('renders loading spinner initially when editing', () => {
    render(
      <BrowserRouter>
        <ContentEdit />
      </BrowserRouter>
    );
    
    expect(screen.getByRole('status')).toBeInTheDocument();
  });

  test('fetches content, categories, and tags on mount when editing', async () => {
    render(
      <BrowserRouter>
        <ContentEdit />
      </BrowserRouter>
    );
    
    // Should call the API methods
    expect(apiService.content.getById).toHaveBeenCalledWith('123');
    expect(apiService.content.getCategories).toHaveBeenCalled();
    expect(apiService.content.getTags).toHaveBeenCalled();
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Should fill the form with content data
    expect(screen.getByDisplayValue('Test Article')).toBeInTheDocument();
    expect(screen.getByDisplayValue('test-article')).toBeInTheDocument();
    expect(screen.getByDisplayValue('This is a test article description')).toBeInTheDocument();
    expect(screen.getByDisplayValue('This is the body of the test article.')).toBeInTheDocument();
  });

  test('does not show loading spinner for new content', () => {
    // Mock useParams to return no ID (new content)
    jest.spyOn(require('react-router-dom'), 'useParams').mockReturnValue({});
    
    render(
      <BrowserRouter>
        <ContentEdit />
      </BrowserRouter>
    );
    
    // Should show "Create New Content" heading
    expect(screen.getByText('Create New Content')).toBeInTheDocument();
    
    // Should not call getById
    expect(apiService.content.getById).not.toHaveBeenCalled();
    
    // Should still fetch categories and tags
    expect(apiService.content.getCategories).toHaveBeenCalled();
    expect(apiService.content.getTags).toHaveBeenCalled();
  });

  test('validates form fields properly', async () => {
    jest.spyOn(require('react-router-dom'), 'useParams').mockReturnValue({});
    
    render(
      <BrowserRouter>
        <ContentEdit />
      </BrowserRouter>
    );
    
    // Wait for categories and tags to load
    await waitFor(() => {
      expect(apiService.content.getCategories).toHaveBeenCalled();
    });
    
    // Try to submit empty form
    fireEvent.click(screen.getByText('Create Content'));
    
    // Check if validation errors appear
    await waitFor(() => {
      expect(screen.getByText('Title is required')).toBeInTheDocument();
      expect(screen.getByText('Content body is required')).toBeInTheDocument();
      expect(screen.getByText('Category is required')).toBeInTheDocument();
    });
    
    // Fill required fields
    fireEvent.change(screen.getByLabelText(/Title/), { 
      target: { value: 'New Test Article' } 
    });
    
    fireEvent.change(screen.getByLabelText(/Content/), { 
      target: { value: 'This is the content body' } 
    });
    
    // Select category
    fireEvent.change(screen.getByLabelText(/Category/), { 
      target: { value: '1' } 
    });
    
    // Submit again
    fireEvent.click(screen.getByText('Create Content'));
    
    // Should call create API
    await waitFor(() => {
      expect(apiService.content.create).toHaveBeenCalledWith(
        expect.objectContaining({
          title: 'New Test Article',
          body: 'This is the content body',
          category: '1'
        })
      );
    });
  });

  test('automatically generates slug from title', async () => {
    jest.spyOn(require('react-router-dom'), 'useParams').mockReturnValue({});
    
    render(
      <BrowserRouter>
        <ContentEdit />
      </BrowserRouter>
    );
    
    // Enter a title with special characters
    fireEvent.change(screen.getByLabelText(/Title/), { 
      target: { value: 'Test Article with Special-Characters!' } 
    });
    
    // Check if slug is auto-generated
    await waitFor(() => {
      const slugInput = screen.getByLabelText(/Slug/);
      expect(slugInput.value).toBe('test-article-with-special-characters');
    });
  });

  test('switches between tabs correctly', async () => {
    render(
      <BrowserRouter>
        <ContentEdit />
      </BrowserRouter>
    );
    
    // Wait for content to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Should start on Content tab
    expect(screen.getByLabelText(/Title/)).toBeInTheDocument();
    
    // Click "Next: Metadata" button
    fireEvent.click(screen.getByText('Next: Metadata'));
    
    // Should show Metadata tab content
    expect(screen.getByLabelText(/Slug/)).toBeInTheDocument();
    expect(screen.getByLabelText(/Category/)).toBeInTheDocument();
    
    // Click "Next: Files" button
    fireEvent.click(screen.getByText('Next: Files'));
    
    // Should show Files tab content
    expect(screen.getByText('Attached Files')).toBeInTheDocument();
    expect(screen.getByText('Upload File')).toBeInTheDocument();
    
    // Go back to Metadata
    fireEvent.click(screen.getByText('Back to Metadata'));
    
    // Should show Metadata tab again
    expect(screen.getByLabelText(/Category/)).toBeInTheDocument();
    
    // Go back to Content
    fireEvent.click(screen.getByText('Back to Content'));
    
    // Should show Content tab again
    expect(screen.getByLabelText(/Title/)).toBeInTheDocument();
  });

  test('adds and removes tags', async () => {
    render(
      <BrowserRouter>
        <ContentEdit />
      </BrowserRouter>
    );
    
    // Wait for content to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Go to Metadata tab
    fireEvent.click(screen.getByText('Next: Metadata'));
    
    // Check existing tags (from mock data)
    expect(screen.getByText('Network')).toBeInTheDocument();
    expect(screen.getByText('Guide')).toBeInTheDocument();
    
    // Add a new tag
    fireEvent.change(screen.getByPlaceholderText('Add a tag'), { 
      target: { value: 'NewTag' } 
    });
    fireEvent.click(screen.getByText('Add'));
    
    // New tag should appear
    expect(screen.getByText('NewTag')).toBeInTheDocument();
    
    // Remove a tag
    const removeButtons = screen.getAllByRole('button', { name: '' });
    fireEvent.click(removeButtons[0]); // Remove first tag
    
    // Tag should be removed
    expect(screen.queryByText('Network')).not.toBeInTheDocument();
  });

  test('shows file list in Files tab', async () => {
    render(
      <BrowserRouter>
        <ContentEdit />
      </BrowserRouter>
    );
    
    // Wait for content to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Go to Files tab
    fireEvent.click(screen.getByText('Next: Metadata'));
    fireEvent.click(screen.getByText('Next: Files'));
    
    // Should show the attached file
    expect(screen.getByText('document.pdf')).toBeInTheDocument();
    expect(screen.getByText('(2.5 MB)')).toBeInTheDocument();
  });

  test('opens file upload modal and handles upload', async () => {
    render(
      <BrowserRouter>
        <ContentEdit />
      </BrowserRouter>
    );
    
    // Wait for content to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Go to Files tab
    fireEvent.click(screen.getByText('Next: Metadata'));
    fireEvent.click(screen.getByText('Next: Files'));
    
    // Click upload button
    fireEvent.click(screen.getByText('Upload File'));
    
    // Modal should appear
    expect(screen.getByText('Choose File')).toBeInTheDocument();
    
    // Cancel upload
    fireEvent.click(screen.getByText('Cancel'));
    
    // Modal should close
    expect(screen.queryByText('Choose File')).not.toBeInTheDocument();
  });

  test('handles form submission for existing content', async () => {
    render(
      <BrowserRouter>
        <ContentEdit />
      </BrowserRouter>
    );
    
    // Wait for content to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Modify the title
    fireEvent.change(screen.getByLabelText(/Title/), { 
      target: { value: 'Updated Test Article' } 
    });
    
    // Submit the form
    fireEvent.click(screen.getByText('Save Changes'));
    
    // Should call update API
    await waitFor(() => {
      expect(apiService.content.update).toHaveBeenCalledWith(
        '123',
        expect.objectContaining({
          title: 'Updated Test Article'
        })
      );
    });
  });

  test('handles "Save As" dropdown options', async () => {
    render(
      <BrowserRouter>
        <ContentEdit />
      </BrowserRouter>
    );
    
    // Wait for content to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Click Save As dropdown
    fireEvent.click(screen.getByText('Save As'));
    
    // Click "Draft" option
    fireEvent.click(screen.getByText('Draft'));
    
    // Should call update API with draft status
    await waitFor(() => {
      expect(apiService.content.update).toHaveBeenCalledWith(
        '123',
        expect.objectContaining({
          status: 'draft'
        })
      );
    });
  });
});
