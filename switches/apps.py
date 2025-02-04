"""Configuration for the switches app."""

from django.apps import AppConfig
from django.conf import settings
from django.utils import timezone
import threading
import time
import logging

logger = logging.getLogger(__name__)


class TokenRefreshThread(threading.Thread):
    """Background thread to refresh authentication tokens."""

    def __init__(self):
        """Initialize the thread."""
        super().__init__(daemon=True)
        self._stop_event = threading.Event()

    def run(self):
        """Run the token refresh loop."""
        while not self._stop_event.is_set():
            try:
                # Import here to avoid circular imports
                from switches.models import Switch
                from switches.services import SwitchAuthService

                # Get switches that need token refresh
                switches = Switch.objects.filter(
                    auth_status=Switch.AUTH_STATUS_AUTHENTICATED,
                    token_expires__lte=timezone.now() + timezone.timedelta(minutes=15),
                )

                # Refresh tokens
                auth_service = SwitchAuthService()
                for switch in switches:
                    try:
                        logger.info(f"Auto-refreshing token for switch {switch.name}")
                        auth_service.refresh_auth_if_needed(switch)
                    except Exception as e:
                        logger.error(
                            f"Error auto-refreshing token for switch {switch.name}: {str(e)}"
                        )

            except Exception as e:
                logger.error(f"Error in token refresh thread: {str(e)}")

            # Sleep for 5 minutes before next check
            self._stop_event.wait(300)

    def stop(self):
        """Stop the token refresh loop."""
        self._stop_event.set()


class SwitchesConfig(AppConfig):
    """Configuration class for the switches app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "switches"

    def ready(self):
        """Start background tasks when the app is ready."""
        if not settings.DEBUG:  # Only run in production
            self.token_refresh_thread = TokenRefreshThread()
            self.token_refresh_thread.start()
