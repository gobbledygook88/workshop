from fastapi.testclient import TestClient
from main import app, Gesture, Result

client = TestClient(app)


def test_player_plays():
    response = client.post("/play", json={"playerPlayed": "paper"})
    assert response.status_code == 200
    assert response.json()['gameId'] == "abc-defg-hijk"
    assert response.json()['playerPlayed'] == "paper"
    assert response.json()['timestamp'] == "2021-12-01T10:10:00Z"


def test_server_returns_allowed_result():
    response = client.post("/play", json={"playerPlayed": "paper"})
    assert response.json()['result'] in [result.value for result in Result]


def test_server_result_when_player_plays_paper():
    response = client.post("/play", json={"playerPlayed": "paper"})
    if (response.json()['serverPlayed'] == Gesture.scissors):
        assert response.json()['result'] == Result.win
    if (response.json()['serverPlayed'] == Gesture.paper):
        assert response.json()['result'] == Result.draw
    if (response.json()['serverPlayed'] == Gesture.rock):
        assert response.json()['result'] == Result.loss


def test_server_result_when_player_plays_rock():
    response = client.post("/play", json={"playerPlayed": "rock"})
    if (response.json()['serverPlayed'] == Gesture.scissors):
        assert response.json()['result'] == Result.win
    if (response.json()['serverPlayed'] == Gesture.paper):
        assert response.json()['result'] == Result.loss
    if (response.json()['serverPlayed'] == Gesture.rock):
        assert response.json()['result'] == Result.draw


def test_server_result_when_player_plays_scissors():
    response = client.post("/play", json={"playerPlayed": "scissors"})
    if (response.json()['serverPlayed'] == Gesture.scissors):
        assert response.json()['result'] == Result.draw
    if (response.json()['serverPlayed'] == Gesture.paper):
        assert response.json()['result'] == Result.win
    if (response.json()['serverPlayed'] == Gesture.rock):
        assert response.json()['result'] == Result.loss


def test_server_plays_allowed_gesture():
    response = client.post("/play", json={"playerPlayed": "paper"})
    assert response.json()['serverPlayed'] in [play.value for play in Gesture]