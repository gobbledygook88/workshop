from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_player_paper():
    response = client.post("/", json={"playerPlayed": "Paper"})
    assert response.status_code == 200
    assert response.json()['playerPlayed'] == "Paper"
    assert response.json()['gameId'] == "abc-defg-hijk"
    assert response.json()['serverPlayed'] == "Rock"




