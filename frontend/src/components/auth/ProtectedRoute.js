import React, { useContext } from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import AuthContext from '../../store/AuthContext';
import { Spinner } from 'react-bootstrap';

/**
 * Protected Route Component
 * 
 * Ensures that routes wrapped by this component are only accessible
 * to authenticated users. Unauthenticated users are redirected to login.
 */
const ProtectedRoute = ({ children, requiredRoles = [] }) => {
  const { isAuthenticated, user, loading } = useContext(AuthContext);
  const location = useLocation();

  // Show loading while authentication status is being determined
  if (loading) {
    return (
      <div className="d-flex justify-content-center align-items-center" style={{ height: '100vh' }}>
        <Spinner animation="border" role="status">
          <span className="visually-hidden">Loading...</span>
        </Spinner>
      </div>
    );
  }

  // Redirect to login if user is not authenticated
  if (!isAuthenticated) {
    // Save the attempted URL for redirection after login
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  // Check for required roles if specified
  if (requiredRoles.length > 0) {
    const hasRequiredRole = requiredRoles.some(role => 
      user.roles.includes(role)
    );
    
    if (!hasRequiredRole) {
      // User doesn't have required role, redirect to dashboard
      return <Navigate to="/" replace />;
    }
  }

  // User is authenticated (and has required roles if specified)
  return children;
};

export default ProtectedRoute;
