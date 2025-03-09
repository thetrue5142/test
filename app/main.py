# FastAPI

import webbrowser
from fastapi import FastAPI

app = FastAPI(title="My API",
    description="This is a FastAPI application.",
    version="1.0.0",
    docs_url="/docs", )

@app.on_event("startup")
async def startup():
    webbrowser.open("http://127.0.0.1:8000/docs")

@app.get("/")
def read_root():
    return {"message": "Message from main.py"}
