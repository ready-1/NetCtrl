import React, { useState } from 'react';
import { Outlet } from 'react-router-dom';
import { 
  Box, 
  CssBaseline, 
  useMediaQuery, 
  useTheme 
} from '@mui/material';
import Header from './Header';
import Sidebar from './Sidebar';
import Footer from './Footer';

/**
 * AppShell component
 * 
 * Main layout wrapper for the application that includes:
 * - Header with navigation
 * - Sidebar for main menu
 * - Content area (via Outlet)
 * - Footer
 * 
 * Handles responsive behavior for mobile/desktop layouts
 */
const AppShell: React.FC = () => {
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('md'));
  
  // Sidebar state
  const [sidebarOpen, setSidebarOpen] = useState(!isMobile);
  
  // Toggle sidebar
  const handleSidebarToggle = () => {
    setSidebarOpen(!sidebarOpen);
  };
  
  // Close sidebar on mobile when clicking outside
  const handleContentClick = () => {
    if (isMobile && sidebarOpen) {
      setSidebarOpen(false);
    }
  };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      <CssBaseline />
      
      {/* Header */}
      <Header onSidebarToggle={handleSidebarToggle} />
      
      {/* Main content area */}
      <Box sx={{ display: 'flex', flex: 1 }}>
        {/* Sidebar */}
        <Sidebar 
          open={sidebarOpen} 
          onClose={() => setSidebarOpen(false)}
          variant={isMobile ? 'temporary' : 'persistent'}
        />
        
        {/* Page content */}
        <Box 
          component="main" 
          sx={{
            flexGrow: 1,
            p: 3,
            width: { md: `calc(100% - ${sidebarOpen ? 240 : 0}px)` },
            ml: { md: sidebarOpen ? '240px' : 0 },
            transition: theme.transitions.create('margin', {
              easing: theme.transitions.easing.sharp,
              duration: theme.transitions.duration.leavingScreen,
            }),
          }}
          onClick={handleContentClick}
        >
          {/* Toolbar spacer */}
          <Box component="div" sx={{ height: 64 }} />
          
          {/* Router outlet for page content */}
          <Outlet />
        </Box>
      </Box>
      
      {/* Footer */}
      <Footer />
    </Box>
  );
};

export default AppShell;
