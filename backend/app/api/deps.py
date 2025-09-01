from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.core.security import verify_token
from app.db.database import get_db
from app.models.user import User
from app.crud.crud_user import user
from app.core.exceptions import (
    AuthenticationError,
    AuthorizationError,
    ResourceNotFoundError
)

security = HTTPBearer()


def get_current_user(
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> User:
    """获取当前用户"""
    token = credentials.credentials
    user_id = verify_token(token)
    
    if user_id is None:
        raise AuthenticationError(
            message="无效的认证凭据",
            details={"headers": {"WWW-Authenticate": "Bearer"}}
        )
    
    current_user = user.get(db, id=int(user_id))
    if not current_user:
        raise ResourceNotFoundError(
            message="用户不存在"
        )
    
    if not current_user.is_active:
        raise AuthorizationError(
            message="用户已被禁用"
        )
    
    return current_user


def get_current_active_superuser(
    current_user: User = Depends(get_current_user),
) -> User:
    """获取当前活跃的超级用户"""
    if not current_user.is_superuser:
        raise AuthorizationError(
            message="用户权限不足"
        )
    return current_user


def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """获取当前活跃用户"""
    if not current_user.is_active:
        raise AuthorizationError(
            message="用户已被禁用"
        )
    return current_user


def get_optional_current_user(
    db: Session = Depends(get_db),
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)
) -> Optional[User]:
    """获取可选的当前用户（用于可选认证的接口）"""
    if not credentials:
        return None
    
    token = credentials.credentials
    user_id = verify_token(token)
    
    if user_id is None:
        return None
    
    current_user = user.get(db, id=int(user_id))
    if not current_user or not current_user.is_active:
        return None
    
    return current_user