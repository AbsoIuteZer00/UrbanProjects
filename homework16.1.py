from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def get_main_page() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def get_admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_user_page(username: Annotated[str, Path(min_lenght=5, max_lenght=20, description="Enter username",
                                                      example="Andrey")],
                        user_id: int = Path(ge=1, le=100, description="Enter user id", example="5")) -> dict:
    return {"message": f"Вы вошли как {username} № {user_id}"}


@app.get("/user/{username}/{age}")
async def get_user_info(username: str = Path(min_length=5, max_lenght=20, description="Enter username",
                                             example="UrbanUser"),
                        age: int = Path(ge=18, le=120, description="Enter age", example="36")) -> dict:
    return {"Пользователь": username, "Возраст": age}
