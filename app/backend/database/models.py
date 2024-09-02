from sqlalchemy.orm import Mapped, mapped_column
from backend.database.connector import Base, str_256
from sqlalchemy import text, ForeignKey, Boolean, BigInteger
import datetime
from typing import Annotated
from enum import Enum


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[
    datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))
]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow(),
    ),
]

class UserOrm(Base):
    __tablename__ = "user"

    tg_user_id: Mapped[int] = mapped_column(
        BigInteger, nullable=False, index=True, primary_key=True, unique=True
    )
    first_name: Mapped[str] = mapped_column(nullable=False, index=True)
    last_name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    date_of_birth: Mapped[datetime.date] = mapped_column(nullable=False)
    description: Mapped[str_256] = mapped_column(nullable=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
