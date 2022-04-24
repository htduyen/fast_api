** Setup

- pyhton3 -m venv <name_of_env>
- source <name_of_env>/bin/activate
- install pip, fastapi, unicorn,...

**Start main.py:**
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello World"
```

`uvicorn main:app --reload`
- ==> main: name of module
- ==> app: name of variable defined in main module


- **FastAPI read line by line:** 
  - @app.get("/blog/unpublished")
  - @app.get("/blog/{id}"

