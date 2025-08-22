from fastapi import APIRouter

from .store import router as store_router
from .phone_number import router as phone_number_router
from .address import router as address_router
from .employee import router as employee_router

main_router = APIRouter()

main_router.include_router(store_router, prefix= '/store', tags= ['store'])
main_router.include_router(phone_number_router, prefix= '/phone', tags= ['phone_number'])
main_router.include_router(address_router, prefix= '/address', tags=['address'])
main_router.include_router(employee_router, prefix='/employee', tags=['employee'])