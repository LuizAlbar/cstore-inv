from app.models import Store, Employee
from .crud import Crud


class StoreService(Crud):

    model = Store
    main_field = 'name'
    table_name = model.__name__
    eager_load_fields = ['phone_numbers','employees']

    
    def get_all_employee(relationship_id, db, search=""):
        
        relationship = 'store_id'
        entity = Employee
        return Crud.get_all(relationship, entity, relationship_id, db, search)
