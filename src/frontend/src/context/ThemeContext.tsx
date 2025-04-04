import React, { createContext, useContext, useState, useEffect, useMemo, ReactNode } from 'react';
import { ThemeProvider as MuiThemeProvider, createTheme, Theme, PaletteMode } from '@mui/material';

type ThemeContextType = {
  mode: PaletteMode;
  toggleColorMode: () => void;
};

// Create context with default values
const ThemeContext = createContext<ThemeContextType>({
  mode: 'light',
  toggleColorMode: () => {},
});

// Hook to use the theme context
export const useTheme = () => useContext(ThemeContext);

type ThemeProviderProps = {
  children: ReactNode;
};

export const ThemeProvider: React.FC<ThemeProviderProps> = ({ children }) => {
  // Get stored theme preference or use system preference
  const getInitialMode = (): PaletteMode => {
    // Check for saved preference in localStorage
    const savedMode = localStorage.getItem('theme-mode');
    if (savedMode && (savedMode === 'light' || savedMode === 'dark')) {
      return savedMode;
    }
    
    // Check for system preference
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return 'dark';
    }
    
    // Default to light mode
    return 'light';
  };

  const [mode, setMode] = useState<PaletteMode>(getInitialMode);

  // Listen for system preference changes
  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    
    const handleChange = (e: MediaQueryListEvent) => {
      if (!localStorage.getItem('theme-mode')) {
        setMode(e.matches ? 'dark' : 'light');
      }
    };
    
    mediaQuery.addEventListener('change', handleChange);
    return () => mediaQuery.removeEventListener('change', handleChange);
  }, []);

  // Toggle theme mode
  const toggleColorMode = () => {
    setMode((prevMode) => {
      const newMode = prevMode === 'light' ? 'dark' : 'light';
      localStorage.setItem('theme-mode', newMode);
      return newMode;
    });
  };

  // Create the theme
  const theme = useMemo(() => createTheme({
    palette: {
      mode,
      primary: {
        main: '#2196f3',
        light: '#64b5f6',
        dark: '#1976d2',
      },
      secondary: {
        main: '#f50057',
        light: '#ff4081',
        dark: '#c51162',
      },
      background: {
        default: mode === 'light' ? '#f5f5f5' : '#121212',
        paper: mode === 'light' ? '#ffffff' : '#1e1e1e',
      },
      text: {
        primary: mode === 'light' ? 'rgba(0, 0, 0, 0.87)' : 'rgba(255, 255, 255, 0.87)',
        secondary: mode === 'light' ? 'rgba(0, 0, 0, 0.6)' : 'rgba(255, 255, 255, 0.6)',
      },
    },
    typography: {
      fontFamily: [
        '"Roboto"',
        'Arial',
        'sans-serif',
      ].join(','),
    },
    components: {
      MuiButton: {
        styleOverrides: {
          root: {
            borderRadius: 4,
          },
        },
      },
      MuiAppBar: {
        styleOverrides: {
          root: {
            boxShadow: mode === 'light' 
              ? '0px 2px 4px rgba(0, 0, 0, 0.1)' 
              : '0px 2px 4px rgba(0, 0, 0, 0.3)',
          },
        },
      },
      MuiInputBase: {
        styleOverrides: {
          root: {
            // Default background to ensure contrast
            backgroundColor: mode === 'light' ? '#fcfcfc' : '#333',
            // Add transition for smooth color changes
            transition: 'all 0.2s ease-in-out',
            // Force text color to ensure visibility
            '& input': {
              color: mode === 'light' ? 'rgba(0, 0, 0, 0.87)' : 'rgba(255, 255, 255, 0.87)',
            },
            // Focus state - maintain text visibility
            '&.Mui-focused': {
              backgroundColor: mode === 'light' ? '#fff' : '#424242',
              '& input': {
                color: mode === 'light' ? 'rgba(0, 0, 0, 0.87)' : 'rgba(255, 255, 255, 0.87)',
              },
            },
            // On hover, ensure contrast
            '&:hover': {
              backgroundColor: mode === 'light' ? '#fff' : '#3a3a3a',
            },
          },
          input: {
            color: mode === 'light' ? 'rgba(0, 0, 0, 0.87)' : 'rgba(255, 255, 255, 0.87)',
            '&::placeholder': {
              color: mode === 'light' ? 'rgba(0, 0, 0, 0.42)' : 'rgba(255, 255, 255, 0.5)',
              opacity: 1,
            },
          },
        },
      },
      MuiFilledInput: {
        styleOverrides: {
          root: {
            backgroundColor: mode === 'light' ? 'rgba(0, 0, 0, 0.06)' : 'rgba(255, 255, 255, 0.09)',
            '&:hover': {
              backgroundColor: mode === 'light' ? 'rgba(0, 0, 0, 0.09)' : 'rgba(255, 255, 255, 0.13)',
            },
            '&.Mui-focused': {
              backgroundColor: mode === 'light' ? 'rgba(0, 0, 0, 0.09)' : 'rgba(255, 255, 255, 0.13)',
            },
          },
        },
      },
      MuiOutlinedInput: {
        styleOverrides: {
          root: {
            // Background color for better contrast
            backgroundColor: mode === 'light' ? '#fff' : '#333',
            // Normal state
            '& fieldset': {
              borderColor: mode === 'light' ? 'rgba(0, 0, 0, 0.23)' : 'rgba(255, 255, 255, 0.23)',
            },
            // Improved focus state
            '&.Mui-focused': {
              '& fieldset': {
                borderColor: mode === 'light' ? '#1976d2' : '#64b5f6',
                borderWidth: 2,
              },
              '& input': {
                color: mode === 'light' ? 'rgba(0, 0, 0, 0.87)' : 'rgba(255, 255, 255, 0.87)',
              },
            },
            // Better hover state
            '&:hover fieldset': {
              borderColor: mode === 'light' ? 'rgba(0, 0, 0, 0.42)' : 'rgba(255, 255, 255, 0.42)',
            },
          },
          notchedOutline: {
            // Better default border
            borderColor: mode === 'light' ? 'rgba(0, 0, 0, 0.23)' : 'rgba(255, 255, 255, 0.23)',
          },
        },
      },
      MuiFormLabel: {
        styleOverrides: {
          root: {
            // Better label visibility
            color: mode === 'light' ? 'rgba(0, 0, 0, 0.6)' : 'rgba(255, 255, 255, 0.6)',
            '&.Mui-focused': {
              color: mode === 'light' ? '#1976d2' : '#64b5f6',
            },
          },
        },
      },
      MuiTextField: {
        defaultProps: {
          variant: 'outlined',
        },
      },
      MuiLink: {
        styleOverrides: {
          root: {
            // Better link visibility
            color: mode === 'light' ? '#0059b3' : '#64b5f6',
          },
        },
      },
    },
  }), [mode]);

  // Context value
  const contextValue = {
    mode,
    toggleColorMode,
  };

  return (
    <ThemeContext.Provider value={contextValue}>
      <MuiThemeProvider theme={theme}>
        {children}
      </MuiThemeProvider>
    </ThemeContext.Provider>
  );
};
