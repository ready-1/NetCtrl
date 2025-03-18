import React from 'react';
import { Link as RouterLink } from 'react-router-dom';
import {
  Box,
  Container,
  Divider,
  Grid,
  Link,
  Stack,
  Typography,
  useTheme,
} from '@mui/material';

/**
 * Footer component
 * 
 * Application footer with:
 * - Documentation links
 * - Information links
 * - Copyright information
 * - Version info
 */
const Footer: React.FC = () => {
  const theme = useTheme();
  const currentYear = new Date().getFullYear();
  
  // Footer links
  const footerLinks = [
    {
      title: 'Documentation',
      links: [
        { name: 'API Documentation', href: '/api-docs' },
        { name: 'User Guide', href: '/user-guide' },
      ],
    },
    {
      title: 'Resources',
      links: [
        { name: 'Help Center', href: '/help' },
        { name: 'Support', href: '/support' },
      ],
    },
    {
      title: 'Legal',
      links: [
        { name: 'Privacy Policy', href: '/privacy' },
        { name: 'Terms of Use', href: '/terms' },
      ],
    },
  ];

  return (
    <Box
      component="footer"
      sx={{
        py: 3,
        px: 2,
        mt: 'auto',
        backgroundColor: theme.palette.mode === 'light' 
          ? theme.palette.grey[100] 
          : theme.palette.grey[900],
      }}
    >
      <Container maxWidth="lg">
        <Grid container spacing={4} justifyContent="space-between">
          {footerLinks.map((section) => (
            <Grid item xs={12} sm={4} key={section.title}>
              <Typography variant="h6" color="text.primary" gutterBottom>
                {section.title}
              </Typography>
              <Stack spacing={1}>
                {section.links.map((link) => (
                  <Link
                    key={link.name}
                    component={RouterLink}
                    to={link.href}
                    color="text.secondary"
                    underline="hover"
                  >
                    {link.name}
                  </Link>
                ))}
              </Stack>
            </Grid>
          ))}
        </Grid>
        
        <Divider sx={{ mt: 3, mb: 2 }} />
        
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <Typography variant="body2" color="text.secondary">
            &copy; {currentYear} NetCtrl CMS. All rights reserved.
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Version 1.0.0
          </Typography>
        </Box>
      </Container>
    </Box>
  );
};

export default Footer;
