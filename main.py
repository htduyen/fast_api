from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello World"


@app.get("/blog/unpublished")
def unpublished():
    return {
        "data": "unpublished"
    }


@app.get("/blog")
def blogs(limit: int = 5, published: bool = False, sort: Optional[str] = None):
    if published:
        return f"{limit} published blogs"
    return f"{limit} blogs"


@app.get("/blog/{id}")
def show(id: int):
    return {
        "data": id
    }


@app.get("/blog/{id}/comments")
def comments(id: int):
    return {
        "comment": id
    }


@app.post("/blog")
def add_post():
    return {
        "Post is created"
    }


@app.get("/about")
def about():
    return {
        "name": "Huynh Thanh Duyen"
    }
