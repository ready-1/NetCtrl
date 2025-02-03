from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

app_name = "authentication"

urlpatterns = [
    # Web interface authentication
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("settings/", views.SettingsView.as_view(), name="settings"),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="authentication/password_change.html",
            success_url="/auth/password_change/done/",
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="authentication/password_change_done.html"
        ),
        name="password_change_done",
    ),
    # API token authentication
    path("api/token/", views.TokenObtainView.as_view(), name="token_obtain"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/revoke/", views.TokenRevokeView.as_view(), name="token_revoke"),
]
