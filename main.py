from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post("/sample")
def create_item(item:dict):
    print(item)
    return {"item":item}

