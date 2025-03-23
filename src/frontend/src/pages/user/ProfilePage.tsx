import React from 'react';
import {
  Box,
  Card,
  CardContent,
  Container,
  Divider,
  Grid,
  Paper,
  Typography,
  Chip,
  Button,
} from '@mui/material';
import { useAuth } from '../../context/AuthContext';
import { useDocumentTitle } from '../../hooks/useDocumentTitle';

const ProfilePage: React.FC = () => {
  const { user, logout } = useAuth();
  useDocumentTitle('User Profile');
  
  // Format date
  const formatDate = (dateString?: string | null) => {
    if (!dateString) return 'N/A';
    
    return new Date(dateString).toLocaleString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    });
  };
  
  // Role colors
  const getRoleColor = (role?: string) => {
    if (!role) return 'default';
    
    switch (role) {
      case 'admin':
        return 'error';
      case 'manager':
        return 'success';
      case 'user':
        return 'primary';
      default:
        return 'default';
    }
  };
  
  // Handle logout
  const handleLogout = () => {
    logout();
  };
  
  // If user is not loaded, show a message
  if (!user) {
    return (
      <Container maxWidth="md">
        <Paper sx={{ p: 3, mt: 3 }}>
          <Typography variant="h5" align="center">
            User profile not available
          </Typography>
        </Paper>
      </Container>
    );
  }
  
  return (
    <Container maxWidth="md">
      <Paper sx={{ p: 3, mb: 4 }}>
        <Box display="flex" alignItems="center" mb={2}>
          <Box flexGrow={1}>
            <Typography variant="h4" component="h1" gutterBottom>
              User Profile
            </Typography>
          </Box>
          <Button
            variant="outlined"
            color="primary"
            onClick={handleLogout}
          >
            Sign Out
          </Button>
        </Box>
        
        <Divider sx={{ mb: 3 }} />
        
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <Card variant="outlined">
              <CardContent>
                <Grid container spacing={2}>
                  <Grid item xs={12} sm={3}>
                    <Typography variant="subtitle2" color="text.secondary">
                      Username
                    </Typography>
                    <Typography variant="body1">{user.username}</Typography>
                  </Grid>
                  
                  <Grid item xs={12} sm={3}>
                    <Typography variant="subtitle2" color="text.secondary">
                      Email
                    </Typography>
                    <Typography variant="body1">{user.email || 'Not provided'}</Typography>
                  </Grid>
                  
                  <Grid item xs={12} sm={3}>
                    <Typography variant="subtitle2" color="text.secondary">
                      Role
                    </Typography>
                    <Box mt={0.5}>
                      <Chip 
                        label={user.role || 'Unknown'} 
                        size="small" 
                        color={getRoleColor(user.role) as any}
                      />
                    </Box>
                  </Grid>
                  
                  <Grid item xs={12} sm={3}>
                    <Typography variant="subtitle2" color="text.secondary">
                      Status
                    </Typography>
                    <Box mt={0.5}>
                      <Chip 
                        label={user.is_active ? 'Active' : 'Inactive'} 
                        size="small"
                        color={user.is_active ? 'success' : 'default'}
                      />
                    </Box>
                  </Grid>
                </Grid>
              </CardContent>
            </Card>
          </Grid>
          
          <Grid item xs={12}>
            <Card variant="outlined">
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  Account Details
                </Typography>
                
                <Grid container spacing={2}>
                  <Grid item xs={12} sm={4}>
                    <Typography variant="subtitle2" color="text.secondary">
                      First Name
                    </Typography>
                    <Typography variant="body1">{user.first_name || 'Not set'}</Typography>
                  </Grid>
                  
                  <Grid item xs={12} sm={4}>
                    <Typography variant="subtitle2" color="text.secondary">
                      Last Name
                    </Typography>
                    <Typography variant="body1">{user.last_name || 'Not set'}</Typography>
                  </Grid>
                  
                  <Grid item xs={12} sm={4}>
                    <Typography variant="subtitle2" color="text.secondary">
                      Last Login
                    </Typography>
                    <Typography variant="body1">{formatDate(user.last_login)}</Typography>
                  </Grid>
                  
                  <Grid item xs={12} sm={4}>
                    <Typography variant="subtitle2" color="text.secondary">
                      Account Created
                    </Typography>
                    <Typography variant="body1">{formatDate(user.created_at)}</Typography>
                  </Grid>
                  
                  <Grid item xs={12} sm={4}>
                    <Typography variant="subtitle2" color="text.secondary">
                      Account Updated
                    </Typography>
                    <Typography variant="body1">{formatDate(user.updated_at)}</Typography>
                  </Grid>
                  
                  <Grid item xs={12} sm={4}>
                    <Typography variant="subtitle2" color="text.secondary">
                      Email Verified
                    </Typography>
                    <Typography variant="body1">{user.is_verified ? 'Yes' : 'No'}</Typography>
                  </Grid>
                </Grid>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </Paper>
    </Container>
  );
};

export default ProfilePage;
