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
        
        # Search all directories and files
        base_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
        
        for root, dirs, filenames in os.walk(base_path):
            # Search directories
            for dirname in dirs:
                if query in dirname.lower():
                    rel_path = os.path.relpath(os.path.join(root, dirname), base_path)
                    results.append({
                        'name': dirname,
                        'path': rel_path,  # For navigation
                        'url': None,  # Directories don't have URLs
                        'tags': [],
                        'is_dir': True,
                        'parent_path': os.path.dirname(rel_path) if rel_path else ''  # For navigation
                    })
            
            # Search files
            for filename in filenames:
                if query in filename.lower():
                    rel_path = os.path.relpath(os.path.join(root, filename), base_path)
                    file_url = f'{settings.MEDIA_URL}uploads/{rel_path}'
                    parent_path = os.path.dirname(rel_path)
                    
                    # Get file object if it exists
                    try:
                        file_obj = File.objects.get(path=f'uploads/{rel_path}')
                        file_id = str(file_obj.id)
                        tags = file_obj.tags or []
                    except File.DoesNotExist:
                        file_id = ''
                        tags = []
                    
                    results.append({
                        'id': file_id,
                        'name': filename,
                        'path': rel_path,  # For navigation
                        'url': file_url,   # For download/preview
                        'tags': tags,
                        'is_dir': False,
                        'parent_path': parent_path  # For navigation
                    })
                    continue
                
                # Check content match for supported file types
                _, ext = os.path.splitext(filename)
                if ext.lower() in self.SUPPORTED_EXTENSIONS:
                    try:
                        file_path = os.path.join(root, filename)
                        content = self._read_file_content(file_path, ext.lower())
                        if content and query in content.lower():
                            rel_path = os.path.relpath(file_path, base_path)
                            file_url = f'{settings.MEDIA_URL}uploads/{rel_path}'
                            parent_path = os.path.dirname(rel_path)
                            
                            # Get file object if it exists
                            try:
                                file_obj = File.objects.get(path=f'uploads/{rel_path}')
                                file_id = str(file_obj.id)
                                tags = file_obj.tags or []
                            except File.DoesNotExist:
                                file_id = ''
                                tags = []
                            
                            results.append({
                                'id': file_id,
                                'name': filename,
                                'path': rel_path,  # For navigation
                                'url': file_url,   # For download/preview
                                'tags': tags,
                                'is_dir': False,
                                'parent_path': parent_path  # For navigation
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
