#!/bin/bash

# Output file
OUTPUT_FILE="grok.txt"

# Clear the output file first
echo "# NetCtrl CMS Project Code - Begin" > "$OUTPUT_FILE"

# Generate and add project tree structure
echo "" >> "$OUTPUT_FILE"
echo "# Project Tree Structure" >> "$OUTPUT_FILE"
echo '```' >> "$OUTPUT_FILE"
echo "/Users/bob/dev/NetCtrl" >> "$OUTPUT_FILE"

# Find main project directories excluding cache and unwanted files
find src -type d | grep -v "__pycache__" | grep -v "node_modules" | grep -v "\.git" | grep -v "\.pytest_cache" | head -n 20 | sort | sed 's/^/├── /' >> "$OUTPUT_FILE"

# Add key top-level directories
echo "├── ..." >> "$OUTPUT_FILE"
echo "├── cline_docs" >> "$OUTPUT_FILE"
echo "├── docs" >> "$OUTPUT_FILE"
echo "├── strategy_tasks" >> "$OUTPUT_FILE"
echo "└── docker-compose.yml" >> "$OUTPUT_FILE"

echo '```' >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Add project description
echo "# Project Overview" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "NetCtrl CMS is a Content Management System with Role-Based Access Control (RBAC) built using:" >> "$OUTPUT_FILE"
echo "- Backend: FastAPI with SQLAlchemy ORM and PostgreSQL" >> "$OUTPUT_FILE"
echo "- Frontend: React with TypeScript and Material UI" >> "$OUTPUT_FILE"
echo "- Infrastructure: Docker, NGINX, and PostgreSQL" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "Key components:" >> "$OUTPUT_FILE"
echo "1. User authentication and authorization with RBAC" >> "$OUTPUT_FILE"
echo "2. Content management with CRUD operations" >> "$OUTPUT_FILE"
echo "3. File management capabilities" >> "$OUTPUT_FILE"
echo "4. API-first design with comprehensive OpenAPI documentation" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Function to add a file to the output
add_file() {
  local filepath="$1"
  
  # Skip if file doesn't exist
  if [ ! -f "$filepath" ]; then
    echo "Warning: File $filepath does not exist, skipping" >&2
    return
  fi
  
  # Add file header
  echo "" >> "$OUTPUT_FILE"
  echo "Begin /Users/bob/dev/NetCtrl/$filepath" >> "$OUTPUT_FILE"
  echo "" >> "$OUTPUT_FILE"
  
  # Add file contents
  cat "$filepath" >> "$OUTPUT_FILE"
  
  # Add file footer
  echo "" >> "$OUTPUT_FILE"
  echo "End /Users/bob/dev/NetCtrl/$filepath" >> "$OUTPUT_FILE"
  echo "" >> "$OUTPUT_FILE"
}

# Add backend files
add_file "src/backend/app/main.py"
add_file "src/backend/scripts/start.sh"
add_file "src/backend/start.sh"
add_file "src/backend/alembic.ini"
add_file "src/backend/app/core/config.py"
add_file "src/backend/alembic/versions/content_management_tables.py"
add_file "src/backend/DATABASE_TROUBLESHOOTING.md"

# Add frontend files
add_file "src/frontend/package.json"
add_file "src/frontend/Dockerfile"
add_file "src/frontend/src/components/ui/molecules/RichTextEditor.tsx"
add_file "src/frontend/src/types/content.ts"
add_file "src/frontend/src/services/api/contentService.ts"
add_file "src/frontend/src/components/content/ContentList.tsx"
add_file "src/frontend/src/components/content/ContentForm.tsx"
add_file "src/frontend/src/components/content/ContentDetail.tsx"
add_file "src/frontend/src/pages/content/ContentListPage.tsx"
add_file "src/frontend/src/hooks/useDocumentTitle.ts"
add_file "src/frontend/src/hooks/useContentQuery.ts"
add_file "src/frontend/src/pages/content/ContentDetailPage.tsx"
add_file "src/frontend/src/pages/content/ContentEditPage.tsx"
add_file "src/frontend/src/index.tsx"
add_file "src/frontend/src/components/layout/AppShell.tsx"
add_file "src/frontend/src/pages/NotFoundPage.tsx"
add_file "src/frontend/src/pages/auth/LoginPage.tsx"
add_file "src/frontend/src/pages/auth/RegisterPage.tsx"
add_file "src/frontend/src/types/user.ts"
add_file "src/frontend/src/pages/user/ProfilePage.tsx"
add_file "src/frontend/src/services/api/apiClient.ts"
add_file "src/frontend/src/pages/WelcomePage.tsx"
add_file "src/frontend/src/App.tsx"
add_file "src/frontend/src/config/routes.ts"
add_file "src/frontend/public/health"

# Add nginx files
add_file "src/nginx/conf/default.conf"
add_file "src/nginx/entrypoint.sh"
add_file "src/nginx/templates/default.template"
add_file "src/nginx/minimal-nginx.conf"

# Add cline_docs
add_file "cline_docs/changelog.md"
add_file "cline_docs/activeContext.md"
add_file ".clinerules"

echo "# NetCtrl CMS Project Code - End" >> "$OUTPUT_FILE"
echo "Files collected in $OUTPUT_FILE"
