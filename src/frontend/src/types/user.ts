/**
 * User-related type definitions for the CMS
 */

// User roles
export enum UserRole {
  ADMIN = 'admin',
  MANAGER = 'manager',
  USER = 'user',
}

// Base user model
export interface User {
  id: number;
  username: string;
  email: string | null;
  is_active: boolean;
  is_superuser: boolean;
  is_verified: boolean;
  role: string;
  first_name: string | null;
  last_name: string | null;
  created_at: string;
  updated_at: string;
  last_login: string | null;
  permissions?: string[];
}

// User update payload
export interface UserUpdate {
  email?: string;
  first_name?: string;
  last_name?: string;
  password?: string;
  role?: UserRole;
}

// User create payload
export interface UserCreate {
  username: string;
  email?: string;
  password: string;
  role?: UserRole;
  first_name?: string;
  last_name?: string;
}

// User query parameters
export interface UserQueryParams {
  role?: UserRole;
  search?: string;
  is_active?: boolean;
  page?: number;
  limit?: number;
}

// User list response
export interface UserListResponse {
  items: User[];
  total: number;
  page: number;
  limit: number;
  pages: number;
}
