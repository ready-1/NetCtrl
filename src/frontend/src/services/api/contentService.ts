import api from './apiClient';
import {
  Content,
  ContentWithRelations,
  ContentCreate,
  ContentUpdate,
  ContentListResponse,
  ContentQueryParams,
  ContentPermission,
} from '../../types/content';

/**
 * Content API Service
 * 
 * Provides methods for interacting with the Content Management API endpoints
 */
const contentService = {
  /**
   * Get a paginated list of content items with optional filtering
   */
  getContentList: async (params: ContentQueryParams = {}): Promise<ContentListResponse> => {
    const response = await api.get<ContentListResponse>('/api/v1/content/', { params });
    return response.data;
  },

  /**
   * Get a single content item by ID
   */
  getContent: async (id: number): Promise<ContentWithRelations> => {
    const response = await api.get<ContentWithRelations>(`/api/v1/content/${id}`);
    return response.data;
  },

  /**
   * Create a new content item
   */
  createContent: async (content: ContentCreate): Promise<Content> => {
    const response = await api.post<Content>('/api/v1/content/', content);
    return response.data;
  },

  /**
   * Update an existing content item
   */
  updateContent: async (id: number, content: ContentUpdate): Promise<Content> => {
    const response = await api.put<Content>(`/api/v1/content/${id}`, content);
    return response.data;
  },

  /**
   * Patch specific fields of a content item
   */
  patchContent: async (id: number, content: ContentUpdate): Promise<Content> => {
    const response = await api.patch<Content>(`/api/v1/content/${id}`, content);
    return response.data;
  },

  /**
   * Delete a content item
   */
  deleteContent: async (id: number): Promise<void> => {
    await api.delete(`/api/v1/content/${id}`);
  },

  /**
   * Get the version history of a content item
   */
  getContentVersions: async (id: number): Promise<any[]> => {
    const response = await api.get<any[]>(`/api/v1/content/${id}/versions`);
    return response.data;
  },

  /**
   * Get a specific version of a content item
   */
  getContentVersion: async (id: number, versionId: string): Promise<Content> => {
    const response = await api.get<Content>(`/api/v1/content/${id}/versions/${versionId}`);
    return response.data;
  },

  /**
   * Roll back to a previous version
   */
  rollbackContent: async (id: number, versionId: string): Promise<Content> => {
    const response = await api.post<Content>(`/api/v1/content/${id}/rollback`, { version_id: versionId });
    return response.data;
  },

  /**
   * Get the permissions for a content item
   */
  getContentPermissions: async (id: number): Promise<ContentPermission[]> => {
    const response = await api.get<ContentPermission[]>(`/api/v1/content/${id}/permissions`);
    return response.data;
  },

  /**
   * Update permissions for a content item
   */
  updateContentPermissions: async (
    id: number, 
    permissions: Partial<ContentPermission>[]
  ): Promise<ContentPermission[]> => {
    const response = await api.put<ContentPermission[]>(`/api/v1/content/${id}/permissions`, { permissions });
    return response.data;
  },

  /**
   * Get files associated with a content item
   */
  getContentFiles: async (id: number): Promise<any[]> => {
    const response = await api.get<any[]>(`/api/v1/content/${id}/files`);
    return response.data;
  },
};

export default contentService;
