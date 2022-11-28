from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.utils import get_db
from . import service
from .schemas import PostCreate

router = APIRouter()


@router.get("/")
def post_list(db: Session = Depends(get_db)):
	result = service.get_post_list(db)
	return result\


@router.post("/")
def post_create(item: PostCreate, db: Session = Depends(get_db)):
	result = service.create_post(db, item)
	return result.id, 200