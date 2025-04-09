"""
Forms for taxonomy management (tags and categories).

This module defines forms for creating and editing taxonomy entities:
- TagForm: For tag creation and editing
- CategoryForm: For category creation and editing with hierarchy support
"""

from django import forms
from django.utils.text import slugify
from ..models.documents import Tag, Category


class BootstrapFormMixin:
    """Add Bootstrap 5 classes to form fields."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ == 'CheckboxInput':
                field.widget.attrs['class'] = 'form-check-input'
            elif field.widget.__class__.__name__ in ['RadioSelect', 'CheckboxSelectMultiple']:
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
                if field.required:
                    field.widget.attrs['required'] = 'required'


class TagForm(BootstrapFormMixin, forms.ModelForm):
    """
    Form for tag creation and editing with validation.
    
    Features:
    - Auto-generation of slug from name if not provided
    - Validation of slug uniqueness
    - Bootstrap styling
    """
    
    class Meta:
        model = Tag
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Tag name'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Leave empty to auto-generate'})
        }
        help_texts = {
            'slug': 'URL-friendly version of the name. Leave empty to auto-generate.'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].required = False
    
    def clean_slug(self):
        """Validate slug uniqueness while allowing unchanged slug during edit."""
        slug = self.cleaned_data.get('slug')
        name = self.cleaned_data.get('name')
        
        # If slug is not provided, generate from name (will be auto-saved in model)
        if not slug and name:
            slug = slugify(name)
        
        # Skip validation if editing and slug hasn't changed
        if self.instance.pk and self.instance.slug == slug:
            return slug
        
        # Check uniqueness
        if slug and Tag.objects.filter(slug=slug).exists():
            raise forms.ValidationError("This slug is already in use. Please choose a different one.")
        
        return slug


class CategoryForm(BootstrapFormMixin, forms.ModelForm):
    """
    Form for category creation and editing with validation.
    
    Features:
    - Auto-generation of slug from name if not provided
    - Validation of slug uniqueness
    - Prevention of circular parent references
    - Bootstrap styling
    """
    
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'parent']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Category name'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Leave empty to auto-generate'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional description'}),
            'parent': forms.Select(attrs={'class': 'form-select'})
        }
        help_texts = {
            'slug': 'URL-friendly version of the name. Leave empty to auto-generate.',
            'parent': 'Optional parent category for hierarchical organization.'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].required = False
        self.fields['description'].required = False
        
        # Exclude self and descendants from parent choices to prevent circular references
        if self.instance.pk:
            # First get all descendants
            descendants = self._get_descendants(self.instance)
            
            # Exclude self and descendants from parent choices
            excluded_ids = [self.instance.pk] + [d.pk for d in descendants]
            self.fields['parent'].queryset = Category.objects.exclude(pk__in=excluded_ids)
    
    def _get_descendants(self, category):
        """Recursively get all descendants of a category."""
        descendants = []
        for child in category.children.all():
            descendants.append(child)
            descendants.extend(self._get_descendants(child))
        return descendants
    
    def clean_slug(self):
        """Validate slug uniqueness while allowing unchanged slug during edit."""
        slug = self.cleaned_data.get('slug')
        name = self.cleaned_data.get('name')
        
        # If slug is not provided, generate from name (will be auto-saved in model)
        if not slug and name:
            slug = slugify(name)
        
        # Skip validation if editing and slug hasn't changed
        if self.instance.pk and self.instance.slug == slug:
            return slug
        
        # Check uniqueness
        if slug and Category.objects.filter(slug=slug).exists():
            raise forms.ValidationError("This slug is already in use. Please choose a different one.")
        
        return slug
    
    def clean(self):
        """Validate that parent is not set to self or descendant."""
        cleaned_data = super().clean()
        parent = cleaned_data.get('parent')
        
        # If instance exists and parent is set to a descendant, raise validation error
        if self.instance.pk and parent and self._is_descendant(parent, self.instance):
            self.add_error('parent', "Cannot set a category's parent to itself or one of its descendants.")
        
        return cleaned_data
    
    def _is_descendant(self, potential_descendant, category):
        """Check if potential_descendant is a descendant of category."""
        if potential_descendant == category:
            return True
        
        if potential_descendant.parent:
            if potential_descendant.parent == category:
                return True
            return self._is_descendant(potential_descendant.parent, category)
        
        return False
