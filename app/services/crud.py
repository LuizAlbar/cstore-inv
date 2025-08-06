from sqlalchemy.orm import Session
from abc import ABC
from app.utils import ResponseHandler  # Importe o handler

class Crud(ABC):
    model = None
    main_field = ''

    @classmethod
    def create(cls, db: Session, schema):
        obj = cls.model(**schema.model_dump())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        
        return ResponseHandler.create_success(
            getattr(obj, cls.main_field, ""), 
            obj.id,
            obj
        )