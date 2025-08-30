from fastapi import APIRouter
from app.api.api_v1.endpoints import works, inspirations, dashboard, profile, settings

api_router = APIRouter()

# 包含各个模块的路由
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(works.router, prefix="/works", tags=["works"])
api_router.include_router(inspirations.router, prefix="/inspirations", tags=["inspirations"])
api_router.include_router(profile.router, prefix="/profile", tags=["profile"])
api_router.include_router(settings.router, prefix="/settings", tags=["settings"])