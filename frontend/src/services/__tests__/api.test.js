import axios from 'axios';
import apiService from '../api';

// Mock axios
jest.mock('axios');

describe('API Service', () => {
  beforeEach(() => {
    // Clear all mocks
    jest.clearAllMocks();
    
    // Setup localStorage mock
    Storage.prototype.getItem = jest.fn();
    Storage.prototype.removeItem = jest.fn();
  });

  afterEach(() => {
    // Restore localStorage mock
    Storage.prototype.getItem.mockRestore();
    Storage.prototype.removeItem.mockRestore();
  });

  test('axios should be configured with correct baseURL', () => {
    expect(axios.create).toHaveBeenCalledWith(
      expect.objectContaining({
        baseURL: '/api',
        headers: {
          'Content-Type': 'application/json',
        }
      })
    );
  });

  test('request interceptor should add Authorization header when token exists', () => {
    // Mock axios create to return an object with interceptors.request.use method
    const mockUse = jest.fn();
    axios.create.mockReturnValue({
      interceptors: {
        request: { use: mockUse },
        response: { use: jest.fn() }
      }
    });

    // Get the interceptor function
    const requestInterceptor = mockUse.mock.calls[0][0];
    
    // Mock localStorage to return a token
    Storage.prototype.getItem.mockReturnValue('test-token');
    
    // Create a mock config object
    const config = { headers: {} };
    
    // Call the interceptor
    const result = requestInterceptor(config);
    
    // Expect Authorization header to be added
    expect(result.headers['Authorization']).toBe('Bearer test-token');
  });

  test('request interceptor should not add Authorization header when token does not exist', () => {
    // Mock axios create to return an object with interceptors.request.use method
    const mockUse = jest.fn();
    axios.create.mockReturnValue({
      interceptors: {
        request: { use: mockUse },
        response: { use: jest.fn() }
      }
    });

    // Get the interceptor function
    const requestInterceptor = mockUse.mock.calls[0][0];
    
    // Mock localStorage to return null
    Storage.prototype.getItem.mockReturnValue(null);
    
    // Create a mock config object
    const config = { headers: {} };
    
    // Call the interceptor
    const result = requestInterceptor(config);
    
    // Expect Authorization header to not be added
    expect(result.headers['Authorization']).toBeUndefined();
  });

  test('response interceptor should handle 401 errors', () => {
    // Mock window.location
    const originalLocation = window.location;
    delete window.location;
    window.location = { pathname: '/dashboard', href: '' };

    // Mock axios create to return an object with interceptors.request.use method
    const mockUse = jest.fn();
    axios.create.mockReturnValue({
      interceptors: {
        request: { use: jest.fn() },
        response: { use: mockUse }
      }
    });

    // Get the error interceptor function
    const errorInterceptor = mockUse.mock.calls[0][1];
    
    // Create a mock error object with 401 status
    const error = {
      response: {
        status: 401,
        data: { message: 'Unauthorized' }
      }
    };
    
    // Call the interceptor and catch the rejection
    expect.assertions(3);
    return errorInterceptor(error).catch(err => {
      // Expect token to be removed from localStorage
      expect(Storage.prototype.removeItem).toHaveBeenCalledWith('token');
      
      // Expect location to be redirected to login if not already there
      expect(window.location.href).toBe('/login');
      
      // Expect the error data to be returned
      expect(err).toBe(error.response.data);
    });
    
    // Restore window.location
    window.location = originalLocation;
  });

  // Test API service methods
  describe('auth', () => {
    test('login should call the correct endpoint with credentials', () => {
      // Mock axios post to return a promise
      axios.post = jest.fn().mockResolvedValue({ data: {} });
      
      // Call the login method
      const credentials = { username: 'test', password: 'password' };
      apiService.auth.login(credentials);
      
      // Expect axios.post to be called with the correct endpoint and data
      expect(axios.post).toHaveBeenCalledWith('/auth/login', credentials);
    });
  });

  describe('switches', () => {
    test('getAll should call the correct endpoint', () => {
      // Mock axios get to return a promise
      axios.get = jest.fn().mockResolvedValue({ data: [] });
      
      // Call the getAll method
      apiService.switches.getAll();
      
      // Expect axios.get to be called with the correct endpoint
      expect(axios.get).toHaveBeenCalledWith('/switch');
    });

    test('getById should call the correct endpoint with id', () => {
      // Mock axios get to return a promise
      axios.get = jest.fn().mockResolvedValue({ data: {} });
      
      // Call the getById method
      apiService.switches.getById(1);
      
      // Expect axios.get to be called with the correct endpoint
      expect(axios.get).toHaveBeenCalledWith('/switch/1');
    });
  });

  describe('content', () => {
    test('getAll should call the correct endpoint', () => {
      // Mock axios get to return a promise
      axios.get = jest.fn().mockResolvedValue({ data: [] });
      
      // Call the getAll method
      apiService.content.getAll();
      
      // Expect axios.get to be called with the correct endpoint
      expect(axios.get).toHaveBeenCalledWith('/cms');
    });

    test('getBySlug should call the correct endpoint with slug', () => {
      // Mock axios get to return a promise
      axios.get = jest.fn().mockResolvedValue({ data: {} });
      
      // Call the getBySlug method
      apiService.content.getBySlug('test-article');
      
      // Expect axios.get to be called with the correct endpoint
      expect(axios.get).toHaveBeenCalledWith('/cms/test-article');
    });
  });

  describe('users', () => {
    test('getAll should call the correct endpoint', () => {
      // Mock axios get to return a promise
      axios.get = jest.fn().mockResolvedValue({ data: [] });
      
      // Call the getAll method
      apiService.users.getAll();
      
      // Expect axios.get to be called with the correct endpoint
      expect(axios.get).toHaveBeenCalledWith('/auth/users');
    });

    test('getRoles should call the correct endpoint', () => {
      // Mock axios get to return a promise
      axios.get = jest.fn().mockResolvedValue({ data: [] });
      
      // Call the getRoles method
      apiService.users.getRoles();
      
      // Expect axios.get to be called with the correct endpoint
      expect(axios.get).toHaveBeenCalledWith('/auth/roles');
    });
  });
});
