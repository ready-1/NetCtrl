"""URL configuration for the switches app."""

from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

app_name = "switches"

urlpatterns = [
    # Web interface URLs
    path("", views.SwitchListView.as_view(), name="switch-list"),
    path("add/", views.SwitchCreateView.as_view(), name="switch-add"),
    path("<int:pk>/edit/", views.SwitchUpdateView.as_view(), name="switch-edit"),
    path("<int:pk>/delete/", views.SwitchDeleteView.as_view(), name="switch-delete"),
    path("<int:pk>/", views.SwitchDetailView.as_view(), name="switch-detail"),
    # Authentication endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # API URLs
    path("api/users/me/", views.UserDetailView.as_view(), name="user-detail"),
    path(
        "api/switches/", views.SwitchListCreateView.as_view(), name="switch-list-create"
    ),
    path(
        "api/switches/<int:pk>/", views.SwitchDetailView.as_view(), name="switch-detail"
    ),
    path(
        "api/switches/<int:switch_id>/ports/",
        views.PortListView.as_view(),
        name="port-list",
    ),
    re_path(
        r"^api/switches/(?P<switch_id>\d+)/ports/(?P<n>[\w/]+)/$",
        views.PortDetailView.as_view(),
        name="port-detail",
    ),
]
