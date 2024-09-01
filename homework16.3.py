from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def create_user(user: User) -> str:
    user.id = len(users) + 1
    users.append(user)
    return f"User {user} is registered!"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> str:
    try:
        edit_username = users[user_id - 1]
        edit_username.username = username
        edit_age = users[user_id - 1]
        edit_age.age = age
        return f"User {user_id} has been updated!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id - 1)
        return f"User {user_id} has been deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
