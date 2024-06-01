#Type this in terminal: pip install "fastapi[all]"  after installing fast api
# stores dependecies in the file  pip freexe > requirements.txt

from fastapi import FastAPI

#Create an instance
app = FastAPI()

@app.get("/")
def start():
    return {"message": "Hello World"}
