from fastapi import APIRouter, status, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import CreateAddress, ReadAddress, ReadAllAddresses, UpdateAddress, ReadDeletedAddress
from app.services import AddressService

router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED, response_model= ReadAddress)
async def create_address(
    address : CreateAddress,
    db : Session = Depends(get_db)
):
    
    return AddressService.create(db, address)

@router.get('/{address_id}', status_code= status.HTTP_200_OK, response_model= ReadAddress)
async def read_address(address_id : int, db : Session = Depends(get_db)):

    return AddressService.read(db, address_id)

@router.get('/', status_code= status.HTTP_200_OK, response_model= ReadAllAddresses)
async def read_all_addresses(search : str | None = Query("", description=""), db : Session = Depends(get_db)):

    return AddressService.read_all(db, search)

@router.put('/{address_id}', status_code= status.HTTP_200_OK, response_model= ReadAddress)
async def update_address(address_id : int, updated_address : UpdateAddress, db : Session = Depends(get_db)):

    return AddressService.update(db, address_id, updated_address)

@router.delete('/{address_id}', status_code= status.HTTP_200_OK, response_model= ReadDeletedAddress)
async def delete_address(address_id : int, db : Session = Depends(get_db)):

    return AddressService.delete(db, address_id)