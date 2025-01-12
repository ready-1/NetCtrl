"""
URL patterns for the netdash app.
"""
from django.urls import path
from . import views

app_name = 'netdash'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('pending-approval/', views.pending_approval_view, name='pending_approval'),
    path('user-approvals/', views.user_approval_list, name='user_approval_list'),
    path('approve-user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('reject-user/<int:user_id>/', views.reject_user, name='reject_user'),
]
