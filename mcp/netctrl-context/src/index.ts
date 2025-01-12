#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ErrorCode,
  ListResourcesRequestSchema,
  ListToolsRequestSchema,
  McpError,
  ReadResourceRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import path from "path";
import fs from "fs/promises";
import { createReadStream } from 'fs';
import { ContextDB } from "./db.js";
import { FileWatcher } from "./watcher.js";
import { PoetryManager } from "./poetry.js";
import { Queue } from "./queue.js";
import crypto from "crypto";
import { glob } from 'glob';

interface ToolResponse {
  content: Array<{
    type: "text" | "binary";
    text?: string;
    data?: Buffer;
  }>;
}

class NetCtrlContextServer {
  private server: Server;
  private db: ContextDB | null = null;
  private watcher: FileWatcher | null = null;
  private poetry: PoetryManager | null = null;
  private projectRoot: string;
  private initialized: boolean = false;
  private operationQueue: Queue = new Queue();
  private changeCallbacks: Map<string, (path: string, content: string) => void> = new Map();

  constructor(projectRoot: string) {
    this.projectRoot = projectRoot;
    this.server = new Server(
      {
        name: "netctrl-context",
        version: "0.1.0",
      },
      {
        capabilities: {
          resources: {},
          tools: {},
        },
      }
    );
    
    this.server.onerror = (error) => console.error("[MCP Error]", error);
    process.on("SIGINT", async () => {
      await this.cleanup();
      process.exit(0);
    });
  }

  private async cleanup(): Promise<void> {
    if (this.watcher) {
      await this.watcher.close();
    }
    if (this.db) {
      await this.db.close();
    }
    await this.server.close();
  }

  private async ensureInitialized(): Promise<void> {
    if (!this.initialized || !this.db || !this.watcher || !this.poetry) {
      throw new Error("Server components not initialized");
    }
  }

  private getDB(): ContextDB {
    if (!this.db) throw new Error("Database not initialized");
    return this.db;
  }

  private getWatcher(): FileWatcher {
    if (!this.watcher) throw new Error("File watcher not initialized");
    return this.watcher;
  }

  private getPoetry(): PoetryManager {
    if (!this.poetry) throw new Error("Poetry manager not initialized");
    return this.poetry;
  }

  private async initializeComponents(): Promise<void> {
    console.error("[MCP] Initializing components");
    
    try {
      console.error("[MCP] Initializing database");
      this.db = new ContextDB(this.projectRoot);
      await this.db.initialize();
      console.error("[MCP] Database initialized");

      console.error("[MCP] Initializing file watcher");
      this.watcher = new FileWatcher(this.projectRoot, this.db);
      await this.watcher.start();
      console.error("[MCP] File watcher initialized");

      console.error("[MCP] Initializing poetry manager");
      this.poetry = new PoetryManager(this.projectRoot);
      console.error("[MCP] Poetry manager initialized");

      this.setupToolHandlers();
      this.setupResourceHandlers();
      
      this.initialized = true;
      console.error("[MCP] All components initialized");
    } catch (error) {
      console.error("[MCP] Failed to initialize components:", error);
      throw error;
    }
  }

