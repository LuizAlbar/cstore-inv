from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING
from app.database import Base

if TYPE_CHECKING:
    from app.models import Store

class PhoneNumber(Base):

    __tablename__ = 'phone_numbers'

    id = Column(Integer, primary_key= True, unique= True, nullable= False, autoincrement= True)
    #Country Code
    cc =  Column(Integer, nullable= False)
    #Area Code
    ac = Column(Integer, nullable= False)
    number = Column(Integer, nullable= False)

    store_id = Column(Integer, ForeignKey('stores.id', ondelete="CASCADE"), nullable= False)

    store = relationship('Store', back_populates='phone_numbers')