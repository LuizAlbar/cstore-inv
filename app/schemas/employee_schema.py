from pydantic import BaseModel, Field, ConfigDict, EmailStr
from datetime import date
from typing import List, Annotated

class BaseConfig:

    config = ConfigDict(from_attributes= True)

class BaseEmployee(BaseModel):

    id : int
    name : Annotated[str, Field(..., min_length= 7)]
    email : Annotated[EmailStr, Field(..., min_length= 8)]  
    password : Annotated[str, Field(..., min_length=8)]
    dateOfBirth : Annotated[date, Field(...)]
    cpf : Annotated[str, Field(..., min_length= 11, max_length=11)]
    role :  Annotated[str, Field(...)]
    store_id : int

    class Config(BaseConfig):
        pass

class CreateEmployee(BaseModel):

    name : Annotated[str, Field(..., min_length= 7)]
    email : Annotated[EmailStr, Field(..., min_length= 8)]  
    password : Annotated[str, Field(..., min_length=8)]
    dateOfBirth : Annotated[date, Field(...)]
    cpf : Annotated[str, Field(..., min_length= 11, max_length=11)]
    role :  Annotated[str, Field(...)]
    store_id : int

    class Config(BaseConfig):
        pass

class ReadEmployee(BaseModel):
    
    message : str
    data : BaseEmployee

    class Config(BaseConfig):
        pass

class ReadAllEmployees(BaseModel):

    message : str
    data : List[BaseEmployee] = []

    class Config(BaseConfig):
        pass

class UpdateEmployee(CreateEmployee):
    pass

class DeleteEmployee(BaseEmployee):
    pass

class ReadDeletedEmployee(BaseModel):

    message : str
    data : DeleteEmployee



