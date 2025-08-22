from sqlalchemy import types
from passlib.context import CryptContext

from app.config import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')

SECRET_KEY = settings.security.secret_key
ALGORITHM = settings.security.algorithm

def verify_password(plain_password, hashed_password) -> bool:

    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password) -> str:
    
    return pwd_context.hash(password)

class HashedPassword(types.TypeDecorator):

    impl = types.String
    @classmethod
    def __get_pydantic_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, info):

        if not isinstance(v, str):
            raise TypeError("String required")
        
        hashed_password = get_password_hash(v)

        return hashed_password