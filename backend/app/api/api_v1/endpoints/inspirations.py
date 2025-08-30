from fastapi import APIRouter
from typing import List, Dict, Any

router = APIRouter()

@router.get("/")
async def get_inspirations() -> List[Dict[str, Any]]:
    """获取灵感列表"""
    return [
        {
            "id": 1,
            "title": "关于时间的思考",
            "content": "如果时间可以倒流，我们会做出不同的选择吗？",
            "tags": ["哲学", "时间", "选择"],
            "category": "思考",
            "created_at": "2024-01-15 10:30",
            "is_used": False
        },
        {
            "id": 2,
            "title": "雨夜的咖啡店",
            "content": "雨夜，一个人坐在咖啡店里，看着窗外的行人匆匆而过...",
            "tags": ["场景", "雨夜", "咖啡店"],
            "category": "场景",
            "created_at": "2024-01-14 20:15",
            "is_used": True
        },
        {
            "id": 3,
            "title": "神秘的图书馆",
            "content": "在城市的角落里，有一座只在午夜开放的图书馆...",
            "tags": ["奇幻", "图书馆", "神秘"],
            "category": "设定",
            "created_at": "2024-01-13 15:45",
            "is_used": False
        }
    ]

@router.get("/categories")
async def get_inspiration_categories() -> List[str]:
    """获取灵感分类"""
    return ["思考", "场景", "设定", "人物", "对话", "情节"]