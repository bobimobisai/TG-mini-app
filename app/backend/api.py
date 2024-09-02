import logging
import os
from typing import List
from aiogram.types import BotCommand
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
import uvicorn
from backend.database.crud import UserCRUD
from starlette.responses import FileResponse
from backend.database.models import UserOrm
from backend.database.connector import async_session_factory
from backend.schemas import UserCreate, UserUpdate, UserResponse, User
from backend.bot import bot, dp


logging.basicConfig(level=logging.INFO)


app = FastAPI()
crud = UserCRUD()

static_dir = os.path.join(os.path.dirname(__file__), "static")

# Убедимся, что директория существует
if not os.path.exists(static_dir):
    raise RuntimeError(f"Directory '{static_dir}' does not exist")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.on_event("startup")
async def on_startup():
    async def start_polling():
        await bot.set_my_commands(
            [
                BotCommand(command="start", description="Start"),])
        await dp.start_polling(bot)

    loop = asyncio.get_event_loop()
    loop.create_task(start_polling())


async def get_db():
    async with async_session_factory() as session:
        yield session


@app.get("/")
async def read_index():
    return FileResponse(os.path.join(static_dir, "index.html"))


@app.get("/get_user/{tg_user_id}", response_class=JSONResponse)
async def get_user(tg_user_id: int, db: AsyncSession = Depends(get_db)):
    user = await crud.get_user_by_id(tg_user_id=tg_user_id)
    if user is False:
        raise HTTPException(status_code=404, detail="User not found")
    user_dict = user_to_dict(user)
    return JSONResponse(content=user_dict, status_code=200)


@app.post("/create_user", response_class=JSONResponse)
async def create_user_(user: UserCreate, db: AsyncSession = Depends(get_db)):
    created_user = await crud.create_user(
        tg_user_id=user.tg_user_id,
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        date_of_birth=user.date_of_birth,
        description=user.description,
    )
    user_dict = user_to_dict(created_user)
    return JSONResponse(content=user_dict, status_code=200)


@app.get("/users", response_class=JSONResponse)
async def read_users(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    users = await crud.get_all_users(skip=skip, limit=limit)
    logging.info(f"Users: {users}")
    if users:
        users_dict = [user_to_dict(user) for user in users]
        return JSONResponse(content=users_dict, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="Users not found")


@app.put("/update_users/{user_id}", response_class=JSONResponse)
async def update_user(
    user_id: int, user: UserUpdate, db: AsyncSession = Depends(get_db)
):
    updated_user = await crud.update_user(
        user_id=user_id,
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        date_of_birth=user.date_of_birth,
        description=user.description,
    )
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_dict = user_to_dict(updated_user)
    return JSONResponse(content=user_dict, status_code=200)


@app.delete("/dell_users/{user_id}", response_class=JSONResponse)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    deleted_user = await crud.delete_user(user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_dict = user_to_dict(deleted_user)
    return JSONResponse(content=user_dict, status_code=200)


@app.post("/webapp_data")
async def handle_webapp_data(request: Request):
    logging.info(f"User data: {request.json()}")


def user_to_dict(user: UserOrm) -> dict:
    return {
        "tg_user_id": user.tg_user_id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "date_of_birth": user.date_of_birth.isoformat() if user.date_of_birth else None,
        "description": user.description,
        "created_at": user.created_at.isoformat() if user.created_at else None,
        "updated_at": user.updated_at.isoformat() if user.updated_at else None,
    }
