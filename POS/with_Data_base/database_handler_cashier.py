import sqlite3 as db

conn = db.connect('Cashiers.db')
cursor = conn.cursor()


def create_table():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS cashier (
        number INTEGER PRIMARY KEY AUTOINCREMENT,
        cashier_name TEXT,
        password TEXT
        )""")


def commit_the_changes():
    conn.commit()


def insert_data(name, password):
    cursor.execute("INSERT INTO cashier(cashier_name, password) VALUES(?,?)", (name, password))


def get_all_items():
    try:
        return cursor.execute("SELECT * FROM cashier ORDER BY cashier_name ASC").fetchall()
    except:
        return False


def get_item_by_name(name):
    try:
        return cursor.execute("SELECT * FROM cashier WHERE cashier_name=?", (name,)).fetchall()
    except:
        return False


def get_all_items_name():
    try:
        data = cursor.execute("SELECT cashier_name FROM cashier ORDER BY cashier_name ASC").fetchall()
        return [item[0].lower() for item in data]
    except:
        return False

def end_connection():
    conn.close()

# create_table()
# commit_the_changes()
# end_connection()