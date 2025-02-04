"""Management command to import switches from CSV file."""

from django.core.management.base import BaseCommand, CommandError
import csv
from switches.models import Switch
from django.core.exceptions import ValidationError


class Command(BaseCommand):
    """Import switches from CSV file."""

    help = "Import switches from CSV file"

    def add_arguments(self, parser):
        """Add command arguments."""
        parser.add_argument("csv_file", type=str, help="Path to CSV file")
        parser.add_argument(
            "--username", default="admin", help="Default username for all switches"
        )
        parser.add_argument(
            "--password",
            default="FuseFuse123!",
            help="Default password for all switches",
        )
        parser.add_argument(
            "--update",
            action="store_true",
            help="Update existing switches instead of skipping",
        )

    def handle(self, *args, **options):
        """Handle the command execution."""
        try:
            with open(options["csv_file"]) as f:
                reader = csv.DictReader(f)

                # Verify required columns
                required_fields = ["name", "in_band_ip", "out_band_ip"]
                missing_fields = [
                    field for field in required_fields if field not in reader.fieldnames
                ]
                if missing_fields:
                    raise CommandError(
                        f"Missing required columns: {', '.join(missing_fields)}"
                    )

                created_count = 0
                updated_count = 0
                skipped_count = 0
                error_count = 0

                for row in reader:
                    try:
                        # Check if switch exists
                        switch, created = Switch.objects.get_or_create(
                            name=row["name"],
                            defaults={
                                "in_band_ip": row["in_band_ip"],
                                "out_band_ip": row["out_band_ip"],
                                "username": options["username"],
                                "password": options["password"],
                                "description": row.get("description", ""),
                            },
                        )

                        if not created and options["update"]:
                            # Update existing switch
                            switch.in_band_ip = row["in_band_ip"]
                            switch.out_band_ip = row["out_band_ip"]
                            switch.description = row.get("description", "")
                            switch.save()
                            self.stdout.write(
                                self.style.WARNING(f"Updated switch: {row['name']}")
                            )
                            updated_count += 1
                        elif not created:
                            self.stdout.write(
                                self.style.WARNING(
                                    f"Skipped existing switch: {row['name']}"
                                )
                            )
                            skipped_count += 1
                        else:
                            self.stdout.write(
                                self.style.SUCCESS(f"Created switch: {row['name']}")
                            )
                            created_count += 1

                    except ValidationError as e:
                        self.stderr.write(
                            self.style.ERROR(
                                f"Validation error for {row['name']}: {str(e)}"
                            )
                        )
                        error_count += 1
                    except Exception as e:
                        self.stderr.write(
                            self.style.ERROR(
                                f"Error processing {row['name']}: {str(e)}"
                            )
                        )
                        error_count += 1

                # Print summary
                self.stdout.write("\nImport Summary:")
                self.stdout.write(f"Created: {created_count}")
                self.stdout.write(f"Updated: {updated_count}")
                self.stdout.write(f"Skipped: {skipped_count}")
                self.stdout.write(f"Errors: {error_count}")

        except FileNotFoundError:
            raise CommandError(f"CSV file not found: {options['csv_file']}")
        except Exception as e:
            raise CommandError(f"Error reading CSV file: {str(e)}")
