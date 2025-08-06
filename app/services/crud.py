from sqlalchemy.orm import Session, selectinload
from abc import ABC
from app.utils import ResponseHandler

class Crud(ABC):
    model = None
    main_field = ''
    table_name = ''
    eager_load_fields = []  

    @classmethod
    def create(cls, db: Session, create_schema):
        obj = cls.model(**create_schema.model_dump())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        
        return ResponseHandler.create_success(
            getattr(obj, cls.main_field, ""), 
            obj.id,
            obj
        )

    @classmethod
    def read(cls, db: Session, id: int):
        obj = db.query(cls.model).filter(cls.model.id == id).first()

        if not obj:
            return ResponseHandler.not_found_error(cls.table_name, id)
        
        return ResponseHandler.get_single_success(
            getattr(obj, cls.main_field, ""),
            obj.id,
            obj
        )

    @classmethod
    def read_all(cls, db: Session, search = ""):
        objs = db.query(cls.model).order_by(cls.model.id.asc()).all()

        if not objs:
            return ResponseHandler.db_not_populated_error(cls.table_name)

        return ResponseHandler.get_all_success(cls.model.__name__, objs)

    @classmethod
    def update(cls, db: Session, id: int, update_schema):
        obj = db.query(cls.model).filter(cls.model.id == id).first()

        if not obj:
            return ResponseHandler.not_found_error(cls.table_name, id)
        
        for key, value in update_schema.model_dump().items():
            setattr(obj, key, value)

        db.commit()
        db.refresh(obj)

        return ResponseHandler.update_success(getattr(obj, cls.main_field, ""), obj.id, obj)

    @classmethod
    def delete(cls, db: Session, id: int):
        query = db.query(cls.model)

        for field in cls.eager_load_fields:
            query = query.options(selectinload(getattr(cls.model, field)))

        obj = query.filter(cls.model.id == id).first()

        if not obj:
            return ResponseHandler.not_found_error(cls.table_name, id)

        db.delete(obj)
        db.commit()

        return ResponseHandler.delete_success(getattr(obj, cls.main_field, ""), obj.id, obj)
