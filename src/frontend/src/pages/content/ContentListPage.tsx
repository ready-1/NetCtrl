import React, { useState, useEffect } from 'react';
import { Link as RouterLink } from 'react-router-dom';
import {
  Box,
  Button,
  Card,
  Container,
  Chip,
  Divider,
  Grid,
  IconButton,
  InputAdornment,
  Menu,
  MenuItem,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TablePagination,
  TableRow,
  TextField,
  Typography,
  useMediaQuery,
  useTheme,
} from '@mui/material';
import {
  Add as AddIcon,
  Delete as DeleteIcon,
  Edit as EditIcon,
  FilterList as FilterIcon,
  MoreVert as MoreVertIcon,
  Search as SearchIcon,
  Visibility as VisibilityIcon,
} from '@mui/icons-material';
import { useAuth } from '../../context/AuthContext';
import routes from '../../config/routes';

// Content status types
type ContentStatus = 'draft' | 'published' | 'archived';

// Content type definition
interface Content {
  id: string;
  title: string;
  type: string;
  status: ContentStatus;
  lastModified: string;
  createdBy: string;
}

// Status color mapping
const getStatusColor = (status: ContentStatus) => {
  switch (status) {
    case 'published':
      return 'success';
    case 'draft':
      return 'warning';
    case 'archived':
      return 'error';
    default:
      return 'default';
  }
};

/**
 * ContentListPage component
 * 
 * Displays a list of content items with:
 * - Search functionality
 * - Filtering options
 * - Sorting capabilities
 * - Pagination
 * - Create/edit/delete actions
 * 
 * Adapts to mobile with a card-based layout
 */
