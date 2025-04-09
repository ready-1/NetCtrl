#!/usr/bin/env python
"""
Setup script for NetCtrl development environment.

This script sets up the Python virtual environment and installs all required
dependencies for the NetCtrl application.
"""
import os
import sys
import subprocess
import platform
from pathlib import Path

def print_step(message):
    """Print a step with formatting."""
    print(f"\n=== {message} ===")

def print_error(message):
    """Print an error message with formatting."""
    print(f"ERROR: {message}")

def print_success(message):
    """Print a success message with formatting."""
    print(f"SUCCESS: {message}")

def check_python_version():
    """Check if the Python version is compatible."""
    print_step("Checking Python version")
    
    version_info = sys.version_info
    if version_info.major < 3 or (version_info.major == 3 and version_info.minor < 8):
        print_error("Python 3.8 or higher is required")
        print(f"Current Python version: {sys.version}")
        return False
    
    print_success(f"Python version {sys.version.split()[0]} is compatible")
    return True

def setup_virtualenv():
    """Set up or validate the virtual environment."""
    print_step("Setting up virtual environment")
    
    # Get project root directory
    project_root = Path(__file__).resolve().parent.parent
    venv_path = project_root / "python"
    
    # Check if virtual environment exists
    if not venv_path.exists():
        print("Creating virtual environment...")
        try:
            subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
            print_success("Virtual environment created successfully")
        except subprocess.CalledProcessError as e:
            print_error(f"Failed to create virtual environment: {e}")
            return False, None
    else:
        print("Virtual environment already exists")
    
    # Get paths for activation and pip
    if platform.system() == "Windows":
        activate_script = venv_path / "Scripts" / "activate"
        pip_path = venv_path / "Scripts" / "pip"
    else:  # Unix/Linux/Mac
        activate_script = venv_path / "bin" / "activate"
        pip_path = venv_path / "bin" / "pip"
    
    if not pip_path.exists():
        print_error(f"Pip not found at expected location: {pip_path}")
        return False, None
    
    print_success("Virtual environment is ready")
    return True, pip_path

def install_requirements(pip_path):
    """Install required packages using pip."""
    print_step("Installing required packages")
    
    project_root = Path(__file__).resolve().parent.parent
    requirements_file = project_root / "app" / "requirements.txt"
    
    if not requirements_file.exists():
        print_error(f"Requirements file not found: {requirements_file}")
        return False
    
    try:
        print(f"Installing packages from {requirements_file}...")
        subprocess.run([str(pip_path), "install", "-r", str(requirements_file)], check=True)
        print_success("All required packages installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to install required packages: {e}")
        return False

def run_verification():
    """Run the environment verification script."""
    print_step("Verifying environment setup")
    
    project_root = Path(__file__).resolve().parent.parent
    verify_script = project_root / "scripts" / "verify_env.py"
    venv_python = project_root / "python" / ("Scripts" if platform.system() == "Windows" else "bin") / "python"
    
    if not verify_script.exists():
        print_error(f"Verification script not found: {verify_script}")
        return False
    
    try:
        result = subprocess.run([str(venv_python), str(verify_script)], 
                              capture_output=True, text=True, check=False)
        
        # Print the output from the verification script
        print(result.stdout)
        
        if result.stderr:
            print("ERRORS:")
            print(result.stderr)
        
        if result.returncode != 0:
            print_error("Environment verification failed")
            return False
        
        print_success("Environment verification completed successfully")
        return True
    except Exception as e:
        print_error(f"Failed to run verification script: {e}")
        return False

def show_activation_instructions():
    """Show instructions for activating the virtual environment."""
    project_root = Path(__file__).resolve().parent.parent
    venv_path = project_root / "python"
    
    print_step("Next Steps")
    
    if platform.system() == "Windows":
        activate_cmd = f"{venv_path}\\Scripts\\activate"
        print(f"Activate the virtual environment with: {activate_cmd}")
    else:  # Unix/Linux/Mac
        activate_cmd = f"source {venv_path}/bin/activate"
        print(f"Activate the virtual environment with: {activate_cmd}")
    
    print("\nAfter activating, you can run the verification script again:")
    print("python scripts/verify_env.py")
    
    print("\nOr start the Django development server:")
    print("cd app && python manage.py runserver")

def main():
    """Main function to set up the environment."""
    print("NetCtrl Environment Setup Tool")
    print("==============================")
    
    if not check_python_version():
        return 1
    
    venv_ok, pip_path = setup_virtualenv()
    if not venv_ok:
        return 1
    
    if not install_requirements(pip_path):
        return 1
    
    verification_ok = run_verification()
    
    # Always show activation instructions, even if verification failed
    show_activation_instructions()
    
    return 0 if verification_ok else 1

if __name__ == "__main__":
    sys.exit(main())
