from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from typing import List, TYPE_CHECKING
from app.database import Base

class Product(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key= True, unique = True, nullable = False, autoincrement= True)
    name = Column(String(100), nullable= False)
    quantity = Column(Integer)
    price = Column(Integer)
    unit = Column(String)

