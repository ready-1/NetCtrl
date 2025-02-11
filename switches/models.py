"""Models for the switches app."""

from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    validate_ipv4_address,
)
from django.utils import timezone


class Switch(models.Model):
    """Model representing a network switch."""

    STATUS_UP = "up"
    STATUS_DOWN = "down"
    STATUS_DEGRADED = "degraded"
    STATUS_UNKNOWN = "unknown"

    STATUS_CHOICES = [
        (STATUS_UP, "Up"),
        (STATUS_DOWN, "Down"),
        (STATUS_DEGRADED, "Degraded"),
        (STATUS_UNKNOWN, "Unknown"),
    ]

    ERROR_AUTH_FAILED = "auth_failed"
    ERROR_SSL = "ssl_error"
    ERROR_NO_RESPONSE = "no_response"
    ERROR_API = "api_error"
    ERROR_NONE = "none"

    ERROR_CHOICES = [
        (ERROR_AUTH_FAILED, "Authentication failed"),
        (ERROR_SSL, "SSL certificate error"),
        (ERROR_NO_RESPONSE, "No response from switch"),
        (ERROR_API, "API error"),
        (ERROR_NONE, "No error"),
    ]

    AUTH_STATUS_AUTHENTICATED = "authenticated"
    AUTH_STATUS_UNAUTHENTICATED = "unauthenticated"
    AUTH_STATUS_ERROR = "error"

    AUTH_STATUS_CHOICES = [
        (AUTH_STATUS_AUTHENTICATED, "Authenticated"),
        (AUTH_STATUS_UNAUTHENTICATED, "Unauthenticated"),
        (AUTH_STATUS_ERROR, "Error"),
    ]

    name = models.CharField(max_length=255)
    in_band_ip = models.GenericIPAddressField(
        protocol="IPv4",
        validators=[validate_ipv4_address],
        verbose_name="In-Band IP",
        help_text="In-band management IP address",
    )
    out_band_ip = models.GenericIPAddressField(
        protocol="IPv4",
        validators=[validate_ipv4_address],
        verbose_name="Out-Band IP",
        help_text="Out-of-band management IP address",
    )
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # Individual interface status fields
    in_band_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_UNKNOWN,
        verbose_name="In-Band Status",
        help_text="Status of the in-band management interface",
    )
    out_band_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_UNKNOWN,
        verbose_name="Out-Band Status",
        help_text="Status of the out-of-band management interface",
    )
    in_band_last_seen = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="In-Band Last Seen",
        help_text="Last successful connection to in-band interface",
    )
    out_band_last_seen = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Out-Band Last Seen",
        help_text="Last successful connection to out-band interface",
    )
    in_band_error = models.CharField(
        max_length=20,
        choices=ERROR_CHOICES,
        default=ERROR_NONE,
        verbose_name="In-Band Error",
        help_text="Last error encountered on in-band interface",
    )
    out_band_error = models.CharField(
        max_length=20,
        choices=ERROR_CHOICES,
        default=ERROR_NONE,
        verbose_name="Out-Band Error",
        help_text="Last error encountered on out-band interface",
    )
    in_band_error_detail = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="In-Band Error Detail",
        help_text="Detailed error message for in-band interface",
    )
    out_band_error_detail = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Out-Band Error Detail",
        help_text="Detailed error message for out-band interface",
    )
    in_band_response_time = models.FloatField(
        null=True,
        blank=True,
        verbose_name="In-Band Response Time",
        help_text="Last response time in milliseconds",
    )
    out_band_response_time = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Out-Band Response Time",
        help_text="Last response time in milliseconds",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_UNKNOWN,
        help_text="Aggregate status based on both interfaces",
    )
    status_details = models.JSONField(
        default=dict,
        blank=True,
        help_text="Detailed status information and history",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Authentication fields
    auth_token = models.CharField(max_length=255, blank=True)
    token_expires = models.DateTimeField(null=True, blank=True)
    auth_status = models.CharField(
        max_length=20,
        choices=AUTH_STATUS_CHOICES,
        default=AUTH_STATUS_UNAUTHENTICATED,
        help_text="Current authentication status with the switch",
    )

    class Meta:
        """Meta class for Switch model."""

        verbose_name_plural = "switches"
        ordering = ["name"]

    def __str__(self):
        """Return a string representation of the switch."""
        return f"{self.name} ({self.in_band_ip})"

    def update_interface_status(
        self,
        interface,
        new_status,
        error_type=ERROR_NONE,
        error_detail="",
        response_time=None,
    ):
        """Update status for a specific interface (in_band or out_band)."""
        if interface not in ["in_band", "out_band"]:
            raise ValueError("Interface must be 'in_band' or 'out_band'")

        # Store old status for history
        old_status = getattr(self, f"{interface}_status")

        # Update status fields
        setattr(self, f"{interface}_status", new_status)
        setattr(self, f"{interface}_error", error_type)
        setattr(self, f"{interface}_error_detail", error_detail)
        if response_time is not None:
            setattr(self, f"{interface}_response_time", response_time)

        # Update last seen timestamp for successful connections
        if new_status == self.STATUS_UP:
            setattr(self, f"{interface}_last_seen", timezone.now())

        # Update aggregate status
        if (
            self.in_band_status == self.STATUS_UP
            and self.out_band_status == self.STATUS_UP
        ):
            self.status = self.STATUS_UP
        elif (
            self.in_band_status == self.STATUS_DOWN
            and self.out_band_status == self.STATUS_DOWN
        ):
            self.status = self.STATUS_DOWN
        else:
            self.status = self.STATUS_DEGRADED

        # Update status history
        current_time = timezone.now().isoformat()
        if "history" not in self.status_details:
            self.status_details["history"] = []

        history_entry = {
            "timestamp": current_time,
            "interface": interface,
            "old_status": old_status,
            "new_status": new_status,
            "aggregate_status": self.status,
            "error_type": error_type,
            "error_detail": error_detail,
        }
        if response_time is not None:
            history_entry["response_time"] = response_time

        self.status_details["history"].append(history_entry)

        # Keep only last 5 status changes
        if len(self.status_details["history"]) > 5:
            self.status_details["history"] = self.status_details["history"][-5:]

        # Prepare fields to update
        update_fields = [
            f"{interface}_status",
            f"{interface}_error",
            f"{interface}_error_detail",
            "status",
            "status_details",
        ]

        if new_status == self.STATUS_UP:
            update_fields.append(f"{interface}_last_seen")
        if response_time is not None:
            update_fields.append(f"{interface}_response_time")

        self.save(update_fields=update_fields)
        return old_status

    def is_interface_online(self, interface):
        """Check if a specific interface is online."""
        if interface not in ["in_band", "out_band"]:
            raise ValueError("Interface must be 'in_band' or 'out_band'")

        last_seen = getattr(self, f"{interface}_last_seen")
        if not last_seen:
            return False

        return (timezone.now() - last_seen).total_seconds() < 30

    @property
    def is_online(self):
        """Check if either interface is online."""
        return self.is_interface_online("in_band") or self.is_interface_online(
            "out_band"
        )


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
