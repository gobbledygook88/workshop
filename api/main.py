from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/game")
async def player():
    return {"gameId": "abc-defg-hijk"}
