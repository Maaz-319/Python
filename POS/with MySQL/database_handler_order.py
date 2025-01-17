import mysql.connector as db

conn = db.connect(
    host="localhost",
    user="root",
    password="000000",
    database="pos"
)
cursor = conn.cursor()


def create_table():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS orderedItems (
        number INT AUTO_INCREMENT PRIMARY KEY,
        orderNo INT,
        item_name VARCHAR(255),
        date_time DATETIME,
        cashier_name VARCHAR(255),
        total INT,
        quantity INT
        )
        """
    )


def commit_the_changes():
    conn.commit()


def insert_data(order_no, name, date_time, cashier, total_price, quantity):
    cursor.execute(
        """
        INSERT INTO orderedItems (orderNo, item_name, date_time, cashier_name, total, quantity)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (order_no, name, date_time, cashier, total_price, quantity)
    )


def get_all_items():
    try:
        cursor.execute("SELECT * FROM orderedItems ORDER BY orderNo ASC")
        return cursor.fetchall()
    except db.Error as e:
        print(f"Error: {e}")
        return False


def get_item_by_order_no(order_no):
    try:
        cursor.execute("SELECT * FROM orderedItems WHERE orderNo=%s", (order_no,))
        return cursor.fetchall()
    except db.Error as e:
        print(f"Error: {e}")
        return False


def get_max_min_order_by_price(mode):
    try:
        if mode == "max":
            cursor.execute("SELECT MAX(total) FROM orderedItems")
        elif mode == "min":
            cursor.execute("SELECT MIN(total) FROM orderedItems")
        return cursor.fetchone()
    except db.Error as e:
        print(f"Error: {e}")
        return False


def get_max_min_order_by_price_on_date(mode, date):
    try:
        if mode == "max":
            cursor.execute("SELECT MAX(total) FROM orderedItems WHERE date_time=%s", (date,))
        elif mode == "min":
            cursor.execute("SELECT MIN(total) FROM orderedItems WHERE date_time=%s", (date,))
        return cursor.fetchone()
    except db.Error as e:
        print(f"Error: {e}")
        return False


def get_most_min_sold_item(mode):
    try:
        if mode == "max":
            cursor.execute("""
                SELECT item_name, COUNT(item_name) as count
                FROM orderedItems
                GROUP BY item_name
                ORDER BY count DESC
                LIMIT 1
            """)
        else:
            cursor.execute("""
                SELECT item_name, COUNT(item_name) as count
                FROM orderedItems
                GROUP BY item_name
                ORDER BY count ASC
                LIMIT 1
            """)
        return cursor.fetchone()
    except db.Error as e:
        print(f"Error: {e}")
        return False


def fetch_data_by_date(start_date, end_date):
    try:
        query = """
            SELECT item_name, date_time, quantity
            FROM orderedItems
            WHERE date_time BETWEEN %s AND %s
        """
        cursor.execute(query, (start_date, end_date))
        return cursor.fetchall()
    except db.Error as e:
        print(f"Error: {e}")
        return False


def fetch_all_data():
    try:
        query = """
            SELECT item_name, date_time, quantity
            FROM orderedItems
        """
        cursor.execute(query)
        return cursor.fetchall()
    except db.Error as e:
        print(f"Error: {e}")
        return False


def end_connection():
    conn.close()

# def modify_item_price(name, price):
#     cursor.execute("UPDATE items SET price = ? WHERE name = ?", (price, name))


# def delete_item(name):
#     cursor.execute('DELETE FROM items WHERE name = ?', (name,))