import { request } from '@/utils/request'
import type {
  Work,
  WorkCreateForm,
  WorkUpdateForm,
  Volume,
  VolumeCreateForm,
  VolumeUpdateForm,
  Chapter,
  ChapterCreateForm,
  ChapterUpdateForm,
  ChapterVersion,
  WorkFavorite,
  WorkQuery
  // ChapterQuery 暂未使用
} from '@/types/work'
import type { ApiResponse, PaginatedResponse, ExportOptions, MessageResponse } from '@/types/common'

/**
 * 作品相关API
 */
export const workApi = {
  /**
   * 获取作品列表
   */
  getWorks(params?: WorkQuery): Promise<ApiResponse<PaginatedResponse<Work>>> {
    return request.get('/works', { params })
  },

  /**
   * 获取作品详情
   */
  getWork(id: number): Promise<ApiResponse<Work>> {
    return request.get(`/works/${id}`)
  },

  /**
   * 创建作品
   */
  createWork(data: WorkCreateForm): Promise<ApiResponse<Work>> {
    return request.post('/works/', data)
  },

  /**
   * 保存草稿
   */
  saveDraft(data: WorkCreateForm): Promise<ApiResponse<Work>> {
    const draftData = { ...data, status: 'DRAFT' }
    return request.post('/works/', draftData)
  },

  /**
   * 更新作品
   */
  updateWork(id: number, data: WorkUpdateForm): Promise<ApiResponse<Work>> {
    return request.put(`/works/${id}`, data)
  },

  /**
   * 删除作品
   */
  deleteWork(id: number): Promise<ApiResponse<null>> {
    return request.delete(`/works/${id}`)
  },

  /**
   * 上传作品封面
   */
  uploadCover(id: number, file: File): Promise<ApiResponse<{ cover_url: string }>> {
    const formData = new FormData()
    formData.append('file', file)
    return request.upload(`/v1/upload/cover`, formData)
  },

  /**
   * 获取作品卷列表
   */
  getVolumes(workId: number): Promise<ApiResponse<Volume[]>> {
    return request.get(`/volumes/?work_id=${workId}`)
  },

  /**
   * 创建卷
   */
  createVolume(workId: number, data: VolumeCreateForm): Promise<ApiResponse<Volume>> {
    return request.post('/volumes/', { ...data, work_id: workId })
  },

  /**
   * 更新卷
   */
  updateVolume(id: number, data: VolumeUpdateForm): Promise<ApiResponse<Volume>> {
    return request.put(`/volumes/${id}`, data)
  },

  /**
   * 删除卷
   */
  deleteVolume(id: number): Promise<ApiResponse<null>> {
    return request.delete(`/volumes/${id}`)
  }
}