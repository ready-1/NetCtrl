from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.utils.translation import gettext_lazy as _

# Create your views here.


def is_staff(user):
    """Check if user is staff."""
    return user.is_staff


@user_passes_test(is_staff)
def styleguide(request):
    """Main style guide view."""
    return render(
        request,
        "styleguide/index.html",
        {
            "title": _("Style Guide"),
        },
    )


@user_passes_test(is_staff)
def components(request):
    """Components style guide view."""
    return render(
        request,
        "styleguide/components.html",
        {
            "title": _("Components"),
        },
    )


@user_passes_test(is_staff)
def forms(request):
    """Forms style guide view."""
    return render(
        request,
        "styleguide/forms.html",
        {
            "title": _("Forms"),
        },
    )


@user_passes_test(is_staff)
def charts(request):
    """Charts style guide view."""
    return render(
        request,
        "styleguide/charts.html",
        {
            "title": _("Charts"),
        },
    )


@user_passes_test(is_staff)
def dark_theme(request):
    """Dark theme style guide view."""
    return render(
        request,
        "styleguide/dark_theme.html",
        {
            "title": _("Dark Theme"),
        },
    )
