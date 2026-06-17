from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()


# API 接口
@app.get("/api/hello")
def read_root():
    return {"message": "Hello World from API"}


# 挂载前端静态文件
app.mount("/", StaticFiles(directory="static", html=True), name="static")
