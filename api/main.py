import random
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel


class Gesture(Enum):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"


class Result(Enum):
    win = "you win!"
    loss = "you lose! haha"
    draw = "draw... lame"


class Action(BaseModel):
    playerPlayed: Gesture


app = FastAPI()


def handle_result(action: Gesture, server: Gesture):
    if action == server:
        return Result.draw
    if action == Gesture.rock and server == Gesture.paper:
        return Result.loss
    if action == Gesture.paper and server == Gesture.scissors:
        return Result.loss
    if action == Gesture.scissors and server == Gesture.rock:
        return Result.loss
    if action == Gesture.rock and server == Gesture.scissors:
        return Result.win
    if action == Gesture.paper and server == Gesture.rock:
        return Result.win
    if action == Gesture.scissors and server == Gesture.paper:
        return Result.win


@app.post("/play")
async def player_plays(action: Action):
    server_action = random.choice(list(Gesture))

    return {
        "gameId": "abc-defg-hijk",
        "playerPlayed": action.playerPlayed,
        "serverPlayed": server_action,
        "result": handle_result(action.playerPlayed, server_action),  # determine win/loss
        "timestamp": "2021-12-01T10:10:00Z"
    }
