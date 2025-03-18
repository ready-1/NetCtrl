# NetCtrl CMS Frontend

This is the frontend for the NetCtrl Content Management System (CMS). It's built with React, Material UI, and TypeScript.

## Running the Frontend

There are multiple ways to run the frontend application:

### Local Development

1. **Using the convenience script (Recommended)**:
   ```bash
   cd src/frontend
   ./start-dev.sh
   ```
   This script handles dependency installation and starts the development server automatically.

2. **Manual installation**:
   ```bash
   cd src/frontend
   npm install --force
   npm start
   ```
   
   > **Note:** The `--force` flag is required to resolve dependency conflicts in the project. This is necessary because of compatibility issues between certain packages.

3. The application will be available at [http://localhost:3000](http://localhost:3000)

### Using Docker

The project includes Docker configuration for running the entire application stack:

1. Make sure Docker is installed and running on your system

2. From the project root, run:
   ```bash
   docker compose up frontend
   ```

3. Access the application at the URL configured in your Docker setup (typically [http://localhost:3000](http://localhost:3000))

### Building for Production

1. Create a production build:
   ```bash
   cd src/frontend
   npm run build
   ```

2. The build output will be in the `build` directory, which you can serve using any static file server

## Features

- **Authentication**: Login, registration, and role-based access control
- **Content Management**: Create, edit, and manage content with versioning
- **File Management**: Upload, download, and manage files with metadata
- **Responsive Design**: Mobile-first approach that works on all device sizes
- **Dark Mode**: Toggle between light and dark themes
- **Role-Based UI**: Interface adapts based on user permissions

## Architecture

The frontend follows a structured architecture:

- **Components**: Organized using atomic design principles
- **Context**: Global state management for auth and theme
- **Services**: API communication and business logic
- **Pages**: Full page components combining smaller components
- **Routing**: Centralized route definitions with proper guards
- **Types**: Complete TypeScript definitions for type safety

## Development Workflow

- **Development**: `npm start`
- **Testing**: `npm test`
- **Building**: `npm run build`
- **Type Checking**: TypeScript is configured to check types on save

## Project Structure

```
src/
├── assets/                  # Static assets
├── components/              # Reusable UI components
│   ├── auth/                # Authentication components
│   ├── content/             # Content management components
│   ├── file/                # File management components
│   ├── layout/              # Layout components
│   ├── common/              # Shared components
│   └── ui/                  # Atomic design components
├── config/                  # Configuration
├── context/                 # Context providers
├── hooks/                   # Custom hooks
├── pages/                   # Page components
├── services/                # API services
├── types/                   # TypeScript types
├── utils/                   # Utility functions
├── App.tsx                  # Main App component
└── index.tsx                # Entry point
