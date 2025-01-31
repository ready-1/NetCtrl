from django.test import TestCase, Client, RequestFactory, override_settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.http import HttpRequest, HttpResponse
from core.models import AuditLog
from core.middleware import AuditLogMiddleware
from core.decorators import audit_log
import json

User = get_user_model()


class TestAuditLogModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass123", is_staff=True
        )

    def test_audit_log_creation(self):
        """Test basic audit log creation"""
        log = AuditLog.objects.create(
            user=self.user, action=AuditLog.ACTION_CREATE, description="Test log entry"
        )
        self.assertEqual(log.action, AuditLog.ACTION_CREATE)
        self.assertEqual(log.user, self.user)
        self.assertEqual(log.description, "Test log entry")

    def test_set_changes(self):
        """Test the set_changes method"""
        log = AuditLog.objects.create(
            user=self.user, action=AuditLog.ACTION_UPDATE, description="Test changes"
        )

        old_data = {"name": "old", "value": 1}
        new_data = {"name": "new", "value": 2}

        log.set_changes(old_data, new_data)
        self.assertIn("modified", log.changes)
        self.assertEqual(log.changes["modified"]["name"]["old"], "old")
        self.assertEqual(log.changes["modified"]["name"]["new"], "new")

    def test_add_metadata(self):
        """Test adding metadata"""
        log = AuditLog.objects.create(
            user=self.user, action=AuditLog.ACTION_OTHER, description="Test metadata"
        )

        log.add_metadata(key1="value1", key2="value2")
        self.assertEqual(log.metadata["key1"], "value1")
        self.assertEqual(log.metadata["key2"], "value2")


class TestAuditLogMiddleware(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.middleware = AuditLogMiddleware(lambda r: HttpResponse())
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_middleware_logs_request(self):
        """Test that middleware creates log entries for requests"""
        request = self.factory.get("/test-path/")
        request.user = self.user
        request.META["REMOTE_ADDR"] = "127.0.0.1"

        # Process the request
        self.middleware(request)

        # Check if log was created
        log = AuditLog.objects.last()
        self.assertIsNotNone(log)
        self.assertEqual(log.user, self.user)
        self.assertEqual(log.action, AuditLog.ACTION_VIEW)
        self.assertEqual(log.ip_address, "127.0.0.1")

    def test_middleware_updates_last_activity(self):
        """Test that middleware updates user's last activity"""
        request = self.factory.get("/test-path/")
        request.user = self.user
        request.META["REMOTE_ADDR"] = "127.0.0.1"

        # Process the request
        self.middleware(request)

        # Refresh user from database
        self.user.refresh_from_db()
        self.assertIsNotNone(self.user.last_activity)


class TestAuditLogDecorator(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_decorator_logs_action(self):
        """Test that decorator creates log entries"""

        @audit_log(action=AuditLog.ACTION_CREATE, description="Test action")
        def test_view(request):
            return HttpResponse("success")

        request = self.factory.get("/test-path/")
        request.user = self.user
        request.META["REMOTE_ADDR"] = "127.0.0.1"

        # Call the decorated function
        test_view(request)

        # Check if log was created
        log = AuditLog.objects.last()
        self.assertIsNotNone(log)
        self.assertEqual(log.user, self.user)
        self.assertEqual(log.action, AuditLog.ACTION_CREATE)
        self.assertEqual(log.description, "Test action")


# Remove AuditLogMiddleware for view tests
TEST_MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


@override_settings(MIDDLEWARE=TEST_MIDDLEWARE)
class TestAuditLogViews(TestCase):
    def setUp(self):
        self.client = Client()
        # Create superuser
        self.superuser = User.objects.create_superuser(
            username="admin", password="admin123", email="admin@example.com"
        )
        # Create regular user
        self.user = User.objects.create_user(username="user", password="user123")
        # Clear any existing logs
        AuditLog.objects.all().delete()

    def test_audit_log_list_view_access(self):
        """Test access control for audit log list view"""
        url = reverse("core:audit_logs")

        # Test unauthenticated access
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Redirect to login

        # Test non-privileged user access
        self.client.login(username="user", password="user123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)  # Forbidden

        # Test privileged user access
        self.client.login(username="admin", password="admin123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_audit_log_filtering(self):
        """Test audit log filtering"""
        # Create test logs
        AuditLog.objects.all().delete()
        for i in range(5):
            AuditLog.objects.create(
                user=self.superuser,
                action=AuditLog.ACTION_CREATE,
                description=f"Test log {i}",
            )

        self.client.login(username="admin", password="admin123")
        url = reverse("core:audit_logs")

        # Get initial count of logs (including login)
        initial_count = AuditLog.objects.filter(action=AuditLog.ACTION_CREATE).count()

        # Test action filter
        response = self.client.get(f"{url}?action={AuditLog.ACTION_CREATE}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["audit_logs"]), initial_count)

        # Test user filter
        response = self.client.get(f"{url}?user={self.superuser.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context["audit_logs"]),
            AuditLog.objects.filter(user=self.superuser).count(),
        )

    def test_pagination(self):
        """Test audit log pagination"""
        # Clear existing logs
        AuditLog.objects.all().delete()

        # Create exactly 65 logs for pagination
        for i in range(65):
            AuditLog.objects.create(
                user=self.superuser,
                action=AuditLog.ACTION_CREATE,
                description=f"Pagination test log {i}",
            )

        self.client.login(username="admin", password="admin123")
        url = reverse("core:audit_logs")

        # Get initial count (including login)
        initial_count = AuditLog.objects.count()
        expected_first_page = min(50, initial_count)
        expected_second_page = max(0, initial_count - 50)

        # Test first page
        response = self.client.get(url)
        self.assertEqual(len(response.context["audit_logs"]), expected_first_page)
        self.assertTrue(response.context["is_paginated"])

        # Test second page
        response = self.client.get(f"{url}?page=2")
        self.assertEqual(len(response.context["audit_logs"]), expected_second_page)
