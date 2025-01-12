#!/usr/bin/env python3
"""
Script to download and set up local static assets (Bootstrap and HTMX).
"""
import os
import shutil
import urllib.request
from pathlib import Path

# Define versions and URLs
BOOTSTRAP_VERSION = "5.3.2"
HTMX_VERSION = "1.9.10"
BOOTSTRAP_ICONS_VERSION = "1.11.3"
ACE_VERSION = "1.32.6"

ASSETS = {
    # Bootstrap
    "bootstrap.min.css": f"https://cdn.jsdelivr.net/npm/bootstrap@{BOOTSTRAP_VERSION}/dist/css/bootstrap.min.css",
    "bootstrap.bundle.min.js": f"https://cdn.jsdelivr.net/npm/bootstrap@{BOOTSTRAP_VERSION}/dist/js/bootstrap.bundle.min.js",
    
    # HTMX
    "htmx.min.js": f"https://unpkg.com/htmx.org@{HTMX_VERSION}/dist/htmx.min.js",
    
    # Bootstrap Icons
    "bootstrap-icons.css": f"https://cdn.jsdelivr.net/npm/bootstrap-icons@{BOOTSTRAP_ICONS_VERSION}/font/bootstrap-icons.css",
    
    # Ace Editor
    "ace.min.js": f"https://cdnjs.cloudflare.com/ajax/libs/ace/{ACE_VERSION}/ace.min.js",
    "theme-monokai.min.js": f"https://cdnjs.cloudflare.com/ajax/libs/ace/{ACE_VERSION}/theme-monokai.min.js",
    "mode-text.min.js": f"https://cdnjs.cloudflare.com/ajax/libs/ace/{ACE_VERSION}/mode-text.min.js",
}

# Bootstrap Icons font files
ICON_FONTS = {
    "fonts/bootstrap-icons.woff": f"https://cdn.jsdelivr.net/npm/bootstrap-icons@{BOOTSTRAP_ICONS_VERSION}/font/fonts/bootstrap-icons.woff",
    "fonts/bootstrap-icons.woff2": f"https://cdn.jsdelivr.net/npm/bootstrap-icons@{BOOTSTRAP_ICONS_VERSION}/font/fonts/bootstrap-icons.woff2",
}

def ensure_dirs():
    """Ensure vendor directories exist."""
    base_dir = Path(__file__).resolve().parent.parent
    vendor_css = base_dir / 'static' / 'vendor' / 'css'
    vendor_js = base_dir / 'static' / 'vendor' / 'js'
    vendor_fonts = base_dir / 'static' / 'vendor' / 'css' / 'fonts'
    
    vendor_css.mkdir(parents=True, exist_ok=True)
    vendor_js.mkdir(parents=True, exist_ok=True)
    vendor_fonts.mkdir(parents=True, exist_ok=True)
    
    return base_dir

def download_file(url, dest_path):
    """Download a file from URL to destination path."""
    print(f"Downloading {url} to {dest_path}")
    try:
        with urllib.request.urlopen(url) as response, open(dest_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print(f"Successfully downloaded {dest_path.name}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        raise

def main():
    """Main function to download all assets."""
    base_dir = ensure_dirs()
    
    # Download main assets
    for filename, url in ASSETS.items():
        if filename.endswith('.css'):
            dest_path = base_dir / 'static' / 'vendor' / 'css' / filename
        else:
            dest_path = base_dir / 'static' / 'vendor' / 'js' / filename
        download_file(url, dest_path)
    
    # Download icon fonts
    for filename, url in ICON_FONTS.items():
        dest_path = base_dir / 'static' / 'vendor' / 'css' / filename
        download_file(url, dest_path)

if __name__ == '__main__':
    main()
