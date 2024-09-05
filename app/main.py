from backend.database.init_db import DbTablesInit
from backend.database.crud import UserCRUD
import logging
from backend.api import app
import uvicorn


logging.basicConfig(level=logging.INFO)

