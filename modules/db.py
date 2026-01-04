import sqlite3


class DB:
    def __init__(self, name="db.sqlite3"):
        self.conn = sqlite3.connect(name)

    def close(self):
        self.conn.close()
        return

    def h_init_db(self):
        cursor = self.conn.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS pupil (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           text TEXT UNIQUE NOT NULL,
                           used INTEGER DEFAULT 0
                       )
        """)
        self.conn.commit()
        return

    def insert_h_data(self, text):
        cursor = self.conn.cursor()
        cursor.execute(
            """INSERT INTO pupil (text, used) 
            VALUES (?, 1)
            ON CONFLICT(text) DO UPDATE SET used = used + 1""",
            (text,),
        )
        self.conn.commit()
        return

    def fetch_all_h_data(self):
        """
        Returns:
            list[list[tuple]]: [(id, text), ...]
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM pupil")
        return cursor.fetchall()

    def delete_h_data(self, id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM pupil WHERE id = ?", (id,))
        self.conn.commit()
        return
