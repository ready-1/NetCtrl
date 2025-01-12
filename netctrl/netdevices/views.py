"""
Views for the device management app.
"""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DeviceListView(LoginRequiredMixin, TemplateView):
    """View for listing network devices."""
    
    template_name = 'netdevices/index.html'
    
    def get_context_data(self, **kwargs):
        """Add device list to context."""
        context = super().get_context_data(**kwargs)
        # Will be implemented to fetch devices from M4300 API
        return context
