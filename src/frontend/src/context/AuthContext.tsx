import React, { createContext, useContext, useReducer, useEffect, ReactNode } from 'react';
import api from '../services/api/apiClient';
import { User } from '../types/user';

// Authentication state types
interface AuthState {
  isInitialized: boolean;
  isAuthenticated: boolean;
  user: User | null;
  token: string | null;
}

// Initial auth state
const initialAuthState: AuthState = {
  isInitialized: false,
  isAuthenticated: false,
  user: null,
  token: null,
};

// Action types
type AuthAction =
  | { type: 'INITIALIZE'; payload: { isAuthenticated: boolean; user: User | null; token: string | null } }
  | { type: 'LOGIN'; payload: { user: User; token: string } }
  | { type: 'LOGOUT' }
  | { type: 'REGISTER'; payload: { user: User; token: string } }
  | { type: 'UPDATE_USER'; payload: { user: User } };

// Auth reducer
const authReducer = (state: AuthState, action: AuthAction): AuthState => {
  switch (action.type) {
    case 'INITIALIZE':
      return {
        ...state,
        isInitialized: true,
        isAuthenticated: action.payload.isAuthenticated,
        user: action.payload.user,
        token: action.payload.token,
      };
    case 'LOGIN':
      return {
        ...state,
        isAuthenticated: true,
        user: action.payload.user,
        token: action.payload.token,
      };
    case 'LOGOUT':
      return {
        ...state,
        isAuthenticated: false,
        user: null,
        token: null,
      };
    case 'REGISTER':
      return {
        ...state,
        isAuthenticated: true,
        user: action.payload.user,
        token: action.payload.token,
      };
    case 'UPDATE_USER':
      return {
        ...state,
        user: action.payload.user,
      };
    default:
      return state;
  }
};

// Auth context type
interface AuthContextType extends AuthState {
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
  register: (username: string, email: string | undefined, password: string) => Promise<void>;
  updateUser: (user: User) => void;
  hasPermission: (permission: string) => boolean;
  hasRole: (role: string) => boolean;
}

// Create context
const AuthContext = createContext<AuthContextType>({
  ...initialAuthState,
  login: () => Promise.resolve(),
  logout: () => {},
  register: () => Promise.resolve(),
  updateUser: () => {},
  hasPermission: () => false,
  hasRole: () => false,
});

// Hook to use auth context
export const useAuth = () => useContext(AuthContext);

// Auth provider props
interface AuthProviderProps {
  children: ReactNode;
}

// Auth provider component
export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [state, dispatch] = useReducer(authReducer, initialAuthState);

  // Initialize auth state
  useEffect(() => {
    const initialize = async () => {
      try {
        // Check if token exists in localStorage
        const token = localStorage.getItem('auth-token');
        
        if (token) {
          // Set token in API headers
          api.defaults.headers.common.Authorization = `Bearer ${token}`;
          
          // Get current user
          const response = await api.get('/api/v1/users/me');
          const user = response.data;
          
          dispatch({
            type: 'INITIALIZE',
            payload: {
              isAuthenticated: true,
              user,
              token,
            },
          });
        } else {
          dispatch({
            type: 'INITIALIZE',
            payload: {
              isAuthenticated: false,
              user: null,
              token: null,
            },
          });
        }
      } catch (error) {
        console.error('Failed to initialize auth:', error);
        // Clear invalid auth data
        localStorage.removeItem('auth-token');
        
        dispatch({
          type: 'INITIALIZE',
          payload: {
            isAuthenticated: false,
            user: null,
            token: null,
          },
        });
      }
    };

    initialize();
  }, []);

  // Login method
  const login = async (username: string, password: string) => {
    try {
      const response = await api.post('/api/v1/jwt/login', {
        username,
        password,
      });
      
      const { access_token } = response.data;
      
      // Store token in localStorage
      localStorage.setItem('auth-token', access_token);
      
      // Set token in API headers
      api.defaults.headers.common.Authorization = `Bearer ${access_token}`;
      
      // Get user data
      const userResponse = await api.get('/api/v1/users/me');
      const user = userResponse.data;
      
      dispatch({
        type: 'LOGIN',
        payload: {
          user,
          token: access_token,
        },
      });
    } catch (error) {
      console.error('Login failed:', error);
      throw error;
    }
  };

  // Logout method
  const logout = () => {
    // Remove token from localStorage
    localStorage.removeItem('auth-token');
    
    // Remove token from API headers
    delete api.defaults.headers.common.Authorization;
    
    dispatch({ type: 'LOGOUT' });
  };

  // Register method
  const register = async (username: string, email: string | undefined, password: string) => {
    try {
      const response = await api.post('/api/v1/register/register', {
        username,
        email,
        password,
      });
      
      const { access_token } = response.data;
      
      // Store token in localStorage
      localStorage.setItem('auth-token', access_token);
      
      // Set token in API headers
      api.defaults.headers.common.Authorization = `Bearer ${access_token}`;
      
      // Get user data
      const userResponse = await api.get('/api/v1/users/me');
      const user = userResponse.data;
      
      dispatch({
        type: 'REGISTER',
        payload: {
          user,
          token: access_token,
        },
      });
    } catch (error) {
      console.error('Registration failed:', error);
      throw error;
    }
  };

  // Update user method
  const updateUser = (user: User) => {
    dispatch({
      type: 'UPDATE_USER',
      payload: {
        user,
      },
    });
  };

  // Permission check method
  const hasPermission = (permission: string): boolean => {
    if (!state.user || !state.user.permissions) {
      return false;
    }
    return state.user.permissions.includes(permission);
  };

  // Role check method
  const hasRole = (role: string): boolean => {
    if (!state.user || !state.user.role) {
      return false;
    }
    return state.user.role === role;
  };

  return (
    <AuthContext.Provider
      value={{
        ...state,
        login,
        logout,
        register,
        updateUser,
        hasPermission,
        hasRole,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};
