#!/usr/bin/env python3
"""
Test script for NetCtrl Syslog Configuration
This script sends test entries to all configured log streams using Python's logging facility
"""

import logging
import logging.handlers
import socket
import datetime
import time

class TCPSysLogHandler(logging.Handler):
    """
    A custom handler that sends log messages to a syslog server using TCP
    
    This handler implements a direct TCP connection to syslog since the standard
    SysLogHandler in Python only supports UDP connections.
    """
    # Priority mappings from logging levels to syslog priority levels
    priority_map = {
        logging.DEBUG: 7,      # Debug: debug-level messages
        logging.INFO: 6,       # Informational: informational messages
        logging.WARNING: 4,    # Warning: warning conditions
        logging.ERROR: 3,      # Error: error conditions
        logging.CRITICAL: 2,   # Critical: critical conditions
    }
    
    def __init__(self, address=('localhost', 601), facility=logging.handlers.SysLogHandler.LOG_USER):
        """
        Initialize the handler with address tuple (host, port) and syslog facility
        """
        logging.Handler.__init__(self)
        self.address = address
        self.facility = facility
        self.sock = None
        
    def emit(self, record):
        """
        Emit a record by formatting it and sending it to the syslog server via TCP
        """
        try:
            # Format the record
            msg = self.format(record)
            
            # Calculate the priority value (facility * 8 + level)
            priority = self.facility * 8 + self.priority_map.get(record.levelno, 7)
            
            # Format the message according to RFC 3164
            timestamp = datetime.datetime.now().strftime("%b %d %H:%M:%S")
            syslog_msg = f"<{priority}>{timestamp} {msg}\n"
            
            # Create a new socket for each message to avoid connection issues
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(self.address)
            self.sock.sendall(syslog_msg.encode('utf-8'))
            self.sock.close()
            
        except Exception as e:
            self.handleError(record)
    
    def close(self):
        """
        Close the handler and any open socket
        """
        if self.sock:
            self.sock.close()
            self.sock = None
        logging.Handler.close(self)

# Configure TCP-based SysLogHandler
def setup_tcp_logger(name, facility=logging.handlers.SysLogHandler.LOG_USER):
    """Set up a logger that sends messages via TCP to syslog"""
    logger = logging.getLogger(f"{name}_tcp")
    logger.setLevel(logging.INFO)
    
    # Create custom TCP SysLog handler
    handler = TCPSysLogHandler(
        address=('localhost', 601),
        facility=facility
    )
    
    # Format: we need to include the tag in the message
    formatter = logging.Formatter(f'{name}: %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

# Configure UDP-based SysLogHandler
def setup_udp_logger(name, facility=logging.handlers.SysLogHandler.LOG_USER):
    """Set up a logger that sends messages via UDP to syslog"""
    logger = logging.getLogger(f"{name}_udp")
    logger.setLevel(logging.INFO)
    
    # Create SysLogHandler for UDP
    handler = logging.handlers.SysLogHandler(
        address=('localhost', 514),
        facility=facility,
        socktype=socket.SOCK_DGRAM
    )
    
    # Format: include the tag in the message
    formatter = logging.Formatter(f'{name}: %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

def main():
    """Main function to send test log messages using Python's logging facility"""
    print("Sending test log entries to NetCtrl Syslog Server using Python's logging facility...")
    
    # Set up loggers for different services
    nginx_tcp_logger = setup_tcp_logger("nginx")
    nginx_udp_logger = setup_udp_logger("nginx")
    
    django_tcp_logger = setup_tcp_logger("django")
    django_udp_logger = setup_udp_logger("django")
    
    gunicorn_udp_logger = setup_udp_logger("gunicorn")
    
    postgres_tcp_logger = setup_tcp_logger("postgres")
    postgres_udp_logger = setup_udp_logger("postgres")
    
    # 1. Nginx logs
    nginx_tcp_logger.info("TEST-TCP: GET /index.html 200 1024 - Response time 0.025s")
    print("Sent 'TEST-TCP: GET /index.html 200 1024 - Response time 0.025s' with tag 'nginx' via TCP port 601")
    
    nginx_udp_logger.info("TEST-UDP: POST /api/data 201 512 - Response time 0.137s")
    print("Sent 'TEST-UDP: POST /api/data 201 512 - Response time 0.137s' with tag 'nginx' via UDP port 514")
    
    nginx_tcp_logger.info("TEST-TCP: GET /static/css/main.css 304 0 - Response time 0.005s")
    print("Sent 'TEST-TCP: GET /static/css/main.css 304 0 - Response time 0.005s' with tag 'nginx' via TCP port 601")
    
    # 2. Django logs
    django_udp_logger.info("TEST-UDP: [INFO] Starting server on port 8000")
    print("Sent 'TEST-UDP: [INFO] Starting server on port 8000' with tag 'django' via UDP port 514")
    
    django_tcp_logger.info("TEST-TCP: [DEBUG] Processing request for /api/users/")
    print("Sent 'TEST-TCP: [DEBUG] Processing request for /api/users/' with tag 'django' via TCP port 601")
    
    gunicorn_udp_logger.info("TEST-UDP: Worker process ready for connections")
    print("Sent 'TEST-UDP: Worker process ready for connections' with tag 'gunicorn' via UDP port 514")
    
    # 3. Postgres logs
    postgres_tcp_logger.info("TEST-TCP: database system is ready to accept connections")
    print("Sent 'TEST-TCP: database system is ready to accept connections' with tag 'postgres' via TCP port 601")
    
    postgres_udp_logger.info("TEST-UDP: connection received: host=172.18.0.3 port=49876")
    print("Sent 'TEST-UDP: connection received: host=172.18.0.3 port=49876' with tag 'postgres' via UDP port 514")
    
    postgres_tcp_logger.info("TEST-TCP: transaction completed: INSERT INTO users VALUES (1, 'testuser')")
    print("Sent 'TEST-TCP: transaction completed: INSERT INTO users VALUES (1, 'testuser')' with tag 'postgres' via TCP port 601")
    
    # 4. Error logs
    nginx_tcp_logger.error("TEST-TCP: [error] 404 Not Found: /missing.html")
    print("Sent 'TEST-TCP: [error] 404 Not Found: /missing.html' with tag 'nginx' via TCP port 601")
    
    django_udp_logger.error("TEST-UDP: [ERROR] Exception in view: Database connection failed")
    print("Sent 'TEST-UDP: [ERROR] Exception in view: Database connection failed' with tag 'django' via UDP port 514")
    
    postgres_tcp_logger.error("TEST-TCP: ERROR: relation \"nonexistent_table\" does not exist")
    print("Sent 'TEST-TCP: ERROR: relation \"nonexistent_table\" does not exist' with tag 'postgres' via TCP port 601")
    
    # Add a small delay to ensure messages are processed
    time.sleep(0.5)
    
    print("\nTest log entries sent. Check the following:")
    print("1. Web viewer at http://localhost:8080/logs/")
    print("2. Individual log files inside the syslog container:")
    print("   - /var/log/nginx.log")
    print("   - /var/log/django.log")
    print("   - /var/log/postgres.log")
    print("   - /var/log/errors.log")
    print("   - /var/log/all.log")
    print("")
    print("To view logs inside container, run:")
    print("docker compose exec syslog cat /var/log/all.log")

if __name__ == "__main__":
    main()
