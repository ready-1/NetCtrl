from django.urls import path
from .views import (
    SwitchListView, SwitchDetailView, 
    SwitchCreateView, SwitchUpdateView, SwitchDeleteView, 
    RefreshSwitchInfoView
)

app_name = "net_frontend"

urlpatterns = [
    path("", SwitchListView.as_view(), name="switch_list"),
    path("<int:pk>/", SwitchDetailView.as_view(), name="switch_detail"),
    path("create/", SwitchCreateView.as_view(), name="switch_create"),
    path("<int:pk>/edit/", SwitchUpdateView.as_view(), name="switch_update"),
    path("<int:pk>/delete/", SwitchDeleteView.as_view(), name="switch_delete"),
    path('switch/<int:pk>/refresh/', RefreshSwitchInfoView.as_view(), name='refresh_switch'),
]