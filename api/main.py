import random
from enum import Enum

from uuid import UUID

from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2


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

    conn = psycopg2.connect(
        "dbname=postgres user=postgres host=0.0.0.0 password=postgres"
    )
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS game (id serial PRIMARY KEY, game_name varchar unique, result varchar, server_played varchar, player_played varchar);"
    )

    

    cur.execute(
        "INSERT INTO game (game_name, result, server_played, player_played) VALUES (%s, %s, %s, %s) ON CONFLICT (game_name) DO NOTHING",
        ("1604217f-4561-4eab-9ee8-7ca923e5ab51", "won", "scissors", "rock"),
    
    )

    cur.execute(
        "INSERT INTO game (game_name, result, server_played, player_played) VALUES (%s, %s, %s, %s) ON CONFLICT (game_name) DO NOTHING",
        ("1604217f-4561-4eab-9ee8-7ca923e5ab52", "won", "scissors", "rock"),
    )

    cur.execute(
        "INSERT INTO game (game_name, result, server_played, player_played) VALUES (%s, %s, %s, %s) ON CONFLICT (game_name) DO NOTHING",
        ("1604217f-4561-4eab-9ee8-7ca923e5ab53", "won", "scissors", "rock"),
    )

    cur.execute(
        "INSERT INTO game (game_name, result, server_played, player_played) VALUES (%s, %s, %s, %s) ON CONFLICT (game_name) DO NOTHING",
        ("1604217f-4561-4eab-9ee8-7ca923e5ab54", "won", "scissors", "rock"),
    )

    cur.execute("SELECT * FROM game")
    historic_results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()



    final_historic_results = [
        HistoricResult(
            game_name=result[1],
            result=result[2],
            server_played=result[3],
            player_played=result[4],
        )
        for result in historic_results
    ]

    return final_historic_results


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
