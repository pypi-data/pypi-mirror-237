import sqlite3

from mlsteam_model_sdk.utils.config import get_config_path


__db_path = str(get_config_path(check=True).parent / 'db')
__db_init = False


def __init_db():
    global __db_init

    if __db_init:
        return

    conn = sqlite3.connect(__db_path)
    conn.execute("""CREATE TABLE IF NOT EXISTS lmvs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pid INTEGER NOT NULL,
        p_create_time TEXT NOT NULL,
        info TEXT NOT NULL
    )""")
    conn.commit()
    __db_init = True


def connect_db() -> sqlite3.Connection:
    __init_db()
    conn = sqlite3.connect(__db_path)
    return conn
