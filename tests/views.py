from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError


@require_http_methods(["GET"])
def test_alert(request):
    """Test alert component."""
    return render(
        request,
        "test/alert.html",
        {"type": "success", "message": "This is a success alert"},
    )


@require_http_methods(["GET"])
def test_buttons(request):
    """Test button states."""
    return render(request, "test/buttons.html")


@require_http_methods(["GET"])
def test_card(request):
    """Test card component."""
    return render(request, "test/card.html")


@require_http_methods(["GET"])
def test_loading(request):
    """Test loading indicator."""
    return render(request, "test/loading.html")


@require_http_methods(["GET", "POST"])
def test_form(request):
    """Test form validation."""
    if request.method == "POST":
        if not request.POST.get("name"):
            return HttpResponse("Name is required", status=400)
        return HttpResponse("Success")
    return render(request, "test/form.html")


@require_http_methods(["GET"])
def test_components(request):
    """Test all components together."""
    return render(request, "test/components.html")


@require_http_methods(["GET", "POST"])
def test_network_failure(request):
    """Test network failure handling."""
    if request.method == "POST":
        content = request.POST.get("name", "")
        if len(content) > 1000:
            return HttpResponse("Request too large", status=400)
        return HttpResponse("Success")
    return render(request, "test/network_failure.html")


@require_http_methods(["GET"])
def test_chart(request):
    """Test chart component."""
    return render(request, "test/chart.html")
