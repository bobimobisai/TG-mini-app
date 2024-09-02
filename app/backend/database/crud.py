from datetime import datetime, date
from sqlalchemy.future import select
from sqlalchemy import update, delete
from sqlalchemy.exc import NoResultFound
from typing import List, Optional
from backend.database.models import UserOrm
from backend.database.connector import async_session_factory


class UserCRUD:

    async def create_user(
        self,
        tg_user_id: int,
        first_name: str,
        last_name: str,
        username: str,
        date_of_birth: Optional[date] = None,
        description: Optional[str] = None,
    ) -> UserOrm:
        async with async_session_factory() as session:
            if isinstance(date_of_birth, str):
                date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
            user = UserOrm(
                tg_user_id=tg_user_id,
                first_name=first_name,
                last_name=last_name,
                username=username,
                date_of_birth=date_of_birth,
                description=description,
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def get_user_by_id(self, tg_user_id: int) -> Optional[UserOrm]:
        async with async_session_factory() as session:
            try:
                result = await session.execute(
                    select(UserOrm).filter_by(tg_user_id=tg_user_id)
                )
                user = result.scalar_one()
                return user
            except NoResultFound:
                return False

    async def get_all_users(self, skip: int = 0, limit: int = 10) -> List[UserOrm]:
        async with async_session_factory() as session:
            result = await session.execute(select(UserOrm).offset(skip).limit(limit))
            users = result.scalars().all()
            return users

    async def update_user(
        self,
        tg_user_id: int,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        username: Optional[str] = None,
        date_of_birth: Optional[date] = None,
        description: Optional[str] = None,
    ) -> Optional[UserOrm]:
        async with async_session_factory() as session:
            stmt = update(UserOrm).where(UserOrm.tg_user_id == tg_user_id)
            if first_name:
                stmt = stmt.values(first_name=first_name)
            if last_name:
                stmt = stmt.values(last_name=last_name)
            if username:
                stmt = stmt.values(username=username)
            if date_of_birth:
                if isinstance(date_of_birth, str):
                    date_of_birth = datetime.strptime(
                            date_of_birth, "%Y-%m-%d"
                        ).date()
                stmt = stmt.values(date_of_birth=date_of_birth)
            if description:
                stmt = stmt.values(description=description)

            stmt = stmt.execution_options(synchronize_session="fetch")

            await session.execute(stmt)
            await session.commit()

        return await self.get_user_by_id(tg_user_id)

    async def delete_user(self, tg_user_id: int) -> Optional[UserOrm]:
        async with async_session_factory() as session:
            user = await self.get_user_by_id(tg_user_id)
            if user:
                await session.execute(
                    delete(UserOrm).where(UserOrm.tg_user_id == tg_user_id)
                )
                await session.commit()
            return user
