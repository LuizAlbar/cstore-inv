from pydantic import BaseModel, Field
from typing import List, Annotated

class BasePhoneNumber(BaseModel):

    id : int
    cc : Annotated[int, Field(..., ge= 1, le= 99999, strict= True)]
    ac : Annotated[int, Field(..., ge= 1, le= 99999, strict= True)]
    number : Annotated[int, Field(..., ge= 1, le= 999999999999, strict= True)]
    store_id : int

    model_config = {
        "from_attributes": True
    }

class CreatePhoneNumber(BaseModel):

    cc : Annotated[int, Field(..., ge= 1, le= 99999, strict= True)]
    ac : Annotated[int, Field(..., ge= 1, le= 99999, strict= True)]
    number : Annotated[int, Field(..., ge= 1, le= 999999999999, strict= True)]
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

    