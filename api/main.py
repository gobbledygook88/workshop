from fastapi import FastAPI

app = FastAPI()



@app.post("/")
async def player_paper():
    return {"playerPlayed": "Paper", "gameId": "abc-defg-hijk"}