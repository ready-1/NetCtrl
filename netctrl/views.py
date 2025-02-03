from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import SwitchForm, TestForm
from .models import Switch
from asgiref.sync import sync_to_async


def home(request):
    """Home page view."""
    return render(request, "home.html")


@login_required
def dashboard(request):
    """Dashboard view showing switch status overview."""
    return render(request, "dashboard.html")


@login_required
def switch_list(request):
    """List all managed switches."""
    switches = Switch.objects.all()
    return render(request, "switches/list.html", {"switches": switches})


@sync_to_async
def create_switch(data):
    switch = Switch.objects.create(**data)
    return switch


@login_required
def switch_add(request):
    if request.method == "POST":
        form = SwitchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            switch = create_switch(data)
            return redirect("netctrl:switch-list")
        return JsonResponse({"errors": form.errors}, status=400)
    return render(request, "switch/add.html")


@login_required
def switch_detail(request, switch_id):
    """Show detailed information for a specific switch."""
    switch = Switch.objects.get(pk=switch_id)
    return render(request, "switch/detail.html", {"switch": switch})


@login_required
def switch_edit(request, switch_id):
    switch = Switch.objects.get(pk=switch_id)
    if request.method == "POST":
        form = SwitchForm(request.POST, instance=switch)
        if form.is_valid():
            form.save()
            return redirect("netctrl:switch-detail", switch_id=switch_id)
        return JsonResponse({"errors": form.errors}, status=400)
    return render(request, "switch/edit.html", {"switch": switch})


@login_required
def switch_delete(request, switch_id):
    switch = Switch.objects.get(pk=switch_id)
    switch.delete()
    return redirect("netctrl:switch-list")


@login_required
def switch_stats(request, switch_id):
    switch = Switch.objects.get(pk=switch_id)
    return render(request, "switch/stats_partial.html", {"switch": switch})


@login_required
def switch_config(request, pk):
    """Show and edit switch configuration."""
    return render(request, "switch/config.html")


@login_required
def switch_ports(request, pk):
    """Show and manage switch ports."""
    return render(request, "switch/ports.html")


@login_required
def switch_backup(request, pk):
    """Manage switch configuration backups."""
    return render(request, "switch/backup.html")


@login_required
def audit_logs(request):
    """Show system audit logs."""
    return render(request, "audit_logs.html")


@require_http_methods(["GET", "POST"])
def test_alert(request):
    if request.method == "POST":
        if "error" in request.POST:
            alert_html = render_to_string(
                "components/alert.html",
                {"type": "danger", "message": "Test error message"},
            )
            return HttpResponse(alert_html)
        alert_html = render_to_string(
            "components/alert.html",
            {"type": "success", "message": "Operation completed successfully"},
        )
        return HttpResponse(alert_html)
    return render(request, "test/alert.html")


def test_button(request):
    return render(request, "test/button.html")


def test_card(request):
    return render(request, "test/card.html")


def test_chart(request):
    return render(request, "test/chart.html")


def test_dark_theme(request):
    return render(request, "test/dark_theme.html")


def test_form(request):
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            return render(
                request,
                "components/alert.html",
                {"type": "success", "message": "Form submitted successfully"},
            )
        return JsonResponse({"errors": form.errors}, status=400)
    return render(request, "test/form.html")


def test_loading(request):
    return render(request, "test/loading.html")


def test_network_failure(request):
    if request.method == "POST":
        content = request.body.decode("utf-8")
        if len(content) > 1024 * 1024:  # 1MB limit
            return HttpResponseBadRequest("Request too large")
        return render(request, "test/network_failure.html")
    return render(request, "test/network_failure.html")
