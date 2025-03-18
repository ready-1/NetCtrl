import React, { useState } from 'react';
import { Link as RouterLink, useNavigate, useLocation } from 'react-router-dom';
import {
  Avatar,
  Box,
  Button,
  Checkbox,
  Container,
  FormControlLabel,
  Grid,
  Link,
  Paper,
  TextField,
  Typography,
  Alert,
  useTheme,
} from '@mui/material';
import { LockOutlined as LockOutlinedIcon } from '@mui/icons-material';
import { useAuth } from '../../context/AuthContext';
import routes from '../../config/routes';

/**
 * Login Page component
 * 
 * Displays a form for user authentication with:
 * - Username input
 * - Password input
 * - Remember me checkbox
 * - Login button
 * - Link to registration page
 */
const LoginPage: React.FC = () => {
  const theme = useTheme();
  const navigate = useNavigate();
  const location = useLocation();
  const { login } = useAuth();
  
  // Form state
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);
  
  // Error handling
  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  
  // Get redirect path from location state or default to dashboard
  const from = (location.state as any)?.from?.pathname || '/';

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    
    // Validate form
    if (!username.trim() || !password) {
      setError('Please enter both username and password');
      return;
    }
    
    setError(null);
    setIsSubmitting(true);
    
    try {
      // Attempt login
      await login(username, password);
      
      // Store remember me preference if selected
      if (rememberMe) {
        localStorage.setItem('remember-user', username);
      } else {
        localStorage.removeItem('remember-user');
      }
      
      // Redirect to previous location or dashboard
      navigate(from, { replace: true });
    } catch (err: any) {
      // Handle login error
      setError(err.message || 'Invalid username or password');
      setIsSubmitting(false);
    }
  };

  // Load remembered username if available
  React.useEffect(() => {
    const rememberedUser = localStorage.getItem('remember-user');
    if (rememberedUser) {
      setUsername(rememberedUser);
      setRememberMe(true);
    }
  }, []);

  return (
    <Container component="main" maxWidth="xs">
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        {/* Logo/Avatar */}
        <Avatar sx={{ m: 1, bgcolor: theme.palette.secondary.main }}>
          <LockOutlinedIcon />
        </Avatar>
        
        {/* Page title */}
        <Typography component="h1" variant="h5">
          Sign in to NetCtrl CMS
        </Typography>
        
        {/* Error alert */}
        {error && (
          <Alert severity="error" sx={{ mt: 2, width: '100%' }}>
            {error}
          </Alert>
        )}
        
        {/* Login form */}
        <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
          {/* Username field */}
          <TextField
            margin="normal"
            required
            fullWidth
            id="username"
            label="Username"
            name="username"
            autoComplete="username"
            autoFocus
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            disabled={isSubmitting}
          />
          
          {/* Password field */}
          <TextField
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            disabled={isSubmitting}
          />
          
          {/* Remember me checkbox */}
          <FormControlLabel
            control={
              <Checkbox 
                value="remember" 
                color="primary" 
                checked={rememberMe}
                onChange={(e) => setRememberMe(e.target.checked)}
                disabled={isSubmitting}
              />
            }
            label="Remember me"
          />
          
          {/* Submit button */}
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
            disabled={isSubmitting}
          >
            Sign In
          </Button>
          
          {/* Links */}
          <Grid container>
            <Grid item xs>
              <Link component={RouterLink} to={routes.auth.resetPassword} variant="body2">
                Forgot password?
              </Link>
            </Grid>
            <Grid item>
              <Link component={RouterLink} to={routes.auth.register} variant="body2">
                {"Don't have an account? Sign Up"}
              </Link>
            </Grid>
          </Grid>
        </Box>
      </Box>
    </Container>
  );
};

export default LoginPage;
