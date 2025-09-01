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
def root():
    """
    API根路径
    """
    return {
        "message": "Writing House API",
        "version": "1.0.0",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }


@api_router.get("/health")
def health_check():
    """
    健康检查接口
    """
    return {
        "status": "ok",
        "message": "API is running"
    }