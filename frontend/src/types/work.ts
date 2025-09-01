// 作品相关类型定义

export interface Work {
  id: number
  author_id: number
  title: string
  description?: string
  cover_url?: string
  genre?: string
  tags?: string[]
  status: 'draft' | 'ongoing' | 'completed' | 'paused'
  word_count: number
  chapter_count: number
  is_public: boolean
  created_at: string
  updated_at: string
  author?: {
    id: number
    username: string
    nickname?: string
  }
}

export interface WorkCreateForm {
  title: string
  description?: string
  cover_url?: string
  genre?: string
  tags?: string[]
  is_public?: boolean
}

export interface WorkUpdateForm {
  title?: string
  description?: string
  cover_url?: string
  genre?: string
  tags?: string[]
  status?: 'draft' | 'ongoing' | 'completed' | 'paused'
  is_public?: boolean
}

export interface Volume {
  id: number
  work_id: number
  title: string
  description?: string
  sort_order: number
  word_count: number
  chapter_count: number
  created_at: string
  updated_at: string
}

export interface VolumeCreateForm {
  title: string
  description?: string
  sort_order?: number
}

export interface VolumeUpdateForm {
  title?: string
  description?: string
  sort_order?: number
}

export interface Chapter {
  id: number
  work_id: number
  volume_id?: number
  title: string
  content: string
  markdown_content?: string
  word_count: number
  sort_order: number
  status: 'draft' | 'published'
  is_free: boolean
  created_at: string
  updated_at: string
  published_at?: string
  work?: Work
  volume?: Volume
}

export interface ChapterCreateForm {
  title: string
  content?: string
  markdown_content?: string
  volume_id?: number
  sort_order?: number
  status?: 'draft' | 'published'
  is_free?: boolean
}

export interface ChapterUpdateForm {
  title?: string
  content?: string
  markdown_content?: string
  volume_id?: number
  sort_order?: number
  status?: 'draft' | 'published'
  is_free?: boolean
}

export interface ChapterVersion {
  id: number
  chapter_id: number
  version_number: number
  title: string
  content: string
  markdown_content?: string
  word_count: number
  created_at: string
  chapter?: Chapter
}

export interface WorkFavorite {
  id: number
  user_id: number
  work_id: number
  created_at: string
  work?: Work
}

export interface WorkQuery {
  page?: number
  size?: number
  search?: string
  genre?: string
  status?: string
  is_public?: boolean
  author_id?: number
  sort_by?: 'created_at' | 'updated_at' | 'word_count' | 'chapter_count'
  sort_order?: 'asc' | 'desc'
}

export interface ChapterQuery {
  page?: number
  size?: number
  work_id?: number
  volume_id?: number
  status?: 'draft' | 'published'
  sort_by?: 'sort_order' | 'created_at' | 'updated_at'
  sort_order?: 'asc' | 'desc'
}

// 导出选项
export interface ExportOptions {
  format: 'docx' | 'pdf' | 'txt' | 'markdown'
  include_chapters?: number[]
  include_volumes?: number[]
  include_metadata?: boolean
}