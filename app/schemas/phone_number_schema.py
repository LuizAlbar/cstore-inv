from pydantic import BaseModel, Field, ConfigDict
from typing import List, Annotated

class BaseConfig:

    config = ConfigDict(from_attributes= True)

class BasePhoneNumber(BaseModel):

    id : int
    cc : Annotated[int, Field(..., ge= 1, le= 99999, strict= True)]
    ac : Annotated[int, Field(..., ge= 1, le= 99999, strict= True)]
    number : Annotated[int, Field(..., ge= 1, le= 999999999999, strict= True)]
    store_id : int

    class Config(BaseConfig):
        pass

class CreatePhoneNumber(BaseModel):

    cc : Annotated[int, Field(..., ge= 1, le= 99999, strict= True)]
    ac : Annotated[int, Field(..., ge= 1, le= 99999, strict= True)]
    number : Annotated[int, Field(..., ge= 1, le= 999999999999, strict= True)]
    store_id : int

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

class ReadDeletedPhoneNumber(BaseModel):

    message : str
    data : DeletePhoneNumber

    