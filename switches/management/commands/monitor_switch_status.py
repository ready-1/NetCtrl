"""Management command to monitor switch status."""

import time
import threading
from django.core.management.base import BaseCommand
from django.utils import timezone
from switches.models import Switch
import requests
from requests.exceptions import RequestException
import logging

logger = logging.getLogger(__name__)


class StatusMonitorThread(threading.Thread):
    """Thread to monitor switch status."""

    def __init__(self, *args, **kwargs):
        """Initialize the thread."""
        self.interval = kwargs.pop("interval", 30)  # Default 30 second interval
        self.stop_event = threading.Event()
        super().__init__(*args, **kwargs)
        self.daemon = True

    def check_interface(self, switch, interface):
        """Check status of a specific interface."""
        ip = getattr(switch, f"{interface}_ip")
        try:
            # Simple TCP connection test to check if interface is responding
            response = requests.get(
                f"https://{ip}:49151/api/v1/system",
                timeout=5,
                verify=False,  # Required for self-signed certs
            )
            if response.status_code == 200:
                switch.update_interface_status(interface, Switch.STATUS_UP)
                logger.info(f"Switch {switch.name} {interface} is UP")
            else:
                switch.update_interface_status(interface, Switch.STATUS_DOWN)
                logger.warning(
                    f"Switch {switch.name} {interface} returned status code {response.status_code}"
                )
        except RequestException as e:
            switch.update_interface_status(interface, Switch.STATUS_DOWN)
            logger.error(f"Error checking {switch.name} {interface}: {str(e)}")

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
