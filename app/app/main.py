from fastapi import FastAPI
import redis
import os
import time

app = FastAPI()

REDIS_HOST = os.environ.get('REDIS_HOST') # PASSWORD is now set to 'aeb72hasow82ajl'

r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/readdata")
def readdata():
    counter = 0
    returnval = 'timed out'
    while counter < 20:
        A = r.get('dataval').decode("utf-8")
        if A == "1":
            counter = 1000
            returnval = 'response requested'
        else:
            counter = counter +1
            time.sleep(1)
      
    return {"dataval": returnval}

@app.get("/redishost")
def redishost():
    return {"dataval": REDIS_HOST}

@app.get("/setdata")
def setdata():
    A = r.set('dataval', '1')
    B = r.get('dataval').decode("utf-8")
    return {"dataval":B}

@app.get("/resetdata")
def resetdata():
    A = r.set('dataval', '0')
    B = r.get('dataval').decode("utf-8")
    return {"dataval":B}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
