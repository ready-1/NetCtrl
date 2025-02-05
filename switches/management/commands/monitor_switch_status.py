"""Management command to monitor switch status."""

import time
import socket
import threading
from django.core.management.base import BaseCommand
from django.utils import timezone
from switches.models import Switch
import requests
from requests.exceptions import RequestException, SSLError
import logging
from urllib3.exceptions import InsecureRequestWarning
import time

# Suppress only the single InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logger = logging.getLogger(__name__)


class StatusMonitorThread(threading.Thread):
    """Thread to monitor switch status."""

    def __init__(self, *args, **kwargs):
        """Initialize the thread."""
        self.interval = kwargs.pop("interval", 30)  # Default 30 second interval
        self.stop_event = threading.Event()
        super().__init__(*args, **kwargs)
        self.daemon = True

    def authenticate_switch(self, switch, ip):
        """Attempt to authenticate with the switch."""
        try:
            start_time = time.time()
            response = requests.post(
                f"https://{ip}:49151/api/v1/auth",
                json={"username": switch.username, "password": switch.password},
                timeout=(3, 7),  # (connect timeout, read timeout)
                verify=False,  # Required for self-signed certs
                headers={
                    "Connection": "close",  # Prevent connection pooling issues
                    "User-Agent": "NetCtrl-StatusMonitor/1.0",
                },
            )
            response_time = (time.time() - start_time) * 1000  # Convert to milliseconds

            if response.status_code == 200:
                return True, response_time, None
            else:
                return (
                    False,
                    response_time,
                    f"Authentication failed: {response.status_code}",
                )
        except Exception as e:
            return False, None, str(e)

    def check_interface(self, switch, interface):
        """Check status of a specific interface."""
        ip = getattr(switch, f"{interface}_ip")
        error_type = Switch.ERROR_NONE
        error_detail = ""
        response_time = None

        try:
            # First try a simple TCP connection to port 49151
            start_time = time.time()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)  # 3 second timeout for initial connection

            try:
                sock.connect((ip, 49151))
                sock.close()
                tcp_response_time = (
                    time.time() - start_time
                ) * 1000  # Convert to milliseconds

                # If TCP succeeds, try authentication
                auth_success, auth_response_time, auth_error = self.authenticate_switch(
                    switch, ip
                )
                if auth_success:
                    response_time = auth_response_time
                    old_status = switch.update_interface_status(
                        interface,
                        Switch.STATUS_UP,
                        error_type=Switch.ERROR_NONE,
                        response_time=response_time,
                    )
                    logger.info(
                        f"Switch {switch.name} {interface} is UP (response time: {response_time:.2f}ms)"
                    )
                else:
                    response_time = tcp_response_time
                    error_type = Switch.ERROR_AUTH_FAILED
                    error_detail = auth_error
                    old_status = switch.update_interface_status(
                        interface,
                        Switch.STATUS_DEGRADED,
                        error_type=error_type,
                        error_detail=error_detail,
                        response_time=response_time,
                    )
                    logger.warning(
                        f"Switch {switch.name} {interface} authentication failed: {error_detail}"
                    )
            except (socket.timeout, socket.error) as e:
                # If TCP fails, mark as DOWN
                error_type = Switch.ERROR_NO_RESPONSE
                error_detail = str(e)
                old_status = switch.update_interface_status(
                    interface,
                    Switch.STATUS_DOWN,
                    error_type=error_type,
                    error_detail=error_detail,
                )
                logger.error(
                    f"Switch {switch.name} {interface} is unreachable: {error_detail}"
                )
        except Exception as e:
            error_type = Switch.ERROR_API
            error_detail = str(e)
            old_status = switch.update_interface_status(
                interface,
                Switch.STATUS_DOWN,
                error_type=error_type,
                error_detail=error_detail,
            )
            logger.error(
                f"Unexpected error checking {switch.name} {interface}: {error_detail}"
            )

    def check_all_switches(self):
        """Check status of all switches."""
        switches = Switch.objects.all()
        for switch in switches:
            # Check both interfaces in parallel using threads
            in_band_thread = threading.Thread(
                target=self.check_interface, args=(switch, "in_band")
            )
            out_band_thread = threading.Thread(
                target=self.check_interface, args=(switch, "out_band")
            )

            in_band_thread.start()
            out_band_thread.start()

            in_band_thread.join()
            out_band_thread.join()

    def run(self):
        """Run the monitoring thread."""
        logger.info("Starting switch status monitoring")
        while not self.stop_event.is_set():
            try:
                self.check_all_switches()
            except Exception as e:
                logger.error(f"Error in status monitoring: {str(e)}")
            finally:
                # Wait for the specified interval or until stopped
                self.stop_event.wait(self.interval)

        logger.info("Switch status monitoring stopped")

    def stop(self):
        """Stop the monitoring thread."""
        self.stop_event.set()


class Command(BaseCommand):
    """Django management command to run the switch status monitor."""

    help = "Runs the switch status monitoring daemon"

    def add_arguments(self, parser):
        """Add command arguments."""
        parser.add_argument(
            "--interval",
            type=int,
            default=30,
            help="Polling interval in seconds (default: 30)",
        )

    def handle(self, *args, **options):
        """Handle the command execution."""
        try:
            monitor = StatusMonitorThread(interval=options["interval"])
            monitor.start()
            self.stdout.write(self.style.SUCCESS("Started switch status monitoring"))

            # Keep the main thread running
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("Stopping monitor..."))
            monitor.stop()
            monitor.join()
            self.stdout.write(self.style.SUCCESS("Monitor stopped"))
