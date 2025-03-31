from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.object_service import ObjectService
from app.repositories.object_repository import ObjectRepository
from app.database import get_db

router = APIRouter()

@router.get("/sysobjects")
def read_objects(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    object_repository = ObjectRepository(db)
    object_service = ObjectService(object_repository)
    return object_service.get_objects(limit, offset)