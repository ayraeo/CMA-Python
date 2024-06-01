#imports FastAPI
from fastapi import FastAPI

#Creates an instance
app = FastAPI()

@app.get("/")
def start():
    return {"message": "Welcome to FastApi"}
