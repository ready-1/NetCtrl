#!/bin/bash

# Test script for NetCtrl Syslog Configuration
# This script sends test entries to all configured log streams

echo "Sending test log entries to NetCtrl Syslog Server..."

# Function to send a log message via TCP to syslog
send_syslog_tcp() {
    local TAG=$1
    local MESSAGE=$2
    # Port 601 is mapped directly to the syslog-ng container
    echo "<14>$(date "+%b %d %H:%M:%S") $TAG: $MESSAGE" | nc localhost 601
    echo "Sent '$MESSAGE' with tag '$TAG' via TCP port 601"
}

# Function to send a log message via UDP to syslog
send_syslog_udp() {
    local TAG=$1
    local MESSAGE=$2
    # Port 514 is mapped directly to the syslog-ng container
    echo "<14>$(date "+%b %d %H:%M:%S") $TAG: $MESSAGE" | nc -u localhost 514
    echo "Sent '$MESSAGE' with tag '$TAG' via UDP port 514"
}

# Create some test log entries for each service

# Send logs using both TCP and UDP for better test coverage

# 1. Nginx logs (tag: nginx)
send_syslog_tcp "nginx" "TEST-TCP: GET /index.html 200 1024 - Response time 0.025s"
send_syslog_udp "nginx" "TEST-UDP: POST /api/data 201 512 - Response time 0.137s"
send_syslog_tcp "nginx" "TEST-TCP: GET /static/css/main.css 304 0 - Response time 0.005s"

# 2. Django logs (tag: django)
send_syslog_udp "django" "TEST-UDP: [INFO] Starting server on port 8000"
send_syslog_tcp "django" "TEST-TCP: [DEBUG] Processing request for /api/users/"
send_syslog_udp "gunicorn" "TEST-UDP: Worker process ready for connections"

# 3. Postgres logs (tag: postgres)
send_syslog_tcp "postgres" "TEST-TCP: database system is ready to accept connections"
send_syslog_udp "postgres" "TEST-UDP: connection received: host=172.18.0.3 port=49876"
send_syslog_tcp "postgres" "TEST-TCP: transaction completed: INSERT INTO users VALUES (1, 'testuser')"

# 4. Error logs (these should appear in both service-specific and error logs)
send_syslog_tcp "nginx" "TEST-TCP: [error] 404 Not Found: /missing.html"
send_syslog_udp "django" "TEST-UDP: [ERROR] Exception in view: Database connection failed"
send_syslog_tcp "postgres" "TEST-TCP: ERROR: relation \"nonexistent_table\" does not exist"

echo "Test log entries sent. Check the following:"
echo "1. Web viewer at http://localhost:8080"
echo "2. Individual log files inside the syslog container:"
echo "   - /var/log/nginx.log"
echo "   - /var/log/django.log"
echo "   - /var/log/postgres.log"
echo "   - /var/log/errors.log"
echo "   - /var/log/all.log"
echo ""
echo "To view logs inside container, run:"
echo "docker compose exec syslog cat /var/log/all.log"
