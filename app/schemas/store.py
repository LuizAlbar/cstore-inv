from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import List, Annotated
from .phone_number import BasePhoneNumber
from .address import BaseAddress

class BaseConfig:
    
    config = ConfigDict(from_attributes = True)
    
class BaseStore(BaseModel):

    id : int
    name: Annotated[str, Field(..., min_length=3, strict=True)]
    cnpj : Annotated[str, Field(..., max_length=14, strict=True)]
    email : Annotated[EmailStr, Field(..., max_length=100, strict=True)]
    phone_numbers : List[BasePhoneNumber] = []
    addresses : List[BaseAddress] = []

    class Config(BaseConfig):
        pass

class CreateStore(BaseModel):

    name: Annotated[str, Field(..., min_length=3, strict=True)]
    cnpj : Annotated[str, Field(..., max_length=14, strict=True)]
    email : Annotated[EmailStr, Field(..., max_length=100, strict=True)]

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



