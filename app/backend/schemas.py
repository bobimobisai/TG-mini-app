from pydantic import BaseModel
from typing import Optional, Union
from datetime import date


class User(BaseModel):
    tg_user_id: int
    first_name: str
    last_name: str
    username: str
    date_of_birth: date
    description: Optional[str] = None

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    tg_user_id: int
    first_name: str
    last_name: str
    username: str
    date_of_birth: Union[date, str]
    description: Optional[str] = None


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    date_of_birth: Optional[date] = None
    description: Optional[str] = None


class UserResponse(BaseModel):
    tg_user_id: int
    first_name: str
    last_name: str
    username: str
    date_of_birth: date
    description: Optional[str] = None

    class Config:
        orm_mode = True
