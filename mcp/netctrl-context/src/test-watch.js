const chokidar = require('chokidar');
const path = require('path');
const fs = require('fs');

// Get project root
const root = process.cwd();
console.log('Starting test watcher');
console.log('Root directory:', root);

// Check test.yaml directly
const testYamlPath = path.join(root, 'test.yaml');
console.log('\nChecking test.yaml:');
if (fs.existsSync(testYamlPath)) {
    console.log('- test.yaml exists');
    console.log('- Content:', fs.readFileSync(testYamlPath, 'utf8'));
} else {
    console.log('- test.yaml not found');
}

// List root directory
console.log('\nRoot directory contents:');
fs.readdirSync(root).forEach(file => {
    console.log(`- ${file}`);
});

// List docs directory
const docsPath = path.join(root, 'docs');
if (fs.existsSync(docsPath)) {
    console.log('\nDocs directory contents:');
    fs.readdirSync(docsPath, { recursive: true }).forEach(file => {
        console.log(`- ${file}`);
    });
}

console.log('\nStarting file watcher...');

// Create watcher
const watcher = chokidar.watch([
  'test.yaml',
  'netctrl/**/*.{py,yaml,yml}',
  'tests/**/*.py',
  'docs/**/*.{pdf,md}'
], {
  cwd: root,
  persistent: true,
  ignoreInitial: false,
  ignored: ['**/node_modules/**', '**/__pycache__/**', '**/.*']
});

// Log everything
watcher
  .on('add', path => console.log(`File added: ${path}`))
  .on('change', path => console.log(`File changed: ${path}`))
  .on('unlink', path => console.log(`File removed: ${path}`))
  .on('error', error => console.log(`Error: ${error}`))
  .on('ready', () => {
    console.log('\nInitial scan complete');
    const watched = watcher.getWatched();
    console.log('Watched paths:', JSON.stringify(watched, null, 2));
    
    // Keep process running
    console.log('\nWatching for changes... (Ctrl+C to exit)');
  });
