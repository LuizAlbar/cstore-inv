from app.models import Address
from .crud import Crud, ResponseHandler
import importlib

models = importlib.import_module('app.models')

class AddressService(Crud):

    model = Address
    main_field = 'postal_code'
    table_name = model.__name__
    

    @classmethod
    def create(cls, db, create_schema):

        model = create_schema.owner_type
        Model = getattr(models, model)

        owner = db.query(Model).filter(Model.id == create_schema.owner_id).first()

        if not owner:
            return ResponseHandler.not_found_error(Model.__name__, create_schema.owner_id)

        return super().create(db, create_schema)