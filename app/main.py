from fastapi import FastAPI
from .routers import main_router

app = FastAPI(title= "C-Store Inv")

app.include_router(main_router)