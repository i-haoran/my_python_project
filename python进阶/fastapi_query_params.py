from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

fake_db = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
    {"id": 3, "name": "Charlie", "age": 35},
]


@app.get("/users")
def get_users(
    page: int = 1, limit: int = 10, min_age: int = 0, name: str | None = None
):
    results = [u for u in fake_db if u["age"] >= min_age]
    if name:
        results = [u for u in results if name.lower() in u["name"].lower()]
    start = (page - 1) * limit
    return {
        "page": page,
        "limit": limit,
        "total": len(results),
        "users": results[start : start + limit],
    }


app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
