import random
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel


class Gesture(Enum):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"


class Action(BaseModel):
    playerPlayed: Gesture


app = FastAPI()


@app.post("/play")
async def player_plays(action: Action):
    server_action = random.choice(['rock', 'paper', 'scissors'])
    return {
        "gameId": "abc-defg-hijk",
        "playerPlayed": action.playerPlayed,
        "serverPlayed": server_action,
        "result": "you won!",  # determine win/loss
        "timestamp": "2021-12-01T10:10:00Z"
    }
