from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_load():
    return {"message": "Hello World!"}
