/**
 * Application routes configuration
 * 
 * This file centralizes all route definitions to avoid hardcoding paths
 * throughout the application. Use these routes when linking between pages.
 */

const routes = {
  // Public routes
  home: '/',
  
  // Auth routes
  auth: {
    login: '/login',
    register: '/register',
    resetPassword: '/reset-password',
  },
  
  // Protected routes (all under /app)
  content: {
    list: '/app/content',
    create: '/app/content/new',
    detail: (id: string) => `/app/content/${id}`,
    edit: (id: string) => `/app/content/${id}/edit`,
  },
  files: {
    list: '/app/files',
    detail: (id: string) => `/app/files/${id}`,
    upload: '/app/files/upload',
  },
  user: {
    profile: '/app/user/profile',
    settings: '/app/user/settings',
  },
  system: {
    settings: '/app/settings',
  },
};

export default routes;
