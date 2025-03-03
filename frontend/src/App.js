import React, { useState, useEffect } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { Container } from 'react-bootstrap';
import { AuthProvider } from './store/AuthContext';
import ProtectedRoute from './components/auth/ProtectedRoute';
import Layout from './components/layout/Layout';
import Login from './pages/auth/Login';
import Dashboard from './pages/dashboard/Dashboard';
import Switches from './pages/switches/Switches';
import SwitchDetail from './pages/switches/SwitchDetail';
import ContentList from './pages/cms/ContentList';
import ContentDetail from './pages/cms/ContentDetail';
import ContentEdit from './pages/cms/ContentEdit';
import UserManagement from './pages/admin/UserManagement';
import Settings from './pages/settings/Settings';
import NotFound from './pages/NotFound';

function App() {
  // State to handle dark mode
  const [darkMode, setDarkMode] = useState(() => {
    const savedMode = localStorage.getItem('darkMode');
    return savedMode ? JSON.parse(savedMode) : false;
  });

  // Apply dark mode to the document
  useEffect(() => {
    document.documentElement.setAttribute('data-bs-theme', darkMode ? 'dark' : 'light');
    localStorage.setItem('darkMode', JSON.stringify(darkMode));
  }, [darkMode]);

  // Toggle dark mode handler
  const toggleDarkMode = () => {
    setDarkMode(prevMode => !prevMode);
  };

  return (
    <AuthProvider>
      <Routes>
        {/* Public routes */}
        <Route path="/login" element={<Login />} />
        
        {/* Protected routes - all require authentication */}
        <Route path="/" element={
          <ProtectedRoute>
            <Layout darkMode={darkMode} toggleDarkMode={toggleDarkMode} />
          </ProtectedRoute>
        }>
          <Route index element={<Dashboard />} />
          <Route path="switches" element={<Switches />} />
          <Route path="switches/:id" element={<SwitchDetail />} />
          <Route path="content" element={<ContentList />} />
          <Route path="content/new" element={<ContentEdit />} />
          <Route path="content/:id" element={<ContentDetail />} />
          <Route path="content/:id/edit" element={<ContentEdit />} />
          <Route path="admin/users" element={<UserManagement />} />
          <Route path="settings" element={<Settings />} />
        </Route>
        
        {/* Redirect root to dashboard */}
        <Route path="/" element={<Navigate to="/dashboard" replace />} />
        
        {/* 404 route */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </AuthProvider>
  );
}

export default App;
