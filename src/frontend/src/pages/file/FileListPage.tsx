import React, { useState, useEffect } from 'react';
import { Link as RouterLink } from 'react-router-dom';
import {
  Box,
  Button,
  Card,
  CardContent,
  Container,
  Chip,
  Divider,
  Grid,
  IconButton,
  InputAdornment,
  LinearProgress,
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
  Tooltip,
  Typography,
  useMediaQuery,
  useTheme,
} from '@mui/material';
import {
  Add as AddIcon,
  Delete as DeleteIcon,
  Download as DownloadIcon,
  FilterList as FilterIcon,
  Folder as FolderIcon,
  FolderOpen as FolderOpenIcon,
  Image as ImageIcon,
  InsertDriveFile as FileIcon,
  MoreVert as MoreVertIcon,
  PictureAsPdf as PdfIcon,
  Search as SearchIcon,
  VideoFile as VideoIcon,
} from '@mui/icons-material';
import { useAuth } from '../../context/AuthContext';
import routes from '../../config/routes';

// File type definition
interface File {
  id: string;
  name: string;
  type: string;
  size: number;
  uploadDate: string;
  uploadedBy: string;
  contentId?: string;
}

// File icon mapping by type
const getFileIcon = (fileType: string) => {
  if (fileType.startsWith('image/')) {
    return <ImageIcon />;
  } else if (fileType.startsWith('video/')) {
    return <VideoIcon />;
  } else if (fileType === 'application/pdf') {
    return <PdfIcon />;
  } else {
    return <FileIcon />;
  }
};

// Format file size
const formatFileSize = (bytes: number): string => {
  if (bytes === 0) return '0 Bytes';
  
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
};

/**
 * FileListPage component
 * 
 * Displays a list of uploaded files with:
 * - Search functionality
 * - Filtering options
 * - File upload button
 * - Download/delete actions
 * - Pagination
 * 
 * Adapts to mobile with a card-based layout
 */
