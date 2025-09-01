import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { Work, WorkCreateForm, WorkUpdateForm, Volume, Chapter } from '@/types/work'
import { workApi } from '@/api/work'
import { ElMessage } from 'element-plus'

export const useWorkStore = defineStore('work', () => {
  // 状态
  const works = ref<Work[]>([])
  const currentWork = ref<Work | null>(null)
  const volumes = ref<Volume[]>([])
  const chapters = ref<Chapter[]>([])
  const loading = ref(false)
  
  // 计算属性
  const workList = computed(() => works.value)
  const currentWorkInfo = computed(() => currentWork.value)
  const volumeList = computed(() => volumes.value)
  const chapterList = computed(() => chapters.value)
  
  // 获取作品列表
  const fetchWorks = async (params?: any) => {
    try {
      loading.value = true
      const response = await workApi.getWorks(params)
      works.value = response.data.items
      return response
    } catch (error: any) {
      ElMessage.error('获取作品列表失败')
      throw error
    } finally {
      loading.value = false
    }
  }
  
  // 获取作品详情
  const fetchWorkDetail = async (id: number) => {
    try {
      loading.value = true
      const response = await workApi.getWork(id)
      currentWork.value = response.data
      return response
    } catch (error: any) {
      ElMessage.error('获取作品详情失败')
      throw error
    } finally {
      loading.value = false
    }
  }
  
  // 创建作品
  const createWork = async (workData: WorkCreateForm) => {
    try {
      const response = await workApi.createWork(workData)
      works.value.unshift(response.data)
      ElMessage.success('作品创建成功')
      return response
    } catch (error: any) {
      ElMessage.error(error.response?.data?.detail || '创建作品失败')
      throw error
    }
  }
  
  // 更新作品
  const updateWork = async (id: number, workData: WorkUpdateForm) => {
    try {
      const response = await workApi.updateWork(id, workData)
      const index = works.value.findIndex(work => work.id === id)
      if (index !== -1) {
        works.value[index] = response.data
      }
      if (currentWork.value?.id === id) {
        currentWork.value = response.data
      }
      ElMessage.success('作品更新成功')
      return response
    } catch (error: any) {
      ElMessage.error(error.response?.data?.detail || '更新作品失败')
      throw error
    }
  }
  
  // 删除作品
  const deleteWork = async (id: number) => {
    try {
      await workApi.deleteWork(id)
      works.value = works.value.filter(work => work.id !== id)
      if (currentWork.value?.id === id) {
        currentWork.value = null
      }
    } catch (error: any) {
      throw error
    }
  }
  
  // 获取作品卷列表
  const fetchVolumes = async (workId: number) => {
    try {
      const response = await workApi.getVolumes(workId)
      volumes.value = response.data
      return response
    } catch (error: any) {
      ElMessage.error('获取卷列表失败')
      throw error
    }
  }
  
  // 获取作品章节列表
  const fetchChapters = async (workId: number, volumeId?: number) => {
    try {
      const response = await workApi.getChapters(workId)
      // 确保 chapters.value 始终是数组
      const chaptersData = response.data.items || response.data
      chapters.value = Array.isArray(chaptersData) ? chaptersData : []
      return response
    } catch (error: any) {
      ElMessage.error('获取章节列表失败')
      throw error
    }
  }
  
  // 创建卷
  const createVolume = async (workId: number, volumeData: any) => {
    try {
      const response = await workApi.createVolume(workId, volumeData)
      volumes.value.push(response.data)
      return response
    } catch (error: any) {
      throw error
    }
  }
  
  // 更新卷
  const updateVolume = async (id: number, volumeData: any) => {
    try {
      const response = await workApi.updateVolume(id, volumeData)
      const index = volumes.value.findIndex(volume => volume.id === id)
      if (index !== -1) {
        volumes.value[index] = response.data
      }
      return response
    } catch (error: any) {
      throw error
    }
  }
  
  // 删除卷
  const deleteVolume = async (id: number) => {
    try {
      const response = await workApi.deleteVolume(id)
      const index = volumes.value.findIndex(volume => volume.id === id)
      if (index !== -1) {
        volumes.value.splice(index, 1)
      }
      return response
    } catch (error: any) {
      throw error
    }
  }
  
  // 创建章节
  const createChapter = async (workId: number, chapterData: any) => {
    try {
      const response = await workApi.createChapter(workId, chapterData)
      chapters.value.push(response.data)
      return response
    } catch (error: any) {
      throw error
    }
  }
  
  // 更新章节
  const updateChapter = async (id: number, chapterData: any) => {
    try {
      const response = await workApi.updateChapter(id, chapterData)
      // 后端现在只返回保存状态，不返回章节数据
      // 如果需要更新本地状态，可以直接使用传入的数据
      const index = chapters.value.findIndex(chapter => chapter.id === id)
      if (index !== -1) {
        // 使用传入的数据更新本地状态
        chapters.value[index] = { ...chapters.value[index], ...chapterData }
      }
      return response
    } catch (error: any) {
      throw error
    }
  }
  
  // 删除章节
  const deleteChapter = async (id: number) => {
    try {
      const response = await workApi.deleteChapter(id)
      // 不在这里更新本地状态，让组件层面的 loadWorkDetail() 来处理数据刷新
      return response
    } catch (error: any) {
      throw error
    }
  }
  
  // 清空状态
  const clearState = () => {
    works.value = []
    currentWork.value = null
    volumes.value = []
    chapters.value = []
  }
  
  return {
    // 状态
    works,
    currentWork,
    volumes,
    chapters,
    loading,
    
    // 计算属性
    workList,
    currentWorkInfo,
    volumeList,
    chapterList,
    
    // 方法
    fetchWorks,
    fetchWorkDetail,
    createWork,
    updateWork,
    deleteWork,
    fetchVolumes,
    fetchChapters,
    createVolume,
    updateVolume,
    deleteVolume,
    createChapter,
    updateChapter,
    deleteChapter,
    clearState
  }
})