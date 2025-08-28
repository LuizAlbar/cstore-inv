from pydantic import BaseModel, Field, ConfigDict
from typing import List, Annotated

class BaseConfig:

    config = ConfigDict(from_attributes=True)

class BaseProduct(BaseModel):

    id : int
    name : Annotated[str, Field(..., min_length=1, max_length=100, strict=True)]
    quantity : Annotated[int, Field(..., ge=0)]
    price : Annotated[int, Field(..., ge=1)]
    unit : Annotated[str, Field(...)]

    class Config(BaseConfig):
        pass

class CreateProduct(BaseModel):

    name : Annotated[str, Field(..., min_length=1, max_length=100, strict=True)]
    quantity : Annotated[int, Field(..., ge=0)]
    price : Annotated[int, Field(..., ge=1)]
    unit : Annotated[str, Field(...)]

    class Config(BaseConfig):
        pass

class ReadProduct(BaseModel):

    message : str
    data : BaseProduct

    class Config(BaseConfig):
        pass

class ReadAllProducts(BaseModel):

    message : str
    data : List[BaseProduct] = []

    class Config(BaseConfig):
        pass

class UpdateProduct(CreateProduct):
    pass

class DeleteProduct(BaseProduct):
    pass

class ReadDeletedProduct(BaseModel):

    message : str
    data : DeleteProduct

