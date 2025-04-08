"""
NetCtrl Logging Configuration Module

This module provides a unified logging configuration for the NetCtrl application
sending logs to both local files and syslog server based on the current environment.
"""

import os
import logging
import logging.handlers
import socket
import datetime

class TCPSysLogHandler(logging.Handler):
    """
    A custom handler that sends log messages to a syslog server using TCP

    This handler implements a direct TCP connection to syslog since the standard
    SysLogHandler in Python only supports UDP connections properly.
    """
    # Priority mappings from logging levels to syslog priority levels
    priority_map = {
        logging.DEBUG: 7,      # Debug: debug-level messages
        logging.INFO: 6,       # Informational: informational messages
        logging.WARNING: 4,    # Warning: warning conditions
        logging.ERROR: 3,      # Error: error conditions
        logging.CRITICAL: 2    # Critical: critical conditions
    }

    def __init__(self, address=('localhost', 601), facility=logging.handlers.SysLogHandler.LOG_LOCAL0):
        """
        Initialize the handler with address tuple (host, port) and syslog facility
        """
        logging.Handler.__init__(self)
        self.address = address
        # Convert facility to integer if it's a string
        if isinstance(facility, str):
            if hasattr(logging.handlers.SysLogHandler, facility):
                self.facility = getattr(logging.handlers.SysLogHandler, facility)
            else:
                self.facility = logging.handlers.SysLogHandler.LOG_LOCAL0
        else:
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
            hostname = socket.gethostname()
            syslog_msg = f"<{priority}>{timestamp} {hostname} {msg}\n"

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

# Log levels
DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

# Environment variables
SYSLOG_HOST = os.environ.get('SYSLOG_HOST', 'syslog')
SYSLOG_PORT = int(os.environ.get('SYSLOG_PORT', 601))
APP_ENV = os.environ.get('APP_ENV', 'development')
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
HOSTNAME = socket.gethostname()

# Mapping of string log levels to actual log levels
LOG_LEVEL_MAP = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}

def get_log_level():
    """Get log level from environment variable"""
    return LOG_LEVEL_MAP.get(LOG_LEVEL.upper(), logging.INFO)

def configure_logging(name='netctrl', service_tag=None):
    """
    Configure logging for the application

    Args:
        name: The logger name defaults to 'netctrl'
        service_tag: Optional service tag to identify the service in logs
                    (e.g. 'django', 'gunicorn', etc.)

    Returns:
        A configured logger object
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(get_log_level())

    # Clear any existing handlers
    if logger.handlers:
        logger.handlers = []

    # Set up formatting
    tag = service_tag if service_tag else name
    formatter = logging.Formatter(
        f'%(asctime)s [{tag}] [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console handler for local development
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Syslog handler for production
    try:
        # Set up custom TCP syslog handler
        syslog_formatter = logging.Formatter(f'{tag}: [%(levelname)s] %(message)s')
        syslog_handler = TCPSysLogHandler(
            address=(SYSLOG_HOST, SYSLOG_PORT),
            facility=logging.handlers.SysLogHandler.LOG_LOCAL0
        )
        syslog_handler.setFormatter(syslog_formatter)
        logger.addHandler(syslog_handler)
    except (socket.error, socket.gaierror) as e:
        # Log the error to console but don't crash the application
        console_handler.setLevel(logging.ERROR)
        logger.error(f"Failed to connect to syslog server: {e}")

    return logger

def get_logger(name='netctrl', service_tag=None):
    """
    Get a configured logger with the given name

    This is the main function to use throughout the application.

    Usage:
        from netctrl.logging_config import get_logger

        # In Django views
        logger = get_logger(__name__, 'django')
        logger.info('Processing request')

        # In background tasks
        task_logger = get_logger('tasks', 'celery')
        task_logger.info('Starting background task')

    Args:
        name: The logger name defaults to 'netctrl'
        service_tag: Optional service tag to identify the service in logs

    Returns:
        A configured logger object
    """
    return configure_logging(name, service_tag)
