import React, { ReactNode } from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { CircularProgress } from '@mui/material';

interface GuestGuardProps {
  children: ReactNode;
}

/**
 * GuestGuard component
 * 
 * Prevents authenticated users from accessing guest-only routes
 * (e.g., login, register pages).
 * 
 * If authenticated, redirects to the dashboard or previous location.
 */
const GuestGuard: React.FC<GuestGuardProps> = ({ children }) => {
  const { isAuthenticated, isInitialized } = useAuth();
  const location = useLocation();
  
  // Get redirect path from location state or default to dashboard
  const from = (location.state as any)?.from?.pathname || '/';

  // Show loading while authentication is being checked
  if (!isInitialized) {
    return (
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
        <CircularProgress />
      </div>
    );
  }

  // If user is authenticated, redirect to dashboard or previous location
  if (isAuthenticated) {
    return <Navigate to={from} replace />;
  }

  // If not authenticated, show the guest page (login/register)
  return <>{children}</>;
};

export default GuestGuard;
