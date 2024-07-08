from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Memes API"}

def test_create_meme():
    response = client.post("/memes", json={"text": "Test meme", "image_url": "http://example.com/image.jpg"})
    assert response.status_code == 200
    assert response.json()["text"] == "Test meme"

def test_read_memes():
    response = client.get("/memes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
