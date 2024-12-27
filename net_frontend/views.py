from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.conf import settings

from net_core.models import Switch
from net_frontend.forms import SwitchForm
from net_core.api_helpers import make_api_request, fetch_device_info, fetch_device_name



class SwitchListView(ListView):
    model = Switch
    template_name = "net_frontend/switch_list.html"
    context_object_name = "switches"

class SwitchDetailView(DetailView):
    model = Switch
    template_name = "net_frontend/switch_detail.html"
    context_object_name = "switch"

class SwitchCreateView(PermissionRequiredMixin, CreateView):
    model = Switch
    form_class = SwitchForm
    template_name = "net_frontend/switch_form.html"
    success_url = reverse_lazy("net_frontend:switch_list")
    permission_required = "net_core.add_switch"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Create"
        return context

class SwitchUpdateView(PermissionRequiredMixin,UpdateView):
    model = Switch
    form_class = SwitchForm
    template_name = "net_frontend/switch_form.html"
    success_url = reverse_lazy("net_frontend:switch_list")
    permission_required = "net_core.change_switch"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Update"
        return context

class SwitchDeleteView(PermissionRequiredMixin,DeleteView):
    model = Switch
    template_name = "net_frontend/switch_confirm_delete.html"
    success_url = reverse_lazy("net_frontend:switch_list")
    permission_required = "net_core.delete_switch"

class RefreshSwitchInfoView(View):
    def post(self, request, pk):
        switch = get_object_or_404(Switch, pk=pk)

        try:
            # Fetch and update device info
            device_info = fetch_device_info(switch.ip_address_in_band)
            switch.serial_number = device_info.get("serialNumber", switch.serial_number)
            switch.mac_address = device_info.get("macAddr", switch.mac_address)
            switch.model = device_info.get("model", switch.model)
            switch.firmware_version = device_info.get("swVer", switch.firmware_version)
            switch.port_count = device_info.get("numOfPorts", switch.port_count)

            # Fetch and update device name
            device_name = fetch_device_name(switch.ip_address_in_band)
            switch.name = device_name.get("name", switch.name)
            switch.location = device_name.get("location", switch.location)

            # Save updated switch
            switch.save()

            messages.success(request, "Switch information successfully refreshed.")
        except Exception as e:
            messages.error(request, f"Failed to refresh switch information: {str(e)}")

        return redirect('net_frontend:switch_detail', pk=switch.pk)