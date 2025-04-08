"""
User profile management views for the CMS application.

This module defines views for user profile management:
- ProfileView: Display user profile details
- ProfileUpdateView: Edit user profile information
- EnhancedPasswordChangeView: Change user password with enhanced UI
- UserActivityView: Display user's recent activities
"""

import logging
from django.views.generic import DetailView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Q, Count, Sum
from django.db import transaction
from django.http import Http404
from django.contrib.auth.models import User

from ..models.users import UserProfile
from ..models.documents import Document, DocumentVersion
from ..models.files import File
from ..forms.user_forms import UserProfileForm, EnhancedPasswordChangeForm

logger = logging.getLogger(__name__)


class ProfileView(LoginRequiredMixin, DetailView):
    """View for displaying the user's profile."""
    model = UserProfile
    template_name = 'cms/profile.html'  # Using existing template
    context_object_name = 'profile'
    
    def get_object(self, queryset=None):
        """Get the current user's profile."""
        try:
            return self.request.user.profile
        except UserProfile.DoesNotExist:
            logger.error(f"Profile does not exist for user {self.request.user.username}")
            # Create a profile if it doesn't exist (fallback)
            return UserProfile.objects.create(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        """Add user activity data to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'User Profile'
        user = self.request.user
        
        # Get user's documents with optimized query
        context['user_documents'] = Document.objects.filter(
            author=user
        ).select_related('category').prefetch_related('tags').order_by('-created_at')[:5]
        
        # Get user's files with optimized query
        context['user_files'] = File.objects.filter(
            uploaded_by=user
        ).select_related('category').prefetch_related('tags').order_by('-uploaded_at')[:5]
        
        # Get user storage statistics
        storage_stats = File.objects.filter(uploaded_by=user).aggregate(
            total_files=Count('id'),
            total_size=Sum('file_size')
        )
        context['total_files'] = storage_stats['total_files'] or 0
        context['total_storage'] = storage_stats['total_size'] or 0
        
        return context


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View for updating user profile information."""
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'cms/profile_edit.html'
    success_url = reverse_lazy('cms:profile')
    
    def test_func(self):
        """Ensure users can only edit their own profile."""
        profile = self.get_object()
        return self.request.user == profile.user
    
    def get_object(self, queryset=None):
        """Get the current user's profile."""
        try:
            return self.request.user.profile
        except UserProfile.DoesNotExist:
            logger.error(f"Profile does not exist for user {self.request.user.username}")
            raise Http404("Profile not found")
    
    def get_context_data(self, **kwargs):
        """Add additional context data."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Profile'
        return context
    
    @transaction.atomic
    def form_valid(self, form):
        """Process valid form data with transaction support."""
        try:
            response = super().form_valid(form)
            
            # Log profile update
            logger.info(f"User profile updated: {self.request.user.username}")
            messages.success(self.request, 'Your profile has been updated successfully.')
            
            return response
        except Exception as e:
            logger.error(f"Error updating profile for {self.request.user.username}: {str(e)}")
            messages.error(self.request, f"An error occurred while updating your profile: {str(e)}")
            transaction.set_rollback(True)
            return self.form_invalid(form)


class EnhancedPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """Enhanced password change view with improved template and error handling."""
    form_class = EnhancedPasswordChangeForm
    template_name = 'cms/password_change.html'
    success_url = reverse_lazy('cms:profile')
    
    def get_context_data(self, **kwargs):
        """Add additional context data."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Change Password'
        return context
    
    def form_valid(self, form):
        """Process valid form data."""
        try:
            response = super().form_valid(form)
            
            # Log password change
            logger.info(f"Password changed for user: {self.request.user.username}")
            messages.success(self.request, 'Your password has been changed successfully.')
            
            return response
        except Exception as e:
            logger.error(f"Error changing password for {self.request.user.username}: {str(e)}")
            messages.error(self.request, f"An error occurred: {str(e)}")
            return self.form_invalid(form)


class UserActivityView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """View for displaying user's recent activities."""
    template_name = 'cms/user_activity.html'
    
    def test_func(self):
        """Ensure users can only view their own activity."""
        user_id = self.kwargs.get('user_id')
        if user_id:
            return self.request.user.id == int(user_id) or self.request.user.is_staff
        return True
    
    def get_context_data(self, **kwargs):
        """Add user activity data to context with optimized queries."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Your Activity'
        
        # Determine which user's activity to show
        user_id = self.kwargs.get('user_id')
        if user_id and self.request.user.is_staff:
            user = get_object_or_404(User, id=user_id)
        else:
            user = self.request.user
        
        context['activity_user'] = user
        
        # Get user's documents with optimized queries
        context['documents'] = Document.objects.filter(
            author=user
        ).select_related('category', 'author').prefetch_related('tags').order_by('-created_at')[:10]
        
        # Get user's files with optimized queries
        context['files'] = File.objects.filter(
            uploaded_by=user
        ).select_related('category').prefetch_related('tags').order_by('-uploaded_at')[:10]
        
        # Get recent document versions with optimized queries
        context['versions'] = DocumentVersion.objects.filter(
            created_by=user
        ).select_related('document', 'created_by').order_by('-created_at')[:10]
        
        return context
