from app.models import Store
from .crud import Crud

class StoreService(Crud):

    model = Store
    main_field = 'name'
    table_name = model.__name__
    eager_load_fields = ['phone_numbers']