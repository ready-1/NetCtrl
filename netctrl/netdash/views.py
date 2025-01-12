"""
Views for the netdash app.
"""
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import UserRegistrationForm

User = get_user_model()


class DashboardView(LoginRequiredMixin, TemplateView):
    """Main dashboard view."""
    
    template_name = 'netdash/index.html'


class RegisterView(CreateView):
    """User registration view."""
    
    template_name = 'netdash/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('netdash:pending_approval')


@login_required
def pending_approval_view(request):
    """View shown to users awaiting approval."""
    if request.user.is_approved:
        return redirect('netdash:index')
    return render(request, 'netdash/pending_approval.html')


@user_passes_test(lambda u: u.is_staff)
def user_approval_list(request):
    """List of users pending approval."""
    pending_users = User.objects.filter(is_approved=False)
    return render(request, 'netdash/user_approval_list.html', {
        'pending_users': pending_users
    })


@user_passes_test(lambda u: u.is_staff)
def approve_user(request, user_id):
    """Approve a user."""
    if request.method == 'POST':
        try:
            user = User.objects.get(id=user_id, is_approved=False)
            user.is_approved = True
            user.approval_date = timezone.now()
            user.save()
            messages.success(request, f'User {user.username} has been approved.')
        except User.DoesNotExist:
            messages.error(request, 'User not found or already approved.')
    return redirect('netdash:user_approval_list')


@user_passes_test(lambda u: u.is_staff)
def reject_user(request, user_id):
    """Reject and delete a user."""
    if request.method == 'POST':
        try:
            user = User.objects.get(id=user_id, is_approved=False)
            username = user.username
            user.delete()
            messages.success(request, f'User {username} has been rejected and deleted.')
        except User.DoesNotExist:
            messages.error(request, 'User not found.')
    return redirect('netdash:user_approval_list')
