from app.models import Employee
from .crud import Crud
from app.security import get_password_hash

class EmployeeService(Crud):

    model = Employee
    main_field = 'name'
    table_name = model.__name__
    eager_load_fields = []

    @classmethod
    def build_object(cls, create_schema):
        
        obj = super().build_object(create_schema)

        obj.password = get_password_hash(obj.password)

        return obj