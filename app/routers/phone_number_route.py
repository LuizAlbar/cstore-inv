from fastapi import APIRouter, status, Depends, Query
from sqlalchemy.orm import Session
from app.schemas import ReadPhoneNumber, CreatePhoneNumber, ReadAllPhoneNumber, UpdatePhoneNumber, ReadDeletedPhoneNumber
from app.database import get_db
from app.services import PhoneNumberService

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ReadPhoneNumber)
async def create_phone_number(
    phone_number : CreatePhoneNumber,
    db : Session = Depends(get_db)):

    return PhoneNumberService.create(db, phone_number)

@router.get('/{phone_number_id}/', status_code= status.HTTP_200_OK, response_model= ReadPhoneNumber)
async def read_phone_number(phone_number_id : int, db: Session = Depends(get_db)):
    
    return PhoneNumberService.read(db, phone_number_id)

@router.get('/', status_code= status.HTTP_200_OK, response_model= ReadAllPhoneNumber)
async def read_all_phone_numbers(search : str | None = Query("", description= ""), db: Session = Depends(get_db)):

    return PhoneNumberService.read_all(db, search)

@router.put('/{phone_number_id}', status_code= status.HTTP_200_OK, response_model = ReadPhoneNumber)
async def update_phone_number(phone_number_id : int, updated_phone_number : UpdatePhoneNumber, db : Session = Depends(get_db)):

    return PhoneNumberService.update(db, phone_number_id, updated_phone_number)

@router.delete('/{phone_number_id}', status_code= status.HTTP_200_OK, response_model= ReadDeletedPhoneNumber)
async def delete_phone_number(phone_number_id : int, db : Session = Depends(get_db)):

    return PhoneNumberService.delete(db, phone_number_id)