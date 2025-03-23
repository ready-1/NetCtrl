/**
 * Content-related type definitions for the CMS
 */

// Content status options
export enum ContentStatus {
  DRAFT = 'draft',
  PUBLISHED = 'published',
  ARCHIVED = 'archived',
}

// Content type options
export enum ContentType {
  TEXT = 'text',
  HTML = 'html',
  MARKDOWN = 'markdown',
  FILE = 'file',
}

// Base content model
export interface Content {
  id: number;
  title: string;
  description: string | null;
  body: string | null;
  content_type: ContentType;
  status: ContentStatus;
  created_by: number;
  updated_by: number;
  created_at: string;
  updated_at: string;
}

// Content with relations (used for detailed views)
export interface ContentWithRelations extends Content {
  files?: ContentFile[];
  permissions?: ContentPermission[];
  creator?: {
    id: number;
    username: string;
  };
  updater?: {
    id: number;
    username: string;
  };
}

// Content creation payload
export interface ContentCreate {
  title: string;
  description?: string;
  body?: string;
  content_type: ContentType;
  status: ContentStatus;
}

// Content update payload
export interface ContentUpdate {
  title?: string;
  description?: string;
  body?: string;
  content_type?: ContentType;
  status?: ContentStatus;
}

// Content file model
export interface ContentFile {
  id: number;
  content_id: number;
  filename: string;
  file_path: string;
  file_size: number;
  mime_type: string;
  uploaded_at: string;
  uploaded_by: number;
}

// Permission level
export interface ContentPermission {
  id: number;
  content_id: number;
  role: string;
  can_view: boolean;
  can_edit: boolean;
  can_delete: boolean;
}

// Content query parameters
export interface ContentQueryParams {
  status?: ContentStatus;
  content_type?: ContentType;
  search?: string;
  page?: number;
  limit?: number;
  sort_by?: string;
  sort_order?: 'asc' | 'desc';
}

// Content list response
export interface ContentListResponse {
  items: Content[];
  total: number;
  page: number;
  limit: number;
  pages: number;
}
