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


@app.get("/about")
def about():
    return {
        "name": "Huynh Thanh Duyen"
    }
