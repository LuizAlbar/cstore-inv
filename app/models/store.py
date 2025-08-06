from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from typing import List, TYPE_CHECKING
from app.database import Base

if TYPE_CHECKING:
    from app.models import PhoneNumber

class Store(Base):
    
    __tablename__ = 'stores'

    id = Column(Integer, primary_key= True, unique= True, index= True, nullable= False, autoincrement= True)
    name = Column(String(50), unique= True, nullable = False)
    cnpj = Column(String(14), unique= True, nullable= False)
    email = Column(String(100), unique= True, nullable= False)

    phone_numbers = relationship('PhoneNumber', back_populates= 'store', cascade= 'all, delete-orphan', passive_deletes= True)
    
    