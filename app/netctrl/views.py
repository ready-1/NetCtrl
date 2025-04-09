import json
import platform
import logging
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings

from .github_api import create_github_issue

logger = logging.getLogger(__name__)

# Issue templates
TEMPLATES = {
    'bug': """
## What happened?
[Describe the issue you encountered]

## What did you expect to happen?
[Describe what you expected]

## Steps to reproduce
1. 
2. 
3. 
""",
    'feature': """
## Feature description
[Describe the feature you'd like to see]

## Why is this valuable?
[Explain why this feature would be useful]
""",
    'question': """
## Your question
[What would you like to know?]

## What you've already tried
[Have you looked for answers elsewhere? What did you find?]
"""
}

@require_POST
def submit_issue(request):
    """Handle issue submission with telemetry"""
    try:
        # Parse JSON data
        data = json.loads(request.body)
        issue_type = data.get('issue_type', 'bug')
        title = data.get('title')
        description = data.get('description')
        
        if not title or not description:
            return JsonResponse({
                'success': False,
                'error': 'Title and description are required'
            }, status=400)
        
        # Collect telemetry
        telemetry = {
            'app_version': getattr(settings, 'APP_VERSION', '1.0.0'),
            'server_os': platform.platform(),
            'python_version': platform.python_version(),
            'username': request.user.username if request.user.is_authenticated else 'Anonymous',
        }
        
        # Add browser info
        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
        telemetry['user_agent'] = user_agent
        
        # Add current URL
        telemetry['current_url'] = request.META.get('HTTP_REFERER', 'Unknown')
        
        # Format issue with telemetry
        telemetry_section = "\n\n## System Information\n"
        for key, value in telemetry.items():
            telemetry_section += f"- **{key}**: {value}\n"
        
        full_description = description + telemetry_section
        
        # Create labels based on issue type
        labels = [issue_type]
        
        # Submit to GitHub
        result = create_github_issue(title, full_description, labels)
        
        if result['success']:
            logger.info(f"Issue submitted: {title}")
            return JsonResponse({
                'success': True,
                'issue_url': result['url'],
                'message': f'Issue #{result["issue_number"]} created successfully'
            })
        else:
            logger.warning(f"Issue submission failed: {result['error']}")
            return JsonResponse({
                'success': False,
                'error': result['error']
            }, status=500)
            
    except ValueError as e:
        # Invalid JSON
        logger.error(f"Invalid JSON in request: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'Invalid request format'
        }, status=400)
    except Exception as e:
        # Catch-all for other errors
        logger.exception("Unexpected error in submit_issue")
        return JsonResponse({
            'success': False,
            'error': f"An unexpected error occurred: {str(e)}"
        }, status=500)

@ensure_csrf_cookie
def get_issue_templates(request):
    """Return template suggestions for different issue types"""
    return JsonResponse({'templates': TEMPLATES})
