import sqlite3

connection = sqlite3.connect("users.db")
cur = connection.cursor()


def create_table():
    try:
        cur.execute("""CREATE TABLE User(
          i_d INTEGER PRIMARY KEY,
          user_name text,
          user_phone text,
          user_email text,
          membership TEXT
        )""")
    except sqlite3.Error:
        return False


def add_record(user_id, name, phone, email, membership):
    try:
        cur.execute("INSERT INTO User VALUES(?,?,?,?,?)", (user_id, name, phone, email, membership))
    except sqlite3.Error:
        return False


def show_all():
    try:
        return cur.execute("SELECT * FROM User ORDER BY i_d ASC").fetchall()
    except sqlite3.Error:
        return False


def search(word, mode):
    try:
        if mode == 0:
            cur.execute("SELECT * FROM User WHERE user_name=?", (word,))
        elif mode == 1:
            cur.execute("SELECT * FROM User WHERE i_d=?", (word,))
        elif mode == 2:
            cur.execute("SELECT * FROM User WHERE user_phone=?", (word,))
        elif mode == 3:
            cur.execute("SELECT * FROM User WHERE user_email=?", (word,))
        results = cur.fetchall()

        if results:
            return results
        else:
            return False
    except sqlite3.Error:
        return False


def get_user_by_id(word):
    try:
        return cur.execute("SELECT user_name FROM User WHERE i_d=?", (word,)).fetchone()[0]
    except sqlite3.Error as e:
        print(e)
        return False

def get_all_user_ids():
    try:
        return cur.execute("SELECT i_d FROM User").fetchall()
    except sqlite3.Error as e:
        print(e)
        return False

def update_record(name, author, genre):
    try:
        cur.execute("UPDATE User SET book_author = ?, book_genre = ? WHERE book_name = ?", (author, genre, name))
    except sqlite3.Error:
        return False


def delete_record(word, mode):
    try:
        if mode == 0:
            cur.execute("DELETE from User WHERE user_name=?", (word,))
        else:
            cur.execute("DELETE from User WHERE i_d=?", (word,))
    except sqlite3.Error:
        return False


def commit_changes():
    connection.commit()


def end_connection():
    connection.close()