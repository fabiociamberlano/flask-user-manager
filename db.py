import sqlite3

def get_conn():
    return sqlite3.connect("database.db")


def init_db():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS persone (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        eta INTEGER
    )
    """)
    conn.commit()
    conn.close()



