from django.urls import resolve, reverse, NoReverseMatch
from django.utils.text import camel_case_to_spaces


def breadcrumbs(request):
    """
    Context processor that provides breadcrumb navigation based on the current URL.
    """
    path = request.path.strip("/")
    url_name = resolve(request.path).url_name
    breadcrumbs = []

    try:
        home_url = reverse("netctrl:home")
    except NoReverseMatch:
        home_url = "/"

    # Always include home
    breadcrumbs.append({"title": "Home", "url": home_url})

    if url_name == "home":
        return {"breadcrumbs": None}  # Don't show breadcrumbs on home page

    # Handle switch-related pages
    if "switch" in url_name:
        try:
            switch_list_url = reverse("netctrl:switch-list")
        except NoReverseMatch:
            switch_list_url = "/switches/"

        breadcrumbs.append({"title": "Switches", "url": switch_list_url})

        if url_name == "switch-add":
            breadcrumbs.append({"title": "Add Switch", "url": None})
        elif url_name in ["switch-detail", "switch-edit", "switch-delete"]:
            switch = request.resolver_match.kwargs.get("pk")
            if switch:
                try:
                    switch_detail_url = reverse(
                        "netctrl:switch-detail", kwargs={"pk": switch}
                    )
                except NoReverseMatch:
                    switch_detail_url = f"/switches/{switch}/"

                breadcrumbs.append(
                    {"title": f"Switch {switch}", "url": switch_detail_url}
                )
                if url_name in ["switch-edit", "switch-delete"]:
                    action = url_name.split("-")[1].title()
                    breadcrumbs.append({"title": action, "url": None})

    # Handle admin pages
    elif url_name in ["audit-log", "user-management"]:
        try:
            admin_index_url = reverse("admin:index")
        except NoReverseMatch:
            admin_index_url = "/admin/"

        breadcrumbs.append({"title": "Administration", "url": admin_index_url})
        breadcrumbs.append(
            {"title": camel_case_to_spaces(url_name).title(), "url": None}
        )

    # Handle user pages
    elif url_name in ["profile", "settings", "notifications"]:
        breadcrumbs.append(
            {"title": camel_case_to_spaces(url_name).title(), "url": None}
        )

    return {"breadcrumbs": breadcrumbs}
