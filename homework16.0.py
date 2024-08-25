from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_main_page() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def get_admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_user_page(user_id) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/id")
async def get_id_info(username: str, age: int) -> dict:
    return {"Пользователь": username, "Возраст": age}
