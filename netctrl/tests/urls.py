"""URL patterns for test views."""

from django.urls import path
from . import views

app_name = "tests"

urlpatterns = [
    path("dark-theme/", views.dark_theme_components, name="test-dark-theme"),
    path("alert/", views.alert_component, name="test-alert"),
    path("loading/", views.loading_component, name="test-loading"),
    path("mobile/", views.mobile_responsive, name="test-mobile"),
    path("button/", views.button_component, name="test-button"),
    path("card/", views.card_component, name="test-card"),
    path("form/", views.form_component, name="test-form"),
    path("all/", views.all_components, name="test-all"),
]
