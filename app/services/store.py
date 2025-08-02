from sqlalchemy.orm import Session
from app.models import Store
from app.schemas import CreateStore, UpdateStore
from app.utils import ResponseHandler

#Only create and delete functions for the first test step
class StoreService:

    @staticmethod
    def create_store(db: Session, store: CreateStore):

        db_store = Store(id = None, **store.model_dump())
        db.add(db_store)
        db.commit()
        db.refresh(db_store)

        return ResponseHandler.create_success(db_store.name, db_store.id, db_store)
    
    @staticmethod
    def read_store(db: Session, store_id: int):

        db_store = db.query(Store).filter(Store.id == store_id).first()
        return ResponseHandler.get_single_success(db_store.name, db_store.id, db_store)

    @staticmethod
    def delete_store(db: Session, store_id: int):
        
        db_store = db.query(Store).filter(Store.id == store_id).first()

        if not db_store:
            return ResponseHandler.not_found_error('Store', store_id)
        
        db.delete(db_store)
        db.commit()

        return ResponseHandler.delete_success(db_store.name, db_store.id, db_store)
    