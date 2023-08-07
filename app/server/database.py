from typing import List
import asyncio
import httpx
import motor.motor_asyncio
from decouple import config
from fastapi import HTTPException
import re
import json
from app.server.models.quote import Quote, Author


MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.quotes

quotes_collection = database.get_collection("quotes_collection")


async def fetch_quotes_from_mongodb():

    cursor = quotes_collection.find({}, {"_id": False})

    # Convert the cursor to a list of JSON objects
    quotes = await cursor.to_list(length=None)
    
    return quotes


# Function to fetch JSON data from a specific page and return the quotes
async def fetch_quotes_from_page(page_num: int) -> List[Quote]:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://quotes.toscrape.com/js/page/{page_num}/")
            response.raise_for_status()
            response_text = response.text

            # Use regex to find and extract the JSON data
            data_match = re.search(r'var data = (\[.*?\]);', response_text, re.DOTALL)
            if not data_match:
                raise ValueError("JSON data not found")

            data_string = data_match.group(1)
            quotes = json.loads(data_string)

            # Convert the fetched data to a list of Quote objects
            quote_objects = [
                Quote(
                    tags=quote['tags'],
                    author=Author(**quote['author']),
                    text=quote['text']
                )
                for quote in quotes
            ]

            return quote_objects

    except (httpx.HTTPError, ValueError, Exception) as e:
        raise HTTPException(status_code=500, detail=str(e))


# Function to store the quotes in mongo
def store_quotes_in_mongodb(quotes: List[Quote]):
    # Convert Quote objects to dictionaries for storage
    quote_dicts = [quote.dict() for quote in quotes]
    quotes_collection.insert_many(quote_dicts)


# Function to fetch and store json data from all pages (1 to 10)
# insert pages to consts file
async def fetch_and_store_quotes():
    try:
        tasks = [fetch_quotes_from_page(page_num) for page_num in range(1, 11)]
        quotes_list = await asyncio.gather(*tasks)
        all_quotes = [quote for quotes in quotes_list for quote in quotes]
        store_quotes_in_mongodb(all_quotes)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Delete the quotes from the database
async def delete_quotes():
    try:
        # Delete all documents in the collection
        result = await quotes_collection.delete_many({})
        if result.deleted_count > 0:
            return True
        else:
            return False
    except Exception as e:
        print("Error deleting quotes:", e)
        return False
