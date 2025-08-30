from sqlalchemy import Column, Integer, String, DateTime, Text, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

Base = declarative_base()

class WorkStatus(enum.Enum):
    """作品状态枚举"""
    DRAFT = "draft"  # 草稿
    WRITING = "writing"  # 进行中
    COMPLETED = "completed"  # 已完成

class WorkCategory(enum.Enum):
    """作品分类枚举"""
    NOVEL = "novel"  # 小说
    ESSAY = "essay"  # 散文
    POETRY = "poetry"  # 诗歌
    NOTE = "note"  # 随笔

class Work(Base):
    """作品模型"""
    __tablename__ = 'works'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    description = Column(Text, nullable=True)
    content = Column(Text, nullable=True)
    category = Column(Enum(WorkCategory), nullable=False)
    status = Column(Enum(WorkStatus), default=WorkStatus.DRAFT)
    word_count = Column(Integer, default=0)
    cover_url = Column(String(255), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 关联关系
    # user = relationship("User", back_populates="works")
    
    def __repr__(self):
        return f"<Work(id={self.id}, title='{self.title}', status='{self.status.value}')>"