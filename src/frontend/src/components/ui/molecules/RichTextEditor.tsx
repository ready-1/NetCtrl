import React, { useRef, useMemo } from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import { styled } from '@mui/material/styles';
import { Box, Typography } from '@mui/material';

// Styled container for the editor
const EditorContainer = styled(Box)(({ theme }) => ({
  '& .quill': {
    borderRadius: theme.shape.borderRadius,
    backgroundColor: theme.palette.background.paper,
    border: `1px solid ${theme.palette.divider}`,
    '&:focus-within': {
      borderColor: theme.palette.primary.main,
    },
  },
  '& .ql-toolbar': {
    borderTop: `1px solid ${theme.palette.divider}`,
    borderLeft: `1px solid ${theme.palette.divider}`,
    borderRight: `1px solid ${theme.palette.divider}`,
    borderTopLeftRadius: theme.shape.borderRadius,
    borderTopRightRadius: theme.shape.borderRadius,
    backgroundColor: theme.palette.background.default,
  },
  '& .ql-container': {
    minHeight: '200px',
    borderLeft: `1px solid ${theme.palette.divider}`,
    borderRight: `1px solid ${theme.palette.divider}`,
    borderBottom: `1px solid ${theme.palette.divider}`,
    borderBottomLeftRadius: theme.shape.borderRadius,
    borderBottomRightRadius: theme.shape.borderRadius,
    fontSize: '1rem',
  },
  '& .ql-editor': {
    minHeight: '200px',
    maxHeight: '500px',
    overflow: 'auto',
  },
  '& .ql-editor.ql-blank::before': {
    fontStyle: 'normal',
    color: theme.palette.text.secondary,
  },
}));

// Error text styling
const ErrorText = styled(Typography)(({ theme }) => ({
  color: theme.palette.error.main,
  fontSize: '0.75rem',
  marginTop: theme.spacing(0.5),
  marginLeft: theme.spacing(1.5),
}));

// Define the toolbar options
const modules = {
  toolbar: [
    [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
    ['bold', 'italic', 'underline', 'strike'],
    [{ 'list': 'ordered'}, { 'list': 'bullet' }],
    [{ 'align': [] }],
    ['link', 'image'],
    ['clean'],
  ],
};

const formats = [
  'header',
  'bold', 'italic', 'underline', 'strike',
  'list', 'bullet',
  'align',
  'link', 'image',
];

interface RichTextEditorProps {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  error?: string;
  label?: string;
  readOnly?: boolean;
  minHeight?: number | string;
}

const RichTextEditor: React.FC<RichTextEditorProps> = ({
  value,
  onChange,
  placeholder = 'Enter content here...',
  error,
  label,
  readOnly = false,
  minHeight = '200px',
}) => {
  const quillRef = useRef<ReactQuill>(null);
  
  // Memoize modules to prevent unnecessary re-renders
  const editorModules = useMemo(() => ({
    ...modules,
    toolbar: readOnly ? false : modules.toolbar,
  }), [readOnly]);
  
  return (
    <Box sx={{ mb: 2 }}>
      {label && (
        <Typography
          variant="body2"
          fontWeight={500}
          color="text.primary"
          sx={{ mb: 1, ml: 1.5 }}
        >
          {label}
        </Typography>
      )}
      
      <EditorContainer>
        <ReactQuill
          ref={quillRef}
          value={value}
          onChange={onChange}
          modules={editorModules}
          formats={formats}
          placeholder={placeholder}
          readOnly={readOnly}
          theme="snow"
          style={{ 
            minHeight: typeof minHeight === 'number' ? `${minHeight}px` : minHeight 
          }}
        />
      </EditorContainer>
      
      {error && <ErrorText>{error}</ErrorText>}
    </Box>
  );
};

export default RichTextEditor;
