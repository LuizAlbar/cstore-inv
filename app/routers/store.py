from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import CreateStore, ReadStore
from app.services import StoreService

router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED, response_model= CreateStore)
async def create_store(
    store: CreateStore,
    db: Session = Depends(get_db)):

    return StoreService.create_store(db, store)

@router.get('/{store_id}', status_code= status.HTTP_200_OK, response_model= ReadStore)
async def read_store(store_id : int, db: Session = Depends(get_db)):
    
    return StoreService.read_store(db, store_id)