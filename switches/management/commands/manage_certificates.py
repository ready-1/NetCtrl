"""Management command to generate and manage SSL certificates for switches."""

import os
from datetime import datetime, timedelta
from pathlib import Path
import ipaddress

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from switches.models import Switch


class Command(BaseCommand):
    help = "Generate and manage SSL certificates for switches"

    def add_arguments(self, parser):
        parser.add_argument(
            "--switch",
            type=str,
            help="Name of the switch to generate certificate for. If not provided, generates for all switches.",
        )
        parser.add_argument(
            "--force",
            action="store_true",
            help="Force regenerate certificates even if they already exist",
        )

    def handle(self, *args, **options):
        # Create certificates directory if it doesn't exist
        certs_dir = Path(settings.BASE_DIR) / "certificates"
        certs_dir.mkdir(exist_ok=True)
        ca_key_path = certs_dir / "ca.key"
        ca_cert_path = certs_dir / "ca.crt"

        # Generate CA if it doesn't exist
        if not ca_cert_path.exists() or not ca_key_path.exists():
            self.stdout.write("Generating CA certificate...")
            ca_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
            )
            ca_name = x509.Name(
                [
                    x509.NameAttribute(NameOID.COMMON_NAME, "NetCtrl Root CA"),
                    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "NetCtrl"),
                ]
            )
            ca_cert = (
                x509.CertificateBuilder()
                .subject_name(ca_name)
                .issuer_name(ca_name)
                .public_key(ca_key.public_key())
                .serial_number(x509.random_serial_number())
                .not_valid_before(datetime.utcnow())
                .not_valid_after(datetime.utcnow() + timedelta(days=3650))  # 10 years
                .add_extension(
                    x509.BasicConstraints(ca=True, path_length=None),
                    critical=True,
                )
                .sign(ca_key, hashes.SHA256())
            )

            # Save CA private key
            with open(ca_key_path, "wb") as f:
                f.write(
                    ca_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.PKCS8,
                        encryption_algorithm=serialization.NoEncryption(),
                    )
                )

            # Save CA certificate
            with open(ca_cert_path, "wb") as f:
                f.write(ca_cert.public_bytes(serialization.Encoding.PEM))

        # Load CA key and certificate
        with open(ca_key_path, "rb") as f:
            ca_key = serialization.load_pem_private_key(f.read(), password=None)
        with open(ca_cert_path, "rb") as f:
            ca_cert = x509.load_pem_x509_certificate(f.read())

        # Get switches to process
        switches = Switch.objects.all()
        if options["switch"]:
            switches = switches.filter(name=options["switch"])
            if not switches.exists():
                raise CommandError(f"Switch {options['switch']} not found")

        for switch in switches:
            cert_path = certs_dir / f"{switch.name}.crt"
            key_path = certs_dir / f"{switch.name}.key"

            if cert_path.exists() and key_path.exists() and not options["force"]:
                self.stdout.write(
                    f"Certificates for {switch.name} already exist. Use --force to regenerate."
                )
                continue

            self.stdout.write(f"Generating certificates for {switch.name}...")

            # Generate key
            key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
            )

            # Generate CSR
            csr = (
                x509.CertificateSigningRequestBuilder()
                .subject_name(
                    x509.Name(
                        [
                            x509.NameAttribute(NameOID.COMMON_NAME, switch.name),
                            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "NetCtrl"),
                        ]
                    )
                )
                .add_extension(
                    x509.SubjectAlternativeName(
                        [
                            x509.DNSName(switch.name),
                            x509.IPAddress(ipaddress.ip_address(switch.in_band_ip)),
                        ]
                    ),
                    critical=False,
                )
                .sign(key, hashes.SHA256())
            )

            # Generate certificate
            cert = (
                x509.CertificateBuilder()
                .subject_name(csr.subject)
                .issuer_name(ca_cert.subject)
                .public_key(csr.public_key())
                .serial_number(x509.random_serial_number())
                .not_valid_before(datetime.utcnow())
                .not_valid_after(datetime.utcnow() + timedelta(days=365))
                .add_extension(
                    x509.BasicConstraints(ca=False, path_length=None),
                    critical=True,
                )
                .sign(ca_key, hashes.SHA256())
            )

            # Save private key
            with open(key_path, "wb") as f:
                f.write(
                    key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.PKCS8,
                        encryption_algorithm=serialization.NoEncryption(),
                    )
                )

            # Save certificate
            with open(cert_path, "wb") as f:
                f.write(cert.public_bytes(serialization.Encoding.PEM))

            self.stdout.write(
                self.style.SUCCESS(
                    f"Generated certificates for {switch.name} in {certs_dir}"
                )
            )
