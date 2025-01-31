from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

app_name = "authentication"

urlpatterns = [
    # Web interface authentication
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # API token authentication
    path("api/token/", views.TokenObtainView.as_view(), name="token_obtain"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/revoke/", views.TokenRevokeView.as_view(), name="token_revoke"),
]
