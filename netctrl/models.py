from django.db import models
from django.core.exceptions import ValidationError
from cryptography.fernet import Fernet
from django.conf import settings
import ipaddress
import os
import re


class EncryptionKey:
    _fernet = None

    @classmethod
    def get_key(cls):
        if not cls._fernet:
            key = os.getenv("ENCRYPTION_KEY") or settings.ENCRYPTION_KEY
            cls._fernet = Fernet(key)
        return cls._fernet


class Switch(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Unique switch identifier (e.g. PDX-RIG-12-SW01)",
    )
    in_band_ip = models.GenericIPAddressField(
        help_text="Private IP for management plane access", verbose_name="In-band IP"
    )
    out_band_ip = models.GenericIPAddressField(
        help_text="Private IP for data plane access", verbose_name="Out-of-band IP"
    )
    username = models.CharField(
        max_length=100, help_text="Privileged account for CLI access"
    )
    encrypted_password = models.BinaryField(
        editable=False, help_text="Fernet-encrypted credentials"
    )
    cert_expiry = models.DateField(
        null=True, blank=True, help_text="Next certificate rotation date"
    )
    last_cert_renewal = models.DateTimeField(
        null=True, blank=True, help_text="Timestamp of last successful cert renewal"
    )
    cli_timeout = models.PositiveSmallIntegerField(
        default=30, help_text="SSH session timeout in seconds (per M4300 docs)"
    )
    aaa_config = models.TextField(
        max_length=1024, help_text="AAA authorization config in CLI format"
    )
    igmp_snooping_enabled = models.BooleanField(
        default=True, help_text="Enable IGMP snooping per port security specs"
    )

    def clean(self):
        # Validate private IP ranges
        for ip in [self.in_band_ip, self.out_band_ip]:
            if not ipaddress.ip_address(ip).is_private:
                raise ValidationError(f"{ip} must be a private IP address")

        # Validate AAA config format
        if not re.match(
            r"^aaa authorization tracing enabled", self.aaa_config, re.IGNORECASE
        ):
            raise ValidationError(
                "AAA config must follow 'aaa authorization tracing enabled' pattern"
            )

        # Validate distinct IP addresses
        if self.in_band_ip == self.out_band_ip:
            raise ValidationError("In-band and out-of-band IPs must be different")

    def save(self, *args, **kwargs):
        # Only encrypt if password is being set
        if hasattr(self, "_password"):
            self.encrypted_password = EncryptionKey.get_key().encrypt(
                self._password.encode()
            )
        super().save(*args, **kwargs)

    @property
    def password(self):
        if not hasattr(self, "_password"):
            if self.encrypted_password:
                self._password = (
                    EncryptionKey.get_key()
                    .decrypt(bytes(self.encrypted_password))
                    .decode()
                )
            else:
                self._password = ""
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def __str__(self):
        return f"{self.name} ({self.in_band_ip})"

    class Meta:
        verbose_name_plural = "Switches"
