import sqlite3
import database_handler_user as db_user

connection = sqlite3.connect("issued_books.db")
cur = connection.cursor()


def create_table():
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS issued_Books(
        book_name text,
        user_id INTEGER,
        issue_date text,
        membership text,
        return_date text
      )""")
    except sqlite3.Error:
        return False


def add_record(book_name, user_id, issue_date, membership, return_date):
    try:
        cur.execute("INSERT INTO issued_Books VALUES(?, ?, ?, ?, ?)",
                    (book_name, user_id, issue_date, membership, return_date))
    except sqlite3.Error:
        return False


def show_all():
    try:
        return cur.execute("SELECT * FROM issued_Books ORDER BY user_id ASC").fetchall()
    except sqlite3.Error:
        return False


def search(word, mode):
    try:
        if mode == 0:
            word = db_user.get_user_by_id(word)
            results = cur.execute("SELECT * FROM issued_Books WHERE book_name=?", (word,)).fetchall()
        elif mode == 1:
            results = cur.execute("SELECT * FROM issued_Books WHERE user_id=?", (word,)).fetchall()
        else:
            results = cur.execute("SELECT * FROM issued_Books WHERE user_id=?", (word,)).fetchall()
    except sqlite3.Error:
        return False

    if results:
        return results
    else:
        return 0


def update_record(name, author, genre):
    try:
        cur.execute("UPDATE Books SET book_author = ?, book_genre = ? WHERE book_name = ?", (author, genre, name))
    except sqlite3.Error:
        return False


def delete_record(name):
    try:
        cur.execute("DELETE from Books WHERE book_name=?", (name,))
    except sqlite3.Error:
        return False


def commit_changes():
    connection.commit()


def end_connection():
    connection.close()
