from fastapi.testclient import TestClient
from app.server import app

client = TestClient(app)

def test_get_quotes_endpoint():
    response = client.get("/api/v1/get-quotes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_fetch_quotes_endpoint():
    response = client.get("/api/v1/fetch-quotes")
    assert response.status_code == 200
    assert response.json() == {"message": "Fetching and storing quotes in the background."}

def test_get_author_info():
    response = client.get("/api/v1/get-author-info?author_name=Albert Einstein")
    assert response.status_code == 200

def test_delete_quotes_data():
    response = client.delete("/api/v1/delete-quotes")
    assert response.status_code == 200