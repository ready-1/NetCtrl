import * as chokidar from "chokidar";
import fs from "fs/promises";
import path from "path";
import crypto from "crypto";
import { FileEntry } from "./types.js";
import { ContextDB } from "./db.js";
import mime from "mime-types";

export class FileWatcher {
  private watcher!: chokidar.FSWatcher;
  private db: ContextDB;
  private root: string;

  constructor(projectRoot: string, db: ContextDB) {
    this.db = db;
    this.root = path.resolve(projectRoot);
  }

  async start(): Promise<void> {
    // Clear database
    await this.db.updateProjectStructure({
      rootPath: this.root,
      poetryConfig: {
        dependencies: {},
        devDependencies: {}
      },
      files: []
    });

    // Debug: Check if test.yaml exists
    try {
      const testYamlPath = path.join(this.root, 'test.yaml');
      await fs.access(testYamlPath);
      console.error(`[FileWatcher] test.yaml exists at ${testYamlPath}`);
      const content = await fs.readFile(testYamlPath, 'utf8');
      console.error('[FileWatcher] test.yaml content:', content);
    } catch (error) {
      console.error('[FileWatcher] Error accessing test.yaml:', error);
    }

    // Watch files
    const patterns = [
      'test.yaml',
      'netctrl/**/*.{py,yaml,yml}',
      'tests/**/*.py',
      'docs/**/*.{pdf,md}'
    ];

    console.error('[FileWatcher] Starting watch with patterns:', patterns);
    console.error('[FileWatcher] Root directory:', this.root);

    this.watcher = chokidar.watch(patterns, {
      cwd: this.root,
      persistent: true,
      ignoreInitial: false,
      ignored: ['**/node_modules/**', '**/__pycache__/**', '**/.*'],
      awaitWriteFinish: {
        stabilityThreshold: 1000,
        pollInterval: 100
      }
    });

    // Handle events
    this.watcher
      .on('add', async filepath => {
        console.error(`[FileWatcher] File added: ${filepath}`);
        try {
          await this.handleFile(filepath);
        } catch (error) {
          console.error(`[FileWatcher] Error handling added file ${filepath}:`, error);
        }
      })
      .on('change', async filepath => {
        console.error(`[FileWatcher] File changed: ${filepath}`);
        try {
          await this.handleFile(filepath);
        } catch (error) {
          console.error(`[FileWatcher] Error handling changed file ${filepath}:`, error);
        }
      })
      .on('unlink', filepath => console.error(`[FileWatcher] File removed: ${filepath}`))
      .on('error', error => console.error(`[FileWatcher] Error:`, error));

    // Wait for initial scan
    await new Promise<void>(resolve => {
      this.watcher.on('ready', () => {
        // Debug: List all watched files
        const watched = this.watcher.getWatched();
        console.error('[FileWatcher] Watched files:', JSON.stringify(watched, null, 2));
        
        // Log completion
        console.error('[FileWatcher] Initial scan complete');
        resolve();
      });
    });

    // Verify database state
    const files = await this.db.getAllFiles();
    console.error(`[FileWatcher] Files in database after scan: ${files.length}`);
    for (const file of files) {
      console.error(`[FileWatcher] - ${file.path} (${file.fileType})`);
    }
  }

  private async handleFile(filepath: string): Promise<void> {
    try {
      const absPath = path.join(this.root, filepath);
      console.error(`[FileWatcher] Processing: ${filepath}`);

      // Basic validation
      if (!await this.isValidFile(filepath)) {
        console.error(`[FileWatcher] File validation failed: ${filepath}`);
        return;
      }

      console.error(`[FileWatcher] File validation passed: ${filepath}`);

      // Get basic file info
      const stats = await fs.stat(absPath);
      const mimeType = mime.lookup(filepath) || 'application/octet-stream';
      const isText = mimeType.startsWith('text/') || 
                    mimeType === 'application/json' ||
                    mimeType === 'application/javascript';

      // Read file content
      const content = await fs.readFile(absPath);
      const hash = crypto.createHash('sha256').update(content).digest('hex');

      // Create entry based on file type and size
      const entry: FileEntry = {
        path: filepath,
        content: isText ? content.toString('utf8') : content.toString('base64'),
        contentType: isText ? 'text' : 'text',
        metadata: {
          size: stats.size,
          mimeType,
          encoding: isText ? 'utf8' : 'base64'
        },
        hash,
        lastModified: stats.mtimeMs,
        fileType: this.getFileType(filepath)
      };

      // For large files, store in chunks
      if (stats.size > 1024 * 1024) { // 1MB
        entry.contentType = 'chunked';
        entry.content = null;
        
        // Split into 1MB chunks
        const chunkSize = 1024 * 1024;
        const chunks: Buffer[] = [];
        let position = 0;
        
        while (position < content.length) {
          chunks.push(content.slice(position, position + chunkSize));
          position += chunkSize;
        }
        
        await this.db.storeFileChunks(hash, chunks, chunks.length);
      }

      // Update database
      await this.db.updateFile(entry);
      console.error(`[FileWatcher] Added to database: ${filepath}`);

    } catch (error) {
      console.error(`[FileWatcher] Error processing ${filepath}:`, error);
    }
  }

  private async isValidFile(filepath: string): Promise<boolean> {
    const ext = path.extname(filepath).toLowerCase();
    const basename = path.basename(filepath);

    // Allow specific files
    if (basename === 'test.yaml') {
      return true;
    }

    // Check extensions
    const allowedExts = ['.py', '.yaml', '.yml', '.pdf', '.md'];
    if (!allowedExts.includes(ext)) {
      return false;
    }

    // Check directories
    const dir = path.dirname(filepath);
    const allowedDirs = ['netctrl', 'tests', 'docs', '.'];
    return allowedDirs.includes(dir.split('/')[0]);
  }

  private getFileType(filepath: string): FileEntry['fileType'] {
    const ext = path.extname(filepath).toLowerCase();
    switch (ext) {
      case '.py': return 'python';
      case '.yaml':
      case '.yml': return 'yaml';
      case '.pdf': return 'pdf';
      default: return 'other';
    }
  }

  async rescanFiles(): Promise<void> {
    // Close existing watcher
    this.watcher.close();
    
    // Start fresh
    await this.start();
  }

  close(): void {
    this.watcher.close();
  }
}
