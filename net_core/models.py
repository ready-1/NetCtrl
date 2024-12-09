from django.db import models

class Switch(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    name = models.CharField(max_length=100, help_text="Friendly name for the switch")
    ip_address_in_band = models.GenericIPAddressField(protocol='IPv4', help_text="IPv4 address for in-band management")
    ip_address_out_band = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True, help_text="IPv4 address for out-of-band management")
    mac_address = models.CharField(max_length=17, unique=True, help_text="MAC address of the switch")
    model = models.CharField(max_length=100, help_text="Switch model number")
    serial_number = models.CharField(max_length=100, unique=True, help_text="Serial number of the switch")
    firmware_version = models.CharField(max_length=50, help_text="Current firmware version")
    last_known_state = models.JSONField(blank=True, null=True, help_text="Last known state or configuration (JSON format)")
    gold_master_config = models.JSONField(blank=True, null=True, help_text="Gold Master configuration (JSON format)")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', help_text="Current status of the switch")
    location = models.CharField(max_length=200, blank=True, null=True, help_text="Physical location or identifier")
    port_count = models.PositiveIntegerField(help_text="Number of physical ports on the switch")
    asset_id = models.CharField(max_length=100, blank=True, null=True, help_text="Inventory tracking asset ID")
    notes = models.TextField(blank=True, null=True, help_text="Optional admin comments")
    last_sync = models.DateTimeField(auto_now=True, help_text="Timestamp of the last synchronization")

    def __str__(self):
        return f"{self.name} ({self.ip_address_in_band})"