"""
GitHub API integration for NetCtrl.

This module provides functionality to interact with the GitHub API,
including creating issues, managing repositories, and other GitHub-related tasks.
"""
import os
import time
import requests
import logging
from django.conf import settings

# Import environment management functions
try:
    from netctrl.env_config import get_env_var, is_placeholder
except ImportError:
    # Fallback if env_config is not available
    def get_env_var(name, default=None, **kwargs):
        return getattr(settings, name, os.environ.get(name, default))
    
    def is_placeholder(value):
        """Simple placeholder detection if env_config is not available"""
        if not isinstance(value, str):
            return False
        placeholders = ['your-token-here', 'replace-with', 'example']
        return any(ph in value.lower() for ph in placeholders)

# Configure module logger
logger = logging.getLogger("netctrl.github")

class GitHubAPIError(Exception):
    """Exception raised for GitHub API errors"""
    def __init__(self, message, status_code=None, response=None):
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(self.message)

def get_github_credentials():
    """
    Get GitHub API credentials with validation.
    
    Returns:
        tuple: (token, repo, is_valid) where is_valid is a boolean indicating 
               if the credentials are valid and complete
    """
    # Get credentials from environment with validation
    token = get_env_var('GITHUB_TOKEN', default=None)
    repo = get_env_var('GITHUB_REPOSITORY', default="ready-1/NetCtrl")
    
    # Check for placeholder or missing token
    if not token or is_placeholder(token):
        logger.warning("GitHub token is missing or contains a placeholder value")
        token = None
    
    # Extract just the repo name if full URL was provided
    if repo and 'github.com/' in repo:
        repo = repo.split('github.com/')[-1]
        # Remove .git suffix if present
        if repo.endswith('.git'):
            repo = repo[:-4]
    
    # Validate repo format
    if not repo or not ('/' in repo):
        logger.warning(f"Invalid GitHub repository format: {repo}")
        return None, None, False
    
    return token, repo, bool(token and repo)

def create_github_issue(title, description, labels=None, rate_limit_wait=True):
    """
    Create a GitHub issue with comprehensive error handling and validation.
    
    Args:
        title: Issue title
        description: Issue body/description
        labels: List of labels to apply (optional)
        rate_limit_wait: Whether to wait and retry on rate limits (default: True)
        
    Returns:
        dict: Result with success status and issue URL if successful
    """
    # Get and validate credentials
    token, repo, is_valid = get_github_credentials()
    
    if not is_valid:
        error_msg = "GitHub integration disabled - Invalid or missing credentials"
        logger.error(error_msg)
        return {
            'success': False,
            'error': error_msg,
            'status': 'disabled'
        }
    
    # Prepare API request
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Input validation
    if not title or not title.strip():
        error_msg = "Issue title cannot be empty"
        logger.error(error_msg)
        return {'success': False, 'error': error_msg}
    
    # Prepare request data
    data = {
        'title': title,
        'body': description or "No description provided"
    }
    
    if labels:
        if isinstance(labels, str):
            labels = [label.strip() for label in labels.split(',') if label.strip()]
        data['labels'] = labels
    
    # Submit to GitHub with error handling
    try:
        logger.info(f"Creating GitHub issue in repository {repo}: {title}")
        response = requests.post(url, headers=headers, json=data, timeout=15)
        
        # Handle rate limiting
        if response.status_code == 403 and 'X-RateLimit-Remaining' in response.headers:
            remaining = int(response.headers.get('X-RateLimit-Remaining', '0'))
            
            if remaining == 0 and rate_limit_wait:
                reset_time = int(response.headers.get('X-RateLimit-Reset', '0'))
                wait_time = reset_time - int(time.time())
                
                if 0 < wait_time < 300:  # Only wait if reasonable (<5 min)
                    logger.warning(f"GitHub API rate limited. Waiting {wait_time} seconds")
                    time.sleep(wait_time + 1)
                    # Retry once with rate_limit_wait=False to avoid infinite recursion
                    return create_github_issue(title, description, labels, False)
                else:
                    return {
                        'success': False,
                        'error': f"GitHub API rate limited. Please try again after {wait_time} seconds.",
                        'status': 'rate_limited',
                        'retry_after': wait_time
                    }
        
        # Check for specific error responses
        if response.status_code == 401:
            logger.error("GitHub API authentication failed - invalid token")
            return {
                'success': False, 
                'error': "GitHub authentication failed. Please check your token.",
                'status': 'auth_error'
            }
        elif response.status_code == 404:
            logger.error(f"GitHub repository not found: {repo}")
            return {
                'success': False, 
                'error': f"GitHub repository not found: {repo}. Please check the repository name.",
                'status': 'not_found'
            }
        
        # Raise exception for other HTTP errors
        response.raise_for_status()
        
        # Parse successful response
        issue_data = response.json()
        logger.info(f"GitHub issue created successfully: #{issue_data['number']}")
        
        return {
            'success': True,
            'issue_number': issue_data['number'],
            'url': issue_data['html_url'],
            'status': 'created'
        }
    except requests.exceptions.RequestException as e:
        error_msg = f"GitHub API error: {str(e)}"
        logger.error(error_msg)
        return {
            'success': False,
            'error': error_msg,
            'status': 'api_error'
        }
    except Exception as e:
        # Catch-all for any other unexpected errors
        error_msg = f"Unexpected error when creating GitHub issue: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return {
            'success': False,
            'error': error_msg,
            'status': 'unexpected_error'
        }
