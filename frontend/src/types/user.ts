// 用户相关类型定义

export interface User {
  id: number
  username: string
  email: string
  nickname?: string
  avatar_url?: string
  bio?: string
  is_active: boolean
  created_at: string
  updated_at: string
}

export interface LoginForm {
  username: string
  password: string
  remember?: boolean
}

export interface RegisterForm {
  username: string
  email: string
  password: string
  nickname?: string
}

export interface ChangePasswordForm {
  old_password: string
  new_password: string
}

export interface UpdateUserForm {
  nickname?: string
  bio?: string
  avatar_url?: string
}

export interface LoginResponse {
  access_token: string
  token_type: string
  user: User
}

export interface ApiResponse<T = any> {
  code: number
  message: string
  data: T
}

// 用户统计信息
export interface UserStats {
  total_works: number
  total_words: number
  total_chapters: number
  today_words: number
  writing_streak: number
}