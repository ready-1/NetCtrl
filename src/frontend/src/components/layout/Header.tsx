import React from 'react';
import { Link as RouterLink } from 'react-router-dom';
import {
  AppBar,
  Avatar,
  Box,
  Button,
  IconButton,
  Menu,
  MenuItem,
  Toolbar,
  Tooltip,
  Typography,
  useMediaQuery,
  useTheme,
} from '@mui/material';
import {
  Menu as MenuIcon,
  Brightness4 as DarkModeIcon,
  Brightness7 as LightModeIcon,
  AccountCircle,
  Logout,
  Settings,
} from '@mui/icons-material';
import { useAuth } from '../../context/AuthContext';
import { useTheme as useAppTheme } from '../../context/ThemeContext';
import routes from '../../config/routes';

interface HeaderProps {
  onSidebarToggle: () => void;
}

/**
 * Header component
 * 
 * Top navigation bar that includes:
 * - Menu toggle button for sidebar
 * - Brand/logo
 * - User profile menu
 * - Dark mode toggle
 */
const Header: React.FC<HeaderProps> = ({ onSidebarToggle }) => {
  const theme = useTheme();
  const { mode, toggleColorMode } = useAppTheme();
  const { user, logout } = useAuth();
  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));
  
  // Profile menu state
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl);
  
  // Profile menu handlers
  const handleMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };
  
  const handleClose = () => {
    setAnchorEl(null);
  };

  // Handle logout
  const handleLogout = () => {
    handleClose();
    logout();
  };

  return (
    <AppBar 
      position="fixed" 
      sx={{ 
        zIndex: theme.zIndex.drawer + 1,
        boxShadow: 1,
      }}
    >
      <Toolbar>
        {/* Menu toggle button */}
        <IconButton
          color="inherit"
          aria-label="open drawer"
          edge="start"
          onClick={onSidebarToggle}
          sx={{ mr: 2 }}
        >
          <MenuIcon />
        </IconButton>
        
        {/* Brand logo and title */}
        <Typography
          variant="h6"
          component={RouterLink}
          to="/"
          sx={{
            flexGrow: 1,
            color: 'inherit',
            textDecoration: 'none',
            fontWeight: 'bold',
            letterSpacing: '0.5px',
          }}
        >
          NetCtrl CMS
        </Typography>
        
        {/* Dark mode toggle */}
        <Tooltip title={mode === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'}>
          <IconButton
            color="inherit"
            onClick={toggleColorMode}
            sx={{ marginRight: 1 }}
          >
            {mode === 'dark' ? <LightModeIcon /> : <DarkModeIcon />}
          </IconButton>
        </Tooltip>
        
        {/* User profile section */}
        <Box>
          <Tooltip title="Account settings">
            <IconButton
              onClick={handleMenu}
              color="inherit"
              size="large"
              aria-controls={open ? 'account-menu' : undefined}
              aria-haspopup="true"
              aria-expanded={open ? 'true' : undefined}
            >
              {user?.username ? (
                <Avatar
                  sx={{
                    width: 32,
                    height: 32,
                    bgcolor: theme.palette.secondary.main,
                  }}
                >
                  {user.username.charAt(0).toUpperCase()}
                </Avatar>
              ) : (
                <AccountCircle />
              )}
            </IconButton>
          </Tooltip>
          
          {/* Profile dropdown menu */}
          <Menu
            id="account-menu"
            anchorEl={anchorEl}
            open={open}
            onClose={handleClose}
            transformOrigin={{ horizontal: 'right', vertical: 'top' }}
            anchorOrigin={{ horizontal: 'right', vertical: 'bottom' }}
          >
            {user ? (
              <>
                <MenuItem 
                  component={RouterLink} 
                  to={routes.user.profile}
                  onClick={handleClose}
                >
                  <AccountCircle sx={{ mr: 1 }} />
                  Profile
                </MenuItem>
                <MenuItem 
                  component={RouterLink}
                  to={routes.system.settings}
                  onClick={handleClose}
                >
                  <Settings sx={{ mr: 1 }} />
                  Settings
                </MenuItem>
                <MenuItem onClick={handleLogout}>
                  <Logout sx={{ mr: 1 }} />
                  Logout
                </MenuItem>
              </>
            ) : (
              <MenuItem 
                component={RouterLink} 
                to={routes.auth.login}
                onClick={handleClose}
              >
                Login
              </MenuItem>
            )}
          </Menu>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
