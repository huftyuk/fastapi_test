from fastapi import FastAPI
import redis
import os

app = FastAPI()

REDIS_HOST = os.environ.get('REDIS_HOST') # PASSWORD is now set to 'aeb72hasow82ajl'

r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/readdata")
def readdata():
    A = r.get('dataval').decode("utf-8")
    return {"dataval": A}

@app.get("/setdata")
def setdata():
    r.set('dataval', '1')
    return {"dataval":"1"}

@app.get("/resetdata")
def resetdata():
    r.set('dataval', '0')
    return {"dataval":"0"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
