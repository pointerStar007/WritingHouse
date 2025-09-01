from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.db.session import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.Chapter])
def read_chapters(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    work_id: Optional[int] = Query(None, description="作品ID"),
    volume_id: Optional[int] = Query(None, description="卷ID"),
    search: Optional[str] = Query(None, description="搜索关键词"),
    status: Optional[str] = Query(None, description="章节状态"),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve chapters.
    """
    # 验证用户权限
    if work_id:
        work = crud.work.get(db=db, id=work_id)
        if not work or not crud.work.is_owner(work, current_user):
            raise HTTPException(status_code=400, detail="Not enough permissions")
    
    if volume_id:
        volume = crud.volume.get(db=db, id=volume_id)
        if not volume:
            raise HTTPException(status_code=404, detail="Volume not found")
        work = crud.work.get(db=db, id=volume.work_id)
        if not work or not crud.work.is_owner(work, current_user):
            raise HTTPException(status_code=400, detail="Not enough permissions")
    
    chapters = crud.chapter.get_multi_by_filters(
        db=db,
        skip=skip,
        limit=limit,
        work_id=work_id,
        volume_id=volume_id,
        search=search,
        status=status
    )
    return chapters


@router.post("/", response_model=schemas.Chapter)
def create_chapter(
    *,
    db: Session = Depends(get_db),
    chapter_in: schemas.ChapterCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new chapter.
    """
    # 验证用户权限
    if chapter_in.work_id:
        work = crud.work.get(db=db, id=chapter_in.work_id)
        if not work or not crud.work.is_owner(work, current_user):
            raise HTTPException(status_code=400, detail="Not enough permissions")
    
    if chapter_in.volume_id:
        volume = crud.volume.get(db=db, id=chapter_in.volume_id)
        if not volume:
            raise HTTPException(status_code=404, detail="Volume not found")
        work = crud.work.get(db=db, id=volume.work_id)
        if not work or not crud.work.is_owner(work, current_user):
            raise HTTPException(status_code=400, detail="Not enough permissions")
    
    chapter = crud.chapter.create(db=db, obj_in=chapter_in)
    return chapter