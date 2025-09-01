#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据库索引优化脚本
用于创建提升自动保存性能的数据库索引
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text
from app.core.config import settings

def create_performance_indexes():
    """创建性能优化索引"""
    engine = create_engine(settings.DATABASE_URL)
    
    indexes = [
        # 章节版本相关索引
        ("idx_chapter_versions_chapter_created", "CREATE INDEX idx_chapter_versions_chapter_created ON chapter_versions(chapter_id, created_at)"),
        ("idx_chapter_versions_created_at", "CREATE INDEX idx_chapter_versions_created_at ON chapter_versions(created_at)"),
        
        # 字数统计更新相关索引
        ("idx_chapters_work_volume", "CREATE INDEX idx_chapters_work_volume ON chapters(work_id, volume_id)"),
        ("idx_works_user_id", "CREATE INDEX idx_works_user_id ON works(user_id)"),
        ("idx_volumes_work_id", "CREATE INDEX idx_volumes_work_id ON volumes(work_id)"),
        
        # 章节内容更新相关索引
        ("idx_chapters_updated_at", "CREATE INDEX idx_chapters_updated_at ON chapters(updated_at)"),
        ("idx_chapters_status", "CREATE INDEX idx_chapters_status ON chapters(status)"),
        
        # 用户统计相关索引
        ("idx_users_word_count", "CREATE INDEX idx_users_word_count ON users(total_word_count)")
    ]
    
    try:
        with engine.connect() as conn:
            # 先检查现有索引
            existing_indexes = conn.execute(text(
                "SELECT INDEX_NAME FROM INFORMATION_SCHEMA.STATISTICS WHERE TABLE_SCHEMA = 'writing_house'"
            )).fetchall()
            existing_index_names = {row[0] for row in existing_indexes}
            
            for index_name, index_sql in indexes:
                if index_name in existing_index_names:
                    print(f"- 索引已存在: {index_name}")
                    continue
                    
                try:
                    conn.execute(text(index_sql))
                    print(f"✓ 索引创建成功: {index_name}")
                except Exception as e:
                    if "Duplicate key name" in str(e) or "already exists" in str(e):
                        print(f"- 索引已存在: {index_name}")
                    else:
                        print(f"✗ 索引创建失败: {index_name} - {e}")
            
            print("\n数据库索引优化完成！")
            
    except Exception as e:
        print(f"数据库连接失败: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("开始创建性能优化索引...")
    success = create_performance_indexes()
    if success:
        print("索引优化成功完成！")
    else:
        print("索引优化失败！")
        sys.exit(1)