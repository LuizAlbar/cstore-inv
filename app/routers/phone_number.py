from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas import ReadPhoneNumber, CreatePhoneNumber
from app.database import get_db
from app.services import PhoneNumberService

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ReadPhoneNumber)
async def create_phone_number(
    phone_number : CreatePhoneNumber,
    db : Session = Depends(get_db)):

    return PhoneNumberService.create(db, phone_number)