import sqlite3 as db

conn = db.connect('Items.db')
cursor = conn.cursor()


def create_table():
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS items (name TEXT, price INTEGER)')


def commit_the_changes():
    conn.commit()


def insert_data(name, price):
    try:
        cursor.execute("INSERT INTO items VALUES(?,?)", (name, price))
    except:
        return False


def get_all_items():
    try:
        return cursor.execute("SELECT * FROM items ORDER BY name ASC").fetchall()
    except:
        return False


def get_item_by_name(name):
    try:
        return cursor.execute("SELECT * FROM items WHERE name=?", (name,)).fetchone()
    except:
        return False


def get_all_items_name():
    data = cursor.execute("SELECT name FROM items ORDER BY name ASC").fetchall()
    print([item[0].lower() for item in data])
    return [item[0].lower() for item in data]


def end_connection():
    conn.close()


def modify_item_price(name, price):
    try:
        cursor.execute("UPDATE items SET price = ? WHERE name = ?", (price, name))
    except:
        return False


def delete_item(name):
    try:
        cursor.execute('DELETE FROM items WHERE name = ?', (name,))
    except:
        return False
