import os
import time
import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

def create_github_issue(title, description, labels=None, rate_limit_wait=True):
    """
    Create a GitHub issue with comprehensive error handling
    
    Args:
        title: Issue title
        description: Issue body/description
        labels: List of labels to apply (optional)
        rate_limit_wait: Whether to wait and retry on rate limits (default: True)
        
    Returns:
        dict: Result with success status and issue URL if successful
    """
    # Get credentials from settings with fallback to environment variables
    token = getattr(settings, 'GITHUB_TOKEN', os.environ.get('GITHUB_TOKEN'))
    repo = getattr(settings, 'GITHUB_REPOSITORY', os.environ.get('GITHUB_REPOSITORY'))
    
    # Extract just the repo name if full URL was provided
    if repo and 'github.com/' in repo:
        repo = repo.split('github.com/')[-1]
        # Remove .git suffix if present
        if repo.endswith('.git'):
            repo = repo[:-4]
    
    if not token:
        logger.error("Missing GitHub token configuration")
        return {
            'success': False,
            'error': "Missing GitHub token configuration. Add GITHUB_TOKEN to environment or settings."
        }
    
    if not repo:
        logger.error("Missing GitHub repository configuration")
        return {
            'success': False,
            'error': "Missing GitHub repository configuration. Add GITHUB_REPOSITORY to environment or settings."
        }
    
    # Prepare API request
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Prepare data
    data = {
        'title': title,
        'body': description
    }
    
    if labels:
        data['labels'] = labels
    
    # Submit to GitHub with error handling
    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        
        # Handle rate limiting
        if response.status_code == 403 and 'X-RateLimit-Remaining' in response.headers:
            if int(response.headers['X-RateLimit-Remaining']) == 0 and rate_limit_wait:
                wait_time = int(response.headers.get('X-RateLimit-Reset', 0)) - int(time.time())
                if wait_time > 0 and wait_time < 300:  # Only wait if reasonable (<5 min)
                    logger.warning(f"GitHub API rate limited. Waiting {wait_time} seconds")
                    time.sleep(wait_time + 1)
                    # Retry once
                    return create_github_issue(title, description, labels, False)
        
        # Raise exception for other HTTP errors
        response.raise_for_status()
        
        # Parse successful response
        issue_data = response.json()
        logger.info(f"GitHub issue created: #{issue_data['number']}")
        
        return {
            'success': True,
            'issue_number': issue_data['number'],
            'url': issue_data['html_url']
        }
    except requests.exceptions.RequestException as e:
        logger.error(f"GitHub API error: {str(e)}")
        return {
            'success': False,
            'error': f"GitHub API error: {str(e)}"
        }
