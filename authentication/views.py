from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView
from django.contrib import messages
from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .forms import LoginForm
from .models import UserSettings


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = "authentication/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        messages.success(self.request, f"Welcome back, {self.request.user.username}!")
        return reverse_lazy("core:dashboard")


class LoginView(LoginView):
    """Custom login view."""

    template_name = "authentication/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("netctrl:dashboard")


class LogoutView(LogoutView):
    """Custom logout view."""

    next_page = reverse_lazy("authentication:login")


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("authentication:login")


class ProfileView(LoginRequiredMixin, TemplateView):
    """User profile view."""

    template_name = "authentication/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {"title": "Profile", "url": reverse_lazy("authentication:profile")}
        ]
        return context


class SettingsView(LoginRequiredMixin, TemplateView):
    """User settings view."""

    template_name = "authentication/settings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {"title": "Settings", "url": reverse_lazy("authentication:settings")}
        ]
        # Get or create user settings
        settings, created = UserSettings.objects.get_or_create(user=self.request.user)
        context["user_settings"] = settings
        return context

    def post(self, request, *args, **kwargs):
        settings, created = UserSettings.objects.get_or_create(user=request.user)
        settings.dark_mode = request.POST.get("dark_mode") == "on"
        settings.email_notifications = request.POST.get("email_notifications") == "on"
        settings.browser_notifications = (
            request.POST.get("browser_notifications") == "on"
        )
        settings.save()

        messages.success(request, _("Settings updated successfully."))
        return redirect("authentication:settings")


class TokenObtainView(TokenObtainPairView):
    """
    Custom token obtain view that adds user role information to the token
    """

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.user
            response.data["user_role"] = (
                "superuser"
                if user.is_superuser
                else "privileged" if user.is_staff else "non_privileged"
            )
        return response


class TokenRevokeView(APIView):
    """
    Revoke the refresh token for the current user
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"detail": "Token has been revoked"}, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {"detail": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )
