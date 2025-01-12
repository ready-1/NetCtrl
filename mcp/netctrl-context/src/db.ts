import Database from "better-sqlite3";
import { FileEntry, CommandEntry, ProjectStructure } from "./types.js";
import path from "path";
import fs from "fs/promises";
import { mkdir, readdir, unlink } from "fs/promises";
import { createReadStream } from "fs";
import crypto from "crypto";

export class ContextDB {
  private db!: Database.Database;
  private readonly backupDir: string;

  private initialized: boolean = false;
  private dbPath: string;
  private mpcDir: string;

  constructor(projectRoot: string) {
    // Resolve absolute paths
    const absRoot = path.resolve(projectRoot);
    this.mpcDir = path.join(absRoot, ".mcp");
    this.backupDir = path.join(this.mpcDir, "backups");
    this.dbPath = path.join(this.mpcDir, "context.db");

    console.error("[ContextDB] Database paths:");
    console.error(`[ContextDB] Project root: ${absRoot}`);
    console.error(`[ContextDB] MPC dir: ${this.mpcDir}`);
    console.error(`[ContextDB] Database: ${this.dbPath}`);
    console.error(`[ContextDB] Backups: ${this.backupDir}`);
  }

  async initialize(): Promise<void> {
    if (this.initialized) {
      return;
    }

    try {
      // Create directories
      await mkdir(this.mpcDir, { recursive: true });
      await mkdir(path.join(this.mpcDir, "logs"), { recursive: true });
      await mkdir(this.backupDir, { recursive: true });

      // Initialize database
      this.db = new Database(this.dbPath);
      await this.initializeDB();
      this.setupBackups();

      this.initialized = true;
      console.error("[ContextDB] Initialization complete");
    } catch (error) {
      console.error("[ContextDB] Initialization failed:", error);
      throw error;
    }
  }

  private async ensureInitialized(): Promise<void> {
    if (!this.initialized) {
      throw new Error("ContextDB not initialized. Call initialize() first.");
    }
  }

  private async initializeDB(): Promise<void> {
    console.error("[ContextDB] Initializing database");
    
    // Check if tables exist
    const tables = this.db.prepare(`
      SELECT name FROM sqlite_master 
      WHERE type='table' AND name IN ('files', 'file_chunks', 'commands', 'project_structure')
    `).all() as { name: string }[];
    
    const existingTables = new Set(tables.map(t => t.name));
    console.error("[ContextDB] Existing tables:", Array.from(existingTables));

    if (!existingTables.has('files') || !existingTables.has('file_chunks')) {
      console.error("[ContextDB] Creating file tables");
      this.db.exec(`
        DROP TABLE IF EXISTS files;
        DROP TABLE IF EXISTS file_chunks;
        
        CREATE TABLE files (
        path TEXT PRIMARY KEY,
        content BLOB,
        contentType TEXT,
        metadata TEXT,
        hash TEXT,
        lastModified INTEGER,
        fileType TEXT
      );

        CREATE TABLE file_chunks (
        fileHash TEXT,
        chunkIndex INTEGER,
        totalChunks INTEGER,
        data BLOB,
        PRIMARY KEY (fileHash, chunkIndex)
      );

      `);
    }

    if (!existingTables.has('commands')) {
      console.error("[ContextDB] Creating commands table");
      this.db.exec(`
        CREATE TABLE commands (
        hash TEXT PRIMARY KEY,
        command TEXT,
        output TEXT,
        timestamp INTEGER
      );

      `);
    }

    if (!existingTables.has('project_structure')) {
      console.error("[ContextDB] Creating project_structure table");
      this.db.exec(`
        CREATE TABLE project_structure (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        rootPath TEXT,
        poetryConfig TEXT
      );
      `);
    }
  }

  private async cleanupOldBackups(): Promise<void> {
    try {
      const files = await readdir(this.backupDir);
      const oldFiles = files.sort().slice(0, -7);
      for (const file of oldFiles) {
        await unlink(path.join(this.backupDir, file));
      }
    } catch (error) {
      console.error("[ContextDB] Error cleaning up old backups:", error);
    }
  }

  private async createBackup(): Promise<void> {
    try {
      const timestamp = new Date().toISOString().split("T")[0];
      const backupPath = path.join(this.backupDir, `context_${timestamp}.db`);
      await this.db.backup(backupPath);
      await this.cleanupOldBackups();
    } catch (error) {
      console.error("[ContextDB] Error creating backup:", error);
    }
  }

  private setupBackups() {
    // Create daily backups
    setInterval(() => {
      this.createBackup().catch(error => {
        console.error("[ContextDB] Backup failed:", error);
      });
    }, 24 * 60 * 60 * 1000);

    // Create initial backup
    this.createBackup().catch(error => {
      console.error("[ContextDB] Initial backup failed:", error);
    });
  }

  async updateFile(entry: FileEntry): Promise<void> {
    await this.ensureInitialized();
    console.error(`[ContextDB] Updating file in database: ${entry.path}`);
    console.error(`[ContextDB] File details: type=${entry.fileType}, contentType=${entry.contentType}, size=${entry.metadata.size}`);
    
    try {
      const stmt = this.db.prepare(`
        INSERT OR REPLACE INTO files 
        (path, content, contentType, metadata, hash, lastModified, fileType) 
        VALUES (?, ?, ?, ?, ?, ?, ?)`
      );
      
      stmt.run(
        entry.path,
        entry.content,
        entry.contentType,
        JSON.stringify(entry.metadata),
        entry.hash,
        entry.lastModified,
        entry.fileType
      );
      
      console.error(`[ContextDB] Successfully updated file: ${entry.path}`);
    } catch (error) {
      console.error(`[ContextDB] Error updating file ${entry.path}:`, error);
      throw error;
    }
  }

  async getFile(path: string): Promise<FileEntry | null> {
    await this.ensureInitialized();
    console.error(`[ContextDB] Getting file from database: ${path}`);
    
    try {
      const stmt = this.db.prepare("SELECT * FROM files WHERE path = ?");
      const result = stmt.get(path) as {
        path: string;
        content: Buffer | string | null;
        contentType: string;
        metadata: string;
        hash: string;
        lastModified: number;
        fileType: FileEntry["fileType"];
      } | undefined;
      
      if (!result) {
        console.error(`[ContextDB] File not found: ${path}`);
        return null;
      }
      
      console.error(`[ContextDB] Found file: ${path}, type=${result.fileType}, contentType=${result.contentType}`);
      
      const entry = {
        path: result.path,
        content: result.content,
        contentType: result.contentType as FileEntry["contentType"],
        metadata: JSON.parse(result.metadata),
        hash: result.hash,
        lastModified: result.lastModified,
        fileType: result.fileType
      };
      
      return entry;
    } catch (error) {
      console.error(`[ContextDB] Error getting file ${path}:`, error);
      throw error;
    }
  }

  async storeFileChunks(fileHash: string, chunks: Buffer[], totalChunks: number): Promise<void> {
    await this.ensureInitialized();
    const stmt = this.db.prepare(`
      INSERT OR REPLACE INTO file_chunks (fileHash, chunkIndex, totalChunks, data)
      VALUES (?, ?, ?, ?)`
    );

    const transaction = this.db.transaction((chunks: Buffer[]) => {
      chunks.forEach((chunk, index) => {
        stmt.run(fileHash, index, totalChunks, chunk);
      });
    });

    transaction(chunks);
  }

  async getFileChunks(fileHash: string): Promise<Buffer[]> {
    await this.ensureInitialized();
    const stmt = this.db.prepare(`
      SELECT data FROM file_chunks 
      WHERE fileHash = ? 
      ORDER BY chunkIndex ASC`
    );
    
    const chunks = stmt.all(fileHash) as { data: Buffer }[];
    return chunks.map(chunk => chunk.data);
  }

