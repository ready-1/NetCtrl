"""Tests for database models."""

import pytest
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db

class TestSwitchModel:
    """Test cases for the Switch model."""

    def test_switch_creation(self, switch_data):
        """Test creating a switch with valid data."""
        from switches.models import Switch
        switch = Switch.objects.create(**switch_data)
        assert switch.name == switch_data['name']
        assert switch.ip_address == switch_data['ip_address']

    def test_switch_str_representation(self, switch_data):
        """Test the string representation of a switch."""
        from switches.models import Switch
        switch = Switch.objects.create(**switch_data)
        assert str(switch) == f"{switch_data['name']} ({switch_data['ip_address']})"

    def test_switch_invalid_ip(self, switch_data):
        """Test that invalid IP addresses are rejected."""
        from switches.models import Switch
        switch_data['ip_address'] = 'invalid-ip'
        with pytest.raises(ValidationError):
            switch = Switch.objects.create(**switch_data)
            switch.full_clean()

class TestPortModel:
    """Test cases for the Port model."""

    def test_port_creation(self, switch_data, port_data):
        """Test creating a port with valid data."""
        from switches.models import Switch, Port
        switch = Switch.objects.create(**switch_data)
        port = Port.objects.create(switch=switch, **port_data)
        assert port.name == port_data['name']
        assert port.description == port_data['description']

    def test_port_str_representation(self, switch_data, port_data):
        """Test the string representation of a port."""
        from switches.models import Switch, Port
        switch = Switch.objects.create(**switch_data)
        port = Port.objects.create(switch=switch, **port_data)
        assert str(port) == f"{switch.name} - {port_data['name']}"

    def test_port_invalid_vlan(self, switch_data, port_data):
        """Test that invalid VLAN numbers are rejected."""
        from switches.models import Switch, Port
        switch = Switch.objects.create(**switch_data)
        port_data['vlan'] = 4096  # Invalid VLAN number
        with pytest.raises(ValidationError):
            port = Port.objects.create(switch=switch, **port_data)
            port.full_clean()

class TestConfigurationModel:
    """Test cases for the Configuration model."""

    def test_configuration_creation(self, switch_data):
        """Test creating a configuration backup."""
        from switches.models import Switch, Configuration
        switch = Switch.objects.create(**switch_data)
        config = Configuration.objects.create(
            switch=switch,
            content='test configuration',
            version='1.0'
        )
        assert config.switch == switch
        assert config.content == 'test configuration'

    def test_configuration_versioning(self, switch_data):
        """Test that configurations are properly versioned."""
        from switches.models import Switch, Configuration
        switch = Switch.objects.create(**switch_data)
        config1 = Configuration.objects.create(
            switch=switch,
            content='version 1',
            version='1.0'
        )
        config2 = Configuration.objects.create(
            switch=switch,
            content='version 2',
            version='2.0'
        )
        assert config1.version != config2.version
