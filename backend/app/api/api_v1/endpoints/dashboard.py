from fastapi import APIRouter
from typing import Dict, Any

router = APIRouter()

@router.get("/stats")
async def get_dashboard_stats() -> Dict[str, Any]:
    """获取仪表盘统计数据"""
    return {
        "total_works": 12,
        "total_words": 156789,
        "total_inspirations": 45,
        "writing_days": 89,
        "recent_activity": [
            {
                "id": 1,
                "type": "work",
                "title": "完成了《星空下的故事》第三章",
                "time": "2024-01-15 14:30"
            },
            {
                "id": 2,
                "type": "inspiration",
                "title": "记录了一个关于时间旅行的灵感",
                "time": "2024-01-15 10:15"
            }
        ],
        "writing_progress": {
            "daily_goal": 2000,
            "today_words": 1250,
            "weekly_goal": 14000,
            "week_words": 8750
        }
    }

@router.get("/charts/writing-trend")
async def get_writing_trend() -> Dict[str, Any]:
    """获取写作趋势图表数据"""
    return {
        "dates": ["1月1日", "1月2日", "1月3日", "1月4日", "1月5日", "1月6日", "1月7日"],
        "words": [1200, 1800, 1500, 2200, 1900, 2100, 1600],
        "goal": 2000
    }