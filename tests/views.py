from django.shortcuts import render


def test_alert(request, type):
    return render(
        request, "test/alert.html", {"type": type, "message": "Test alert message"}
    )


def test_buttons(request):
    return render(request, "test/buttons.html")


def test_card(request):
    return render(request, "test/card.html")


def test_loading(request):
    return render(request, "test/loading.html")


def test_form(request):
    return render(request, "test/form.html", {"show_validation": True})


def test_components(request):
    return render(request, "test/dark_theme.html", {"dark_mode": True})
