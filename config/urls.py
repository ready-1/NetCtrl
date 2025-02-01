from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("netctrl.urls")),
    path("test/", include("tests.urls")),
]
