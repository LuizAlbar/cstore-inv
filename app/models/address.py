from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext import associationproxy
from typing import TYPE_CHECKING
from app.database import Base

if TYPE_CHECKING:
    from app.models import Store

class Address(Base):

    __tablename__ = "addresses"

    id = Column(Integer, primary_key= True, unique = True, nullable= False, auto_increment = True)
    state = Column(String(40))
    city = Column(String(40))
    neighbourhood = Column(String(60))
    street = Column(String(100))
    place_number = Column(String(10))
    # additional information
    additional_info = Column(String(100))

    postal_code = Column(String(8))

    owner_id = Column(Integer)
    owner_type = Column(String(20))

    owner = None

    owner_name = associationproxy("owner", "name")




