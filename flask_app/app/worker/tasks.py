import time
import logging
import requests
from celery import shared_task
from celery.utils.log import get_task_logger
import redis
import json

# Set up logging
logger = get_task_logger(__name__)

# Disable SSL warnings for requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@shared_task(
    bind=True,
    max_retries=3,
    default_retry_delay=60,
    queue='config'
)
def poll_switches_config(self):
    """
    Poll switches for configuration data using the OpenAPI client.
    Stores results in PostgreSQL database.
    
    This task runs every 5 minutes.
    """
    from app import db
    from app.models.switch import Switch
    from openapi_client.api.authentication_api import AuthenticationApi
    from openapi_client.api.device_settings_api import DeviceSettingsApi
    from openapi_client.configuration import Configuration
    from openapi_client.api_client import ApiClient
    import os
    
    logger.info("Starting configuration polling for all switches...")
    
    # Get all active switches
    switches = Switch.query.filter_by(is_active=True).all()
    logger.info(f"Found {len(switches)} active switches to poll")
    
    for switch in switches:
        try:
            # Create API configuration
            config = Configuration(
                host=f"https://{switch.ip_address}"
            )
            config.verify_ssl = False
            
            # Get default credentials from environment
            default_username = os.environ.get('SWITCH_DEFAULT_USERNAME', 'admin')
            default_password = os.environ.get('SWITCH_DEFAULT_PASSWORD', '')
            
            # Use switch credentials if available, otherwise use defaults
            username = switch.username or default_username
            password = switch.password or default_password
            
            # Create API client
            with ApiClient(config) as api_client:
                # Authenticate
                auth_api = AuthenticationApi(api_client)
                login_result = auth_api.login_post(
                    {"username": username, "password": password}
                )
                
                # Store authentication token
                api_client.default_headers['Authorization'] = f"Bearer {login_result.token}"
                
                # Get device information
                device_api = DeviceSettingsApi(api_client)
                device_info = device_api.device_info_get()
                
                # Update switch information in database
                switch.name = device_info.name
                switch.firmware_version = device_info.firmware_version
                switch.model = device_info.model
                switch.serial_number = device_info.service_tag
                switch.last_polled = db.func.now()
                switch.status = "online"
                
                # Save to database
                db.session.commit()
                
                # Log out
                auth_api.logout_post()
                
                logger.info(f"Successfully polled switch {switch.name} ({switch.ip_address})")
                
        except Exception as exc:
            # Mark switch as offline
            switch.status = "offline"
            switch.last_error = str(exc)
            db.session.commit()
            
            logger.error(f"Error polling switch {switch.ip_address}: {str(exc)}")
            
            # Retry the task
            raise self.retry(exc=exc)
    
    logger.info("Completed configuration polling for all switches")
    return {"status": "completed", "switches_polled": len(switches)}


@shared_task(
    bind=True,
    max_retries=3,
    default_retry_delay=30,
    queue='metrics'
)
def poll_switches_metrics(self):
    """
    Poll switches for real-time metrics using SNMP.
    Stores results in Redis with TTL.
    
    This task runs every minute.
    """
    import os
    from app.models.switch import Switch
    import redis
    from pysnmp.hlapi import (
        SnmpEngine, CommunityData, UdpTransportTarget,
        ContextData, ObjectType, ObjectIdentity, getCmd
    )
    
    logger.info("Starting metrics polling for all switches...")
    
    # Connect to Redis
    redis_url = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
    r = redis.from_url(redis_url)
    
    # Get all active switches
    switches = Switch.query.filter_by(is_active=True).all()
    logger.info(f"Found {len(switches)} active switches to poll for metrics")
    
    # OIDs to poll
    interface_oids = {
        'ifInOctets': '1.3.6.1.2.1.2.2.1.10',
        'ifOutOctets': '1.3.6.1.2.1.2.2.1.16',
        'ifInErrors': '1.3.6.1.2.1.2.2.1.14',
        'ifOutErrors': '1.3.6.1.2.1.2.2.1.20',
        'ifOperStatus': '1.3.6.1.2.1.2.2.1.8',
    }
    
    for switch in switches:
        try:
            # Use switch SNMP community if available, otherwise use default
            community = switch.snmp_community or 'public'
            
            # Prepare metrics dictionary
            metrics = {
                'timestamp': time.time(),
                'interfaces': {}
            }
            
            # Poll each interface for each OID
            for port in range(1, 49):  # Assuming up to 48 ports
                port_metrics = {}
                
                for name, oid in interface_oids.items():
                    # Construct the full OID with port index
                    full_oid = f"{oid}.{port}"
                    
                    # Perform SNMP GET
                    error_indication, error_status, error_index, var_binds = next(
                        getCmd(
                            SnmpEngine(),
                            CommunityData(community),
                            UdpTransportTarget((switch.ip_address, 161)),
                            ContextData(),
                            ObjectType(ObjectIdentity(full_oid))
                        )
                    )
                    
                    if error_indication:
                        logger.warning(f"SNMP error for {switch.ip_address}: {error_indication}")
                        continue
                    elif error_status:
                        logger.warning(f"SNMP error: {error_status.prettyPrint()}")
                        continue
                    
                    # Extract the value
                    for var_bind in var_binds:
                        value = var_bind[1]
                        port_metrics[name] = int(value)
                
                # Store interface metrics if any were collected
                if port_metrics:
                    metrics['interfaces'][f"port{port}"] = port_metrics
            
            # Store in Redis with TTL of 5 minutes
            r.setex(
                f"switch:{switch.id}:metrics",
                300,  # TTL in seconds
                json.dumps(metrics)
            )
            
            logger.info(f"Successfully collected metrics for switch {switch.name} ({switch.ip_address})")
            
        except Exception as exc:
            logger.error(f"Error polling metrics for switch {switch.ip_address}: {str(exc)}")
            # Retry the task
            raise self.retry(exc=exc)
    
    logger.info("Completed metrics polling for all switches")
    return {"status": "completed", "switches_polled": len(switches)}


@shared_task(queue='default')
def cleanup_old_metrics():
    """
    Cleanup task for old metrics in Redis.
    Automatically removes metrics older than the retention period.
    """
    # This is handled by Redis TTL, but this task can be used
    # for additional cleanup if needed
    logger.info("Metrics cleanup is handled by Redis TTL, no action needed")
    return {"status": "completed"}
