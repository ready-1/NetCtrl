import React, { useEffect, useState } from 'react';
import { Link as RouterLink } from 'react-router-dom';
import {
  Avatar,
  Box,
  Breadcrumbs,
  Button,
  Container,
  Divider,
  Grid,
  Link,
  Paper,
  Tab,
  Tabs,
  TextField,
  Typography,
  useTheme,
} from '@mui/material';
import {
  AccountCircle as AccountCircleIcon,
  Edit as EditIcon,
  Save as SaveIcon,
  Visibility as VisibilityIcon,
  VisibilityOff as VisibilityOffIcon,
} from '@mui/icons-material';
import { useAuth } from '../../context/AuthContext';
import routes from '../../config/routes';

/**
 * ProfilePage component
 * 
 * User profile page with:
 * - User details (username, email, role)
 * - Password change form
 * - Recent activity
 */
const ProfilePage: React.FC = () => {
  const theme = useTheme();
  const { user } = useAuth();
  
  // Tab state
  const [currentTab, setCurrentTab] = useState(0);
  
  // Edit mode state
  const [isEditMode, setIsEditMode] = useState(false);
  
  // Form values
  const [formValues, setFormValues] = useState({
    username: '',
    email: '',
    currentPassword: '',
    newPassword: '',
    confirmPassword: '',
  });
  
  // Validation state
  const [errors, setErrors] = useState<Record<string, string>>({});
  
  // Password visibility
  const [showPassword, setShowPassword] = useState(false);
  
  // Recent activity mock data
  const [recentActivity, setRecentActivity] = useState([
    { id: 1, action: 'Edited content', item: 'Homepage Content', date: '2025-03-15 14:32' },
    { id: 2, action: 'Uploaded file', item: 'product-image.jpg', date: '2025-03-14 10:15' },
    { id: 3, action: 'Created content', item: 'About Us Page', date: '2025-03-12 09:45' },
    { id: 4, action: 'Login', item: '', date: '2025-03-12 09:30' },
  ]);
  
  // Load user data
  useEffect(() => {
    if (user) {
      setFormValues({
        ...formValues,
        username: user.username,
        email: user.email || '',
      });
    }
  }, [user]);
  
  // Handle tab change
  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setCurrentTab(newValue);
  };
  
  // Handle form field changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormValues(prev => ({ ...prev, [name]: value }));
    
    // Clear validation error when field is changed
    if (errors[name]) {
      setErrors(prev => ({ ...prev, [name]: '' }));
    }
  };
  
  // Toggle password visibility
  const handleTogglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };
  
  // Toggle edit mode
  const handleToggleEditMode = () => {
    setIsEditMode(!isEditMode);
    
    // Reset form values and errors when canceling edit
    if (isEditMode && user) {
      setFormValues({
        ...formValues,
        username: user.username,
        email: user.email || '',
        currentPassword: '',
        newPassword: '',
        confirmPassword: '',
      });
      setErrors({});
    }
  };
  
  // Validate profile form
  const validateProfileForm = () => {
    const newErrors: Record<string, string> = {};
    
    if (!formValues.username.trim()) {
      newErrors.username = 'Username is required';
    }
    
    if (formValues.email && !/\S+@\S+\.\S+/.test(formValues.email)) {
      newErrors.email = 'Invalid email address';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };
  
  // Validate password form
  const validatePasswordForm = () => {
    const newErrors: Record<string, string> = {};
    
    if (!formValues.currentPassword) {
      newErrors.currentPassword = 'Current password is required';
    }
    
    if (!formValues.newPassword) {
      newErrors.newPassword = 'New password is required';
    } else if (formValues.newPassword.length < 8) {
      newErrors.newPassword = 'Password must be at least 8 characters long';
    }
    
    if (formValues.newPassword !== formValues.confirmPassword) {
      newErrors.confirmPassword = 'Passwords do not match';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };
  
  // Handle profile form submission
  const handleProfileSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    
    if (!validateProfileForm()) {
      return;
    }
    
    // In a real app, submit to API
    console.log('Submitting profile update:', {
      username: formValues.username,
      email: formValues.email,
    });
    
    // Mock success
    alert('Profile updated successfully');
    setIsEditMode(false);
  };
  
  // Handle password form submission
  const handlePasswordSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    
    if (!validatePasswordForm()) {
      return;
    }
    
    // In a real app, submit to API
    console.log('Submitting password update');
    
    // Mock success
    alert('Password updated successfully');
    
    // Reset password fields
    setFormValues({
      ...formValues,
      currentPassword: '',
      newPassword: '',
      confirmPassword: '',
    });
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      {/* Breadcrumbs navigation */}
      <Breadcrumbs sx={{ mb: 2 }}>
        <Link component={RouterLink} to="/" color="inherit">
          Dashboard
        </Link>
        <Typography color="text.primary">My Profile</Typography>
      </Breadcrumbs>
      
      {/* Page header */}
      <Box sx={{ mb: 4, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Box sx={{ display: 'flex', alignItems: 'center' }}>
          <Avatar
            sx={{ 
              width: 64, 
              height: 64, 
              bgcolor: theme.palette.primary.main,
              mr: 2,
            }}
          >
            {user?.username ? user.username.charAt(0).toUpperCase() : 'U'}
          </Avatar>
          <Box>
            <Typography variant="h4" component="h1" gutterBottom>
              {user?.username || 'User Profile'}
            </Typography>
            <Typography variant="subtitle1" color="text.secondary">
              {user?.role.toUpperCase()} • Joined {user?.created_at ? new Date(user.created_at).toLocaleDateString() : 'Recently'}
            </Typography>
          </Box>
        </Box>
        
        {currentTab === 0 && (
          <Button
            variant={isEditMode ? 'outlined' : 'contained'}
            color={isEditMode ? 'inherit' : 'primary'}
            startIcon={isEditMode ? null : <EditIcon />}
            onClick={handleToggleEditMode}
          >
            {isEditMode ? 'Cancel' : 'Edit Profile'}
          </Button>
        )}
      </Box>
      
      {/* Profile tabs */}
      <Paper sx={{ mb: 4 }}>
        <Tabs value={currentTab} onChange={handleTabChange}>
          <Tab label="Profile" />
          <Tab label="Change Password" />
          <Tab label="Recent Activity" />
        </Tabs>
        
        <Divider />
        
        {/* Profile tab */}
        {currentTab === 0 && (
          <Box sx={{ p: 3 }}>
            <Box component="form" onSubmit={handleProfileSubmit}>
              <Grid container spacing={3}>
                <Grid item xs={12} md={6}>
                  <TextField
                    name="username"
                    label="Username"
                    fullWidth
                    value={formValues.username}
                    onChange={handleChange}
                    disabled={!isEditMode}
                    error={!!errors.username}
                    helperText={errors.username}
                    required
                  />
                </Grid>
                
                <Grid item xs={12} md={6}>
                  <TextField
                    name="email"
                    label="Email (Optional)"
                    fullWidth
                    value={formValues.email}
                    onChange={handleChange}
                    disabled={!isEditMode}
                    error={!!errors.email}
                    helperText={errors.email}
                  />
                </Grid>
                
                <Grid item xs={12} md={6}>
                  <TextField
                    label="Role"
                    fullWidth
                    value={user?.role || 'user'}
                    disabled
                  />
                </Grid>
                
                <Grid item xs={12} md={6}>
                  <TextField
                    label="Member Since"
                    fullWidth
                    value={user?.created_at ? new Date(user.created_at).toLocaleDateString() : 'Not available'}
                    disabled
                  />
                </Grid>
                
                {isEditMode && (
                  <Grid item xs={12}>
                    <Box sx={{ display: 'flex', justifyContent: 'flex-end', mt: 2 }}>
                      <Button
                        type="submit"
                        variant="contained"
                        color="primary"
                        startIcon={<SaveIcon />}
                      >
                        Save Changes
                      </Button>
                    </Box>
                  </Grid>
                )}
              </Grid>
            </Box>
          </Box>
        )}
        
        {/* Change password tab */}
        {currentTab === 1 && (
          <Box sx={{ p: 3 }}>
            <Box component="form" onSubmit={handlePasswordSubmit}>
              <Grid container spacing={3}>
                <Grid item xs={12}>
                  <TextField
                    name="currentPassword"
                    label="Current Password"
                    type={showPassword ? 'text' : 'password'}
                    fullWidth
                    value={formValues.currentPassword}
                    onChange={handleChange}
                    error={!!errors.currentPassword}
                    helperText={errors.currentPassword}
                    required
                    InputProps={{
                      endAdornment: (
                        <Box 
                          component="button" 
                          type="button" 
                          onClick={handleTogglePasswordVisibility} 
                          sx={{ 
                            background: 'none',
                            border: 'none',
                            cursor: 'pointer',
                            color: theme.palette.action.active,
                          }}
                        >
                          {showPassword ? <VisibilityOffIcon /> : <VisibilityIcon />}
                        </Box>
                      ),
                    }}
                  />
                </Grid>
                
                <Grid item xs={12}>
                  <TextField
                    name="newPassword"
                    label="New Password"
                    type={showPassword ? 'text' : 'password'}
                    fullWidth
                    value={formValues.newPassword}
                    onChange={handleChange}
                    error={!!errors.newPassword}
                    helperText={errors.newPassword || 'Password must be at least 8 characters long'}
                    required
                  />
                </Grid>
                
                <Grid item xs={12}>
                  <TextField
                    name="confirmPassword"
                    label="Confirm New Password"
                    type={showPassword ? 'text' : 'password'}
                    fullWidth
                    value={formValues.confirmPassword}
                    onChange={handleChange}
                    error={!!errors.confirmPassword}
                    helperText={errors.confirmPassword}
                    required
                  />
                </Grid>
                
                <Grid item xs={12}>
                  <Box sx={{ display: 'flex', justifyContent: 'flex-end', mt: 2 }}>
                    <Button
                      type="submit"
                      variant="contained"
                      color="primary"
                    >
                      Update Password
                    </Button>
                  </Box>
                </Grid>
              </Grid>
            </Box>
          </Box>
        )}
        
        {/* Recent activity tab */}
        {currentTab === 2 && (
          <Box sx={{ p: 3 }}>
            {recentActivity.length > 0 ? (
              <Box>
                {recentActivity.map((activity) => (
                  <Box key={activity.id} sx={{ mb: 2, pb: 2, borderBottom: 1, borderColor: 'divider' }}>
                    <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
                      <Typography variant="subtitle1">
                        {activity.action}
                        {activity.item && (
                          <Typography component="span" color="primary.main">
                            {' '}{activity.item}
                          </Typography>
                        )}
                      </Typography>
                      <Typography variant="body2" color="text.secondary">
                        {activity.date}
                      </Typography>
                    </Box>
                  </Box>
                ))}
              </Box>
            ) : (
              <Typography variant="body1" color="text.secondary">
                No recent activity found.
              </Typography>
            )}
          </Box>
        )}
      </Paper>
    </Container>
  );
};

export default ProfilePage;
