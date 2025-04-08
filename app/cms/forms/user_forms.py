"""
User management forms for the CMS application.

This module defines forms for user profile management:
- UserProfileForm: Form for updating user profile information
- EnhancedPasswordChangeForm: Improved password change form with styling and validation
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.core.validators import FileExtensionValidator
from ..models.users import UserProfile


class UserProfileForm(forms.ModelForm):
    """Form for updating user profile information."""
    
    first_name = forms.CharField(
        max_length=30, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'dark_mode']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'dark_mode': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        """Initialize form with user data."""
        super().__init__(*args, **kwargs)
        
        # Set initial values from user model
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email
            
        # Add validators to ensure security and data integrity
        self.fields['profile_picture'].validators.append(
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png', 'gif'],
                message="Only image files (jpg, jpeg, png, gif) are allowed."
            )
        )
    
    def clean_email(self):
        """Validate that the email is unique."""
        email = self.cleaned_data.get('email')
        user_id = self.instance.user.id if self.instance and self.instance.user else None
        
        if email and User.objects.filter(email=email).exclude(id=user_id).exists():
            raise forms.ValidationError("This email is already in use by another account.")
        
        return email
    
    def save(self, commit=True):
        """Save both the profile and user model fields."""
        profile = super().save(commit=False)
        
        # Save associated User fields
        if profile.user:
            profile.user.first_name = self.cleaned_data['first_name']
            profile.user.last_name = self.cleaned_data['last_name']
            profile.user.email = self.cleaned_data['email']
            
            if commit:
                profile.user.save()
        
        if commit:
            profile.save()
            
        return profile


class EnhancedPasswordChangeForm(PasswordChangeForm):
    """Enhanced password change form with Bootstrap styling and additional validation."""
    
    def __init__(self, *args, **kwargs):
        """Initialize form with Bootstrap styling."""
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'new-password' if 'new_password' in field_name else 'current-password'
            })
    
    def clean_new_password2(self):
        """Add additional validation for new password."""
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')
        
        # First perform the standard validation
        password2 = super().clean_new_password2()
        
        # Check if new password is different from the old one
        if old_password and new_password1 and old_password == new_password1:
            raise forms.ValidationError(
                "Your new password must be different from your current password."
            )
        
        return password2
