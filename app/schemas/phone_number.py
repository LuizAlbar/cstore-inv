from pydantic import BaseModel
from typing import List

class BaseConfig:
    from_attributes = True

class BasePhoneNumber(BaseModel):

    id : int
    cc : int
    ac : int
    number : int

    class Config(BaseConfig):
        pass

class CreatePhoneNumber(BaseModel):

    cc : int
    ac : int
    number : int

    class Config(BaseConfig):
        pass

class ReadPhoneNumber(BaseModel):

    message : str
    data : BasePhoneNumber

    class Config(BaseConfig):
        pass

class ReadAllPhoneNumber(BaseModel):

    message : str
    data : List[BasePhoneNumber] = []

    class Config(BaseConfig):
        pass

class UpdatePhoneNumber(CreatePhoneNumber):
    pass

class DeletePhoneNumber(BasePhoneNumber):
    pass

class GetDeletedPhoneNumber(BaseModel):

    message : str
    data =  DeletePhoneNumber

    