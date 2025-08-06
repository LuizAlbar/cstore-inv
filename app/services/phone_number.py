from app.models import PhoneNumber
from app.schemas import UpdatePhoneNumber
from .crud import Crud

class PhoneNumberService(Crud):
    
    model = PhoneNumber
    main_field = 'number'
    table_name = model.__name__
    update_schema = UpdatePhoneNumber