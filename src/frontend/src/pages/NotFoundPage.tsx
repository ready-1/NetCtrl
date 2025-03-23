import React from 'react';
import { Box, Button, Container, Typography, Paper } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { useDocumentTitle } from '../hooks/useDocumentTitle';
import routes from '../config/routes';

const NotFoundPage: React.FC = () => {
  const navigate = useNavigate();
  useDocumentTitle('Page Not Found');
  
  return (
    <Container maxWidth="md">
      <Paper sx={{ p: 4, mt: 8, textAlign: 'center' }}>
        <Typography variant="h1" component="h1" gutterBottom>
          404
        </Typography>
        
        <Typography variant="h5" component="h2" gutterBottom>
          Page Not Found
        </Typography>
        
        <Typography variant="body1" color="text.secondary" paragraph>
          The page you're looking for doesn't exist or has been moved.
        </Typography>
        
        <Box mt={4}>
          <Button 
            variant="contained" 
            color="primary" 
            onClick={() => navigate(routes.content.list)}
          >
            Go to Content Dashboard
          </Button>
        </Box>
      </Paper>
    </Container>
  );
};

export default NotFoundPage;
