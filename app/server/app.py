from fastapi import FastAPI

from app.server.routes.quote import router as QuoteRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(QuoteRouter, tags=["Quote"], prefix="/api/v1")

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hi intail! Welcome to my quote scraper!"}
