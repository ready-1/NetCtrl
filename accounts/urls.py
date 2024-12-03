from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('pending-approvals/', views.pending_approvals, name='pending_approvals'),
    path('approve-user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('signup/', views.SignUpView.as_view(), name='register'),
]