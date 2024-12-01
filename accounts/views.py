from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser

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