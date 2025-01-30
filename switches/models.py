"""Models for the switches app."""

from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    validate_ipv4_address,
)


class Switch(models.Model):
    """Model representing a network switch."""

    name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(
        protocol="IPv4", validators=[validate_ipv4_address]
    )
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the switch."""
        return f"{self.name} ({self.ip_address})"

    class Meta:
        """Meta class for Switch model."""

        verbose_name_plural = "switches"
        ordering = ["name"]


class Port(models.Model):
    """Model representing a switch port."""

    ADMIN_STATUS_CHOICES = [
        ("up", "Up"),
        ("down", "Down"),
    ]

    SPEED_CHOICES = [
        ("auto", "Auto"),
        ("1G", "1 Gbps"),
        ("10G", "10 Gbps"),
        ("40G", "40 Gbps"),
    ]

    DUPLEX_CHOICES = [
        ("auto", "Auto"),
        ("full", "Full"),
        ("half", "Half"),
    ]

    switch = models.ForeignKey(Switch, on_delete=models.CASCADE, related_name="ports")
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    admin_status = models.CharField(
        max_length=4, choices=ADMIN_STATUS_CHOICES, default="up"
    )
    vlan = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4094)]
    )
    speed = models.CharField(max_length=4, choices=SPEED_CHOICES, default="auto")
    duplex = models.CharField(max_length=4, choices=DUPLEX_CHOICES, default="auto")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the port."""
        return f"{self.switch.name} - {self.name}"

    class Meta:
        """Meta class for Port model."""

        unique_together = ["switch", "name"]
        ordering = ["switch", "name"]


class Configuration(models.Model):
    """Model representing a switch configuration backup."""

    switch = models.ForeignKey(
        Switch, on_delete=models.CASCADE, related_name="configurations"
    )
    content = models.TextField()
    version = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the configuration."""
        return f"{self.switch.name} - {self.version}"

    class Meta:
        """Meta class for Configuration model."""

        ordering = ["-created_at"]
        get_latest_by = "created_at"
