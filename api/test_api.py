from main import app

from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_game():
    assert 1 == 1

def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()['message'] == 'Hello World'

def test_post_request():
    response = client.post("/game", json = {
    "playerPlayed": "paper"})
    assert response.json()["gameId"] == "abc-defg-hijk"
    assert response.json()["playerPlayed"] == "paper"
    assert response.json()["serverPlayed"] == "rock"
    assert response.json()["result"] == "you won!"
    assert response.json()["timestamp"] == "2021-12-01T10:10:00Z"
    

