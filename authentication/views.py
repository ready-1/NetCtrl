from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import LoginForm
from django.contrib import messages
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = "authentication/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        messages.success(self.request, f"Welcome back, {self.request.user.username}!")
        return reverse_lazy("core:dashboard")


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("authentication:login")


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
