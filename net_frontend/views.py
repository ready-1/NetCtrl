from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from net_core.models import Switch
from net_frontend.forms import SwitchForm

class SwitchListView(ListView):
    model = Switch
    template_name = "net_frontend/switch_list.html"
    context_object_name = "switches"

class SwitchDetailView(DetailView):
    model = Switch
    template_name = "net_frontend/switch_detail.html"
    context_object_name = "switch"

class SwitchCreateView(CreateView):
    model = Switch
    form_class = SwitchForm
    template_name = "net_frontend/switch_form.html"
    success_url = reverse_lazy("net_frontend:switch_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Create"
        return context

class SwitchUpdateView(UpdateView):
    model = Switch
    form_class = SwitchForm
    template_name = "net_frontend/switch_form.html"
    success_url = reverse_lazy("net_frontend:switch_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Update"
        return context

class SwitchDeleteView(DeleteView):
    model = Switch
    template_name = "net_frontend/switch_confirm_delete.html"
    success_url = reverse_lazy("net_frontend:switch_list")