from django.urls import path

from . import views

app_name = "devices"

urlpatterns = [
    path("device/create/", views.create, name="create"),
    path("device/edit/<str:short_name>/", views.edit, name="edit"),
    path("device/delete/<str:short_name>/", views.delete, name="delete"),
    path("device/<str:short_name>/", views.device, name="device"),
    path("", views.devices, name="devices"),
]