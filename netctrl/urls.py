from django.urls import path, include
from . import views

app_name = "netctrl"

urlpatterns = [
    path("", views.dashboard, name="home"),  # Make dashboard the home page
    path("dashboard/", views.dashboard, name="dashboard"),
    path("switches/", views.switch_list, name="switch-list"),
    path("switches/<int:pk>/", views.switch_detail, name="switch-detail"),
    path("switches/<int:pk>/config/", views.switch_config, name="switch-config"),
    path("switches/<int:pk>/ports/", views.switch_ports, name="switch-ports"),
    path("switches/<int:pk>/backup/", views.switch_backup, name="switch-backup"),
    path("audit-logs/", views.audit_logs, name="audit-logs"),
    path("tests/", include("netctrl.tests.urls")),  # Include test URLs under /tests/
]
