"""Tests for the Content Management API endpoints."""
import json
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.models.content import ContentType, ContentStatus

client = TestClient(app)

def test_create_content(admin_token):
    """Test creating content as admin user."""
    headers = {"Authorization": f"Bearer {admin_token}"}
    content_data = {
        "title": "Test Content",
        "description": "Test description",
        "body": "Test content body",
        "content_type": "text",
        "status": "draft"
    }
    
    response = client.post(
        "/api/v1/content/", 
        headers=headers,
        json=content_data
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Content"
    assert data["description"] == "Test description"
    assert data["body"] == "Test content body"
    assert data["content_type"] == "text"
    assert data["status"] == "draft"
    assert "id" in data
    assert "created_by" in data
    assert "updated_by" in data
    assert "created_at" in data
    assert "updated_at" in data
    
    return data["id"]

def test_get_content(admin_token):
    """Test getting content by ID."""
    # First create content
    content_id = test_create_content(admin_token)
    
    # Now get it
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.get(
        f"/api/v1/content/{content_id}",
        headers=headers
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == content_id
    assert data["title"] == "Test Content"
    assert "files" in data
    assert "permissions" in data
    
def test_list_content(admin_token):
    """Test listing content with filters."""
    # Create a few content items
    headers = {"Authorization": f"Bearer {admin_token}"}
    
    # Create first content
    content_data1 = {
        "title": "SearchableTitle",
        "description": "Test description 1",
        "body": "Test content body 1",
        "content_type": "text",
        "status": "draft"
    }
    client.post("/api/v1/content/", headers=headers, json=content_data1)
    
    # Create second content
    content_data2 = {
        "title": "Another Title",
        "description": "Test description 2",
        "body": "This is searchable content",
        "content_type": "html",
        "status": "published"
    }
    client.post("/api/v1/content/", headers=headers, json=content_data2)
    
    # List all content
    response = client.get(
        "/api/v1/content/",
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["total"] >= 2
    assert len(data["items"]) >= 2
    
    # Test filtering by status
    response = client.get(
        "/api/v1/content/?status_filter=draft",
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["total"] >= 1
    assert all(item["status"] == "draft" for item in data["items"])
    
    # Test filtering by content type
    response = client.get(
        "/api/v1/content/?content_type_filter=html",
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["total"] >= 1
    assert all(item["content_type"] == "html" for item in data["items"])
    
    # Test search
    response = client.get(
        "/api/v1/content/?search=searchable",
        headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["total"] >= 2
    
def test_update_content(admin_token):
    """Test updating content."""
    # First create content
    content_id = test_create_content(admin_token)
    
    # Now update it
    headers = {"Authorization": f"Bearer {admin_token}"}
    update_data = {
        "title": "Updated Title",
        "description": "Updated description",
        "status": "published"
    }
    
    response = client.put(
        f"/api/v1/content/{content_id}",
        headers=headers,
        json=update_data
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == content_id
    assert data["title"] == "Updated Title"
    assert data["description"] == "Updated description"
    assert data["status"] == "published"
    
def test_delete_content(admin_token):
    """Test deleting content."""
    # First create content
    content_id = test_create_content(admin_token)
    
    # Now delete it
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.delete(
        f"/api/v1/content/{content_id}",
        headers=headers
    )
    
    assert response.status_code == 204
    
    # Verify it's gone
    response = client.get(
        f"/api/v1/content/{content_id}",
        headers=headers
    )
    assert response.status_code == 404
    
def test_set_content_permissions(admin_token):
    """Test setting content permissions."""
    # First create content
    content_id = test_create_content(admin_token)
    
    # Now set permissions
    headers = {"Authorization": f"Bearer {admin_token}"}
    permissions_data = {
        "permissions": {
            "admin": {
                "can_view": True,
                "can_edit": True,
                "can_delete": True
            },
            "editor": {
                "can_view": True,
                "can_edit": True,
                "can_delete": False
            },
            "user": {
                "can_view": True,
                "can_edit": False,
                "can_delete": False
            }
        }
    }
    
    response = client.post(
        f"/api/v1/content/{content_id}/permissions",
        headers=headers,
        json=permissions_data
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    
    # Now get permissions
    response = client.get(
        f"/api/v1/content/{content_id}/permissions",
        headers=headers
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "admin" in data
    assert data["admin"]["can_view"] is True
    assert data["admin"]["can_edit"] is True
    assert data["admin"]["can_delete"] is True
    
    assert "editor" in data
    assert data["editor"]["can_view"] is True
    assert data["editor"]["can_edit"] is True
    assert data["editor"]["can_delete"] is False
    
    assert "user" in data
    assert data["user"]["can_view"] is True
    assert data["user"]["can_edit"] is False
    assert data["user"]["can_delete"] is False
