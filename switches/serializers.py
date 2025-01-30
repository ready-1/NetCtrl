"""Serializers for the switches app."""

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Switch, Port

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""

    class Meta:
        """Meta class for UserSerializer."""
        model = get_user_model()
        fields = ['id', 'username', 'email']
        read_only_fields = ['id']

class SwitchSerializer(serializers.ModelSerializer):
    """Serializer for the Switch model."""

    class Meta:
        """Meta class for SwitchSerializer."""
        model = Switch
        fields = ['id', 'name', 'ip_address', 'username', 'password',
                 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class PortSerializer(serializers.ModelSerializer):
    """Serializer for the Port model."""

    class Meta:
        """Meta class for PortSerializer."""
        model = Port
        fields = ['id', 'switch', 'name', 'description', 'admin_status',
                 'vlan', 'speed', 'duplex', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
