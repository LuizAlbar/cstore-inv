from sqlalchemy.orm import Session
from app.models import PhoneNumber
from app.schemas import CreatePhoneNumber, UpdatePhoneNumber
from app.utils import ResponseHandler

#Only create and delete functions for the first test step
class PhoneNumberService:
    
    @staticmethod
    def create_phone_number(db: Session, phone_number: CreatePhoneNumber):

        db_phone_number = PhoneNumber(id = None, **phone_number.model_dump())
        db.add(db_phone_number)
        db.commit()
        db.refresh(db_phone_number)

        return ResponseHandler.create_success(db_phone_number.number, db_phone_number.id, db_phone_number)
    
    @staticmethod
    def delete_phone_number(db: Session, phone_number_id : int):

        db_phone_number = db.query(PhoneNumber).filter(PhoneNumber.id == phone_number_id).first()
        
        if not db_phone_number:
            
            return ResponseHandler.not_found_error('Phone Number', phone_number_id)
        
        db.delete(db_phone_number)
        db.commit()

        return ResponseHandler.delete_success(db_phone_number.number, db_phone_number.id, db_phone_number)