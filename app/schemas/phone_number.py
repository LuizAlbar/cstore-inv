from pydantic import BaseModel
from typing import List

class BasePhoneNumber(BaseModel):

    id : int
    cc : int
    ac : int
    number : int
    store_id : int

    model_config = {
        "from_attributes": True
    }

class CreatePhoneNumber(BaseModel):

    cc : int
    ac : int
    number : int
    store_id : int

    model_config = {
        "from_attributes": True
    }

class ReadPhoneNumber(BaseModel):

    message : str
    data : BasePhoneNumber

    model_config = {
        "from_attributes": True
    }

class ReadAllPhoneNumber(BaseModel):

    message : str
    data : List[BasePhoneNumber] = []

    model_config = {
        "from_attributes": True
    }

class UpdatePhoneNumber(CreatePhoneNumber):
    pass

class DeletePhoneNumber(BasePhoneNumber):
    pass

class ReadDeletedPhoneNumber(BaseModel):

    message : str
    data : DeletePhoneNumber

    