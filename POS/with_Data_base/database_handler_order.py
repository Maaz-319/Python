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
        cashier_name TEXT,
        total INTEGER
        )""")


def commit_the_changes():
    conn.commit()


def insert_data(order_no, name, date_time, cashier, total_price):
    cursor.execute("INSERT INTO orderedItems(orderNo, item_name, date_time, cashier_name, total) VALUES(?,?,?,?,?)",
                   (order_no, name, date_time, cashier, total_price))


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


def get_max_min_order_by_price(mode):
    if mode == "max":
        return cursor.execute("SELECT MAX(total) FROM orderedItems").fetchone()
    elif mode == "min":
        return cursor.execute("SELECT MIN(total) FROM orderedItems").fetchone()


def get_max_min_order_by_price_on_date(mode, date):
    if mode == "max":
        return cursor.execute("SELECT MAX(total) FROM orderedItems WHERE date_time=?", (date,)).fetchone()
    elif mode == "min":
        return cursor.execute("SELECT MIN(total) FROM orderedItems WHERE date_time=?", (date,)).fetchone()


def get_most_min_sold_item(mode):
    if mode == "max":
        return cursor.execute("""
                    SELECT item_name, COUNT(item_name) as count
                FROM orderedItems
                GROUP BY item_name
                ORDER BY count DESC
                LIMIT 1
                """).fetchone()
    else:
        return cursor.execute("""
                    SELECT item_name, COUNT(item_name) as count
                FROM orderedItems
                GROUP BY item_name
                ORDER BY count ASC
                LIMIT 1
                """).fetchone()


def end_connection():
    conn.close()

# def modify_item_price(name, price):
#     cursor.execute("UPDATE items SET price = ? WHERE name = ?", (price, name))


# def delete_item(name):
#     cursor.execute('DELETE FROM items WHERE name = ?', (name,))

# create_table()
# commit_the_changes()
# end_connection()