  private setupToolHandlers() {
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [
        {
          name: "cache_command",
          description: "Cache command output for future use",
          inputSchema: {
            type: "object",
            properties: {
              command: {
                type: "string",
                description: "Command to execute and cache",
              },
            },
            required: ["command"],
          },
        },
        {
          name: "get_project_structure",
          description: "Get current project structure and Poetry configuration",
          inputSchema: {
            type: "object",
            properties: {},
            required: [],
          },
        },
        {
          name: "get_file_content",
          description: "Get cached content of a file",
          inputSchema: {
            type: "object",
            properties: {
              path: {
                type: "string",
                description: "Path to the file",
              },
            },
            required: ["path"],
          },
        },
        {
          name: "rescan_files",
          description: "Trigger a manual rescan of all project files",
          inputSchema: {
            type: "object",
            properties: {},
            required: [],
          },
        },
        {
          name: "search_files",
          description: "Search for files matching a pattern and content",
          inputSchema: {
            type: "object",
            properties: {
              pattern: {
                type: "string",
                description: "Glob pattern to match files",
              },
              content: {
                type: "string",
                description: "Optional content to search for",
              },
            },
            required: ["pattern"],
          },
        },
        {
          name: "watch_changes",
          description: "Watch for file changes and get notifications",
          inputSchema: {
            type: "object",
            properties: {
              pattern: {
                type: "string",
                description: "Glob pattern to watch",
              },
              callback: {
                type: "string",
                description: "Callback ID for notifications",
              },
            },
            required: ["pattern", "callback"],
          },
        },
        {
          name: "batch_update",
          description: "Update multiple files in a single operation",
          inputSchema: {
            type: "object",
            properties: {
              updates: {
                type: "array",
                items: {
                  type: "object",
                  properties: {
                    path: { type: "string" },
                    content: { type: "string" },
                  },
                  required: ["path", "content"],
                },
              },
            },
            required: ["updates"],
          },
        },
        {
          name: "stream_content",
          description: "Stream file content in chunks",
          inputSchema: {
            type: "object",
            properties: {
              path: {
                type: "string",
                description: "Path to the file",
              },
              chunkSize: {
                type: "number",
                description: "Size of each chunk in bytes",
              },
            },
            required: ["path"],
          },
        },
        {
          name: "regex_search",
          description: "Search files using regex pattern",
          inputSchema: {
            type: "object",
            properties: {
              pattern: {
                type: "string",
                description: "Regex pattern to search for",
              },
              filePattern: {
                type: "string",
                description: "Glob pattern for files to search",
              },
            },
            required: ["pattern"],
          },
        },
        {
          name: "invalidate_cache",
          description: "Invalidate cached file content",
          inputSchema: {
            type: "object",
            properties: {
              pattern: {
                type: "string",
                description: "Glob pattern of files to invalidate",
              },
            },
            required: ["pattern"],
          },
        },
      ],
    }));

    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      switch (request.params.name) {
        case "cache_command": {
          const { command } = request.params.arguments as { command: string };
          const hash = crypto.createHash("sha256").update(command).digest("hex");
          await this.ensureInitialized();
          const cached = await this.getDB().getCommand(command);
          
          if (cached) {
            return {
              content: [
                {
                  type: "text",
                  text: cached.output,
                },
              ],
            };
          }

          const { exec } = await import('child_process');
          const { promisify } = await import('util');
          const execAsync = promisify(exec);
          
          try {
            const { stdout } = await execAsync(command);
            await this.ensureInitialized();
            await this.getDB().cacheCommand({
              command,
              output: stdout,
              timestamp: Date.now(),
              hash
            });
            return {
              content: [
                {
                  type: "text",
                  text: stdout,
                },
              ],
            };
          } catch (error: any) {
            throw new McpError(
              ErrorCode.InvalidRequest,
              `Failed to execute command: ${error.message}`
            );
          }
        }

        case "get_project_structure": {
          await this.ensureInitialized();
          const structure = await this.getDB().getProjectStructure();
          if (!structure) {
            throw new McpError(
              ErrorCode.InvalidRequest,
              "Project structure not available"
            );
          }

          return {
            content: [
              {
                type: "text",
                text: JSON.stringify(structure, null, 2),
              },
            ],
          };
        }

        case "get_file_content": {
          const { path: filePath } = request.params.arguments as { path: string };
          await this.ensureInitialized();
          const file = await this.getDB().getFile(filePath);
          if (!file) {
            throw new McpError(
              ErrorCode.InvalidRequest,
              `File not found: ${filePath}`
            );
          }

          if (file.contentType === "chunked") {
            await this.ensureInitialized();
            const chunks = await this.getDB().getFileChunks(file.hash);
            const content = Buffer.concat(chunks);
            
            if (file.metadata.mimeType.startsWith("text/") || 
                file.metadata.mimeType === "application/json" ||
                file.metadata.mimeType === "application/javascript") {
              return {
                content: [
                  {
                    type: "text",
                    text: content.toString(file.metadata.encoding || "utf-8"),
                  },
                ],
              };
            } else {
              return {
                content: [
                  {
                    type: "binary",
                    data: content,
                    mimeType: file.metadata.mimeType,
                  },
                ],
              };
            }
          } else {
            if (file.contentType === "text") {
              return {
                content: [
                  {
                    type: "text",
                    text: file.content as string,
                  },
                ],
              };
            } else {
              return {
                content: [
                  {
                    type: "binary",
                    data: file.content as Buffer,
                    mimeType: file.metadata.mimeType,
                  },
                ],
              };
            }
          }
        }

        case "rescan_files": {
          console.error("[MCP] Starting manual file rescan");
          await this.ensureInitialized();
          await this.getWatcher().rescanFiles();
          console.error("[MCP] Manual file rescan complete");
          return {
            content: [
              {
                type: "text",
                text: "File rescan completed successfully",
              },
            ],
          };
        }

        case "search_files": {
          const { pattern, content } = request.params.arguments as { 
            pattern: string; 
            content?: string 
          };
          const matches = await glob(path.join(this.projectRoot, pattern));
          const results = [];

          for (const match of matches) {
            if (content) {
              const fileContent = await fs.readFile(match, 'utf8');
              if (fileContent.includes(content)) {
                results.push(match);
              }
            } else {
              results.push(match);
            }
          }

          return {
            content: [
              {
                type: "text",
                text: JSON.stringify(results, null, 2),
              },
            ],
          };
        }

        case "watch_changes": {
          const { pattern, callback } = request.params.arguments as { 
            pattern: string; 
            callback: string 
          };
          
          this.changeCallbacks.set(callback, async (filepath, content) => {
            if (filepath.match(pattern)) {
              console.error(`[FileWatch] Change in ${filepath}`);
            }
          });

          return {
            content: [
              {
                type: "text",
                text: `Watching ${pattern} with callback ${callback}`,
              },
            ],
          };
        }

        case "stream_content": {
          const { path: filePath, chunkSize = 1024 * 1024 } = request.params.arguments as { 
            path: string; 
            chunkSize?: number 
          };

          const fullPath = path.join(this.projectRoot, filePath);
          const stream = createReadStream(fullPath, { highWaterMark: chunkSize });
          
          const chunks: Buffer[] = [];
          for await (const chunk of stream) {
            chunks.push(Buffer.from(chunk));
          }

          return {
            content: chunks.map(chunk => ({
              type: "binary",
              data: chunk
            }))
          };
        }

        case "regex_search": {
          const { pattern, filePattern = "**/*" } = request.params.arguments as {
            pattern: string;
            filePattern?: string;
          };

          const regex = new RegExp(pattern);
          const matches = await glob(path.join(this.projectRoot, filePattern));
          const results = [];

          for (const match of matches) {
            try {
              const content = await fs.readFile(match, 'utf8');
              const lines = content.split('\n');
              for (let i = 0; i < lines.length; i++) {
                if (regex.test(lines[i])) {
                  results.push({
                    file: match,
                    line: i + 1,
                    content: lines[i].trim(),
                    matches: [...lines[i].matchAll(regex)].map(m => ({
                      index: m.index,
                      match: m[0]
                    }))
                  });
                }
              }
            } catch (error) {
              console.error(`Error searching file ${match}:`, error);
            }
          }

          return {
            content: [{
              type: "text",
              text: JSON.stringify(results, null, 2)
            }]
          };
        }

        case "batch_update": {
          const { updates } = request.params.arguments as { 
            updates: Array<{ path: string; content: string }> 
          };

          const results = await Promise.all(
            updates.map(update => 
              this.operationQueue.add(async () => {
                try {
                  const fullPath = path.join(this.projectRoot, update.path);
                  await fs.writeFile(fullPath, update.content);
                  return { path: update.path, success: true };
                } catch (error) {
                  return { path: update.path, success: false, error: String(error) };
                }
              })
            )
          );

          return {
            content: [{
              type: "text",
              text: JSON.stringify(results, null, 2)
            }]
          };
        }

        case "invalidate_cache": {
          const { pattern } = request.params.arguments as { pattern: string };
          const matches = await glob(path.join(this.projectRoot, pattern));
          
          await this.ensureInitialized();
          for (const match of matches) {
            const relativePath = path.relative(this.projectRoot, match);
            await this.getDB().invalidateFile(relativePath);
          }

          return {
            content: [{
              type: "text",
              text: `Invalidated cache for ${matches.length} files`
            }]
          };
        }

        default:
          throw new McpError(
            ErrorCode.MethodNotFound,
            `Unknown tool: ${request.params.name}`
          );
      }
    });
  }

  private setupResourceHandlers() {
    this.server.setRequestHandler(ListResourcesRequestSchema, async () => ({
      resources: [
        {
          uri: "netctrl://project/structure",
          name: "Project Structure",
          description: "Current project structure including Poetry configuration",
          mimeType: "application/json",
        },
        {
          uri: "netctrl://project/poetry",
          name: "Poetry Configuration",
          description: "Poetry project information and dependencies",
          mimeType: "application/json",
        },
      ],
    }));

    this.server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
      if (request.params.uri === "netctrl://project/structure") {
        await this.ensureInitialized();
        const structure = await this.getDB().getProjectStructure();
        if (!structure) {
          throw new McpError(
            ErrorCode.InvalidRequest,
            "Project structure not available"
          );
        }

        return {
          contents: [
            {
              uri: request.params.uri,
              mimeType: "application/json",
              text: JSON.stringify(structure, null, 2),
            },
          ],
        };
      }

      if (request.params.uri === "netctrl://project/poetry") {
        await this.ensureInitialized();
        const info = await this.getPoetry().getProjectInfo();
        const deps = await this.getPoetry().getDependencies();
        const venvPath = await this.getPoetry().getVirtualEnvPath();

        return {
          contents: [
            {
              uri: request.params.uri,
              mimeType: "application/json",
              text: JSON.stringify(
                {
                  project: info,
                  virtualEnvPath: venvPath,
                  dependencies: deps.dependencies,
                  devDependencies: deps.devDependencies,
                },
                null,
                2
              ),
            },
          ],
        };
      }

      throw new McpError(
        ErrorCode.InvalidRequest,
        `Unknown resource: ${request.params.uri}`
      );
    });
  }

  async run(): Promise<void> {
    try {
      await this.initializeComponents();

      try {
        await fs.access(path.join(this.projectRoot, "netctrl/pyproject.toml"));
      } catch {
        console.error("[Poetry] No pyproject.toml found in netctrl directory");
        await this.ensureInitialized();
        await this.getDB().updateProjectStructure({
          rootPath: this.projectRoot,
          files: [],
        });
        const transport = new StdioServerTransport();
        await this.server.connect(transport);
        console.error("NetCtrl Context MCP server running on stdio");
        return;
      }

      try {
        await this.ensureInitialized();
        const poetryConfig = await this.getPoetry().getDependencies();
        const virtualEnvPath = await this.getPoetry().getVirtualEnvPath();
        
        await this.getDB().updateProjectStructure({
          rootPath: this.projectRoot,
          poetryConfig: {
            virtualEnvPath: virtualEnvPath || undefined,
            ...poetryConfig,
          },
          files: [],
        });
      } catch (error) {
        console.error("[Poetry] Failed to read Poetry configuration:", error);
        await this.getDB().updateProjectStructure({
          rootPath: this.projectRoot,
          files: [],
        });
      }

      const transport = new StdioServerTransport();
      await this.server.connect(transport);
      console.error("NetCtrl Context MCP server running on stdio");
    } catch (error) {
      console.error("[MCP] Failed to initialize server:", error);
      process.exit(1);
    }
  }
}

// Get project root from environment variable or use current directory
const projectRoot = process.env.NETCTRL_PROJECT_ROOT || process.cwd();
const server = new NetCtrlContextServer(projectRoot);
server.run().catch(console.error);
