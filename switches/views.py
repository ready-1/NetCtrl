"""API views for the switches app."""

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Switch, Port
from .serializers import (
    UserSerializer,
    SwitchSerializer,
    PortSerializer,
)
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
@api_view(["GET"])
def switch_status(request):
    """API endpoint for getting switch status."""
    switches = Switch.objects.all()
    data = []
    for switch in switches:
        data.append(
            {
                "id": switch.pk,
                "name": switch.name,
                "status": switch.status,
                "in_band_status": switch.in_band_status,
                "out_band_status": switch.out_band_status,
                "in_band_last_seen": (
                    switch.in_band_last_seen.isoformat()
                    if switch.in_band_last_seen
                    else None
                ),
                "out_band_last_seen": (
                    switch.out_band_last_seen.isoformat()
                    if switch.out_band_last_seen
                    else None
                ),
                "in_band_error": switch.in_band_error,
                "out_band_error": switch.out_band_error,
                "in_band_error_detail": switch.in_band_error_detail,
                "out_band_error_detail": switch.out_band_error_detail,
                "in_band_response_time": switch.in_band_response_time,
                "out_band_response_time": switch.out_band_response_time,
                "status_details": switch.status_details,
            }
        )
    return Response(data)


class SwitchListView(LoginRequiredMixin, ListView):
    """View for listing switches."""

    model = Switch
    template_name = "switches/list.html"
    context_object_name = "switches"

    def get_context_data(self, **kwargs):
        """Add extra context data."""
        context = super().get_context_data(**kwargs)
        for switch in context["switches"]:
            if not hasattr(switch, "status_details"):
                switch.status_details = {"history": []}
        return context


class SwitchCreateView(LoginRequiredMixin, CreateView):
    """View for creating a new switch."""

    model = Switch
    template_name = "switches/switch_form.html"
    fields = ["name", "in_band_ip", "out_band_ip", "username", "password"]
    success_url = reverse_lazy("switches:switch-list")


class SwitchUpdateView(LoginRequiredMixin, UpdateView):
    """View for updating an existing switch."""

    model = Switch
    template_name = "switches/switch_form.html"
    fields = ["name", "in_band_ip", "out_band_ip", "username", "password"]
    success_url = reverse_lazy("switches:switch-list")


class SwitchDetailView(LoginRequiredMixin, DetailView):
    """View for viewing switch details."""

    model = Switch
    template_name = "switches/switch_detail.html"


class SwitchDeleteView(LoginRequiredMixin, DeleteView):
    """View for deleting a switch."""

    model = Switch
    template_name = "switches/switch_confirm_delete.html"
    success_url = reverse_lazy("switches:switch-list")
