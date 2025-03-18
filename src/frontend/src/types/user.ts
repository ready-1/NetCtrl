/**
 * User-related type definitions
 */

// Role enum
export enum UserRole {
  ADMIN = 'admin',
  EDITOR = 'editor',
  USER = 'user',
}

// User interface
export interface User {
  id: number;
  username: string;
  email?: string;
  role: UserRole;
  permissions: string[];
  is_active: boolean;
  is_superuser: boolean;
  created_at: string;
  updated_at: string;
}

// User creation/update payload
export interface UserCreatePayload {
  username: string;
  email?: string;
  password: string;
  role?: UserRole;
  is_active?: boolean;
}

// User update payload
export interface UserUpdatePayload {
  username?: string;
  email?: string;
  password?: string;
  role?: UserRole;
  is_active?: boolean;
}

// Login credentials
export interface LoginCredentials {
  username: string;
  password: string;
}

// Registration credentials
export interface RegistrationCredentials {
  username: string;
  email?: string;
  password: string;
  password_confirm: string;
}

// Auth tokens
export interface AuthTokens {
  access_token: string;
  token_type: string;
}
