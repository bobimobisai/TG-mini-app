from backend.database.init_db import DbTablesInit
from backend.database.crud import UserCRUD
import logging
from backend.api import app
import uvicorn


logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
