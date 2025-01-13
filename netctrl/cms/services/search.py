"""
Search service for CMS content.
Handles file name and content search across different file types.
"""

import os
import yaml
import PyPDF2
from typing import List, Dict, Any
from django.conf import settings
from ..models import File

class SearchService:
    """Service class for searching files by name and content."""
    
    SUPPORTED_EXTENSIONS = {
        '.txt': 'text',
        '.md': 'text',
        '.yaml': 'yaml',
        '.yml': 'yaml',
        '.pdf': 'pdf'
    }
    
    def search(self, query: str) -> List[Dict[str, Any]]:
        """
        Search files by name and content.
        
        Args:
            query: Search query string
            
        Returns:
            List of matching files with metadata
        """
        if not query:
            return []
            
        query = query.lower()
        results = []
        
        # Get all files
        files = File.objects.all()
        
        for file in files:
            file_path = os.path.join(settings.MEDIA_ROOT, file.path)
            
            # Skip if file doesn't exist
            if not os.path.exists(file_path):
                file.delete()  # Clean up orphaned record
                continue
                
            # Check filename match
            if query in file.name.lower():
                results.append({
                    'id': str(file.id),
                    'name': file.name,
                    'path': f'{settings.MEDIA_URL}{file.path}',
                    'tags': file.tags or [],
                    'match_type': 'filename'
                })
                continue
            
            # Check content match for supported file types
            _, ext = os.path.splitext(file.name)
            if ext.lower() in self.SUPPORTED_EXTENSIONS:
                try:
                    content = self._read_file_content(file_path, ext.lower())
                    if content and query in content.lower():
                        results.append({
                            'id': str(file.id),
                            'name': file.name,
                            'path': f'{settings.MEDIA_URL}{file.path}',
                            'tags': file.tags or [],
                            'match_type': 'content'
                        })
                except Exception:
                    continue  # Skip files that can't be read
                    
        return results
        
    def _read_file_content(self, file_path: str, extension: str) -> str:
        """Read content from file based on type."""
        file_type = self.SUPPORTED_EXTENSIONS.get(extension)
        
        if file_type == 'text':
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
                
        elif file_type == 'yaml':
            with open(file_path, 'r', encoding='utf-8') as f:
                content = yaml.safe_load(f)
                return str(content)  # Convert YAML structure to string
                
        elif file_type == 'pdf':
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ''
                for page in reader.pages:
                    text += page.extract_text() + '\n'
                return text
                
        return ''  # Unsupported file type
