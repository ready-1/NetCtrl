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
    currentUser: () => api.get('/auth/profile'),
    register: (userData) => api.post('/auth/register', userData),
  },
  
  // Switch management
  switches: {
    getAll: () => api.get('/switch'),
    getById: (id) => api.get(`/switch/${id}`),
    create: (data) => api.post('/switch', data),
    update: (id, data) => api.put(`/switch/${id}`, data),
    delete: (id) => api.delete(`/switch/${id}`),
    getMetrics: (id) => api.get(`/switch/${id}/metrics`),
    getStatus: () => api.get('/switch/dashboard'),
    poll: (id) => api.post(`/switch/${id}/poll`),
  },
  
  // Content management
  content: {
    getAll: (params) => api.get('/cms', { params }),
    getUnpublished: () => api.get('/cms/unpublished'),
    getById: (id) => api.get(`/cms/id/${id}`),
    getBySlug: (slug) => api.get(`/cms/${slug}`),
    create: (data) => api.post('/cms', data),
    update: (id, data) => api.put(`/cms/${id}`, data),
    delete: (id) => api.delete(`/cms/${id}`),
    getCategories: () => api.get('/cms/categories'),
    getTags: () => api.get('/cms/tags'),
    getRevisions: (id) => api.get(`/cms/${id}/revisions`),
    getRevision: (id, revisionId) => api.get(`/cms/${id}/revisions/${revisionId}`),
    restoreRevision: (id, revisionId) => api.post(`/cms/${id}/revisions/${revisionId}/restore`),
    uploadAttachment: (id, formData) => api.post(`/cms/${id}/attachments`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }),
    deleteAttachment: (id, attachmentId) => api.delete(`/cms/${id}/attachments/${attachmentId}`),
    getAttachments: (id) => api.get(`/cms/${id}/attachments`),
    getStats: () => api.get('/cms/stats'),
    search: (query) => api.get('/cms/search', { params: { q: query } }),
  },
  
  // User management
  users: {
    getAll: () => api.get('/auth/users'),
    getById: (id) => api.get(`/auth/users/${id}`),
    create: (data) => api.post('/auth/register', data),
    update: (id, data) => api.put(`/auth/users/${id}`, data),
    delete: (id) => api.delete(`/auth/users/${id}`),
    updateRole: (id, roles) => api.put(`/auth/users/${id}`, { roles }),
    getRoles: () => api.get('/auth/roles'),
  },
  
  // Dashboard
  dashboard: {
    getStats: () => api.get('/switch/dashboard'),
  },
};

export default apiService;
