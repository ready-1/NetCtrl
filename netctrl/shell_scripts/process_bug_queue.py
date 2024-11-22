import json
import os
import requests
import logging
from logging.handlers import SysLogHandler  # Explicitly import SysLogHandler
from datetime import datetime

# Constants
QUEUE_FILE = "/srv/NetCtrl/netctrl/data/bug_queue.json"
TOKEN_FILE = "/srv/NetCtrl/netctrl/shell_scripts/.gh_token"
REPO_API = "https://api.github.com/repos/ready-1/NetCtrl/issues"

# Configure rsyslog
LOG_IDENTIFIER = "NetCtrl_BugTracker"
logging.basicConfig(
    level=logging.INFO,
    format=f"%(asctime)s {LOG_IDENTIFIER}[%(process)d]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        SysLogHandler(address="/dev/log")  # Correct import and usage
    ],
)
logger = logging.getLogger(LOG_IDENTIFIER)

# Load GitHub token
def load_token(token_file):
    if not os.path.isfile(token_file):
        logger.error(f"Token file not found at {token_file}")
        return None
    with open(token_file, "r") as file:
        return file.read().strip()

# Load JSON queue
def load_queue(queue_file):
    if not os.path.isfile(queue_file):
        logger.error(f"Queue file not found at {queue_file}")
        return None
    with open(queue_file, "r") as file:
        return json.load(file)

# Save updated queue
def save_queue(queue_file, data):
    with open(queue_file, "w") as file:
        json.dump(data, file, indent=4)

# Send issue to GitHub
def send_to_github(token, issue):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    response = requests.post(REPO_API, headers=headers, json=issue)
    return response

# Process queue
def process_queue():
    logger.info("Starting bug tracker queue processing...")

    token = load_token(TOKEN_FILE)
    if not token:
        return

    queue = load_queue(QUEUE_FILE)
    if not queue or "issues" not in queue:
        logger.info("No issues found in the queue.")
        return

    remaining_issues = []
    for issue in queue["issues"]:
        logger.info(f"Processing issue: {issue['title']}")

        clean_body = issue["body"].replace("\\r\\n", "\n").replace("\\n", "\n")
        issue_payload = {
            "title": issue["title"],
            "body": clean_body,
            "labels": issue["labels"],
        }

        response = send_to_github(token, issue_payload)
        if response.status_code == 201:
            logger.info(f"Successfully created issue: {issue['title']}")
        else:
            logger.error(f"Failed to create issue: {issue['title']}, "
                         f"Response: {response.status_code}, {response.text}")
            issue["retry_count"] += 1
            remaining_issues.append(issue)

    # Save remaining issues back to the queue
    queue["issues"] = remaining_issues
    save_queue(QUEUE_FILE, queue)
    logger.info("Queue processing complete.")

# Entry point
if __name__ == "__main__":
    process_queue()