import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import Switches from '../Switches';
import apiService from '../../../services/api';

// Mock the API service
jest.mock('../../../services/api', () => ({
  switches: {
    getAll: jest.fn(),
    getStatus: jest.fn(),
    delete: jest.fn()
  }
}));

// Mock data
const mockSwitches = [
  {
    id: 1,
    name: 'Switch 1',
    ip_address: '192.168.1.1',
    model: 'Model A',
    status: 'online'
  },
  {
    id: 2,
    name: 'Switch 2',
    ip_address: '192.168.1.2',
    model: 'Model B',
    status: 'offline'
  }
];

const mockStatusData = {
  "1": {
    status: 'online',
    last_updated: '2023-03-01T12:00:00Z'
  },
  "2": {
    status: 'offline',
    last_updated: '2023-03-01T12:00:00Z'
  }
};

describe('Switches Component', () => {
  beforeEach(() => {
    // Reset mocks
    jest.clearAllMocks();
    
    // Setup default mocks
    apiService.switches.getAll.mockResolvedValue({ data: mockSwitches });
    apiService.switches.getStatus.mockResolvedValue({ 
      data: {
        switches: mockSwitches.map(s => ({
          ...s,
          id: s.id,
          status: s.status,
          last_updated: '2023-03-01T12:00:00Z'
        }))
      }
    });
  });

  test('renders loading spinner initially', () => {
    render(
      <BrowserRouter>
        <Switches />
      </BrowserRouter>
    );
    
    expect(screen.getByRole('status')).toBeInTheDocument();
  });

  test('fetches switches and status on mount', async () => {
    render(
      <BrowserRouter>
        <Switches />
      </BrowserRouter>
    );
    
    // Should call the API methods
    expect(apiService.switches.getAll).toHaveBeenCalledTimes(1);
    expect(apiService.switches.getStatus).toHaveBeenCalledTimes(1);
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Should render switch names
    expect(screen.getByText('Switch 1')).toBeInTheDocument();
    expect(screen.getByText('Switch 2')).toBeInTheDocument();
  });

  test('renders proper status badges', async () => {
    render(
      <BrowserRouter>
        <Switches />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Check for online and offline badges
    const statusBadges = screen.getAllByText(/Online|Offline/);
    expect(statusBadges).toHaveLength(2);
    expect(statusBadges[0].textContent).toBe('Online');
    expect(statusBadges[1].textContent).toBe('Offline');
  });

  test('search filter works properly', async () => {
    render(
      <BrowserRouter>
        <Switches />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Search for "Switch 1"
    const searchInput = screen.getByPlaceholderText('Search by name or IP address...');
    fireEvent.change(searchInput, { target: { value: 'Switch 1' } });
    
    // Should show Switch 1 but not Switch 2
    expect(screen.getByText('Switch 1')).toBeInTheDocument();
    expect(screen.queryByText('Switch 2')).not.toBeInTheDocument();
    
    // Search for IP address
    fireEvent.change(searchInput, { target: { value: '192.168.1.2' } });
    
    // Should show Switch 2 but not Switch 1
    expect(screen.queryByText('Switch 1')).not.toBeInTheDocument();
    expect(screen.getByText('Switch 2')).toBeInTheDocument();
  });

  test('refresh button triggers status fetch', async () => {
    render(
      <BrowserRouter>
        <Switches />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Reset mock to count new calls
    apiService.switches.getStatus.mockClear();
    
    // Click the refresh button
    const refreshButton = screen.getByText('Refresh Status');
    fireEvent.click(refreshButton);
    
    // Should call getStatus again
    expect(apiService.switches.getStatus).toHaveBeenCalledTimes(1);
    
    // Should show refreshing state
    expect(screen.getByText('Refreshing...')).toBeInTheDocument();
  });

  test('delete modal shows and confirms deletion', async () => {
    // Mock delete to resolve successfully
    apiService.switches.delete.mockResolvedValue({});
    
    render(
      <BrowserRouter>
        <Switches />
      </BrowserRouter>
    );
    
    // Wait for data to load
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
    
    // Find delete buttons (the trashcan icons)
    const deleteButtons = screen.getAllByRole('button', { name: '' });
    
    // Click the first delete button
    fireEvent.click(deleteButtons[2]); // The third button should be the delete button for the first switch
    
    // Confirm modal is showing
    expect(screen.getByText(/Are you sure you want to delete the switch/)).toBeInTheDocument();
    
    // Click the confirm delete button
    const confirmButton = screen.getByText('Delete', { selector: 'button' });
    fireEvent.click(confirmButton);
    
    // Should call delete with the correct ID
    expect(apiService.switches.delete).toHaveBeenCalledWith(1);
    
    // Wait for deletion to process
    await waitFor(() => {
      // Should only show one switch now
      expect(screen.queryByText('Switch 1')).not.toBeInTheDocument();
      expect(screen.getByText('Switch 2')).toBeInTheDocument();
    });
  });
});
