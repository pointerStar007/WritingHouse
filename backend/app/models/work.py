from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Enum, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.database import Base
import enum


class WorkStatus(str, enum.Enum):
    """作品状态枚举"""
    DRAFT = "DRAFT"  # 草稿
    ONGOING = "ONGOING"  # 连载中
    COMPLETED = "COMPLETED"  # 已完结
    PAUSED = "PAUSED"  # 暂停


class Work(Base):
    """作品模型"""
    __tablename__ = "works"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True, comment="作者ID")
    title = Column(String(200), nullable=False, comment="作品标题")
    description = Column(Text, comment="作品简介")
    cover_url = Column(String(255), comment="封面图片URL")
    genre = Column(String(50), comment="作品类型")
    tags = Column(JSON, comment="标签数组")
    status = Column(Enum(WorkStatus), default=WorkStatus.DRAFT, index=True, comment="作品状态")
    word_count = Column(Integer, default=0, comment="总字数")
    chapter_count = Column(Integer, default=0, comment="章节数")
    is_public = Column(Boolean, default=False, comment="是否公开")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True, comment="创建时间")
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), comment="更新时间")
    
    # 关联关系
    author = relationship("User", back_populates="works")
    volumes = relationship("Volume", back_populates="work", cascade="all, delete-orphan", order_by="Volume.sort_order")
    chapters = relationship("Chapter", back_populates="work", cascade="all, delete-orphan", order_by="Chapter.sort_order")
    writing_statistics = relationship("WritingStatistics", back_populates="work", cascade="all, delete-orphan")
    favorites = relationship("WorkFavorite", back_populates="work", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Work(id={self.id}, title='{self.title}', status='{self.status}')>"