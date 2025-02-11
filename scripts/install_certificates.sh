#!/bin/bash

# Check if switch name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <switch_name>"
    exit 1
fi

SWITCH_NAME="$1"
CERTS_DIR="../certificates"
SWITCH_IP=$(python -c "from django.core.management import execute_from_command_line; import os, sys; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netctrl.settings'); from switches.models import Switch; print(Switch.objects.get(name='$SWITCH_NAME').in_band_ip)" 2>/dev/null)

if [ -z "$SWITCH_IP" ]; then
    echo "Error: Could not find switch $SWITCH_NAME"
    exit 1
fi

echo "Installing certificates for $SWITCH_NAME ($SWITCH_IP)..."

# Copy certificates to switch
scp "$CERTS_DIR/$SWITCH_NAME.key" "admin@$SWITCH_IP:/etc/ssl/private/"
scp "$CERTS_DIR/$SWITCH_NAME.crt" "admin@$SWITCH_IP:/etc/ssl/certs/"
scp "$CERTS_DIR/ca.crt" "admin@$SWITCH_IP:/etc/ssl/certs/"

# Configure switch to use certificates
ssh "admin@$SWITCH_IP" << EOF
configure terminal
crypto pki import-certificate ca.crt
crypto pki import-certificate $SWITCH_NAME.crt
crypto key import $SWITCH_NAME.key
crypto ssl profile default
certificate $SWITCH_NAME.crt
private-key $SWITCH_NAME.key
exit
EOF

echo "Certificate installation complete for $SWITCH_NAME"
