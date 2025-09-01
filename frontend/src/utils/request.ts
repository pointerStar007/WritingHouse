import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios'
import { ElMessage, ElMessageBox } from 'element-plus'
import { getToken, removeToken } from './auth'
import router from '@/router'
import NProgress from 'nprogress'

// 创建axios实例
const service: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '/api',
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器
service.interceptors.request.use(
  (config: AxiosRequestConfig) => {
    // 开始进度条
    NProgress.start()
    
    // 添加认证token
    const token = getToken()
    if (token && config.headers) {
      config.headers.Authorization = `Bearer ${token}`
    }
    
    return config
  },
  (error) => {
    NProgress.done()
    console.error('Request error:', error)
    return Promise.reject(error)
  }
)

// 响应拦截器
service.interceptors.response.use(
  (response: AxiosResponse) => {
    NProgress.done()
    
    // 检查响应数据格式
    const responseData = response.data
    
    // 如果是blob类型响应，直接返回
    if (responseData instanceof Blob) {
      return responseData
    }
    
    // 如果响应包含code字段，按原逻辑处理
    if (responseData && typeof responseData === 'object' && 'code' in responseData) {
      const { code, message } = responseData
      
      // 成功响应
      if (code === 200 || code === 0) {
        return responseData
      }
      
      // 业务错误
      ElMessage.error(message || '请求失败')
      return Promise.reject(new Error(message || '请求失败'))
    }
    
    // 如果响应是直接的数据对象（如用户对象），包装成标准格式
    return {
      code: 200,
      message: 'success',
      data: responseData
    }
  },
  (error) => {
    NProgress.done()
    
    const { response } = error
    
    if (response) {
      const { status, data } = response
      
      switch (status) {
        case 401: {
          // 未授权，清除token并跳转到登录页
          ElMessageBox.confirm(
            '登录状态已过期，请重新登录',
            '系统提示',
            {
              confirmButtonText: '重新登录',
              cancelButtonText: '取消',
              type: 'warning'
            }
          ).then(() => {
            removeToken()
            router.push('/login')
          })
          break
        }
        case 403:
          ElMessage.error('没有权限访问该资源')
          break
        case 404:
          ElMessage.error('请求的资源不存在')
          break
        case 422:
          // 表单验证错误
          if (data && data.detail) {
            if (Array.isArray(data.detail)) {
              // FastAPI 验证错误格式
              const errors = data.detail.map((err: any) => {
                const field = err.loc ? err.loc.join('.') : 'unknown'
                return `${field}: ${err.msg}`
              }).join(', ')
              ElMessage.error(`验证错误: ${errors}`)
            } else {
              ElMessage.error(data.detail)
            }
          } else {
            ElMessage.error('请求参数错误')
          }
          break
        case 500:
          ElMessage.error('服务器内部错误')
          break
        default:
          ElMessage.error(data?.message || data?.detail || `请求失败 (${status})`)
      }
    } else if (error.code === 'ECONNABORTED') {
      ElMessage.error('请求超时，请稍后重试')
    } else if (error.message === 'Network Error') {
      ElMessage.error('网络连接失败，请检查网络设置')
    } else {
      ElMessage.error('请求失败，请稍后重试')
    }
    
    return Promise.reject(error)
  }
)

// 导出请求实例
export const request = service

// 导出常用请求方法
export default {
  get<T = any>(url: string, config?: AxiosRequestConfig): Promise<T> {
    return service.get(url, config)
  },
  
  post<T = any>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> {
    return service.post(url, data, config)
  },
  
  put<T = any>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> {
    return service.put(url, data, config)
  },
  
  delete<T = any>(url: string, config?: AxiosRequestConfig): Promise<T> {
    return service.delete(url, config)
  },
  
  patch<T = any>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> {
    return service.patch(url, data, config)
  },
  
  upload<T = any>(url: string, formData: FormData, config?: AxiosRequestConfig): Promise<T> {
    return service.post(url, formData, {
      ...config,
      headers: {
        'Content-Type': 'multipart/form-data',
        ...config?.headers
      }
    })
  },
  
  download(url: string, config?: AxiosRequestConfig): Promise<Blob> {
    return service.get(url, {
      ...config,
      responseType: 'blob'
    })
  }
}