"""Management command to test switch authentication."""

from django.core.management.base import BaseCommand
from django.utils import timezone
from switches.models import Switch
from switches.services import SwitchAuthService


class Command(BaseCommand):
    """Test switch authentication functionality."""

    help = "Test authentication with a switch"

    def add_arguments(self, parser):
        """Add command arguments."""
        parser.add_argument(
            "switch_id",
            type=int,
            help="ID of the switch to test authentication with",
        )

    def handle(self, *args, **options):
        """Handle the command."""
        try:
            # Get the switch
            switch = Switch.objects.get(id=options["switch_id"])
            self.stdout.write(f"Testing authentication for switch: {switch.name}")

            # Initialize auth service
            auth_service = SwitchAuthService()

            # Test authentication
            self.stdout.write("Attempting to authenticate...")
            success = auth_service.authenticate_switch(switch)

            if success:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully authenticated! Token expires: {switch.token_expires}"
                    )
                )

                # Test token check
                is_valid = auth_service.check_auth_status(switch)
                self.stdout.write(f"Token valid: {is_valid}")

                # Test logout
                self.stdout.write("Testing logout...")
                if auth_service.logout_switch(switch):
                    self.stdout.write(self.style.SUCCESS("Successfully logged out"))
                else:
                    self.stdout.write(self.style.ERROR("Error occurred during logout"))

            else:
                self.stdout.write(
                    self.style.ERROR(
                        f"Authentication failed. Status: {switch.auth_status}"
                    )
                )

        except Switch.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f"Switch with ID {options['switch_id']} not found")
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error occurred: {str(e)}"))
