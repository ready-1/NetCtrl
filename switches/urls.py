"""URL configuration for the switches app."""

from django.urls import path, re_path
from . import views

app_name = "switches"

urlpatterns = [
    # API endpoints
    path(
        "api/status/", views.switch_status, name="switch-status"
    ),  # Changed to api/status
    # Web interface URLs
    path("", views.SwitchListView.as_view(), name="switch-list"),
    path("add/", views.SwitchCreateView.as_view(), name="switch-add"),
    path("<int:pk>/edit/", views.SwitchUpdateView.as_view(), name="switch-edit"),
    path("<int:pk>/delete/", views.SwitchDeleteView.as_view(), name="switch-delete"),
    path("<int:pk>/", views.SwitchDetailView.as_view(), name="switch-detail"),
]
