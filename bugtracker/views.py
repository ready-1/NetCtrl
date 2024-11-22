from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from pathlib import Path
from django.conf import settings
from datetime import datetime, timezone

# Use QUEUE_FILE from settings
QUEUE_FILE = settings.BUG_QUEUE_FILE


def new_bug_request(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description", "")
        issue_type = request.POST.get("issue_type")
        submitter_name = request.POST.get("submitter_name")

        # Validate input
        if not title or not submitter_name or not issue_type:
            return JsonResponse(
                {"error": "All required fields must be completed."}, status=400
            )

        # Assign labels programmatically
        labels = [issue_type.lower(), "created-via-NetCtrl"]

        # Ensure the queue file exists
        if not QUEUE_FILE.parent.exists():
            QUEUE_FILE.parent.mkdir(parents=True, exist_ok=True)

        if not QUEUE_FILE.exists():
            with open(QUEUE_FILE, "w") as f:
                json.dump({"issues": []}, f, indent=4)

        # Load queue
        with open(QUEUE_FILE, "r") as f:
            queue_data = json.load(f)

        # Add to queue
        issue = {
            "title": title,
            "body": f"{description}\n\n**Submitted by:** {submitter_name}",
            "labels": labels,
            "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),  # ISO 8601 with Z
            "retry_count": 0,
            "status": "queued",
        }
        queue_data["issues"].append(issue)

        # Save queue
        with open(QUEUE_FILE, "w") as f:
            json.dump(queue_data, f, indent=4)

        return redirect("bugtracker:success")  # Redirect to a success page

    return render(request, "bugtracker/bug_form.html")

def success_page(request):
    return render(request, "bugtracker/success.html")