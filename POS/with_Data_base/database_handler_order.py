import sqlite3 as db

conn = db.connect('Orders.db')
cursor = conn.cursor()


def create_table():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS orderedItems (
        number INTEGER PRIMARY KEY AUTOINCREMENT,
        orderNo INTEGER,
        item_name TEXT,
        date_time TEXT,
        cashier_name TEXT
        )""")


def commit_the_changes():
    conn.commit()


def insert_data(order_no, name, date_time, cashier):
    cursor.execute("INSERT INTO orderedItems(orderNo, item_name, date_time, cashier_name) VALUES(?,?,?,?)", (order_no, name, date_time, cashier))


def get_all_items():
    try:
        return cursor.execute("SELECT * FROM orderedItems ORDER BY orderNo ASC").fetchall()
    except:
        return False


def get_item_by_order_no(order_no):
    try:
        return cursor.execute("SELECT * FROM orderedItems WHERE orderNo=?", (order_no,)).fetchall()
    except:
        return False


def end_connection():
    conn.close()


# def modify_item_price(name, price):
#     cursor.execute("UPDATE items SET price = ? WHERE name = ?", (price, name))


# def delete_item(name):
#     cursor.execute('DELETE FROM items WHERE name = ?', (name,))

# create_table()
# commit_the_changes()
# end_connection()