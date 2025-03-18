/**
 * Application routes configuration
 * 
 * This file centralizes all route definitions to avoid hardcoding paths
 * throughout the application. Use these routes when linking between pages.
 */

const routes = {
  auth: {
    login: '/login',
    register: '/register',
    resetPassword: '/reset-password',
  },
  content: {
    list: '/content',
    create: '/content/new',
    detail: (id: string) => `/content/${id}`,
    edit: (id: string) => `/content/${id}/edit`,
  },
  files: {
    list: '/files',
    detail: (id: string) => `/files/${id}`,
    upload: '/files/upload',
  },
  user: {
    profile: '/user/profile',
    settings: '/user/settings',
  },
  system: {
    settings: '/settings',
  },
};

export default routes;