  async cacheCommand(entry: CommandEntry): Promise<void> {
    await this.ensureInitialized();
    const stmt = this.db.prepare(
      "INSERT OR REPLACE INTO commands (hash, command, output, timestamp) VALUES (?, ?, ?, ?)"
    );
    stmt.run(entry.hash, entry.command, entry.output, entry.timestamp);
  }

  async getCommand(command: string): Promise<CommandEntry | null> {
    await this.ensureInitialized();
    const hash = crypto.createHash("sha256").update(command).digest("hex");
    const stmt = this.db.prepare("SELECT * FROM commands WHERE hash = ?");
    return stmt.get(hash) as CommandEntry | null;
  }

  async updateProjectStructure(structure: ProjectStructure): Promise<void> {
    await this.ensureInitialized();
    // Start a transaction
    const transaction = this.db.transaction((structure: ProjectStructure) => {
      // Update project structure
      const stmt = this.db.prepare(
        "INSERT OR REPLACE INTO project_structure (id, rootPath, poetryConfig) VALUES (1, ?, ?)"
      );
      stmt.run(structure.rootPath, JSON.stringify(structure.poetryConfig));

      // Don't clear files table when updating project structure
      // This allows files to accumulate from scanning
      console.error(`[ContextDB] Updated project structure for ${structure.rootPath}`);
    });

    transaction(structure);
  }

  async getAllFiles(): Promise<FileEntry[]> {
    await this.ensureInitialized();
    console.error("[ContextDB] Getting all files from database");
    const stmt = this.db.prepare("SELECT * FROM files");
    const results = stmt.all() as {
      path: string;
      content: Buffer | string | null;
      contentType: string;
      metadata: string;
      hash: string;
      lastModified: number;
      fileType: FileEntry["fileType"];
    }[];
    
    return results.map(result => ({
      path: result.path,
      content: result.content,
      contentType: result.contentType as FileEntry["contentType"],
      metadata: JSON.parse(result.metadata),
      hash: result.hash,
      lastModified: result.lastModified,
      fileType: result.fileType
    }));
  }

  async getProjectStructure(): Promise<ProjectStructure | null> {
    await this.ensureInitialized();
    console.error("[ContextDB] Getting project structure");
    const stmt = this.db.prepare("SELECT * FROM project_structure WHERE id = 1");
    const result = stmt.get() as { rootPath: string; poetryConfig: string } | undefined;
    if (!result) {
      console.error("[ContextDB] No project structure found");
      return null;
    }
    
    const files = await this.getAllFiles();
    console.error(`[ContextDB] Found ${files.length} files in database`);
    
    // Log each file for debugging
    files.forEach(file => {
      console.error(`[ContextDB] File: ${file.path} (${file.fileType})`);
    });
    
    const structure = {
      rootPath: result.rootPath,
      poetryConfig: JSON.parse(result.poetryConfig),
      files
    };
    
    console.error("[ContextDB] Returning project structure:", JSON.stringify(structure, null, 2));
    return structure;
  }

  async invalidateFile(path: string): Promise<void> {
    await this.ensureInitialized();
    console.error(`[ContextDB] Invalidating file in cache: ${path}`);
    
    try {
      // Get file to get its hash
      const file = await this.getFile(path);
      if (!file) {
        console.error(`[ContextDB] File not found for invalidation: ${path}`);
        return;
      }

      // Start a transaction
      const transaction = this.db.transaction(() => {
        // Delete from files table
        const deleteFileStmt = this.db.prepare("DELETE FROM files WHERE path = ?");
        deleteFileStmt.run(path);

        // Delete chunks if they exist
        if (file.contentType === "chunked") {
          const deleteChunksStmt = this.db.prepare("DELETE FROM file_chunks WHERE fileHash = ?");
          deleteChunksStmt.run(file.hash);
        }
      });

      transaction();
      console.error(`[ContextDB] Successfully invalidated file: ${path}`);
    } catch (error) {
      console.error(`[ContextDB] Error invalidating file ${path}:`, error);
      throw error;
    }
  }

  close(): void {
    this.db.close();
  }
}
