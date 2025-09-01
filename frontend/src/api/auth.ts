import { request } from '@/utils/request'
import type { LoginForm, RegisterForm, LoginResponse, User } from '@/types/user'
import type { ApiResponse } from '@/types/common'

/**
 * 认证相关API
 */
export const authApi = {
  /**
   * 用户登录
   */
  login(data: LoginForm): Promise<ApiResponse<LoginResponse>> {
    // 后端期望application/x-www-form-urlencoded格式
    const params = new URLSearchParams()
    params.append('username', data.username)
    params.append('password', data.password)
    
    return request.post('/auth/login', params, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    })
  },

  /**
   * 用户注册
   */
  register(data: RegisterForm): Promise<ApiResponse<User>> {
    return request.post('/auth/register', data)
  },

  /**
   * 用户登出
   */
  logout(): Promise<ApiResponse<null>> {
    return request.post('/auth/logout')
  },

  /**
   * 刷新token
   */
  refreshToken(): Promise<ApiResponse<{ access_token: string }>> {
    return request.post('/auth/refresh')
  },

  /**
   * 验证token
   */
  verifyToken(): Promise<ApiResponse<User>> {
    return request.get('/auth/verify')
  },

  /**
   * 忘记密码
   */
  forgotPassword(email: string): Promise<ApiResponse<null>> {
    return request.post('/auth/forgot-password', { email })
  },

  /**
   * 重置密码
   */
  resetPassword(data: {
    token: string
    new_password: string
  }): Promise<ApiResponse<null>> {
    return request.post('/auth/reset-password', data)
  },

  /**
   * 发送验证邮件
   */
  sendVerificationEmail(): Promise<ApiResponse<null>> {
    return request.post('/auth/send-verification')
  },

  /**
   * 验证邮箱
   */
  verifyEmail(token: string): Promise<ApiResponse<null>> {
    return request.post('/auth/verify-email', { token })
  },

  /**
   * 检查用户名是否可用
   */
  checkUsername(username: string): Promise<ApiResponse<{ available: boolean }>> {
    return request.get(`/auth/check-username/${username}`)
  },

  /**
   * 检查邮箱是否可用
   */
  checkEmail(email: string): Promise<ApiResponse<{ available: boolean }>> {
    return request.get(`/auth/check-email/${email}`)
  }
}