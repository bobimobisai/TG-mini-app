from backend.database.init_db import DbTablesInit
from backend.database.crud import UserCRUD
import logging
from backend.api import app
import uvicorn


logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8050)