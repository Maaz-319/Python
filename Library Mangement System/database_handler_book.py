import sqlite3

connection = sqlite3.connect("books.db")
cur = connection.cursor()


def create_table():
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS Books(
        book_name text,
        book_author text,
        book_genre text
      )""")
    except sqlite3.Error:
        return False


def add_record(name, author, genre):
    try:
        cur.execute("INSERT INTO Books VALUES(?,?,?)", (name, author, genre))
        return True
    except sqlite3.Error as e:
        print(e)
        return False


def show_all():
    try:
        return cur.execute("SELECT * FROM Books ORDER BY book_name ASC").fetchall()
    except sqlite3.Error:
        return False


def search_book_by_mode(word, mode):
    try:
        if mode == 0:
            cur.execute("SELECT * FROM Books WHERE book_name=?", (word,))
        elif mode == 1:
            cur.execute("SELECT * FROM Books WHERE book_author=?", (word,))
        elif mode == 2:
            cur.execute("SELECT * FROM Books WHERE book_genre=?", (word,))
        results = cur.fetchall()

        if results:
            return results
        else:
            return False
    except sqlite3.Error:
        return False


def get_all_book_names():
    results = []
    try:
        result = set(cur.execute("SELECT book_name FROM Books ORDER BY book_name ASC").fetchall())
        for r in result:
            results.append(r[0])
        return results
    except sqlite3.Error:
        return False


def get_all_book_authors():
    results = []
    try:
        result = cur.execute("SELECT book_author FROM Books ORDER BY book_name ASC").fetchall()
        for r in result:
            results.append(r[0])
        return results
    except sqlite3.Error:
        return False


def get_all_book_genres():
    results = []
    try:
        result = cur.execute("SELECT book_genre FROM Books ORDER BY book_name ASC").fetchall()
        for r in result:
            results.append(r[0])
        return results
    except sqlite3.Error:
        return False


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
