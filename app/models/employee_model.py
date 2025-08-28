from sqlalchemy import Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING
from app.database import Base
import enum
from app.security import HashedPassword

if TYPE_CHECKING:
    from app.models import Store

class RolesEnum(enum.Enum):

    viewer = 'Viewer'
    editor = 'Editor'
    admin = 'Admin'

class Employee(Base):

    __tablename__ = 'employees'

    id = Column(Integer, primary_key = True, unique = True, autoincrement= True, nullable= False, index = True)
    name = Column(String(50), nullable= False)
    email = Column(String, unique = True, nullable = False)
    password = Column(HashedPassword, nullable = False)
    dateOfBirth = Column(Date, nullable = False)
    cpf = Column(String(11), nullable = False, unique= True)
    role = Column(Enum(RolesEnum), nullable= False)
    store_id = Column(Integer, ForeignKey('stores.id', ondelete= 'CASCADE'), nullable= False)

    store = relationship('Store', back_populates= 'employees')


    model_config = {
        "arbitrary_types_allowed" : True
    }
