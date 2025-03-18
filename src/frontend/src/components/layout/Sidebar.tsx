import React from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import {
  Box,
  Drawer,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Divider,
  useTheme,
} from '@mui/material';
import {
  Dashboard as DashboardIcon,
  Article as ContentIcon,
  InsertDriveFile as FileIcon,
  Group as UsersIcon,
  Settings as SettingsIcon,
} from '@mui/icons-material';
import { useAuth } from '../../context/AuthContext';
import routes from '../../config/routes';

// Sidebar width
const DRAWER_WIDTH = 240;

interface SidebarProps {
  open: boolean;
  onClose: () => void;
  variant: 'permanent' | 'persistent' | 'temporary';
}

/**
 * Sidebar navigation component
 * 
 * Displays the main application navigation links:
 * - Dashboard
 * - Content management
 * - File management
 * - User management (admin only)
 * - Settings
 * 
 * Adapts to mobile/desktop layouts
 */
const Sidebar: React.FC<SidebarProps> = ({ open, onClose, variant }) => {
  const theme = useTheme();
  const location = useLocation();
  const { hasRole } = useAuth();
  const isAdmin = hasRole('admin');
  
  // Navigation items
  const navItems = [
    {
      text: 'Dashboard',
      icon: <DashboardIcon />,
      path: '/',
      roles: ['admin', 'editor', 'user'],
    },
    {
      text: 'Content',
      icon: <ContentIcon />,
      path: routes.content.list,
      roles: ['admin', 'editor', 'user'],
    },
    {
      text: 'Files',
      icon: <FileIcon />,
      path: routes.files.list,
      roles: ['admin', 'editor', 'user'],
    },
    {
      text: 'Users',
      icon: <UsersIcon />,
      path: '/users',
      roles: ['admin'],
    },
    {
      text: 'Settings',
      icon: <SettingsIcon />,
      path: routes.system.settings,
      roles: ['admin', 'editor', 'user'],
    },
  ];

  // Filter items by user role
  const filteredNavItems = navItems.filter(item => 
    item.roles.includes('user') || (isAdmin && item.roles.includes('admin'))
  );

  // Drawer content
  const drawerContent = (
    <div>
      {/* Logo/branding area */}
      <Box
        sx={{
          height: 64,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          borderBottom: `1px solid ${theme.palette.divider}`,
        }}
      >
        <Box
          component="img"
          sx={{ height: 40 }}
          alt="NetCtrl Logo"
          src="/logo192.png"
          onError={(e: React.SyntheticEvent<HTMLImageElement>) => {
            e.currentTarget.src = ''; // Fallback if image doesn't exist
          }}
        />
      </Box>
      <Divider />
      
      {/* Navigation list */}
      <List>
        {filteredNavItems.map((item) => (
          <ListItem key={item.text} disablePadding>
            <ListItemButton
              component={NavLink}
              to={item.path}
              selected={location.pathname === item.path}
              onClick={variant === 'temporary' ? onClose : undefined}
              sx={{
                '&.active': {
                  backgroundColor: theme.palette.action.selected,
                },
              }}
            >
              <ListItemIcon>{item.icon}</ListItemIcon>
              <ListItemText primary={item.text} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </div>
  );

  // Choose drawer variant based on props
  return variant === 'temporary' ? (
    <Drawer
      variant="temporary"
      open={open}
      onClose={onClose}
      ModalProps={{ keepMounted: true }}
      sx={{
        display: { xs: 'block', md: 'none' },
        '& .MuiDrawer-paper': {
          boxSizing: 'border-box',
          width: DRAWER_WIDTH,
        },
      }}
    >
      {drawerContent}
    </Drawer>
  ) : (
    <Drawer
      variant="persistent"
      open={open}
      sx={{
        display: { xs: 'none', md: 'block' },
        width: DRAWER_WIDTH,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: DRAWER_WIDTH,
          boxSizing: 'border-box',
        },
      }}
    >
      {drawerContent}
    </Drawer>
  );
};

export default Sidebar;
