from sqlalchemy import Column, Integer, String, DateTime, Text, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

Base = declarative_base()

class InspirationTag(enum.Enum):
    """灵感标签枚举"""
    CHARACTER = "character"  # 人物
    PLOT = "plot"  # 情节
    SCENE = "scene"  # 场景
    DIALOGUE = "dialogue"  # 对话

class Inspiration(Base):
    """灵感模型"""
    __tablename__ = 'inspirations'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    content = Column(Text, nullable=False)
    tag = Column(Enum(InspirationTag), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 关联关系
    # user = relationship("User", back_populates="inspirations")
    
    def __repr__(self):
        return f"<Inspiration(id={self.id}, title='{self.title}', tag='{self.tag.value}')>"