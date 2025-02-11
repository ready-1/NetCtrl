# SSL Certificate Management

This document describes how to manage SSL certificates for secure communication with network switches.

## Overview

NetCtrl uses a Certificate Authority (CA) to generate and manage SSL certificates for each switch. This ensures secure communication between the application and the switches.

## Generating Certificates

### 1. Generate CA Certificate

The first time you run the certificate management command, it will automatically generate a CA certificate if one doesn't exist:

```bash
python manage.py manage_certificates
```

This creates:
- `certificates/ca.key` - CA private key
- `certificates/ca.crt` - CA certificate

### 2. Generate Switch Certificates

To generate certificates for a specific switch:

```bash
python manage.py manage_certificates --switch ENG-SW1
```

This creates:
- `certificates/ENG-SW1.key` - Switch private key
- `certificates/ENG-SW1.crt` - Switch certificate

To generate certificates for all switches:

```bash
python manage.py manage_certificates
```

### 3. Force Regenerate Certificates

To force regenerate certificates even if they already exist:

```bash
python manage.py manage_certificates --switch ENG-SW1 --force
```

## Installing Certificates on Switches

1. Copy the generated certificate files to the switch:
   ```bash
   scp certificates/ENG-SW1.key admin@<switch-ip>:/etc/ssl/private/
   scp certificates/ENG-SW1.crt admin@<switch-ip>:/etc/ssl/certs/
   scp certificates/ca.crt admin@<switch-ip>:/etc/ssl/certs/
   ```

2. Configure the switch to use the certificates:
   ```bash
   # On the switch
   configure terminal
   crypto pki import-certificate ca.crt
   crypto pki import-certificate ENG-SW1.crt
   crypto key import ENG-SW1.key
   crypto ssl profile default
   certificate ENG-SW1.crt
   private-key ENG-SW1.key
   exit
   ```

## Troubleshooting

1. If you see SSL verification errors in the logs, ensure:
   - The CA certificate exists in the `certificates` directory
   - The switch's certificate and private key exist
   - The certificates are properly installed on the switch

2. To verify certificate installation on a switch:
   ```bash
   # On the switch
   show crypto certificates
   show crypto ssl profiles
   ```

3. To check certificate expiration:
   ```bash
   openssl x509 -in certificates/ENG-SW1.crt -text -noout | grep "Not After"
   ```
