import React from 'react';
import { Outlet } from 'react-router-dom';
import {
  AppBar,
  Box,
  CssBaseline,
  Divider,
  Drawer,
  IconButton,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Toolbar,
  Typography,
  useTheme,
  useMediaQuery,
} from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import DashboardIcon from '@mui/icons-material/Dashboard';
import ArticleIcon from '@mui/icons-material/Article';
import FolderIcon from '@mui/icons-material/Folder';
import SettingsIcon from '@mui/icons-material/Settings';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import BrightnessMediumIcon from '@mui/icons-material/BrightnessMedium';
import { useAuth } from '../../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import routes from '../../config/routes';

// Drawer width for desktop
const drawerWidth = 240;

const AppShell: React.FC = () => {
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('md'));
  const [mobileOpen, setMobileOpen] = React.useState(false);
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  
  // Handle drawer toggle
  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };
  
  // Navigate to a route and close mobile drawer
  const navigateTo = (route: string) => {
    navigate(route);
    if (isMobile) {
      setMobileOpen(false);
    }
  };
  
  // Navigation items
  const navigationItems = [
    {
      text: 'Content',
      icon: <ArticleIcon />,
      route: routes.content.list,
      requiredRole: '',  // empty string means available to all authenticated users
    },
    {
      text: 'Files',
      icon: <FolderIcon />,
      route: routes.files.list,
      requiredRole: '',
    },
    {
      text: 'Profile',
      icon: <AccountCircleIcon />,
      route: routes.user.profile,
      requiredRole: '',
    },
    {
      text: 'Settings',
      icon: <SettingsIcon />,
      route: routes.system.settings,
      requiredRole: 'admin',  // only admin can access
    },
  ];
  
  // Drawer content
  const drawer = (
    <Box>
      <Toolbar sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Typography variant="h6" noWrap>
          NetCtrl CMS
        </Typography>
        {isMobile && (
          <IconButton onClick={handleDrawerToggle}>
            <ChevronLeftIcon />
          </IconButton>
        )}
      </Toolbar>
      <Divider />
      <List>
        {navigationItems.map((item) => {
          // Skip items that require specific roles if user doesn't have that role
          if (item.requiredRole && !user?.role?.includes(item.requiredRole)) {
            return null;
          }
          
          return (
            <ListItem key={item.text} disablePadding>
              <ListItemButton onClick={() => navigateTo(item.route)}>
                <ListItemIcon>{item.icon}</ListItemIcon>
                <ListItemText primary={item.text} />
              </ListItemButton>
            </ListItem>
          );
        })}
      </List>
    </Box>
  );
  
  return (
    <Box sx={{ display: 'flex', minHeight: '100vh' }}>
      <CssBaseline />
      
      {/* App bar */}
      <AppBar
        position="fixed"
        sx={{
          width: { md: `calc(100% - ${drawerWidth}px)` },
          ml: { md: `${drawerWidth}px` },
        }}
      >
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            edge="start"
            onClick={handleDrawerToggle}
            sx={{ mr: 2, display: { md: 'none' } }}
          >
            <MenuIcon />
          </IconButton>
          
          <Typography variant="h6" noWrap component="div" sx={{ flexGrow: 1 }}>
            Content Management System
          </Typography>
          
          {/* User profile and theme toggle */}
          <Box sx={{ display: 'flex', alignItems: 'center' }}>
            <IconButton color="inherit" size="small" sx={{ ml: 1 }}>
              <BrightnessMediumIcon />
            </IconButton>
            
            <Box
              sx={{
                display: 'flex',
                alignItems: 'center',
                ml: 2,
                cursor: 'pointer',
              }}
              onClick={() => navigateTo(routes.user.profile)}
            >
              <AccountCircleIcon sx={{ mr: 1 }} />
              <Typography variant="body2" sx={{ display: { xs: 'none', sm: 'block' } }}>
                {user?.username || 'User'}
              </Typography>
            </Box>
          </Box>
        </Toolbar>
      </AppBar>
      
      {/* Drawer - different behavior for mobile and desktop */}
      <Box
        component="nav"
        sx={{ width: { md: drawerWidth }, flexShrink: { md: 0 } }}
      >
        {/* Mobile drawer - temporary */}
        {isMobile && (
          <Drawer
            variant="temporary"
            open={mobileOpen}
            onClose={handleDrawerToggle}
            ModalProps={{ keepMounted: true }}
            sx={{
              display: { xs: 'block', md: 'none' },
              '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
            }}
          >
            {drawer}
          </Drawer>
        )}
        
        {/* Desktop drawer - permanent */}
        <Drawer
          variant="permanent"
          sx={{
            display: { xs: 'none', md: 'block' },
            '& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
          }}
          open
        >
          {drawer}
        </Drawer>
      </Box>
      
      {/* Main content */}
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          p: 3,
          width: { md: `calc(100% - ${drawerWidth}px)` },
          backgroundColor: theme.palette.background.default,
          marginTop: '64px', // AppBar height
        }}
      >
        <Outlet />
      </Box>
    </Box>
  );
};

export default AppShell;
