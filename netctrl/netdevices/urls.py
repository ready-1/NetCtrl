"""
URL patterns for the device management app.
"""
from django.urls import path
from . import views

app_name = 'netdevices'

urlpatterns = [
    path('', views.DeviceListView.as_view(), name='index'),
]
