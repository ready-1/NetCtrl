from django.test import TestCase
from core.models import Switch
from core.utils import validate_ip_address, format_mac_address

class SwitchModelTest(TestCase):
    def test_create_switch(self):
        switch = Switch.objects.create(
            name="Test Switch",
            ip_address_in_band="192.168.1.1",
            mac_address="00:11:22:33:44:55",
            model="Netgear XS724EM",
            serial_number="SN12345",
            firmware_version="1.0.0",
            port_count=24,
        )
        self.assertEqual(switch.name, "Test Switch")

    def test_validate_ip_address(self):
        valid_ip = validate_ip_address("192.168.1.1")
        self.assertEqual(valid_ip, "192.168.1.1")
        
        with self.assertRaises(ValueError):
            validate_ip_address("999.999.999.999")

    def test_format_mac_address(self):
        mac = format_mac_address("00-11-22-33-44-55")
        self.assertEqual(mac, "00:11:22:33:44:55")