from pydantic import BaseModel, EmailStr, Field
from typing import List, Annotated
from .phone_number import BasePhoneNumber

class BaseConfig:
    from_attributes = True
    
class BaseStore(BaseModel):

    id : int
    name: Annotated[str, Field(..., min_length=3, strict=True)]
    cnpj : str
    email : EmailStr
    phone_numbers : List[BasePhoneNumber] = []

    class Config(BaseConfig):
        pass

class CreateStore(BaseModel):

    name: Annotated[str, Field(..., min_length=3, strict=True)]
    cnpj : str
    email : EmailStr

    class Config(BaseConfig):
        pass

class ReadStore(BaseModel):
    
    message : str
    data : BaseStore

    class Config(BaseConfig):
        pass

class ReadAllStores(BaseModel):
    message: str
    data : List[BaseStore] = []

    class Config(BaseConfig):
        pass

class UpdateStore(CreateStore):
    pass

class DeleteStore(BaseStore):
    pass

class ReadDeletedStore(BaseModel):

    message : str
    data : DeleteStore



