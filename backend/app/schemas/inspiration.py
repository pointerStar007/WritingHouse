from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from ..models.inspiration import InspirationTag

class InspirationBase(BaseModel):
    """灵感基础模式"""
    title: str
    content: str
    tag: InspirationTag

class InspirationCreate(InspirationBase):
    """创建灵感模式"""
    user_id: int

class InspirationUpdate(BaseModel):
    """更新灵感模式"""
    title: Optional[str] = None
    content: Optional[str] = None
    tag: Optional[InspirationTag] = None

class InspirationResponse(InspirationBase):
    """灵感响应模式"""
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True