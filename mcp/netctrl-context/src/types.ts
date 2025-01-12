export type FileContentType = 'text' | 'binary' | 'chunked';

export interface FileMetadata {
  size: number;
  mimeType: string;
  encoding?: BufferEncoding;
}

export interface FileEntry {
  path: string;
  content: string | Buffer | null;
  contentType: FileContentType;
  metadata: FileMetadata;
  hash: string;
  lastModified: number;
  fileType: 'python' | 'yaml' | 'pdf' | 'other';
}

export interface FileChunk {
  fileHash: string;
  chunkIndex: number;
  totalChunks: number;
  data: Buffer;
}

// Maximum file size for direct content storage (100KB)
export const MAX_DIRECT_FILE_SIZE = 100 * 1024;
// Maximum chunk size (50KB)
export const MAX_CHUNK_SIZE = 50 * 1024;

export interface CommandEntry {
  command: string;
  output: string;
  timestamp: number;
  hash: string;
}

export interface ProjectStructure {
  rootPath: string;
  poetryConfig?: {
    virtualEnvPath?: string;
    dependencies: Record<string, string>;
    devDependencies: Record<string, string>;
  };
  files: FileEntry[];
}
