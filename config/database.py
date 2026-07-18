import os
import sqlite3
from .config import DATABASE_PATH

os.makedirs("instance", exist_ok=True)
def get_db():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn
