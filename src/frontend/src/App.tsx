import React, { Suspense } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { CircularProgress } from '@mui/material';

// Layouts
import AppShell from './components/layout/AppShell';

// Routes configuration
import routes from './config/routes';

// Auth guards
import AuthGuard from './components/auth/AuthGuard';
import GuestGuard from './components/auth/GuestGuard';

// Lazy-loaded components
const LoginPage = React.lazy(() => import('./pages/auth/LoginPage'));
const RegisterPage = React.lazy(() => import('./pages/auth/RegisterPage'));
const ContentListPage = React.lazy(() => import('./pages/content/ContentListPage'));
const ContentDetailPage = React.lazy(() => import('./pages/content/ContentDetailPage'));
const ContentEditPage = React.lazy(() => import('./pages/content/ContentEditPage'));
const FileListPage = React.lazy(() => import('./pages/file/FileListPage'));
const FileDetailPage = React.lazy(() => import('./pages/file/FileDetailPage'));
const ProfilePage = React.lazy(() => import('./pages/user/ProfilePage'));
const NotFoundPage = React.lazy(() => import('./pages/NotFoundPage'));

// Loading component for suspense fallback
const Loader = () => (
  <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
    <CircularProgress />
  </div>
);

const App: React.FC = () => {
  return (
    <Suspense fallback={<Loader />}>
      <Routes>
        {/* Auth routes */}
        <Route
          path={routes.auth.login}
          element={
            <GuestGuard>
              <LoginPage />
            </GuestGuard>
          }
        />
        <Route
          path={routes.auth.register}
          element={
            <GuestGuard>
              <RegisterPage />
            </GuestGuard>
          }
        />

        {/* Protected routes */}
        <Route
          path="/"
          element={
            <AuthGuard>
              <AppShell />
            </AuthGuard>
          }
        >
          {/* Redirect root to content list */}
          <Route path="/" element={<Navigate to={routes.content.list} replace />} />

          {/* Content routes */}
          <Route path={routes.content.list} element={<ContentListPage />} />
          <Route path={routes.content.create} element={<ContentEditPage />} />
          <Route path={routes.content.detail(':id')} element={<ContentDetailPage />} />
          <Route path={routes.content.edit(':id')} element={<ContentEditPage />} />

          {/* File routes */}
          <Route path={routes.files.list} element={<FileListPage />} />
          <Route path={routes.files.detail(':id')} element={<FileDetailPage />} />

          {/* User routes */}
          <Route path={routes.user.profile} element={<ProfilePage />} />
        </Route>

        {/* 404 - Not Found */}
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </Suspense>
  );
};

export default App;
