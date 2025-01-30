"""URL configuration for the switches app."""

from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

app_name = "api"

urlpatterns = [
    # Authentication endpoints
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # User endpoints
    path("user/", views.UserDetailView.as_view(), name="user-detail"),
    # Switch endpoints
    path("switches/", views.SwitchListCreateView.as_view(), name="switch-list"),
    path("switches/<int:pk>/", views.SwitchDetailView.as_view(), name="switch-detail"),
    # Port endpoints
    path(
        "switches/<int:switch_id>/ports/",
        views.PortListView.as_view(),
        name="port-list",
    ),
    re_path(
        r"^switches/(?P<switch_id>\d+)/ports/(?P<n>[\w/]+)/$",
        views.PortDetailView.as_view(),
        name="port-detail",
    ),
]
