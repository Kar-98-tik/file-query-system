from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Document Q&A Assistant", 
    description="A FastAPI application for querying uploaded documents", 
    version="1.0.0")

app.include_router(router)
