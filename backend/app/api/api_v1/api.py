from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, users, works, volumes, chapters, statistics, user_profile, upload

api_router = APIRouter()

# 认证相关路由
api_router.include_router(auth.router, prefix="/auth", tags=["认证"])

# 用户相关路由
api_router.include_router(users.router, prefix="/users", tags=["用户管理"])

# 作品相关路由
api_router.include_router(works.router, prefix="/works", tags=["作品管理"])

# 卷相关路由
api_router.include_router(volumes.router, prefix="/volumes", tags=["卷管理"])

# 章节相关路由
api_router.include_router(chapters.router, prefix="/chapters", tags=["章节管理"])

# 统计相关路由
api_router.include_router(statistics.router, prefix="/statistics", tags=["写作统计"])

# 用户资料相关路由
api_router.include_router(user_profile.router, prefix="/user-profile", tags=["用户资料"])

# 上传相关路由
api_router.include_router(upload.router, prefix="/upload", tags=["文件上传"])


@api_router.get("/")
async def api_info():
    """API信息"""
    return {
        "message": "WritingHouse API v1",
        "version": "2.0.0",
        "endpoints": {
            "auth": "/auth",
            "users": "/users",
            "works": "/works",
            "volumes": "/volumes",
            "chapters": "/chapters",
            "statistics": "/statistics",
            "user_profile": "/user-profile",
            "upload": "/upload"
        }
    }


@api_router.get("/health")
async def health_check():
    """健康检查"""
    return {
        "status": "healthy",
        "service": "WritingHouse API",
        "version": "2.0.0"
    }