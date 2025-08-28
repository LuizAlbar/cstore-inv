from app.models import PhoneNumber, Store
from .crud import Crud, Session, ResponseHandler
from app.utils import PhoneNumberHandler

class PhoneNumberService(Crud):
    
    model = PhoneNumber
    main_field = 'number'
    table_name = model.__name__

    @classmethod
    def create(cls, db: Session, create_schema):

        store = db.query(Store).filter(Store.id == create_schema.store_id).first()

        if not store:
            return ResponseHandler.not_found_error('Store', create_schema.store_id)
        
        if len(store.phone_numbers) >=2:
            return PhoneNumberHandler.phone_numbers_limit_exceeded(Store.__name__, store.name, store.id)

        return super().create(db, create_schema)
    
    