from fastapi import APIRouter, status, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import CreateStore, ReadStore, ReadAllStores, UpdateStore, ReadDeletedStore
from app.services import StoreService

router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED, response_model= ReadStore)
async def create_store(
    store: CreateStore,
    db: Session = Depends(get_db)):

    return StoreService.create(db, store)

@router.get('/{store_id}', status_code= status.HTTP_200_OK, response_model= ReadStore)
async def read_store(store_id : int, db: Session = Depends(get_db)):
    
    return StoreService.read(db, store_id)

@router.get('/', status_code= status.HTTP_200_OK, response_model= ReadAllStores)
async def read_all_stores(search : str | None = Query("", description= ""), db: Session = Depends(get_db)):
    
    return StoreService.read_all(db, search)

@router.put('/{store_id}', status_code = status.HTTP_200_OK, response_model= ReadStore)
async def update_store(store_id : int, updated_store : UpdateStore, db: Session = Depends(get_db)):

    return StoreService.update(db, store_id, updated_store)

@router.delete('/{store_id}', status_code= status.HTTP_200_OK, response_model= ReadDeletedStore)
async def delete_store(store_id: int, db: Session = Depends(get_db)):

    return StoreService.delete(db, store_id)

