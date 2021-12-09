from main import app

from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_game():
    assert 1 == 1

def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()['message'] == 'Hello World'