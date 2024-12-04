from django.contrib.auth import views as auth_views
from django.urls import path
from .views import pending_approvals, approve_user, SignUpView

app_name = 'accounts'

urlpatterns = [
    path('pending-approvals/', pending_approvals, name='pending_approvals'),
    path('approve-user/<int:user_id>/', approve_user, name='approve_user'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]