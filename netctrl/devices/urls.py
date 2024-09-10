from django.urls import path

from . import views

app_name = "devices"

urlpatterns = [
    path("", views.devices, name="devices"),
    path("device/<str:short_name>/", views.device, name="device"),
]