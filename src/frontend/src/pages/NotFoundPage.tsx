import React from 'react';
import { Link as RouterLink } from 'react-router-dom';
import {
  Box,
  Button,
  Container,
  Typography,
  useTheme,
} from '@mui/material';
import { Error as ErrorIcon } from '@mui/icons-material';

/**
 * NotFoundPage component
 * 
 * Displays a 404 error page when a user navigates to a non-existent route.
 * Provides a link to return to the home page.
 */
const NotFoundPage: React.FC = () => {
  const theme = useTheme();

  return (
    <Container maxWidth="md">
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          height: '100vh',
          textAlign: 'center',
        }}
      >
        <ErrorIcon
          sx={{
            fontSize: 100,
            color: theme.palette.error.main,
            mb: 2,
          }}
        />
        
        <Typography variant="h1" component="h1" gutterBottom>
          404
        </Typography>
        
        <Typography variant="h4" component="h2" gutterBottom>
          Page Not Found
        </Typography>
        
        <Typography variant="body1" color="text.secondary" paragraph>
          The page you are looking for doesn't exist or has been moved.
        </Typography>
        
        <Button
          variant="contained"
          color="primary"
          component={RouterLink}
          to="/"
          sx={{ mt: 2 }}
        >
          Return to Dashboard
        </Button>
      </Box>
    </Container>
  );
};

export default NotFoundPage;
