from pydantic import BaseModel, EmailStr
from typing import List
from app.schemas import PhoneNumberBase

class BaseConfig:
    from_attributes = True
    
class BaseStore(BaseModel):

    id : int
    name : str
    cnpj : str
    email : EmailStr
    phone_numbers = List[PhoneNumberBase]

    class Config(BaseConfig):
        pass

class CreateStore(BaseModel):

    name : str
    cnpj : str
    email : EmailStr

    class Config(BaseConfig):
        pass

class ReadStore(BaseModel):
    
    message : str
    data : BaseStore

    class Config(BaseConfig):
        pass

class ReadAllStores(BaseConfig):
    message: str
    data : List[BaseStore] = []

    class Config(BaseConfig):
        pass

class UpdateStore(CreateStore):
    pass

class DeleteStore(BaseStore):
    pass

class GetDeletedStore(BaseModel):

    message : str
    data : DeleteStore

# Others operations beyond CRUD

class AssignPhoneNumber:

    store_id : int
    phone_id : int

    class Config(BaseConfig):
        pass


