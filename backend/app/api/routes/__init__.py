from .users import router as users_router
from .works import router as works_router
from .inspirations import router as inspirations_router

__all__ = ['users_router', 'works_router', 'inspirations_router']