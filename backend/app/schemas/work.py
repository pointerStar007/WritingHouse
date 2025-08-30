from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from ..models.work import WorkStatus, WorkCategory

class WorkBase(BaseModel):
    """作品基础模式"""
    title: str
    description: Optional[str] = None
    category: WorkCategory
    cover_url: Optional[str] = None

class WorkCreate(WorkBase):
    """创建作品模式"""
    content: Optional[str] = None
    status: Optional[WorkStatus] = WorkStatus.DRAFT
    user_id: int

class WorkUpdate(BaseModel):
    """更新作品模式"""
    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None
    category: Optional[WorkCategory] = None
    status: Optional[WorkStatus] = None
    cover_url: Optional[str] = None

class WorkResponse(WorkBase):
    """作品响应模式"""
    id: int
    content: Optional[str] = None
    status: WorkStatus
    word_count: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True