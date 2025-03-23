import axios from 'axios';

/**
 * API client configuration
 * 
 * Creates an Axios instance configured for the API with:
 * - Base URL from environment variables (or fallback)
 * - Default request timeout
 * - Default headers
 * - Response/error interceptors
 */
const apiClient = axios.create({
  // Use environment variable for API URL with fallback
  baseURL: process.env.REACT_APP_API_URL || '/api/v1',
  // Default timeout in milliseconds
  timeout: 30000,
  // Common headers
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
});

// Request interceptor
apiClient.interceptors.request.use(
  (config) => {
    // Development mode - mock API for testing UI
    if (process.env.NODE_ENV === 'development' && process.env.REACT_APP_MOCK_API === 'true') {
      console.log('Using mock API responses in development mode');
      
      // Return a mock response instead of making the actual request
      return {
        ...config,
        // @ts-ignore - Ignore TypeScript errors for the mock adapter
        adapter: (config: any) => {
          return new Promise((resolve) => {
            // Simulate network delay
            setTimeout(() => {
              // Mock different API endpoints
              if (config.url === '/jwt/login') {
                resolve({
                  data: {
                    access_token: 'mock-jwt-token',
                    token_type: 'bearer',
                  },
                  status: 200,
                  statusText: 'OK',
                  headers: {},
                  config,
                });
              } else if (config.url === '/users/me') {
                resolve({
                  data: {
                    id: '1',
                    username: 'admin',
                    email: 'admin@example.com',
                    role: 'admin',
                    permissions: ['content:create', 'content:edit', 'content:delete', 'file:upload', 'file:delete', 'user:manage'],
                    created_at: '2025-01-01T00:00:00',
                    is_active: true,
                  },
                  status: 200,
                  statusText: 'OK',
                  headers: {},
                  config,
                });
              } else {
                // Default mock response
                resolve({
                  data: { message: 'Mock API response' },
                  status: 200,
                  statusText: 'OK',
                  headers: {},
                  config,
                });
              }
            }, 500); // 500ms delay to simulate network
          });
        },
      };
    }
    
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle specific API errors
    if (error.response) {
      // Server responded with an error status
      const { status } = error.response;
      
      // Handle unauthorized errors (redirect to login)
      if (status === 401) {
        // Clear stored auth tokens
        localStorage.removeItem('auth-token');
        
        // Only redirect if not already on login or register page
        if (!window.location.pathname.includes('/login') && !window.location.pathname.includes('/register')) {
          window.location.href = '/login';
        }
      }
      
      // Add more specific error handling as needed
    } else if (error.request) {
      // Request was made but no response received
      console.error('Network error. Please check your connection.');
    } else {
      // Error in setting up the request
      console.error('Error setting up the request:', error.message);
    }
    
    return Promise.reject(error);
  }
);

// Enable mock API in development by default
if (process.env.NODE_ENV === 'development' && process.env.REACT_APP_MOCK_API === undefined) {
  process.env.REACT_APP_MOCK_API = 'true';
  console.log('Mock API automatically enabled in development environment');
}

export default apiClient;
