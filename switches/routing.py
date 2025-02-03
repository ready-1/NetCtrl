"""WebSocket URL configuration for the switches app."""

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/switches/status/$", consumers.SwitchStatusConsumer.as_asgi()),
]
