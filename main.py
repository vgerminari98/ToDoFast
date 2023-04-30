from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
