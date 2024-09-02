from backend.database.connector import async_engine, sync_engine
from sqlalchemy.exc import NoSuchTableError
from sqlalchemy import inspect
from backend.database.models import Base
import logging
import asyncio

logging.basicConfig(level=logging.INFO)


async def check_and_create_tables(sync_engine, async_engine):
    """
    Проверка наличия таблиц и их создание, если их нет.

    :param sync_engine: Синхронный движок, используемый для инспекции.
    :param async_engine: Асинхронный движок, используемый для создания таблиц.
    """
    inspector = inspect(sync_engine)
    tables = inspector.get_table_names()

    if tables:
        logging.info("Таблицы уже существуют: %s", tables)
    else:
        logging.info("Таблицы не найдены, создаем...")
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logging.info("Таблицы успешно созданы.")

async def DbTablesInit():
    await check_and_create_tables(sync_engine, async_engine)
