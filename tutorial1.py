from fastapi import FastAPI

app = FastAPI()

@app.get("/", description="This is our first route.")
async def root():
    return {"message": "hello world"}

@app.post("/")
async def post():
    return {"message": "hello from the post route"}

@app.put("/")
async def put():
    return {"message": "hello from the put route"}