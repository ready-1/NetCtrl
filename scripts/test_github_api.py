#!/usr/bin/env python
"""
GitHub API integration test script.

This script demonstrates the GitHub API integration by retrieving repository information
and testing issue creation capabilities.
"""
import os
import sys
import argparse
from pathlib import Path

# Add application path to Python path
script_dir = Path(__file__).resolve().parent
app_dir = script_dir.parent / 'app'
sys.path.insert(0, str(app_dir))

def get_repo_info():
    """Get basic information about the configured GitHub repository"""
    from netctrl.github_api import get_github_credentials
    import requests
    
    token, repo, is_valid = get_github_credentials()
    
    if not is_valid:
        print("ERROR: GitHub credentials are invalid or missing.")
        return None
    
    print(f"✓ GitHub credentials valid for repository: {repo}")
    
    # Make API request to get repository information
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    try:
        response = requests.get(
            f"https://api.github.com/repos/{repo}", 
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            repo_data = response.json()
            return {
                "name": repo_data.get("name"),
                "full_name": repo_data.get("full_name"),
                "description": repo_data.get("description"),
                "url": repo_data.get("html_url"),
                "stars": repo_data.get("stargazers_count"),
                "forks": repo_data.get("forks_count"),
                "open_issues": repo_data.get("open_issues_count"),
                "owner": repo_data.get("owner", {}).get("login"),
                "private": repo_data.get("private")
            }
        else:
            print(f"ERROR: API request failed with status code {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"ERROR: Failed to fetch repository information: {e}")
        return None

def test_create_issue(title, description=None, labels=None):
    """
    Test creating a GitHub issue using the application's API.
    
    This demonstrates the GitHub API integration for issue creation.
    
    Args:
        title: Issue title
        description: Issue description (optional)
        labels: Comma-separated list of labels (optional)
    """
    from netctrl.github_api import create_github_issue
    
    print(f"Creating test issue: '{title}'")
    if labels:
        labels = [label.strip() for label in labels.split(",") if label.strip()]
        print(f"Labels: {', '.join(labels)}")
    
    # Create the issue
    result = create_github_issue(title, description, labels)
    
    if result['success']:
        print(f"✓ Issue created successfully!")
        print(f"Issue number: #{result['issue_number']}")
        print(f"URL: {result['url']}")
    else:
        print(f"✗ Failed to create issue: {result['error']}")
        print(f"Status: {result['status']}")

def main():
    """Run GitHub API tests"""
    parser = argparse.ArgumentParser(description='Test GitHub API integration')
    parser.add_argument('--info', action='store_true', help='Get repository information')
    parser.add_argument('--create-issue', action='store_true', help='Create a test issue')
    parser.add_argument('--title', default='Test Issue from API Script', help='Issue title')
    parser.add_argument('--description', help='Issue description')
    parser.add_argument('--labels', help='Comma-separated list of labels')
    
    args = parser.parse_args()
    
    # Default to showing repo info if no specific action is requested
    if not (args.info or args.create_issue):
        args.info = True
    
    print("GitHub API Test")
    print("==============")
    
    if args.info:
        print("\n=== Repository Information ===")
        repo_info = get_repo_info()
        
        if repo_info:
            for key, value in repo_info.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
    
    if args.create_issue:
        print("\n=== Issue Creation Test ===")
        test_create_issue(args.title, args.description, args.labels)

if __name__ == "__main__":
    main()
