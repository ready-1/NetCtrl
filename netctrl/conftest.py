"""Configure pytest for netctrl tests."""

import pytest
from django.test import Client


@pytest.fixture
def client():
    """Create a test client."""
    return Client()
