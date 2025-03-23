import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import contentService from '../services/api/contentService';
import {
  Content,
  ContentWithRelations,
  ContentCreate,
  ContentUpdate,
  ContentQueryParams,
  ContentListResponse,
} from '../types/content';

/**
 * React Query hooks for content-related API calls
 */

// Query key factory for content
const contentKeys = {
  all: ['content'] as const,
  lists: () => [...contentKeys.all, 'list'] as const,
  list: (params: ContentQueryParams) => [...contentKeys.lists(), params] as const,
  details: () => [...contentKeys.all, 'detail'] as const,
  detail: (id: number) => [...contentKeys.details(), id] as const,
  permissions: (id: number) => [...contentKeys.detail(id), 'permissions'] as const,
  versions: (id: number) => [...contentKeys.detail(id), 'versions'] as const,
  files: (id: number) => [...contentKeys.detail(id), 'files'] as const,
};

/**
 * Hook to fetch content list with filtering and pagination
 */
export const useContentList = (params: ContentQueryParams = {}) => {
  return useQuery({
    queryKey: contentKeys.list(params),
    queryFn: () => contentService.getContentList(params),
    keepPreviousData: true, // Keeps previous data while fetching new data
  });
};

/**
 * Hook to fetch a single content item by ID
 */
export const useContent = (id: number, options = {}) => {
  return useQuery({
    queryKey: contentKeys.detail(id),
    queryFn: () => contentService.getContent(id),
    enabled: !!id, // Only run if id is provided
    ...options,
  });
};

/**
 * Hook to create a new content item
 */
export const useCreateContent = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: (newContent: ContentCreate) => contentService.createContent(newContent),
    onSuccess: () => {
      // Invalidate the content list cache to trigger a refetch
      queryClient.invalidateQueries(contentKeys.lists());
    },
  });
};

/**
 * Hook to update an existing content item
 */
export const useUpdateContent = (id: number) => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: (updatedContent: ContentUpdate) => contentService.updateContent(id, updatedContent),
    onSuccess: (data) => {
      // Update the cache for this specific content item
      queryClient.setQueryData(contentKeys.detail(id), data);
      // Invalidate related lists to trigger a refetch
      queryClient.invalidateQueries(contentKeys.lists());
    },
  });
};

/**
 * Hook to patch an existing content item
 */
export const usePatchContent = (id: number) => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: (patchedContent: ContentUpdate) => contentService.patchContent(id, patchedContent),
    onSuccess: (data) => {
      // Update the cache for this specific content item
      queryClient.setQueryData(contentKeys.detail(id), data);
      // Invalidate related lists to trigger a refetch
      queryClient.invalidateQueries(contentKeys.lists());
    },
  });
};

/**
 * Hook to delete a content item
 */
export const useDeleteContent = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: (id: number) => contentService.deleteContent(id),
    onSuccess: (_, id) => {
      // Remove the item from the cache
      queryClient.removeQueries(contentKeys.detail(id));
      // Invalidate related lists to trigger a refetch
      queryClient.invalidateQueries(contentKeys.lists());
    },
  });
};

/**
 * Hook to fetch content versions
 */
export const useContentVersions = (id: number) => {
  return useQuery({
    queryKey: contentKeys.versions(id),
    queryFn: () => contentService.getContentVersions(id),
    enabled: !!id,
  });
};

/**
 * Hook to roll back to a previous version
 */
export const useRollbackContent = (id: number) => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: (versionId: string) => contentService.rollbackContent(id, versionId),
    onSuccess: (data) => {
      // Update the cache for this specific content item
      queryClient.setQueryData(contentKeys.detail(id), data);
      // Invalidate versions to trigger a refetch
      queryClient.invalidateQueries(contentKeys.versions(id));
    },
  });
};

/**
 * Hook to fetch content permissions
 */
export const useContentPermissions = (id: number) => {
  return useQuery({
    queryKey: contentKeys.permissions(id),
    queryFn: () => contentService.getContentPermissions(id),
    enabled: !!id,
  });
};

/**
 * Hook to update content permissions
 */
export const useUpdateContentPermissions = (id: number) => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: (permissions: Partial<{ role: string, can_view: boolean, can_edit: boolean, can_delete: boolean }>[]) => 
      contentService.updateContentPermissions(id, permissions),
    onSuccess: () => {
      // Invalidate permissions to trigger a refetch
      queryClient.invalidateQueries(contentKeys.permissions(id));
      // Also invalidate the content detail to update any embedded permissions
      queryClient.invalidateQueries(contentKeys.detail(id));
    },
  });
};

/**
 * Hook to fetch files associated with a content item
 */
export const useContentFiles = (id: number) => {
  return useQuery({
    queryKey: contentKeys.files(id),
    queryFn: () => contentService.getContentFiles(id),
    enabled: !!id,
  });
};
