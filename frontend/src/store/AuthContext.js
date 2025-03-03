import React, { createContext, useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import jwtDecode from 'jwt-decode';

// Create Auth Context
export const AuthContext = createContext({
  isAuthenticated: false,
  user: null,
  token: null,
  login: () => {},
  logout: () => {},
  checkAuthStatus: () => {},
});

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  // Initialize auth state from local storage
  useEffect(() => {
    checkAuthStatus();
  }, []);

  // Check if the user is authenticated
  const checkAuthStatus = () => {
    const storedToken = localStorage.getItem('token');
    if (storedToken) {
      try {
        // Verify token is valid and not expired
        const decoded = jwtDecode(storedToken);
        const currentTime = Date.now() / 1000;
        
        if (decoded.exp && decoded.exp > currentTime) {
          setToken(storedToken);
          setUser({
            id: decoded.sub,
            username: decoded.username,
            email: decoded.email,
            roles: decoded.roles || [],
          });
          setIsAuthenticated(true);
          
          // Set Authorization header for future requests
          axios.defaults.headers.common['Authorization'] = `Bearer ${storedToken}`;
        } else {
          // Token is expired
          handleLogout();
        }
      } catch (error) {
        console.error('Invalid token:', error);
        handleLogout();
      }
    }
    setLoading(false);
  };

  // Login user
  const login = async (credentials) => {
    try {
      const response = await axios.post('/api/auth/login', credentials);
      const { token } = response.data;
      
      // Store token in local storage
      localStorage.setItem('token', token);
      
      // Decode and set user info
      const decoded = jwtDecode(token);
      setToken(token);
      setUser({
        id: decoded.sub,
        username: decoded.username,
        email: decoded.email,
        roles: decoded.roles || [],
      });
      
      // Set authenticated status and axios default header
      setIsAuthenticated(true);
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      
      return { success: true };
    } catch (error) {
      console.error('Login error:', error);
      return { 
        success: false, 
        message: error.response?.data?.message || 'Login failed. Please check your credentials.' 
      };
    }
  };

  // Logout user
  const handleLogout = () => {
    // Clear token from local storage
    localStorage.removeItem('token');
    
    // Reset auth state
    setToken(null);
    setUser(null);
    setIsAuthenticated(false);
    
    // Remove Authorization header
    delete axios.defaults.headers.common['Authorization'];
    
    // Redirect to login page
    navigate('/login');
  };

  // Context value
  const contextValue = {
    isAuthenticated,
    user,
    token,
    login,
    logout: handleLogout,
    checkAuthStatus,
    loading,
  };

  return (
    <AuthContext.Provider value={contextValue}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
