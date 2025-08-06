from app.models import PhoneNumber
from app.schemas import CreatePhoneNumber
from .crud import Crud

class PhoneNumberService(Crud):
    
    model = PhoneNumber
    main_field = 'number'
