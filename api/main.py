
   
import random
from enum import Enum

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


class Action(BaseModel):
    playerPlayed: Gesture


app = FastAPI()


@app.post("/game")
async def player_plays(action: Action):
  server_action = random.choice(list(Gesture))

  return {
  "gameId": "abc-defg-hijk",           
  "playerPlayed": action.playerPlayed,
  "serverPlayed": server_action,
  "result": handle_result(action.playerPlayed, server_action),               
  "timestamp": "2021-12-01T10:10:00Z"  
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