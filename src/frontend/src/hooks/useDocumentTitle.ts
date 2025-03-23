import { useEffect } from 'react';

/**
 * A custom hook to set the document title with an optional app name prefix
 * 
 * @param title The page-specific title
 * @param appName Optional app name to be prefixed (with separator)
 */
export const useDocumentTitle = (title: string, appName = 'NetCtrl CMS') => {
  useEffect(() => {
    // Set the document title
    document.title = appName ? `${title} | ${appName}` : title;
    
    // Optionally return to previous title on unmount
    return () => {
      // We could restore previous title here if needed
    };
  }, [title, appName]);
};
