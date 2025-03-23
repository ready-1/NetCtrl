import React from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Box,
  Button,
  Container,
  Typography,
  Paper,
  Grid,
  Card,
  CardContent,
  CardHeader,
  CardActions,
  Divider,
} from '@mui/material';
import ArticleIcon from '@mui/icons-material/Article';
import FolderIcon from '@mui/icons-material/Folder';
import PeopleIcon from '@mui/icons-material/People';
import { useDocumentTitle } from '../hooks/useDocumentTitle';
import routes from '../config/routes';

const WelcomePage: React.FC = () => {
  const navigate = useNavigate();
  useDocumentTitle('Welcome to NetCtrl CMS');

  return (
    <Box
      sx={{
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        backgroundColor: 'background.default',
      }}
    >
      {/* Header */}
      <Box
        sx={{
          backgroundColor: 'primary.main',
          color: 'primary.contrastText',
          p: 4,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          textAlign: 'center',
        }}
      >
        <Typography variant="h2" component="h1" gutterBottom>
          NetCtrl CMS
        </Typography>
        <Typography variant="h5" component="h2" sx={{ mb: 4, maxWidth: '800px' }}>
          A comprehensive content management system with role-based access control
        </Typography>
        <Button
          variant="contained"
          color="secondary"
          size="large"
          onClick={() => navigate(routes.auth.login)}
          sx={{ px: 4, py: 1.5, fontSize: '1.1rem', fontWeight: 'bold' }}
        >
          Sign In
        </Button>
      </Box>

      {/* Features section */}
      <Container maxWidth="lg" sx={{ mt: 6, mb: 8 }}>
        <Typography variant="h4" component="h2" align="center" gutterBottom>
          Features
        </Typography>
        <Typography variant="subtitle1" align="center" color="text.secondary" sx={{ mb: 6 }}>
          A powerful content management system built for security and flexibility
        </Typography>

        <Grid container spacing={4} justifyContent="center">
          {/* Content Management */}
          <Grid item xs={12} sm={6} md={4}>
            <Card sx={{ height: '100%' }}>
              <CardHeader
                title="Content Management"
                titleTypographyProps={{ align: 'center' }}
                avatar={<ArticleIcon color="primary" fontSize="large" />}
                sx={{ pb: 0 }}
              />
              <CardContent>
                <Box sx={{ minHeight: '120px' }}>
                  <Typography variant="body1" align="center" sx={{ mb: 2 }}>
                    Create, edit and manage content with a modern rich text editor. Support for HTML, Markdown, and plain text formats.
                  </Typography>
                </Box>
              </CardContent>
            </Card>
          </Grid>

          {/* File Management */}
          <Grid item xs={12} sm={6} md={4}>
            <Card sx={{ height: '100%' }}>
              <CardHeader
                title="File Management"
                titleTypographyProps={{ align: 'center' }}
                avatar={<FolderIcon color="primary" fontSize="large" />}
                sx={{ pb: 0 }}
              />
              <CardContent>
                <Box sx={{ minHeight: '120px' }}>
                  <Typography variant="body1" align="center" sx={{ mb: 2 }}>
                    Upload, organize and manage files with ease. Support for file versioning, metadata, and content association.
                  </Typography>
                </Box>
              </CardContent>
            </Card>
          </Grid>

          {/* Role-Based Access Control */}
          <Grid item xs={12} sm={6} md={4}>
            <Card sx={{ height: '100%' }}>
              <CardHeader
                title="Access Control"
                titleTypographyProps={{ align: 'center' }}
                avatar={<PeopleIcon color="primary" fontSize="large" />}
                sx={{ pb: 0 }}
              />
              <CardContent>
                <Box sx={{ minHeight: '120px' }}>
                  <Typography variant="body1" align="center" sx={{ mb: 2 }}>
                    Secure your content with granular role-based access controls. Define exactly who can view, edit, and manage content.
                  </Typography>
                </Box>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </Container>

      {/* Call to action */}
      <Box sx={{ mt: 'auto', py: 4, backgroundColor: 'background.paper' }}>
        <Container maxWidth="md">
          <Paper elevation={0} sx={{ p: 4, textAlign: 'center' }}>
            <Typography variant="h5" component="h3" gutterBottom>
              Ready to get started?
            </Typography>
            <Typography variant="body1" sx={{ mb: 3 }}>
              Sign in to access the full features of NetCtrl CMS.
            </Typography>
            <Button
              variant="contained"
              color="primary"
              onClick={() => navigate(routes.auth.login)}
              sx={{ mr: 2 }}
            >
              Sign In
            </Button>
            <Button
              variant="outlined"
              color="primary"
              onClick={() => navigate(routes.auth.register)}
            >
              Register
            </Button>
          </Paper>
        </Container>
      </Box>

      {/* Footer */}
      <Box sx={{ py: 3, backgroundColor: 'background.default', borderTop: 1, borderColor: 'divider' }}>
        <Container maxWidth="lg">
          <Typography variant="body2" color="text.secondary" align="center">
            © {new Date().getFullYear()} NetCtrl CMS. All rights reserved.
          </Typography>
        </Container>
      </Box>
    </Box>
  );
};

export default WelcomePage;
