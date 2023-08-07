from typing import List, Optional

from fastapi import APIRouter, Body, Query, BackgroundTasks, HTTPException
from fastapi.encoders import jsonable_encoder
import httpx
from app.server.routes.author_info import get_author_open_lib_info

from app.server.database import (
    fetch_quotes_from_mongodb,
    fetch_and_store_quotes,
    delete_quotes,
)
from app.server.models.quote import (
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()


@router.get("/get-quotes", response_model=list[dict])
async def get_quotes_endpoint():
    quotes = await fetch_quotes_from_mongodb()
    return quotes

@router.get("/fetch-quotes")
async def fetch_quotes_endpoint(background_tasks: BackgroundTasks):
    background_tasks.add_task(fetch_and_store_quotes)
    return {"message": "Fetching and storing quotes in the background."}


@router.get("/get-author-info")
async def get_author_info(author_name: str):
    try:
        return await get_author_open_lib_info(author_name=author_name)
        
    except (httpx.HTTPError, ValueError, Exception) as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete-qoutes", response_description="Quotes data deleted from the database")
async def delete_quotes_data():
    deleted_quotes = await delete_quotes()
    if deleted_quotes:
        return ResponseModel(
            "Quotes deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "No Quotes found"
    )

