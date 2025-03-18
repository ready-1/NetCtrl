import axios from 'axios';

/**
 * Configure Axios instance with default settings
 * 
 * This creates a pre-configured axios instance with:
 * - Base URL for API requests
 * - Default headers
 * - Request/response interceptors for consistent error handling
 */

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for adding auth token
api.interceptors.request.use(
  (config) => {
    // Get token from localStorage
    const token = localStorage.getItem('auth-token');
    
    // If token exists, add it to the request headers
    if (token) {
      config.headers = config.headers || {};
      config.headers.Authorization = `Bearer ${token}`;
    }
    
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor for handling errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle authentication errors
    if (error.response && error.response.status === 401) {
      // Clear local storage
      localStorage.removeItem('auth-token');
      
      // Redirect to login page if not already there
      if (window.location.pathname !== '/login') {
        window.location.href = '/login';
      }
    }
    
    // Create more detailed error information
    const enhancedError = {
      ...error,
      message: error.response?.data?.detail || error.message || 'An unknown error occurred',
      status: error.response?.status,
      data: error.response?.data,
    };
    
    return Promise.reject(enhancedError);
  }
);

export default api;
