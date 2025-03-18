import React, { useEffect, useState } from 'react';
import { useParams, useNavigate, Link as RouterLink } from 'react-router-dom';
import {
  Box,
  Breadcrumbs,
  Button,
  Container,
  Divider,
  FormControl,
  FormControlLabel,
  FormHelperText,
  Grid,
  InputLabel,
  Link,
  MenuItem,
  Paper,
  Select,
  Switch,
  TextField,
  Typography,
  useTheme,
} from '@mui/material';
import {
  ArrowBack as ArrowBackIcon,
  Save as SaveIcon,
  Delete as DeleteIcon,
} from '@mui/icons-material';
import { useAuth } from '../../context/AuthContext';
import routes from '../../config/routes';

/**
 * ContentEditPage component
 * 
 * Form for creating or editing content with:
 * - Content metadata (title, type, status, etc.)
 * - Rich text editor for content body
 * - File attachments
 * - Save/Cancel actions
 */
const ContentEditPage: React.FC = () => {
  const theme = useTheme();
  const navigate = useNavigate();
  const { contentId } = useParams<{ contentId: string }>();
  const isNewContent = !contentId;
  
  // Form state
  const [formValues, setFormValues] = useState({
    title: '',
    type: 'page',
    status: 'draft',
    body: '',
    isPublished: false,
  });
  
  // Validation state
  const [errors, setErrors] = useState<Record<string, string>>({});
  
  // Load content data for editing
  useEffect(() => {
    if (isNewContent) return;
    
    // In a real app, fetch content from API
    // For demo, using mock data
    setFormValues({
      title: 'Sample Content Item',
      type: 'page',
      status: 'published',
      body: 'This is a sample content item for demonstration purposes.',
      isPublished: true,
    });
  }, [contentId, isNewContent]);
  
  // Handle form field changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormValues(prev => ({ ...prev, [name]: value }));
    
    // Clear validation error when field is changed
    if (errors[name]) {
      setErrors(prev => ({ ...prev, [name]: '' }));
    }
  };
  
  // Handle select field changes
  const handleSelectChange = (e: React.ChangeEvent<{ name?: string; value: unknown }>) => {
    const name = e.target.name as string;
    const value = e.target.value as string;
    setFormValues(prev => ({ ...prev, [name]: value }));
  };
  
  // Handle switch changes
  const handleSwitchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, checked } = e.target;
    setFormValues(prev => ({ ...prev, [name]: checked }));
  };
  
  // Validate form
  const validateForm = () => {
    const newErrors: Record<string, string> = {};
    
    if (!formValues.title.trim()) {
      newErrors.title = 'Title is required';
    }
    
    if (!formValues.body.trim()) {
      newErrors.body = 'Content is required';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };
  
  // Handle form submission
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }
    
    // In a real app, save data via API
    // For demo, just redirect
    const successMessage = isNewContent ? 'Content created successfully' : 'Content updated successfully';
    
    console.log('Form data submitted:', formValues);
    alert(successMessage);
    
    navigate(routes.content.list);
  };
  
  // Handle cancel
  const handleCancel = () => {
    if (isNewContent) {
      navigate(routes.content.list);
    } else {
      navigate(routes.content.detail(contentId!));
    }
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      {/* Breadcrumbs navigation */}
      <Breadcrumbs sx={{ mb: 2 }}>
        <Link component={RouterLink} to="/" color="inherit">
          Dashboard
        </Link>
        <Link component={RouterLink} to={routes.content.list} color="inherit">
          Content
        </Link>
        <Typography color="text.primary">
          {isNewContent ? 'Create Content' : 'Edit Content'}
        </Typography>
      </Breadcrumbs>
      
      {/* Page header */}
      <Box sx={{ mb: 4 }}>
        <Button
          startIcon={<ArrowBackIcon />}
          component={RouterLink}
          to={isNewContent ? routes.content.list : routes.content.detail(contentId!)}
          sx={{ mb: 2 }}
        >
          {isNewContent ? 'Back to Content List' : 'Back to Content Details'}
        </Button>
        <Typography variant="h4" component="h1" gutterBottom>
          {isNewContent ? 'Create New Content' : 'Edit Content'}
        </Typography>
      </Box>
      
      {/* Form */}
      <Paper sx={{ p: 3 }}>
        <Box component="form" onSubmit={handleSubmit}>
          <Grid container spacing={3}>
            {/* Title */}
            <Grid item xs={12}>
              <TextField
                name="title"
                label="Title"
                fullWidth
                value={formValues.title}
                onChange={handleChange}
                error={!!errors.title}
                helperText={errors.title}
                required
              />
            </Grid>
            
            {/* Content type */}
            <Grid item xs={12} sm={6}>
              <FormControl fullWidth>
                <InputLabel id="type-label">Content Type</InputLabel>
                <Select
                  labelId="type-label"
                  name="type"
                  value={formValues.type}
                  onChange={handleSelectChange as any}
                  label="Content Type"
                >
                  <MenuItem value="page">Page</MenuItem>
                  <MenuItem value="post">Post</MenuItem>
                  <MenuItem value="document">Document</MenuItem>
                </Select>
              </FormControl>
            </Grid>
            
            {/* Status */}
            <Grid item xs={12} sm={6}>
              <FormControl fullWidth>
                <InputLabel id="status-label">Status</InputLabel>
                <Select
                  labelId="status-label"
                  name="status"
                  value={formValues.status}
                  onChange={handleSelectChange as any}
                  label="Status"
                >
                  <MenuItem value="draft">Draft</MenuItem>
                  <MenuItem value="published">Published</MenuItem>
                  <MenuItem value="archived">Archived</MenuItem>
                </Select>
              </FormControl>
            </Grid>
            
            {/* Content body */}
            <Grid item xs={12}>
              <TextField
                name="body"
                label="Content"
                fullWidth
                multiline
                rows={12}
                value={formValues.body}
                onChange={handleChange}
                error={!!errors.body}
                helperText={errors.body}
                required
              />
            </Grid>
            
            {/* Publish switch */}
            <Grid item xs={12}>
              <FormControlLabel
                control={
                  <Switch
                    name="isPublished"
                    checked={formValues.isPublished}
                    onChange={handleSwitchChange}
                    color="primary"
                  />
                }
                label="Publish immediately"
              />
              <FormHelperText>
                {formValues.isPublished 
                  ? 'Content will be visible to users with appropriate permissions' 
                  : 'Content will be saved as a draft'}
              </FormHelperText>
            </Grid>
            
            <Grid item xs={12}>
              <Divider sx={{ my: 2 }} />
            </Grid>
            
            {/* Action buttons */}
            <Grid item xs={12}>
              <Box sx={{ display: 'flex', justifyContent: 'flex-end', gap: 2 }}>
                <Button
                  variant="outlined"
                  onClick={handleCancel}
                >
                  Cancel
                </Button>
                <Button
                  type="submit"
                  variant="contained"
                  color="primary"
                  startIcon={<SaveIcon />}
                >
                  {isNewContent ? 'Create Content' : 'Save Changes'}
                </Button>
              </Box>
            </Grid>
          </Grid>
        </Box>
      </Paper>
    </Container>
  );
};

export default ContentEditPage;
