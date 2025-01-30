"""API views for the switches app."""

from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Switch, Port
from .serializers import (
    UserSerializer,
    SwitchSerializer,
    PortSerializer,
)


class UserDetailView(generics.RetrieveAPIView):
    """API view for retrieving user details."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        """Return the authenticated user."""
        return self.request.user


class SwitchListCreateView(generics.ListCreateAPIView):
    """API view for listing and creating switches."""

    permission_classes = [permissions.IsAuthenticated]
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer


class SwitchDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API view for retrieving, updating and deleting switches."""

    permission_classes = [permissions.IsAuthenticated]
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer


class PortListView(generics.ListAPIView):
    """API view for listing ports."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PortSerializer

    def get_queryset(self):
        """Return ports for a specific switch."""
        switch_id = self.kwargs["switch_id"]
        return Port.objects.filter(switch_id=switch_id)


class PortDetailView(generics.RetrieveUpdateAPIView):
    """API view for retrieving and updating ports."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PortSerializer
    lookup_field = "name"  # Field in the model
    lookup_url_kwarg = "n"  # Parameter in the URL

    def get_queryset(self):
        """Return ports for a specific switch."""
        switch_id = self.kwargs["switch_id"]
        return Port.objects.filter(switch_id=switch_id)
