"""Tests for API endpoints."""

import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = [pytest.mark.django_db, pytest.mark.api]


class TestSwitchAPI:
    """Test cases for switch management API endpoints."""

    def test_list_switches(self, authenticated_client):
        """Test listing switches."""
        url = reverse("api:switch-list")
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data, list)

    def test_create_switch(self, authenticated_client, switch_data):
        """Test creating a new switch."""
        url = reverse("api:switch-list")
        response = authenticated_client.post(url, switch_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["name"] == switch_data["name"]

    def test_retrieve_switch(self, authenticated_client, switch_data):
        """Test retrieving a specific switch."""
        # First create a switch
        url = reverse("api:switch-list")
        response = authenticated_client.post(url, switch_data)
        switch_id = response.data["id"]

        # Then retrieve it
        url = reverse("api:switch-detail", args=[switch_id])
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == switch_data["name"]

    def test_update_switch(self, authenticated_client, switch_data):
        """Test updating a switch."""
        # First create a switch
        url = reverse("api:switch-list")
        response = authenticated_client.post(url, switch_data)
        switch_id = response.data["id"]

        # Then update it
        url = reverse("api:switch-detail", args=[switch_id])
        updated_data = {**switch_data, "name": "Updated Switch"}
        response = authenticated_client.put(url, updated_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == "Updated Switch"

    def test_delete_switch(self, authenticated_client, switch_data):
        """Test deleting a switch."""
        # First create a switch
        url = reverse("api:switch-list")
        response = authenticated_client.post(url, switch_data)
        switch_id = response.data["id"]

        # Then delete it
        url = reverse("api:switch-detail", args=[switch_id])
        response = authenticated_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

        # Verify it's gone
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestPortAPI:
    """Test cases for port management API endpoints."""

    def test_list_ports(self, authenticated_client, switch_data):
        """Test listing ports for a switch."""
        # First create a switch
        url = reverse("api:switch-list")
        response = authenticated_client.post(url, switch_data)
        switch_id = response.data["id"]

        # Then list its ports
        url = reverse("api:port-list", args=[switch_id])
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data, list)

    def test_update_port(self, authenticated_client, switch_data, port_data):
        """Test updating a port configuration."""
        # First create a switch
        url = reverse("api:switch-list")
        response = authenticated_client.post(url, switch_data)
        switch_id = response.data["id"]

        # Create a port
        from switches.models import Port, Switch

        switch = Switch.objects.get(id=switch_id)
        Port.objects.create(switch=switch, **port_data)

        # Then update the port
        url = reverse(
            "api:port-detail", kwargs={"switch_id": switch_id, "n": port_data["name"]}
        )
        updated_data = {**port_data, "description": "Updated Port", "switch": switch_id}
        response = authenticated_client.put(url, updated_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["description"] == "Updated Port"
