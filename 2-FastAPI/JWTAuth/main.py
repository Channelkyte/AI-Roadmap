import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
def get_user():
    return{"Testing": "Hello"}