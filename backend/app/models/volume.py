from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.database import Base


class Volume(Base):
    """卷模型"""
    __tablename__ = "volumes"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    work_id = Column(Integer, ForeignKey("works.id", ondelete="CASCADE"), nullable=False, index=True, comment="作品ID")
    title = Column(String(200), nullable=False, comment="卷标题")
    description = Column(Text, comment="卷简介")
    sort_order = Column(Integer, default=0, index=True, comment="排序序号")
    word_count = Column(Integer, default=0, comment="卷字数")
    chapter_count = Column(Integer, default=0, comment="章节数")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), comment="创建时间")
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), comment="更新时间")
    
    # 关联关系
    work = relationship("Work", back_populates="volumes")
    chapters = relationship("Chapter", back_populates="volume", cascade="all, delete-orphan", order_by="Chapter.sort_order")
    
    def __repr__(self):
        return f"<Volume(id={self.id}, title='{self.title}', work_id={self.work_id})>"