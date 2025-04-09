"""
Form modules for the NetCtrl CMS application.

This package contains all form modules for the CMS application:
- user_forms.py: Forms for user profile management
"""

from .user_forms import UserProfileForm, EnhancedPasswordChangeForm
# Expose the document form classes directly
import sys
from django import forms
from django.core.exceptions import ValidationError
from ..models.documents import Document, DocumentVersion, Category, Tag
from ..models.files import File

# Document form classes
class DocumentVersionForm(forms.Form):
    """Form for creating a new document version with changelog."""
    
    changelog = forms.CharField(
        label="Change Description",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'form-control',
            'placeholder': 'Describe the changes made in this version...'
        }),
        required=True,
        help_text="Please provide a description of the changes in this version."
    )


class DocumentFileForm(forms.Form):
    """Form for selecting and attaching files to a document."""
    
    files = forms.MultipleChoiceField(
        label="Select Files",
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text="Select one or more files to attach to this document."
    )
    
    def __init__(self, *args, available_files=None, **kwargs):
        """Initialize the form with available files."""
        super().__init__(*args, **kwargs)
        
        # Set choices from available files
        if available_files is not None:
            self.fields['files'].choices = [
                (str(f.id), f.name) for f in available_files
            ]
    
    def clean_files(self):
        """Ensure selected file IDs are valid integers."""
        file_ids = self.cleaned_data.get('files', [])
        
        # Convert to integers
        try:
            return [int(file_id) for file_id in file_ids]
        except (ValueError, TypeError):
            raise ValidationError("Invalid file ID format.")


class DocumentFilterForm(forms.Form):
    """Form for filtering documents in the list view."""
    
    q = forms.CharField(
        label="Search",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search documents...'
        })
    )
    
    category_id = forms.ChoiceField(
        label="Category",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    tag_id = forms.ChoiceField(
        label="Tag",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    status = forms.ChoiceField(
        label="Status",
        required=False,
        choices=[('', 'All'), ('draft', 'Draft'), ('published', 'Published')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    def __init__(self, *args, **kwargs):
        """Initialize form with dynamic category and tag choices."""
        super().__init__(*args, **kwargs)
        
        # Set category choices
        category_choices = [('', 'All Categories')]
        category_choices.extend(
            [(str(c.id), c.name) for c in Category.objects.all()]
        )
        self.fields['category_id'].choices = category_choices
        
        # Set tag choices
        tag_choices = [('', 'All Tags')]
        tag_choices.extend(
            [(str(t.id), t.name) for t in Tag.objects.all()]
        )
        self.fields['tag_id'].choices = tag_choices

__all__ = [
    'UserProfileForm',
    'EnhancedPasswordChangeForm',
    'DocumentVersionForm',
    'DocumentFileForm',
    'DocumentFilterForm',
]
