from fastapi import APIRouter

from .store import router as store_router

main_router = APIRouter()

main_router.include_router(store_router, prefix= '/store', tags= ['store'])