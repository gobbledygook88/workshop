from fastapi.testclient import TestClient
from main import app, Gesture, Result, create_results_no_database
import pytest

client = TestClient(app)


class TestRockPaperScissors:
    def test_player_plays(self):
        response = client.post("/play", json={"playerPlayed": "paper"})
        print("response", response)
        assert response.status_code == 200
        assert response.json()["gameId"] == "abc-defg-hijk"
        assert response.json()["playerPlayed"] == "paper"
        assert response.json()["timestamp"] == "2021-12-01T10:10:00Z"

    def test_server_returns_allowed_result(self):
        response = client.post("/play", json={"playerPlayed": "paper"})
        assert response.json()["result"] in [result.value for result in Result]

    def test_server_result_when_player_plays_paper(self):
        response = client.post("/play", json={"playerPlayed": "paper"})
        if response.json()["serverPlayed"] == Gesture.scissors:
            assert response.json()["result"] == Result.win
        if response.json()["serverPlayed"] == Gesture.paper:
            assert response.json()["result"] == Result.draw
        if response.json()["serverPlayed"] == Gesture.rock:
            assert response.json()["result"] == Result.loss

    def test_server_result_when_player_plays_rock(self):
        response = client.post("/play", json={"playerPlayed": "rock"})
        if response.json()["serverPlayed"] == Gesture.scissors:
            assert response.json()["result"] == Result.win
        if response.json()["serverPlayed"] == Gesture.paper:
            assert response.json()["result"] == Result.loss
        if response.json()["serverPlayed"] == Gesture.rock:
            assert response.json()["result"] == Result.draw

    def test_server_result_when_player_plays_scissors(self):
        response = client.post("/play", json={"playerPlayed": "scissors"})
        if response.json()["serverPlayed"] == Gesture.scissors:
            assert response.json()["result"] == Result.draw
        if response.json()["serverPlayed"] == Gesture.paper:
            assert response.json()["result"] == Result.win
        if response.json()["serverPlayed"] == Gesture.rock:
            assert response.json()["result"] == Result.loss

    def test_server_plays_allowed_gesture(self):
        response = client.post("/play", json={"playerPlayed": "paper"})
        assert response.json()["serverPlayed"] in [play.value for play in Gesture]

    def test_response_returns_results(self):
        response = client.get("/")
        assert len(response.json()) > 3

        list_of_game_names = [result["game_name"] for result in response.json()]
        set_of_game_names = set(list_of_game_names)
        assert len(list_of_game_names) == len(set_of_game_names)
