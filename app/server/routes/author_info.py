from fastapi import HTTPException
import httpx

async def get_author_open_lib_info(author_name: str):
    async with httpx.AsyncClient() as client:
        search_response = await client.get("https://openlibrary.org/search/authors.json", params={"q": author_name})
        search_response.raise_for_status()
        search_data = search_response.json()

        if "docs" in search_data and len(search_data["docs"]) > 0:
            author_key = search_data["docs"][0]["key"]

            author_response = await client.get(f"https://openlibrary.org/authors/{author_key}.json")
            author_response.raise_for_status()
            author_info = author_response.json()

            # fetch paginated works by the author
            works_response = await client.get(f"https://openlibrary.org/authors/{author_key}/works.json", params={"limit": 5})
            works_response.raise_for_status()
            works_data = works_response.json()

            works_entries = works_data.get("entries", [])
            work_titles = [entry.get("title", "") for entry in works_entries]

            bio_value = author_info.get("bio")
            # bio information
            if isinstance(bio_value, str):
                bio_value = author_info.get("bio", "")

            if isinstance(bio_value, dict):
                bio_value = author_info.get("bio", {})["value"]


            simplified_response = {
                "date_of_birth": author_info.get("birth_date", ""),
                "bio": bio_value,
                "books": work_titles,
            }

            return simplified_response
        else:
            raise HTTPException(status_code=404, detail="Author not found")