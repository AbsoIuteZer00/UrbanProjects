from fastapi import FastAPI, status, Body, HTTPException, Request, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get("/users/{user_id}")
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id]})
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.post("/")
async def create_user(request: Request, user: User) -> HTMLResponse:
    if users:
        user.id = max(users, key=lambda u: u.id).id + 1
    else:
        user.id = 0
    users.append(user)
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> str:
    try:
        edit_username = users[user_id]
        edit_username.username = username
        edit_age = users[user_id]
        edit_age.age = age
        return f"User {user_id} has been updated!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f"User {user_id} has been deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
