from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.database import Base
import enum


class ChapterStatus(str, enum.Enum):
    """章节状态枚举"""
    DRAFT = "draft"  # 草稿
    PUBLISHED = "published"  # 已发布


class Chapter(Base):
    """章节模型"""
    __tablename__ = "chapters"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    work_id = Column(Integer, ForeignKey("works.id", ondelete="CASCADE"), nullable=False, index=True, comment="作品ID")
    volume_id = Column(Integer, ForeignKey("volumes.id", ondelete="SET NULL"), nullable=True, index=True, comment="卷ID")
    title = Column(String(200), nullable=False, comment="章节标题")
    content = Column(Text, comment="章节内容")
    content_markdown = Column(Text, comment="Markdown格式内容")
    word_count = Column(Integer, default=0, comment="字数")
    sort_order = Column(Integer, default=0, index=True, comment="排序序号")
    status = Column(Enum(ChapterStatus), default=ChapterStatus.DRAFT, index=True, comment="章节状态")
    is_free = Column(Boolean, default=True, comment="是否免费")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), comment="创建时间")
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), comment="更新时间")
    published_at = Column(DateTime(timezone=True), nullable=True, comment="发布时间")
    
    # 关联关系
    work = relationship("Work", back_populates="chapters")
    volume = relationship("Volume", back_populates="chapters")
    versions = relationship("ChapterVersion", back_populates="chapter", cascade="all, delete-orphan", order_by="ChapterVersion.version_number.desc()")
    
    def __repr__(self):
        return f"<Chapter(id={self.id}, title='{self.title}', work_id={self.work_id})>"