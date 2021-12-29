from enum import Enum

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class Gesture(Enum):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"


def test_player_plays():
    response = client.post("/play", json={"playerPlayed": "paper"})
    assert response.status_code == 200
    assert response.json()['playerPlayed'] == "paper"
    assert response.json()['gameId'] == "abc-defg-hijk"
    assert response.json()['serverPlayed'] == Gesture.rock or Gesture.paper or Gesture.scissors
    assert response.json()['result'] == "you won!"
    assert response.json()['timestamp'] == "2021-12-01T10:10:00Z"
