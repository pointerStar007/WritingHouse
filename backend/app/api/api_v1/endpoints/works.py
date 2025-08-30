from fastapi import APIRouter
from typing import List, Dict, Any

router = APIRouter()

@router.get("/")
async def get_works() -> List[Dict[str, Any]]:
    """获取作品列表"""
    return [
        {
            "id": 1,
            "title": "星空下的故事",
            "description": "一个关于梦想与现实的温暖故事",
            "status": "进行中",
            "word_count": 25000,
            "target_words": 80000,
            "tags": ["小说", "青春", "励志"],
            "created_at": "2024-01-01",
            "updated_at": "2024-01-15",
            "cover": "/images/covers/story1.jpg"
        },
        {
            "id": 2,
            "title": "时间的旅行者",
            "description": "科幻题材的短篇小说集",
            "status": "草稿",
            "word_count": 8500,
            "target_words": 30000,
            "tags": ["科幻", "短篇", "时间"],
            "created_at": "2024-01-10",
            "updated_at": "2024-01-14",
            "cover": "/images/covers/story2.jpg"
        }
    ]

@router.get("/{work_id}")
async def get_work(work_id: int) -> Dict[str, Any]:
    """获取单个作品详情"""
    return {
        "id": work_id,
        "title": "星空下的故事",
        "description": "一个关于梦想与现实的温暖故事",
        "content": "这里是作品的正文内容...",
        "status": "进行中",
        "word_count": 25000,
        "target_words": 80000,
        "tags": ["小说", "青春", "励志"],
        "chapters": [
            {"id": 1, "title": "第一章：初遇", "word_count": 3200},
            {"id": 2, "title": "第二章：相识", "word_count": 2800},
            {"id": 3, "title": "第三章：成长", "word_count": 3500}
        ],
        "created_at": "2024-01-01",
        "updated_at": "2024-01-15"
    }