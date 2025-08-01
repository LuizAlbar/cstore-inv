from fastapi import FastAPI

app = FastAPI(title= "C-Store Inv")

@app.get("/")
def read_root():
    return {'message':'hello, world'}