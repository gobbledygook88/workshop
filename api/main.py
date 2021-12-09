from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/game")
async def player():
    return {
  "gameId": "abc-defg-hijk",           
  "playerPlayed": "paper",
  "serverPlayed": "rock",
  "result": "you won!",               
  "timestamp": "2021-12-01T10:10:00Z"  
}
