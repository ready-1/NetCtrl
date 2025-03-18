#!/bin/bash
# Script to set up and run the NetCtrl CMS frontend in development mode

# Exit on error
set -e

echo "📦 Installing dependencies..."
# Use legacy-peer-deps to handle TypeScript version compatibility with react-scripts
npm install --legacy-peer-deps

echo "🚀 Starting development server..."
npm start

# The server will continue running until manually stopped
# Access the app at http://localhost:3000
