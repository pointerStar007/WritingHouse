from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core import security
from app.core.config import settings
from app.db.session import get_db

router = APIRouter()


@router.post("/login", response_model=schemas.Token)
def login_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.user.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    elif not crud.user.is_active(user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        user.id, expires_delta=access_token_expires
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user
    }


@router.post("/register", response_model=schemas.User)
def register(
    *,
    db: Session = Depends(get_db),
    user_in: schemas.UserCreate,
) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.get_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    return user


@router.post("/test-token", response_model=schemas.User)
def test_token(current_user: models.User = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    return current_user


@router.post("/logout")
def logout(
    current_user: models.User = Depends(deps.get_current_user)
) -> Any:
    """
    Logout user
    """
    # 在实际应用中，这里可以将token加入黑名单
    # 目前只是返回成功消息
    return {"message": "Successfully logged out"}


@router.post("/refresh", response_model=schemas.Token)
def refresh_token(
    current_user: models.User = Depends(deps.get_current_user)
) -> Any:
    """
    Refresh access token
    """
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        current_user.id, expires_delta=access_token_expires
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": current_user
    }


@router.get("/verify", response_model=schemas.User)
def verify_token(
    current_user: models.User = Depends(deps.get_current_user)
) -> Any:
    """
    Verify access token
    """
    return current_user


@router.post("/forgot-password")
def forgot_password(
    email: str,
    db: Session = Depends(get_db)
) -> Any:
    """
    Password recovery
    """
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this email does not exist in the system.",
        )
    # TODO: 实现发送重置密码邮件的逻辑
    return {"message": "Password recovery email sent"}


@router.post("/reset-password")
def reset_password(
    token: str,
    new_password: str,
    db: Session = Depends(get_db)
) -> Any:
    """
    Reset password
    """
    # TODO: 实现重置密码的逻辑
    return {"message": "Password has been reset"}


@router.post("/send-verification")
def send_verification_email(
    current_user: models.User = Depends(deps.get_current_user)
) -> Any:
    """
    Send verification email
    """
    # TODO: 实现发送验证邮件的逻辑
    return {"message": "Verification email sent"}


@router.post("/verify-email")
def verify_email(
    token: str,
    db: Session = Depends(get_db)
) -> Any:
    """
    Verify email
    """
    # TODO: 实现邮箱验证的逻辑
    return {"message": "Email verified successfully"}


@router.get("/check-username/{username}")
def check_username(
    username: str,
    db: Session = Depends(get_db)
) -> Any:
    """
    Check if username is available
    """
    user = crud.user.get_by_username(db, username=username)
    return {"available": user is None}


@router.get("/check-email/{email}")
def check_email(
    email: str,
    db: Session = Depends(get_db)
) -> Any:
    """
    Check if email is available
    """
    user = crud.user.get_by_email(db, email=email)
    return {"available": user is None}