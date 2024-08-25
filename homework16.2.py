from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_lenght=1, max_length=15, description="Enter your name",
                                                    example="Andrey")],
                      age: int = Path(ge=18, le=120, description="Enter age", example="36")) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = username, age
    return f"User {user_id} is registered!"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str = Path(min_lenght=1, max_length=15, description="Enter your name",
                                                         example="Anton"),
                      age: int = Path(ge=18, le=120, description="Enter age", example="22")) -> str:
    users[user_id] = str(f"Имя: {username}, возраст: {age}")
    return f"User {user_id} has been updated!"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted!"
