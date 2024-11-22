#!/bin/bash

# Debugging
set -x  # Enable shell debugging
exec > >(tee -i /var/log/bugtracker_debug.log) 2>&1  # Log output

QUEUE_FILE="/srv/NetCtrl/netctrl/data/bug_queue.json"
TOKEN_FILE="/srv/NetCtrl/netctrl/shell_scripts/.gh_token"
REPO_API="https://api.github.com/repos/ready-1/NetCtrl/issues"

if [[ ! -f "$QUEUE_FILE" ]]; then
    echo "Error: Queue file not found at $QUEUE_FILE"
    exit 1
fi

if [[ ! -f "$TOKEN_FILE" ]]; then
    echo "Error: GitHub token file not found at $TOKEN_FILE"
    exit 1
fi

echo "Validating JSON structure..."
if ! jq empty "$QUEUE_FILE"; then
    echo "Error: Invalid JSON structure in $QUEUE_FILE."
    exit 1
fi

echo "Processing issues..."
jq -c '.issues[]' "$QUEUE_FILE" | while IFS= read -r issue; do
    echo "Processing issue: $issue"

    # Extract fields
    title=$(echo "$issue" | jq -r '.title')
    body=$(echo "$issue" | jq -r '.body')
    labels=$(echo "$issue" | jq -c '.labels')
    created_at=$(echo "$issue" | jq -r '.created_at')
    retry_count=$(echo "$issue" | jq -r '.retry_count')
    status=$(echo "$issue" | jq -r '.status')

    # Sanitize the body field to remove problematic control characters
    clean_body=$(echo "$body" | sed 's/\\r\\n/\n/g')

    # Debug extracted and cleaned fields
    echo "Title: $title"
    echo "Body: $clean_body"
    echo "Labels: $labels"
    echo "Created At: $created_at"
    echo "Retry Count: $retry_count"
    echo "Status: $status"

    # Make the API call
    echo "Sending issue to GitHub..."
    response=$(curl -s -w "%{http_code}" -o /tmp/gh_response.json -X POST \
        -H "Authorization: Bearer $(cat "$TOKEN_FILE")" \
        -H "Content-Type: application/json" \
        -d "{
            \"title\": \"$title\",
            \"body\": \"$clean_body\",
            \"labels\": $labels
        }" \
        "$REPO_API")

    http_code="${response:(-3