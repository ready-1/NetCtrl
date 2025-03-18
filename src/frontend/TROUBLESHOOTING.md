# Troubleshooting the NetCtrl CMS Frontend

This guide provides solutions for common issues you might encounter when setting up and running the frontend application.

## Dependency Installation Issues

### General Dependency Conflicts

If you encounter dependency conflicts during installation, try one of these approaches:

1. **Use the `--force` flag (Recommended):**
   ```bash
   npm install --force
   ```
   This forces npm to resolve conflicts and can bypass compatibility warnings.

2. **Use the `--legacy-peer-deps` flag:**
   ```bash
   npm install --legacy-peer-deps
   ```
   This ignores peer dependency conflicts but may not resolve deeper package issues.

3. **Clear npm cache and retry:**
   ```bash
   npm cache clean --force
   npm install --force
   ```

### Missing Module Errors

If you encounter errors like `Cannot find module 'ajv/dist/compile/codegen'` or similar, try these solutions:

1. **Reinstall with a clean node_modules:**
   ```bash
   rm -rf node_modules
   rm package-lock.json
   npm install --force
   ```

2. **Install specific versions of problematic packages:**
   ```bash
   npm install ajv@latest --force
   npm install ajv-keywords@latest --force
   ```

3. **Try using another package manager:**
   ```bash
   # Using yarn
   rm -rf node_modules
   rm package-lock.json
   yarn install
   
   # Using pnpm
   rm -rf node_modules
   rm package-lock.json
   pnpm install
   ```

## TypeScript Errors

### TypeScript Version Compatibility

React Scripts may have compatibility issues with newer TypeScript versions. If you encounter TypeScript-related errors:

1. **Downgrade TypeScript:**
   ```bash
   npm install typescript@4.9.5 --force
   ```

2. **Override TypeScript settings:**
   Create a `.npmrc` file in the project root with:
   ```
   legacy-peer-deps=true
   ```

### Type Errors in the Editor

If you see TypeScript errors in your editor but the application builds and runs:

1. **Restart the TypeScript server in VS Code:**
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
   - Type "TypeScript: Restart TS Server" and select it

2. **Update type definitions:**
   ```bash
   npm install @types/react @types/react-dom --force
   ```

## Running the Application

### Development Server Issues

If the development server fails to start:

1. **Try a different port:**
   ```bash
   PORT=3001 npm start
   ```

2. **Check for processes using port 3000:**
   ```bash
   # On macOS/Linux:
   lsof -i :3000
   
   # On Windows:
   netstat -ano | findstr :3000
   ```

### Build Issues

If you encounter problems when building for production:

1. **Skip TypeScript type checking during build:**
   ```bash
   TSC_COMPILE_ON_ERROR=true npm run build
   ```

2. **Clear build cache:**
   ```bash
   rm -rf build
   npm run build -- --no-cache
   ```

## Docker-Specific Issues

If running via Docker:

1. **Rebuild the container:**
   ```bash
   docker compose build --no-cache frontend
   ```

2. **Ensure node_modules isn't mounted:**
   Check that your volume mounts in `docker-compose.yml` don't include node_modules.

## Still Having Issues?

If you're still experiencing problems:

1. Check the exact versions of your dependencies in `package.json`
2. Review the application logs for specific error messages
3. Consider contributing to this troubleshooting guide with your solutions
