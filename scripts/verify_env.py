#!/usr/bin/env python
"""
Environment configuration verification tool for NetCtrl.

This script verifies that environment variables are loaded correctly
and validates the environment configuration.
"""
import os
import sys
import logging
import importlib.util
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("env-verify")

# Add the app directory to the Python path
script_dir = Path(__file__).resolve().parent
app_dir = script_dir.parent / 'app'
sys.path.insert(0, str(app_dir))

def check_virtualenv():
    """Verify the script is running in the correct virtual environment"""
    # Get project root directory
    project_root = Path(__file__).resolve().parent.parent
    venv_path = project_root / 'python'
    
    # Check if we're running in a virtual environment
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    expected_python = str(venv_path / 'bin' / 'python')
    current_python = sys.executable
    
    if not in_venv:
        logger.warning("Not running in any virtual environment")
        logger.info(f"Current Python: {current_python}")
        logger.info(f"Expected Python: {expected_python}")
        logger.info("\nTo activate the virtual environment, run:")
        logger.info(f"source {venv_path}/bin/activate")
        return False
    
    if expected_python not in current_python:
        logger.warning("Running in a different virtual environment than expected")
        logger.info(f"Current Python: {current_python}")
        logger.info(f"Expected Python: {expected_python}")
        return False
        
    logger.info("✓ Running in the correct virtual environment")
    return True

def check_prerequisites():
    """Check that all required packages are installed"""
    required_packages = {
        'dotenv': 'python-dotenv',
        'requests': 'requests',
        'markdown': 'markdown',
        'bleach': 'bleach'
    }
    missing_packages = []
    
    for module_name, package_name in required_packages.items():
        spec = importlib.util.find_spec(module_name)
        if spec is None:
            missing_packages.append(package_name)
    
    if missing_packages:
        logger.error(f"Missing required packages: {', '.join(missing_packages)}")
        logger.info("\nTo install required packages, run:")
        logger.info("pip install -r app/requirements.txt")
        return False
    
    logger.info("✓ All required packages are installed")
    return True

def test_env_loading():
    """Test environment variable loading mechanism"""
    logger.info("=== Testing Environment Loading ===")
    
    try:
        from netctrl.env_config import load_environment, get_env_var, is_placeholder
        logger.info("✓ Successfully imported environment config module")
    except ImportError as e:
        logger.error(f"✗ Failed to import environment config module: {e}")
        return False
    
    # Test loading environment variables
    load_result = load_environment()
    if load_result:
        logger.info("✓ Successfully loaded environment variables")
    else:
        logger.warning("! Environment variables may not be fully loaded")
    
    # Test placeholder detection
    placeholders = [
        "your-token-here",
        "replace-with-actual-key",
        "example-key",
        "<insert-key-here>",
        "CHANGEME",
        "your-actual-token-here"
    ]
    
    placeholder_failures = 0
    for p in placeholders:
        if not is_placeholder(p):
            logger.warning(f"! Placeholder detection may be incomplete: Failed to detect '{p}'")
            # Update the placeholder pattern in env_config.py to include more patterns
            placeholder_failures += 1
    
    if placeholder_failures == 0:
        logger.info("✓ Placeholder detection is working correctly")
    
    return True

def check_critical_variables():
    """Check that critical environment variables are properly configured"""
    logger.info("\n=== Checking Critical Variables ===")
    
    critical_vars = [
        ('DJANGO_SECRET_KEY', "Check that it's not the default insecure key"),
        ('DJANGO_DEBUG', "Should be 'True' for development"),
        ('GITHUB_TOKEN', "Should be set for GitHub integration (or explicitly absent)"),
        ('ENVIRONMENT', "Should be 'development', 'testing', or 'production'"),
    ]
    
    failures = 0
    for var_name, description in critical_vars:
        value = os.environ.get(var_name)
        if value:
            if var_name == 'DJANGO_SECRET_KEY' and 'django-insecure' in value:
                logger.warning(f"! {var_name}: Using default insecure key")
                failures += 1
            elif var_name == 'GITHUB_TOKEN' and 'your-' in value.lower():
                logger.warning(f"! {var_name}: Contains placeholder value")
                failures += 1
            else:
                logger.info(f"✓ {var_name}: Properly configured")
        else:
            if var_name == 'GITHUB_TOKEN':
                logger.info(f"✓ {var_name}: Not set (GitHub integration will be disabled)")
            else:
                logger.warning(f"! {var_name}: Not set - {description}")
                failures += 1
    
    return failures == 0