const ContentListPage: React.FC = () => {
  const theme = useTheme();
  const { hasPermission } = useAuth();
  const isMobile = useMediaQuery(theme.breakpoints.down('md'));
  
  // Mock data for demonstration
  const mockData: Content[] = [
    {
      id: '1',
      title: 'Homepage Content',
      type: 'Page',
      status: 'published',
      lastModified: '2025-03-01',
      createdBy: 'admin',
    },
    {
      id: '2',
      title: 'About Us',
      type: 'Page',
      status: 'draft',
      lastModified: '2025-03-05',
      createdBy: 'editor',
    },
    {
      id: '3',
      title: 'Latest News',
      type: 'Post',
      status: 'published',
      lastModified: '2025-03-10',
      createdBy: 'editor',
    },
    {
      id: '4',
      title: 'Product Information',
      type: 'Document',
      status: 'published',
      lastModified: '2025-03-12',
      createdBy: 'admin',
    },
    {
      id: '5',
      title: 'Service Announcement',
      type: 'Post',
      status: 'draft',
      lastModified: '2025-03-15',
      createdBy: 'editor',
    },
  ];
  
  // State
  const [content, setContent] = useState<Content[]>(mockData);
  const [filteredContent, setFilteredContent] = useState<Content[]>(mockData);
  const [search, setSearch] = useState('');
  const [statusFilter, setStatusFilter] = useState<ContentStatus | 'all'>('all');
  const [typeFilter, setTypeFilter] = useState<string | 'all'>('all');
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  
  // Action menu state
  const [actionMenuAnchor, setActionMenuAnchor] = useState<null | HTMLElement>(null);
  const [selectedContentId, setSelectedContentId] = useState<string | null>(null);
  
  // Filter menu state
  const [filterMenuAnchor, setFilterMenuAnchor] = useState<null | HTMLElement>(null);
  
  // Permissions
  const canCreate = hasPermission('content:create');
  const canEdit = hasPermission('content:edit');
  const canDelete = hasPermission('content:delete');
  
  // Filter content based on search and filters
  useEffect(() => {
    let result = content;
    
    // Apply search filter
    if (search) {
      const searchLower = search.toLowerCase();
      result = result.filter((item) => 
        item.title.toLowerCase().includes(searchLower) ||
        item.type.toLowerCase().includes(searchLower) ||
        item.createdBy.toLowerCase().includes(searchLower)
      );
    }
    
    // Apply status filter
    if (statusFilter !== 'all') {
      result = result.filter((item) => item.status === statusFilter);
    }
    
    // Apply type filter
    if (typeFilter !== 'all') {
      result = result.filter((item) => item.type === typeFilter);
    }
    
    setFilteredContent(result);
  }, [content, search, statusFilter, typeFilter]);
  
  // Handle search change
  const handleSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSearch(e.target.value);
  };
  
  // Handle pagination
  const handleChangePage = (event: unknown, newPage: number) => {
    setPage(newPage);
  };
  
  const handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };
  
  // Handle action menu
  const handleActionMenuOpen = (event: React.MouseEvent<HTMLElement>, contentId: string) => {
    setActionMenuAnchor(event.currentTarget);
    setSelectedContentId(contentId);
  };
  
  const handleActionMenuClose = () => {
    setActionMenuAnchor(null);
    setSelectedContentId(null);
  };
  
  // Handle filter menu
  const handleFilterMenuOpen = (event: React.MouseEvent<HTMLElement>) => {
    setFilterMenuAnchor(event.currentTarget);
  };
  
  const handleFilterMenuClose = () => {
    setFilterMenuAnchor(null);
  };
  
  // Handle status filter
  const handleStatusFilterChange = (status: ContentStatus | 'all') => {
    setStatusFilter(status);
    handleFilterMenuClose();
  };
  
  // Handle type filter
  const handleTypeFilterChange = (type: string | 'all') => {
    setTypeFilter(type);
    handleFilterMenuClose();
  };
  
  // Get unique content types
  const contentTypes = Array.from(
    new Set(content.map((item) => item.type))
  );
  
  // Mobile card view
  const renderMobileView = () => (
    <Grid container spacing={2}>
      {filteredContent
        .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
        .map((item) => (
          <Grid item xs={12} key={item.id}>
            <Card sx={{ p: 2 }}>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 2 }}>
                <Typography variant="h6" component="div">
                  {item.title}
                </Typography>
                <IconButton 
                  size="small"
                  onClick={(e) => handleActionMenuOpen(e, item.id)}
                >
                  <MoreVertIcon />
                </IconButton>
              </Box>
              
              <Divider sx={{ my: 1 }} />
              
              <Grid container spacing={2}>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">
                    Type
                  </Typography>
                  <Typography variant="body1">
                    {item.type}
                  </Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">
                    Status
                  </Typography>
                  <Chip 
                    label={item.status}
                    size="small"
                    color={getStatusColor(item.status) as any}
                  />
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">
                    Last Modified
                  </Typography>
                  <Typography variant="body1">
                    {item.lastModified}
                  </Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">
                    Created By
                  </Typography>
                  <Typography variant="body1">
                    {item.createdBy}
                  </Typography>
                </Grid>
              </Grid>
            </Card>
          </Grid>
      ))}
    </Grid>
  );
  
  // Desktop table view
  const renderDesktopView = () => (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Title</TableCell>
            <TableCell>Type</TableCell>
            <TableCell>Status</TableCell>
            <TableCell>Last Modified</TableCell>
            <TableCell>Created By</TableCell>
            <TableCell align="right">Actions</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {filteredContent
            .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
            .map((item) => (
              <TableRow key={item.id}>
                <TableCell component="th" scope="row">
                  {item.title}
                </TableCell>
                <TableCell>{item.type}</TableCell>
                <TableCell>
                  <Chip 
                    label={item.status}
                    size="small"
                    color={getStatusColor(item.status) as any}
                  />
                </TableCell>
                <TableCell>{item.lastModified}</TableCell>
                <TableCell>{item.createdBy}</TableCell>
                <TableCell align="right">
                  <IconButton
                    component={RouterLink}
                    to={routes.content.detail(item.id)}
                    size="small"
                  >
                    <VisibilityIcon fontSize="small" />
                  </IconButton>
                  {canEdit && (
                    <IconButton
                      component={RouterLink}
                      to={routes.content.edit(item.id)}
                      size="small"
                    >
                      <EditIcon fontSize="small" />
                    </IconButton>
                  )}
                  {canDelete && (
                    <IconButton
                      size="small"
                      onClick={(e) => handleActionMenuOpen(e, item.id)}
                    >
                      <DeleteIcon fontSize="small" />
                    </IconButton>
                  )}
                </TableCell>
              </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      {/* Page header */}
      <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 3 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Content Management
        </Typography>
        
        {canCreate && (
          <Button
            variant="contained"
            color="primary"
            startIcon={<AddIcon />}
            component={RouterLink}
            to={routes.content.create}
          >
            Create New
          </Button>
        )}
      </Box>
      
      {/* Filters and search */}
      <Box sx={{ mb: 3 }}>
        <Grid container spacing={2} alignItems="center">
          <Grid item xs={12} md={6}>
            <TextField
              fullWidth
              placeholder="Search content..."
              value={search}
              onChange={handleSearchChange}
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <SearchIcon />
                  </InputAdornment>
                ),
              }}
            />
          </Grid>
          <Grid item xs={12} md={6}>
            <Box sx={{ display: 'flex', justifyContent: 'flex-end' }}>
              <Button
                variant="outlined"
                startIcon={<FilterIcon />}
                onClick={handleFilterMenuOpen}
                sx={{ mr: 1 }}
              >
                Filter
              </Button>
              
              {/* Show active filters */}
              {statusFilter !== 'all' && (
                <Chip 
                  label={`Status: ${statusFilter}`}
                  color={getStatusColor(statusFilter as ContentStatus)}
                  onDelete={() => setStatusFilter('all')}
                  sx={{ mr: 1 }}
                />
              )}
              
              {typeFilter !== 'all' && (
                <Chip 
                  label={`Type: ${typeFilter}`}
                  onDelete={() => setTypeFilter('all')}
                />
              )}
            </Box>
          </Grid>
        </Grid>
        
        {/* Filter menu */}
        <Menu
          anchorEl={filterMenuAnchor}
          open={Boolean(filterMenuAnchor)}
          onClose={handleFilterMenuClose}
        >
          <MenuItem disabled>
            <Typography variant="subtitle2">Status</Typography>
          </MenuItem>
          <MenuItem
            selected={statusFilter === 'all'}
            onClick={() => handleStatusFilterChange('all')}
          >
            All
          </MenuItem>
          <MenuItem
            selected={statusFilter === 'published'}
            onClick={() => handleStatusFilterChange('published')}
          >
            Published
          </MenuItem>
          <MenuItem
            selected={statusFilter === 'draft'}
            onClick={() => handleStatusFilterChange('draft')}
          >
            Draft
          </MenuItem>
          <MenuItem
            selected={statusFilter === 'archived'}
            onClick={() => handleStatusFilterChange('archived')}
          >
            Archived
          </MenuItem>
          
          <Divider />
          
          <MenuItem disabled>
            <Typography variant="subtitle2">Type</Typography>
          </MenuItem>
          <MenuItem
            selected={typeFilter === 'all'}
            onClick={() => handleTypeFilterChange('all')}
          >
            All
          </MenuItem>
          {contentTypes.map((type) => (
            <MenuItem
              key={type}
              selected={typeFilter === type}
              onClick={() => handleTypeFilterChange(type)}
            >
              {type}
            </MenuItem>
          ))}
        </Menu>
      </Box>
      
      {/* Content list */}
      {filteredContent.length === 0 ? (
        <Box sx={{ textAlign: 'center', py: 5 }}>
          <Typography variant="body1" color="text.secondary">
            No content items found.
          </Typography>
        </Box>
      ) : (
        <>
          {isMobile ? renderMobileView() : renderDesktopView()}
          
          {/* Pagination */}
          <TablePagination
            component="div"
            count={filteredContent.length}
            page={page}
            onPageChange={handleChangePage}
            rowsPerPage={rowsPerPage}
            onRowsPerPageChange={handleChangeRowsPerPage}
            rowsPerPageOptions={[5, 10, 25, 50]}
          />
        </>
      )}
      
      {/* Action menu */}
      <Menu
        anchorEl={actionMenuAnchor}
        open={Boolean(actionMenuAnchor)}
        onClose={handleActionMenuClose}
      >
        <MenuItem
          component={RouterLink}
          to={selectedContentId ? routes.content.detail(selectedContentId) : '#'}
          onClick={handleActionMenuClose}
        >
          <VisibilityIcon fontSize="small" sx={{ mr: 1 }} />
          View
        </MenuItem>
        {canEdit && (
          <MenuItem
            component={RouterLink}
            to={selectedContentId ? routes.content.edit(selectedContentId) : '#'}
            onClick={handleActionMenuClose}
          >
            <EditIcon fontSize="small" sx={{ mr: 1 }} />
            Edit
          </MenuItem>
        )}
        {canDelete && (
          <MenuItem onClick={handleActionMenuClose}>
            <DeleteIcon fontSize="small" sx={{ mr: 1 }} />
            Delete
          </MenuItem>
        )}
      </Menu>
    </Container>
  );
};

export default ContentListPage;