const FileListPage: React.FC = () => {
  const theme = useTheme();
  const { hasPermission } = useAuth();
  const isMobile = useMediaQuery(theme.breakpoints.down('md'));
  
  // Mock data for demonstration
  const mockData: File[] = [
    {
      id: '1',
      name: 'product-image.jpg',
      type: 'image/jpeg',
      size: 1024 * 1024 * 2.5, // 2.5 MB
      uploadDate: '2025-03-01',
      uploadedBy: 'admin',
      contentId: '4',
    },
    {
      id: '2',
      name: 'report-q1.pdf',
      type: 'application/pdf',
      size: 1024 * 1024 * 5.8, // 5.8 MB
      uploadDate: '2025-03-05',
      uploadedBy: 'editor',
    },
    {
      id: '3',
      name: 'company-presentation.mp4',
      type: 'video/mp4',
      size: 1024 * 1024 * 45, // 45 MB
      uploadDate: '2025-03-10',
      uploadedBy: 'editor',
      contentId: '3',
    },
    {
      id: '4',
      name: 'product-specifications.docx',
      type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
      size: 1024 * 1024 * 1.2, // 1.2 MB
      uploadDate: '2025-03-12',
      uploadedBy: 'admin',
      contentId: '4',
    },
    {
      id: '5',
      name: 'logo.png',
      type: 'image/png',
      size: 1024 * 512, // 512 KB
      uploadDate: '2025-03-15',
      uploadedBy: 'editor',
    },
  ];
  
  // State
  const [files, setFiles] = useState<File[]>(mockData);
  const [filteredFiles, setFilteredFiles] = useState<File[]>(mockData);
  const [search, setSearch] = useState('');
  const [typeFilter, setTypeFilter] = useState<string | 'all'>('all');
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  
  // Action menu state
  const [actionMenuAnchor, setActionMenuAnchor] = useState<null | HTMLElement>(null);
  const [selectedFileId, setSelectedFileId] = useState<string | null>(null);
  
  // Filter menu state
  const [filterMenuAnchor, setFilterMenuAnchor] = useState<null | HTMLElement>(null);
  
  // Permissions
  const canUpload = hasPermission('file:upload');
  const canDelete = hasPermission('file:delete');
  
  // Filter files based on search and filters
  useEffect(() => {
    let result = files;
    
    // Apply search filter
    if (search) {
      const searchLower = search.toLowerCase();
      result = result.filter((item) => 
        item.name.toLowerCase().includes(searchLower) ||
        item.type.toLowerCase().includes(searchLower) ||
        item.uploadedBy.toLowerCase().includes(searchLower)
      );
    }
    
    // Apply type filter
    if (typeFilter !== 'all') {
      result = result.filter((item) => item.type.startsWith(typeFilter + '/'));
    }
    
    setFilteredFiles(result);
  }, [files, search, typeFilter]);
  
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
  const handleActionMenuOpen = (event: React.MouseEvent<HTMLElement>, fileId: string) => {
    setActionMenuAnchor(event.currentTarget);
    setSelectedFileId(fileId);
  };
  
  const handleActionMenuClose = () => {
    setActionMenuAnchor(null);
    setSelectedFileId(null);
  };
  
  // Handle filter menu
  const handleFilterMenuOpen = (event: React.MouseEvent<HTMLElement>) => {
    setFilterMenuAnchor(event.currentTarget);
  };
  
  const handleFilterMenuClose = () => {
    setFilterMenuAnchor(null);
  };
  
  // Handle type filter
  const handleTypeFilterChange = (type: string | 'all') => {
    setTypeFilter(type);
    handleFilterMenuClose();
  };
  
  // Get unique file types
  const fileTypes = Array.from(
    new Set(files.map((item) => item.type.split('/')[0]))
  );
  
  // Mobile card view
  const renderMobileView = () => (
    <Grid container spacing={2}>
      {filteredFiles
        .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
        .map((item) => (
          <Grid item xs={12} key={item.id}>
            <Card sx={{ p: 2 }}>
              <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                <Box sx={{ mr: 2 }}>
                  {getFileIcon(item.type)}
                </Box>
                <Box sx={{ flexGrow: 1 }}>
                  <Typography variant="h6" component="div" noWrap>
                    {item.name}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    {formatFileSize(item.size)}
                  </Typography>
                </Box>
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
                    {item.type.split('/')[1]}
                  </Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">
                    Upload Date
                  </Typography>
                  <Typography variant="body1">
                    {item.uploadDate}
                  </Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">
                    Uploaded By
                  </Typography>
                  <Typography variant="body1">
                    {item.uploadedBy}
                  </Typography>
                </Grid>
                {item.contentId && (
                  <Grid item xs={6}>
                    <Typography variant="body2" color="text.secondary">
                      Linked Content
                    </Typography>
                    <Link
                      component={RouterLink}
                      to={routes.content.detail(item.contentId)}
                    >
                      View Content
                    </Link>
                  </Grid>
                )}
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
            <TableCell>File</TableCell>
            <TableCell>Type</TableCell>
            <TableCell>Size</TableCell>
            <TableCell>Upload Date</TableCell>
            <TableCell>Uploaded By</TableCell>
            <TableCell>Linked Content</TableCell>
            <TableCell align="right">Actions</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {filteredFiles
            .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
            .map((item) => (
              <TableRow key={item.id}>
                <TableCell>
                  <Box sx={{ display: 'flex', alignItems: 'center' }}>
                    <Box sx={{ mr: 1 }}>{getFileIcon(item.type)}</Box>
                    <Typography noWrap>{item.name}</Typography>
                  </Box>
                </TableCell>
                <TableCell>{item.type.split('/')[1]}</TableCell>
                <TableCell>{formatFileSize(item.size)}</TableCell>
                <TableCell>{item.uploadDate}</TableCell>
                <TableCell>{item.uploadedBy}</TableCell>
                <TableCell>
                  {item.contentId ? (
                    <Link
                      component={RouterLink}
                      to={routes.content.detail(item.contentId)}
                    >
                      View Content
                    </Link>
                  ) : (
                    '-'
                  )}
                </TableCell>
                <TableCell align="right">
                  <Tooltip title="Download">
                    <IconButton size="small">
                      <DownloadIcon fontSize="small" />
                    </IconButton>
                  </Tooltip>
                  
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
          File Management
        </Typography>
        
        {canUpload && (
          <Button
            variant="contained"
            color="primary"
            startIcon={<AddIcon />}
            component={RouterLink}
            to={routes.files.upload}
          >
            Upload File
          </Button>
        )}
      </Box>
      
      {/* Filters and search */}
      <Box sx={{ mb: 3 }}>
        <Grid container spacing={2} alignItems="center">
          <Grid item xs={12} md={6}>
            <TextField
              fullWidth
              placeholder="Search files..."
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
          <MenuItem
            selected={typeFilter === 'all'}
            onClick={() => handleTypeFilterChange('all')}
          >
            All Files
          </MenuItem>
          {fileTypes.map((type) => (
            <MenuItem
              key={type}
              selected={typeFilter === type}
              onClick={() => handleTypeFilterChange(type)}
            >
              {type.charAt(0).toUpperCase() + type.slice(1)}
            </MenuItem>
          ))}
        </Menu>
      </Box>
      
      {/* File list */}
      {filteredFiles.length === 0 ? (
        <Box sx={{ textAlign: 'center', py: 5 }}>
          <Typography variant="body1" color="text.secondary">
            No files found.
          </Typography>
        </Box>
      ) : (
        <>
          {isMobile ? renderMobileView() : renderDesktopView()}
          
          {/* Pagination */}
          <TablePagination
            component="div"
            count={filteredFiles.length}
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
        <MenuItem onClick={handleActionMenuClose}>
          <DownloadIcon fontSize="small" sx={{ mr: 1 }} />
          Download
        </MenuItem>
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

export default FileListPage;