def test_settings_integration():
    """Verify Django settings properly use environment variables"""
    logger.info("\n=== Testing Django Settings Integration ===")
    
    try:
        # Import Django settings (this will load and process environment variables)
        from netctrl import settings
        logger.info("✓ Successfully imported Django settings")
        
        # Check key settings
        if getattr(settings, 'SECRET_KEY', '').startswith('django-insecure'):
            logger.warning("! Using insecure default SECRET_KEY")
        else:
            logger.info("✓ Using custom SECRET_KEY")
        
        # Check ALLOWED_HOSTS
        if isinstance(settings.ALLOWED_HOSTS, list) and len(settings.ALLOWED_HOSTS) > 0:
            logger.info(f"✓ ALLOWED_HOSTS configured: {settings.ALLOWED_HOSTS}")
        else:
            logger.warning("! ALLOWED_HOSTS not properly configured")
        
        # Check GitHub token
        if hasattr(settings, 'GITHUB_TOKEN') and settings.GITHUB_TOKEN:
            logger.info("✓ GitHub token is configured in settings")
        else:
            logger.info("! GitHub token not set - GitHub integration will be disabled")
        
        return True
    except Exception as e:
        logger.error(f"✗ Error importing or checking Django settings: {e}")
        return False

def test_github_api():
    """Test GitHub API integration"""
    logger.info("\n=== Testing GitHub API Integration ===")
    
    try:
        from netctrl.github_api import get_github_credentials
        
        token, repo, is_valid = get_github_credentials()
        
        if is_valid:
            logger.info(f"✓ GitHub credentials valid: repository {repo}")
        else:
            if token is None:
                logger.info("! GitHub token not configured - API integration will be disabled")
            else:
                logger.warning(f"! GitHub credentials invalid: token={bool(token)}, repo={repo}")
        
        return True
    except Exception as e:
        logger.error(f"✗ Error testing GitHub API: {e}")
        return False

def verify_bleach_config():
    """Verify Bleach CSS sanitizer configuration"""
    logger.info("\n=== Testing Bleach CSS Sanitizer ===")
    
    try:
        from cms.templatetags.markdown_filters import CSS_SANITIZER_AVAILABLE
        
        if CSS_SANITIZER_AVAILABLE:
            logger.info("✓ Bleach CSS sanitizer is available")
            # Try to create a sanitizer
            from bleach.css_sanitizer import CSSSanitizer
            sanitizer = CSSSanitizer(allowed_css_properties=['color', 'background-color'])
            logger.info("✓ Successfully created CSSSanitizer instance")
        else:
            logger.warning("! Bleach CSS sanitizer is not available - using fallback sanitization")
        
        return True
    except Exception as e:
        logger.error(f"✗ Error testing Bleach CSS sanitizer: {e}")
        return False

def main():
    """Main verification function"""
    logger.info("NetCtrl Environment Verification Tool")
    logger.info("====================================")
    
    # First check virtual environment and prerequisites
    logger.info("=== Checking Environment Prerequisites ===")
    venv_ok = check_virtualenv()
    prereq_ok = check_prerequisites()
    
    if not (venv_ok and prereq_ok):
        logger.error("\n❌ Environment prerequisites check failed")
        logger.warning("\nPlease resolve environment issues before continuing")
        logger.info("See instructions above for activating the virtual environment and installing packages")
        return 1
    
    # Run all verification checks
    env_loading_ok = test_env_loading()
    vars_ok = check_critical_variables()
    settings_ok = test_settings_integration()
    github_ok = test_github_api()
    bleach_ok = verify_bleach_config()
    
    # Final summary
    logger.info("\n=== Verification Summary ===")
    for test, result in [
        ("Virtual Environment", venv_ok),
        ("Required Packages", prereq_ok),
        ("Environment Loading", env_loading_ok),
        ("Critical Variables", vars_ok),
        ("Django Settings", settings_ok),
        ("GitHub API", github_ok),
        ("Bleach CSS Sanitizer", bleach_ok)
    ]:
        status = "✓ PASS" if result else "✗ FAIL"
        logger.info(f"{status}: {test}")
    
    all_ok = venv_ok and prereq_ok and env_loading_ok and vars_ok and settings_ok and github_ok and bleach_ok
    
    logger.info("\n" + ("=" * 50))
    if all_ok:
        logger.info("✅ All verification checks passed!")
    else:
        logger.warning("⚠️ Some verification checks failed. Review output for details.")
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
