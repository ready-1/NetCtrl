"""Services for the switches app."""

import json
import logging
import requests
import ssl
import urllib3
from datetime import timedelta
from django.utils import timezone
import openapi_client
from openapi_client.rest import ApiException
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context
from pathlib import Path
from django.conf import settings

# Disable SSL verification warnings in development
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning
)

logger = logging.getLogger(__name__)


class CustomSSLAdapter(HTTPAdapter):
    """Custom SSL Adapter that allows setting the SSL/TLS version."""

    def __init__(self, ssl_version=None, **kwargs):
        self.ssl_version = ssl_version
        super().__init__(**kwargs)

    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ssl_version=self.ssl_version)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        # Enable all available ciphers
        context.set_ciphers("ALL:@SECLEVEL=0")
        # Disable certificate verification
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        # Allow legacy renegotiation
        context.options &= ~ssl.OP_NO_SSLv2
        context.options &= ~ssl.OP_NO_SSLv3
        context.options &= ~ssl.OP_NO_TLSv1
        context.options &= ~ssl.OP_NO_TLSv1_1
        context.options &= ~ssl.OP_NO_RENEGOTIATION
        kwargs["ssl_context"] = context
        return super().init_poolmanager(*args, **kwargs)


class SwitchAuthService:
    """Service for handling switch authentication."""

    def __init__(self):
        """Initialize the service."""
        # Configure API client for development
        configuration = openapi_client.Configuration()

        # Get certificate paths
        certs_dir = Path(settings.BASE_DIR) / "certificates"
        ca_cert_path = certs_dir / "ca.crt"

        # Use our CA certificate if it exists, otherwise disable SSL verification
        if ca_cert_path.exists():
            configuration.ssl_ca_cert = str(ca_cert_path)
            configuration.verify_ssl = True
        else:
            configuration.verify_ssl = False
            logger.warning("CA certificate not found. SSL verification disabled.")

        # Create SSL context
        ssl_context = ssl.create_default_context()
        if ca_cert_path.exists():
            ssl_context.load_verify_locations(cafile=str(ca_cert_path))
        else:
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

        # Create pool manager with our SSL context
        pool_manager = urllib3.PoolManager(
            ssl_version=ssl.PROTOCOL_TLS,
            ssl_context=ssl_context,
            retries=urllib3.Retry(3),
        )

        # Configure API client to use our custom pool manager
        configuration.pool_manager = pool_manager

        self.api_client = openapi_client.ApiClient(configuration)
        self.auth_api = openapi_client.AuthenticationApi(self.api_client)

    def authenticate_switch(self, switch):
        """Authenticate with a switch and store the token.

        Args:
            switch: The Switch model instance to authenticate with.

        Returns:
            bool: True if authentication was successful, False otherwise.
        """
        try:
            # Get certificate paths for this switch
            certs_dir = Path(settings.BASE_DIR) / "certificates"
            cert_path = certs_dir / f"{switch.name}.crt"
            key_path = certs_dir / f"{switch.name}.key"

            # Create session with certificate if available
            session = requests.Session()
            if cert_path.exists() and key_path.exists():
                session.cert = (str(cert_path), str(key_path))

            # Make authentication request
            response = session.post(
                f"https://{switch.in_band_ip}:8443/api/v1/login",
                json={
                    "login": {"username": switch.username, "password": switch.password}
                },
                verify=(
                    False
                    if not (certs_dir / "ca.crt").exists()
                    else str(certs_dir / "ca.crt")
                ),
                timeout=10,
            )

            if response.status_code == 200:
                # Parse JSON response
                try:
                    data = json.loads(response.text)
                except json.JSONDecodeError as e:
                    logger.error(f"Failed to parse response: {str(e)}")
                    raise Exception(f"Invalid response format: {response.text}")

                # Check response status
                if data.get("resp", {}).get("status") != "success":
                    raise Exception(
                        f"Login failed: {data.get('resp', {}).get('respMsg', 'Unknown error')}"
                    )

                # Verify response has required fields
                if (
                    "login" not in data
                    or "token" not in data["login"]
                    or "expire" not in data["login"]
                ):
                    raise Exception(
                        f"Invalid response format - missing required fields: {data}"
                    )

                # Store token and expiry from response
                switch.auth_token = data["login"]["token"]
                expires = int(data["login"]["expire"])
                switch.token_expires = timezone.now() + timedelta(seconds=expires)
                switch.auth_status = switch.AUTH_STATUS_AUTHENTICATED
                switch.save(
                    update_fields=["auth_token", "token_expires", "auth_status"]
                )

                logger.info(f"Successfully authenticated with switch {switch.name}")
                return True
            else:
                switch.auth_status = "failed"
                switch.auth_token = None
                switch.save()
                return False

        except Exception as e:
            logger.error(f"Authentication failed for switch {switch.name}: {str(e)}")
            switch.auth_status = "failed"
            switch.auth_token = None
            switch.save()
            return False

    def logout_switch(self, switch):
        """Log out from a switch and clear stored token.

        Args:
            switch: The Switch model instance to log out from.

        Returns:
            bool: True if logout was successful or no token existed, False if logout failed.
        """
        if not switch.auth_token:
            return True

        try:
            # Configure API client
            configuration = openapi_client.Configuration(
                host=f"https://{switch.in_band_ip}:8443/api/v1"
            )
            configuration.verify_ssl = False
            configuration.access_token = switch.auth_token

            # Create API client
            with openapi_client.ApiClient(configuration) as api_client:
                # Create auth API instance
                auth_api = openapi_client.AuthenticationApi(api_client)

                # Make logout request
                logger.info(f"Attempting to log out from switch {switch.name}")
                auth_api.logout_post()

            logger.info(f"Successfully logged out from switch {switch.name}")
            return True

        except openapi_client.ApiException as e:
            logger.error(f"Error logging out from switch {switch.name}: {str(e)}")
            return False

        finally:
            # Always clear token data regardless of logout success
            switch.auth_token = ""
            switch.token_expires = None
            switch.auth_status = switch.AUTH_STATUS_UNAUTHENTICATED
            switch.save(update_fields=["auth_token", "token_expires", "auth_status"])

    def check_auth_status(self, switch):
        """Check if the switch's authentication token is valid and not expired.

        Args:
            switch: The Switch model instance to check.

        Returns:
            bool: True if the token is valid and not expired, False otherwise.
        """
        if not switch.auth_token or not switch.token_expires:
            return False

        now = timezone.now()

        # Token is expired
        if switch.token_expires <= now:
            logger.info(f"Token expired for switch {switch.name}")
            return False

        # Token will expire soon (within 15 minutes)
        if switch.token_expires <= now + timedelta(minutes=15):
            logger.info(f"Token expiring soon for switch {switch.name}")
            return False

        return switch.auth_status == switch.AUTH_STATUS_AUTHENTICATED

    def refresh_auth_if_needed(self, switch):
        """Check auth status and refresh if needed.

        Args:
            switch: The Switch model instance to refresh authentication for.

        Returns:
            bool: True if authentication is valid (either existing or refreshed), False otherwise.
        """
        try:
            # Check current token status
            if self.check_auth_status(switch):
                return True

            logger.info(f"Refreshing auth token for switch {switch.name}")

            # Clear existing token
            switch.auth_token = ""
            switch.token_expires = None
            switch.auth_status = switch.AUTH_STATUS_UNAUTHENTICATED
            switch.save(update_fields=["auth_token", "token_expires", "auth_status"])

            # Get new token
            success = self.authenticate_switch(switch)
            if success:
                logger.info(
                    f"Successfully refreshed auth token for switch {switch.name}"
                )
            else:
                logger.error(f"Failed to refresh auth token for switch {switch.name}")
            return success

        except Exception as e:
            logger.error(
                f"Error refreshing auth token for switch {switch.name}: {str(e)}"
            )
            switch.auth_status = switch.AUTH_STATUS_ERROR
            switch.save(update_fields=["auth_status"])
            return False
