from django.contrib import admin
from django.urls import path, include
from netctrl.views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("", include("netctrl.urls")),
    path("core/", include("core.urls")),
    path("tests/", include("tests.urls", namespace="tests")),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("auth/", include("authentication.urls", namespace="authentication")),
]
