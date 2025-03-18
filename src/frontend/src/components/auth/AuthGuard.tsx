import React, { ReactNode } from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import routes from '../../config/routes';
import { CircularProgress } from '@mui/material';

interface AuthGuardProps {
  children: ReactNode;
  requiredPermission?: string;
  requiredRole?: string;
}

/**
 * AuthGuard component
 * 
 * Protects routes from unauthorized access by checking:
 * 1. If the user is authenticated
 * 2. If the auth context is initialized
 * 3. If the user has the required permission/role (if specified)
 * 
 * If any check fails, redirects to login page
 */
const AuthGuard: React.FC<AuthGuardProps> = ({
  children,
  requiredPermission,
  requiredRole,
}) => {
  const { isAuthenticated, isInitialized, hasPermission, hasRole } = useAuth();
  const location = useLocation();

  // Show loading while authentication is being checked
  if (!isInitialized) {
    return (
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
        <CircularProgress />
      </div>
    );
  }

  // Redirect to login if not authenticated
  if (!isAuthenticated) {
    return <Navigate to={routes.auth.login} state={{ from: location }} replace />;
  }

  // Check for required permission
  if (requiredPermission && !hasPermission(requiredPermission)) {
    // Redirect to unauthorized page or dashboard
    return <Navigate to="/" replace />;
  }

  // Check for required role
  if (requiredRole && !hasRole(requiredRole)) {
    // Redirect to unauthorized page or dashboard
    return <Navigate to="/" replace />;
  }

  // If all checks pass, render the protected content
  return <>{children}</>;
};

export default AuthGuard;
