from django.urls import path
from . import views

app_name = "bugtracker"

urlpatterns = [
    path("new/", views.new_bug_request, name="new"),
    path("success/", views.success_page, name="success"),
]