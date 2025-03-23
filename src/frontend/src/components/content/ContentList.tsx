import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import {
  Box,
  Button,
  Card,
  CardContent,
  Chip,
  FormControl,
  Grid,
  IconButton,
  InputLabel,
  MenuItem,
  Paper,
  Select,
  SelectChangeEvent,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TablePagination,
  TableRow,
  TextField,
  Tooltip,
  Typography,
  useTheme,
  useMediaQuery,
} from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import VisibilityIcon from '@mui/icons-material/Visibility';
import SearchIcon from '@mui/icons-material/Search';
import RefreshIcon from '@mui/icons-material/Refresh';
import { ContentStatus, ContentType } from '../../types/content';
import { useContentList, useDeleteContent } from '../../hooks/useContentQuery';
import { useAuth } from '../../context/AuthContext';
import routes from '../../config/routes';

// Status chip colors
const statusColorMap: Record<ContentStatus, 'default' | 'primary' | 'success' | 'error'> = {
  [ContentStatus.DRAFT]: 'default',
  [ContentStatus.PUBLISHED]: 'success',
  [ContentStatus.ARCHIVED]: 'error',
};

// Helper to format dates
const formatDate = (dateString: string) => {
  const date = new Date(dateString);
  return new Intl.DateTimeFormat('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  }).format(date);
};

// Content type display names
const contentTypeDisplayMap: Record<ContentType, string> = {
  [ContentType.TEXT]: 'Text',
  [ContentType.HTML]: 'HTML',
  [ContentType.MARKDOWN]: 'Markdown',
  [ContentType.FILE]: 'File',
};

const ContentList: React.FC = () => {
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));
  const navigate = useNavigate();
  const { hasRole } = useAuth();
  
  // State for filters and pagination
  const [filters, setFilters] = useState({
    status: '',
    content_type: '',
    search: '',
  });
  
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  
  // Query params for API
  const queryParams = {
    status: filters.status ? filters.status as ContentStatus : undefined,
    content_type: filters.content_type ? filters.content_type as ContentType : undefined,
    search: filters.search ? filters.search : undefined,
    page: page + 1, // API uses 1-based indexing
    limit: rowsPerPage,
  };
  
  // Fetch content data with React Query
  const { 
    data, 
    isLoading, 
    isError, 
    refetch 
  } = useContentList(queryParams);
  
  // Delete mutation
  const { mutate: deleteContent, isLoading: isDeleting } = useDeleteContent();
  
  // Calculate placeholder rows for loading state
  const loadingRows = Array.from({ length: rowsPerPage }, (_, i) => i);
  
  // Filter change handlers
  const handleStatusChange = (event: SelectChangeEvent) => {
    setFilters({
      ...filters,
      status: event.target.value,
    });
    setPage(0); // Reset to first page when filter changes
  };
  
  const handleTypeChange = (event: SelectChangeEvent) => {
    setFilters({
      ...filters,
      content_type: event.target.value,
    });
    setPage(0); // Reset to first page when filter changes
  };
  
  const handleSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFilters({
      ...filters,
      search: event.target.value,
    });
    setPage(0); // Reset to first page when search changes
  };
  
  // Pagination handlers
  const handleChangePage = (event: unknown, newPage: number) => {
    setPage(newPage);
  };
  
  const handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };
  
  // View/Edit/Delete handlers
  const handleView = (id: number) => {
    navigate(routes.content.detail(id.toString()));
  };
  
  const handleEdit = (id: number) => {
    navigate(routes.content.edit(id.toString()));
  };
  
  const handleDelete = (id: number) => {
    if (window.confirm('Are you sure you want to delete this content? This action cannot be undone.')) {
      deleteContent(id);
    }
  };
  
  const handleAddNew = () => {
    navigate(routes.content.create);
  };

  // Check if user can edit/delete based on role
  const canEdit = hasRole('admin') || hasRole('manager');
  const canDelete = hasRole('admin');
  
  return (
    <Box>
      <Paper sx={{ p: 2, mb: 2 }}>
        <Box display="flex" justifyContent="space-between" alignItems="center" mb={2}>
          <Typography variant="h5" component="h1">
            Content Management
          </Typography>
          
          {/* Only show add button if user has permission */}
          {canEdit && (
            <Button
              variant="contained"
              color="primary"
              startIcon={<AddIcon />}
              onClick={handleAddNew}
            >
              Create New
            </Button>
          )}
        </Box>
        
        <Grid container spacing={2} alignItems="center" mb={2}>
          {/* Search input */}
          <Grid item xs={12} sm={6} md={4}>
            <TextField
              fullWidth
              variant="outlined"
              size="small"
              placeholder="Search..."
              value={filters.search}
              onChange={handleSearchChange}
              InputProps={{
                startAdornment: <SearchIcon color="action" sx={{ mr: 1 }} />,
              }}
            />
          </Grid>
          
          {/* Status filter */}
          <Grid item xs={6} sm={3} md={2}>
            <FormControl fullWidth size="small">
              <InputLabel id="status-filter-label">Status</InputLabel>
              <Select
                labelId="status-filter-label"
                value={filters.status}
                label="Status"
                onChange={handleStatusChange}
              >
                <MenuItem value="">All</MenuItem>
                <MenuItem value={ContentStatus.DRAFT}>Draft</MenuItem>
                <MenuItem value={ContentStatus.PUBLISHED}>Published</MenuItem>
                <MenuItem value={ContentStatus.ARCHIVED}>Archived</MenuItem>
              </Select>
            </FormControl>
          </Grid>
          
          {/* Type filter */}
          <Grid item xs={6} sm={3} md={2}>
            <FormControl fullWidth size="small">
              <InputLabel id="type-filter-label">Type</InputLabel>
              <Select
                labelId="type-filter-label"
                value={filters.content_type}
                label="Type"
                onChange={handleTypeChange}
              >
                <MenuItem value="">All</MenuItem>
                <MenuItem value={ContentType.TEXT}>Text</MenuItem>
                <MenuItem value={ContentType.HTML}>HTML</MenuItem>
                <MenuItem value={ContentType.MARKDOWN}>Markdown</MenuItem>
                <MenuItem value={ContentType.FILE}>File</MenuItem>
              </Select>
            </FormControl>
          </Grid>
          
          {/* Refresh button */}
          <Grid item xs={12} sm="auto">
            <Tooltip title="Refresh">
              <IconButton onClick={() => refetch()} disabled={isLoading}>
                <RefreshIcon />
              </IconButton>
            </Tooltip>
          </Grid>
        </Grid>
        
        {/* Desktop table view */}
        {!isMobile && (
          <>
            <TableContainer>
              <Table aria-label="content table">
                <TableHead>
                  <TableRow>
                    <TableCell>Title</TableCell>
                    <TableCell>Type</TableCell>
                    <TableCell>Status</TableCell>
                    <TableCell>Created</TableCell>
                    <TableCell>Updated</TableCell>
                    <TableCell align="right">Actions</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {isLoading ? (
                    // Loading placeholder rows
                    loadingRows.map((index) => (
                      <TableRow key={`loading-${index}`}>
                        <TableCell colSpan={6}>
                          <Box sx={{ display: 'flex', alignItems: 'center', height: '57px' }}>
                            <Typography variant="body2" color="text.secondary">
                              Loading...
                            </Typography>
                          </Box>
                        </TableCell>
                      </TableRow>
                    ))
                  ) : isError ? (
                    // Error state
                    <TableRow>
                      <TableCell colSpan={6}>
                        <Typography color="error">
                          Error loading content. Please try again.
                        </Typography>
                      </TableCell>
                    </TableRow>
                  ) : (
                    // Content rows
                    data?.items.map((content) => (
                      <TableRow key={content.id}>
                        <TableCell>{content.title}</TableCell>
                        <TableCell>{contentTypeDisplayMap[content.content_type]}</TableCell>
                        <TableCell>
                          <Chip 
                            label={content.status.charAt(0).toUpperCase() + content.status.slice(1)} 
                            color={statusColorMap[content.status]}
                            size="small"
                          />
                        </TableCell>
                        <TableCell>{formatDate(content.created_at)}</TableCell>
                        <TableCell>{formatDate(content.updated_at)}</TableCell>
                        <TableCell align="right">
                          <Tooltip title="View">
                            <IconButton 
                              size="small" 
                              onClick={() => handleView(content.id)}
                            >
                              <VisibilityIcon fontSize="small" />
                            </IconButton>
                          </Tooltip>
                          
                          {canEdit && (
                            <Tooltip title="Edit">
                              <IconButton 
                                size="small" 
                                onClick={() => handleEdit(content.id)}
                              >
                                <EditIcon fontSize="small" />
                              </IconButton>
                            </Tooltip>
                          )}
                          
                          {canDelete && (
                            <Tooltip title="Delete">
                              <IconButton 
                                size="small" 
                                onClick={() => handleDelete(content.id)}
                                disabled={isDeleting}
                              >
                                <DeleteIcon fontSize="small" />
                              </IconButton>
                            </Tooltip>
                          )}
                        </TableCell>
                      </TableRow>
                    ))
                  )}
                  
                  {/* No results row */}
                  {!isLoading && !isError && data?.items.length === 0 && (
                    <TableRow>
                      <TableCell colSpan={6} align="center">
                        <Box py={2}>
                          <Typography variant="body1">
                            No content matches your filters.
                          </Typography>
                        </Box>
                      </TableCell>
                    </TableRow>
                  )}
                </TableBody>
              </Table>
            </TableContainer>
            
            {/* Pagination */}
            {!isLoading && !isError && data?.total > 0 && (
              <TablePagination
                rowsPerPageOptions={[5, 10, 25, 50]}
                component="div"
                count={data?.total || 0}
                rowsPerPage={rowsPerPage}
                page={page}
                onPageChange={handleChangePage}
                onRowsPerPageChange={handleChangeRowsPerPage}
              />
            )}
          </>
        )}
        
        {/* Mobile card view */}
        {isMobile && (
          <Box>
            {isLoading ? (
              // Loading cards
              loadingRows.slice(0, 3).map((index) => (
                <Card key={`loading-${index}`} sx={{ mb: 2 }}>
                  <CardContent>
                    <Typography>Loading...</Typography>
                  </CardContent>
                </Card>
              ))
            ) : isError ? (
              // Error card
              <Card sx={{ mb: 2 }}>
                <CardContent>
                  <Typography color="error">
                    Error loading content. Please try again.
                  </Typography>
                </CardContent>
              </Card>
            ) : (
              // Content cards
              <>
                {data?.items.map((content) => (
                  <Card key={content.id} sx={{ mb: 2 }}>
                    <CardContent>
                      <Box display="flex" justifyContent="space-between" alignItems="flex-start">
                        <Typography variant="h6" component="h2" gutterBottom>
                          {content.title}
                        </Typography>
                        <Chip 
                          label={content.status.charAt(0).toUpperCase() + content.status.slice(1)} 
                          color={statusColorMap[content.status]}
                          size="small"
                        />
                      </Box>
                      
                      <Box display="flex" flexDirection="column" gap={1} mb={2}>
                        <Typography variant="body2" color="text.secondary">
                          <strong>Type:</strong> {contentTypeDisplayMap[content.content_type]}
                        </Typography>
                        <Typography variant="body2" color="text.secondary">
                          <strong>Created:</strong> {formatDate(content.created_at)}
                        </Typography>
                        <Typography variant="body2" color="text.secondary">
                          <strong>Updated:</strong> {formatDate(content.updated_at)}
                        </Typography>
                      </Box>
                      
                      <Box display="flex" justifyContent="flex-end" gap={1}>
                        <Button
                          size="small"
                          startIcon={<VisibilityIcon />}
                          onClick={() => handleView(content.id)}
                        >
                          View
                        </Button>
                        
                        {canEdit && (
                          <Button
                            size="small"
                            startIcon={<EditIcon />}
                            onClick={() => handleEdit(content.id)}
                          >
                            Edit
                          </Button>
                        )}
                        
                        {canDelete && (
                          <Button
                            size="small"
                            color="error"
                            startIcon={<DeleteIcon />}
                            onClick={() => handleDelete(content.id)}
                            disabled={isDeleting}
                          >
                            Delete
                          </Button>
                        )}
                      </Box>
                    </CardContent>
                  </Card>
                ))}
                
                {/* No results */}
                {data?.items.length === 0 && (
                  <Box textAlign="center" py={4}>
                    <Typography variant="body1">
                      No content matches your filters.
                    </Typography>
                  </Box>
                )}
                
                {/* Pagination for mobile */}
                {data?.total > 0 && (
                  <TablePagination
                    rowsPerPageOptions={[5, 10, 25]}
                    component="div"
                    count={data?.total || 0}
                    rowsPerPage={rowsPerPage}
                    page={page}
                    onPageChange={handleChangePage}
                    onRowsPerPageChange={handleChangeRowsPerPage}
                  />
                )}
              </>
            )}
          </Box>
        )}
      </Paper>
    </Box>
  );
};

export default ContentList;
