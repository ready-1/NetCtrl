#!/bin/bash
# Script to remove TinyMCE files and directories from the NetCtrl CMS project
# This is part of the migration from TinyMCE to Markdown/plaintext only

# Set the project root
PROJECT_ROOT="$(dirname "$0")/.."
cd "$PROJECT_ROOT" || { echo "Failed to change to project root"; exit 1; }

echo "Removing TinyMCE files from the project..."

# Remove TinyMCE JavaScript files
echo "Removing TinyMCE JavaScript files..."
rm -f app/static/js/tinymce-core.js
rm -f app/static/js/tinymce-init.js
rm -f app/static/js/tinymce-direct.js
rm -f app/static/js/tinymce-config.js
rm -f app/static/js/tinymce-manager.js
rm -f app/static/cms/js/editor-switcher.js

# Remove TinyMCE vendor directory if it exists
if [ -d "app/static/vendor/tinymce" ]; then
    echo "Removing TinyMCE vendor directory..."
    rm -rf app/static/vendor/tinymce
fi

# Create a placeholder in case scripts need to reference these files
echo "Creating placeholders for removed files..."
mkdir -p app/static/vendor/tinymce_removed
touch app/static/vendor/tinymce_removed/README.md
echo "# TinyMCE Removed" > app/static/vendor/tinymce_removed/README.md
echo "This directory exists as a placeholder. TinyMCE has been removed from the project." >> app/static/vendor/tinymce_removed/README.md
echo "The CMS now uses Markdown and plaintext formats only." >> app/static/vendor/tinymce_removed/README.md

echo "TinyMCE removal complete."
