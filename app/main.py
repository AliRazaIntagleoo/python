from fastapi import FastAPI, Depends
import asyncio
from app.schemas.user import UserCreate, UserResponse

app = FastAPI()

fake_users_db = []

counter = 0 
shared_list = []
data = {"count": 0}


@app.get("/inc")
async def inc():
    data["count"] += 1
    await asyncio.sleep(1)
    return data


@app.get("/add")
async def add():
    shared_list.append("X")
    await asyncio.sleep(1)
    return shared_list

def get_user():
    return {"id": 1}

@app.get("/profile")
def profile(user=Depends(get_user)):
    return user

@app.get("/block")
def block():
    return {"msg": "done"}


@app.get("/non-block")
async def non_block():
    await asyncio.sleep(5)
    return {"msg": "done"}

@app.get("/sync")
def sync_route():
    return {"type": "sync"}

@app.get("/async")
async def async_route():
    return {"type": "async"}

@app.get("/hit")
async def hit():
    global counter
    temp = counter
    await asyncio.sleep(1)
    counter = temp + 1
    return {"counter": counter}

@app.get("/users")
def get_user():
    print("Fetching users",fake_users_db)
    return fake_users_db

@app.post("/users")
def create_user(user: UserCreate):
    fake_users_db.append(user)
    return user