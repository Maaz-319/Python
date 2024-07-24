import sqlite3 as db

conn = db.connect('librarians.db')
cursor = conn.cursor()


def create_table():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS librarian (
        number INTEGER PRIMARY KEY AUTOINCREMENT,
        librarian_name TEXT,
        password TEXT
        )""")


def commit_the_changes():
    conn.commit()


def insert_data(name, password):
    cursor.execute("INSERT INTO librarian(librarian_name, password) VALUES(?,?)", (name, password))


def get_all_items():
    try:
        return cursor.execute("SELECT * FROM librarian ORDER BY librarian_name ASC").fetchall()
    except:
        return False


def get_item_by_name(word):
    return cursor.execute("SELECT * FROM librarian WHERE librarian_name=?", (word,)).fetchone()


def get_all_items_name():
    try:
        data = cursor.execute("SELECT librarian_name FROM librarian ORDER BY librarian_name ASC").fetchall()
        return [item[0].lower() for item in data]
    except:
        return False

def end_connection():
    conn.close()
