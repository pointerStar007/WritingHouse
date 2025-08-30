// 用户相关类型
export interface User {
  id: number
  username: string
  email: string
  nickname?: string
  bio?: string
  avatar_url?: string
  created_at: string
  updated_at: string
}

export interface UserCreate {
  username: string
  email: string
  password: string
  nickname?: string
  bio?: string
}

export interface UserUpdate {
  nickname?: string
  bio?: string
  avatar_url?: string
}

// 作品相关类型
export enum WorkStatus {
  DRAFT = 'draft',
  WRITING = 'writing',
  COMPLETED = 'completed'
}

export enum WorkCategory {
  NOVEL = 'novel',
  ESSAY = 'essay',
  POETRY = 'poetry',
  NOTE = 'note'
}

export interface Work {
  id: number
  title: string
  description?: string
  content?: string
  category: WorkCategory
  status: WorkStatus
  word_count: number
  cover_url?: string
  user_id: number
  created_at: string
  updated_at: string
}

export interface WorkCreate {
  title: string
  description?: string
  content?: string
  category: WorkCategory
  status?: WorkStatus
  user_id: number
}

export interface WorkUpdate {
  title?: string
  description?: string
  content?: string
  category?: WorkCategory
  status?: WorkStatus
  cover_url?: string
}

// 灵感相关类型
export enum InspirationTag {
  CHARACTER = 'character',
  PLOT = 'plot',
  SCENE = 'scene',
  DIALOGUE = 'dialogue'
}

export interface Inspiration {
  id: number
  title: string
  content: string
  tag: InspirationTag
  user_id: number
  created_at: string
  updated_at: string
}

export interface InspirationCreate {
  title: string
  content: string
  tag: InspirationTag
  user_id: number
}

export interface InspirationUpdate {
  title?: string
  content?: string
  tag?: InspirationTag
}

// API响应类型
export interface ApiResponse<T = any> {
  code: number
  message: string
  data: T
}

export interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  size: number
  pages: number
}

// 统计数据类型
export interface UserStats {
  total_works: number
  total_words: number
  completed_works: number
  completion_rate: number
}