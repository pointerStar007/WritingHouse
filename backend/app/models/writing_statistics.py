from sqlalchemy import Column, Integer, Date, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.database import Base


class WritingStatistics(Base):
    """写作统计模型"""
    __tablename__ = "writing_statistics"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True, comment="用户ID")
    work_id = Column(Integer, ForeignKey("works.id", ondelete="SET NULL"), nullable=True, index=True, comment="作品ID")
    date = Column(Date, nullable=False, index=True, comment="统计日期")
    word_count = Column(Integer, default=0, comment="当日码字数")
    writing_time = Column(Integer, default=0, comment="写作时长(分钟)")
    chapter_count = Column(Integer, default=0, comment="当日完成章节数")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), comment="创建时间")
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), comment="更新时间")
    
    # 唯一约束
    __table_args__ = (
        UniqueConstraint('user_id', 'work_id', 'date', name='uk_user_work_date'),
    )
    
    # 关联关系
    user = relationship("User", back_populates="writing_statistics")
    work = relationship("Work", back_populates="writing_statistics")
    
    def __repr__(self):
        return f"<WritingStatistics(id={self.id}, user_id={self.user_id}, date={self.date}, word_count={self.word_count})>"