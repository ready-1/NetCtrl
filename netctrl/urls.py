from django.urls import path
from . import views

app_name = "netctrl"

urlpatterns = [
    path("", views.home, name="home"),
    path("switches/", views.switch_list, name="switch-list"),
    path("switches/add/", views.switch_add, name="switch-add"),
    path("switches/<int:pk>/", views.switch_detail, name="switch-detail"),
    path("switches/<int:pk>/edit/", views.switch_edit, name="switch-edit"),
    path("switches/<int:pk>/delete/", views.switch_delete, name="switch-delete"),
    path("test/alert/", views.test_alert, name="test-alert"),
    path("test/button/", views.test_button, name="test-button"),
    path("test/form/", views.test_form, name="test-form"),
    path("test/loading/", views.test_loading, name="test-loading"),
    path(
        "test/network-failure/", views.test_network_failure, name="test-network-failure"
    ),
    path("test/chart/", views.test_chart, name="test-chart"),
]
