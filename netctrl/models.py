from django.db import models


class Switch(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_stats(self):
        # TODO: Implement real stats collection
        return {
            "cpu_usage": 25,
            "memory_usage": 60,
            "uptime": "7 days",
            "temperature": "45°C",
        }

    def __str__(self):
        return self.name
