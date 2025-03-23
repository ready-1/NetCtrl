import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Box,
  Button,
  Card,
  CardContent,
  FormControl,
  FormHelperText,
  Grid,
  InputLabel,
  MenuItem,
  Paper,
  Select,
  SelectChangeEvent,
  TextField,
  Typography,
  Alert,
} from '@mui/material';
import SaveIcon from '@mui/icons-material/Save';
import CancelIcon from '@mui/icons-material/Cancel';
import RichTextEditor from '../ui/molecules/RichTextEditor';
import { ContentType, ContentStatus, ContentCreate, ContentUpdate, Content } from '../../types/content';
import { useCreateContent, useUpdateContent } from '../../hooks/useContentQuery';
import routes from '../../config/routes';

interface ContentFormProps {
  initialContent?: Content;
  isEditing?: boolean;
}

const ContentForm: React.FC<ContentFormProps> = ({ initialContent, isEditing = false }) => {
  const navigate = useNavigate();
  
  // Create or update mutation
  const createMutation = useCreateContent();
  const updateMutation = useUpdateContent(initialContent?.id || 0);
  
  // Determine if we're in a loading or error state
  const isLoading = createMutation.isLoading || updateMutation.isLoading;
  const error = createMutation.error || updateMutation.error;
  
  // Form state
  const [formData, setFormData] = useState<ContentCreate | ContentUpdate>({
    title: '',
    description: '',
    body: '',
    content_type: ContentType.HTML,
    status: ContentStatus.DRAFT,
  });
  
  // Form validation
  const [formErrors, setFormErrors] = useState({
    title: '',
    description: '',
    body: '',
  });
  
  // Initialize form with existing content if editing
  useEffect(() => {
    if (initialContent && isEditing) {
      setFormData({
        title: initialContent.title,
        description: initialContent.description || '',
        body: initialContent.body || '',
        content_type: initialContent.content_type,
        status: initialContent.status,
      });
    }
  }, [initialContent, isEditing]);
  
  // Form change handlers
  const handleTextChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    
    // Clear error when field is updated
    if (formErrors[name as keyof typeof formErrors]) {
      setFormErrors((prev) => ({ ...prev, [name]: '' }));
    }
  };
  
  const handleSelectChange = (e: SelectChangeEvent<ContentType | ContentStatus>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };
  
  const handleEditorChange = (value: string) => {
    setFormData((prev) => ({ ...prev, body: value }));
    
    // Clear error when editor content is updated
    if (formErrors.body) {
      setFormErrors((prev) => ({ ...prev, body: '' }));
    }
  };
  
  // Validate form
  const validateForm = (): boolean => {
    let isValid = true;
    const newErrors = { ...formErrors };
    
    if (!formData.title) {
      newErrors.title = 'Title is required';
      isValid = false;
    }
    
    // Only validate body for text/html/markdown content
    if (formData.content_type !== ContentType.FILE && !formData.body) {
      newErrors.body = 'Content is required';
      isValid = false;
    }
    
    setFormErrors(newErrors);
    return isValid;
  };
  
  // Handle form submission
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }
    
    if (isEditing && initialContent) {
      updateMutation.mutate(formData as ContentUpdate, {
        onSuccess: () => {
          navigate(routes.content.detail(initialContent.id.toString()));
        },
      });
    } else {
      createMutation.mutate(formData as ContentCreate, {
        onSuccess: (newContent) => {
          navigate(routes.content.detail(newContent.id.toString()));
        },
      });
    }
  };
  
  // Handle cancellation
  const handleCancel = () => {
    if (initialContent) {
      navigate(routes.content.detail(initialContent.id.toString()));
    } else {
      navigate(routes.content.list);
    }
  };
  
  return (
    <Box component="form" onSubmit={handleSubmit} noValidate>
      <Paper sx={{ p: 2, mb: 2 }}>
        <Box display="flex" justifyContent="space-between" alignItems="center" mb={3}>
          <Typography variant="h5" component="h1">
            {isEditing ? 'Edit Content' : 'Create New Content'}
          </Typography>
          
          <Box>
            <Button
              variant="outlined"
              color="secondary"
              onClick={handleCancel}
              startIcon={<CancelIcon />}
              sx={{ mr: 1 }}
              disabled={isLoading}
            >
              Cancel
            </Button>
            
            <Button
              type="submit"
              variant="contained"
              color="primary"
              startIcon={<SaveIcon />}
              disabled={isLoading}
            >
              {isLoading ? 'Saving...' : 'Save'}
            </Button>
          </Box>
        </Box>
        
        {error ? (
          <Alert severity="error" sx={{ mb: 3 }}>
            {error instanceof Error ? error.message : 'An error occurred while saving.'}
          </Alert>
        ) : null}
        
        <Grid container spacing={3}>
          {/* Title */}
          <Grid item xs={12}>
            <TextField
              required
              fullWidth
              id="title"
              name="title"
              label="Title"
              value={formData.title}
              onChange={handleTextChange}
              error={Boolean(formErrors.title)}
              helperText={formErrors.title}
              disabled={isLoading}
            />
          </Grid>
          
          {/* Description */}
          <Grid item xs={12}>
            <TextField
              fullWidth
              id="description"
              name="description"
              label="Description"
              value={formData.description}
              onChange={handleTextChange}
              multiline
              rows={2}
              error={Boolean(formErrors.description)}
              helperText={formErrors.description}
              disabled={isLoading}
            />
          </Grid>
          
          {/* Content Type */}
          <Grid item xs={12} sm={6}>
            <FormControl fullWidth>
              <InputLabel id="content-type-label">Content Type</InputLabel>
              <Select
                labelId="content-type-label"
                id="content_type"
                name="content_type"
                value={formData.content_type}
                onChange={handleSelectChange}
                label="Content Type"
                disabled={isEditing || isLoading} // Can't change content type when editing
              >
                <MenuItem value={ContentType.TEXT}>Plain Text</MenuItem>
                <MenuItem value={ContentType.HTML}>Rich Text (HTML)</MenuItem>
                <MenuItem value={ContentType.MARKDOWN}>Markdown</MenuItem>
                <MenuItem value={ContentType.FILE}>File</MenuItem>
              </Select>
              <FormHelperText>
                {isEditing ? "Content type can't be changed after creation" : "Choose the type of content you're creating"}
              </FormHelperText>
            </FormControl>
          </Grid>
          
          {/* Status */}
          <Grid item xs={12} sm={6}>
            <FormControl fullWidth>
              <InputLabel id="status-label">Status</InputLabel>
              <Select
                labelId="status-label"
                id="status"
                name="status"
                value={formData.status}
                onChange={handleSelectChange}
                label="Status"
                disabled={isLoading}
              >
                <MenuItem value={ContentStatus.DRAFT}>Draft</MenuItem>
                <MenuItem value={ContentStatus.PUBLISHED}>Published</MenuItem>
                <MenuItem value={ContentStatus.ARCHIVED}>Archived</MenuItem>
              </Select>
              <FormHelperText>
                Set the visibility status of this content
              </FormHelperText>
            </FormControl>
          </Grid>
          
          {/* Content Body - only show for text/html/markdown types */}
          {formData.content_type !== ContentType.FILE && (
            <Grid item xs={12}>
              <Card variant="outlined">
                <CardContent>
                  <Typography variant="subtitle1" gutterBottom>
                    Content
                  </Typography>
                  
                  {formData.content_type === ContentType.HTML ? (
                    <RichTextEditor
                      value={formData.body || ''}
                      onChange={handleEditorChange}
                      error={formErrors.body}
                      readOnly={isLoading}
                    />
                  ) : (
                    <TextField
                      fullWidth
                      id="body"
                      name="body"
                      label="Content"
                      value={formData.body || ''}
                      onChange={handleTextChange}
                      multiline
                      rows={12}
                      variant="outlined"
                      error={Boolean(formErrors.body)}
                      helperText={formErrors.body}
                      disabled={isLoading}
                    />
                  )}
                </CardContent>
              </Card>
            </Grid>
          )}
          
          {/* File Upload - only show for file type */}
          {formData.content_type === ContentType.FILE && (
            <Grid item xs={12}>
              <Card variant="outlined">
                <CardContent>
                  <Typography variant="subtitle1" gutterBottom>
                    File Upload
                  </Typography>
                  
                  <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
                    File upload functionality will be implemented separately.
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          )}
        </Grid>
      </Paper>
    </Box>
  );
};

export default ContentForm;
