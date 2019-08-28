from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/readdata")
def readdata():
    return {"dataval":dataval}

@app.get("/setdata")
def setdata():
    dataval = "1"
    return {"dataval":dataval}

@app.get("/resetdata")
def resetdata():
    dataval = "0"
    return {"dataval":dataval}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
