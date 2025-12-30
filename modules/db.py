import sqlite3

def get_db_conn(name="db.sqlite3"):
    conn = sqlite3.connect(name)
    return conn

