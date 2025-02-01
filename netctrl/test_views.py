"""Test views for NetCtrl components."""

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def dark_theme_components(request):
    """Test components in dark theme."""
    return render(request, "test/dark_theme.html", {"dark_theme": True})


@require_http_methods(["GET"])
def alert_component(request):
    """Test alert component."""
    return render(
        request,
        "test/alert.html",
        {
            "alert_type": request.GET.get("type", "success"),
            "message": "Test alert message",
        },
    )


@require_http_methods(["GET"])
def loading_component(request):
    """Test loading component."""
    return render(request, "test/loading.html")


@require_http_methods(["GET"])
def mobile_responsive(request):
    """Test mobile responsive layout."""
    return render(request, "test/mobile.html")


@require_http_methods(["GET"])
def button_component(request):
    """Test button component."""
    return render(request, "test/buttons.html")


@require_http_methods(["GET"])
def card_component(request):
    """Test card component."""
    return render(request, "test/card.html")


@require_http_methods(["GET"])
def form_component(request):
    """Test form component."""
    return render(request, "test/form.html")


@require_http_methods(["GET"])
def all_components(request):
    """Test all components together."""
    return render(request, "test/components.html")
