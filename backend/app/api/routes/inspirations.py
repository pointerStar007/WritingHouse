from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ...database import get_db
from ...models.inspiration import Inspiration, InspirationTag
from ...schemas.inspiration import InspirationCreate, InspirationResponse, InspirationUpdate

router = APIRouter(prefix="/inspirations", tags=["inspirations"])

@router.post("/", response_model=InspirationResponse)
def create_inspiration(inspiration: InspirationCreate, db: Session = Depends(get_db)):
    """创建新灵感"""
    db_inspiration = Inspiration(
        title=inspiration.title,
        content=inspiration.content,
        tag=inspiration.tag,
        user_id=inspiration.user_id
    )
    db.add(db_inspiration)
    db.commit()
    db.refresh(db_inspiration)
    
    return db_inspiration

@router.get("/", response_model=List[InspirationResponse])
def get_inspirations(
    skip: int = 0,
    limit: int = 100,
    user_id: Optional[int] = Query(None, description="按用户ID筛选"),
    tag: Optional[InspirationTag] = Query(None, description="按标签筛选"),
    search: Optional[str] = Query(None, description="搜索关键词"),
    db: Session = Depends(get_db)
):
    """获取灵感列表"""
    query = db.query(Inspiration)
    
    # 应用筛选条件
    if user_id:
        query = query.filter(Inspiration.user_id == user_id)
    if tag:
        query = query.filter(Inspiration.tag == tag)
    if search:
        query = query.filter(
            Inspiration.title.contains(search) | Inspiration.content.contains(search)
        )
    
    inspirations = query.offset(skip).limit(limit).all()
    return inspirations

@router.get("/{inspiration_id}", response_model=InspirationResponse)
def get_inspiration(inspiration_id: int, db: Session = Depends(get_db)):
    """获取单个灵感详情"""
    inspiration = db.query(Inspiration).filter(Inspiration.id == inspiration_id).first()
    if not inspiration:
        raise HTTPException(status_code=404, detail="灵感不存在")
    return inspiration

@router.put("/{inspiration_id}", response_model=InspirationResponse)
def update_inspiration(inspiration_id: int, inspiration_update: InspirationUpdate, db: Session = Depends(get_db)):
    """更新灵感信息"""
    inspiration = db.query(Inspiration).filter(Inspiration.id == inspiration_id).first()
    if not inspiration:
        raise HTTPException(status_code=404, detail="灵感不存在")
    
    # 更新灵感信息
    for field, value in inspiration_update.dict(exclude_unset=True).items():
        setattr(inspiration, field, value)
    
    db.commit()
    db.refresh(inspiration)
    return inspiration

@router.delete("/{inspiration_id}")
def delete_inspiration(inspiration_id: int, db: Session = Depends(get_db)):
    """删除灵感"""
    inspiration = db.query(Inspiration).filter(Inspiration.id == inspiration_id).first()
    if not inspiration:
        raise HTTPException(status_code=404, detail="灵感不存在")
    
    db.delete(inspiration)
    db.commit()
    return {"message": "灵感删除成功"}

@router.post("/{inspiration_id}/convert-to-work")
def convert_to_work(inspiration_id: int, db: Session = Depends(get_db)):
    """将灵感转换为作品"""
    inspiration = db.query(Inspiration).filter(Inspiration.id == inspiration_id).first()
    if not inspiration:
        raise HTTPException(status_code=404, detail="灵感不存在")
    
    # 这里可以实现将灵感转换为作品的逻辑
    # 例如创建一个新的作品，内容基于灵感
    
    return {"message": "灵感已转换为作品", "inspiration_id": inspiration_id}