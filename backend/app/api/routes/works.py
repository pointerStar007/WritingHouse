from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ...database import get_db
from ...models.work import Work, WorkStatus, WorkCategory
from ...schemas.work import WorkCreate, WorkResponse, WorkUpdate

router = APIRouter(prefix="/works", tags=["works"])

@router.post("/", response_model=WorkResponse)
def create_work(work: WorkCreate, db: Session = Depends(get_db)):
    """创建新作品"""
    db_work = Work(
        title=work.title,
        description=work.description,
        content=work.content,
        category=work.category,
        status=work.status or WorkStatus.DRAFT,
        user_id=work.user_id
    )
    db.add(db_work)
    db.commit()
    db.refresh(db_work)
    
    return db_work

@router.get("/", response_model=List[WorkResponse])
def get_works(
    skip: int = 0,
    limit: int = 100,
    user_id: Optional[int] = Query(None, description="按用户ID筛选"),
    category: Optional[WorkCategory] = Query(None, description="按分类筛选"),
    status: Optional[WorkStatus] = Query(None, description="按状态筛选"),
    search: Optional[str] = Query(None, description="搜索关键词"),
    db: Session = Depends(get_db)
):
    """获取作品列表"""
    query = db.query(Work)
    
    # 应用筛选条件
    if user_id:
        query = query.filter(Work.user_id == user_id)
    if category:
        query = query.filter(Work.category == category)
    if status:
        query = query.filter(Work.status == status)
    if search:
        query = query.filter(
            Work.title.contains(search) | Work.description.contains(search)
        )
    
    works = query.offset(skip).limit(limit).all()
    return works

@router.get("/{work_id}", response_model=WorkResponse)
def get_work(work_id: int, db: Session = Depends(get_db)):
    """获取单个作品详情"""
    work = db.query(Work).filter(Work.id == work_id).first()
    if not work:
        raise HTTPException(status_code=404, detail="作品不存在")
    return work

@router.put("/{work_id}", response_model=WorkResponse)
def update_work(work_id: int, work_update: WorkUpdate, db: Session = Depends(get_db)):
    """更新作品信息"""
    work = db.query(Work).filter(Work.id == work_id).first()
    if not work:
        raise HTTPException(status_code=404, detail="作品不存在")
    
    # 更新作品信息
    for field, value in work_update.dict(exclude_unset=True).items():
        setattr(work, field, value)
    
    # 更新字数统计
    if work_update.content is not None:
        work.word_count = len(work_update.content)
    
    db.commit()
    db.refresh(work)
    return work

@router.delete("/{work_id}")
def delete_work(work_id: int, db: Session = Depends(get_db)):
    """删除作品"""
    work = db.query(Work).filter(Work.id == work_id).first()
    if not work:
        raise HTTPException(status_code=404, detail="作品不存在")
    
    db.delete(work)
    db.commit()
    return {"message": "作品删除成功"}

@router.get("/stats/{user_id}")
def get_user_stats(user_id: int, db: Session = Depends(get_db)):
    """获取用户写作统计"""
    works = db.query(Work).filter(Work.user_id == user_id).all()
    
    total_works = len(works)
    total_words = sum(work.word_count for work in works)
    completed_works = len([work for work in works if work.status == WorkStatus.COMPLETED])
    
    return {
        "total_works": total_works,
        "total_words": total_words,
        "completed_works": completed_works,
        "completion_rate": completed_works / total_works if total_works > 0 else 0
    }