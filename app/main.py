from fastapi import FastAPI
from .routers import main_router

app = FastAPI(title= "C-Store Inv")

@app.get("/")
def read_root():
    return {'message':'hello, world'}

app.include_router(main_router)