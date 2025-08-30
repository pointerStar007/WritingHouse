import os
from typing import Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
    """应用配置"""
    
    # 应用基础配置
    app_name: str = "Writing House API"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # 服务器配置
    host: str = "0.0.0.0"
    port: int = 8000
    
    # 数据库配置
    database_url: str = "sqlite:///./writing_house.db"
    
    # JWT配置
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # CORS配置
    allowed_origins: list = ["http://localhost:3000", "http://localhost:5173"]
    
    # 文件上传配置
    upload_dir: str = "uploads"
    max_file_size: int = 10 * 1024 * 1024  # 10MB
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# 创建配置实例
settings = Settings()