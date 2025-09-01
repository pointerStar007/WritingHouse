from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.db.session import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.Work])
def read_works(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    search: Optional[str] = Query(None, description="搜索关键词"),
    status: Optional[str] = Query(None, description="作品状态"),
    work_type: Optional[str] = Query(None, description="作品类型"),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve works for current user.
    """
    works = crud.work.get_multi_by_owner(
        db=db, 
        owner_id=current_user.id, 
        skip=skip, 
        limit=limit,
        search=search,
        status=status,
        work_type=work_type
    )
    return works


@router.post("/", response_model=schemas.Work)
def create_work(
    *,
    db: Session = Depends(get_db),
    work_in: schemas.WorkCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new work.
    """
    work_in_data = work_in.dict()
    work_in_data["user_id"] = current_user.id
    work = crud.work.create(db=db, obj_in=schemas.WorkCreate(**work_in_data))
    return work