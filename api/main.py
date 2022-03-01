import random
from enum import Enum

from uuid import UUID

from fastapi import FastAPI
from pydantic import BaseModel


class Gesture(Enum):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"


class Result(Enum):
    win = "you win... hurray!"
    loss = "you lose :("
    draw = "it's a draw... hurray?"


class HistoricResult(BaseModel):
    game_name: UUID
    player_played: str
    server_played: str
    result: str


class Action(BaseModel):
    playerPlayed: Gesture


app = FastAPI()


def create_results_no_database():
    RESULTS = []
    book_1 = HistoricResult(
        game_name="1604217f-4561-4eab-9ee8-7ca923e5ab51",
        player_played="Title One",
        server_played="Author One",
        result="Desc One",
    )
    book_2 = HistoricResult(
        game_name="1604217f-4561-4eab-9ee8-7ca923e5ab52",
        player_played="Title Two",
        server_played="Author Two",
        result="Desc Two",
    )
    book_3 = HistoricResult(
        game_name="1604217f-4561-4eab-9ee8-7ca923e5ab53",
        player_played="Title Three",
        server_played="Author Three",
        result="Desc Three",
    )
    book_4 = HistoricResult(
        game_name="1604217f-4561-4eab-9ee8-7ca923e5ab54",
        player_played="Title Four",
        server_played="Author Four",
        result="Desc Four",
    )
    RESULTS.append(book_1)
    RESULTS.append(book_2)
    RESULTS.append(book_3)
    RESULTS.append(book_4)
    return RESULTS


@app.get("/")
async def returns_result():
    return create_results_no_database()
     


@app.post("/play")
async def player_plays(action: Action):
    server_action = random.choice(list(Gesture))

    return {
        "gameId": "abc-defg-hijk",
        "playerPlayed": action.playerPlayed,
        "serverPlayed": server_action,
        "result": handle_result(action.playerPlayed, server_action),
        "timestamp": "2021-12-01T10:10:00Z",
    }


def handle_result(player: Gesture, server: Gesture):
    if player == server:
        return Result.draw
    if player == Gesture.rock and server == Gesture.paper:
        return Result.loss
    if player == Gesture.paper and server == Gesture.scissors:
        return Result.loss
    if player == Gesture.scissors and server == Gesture.rock:
        return Result.loss
    if player == Gesture.rock and server == Gesture.scissors:
        return Result.win
    if player == Gesture.paper and server == Gesture.rock:
        return Result.win
    if player == Gesture.scissors and server == Gesture.paper:
        return Result.win
