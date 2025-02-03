from django.urls import path
from . import views

app_name = "styleguide"

urlpatterns = [
    path("", views.styleguide, name="index"),
    path("components/", views.components, name="components"),
    path("forms/", views.forms, name="forms"),
    path("charts/", views.charts, name="charts"),
    path("dark-theme/", views.dark_theme, name="dark_theme"),
]
