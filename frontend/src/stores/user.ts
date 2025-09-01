import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { User, LoginForm, RegisterForm } from '@/types/user'
import { authApi } from '@/api/auth'
import { userApi } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'
import { ElMessage } from 'element-plus'

export const useUserStore = defineStore('user', () => {
  // 状态
  const user = ref<User | null>(null)
  const token = ref<string>(getToken() || '')
  
  // 计算属性
  const isAuthenticated = computed(() => !!token.value)
  const userInfo = computed(() => user.value)
  
  // 登录
  const login = async (loginForm: LoginForm) => {
    try {
      const response = await authApi.login(loginForm)
      const { access_token, user: userInfo } = response.data
      
      // 保存token和用户信息
      token.value = access_token
      user.value = userInfo
      setToken(access_token)
      
      ElMessage.success('登录成功')
      return response
    } catch (error: any) {
      ElMessage.error(error.response?.data?.detail || '登录失败')
      throw error
    }
  }
  
  // 注册
  const register = async (registerForm: RegisterForm) => {
    try {
      const response = await authApi.register(registerForm)
      ElMessage.success('注册成功，请登录')
      return response
    } catch (error: any) {
      ElMessage.error(error.response?.data?.detail || '注册失败')
      throw error
    }
  }
  
  // 登出
  const logout = () => {
    token.value = ''
    user.value = null
    removeToken()
    ElMessage.success('已退出登录')
  }
  
  // 获取用户信息
  const fetchUserInfo = async () => {
    try {
      const response = await userApi.getCurrentUser()
      user.value = response.data
      return response
    } catch (error: any) {
      ElMessage.error('获取用户信息失败')
      throw error
    }
  }
  
  // 更新用户信息
  const updateUserInfo = async (userData: Partial<User>) => {
    try {
      const response = await userApi.updateUser(userData)
      user.value = response.data
      ElMessage.success('更新成功')
      return response
    } catch (error: any) {
      ElMessage.error(error.response?.data?.detail || '更新失败')
      throw error
    }
  }
  
  // 修改密码
  const changePassword = async (oldPassword: string, newPassword: string) => {
    try {
      await userApi.changePassword({ old_password: oldPassword, new_password: newPassword })
      ElMessage.success('密码修改成功')
    } catch (error: any) {
      ElMessage.error(error.response?.data?.detail || '密码修改失败')
      throw error
    }
  }
  
  return {
    // 状态
    user,
    token,
    
    // 计算属性
    isAuthenticated,
    userInfo,
    
    // 方法
    login,
    register,
    logout,
    fetchUserInfo,
    updateUserInfo,
    changePassword
  }
})