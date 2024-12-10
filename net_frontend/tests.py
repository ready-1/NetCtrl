from django.test import TestCase
from django.urls import reverse
from net_core.models import Switch

class SwitchCRUDTests(TestCase):
    def setUp(self):
        # Create a sample switch for testing
        self.switch = Switch.objects.create(
            name="Test Switch",
            ip_address_in_band="192.168.1.1",
            ip_address_out_band="192.168.2.1",
            mac_address="00:1A:2B:3C:4D:5E",
            model="TestModel",
            serial_number="SN12345",
            firmware_version="1.0.0",
            status="active",
            location="Test Lab",
            port_count=48,
            asset_id="ASSET12345",
            notes="Initial test switch"
        )

    def test_switch_list_view(self):
        response = self.client.get(reverse("net_frontend:switch_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Switch")

    def test_switch_detail_view(self):
        response = self.client.get(reverse("net_frontend:switch_detail", args=[self.switch.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Switch")

    def test_switch_create_view(self):
        response = self.client.post(reverse("net_frontend:switch_create"), {
            "name": "New Switch",
            "ip_address_in_band": "192.168.1.2",
            "ip_address_out_band": "192.168.2.2",
            "mac_address": "AA:BB:CC:DD:EE:FF",
            "model": "NewModel",
            "serial_number": "SN54321",
            "firmware_version": "2.0.0",
            "status": "active",
            "location": "New Lab",
            "port_count": 24,
            "asset_id": "ASSET54321",
            "notes": "Created for testing"
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Switch.objects.filter(name="New Switch").exists())

    def test_switch_update_view(self):
        response = self.client.post(reverse("net_frontend:switch_update", args=[self.switch.pk]), {
            "name": "Updated Switch",
            "ip_address_in_band": "192.168.1.10",
            "ip_address_out_band": "192.168.2.10",
            "mac_address": "00:1A:2B:3C:4D:5E",
            "model": "UpdatedModel",
            "serial_number": "SN12345",
            "firmware_version": "1.1.0",
            "status": "inactive",
            "location": "Updated Lab",
            "port_count": 48,
            "asset_id": "ASSET54321",
            "notes": "Updated for testing"
        })
        self.assertEqual(response.status_code, 302)
        self.switch.refresh_from_db()
        self.assertEqual(self.switch.name, "Updated Switch")
        self.assertEqual(self.switch.status, "inactive")

    def test_switch_delete_view(self):
        response = self.client.post(reverse("net_frontend:switch_delete", args=[self.switch.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Switch.objects.filter(pk=self.switch.pk).exists())