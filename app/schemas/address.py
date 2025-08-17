from pydantic import BaseModel, Field, ConfigDict
from typing import List, Annotated

class BaseConfig:

    config = ConfigDict(from_attributes=True)

class BaseAddress(BaseModel):

    id : int
    state : Annotated[str, Field(..., min_length= 3, strict= True)]
    city : Annotated[str, Field(..., min_length= 3, strict= True)]
    neighbourhood: Annotated[str, Field(..., min_length= 3, strict= True)]
    street : Annotated[str, Field(..., min_length= 10, strict= True)]
    place_number = Annotated[int, Field(..., ge=1, strict= True)]
    
    additional_info = Annotated[str, Field(..., strict= True)]

    postal_code = Annotated[int, Field(..., strict= True)]

    owner_id : int
    owner_type = Annotated[str, Field(..., strict= True)]

    class Config(BaseConfig):
        pass

class CreateAddress(BaseModel):

    state : Annotated[str, Field(..., min_length= 3, strict= True)]
    city : Annotated[str, Field(..., min_length= 3, strict= True)]
    neighbourhood: Annotated[str, Field(..., min_length= 3, strict= True)]
    street : Annotated[str, Field(..., min_length= 10, strict= True)]
    place_number = Annotated[int, Field(..., ge=1, strict= True)]
    
    additional_info = Annotated[str, Field(..., strict= True)]

    postal_code = Annotated[int, Field(..., strict= True)]

    owner_id : int
    owner_type = Annotated[str, Field(..., strict= True)]

    class Config(BaseConfig):
        pass

class ReadAddress(BaseModel):

    message : str
    data : BaseAddress

    class Config(BaseConfig):
        pass

class ReadAllAddresses(BaseModel):
    
    message : str
    data : List[BaseAddress] = []

    class Config(BaseConfig):
        pass

class UpdateAddress(CreateAddress):
    pass

class DeleteAddress(BaseAddress):
    pass

class ReadDeletedAddress(BaseModel):

    message : str
    data : DeleteAddress






