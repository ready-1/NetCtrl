from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CustomUser
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.views import View
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm



class TestView(View):
    def get(self, request):
        messages.success(request, "Test flash message.")
        return render(request, 'test.html')

# Check if the user is an approver
def is_approver(user):
    return user.is_authenticated and user.notify_on_approval


@login_required
def user_approvals(request):
    if not request.user.is_staff:
        return redirect('home')  # Restrict access to staff

    pending_users = CustomUser.objects.filter(is_active=False)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')
        user = CustomUser.objects.get(id=user_id)
        if action == 'approve':
            user.is_active = True
            user.save()

    return render(request, 'user_approvals.html', {'pending_users': pending_users})


@login_required
@user_passes_test(is_approver)
def pending_approvals(request):
    pending_users = CustomUser.objects.filter(is_active=False)
    return render(request, 'accounts/pending_approvals.html', {'pending_users': pending_users})

@login_required
@user_passes_test(is_approver)
def approve_user(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id, is_active=False)
        user.is_active = True
        user.save()
        messages.success(request, f"User {user.username} has been approved.")
    except CustomUser.DoesNotExist:
        messages.error(request, "User not found or already approved.")
    return redirect('accounts:pending_approvals')



class SignUpView(CreateView):
    template_name = "accounts/signup.html"  # Template for the signup page
    form_class = CustomUserCreationForm  # Form class for signup
    success_url = reverse_lazy("login")  # Redirect after successful signup

    def form_valid(self, form):
        print("form_valid executed")  # Debugging
        response = super().form_valid(form)

        # Notify admins about the new user
        user = self.object  # Newly created user instance
        admin_users = CustomUser.objects.filter(is_staff=True, notify_on_approval=True)
        for admin in admin_users:
            print(f"Adding flash message for admin: {admin.username}")  # Debugging
            link = reverse('admin:accounts_customuser_change', args=[user.id])
            messages.success(
                self.request,
                f"New user '{user.username}' created and is pending approval. "
                f"<a href='{link}'>Approve now</a>",
                extra_tags='safe',  # Allow HTML in the message
            )
        return response
