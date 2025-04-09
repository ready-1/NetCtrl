# GitHub Integration Guide

This document provides information about the GitHub API integration in NetCtrl and explains best practices for configuration and troubleshooting.

## Configuration

The GitHub integration requires a Personal Access Token (PAT) with appropriate permissions to interact with repositories. The integration is configured through environment variables in the `.env` file.

### Required Environment Variables

```
# GitHub token for API access
GITHUB_TOKEN=your_github_token_here

# Target repository in format owner/repo
GITHUB_REPOSITORY=owner/repo-name
```

### GitHub Token Types

GitHub supports two types of personal access tokens:

1. **Fine-grained tokens** - Start with `github_pat_`
2. **Classic tokens** - Start with `ghp_`

Both token types are supported by the NetCtrl application.

## Token Security

GitHub tokens are sensitive credentials that should be protected:

- Never commit tokens to version control
- Use environment variables to store tokens
- Limit token permissions to only what's needed
- Periodically rotate tokens

## Features

The GitHub integration provides the following features:

- Repository information retrieval
- Issue creation and tracking
- Error handling for API rate limits and authentication failures
- Graceful degradation when GitHub integration is disabled

## Testing the Integration

The repository includes a test script for verifying GitHub integration:

```bash
# Test repository access
python scripts/test_github_api.py --info

# Create a test issue
python scripts/test_github_api.py --create-issue --title "Test Issue" --description "Testing the GitHub API integration" --labels "test,documentation"
```

## Troubleshooting

### Token Not Recognized

If your GitHub token is not being recognized, check:

1. The token is correctly set in the `.env` file (not commented out)
2. The token format is valid (starts with `github_pat_` or `ghp_`)
3. The token has not expired

### Environment Variables Not Loaded

The NetCtrl application has special handling for environment variables:

- Variables are loaded from the `.env` file using python-dotenv
- Variables are validated to detect and filter out placeholder values
- GitHub tokens are specifically whitelisted to prevent false positives

### API Rate Limits

GitHub API has rate limits that may affect integration:

- Unauthenticated requests: 60 per hour
- Authenticated requests: 5,000 per hour

The application includes automatic handling for rate limits, with exponential backoff and retry logic.

## Implementation Details

The GitHub integration is implemented in `app/netctrl/github_api.py` with these key components:

- `get_github_credentials()` - Retrieves and validates GitHub credentials
- `create_github_issue()` - Creates issues with comprehensive error handling

The integration uses environment variable handling from `app/netctrl/env_config.py` which includes:

- `is_placeholder()` - Detects placeholder values while whitelisting legitimate tokens
- `load_environment()` - Loads and validates environment variables

## Recent Enhancements

Recent improvements to GitHub token handling:

- Added whitelisting for GitHub token formats to prevent false positives in placeholder detection
- Enhanced error handling with more specific error codes and messages
- Added comprehensive testing tools for GitHub API integration
- Improved documentation for token management best practices
