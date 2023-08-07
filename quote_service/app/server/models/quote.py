from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field

class Author(BaseModel):
    name: str = Field(..., description="Name of the author")
    goodreads_link: str = Field(..., description="Link to the author's Goodreads profile")
    slug: str = Field(..., description="Slug of the author")

    class Config:
        title = "Author Model"
        description = "Schema for author data"
        orm_mode = True

        schema_extra = {
            "example": {
                "name": "Jane Austen",
                "goodreads_link": "/author/show/1265.Jane_Austen",
                "slug": "Jane-Austen"
            }
        }

class Quote(BaseModel):
    tags: List[str] = Field(..., description="List of tags for the quote")
    author: Author = Field(..., description="Author of the quote")
    text: str = Field(..., description="Text of the quote")

    class Config:
        title = "Quote Model"
        description = "Schema for quote data"
        orm_mode = True

        schema_extra = {
            "example": {
                "tags": ["aliteracy", "books", "classic", "humor"],
                "author": {
                    "name": "Jane Austen",
                    "goodreads_link": "/author/show/1265.Jane_Austen",
                    "slug": "Jane-Austen"
                },
                "text": "“The person, be it gentleman or lady, who has not pleasure in a good n…”"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}