import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import ContentList from '../ContentList';
import apiService from '../../../services/api';

// Mock the API service
jest.mock('../../../services/api', () => ({
  content: {
    getAll: jest.fn(),
    getUnpublished: jest.fn(),
    getCategories: jest.fn(),
    getTags: jest.fn(),
    delete: jest.fn()
  }
}));

// Mock data
const mockContent = [
  {
    id: 1,
    title: 'Test Article 1',
    slug: 'test-article-1',
    summary: 'This is a test article',
    content: 'Content for article 1',
    published: true,
    author_name: 'John Doe',
    category: { id: 1, name: 'Documentation' },
    tags: [{ id: 1, name: 'Network' }, { id: 2, name: 'Guide' }],
    created_at: '2023-01-01T10:00:00Z',
    updated_at: '2023-01-02T10:00:00Z'
  },
  {
    id: 2,
    title: 'Test Article 2',
    slug: 'test-article-2',
    summary: 'This is another test article',
    content: 'Content for article 2',
    published: false,
    author_name: 'Jane Smith',
    category: { id: 2, name: 'Tutorials' },
    tags: [{ id: 3, name: 'Setup' }],
    created_at: '2023-02-01T10:00:00Z',
    updated_at: '2023-02-02T10:00:00Z'
  }
];

const mockCategories = [
  { id: 1, name: 'Documentation' },
  { id: 2, name: 'Tutorials' },
  { id: 3, name: 'News' }
];

const mockTags = [
  { id: 1, name: 'Network' },
  { id: 2, name: 'Guide' },
  { id: 3, name: 'Setup' }
];

describe('ContentList Component', () => {
  beforeEach(() => {
    // Reset mocks
    jest.clearAllMocks();
    
    // Setup default mocks
    apiService.content.getAll.mockResolvedValue({ 
      data: mockContent
    });
    apiService.content.getUnpublished.mockResolvedValue({
      data: mockContent.filter(c => !c.published)
    });
    apiService.content.getCategories.mockResolvedValue({ 
      data: mockCategories
    });
    apiService.content.getTags.mockResolvedValue({ 
      data: mockTags
    });
  });

  test('renders loading spinner initially', () => {
    render(
      <BrowserRouter>
        <ContentList />
      </BrowserRouter>
    );
    
    expect(screen.getByRole('status')).toBeInTheDocument();
  });

  test('fetches content, categories, and tags on mount', async () => {
    render(
      <BrowserRouter>
        <ContentList />
      </BrowserRouter>
    );
    
    // Should call the API methods
    expect(apiService.content.getAll).toHaveBeenCalledTimes(1);
    expect(apiService.content.getCategories).toHaveBeenCalledTimes(1);
    expect(apiService.content.getTags).toHaveBeenCalledTimes(1);
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Should render content titles
    expect(screen.getByText('Test Article 1')).toBeInTheDocument();
    expect(screen.getByText('Test Article 2')).toBeInTheDocument();
  });

  test('renders content with correct status badges', async () => {
    render(
      <BrowserRouter>
        <ContentList />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Check for published and draft badges
    const publishedBadge = screen.getByText('Published');
    const draftBadge = screen.getByText('Draft');
    
    expect(publishedBadge).toBeInTheDocument();
    expect(draftBadge).toBeInTheDocument();
  });

  test('search filter works properly', async () => {
    render(
      <BrowserRouter>
        <ContentList />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Search for "Article 1"
    const searchInput = screen.getByPlaceholderText('Search by title or description...');
    fireEvent.change(searchInput, { target: { value: 'Article 1' } });
    
    // Should show Article 1 but not Article 2
    expect(screen.getByText('Test Article 1')).toBeInTheDocument();
    expect(screen.queryByText('Test Article 2')).not.toBeInTheDocument();
  });

  test('tab switching filters content correctly', async () => {
    render(
      <BrowserRouter>
        <ContentList />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Default tab should be "Published", which shows only published content
    
    // Switch to "All Content" tab
    fireEvent.click(screen.getByText('All Content'));
    
    // Should show both articles
    expect(screen.getByText('Test Article 1')).toBeInTheDocument();
    expect(screen.getByText('Test Article 2')).toBeInTheDocument();
    
    // Switch to "Drafts" tab
    fireEvent.click(screen.getByText('Drafts'));
    
    // Should only show Draft article
    expect(screen.queryByText('Test Article 1')).not.toBeInTheDocument();
    expect(screen.getByText('Test Article 2')).toBeInTheDocument();
  });

  test('delete modal shows and confirms deletion', async () => {
    // Mock delete to resolve successfully
    apiService.content.delete.mockResolvedValue({});
    
    render(
      <BrowserRouter>
        <ContentList />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Find the dropdown toggle button for the first article
    const dropdownButtons = screen.getAllByRole('button', { name: '' });
    
    // Open the dropdown for the first article
    fireEvent.click(dropdownButtons[3]); // This is a bit fragile, but it's the dropdown toggle
    
    // Wait for dropdown to open
    await waitFor(() => {
      // Click the Delete option
      fireEvent.click(screen.getByText('Delete'));
    });
    
    // Confirm modal is showing
    expect(screen.getByText(/Are you sure you want to delete/)).toBeInTheDocument();
    
    // Click the confirm delete button
    const confirmButton = screen.getByText('Delete', { selector: 'button.btn-danger' });
    fireEvent.click(confirmButton);
    
    // Should call delete with the correct ID
    expect(apiService.content.delete).toHaveBeenCalledWith(1);
    
    // Wait for deletion to process
    await waitFor(() => {
      // Should only show one article now
      expect(screen.queryByText('Test Article 1')).not.toBeInTheDocument();
      expect(screen.getByText('Test Article 2')).toBeInTheDocument();
    });
  });

  test('sorting works correctly', async () => {
    render(
      <BrowserRouter>
        <ContentList />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Get the title sort button
    const titleSortButton = screen.getByText('Title');
    
    // Click the title sort button to sort by title (default descending)
    fireEvent.click(titleSortButton);
    
    // Check if the sort direction indicator appears (using icon class)
    const sortIndicator = screen.getByClassName('bi-caret-down-fill');
    expect(sortIndicator).toBeInTheDocument();
    
    // Click again to toggle sort direction
    fireEvent.click(titleSortButton);
    
    // Check if the sort direction indicator changes
    await waitFor(() => {
      const ascendingIndicator = screen.getByClassName('bi-caret-up-fill');
      expect(ascendingIndicator).toBeInTheDocument();
    });
  });

  test('category filter works correctly', async () => {
    render(
      <BrowserRouter>
        <ContentList />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Get the category filter dropdown
    const categoryFilter = screen.getByDisplayValue('All Categories');
    
    // Set category filter to "Tutorials"
    fireEvent.change(categoryFilter, { target: { value: '2' } });
    
    // Should only show content with Tutorials category
    expect(screen.queryByText('Test Article 1')).not.toBeInTheDocument();
    expect(screen.getByText('Test Article 2')).toBeInTheDocument();
  });
});
