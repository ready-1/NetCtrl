import axios from 'axios';

// Create axios instance with base configuration
const api = axios.create({
  baseURL: '/api', // Will be prepended to all request URLs
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    // Get the token from localStorage
    const token = localStorage.getItem('token');
    
    // If token exists, add it to request headers
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    
    return config;
  },
  (error) => {
    // Handle request errors
    return Promise.reject(error);
  }
);

// Response interceptor
api.interceptors.response.use(
  (response) => {
    // Return successful responses
    return response;
  },
  (error) => {
    // Handle response errors
    if (error.response) {
      // Handle 401 Unauthorized errors (token expired or invalid)
      if (error.response.status === 401) {
        // Clear token from localStorage
        localStorage.removeItem('token');
        
        // Redirect to login page if not already there
        if (window.location.pathname !== '/login') {
          window.location.href = '/login';
        }
      }
      
      // Return response error
      return Promise.reject(error.response.data);
    }
    
    // Return network errors or other errors
    return Promise.reject(error);
  }
);

// API service object with methods for different API endpoints
const apiService = {
  // Authentication
  auth: {
    login: (credentials) => api.post('/auth/login', credentials),
    logout: () => api.post('/auth/logout'),
    currentUser: () => api.get('/auth/me'),
  },
  
  // Switch management
  switches: {
    getAll: () => api.get('/switches'),
    getById: (id) => api.get(`/switches/${id}`),
    create: (data) => api.post('/switches', data),
    update: (id, data) => api.put(`/switches/${id}`, data),
    delete: (id) => api.delete(`/switches/${id}`),
    getMetrics: (id) => api.get(`/switches/${id}/metrics`),
    getStatus: () => api.get('/switches/status'),
  },
  
  // Content management
  content: {
    getAll: () => api.get('/cms/content'),
    getById: (id) => api.get(`/cms/content/${id}`),
    getBySlug: (slug) => api.get(`/cms/content/slug/${slug}`),
    create: (data) => api.post('/cms/content', data),
    update: (id, data) => api.put(`/cms/content/${id}`, data),
    delete: (id) => api.delete(`/cms/content/${id}`),
    getCategories: () => api.get('/cms/categories'),
    getTags: () => api.get('/cms/tags'),
  },
  
  // User management
  users: {
    getAll: () => api.get('/admin/users'),
    getById: (id) => api.get(`/admin/users/${id}`),
    create: (data) => api.post('/admin/users', data),
    update: (id, data) => api.put(`/admin/users/${id}`, data),
    delete: (id) => api.delete(`/admin/users/${id}`),
    updateRole: (id, roles) => api.put(`/admin/users/${id}/roles`, { roles }),
    getRoles: () => api.get('/admin/roles'),
  },
  
  // Dashboard
  dashboard: {
    getStats: () => api.get('/dashboard/stats'),
  },
};

export default apiService;
