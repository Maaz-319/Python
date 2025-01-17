import mysql.connector as db

# Establishing the connection to MySQL database
conn = db.connect(
    host="localhost",
    user="root",
    password="000000",
    database="pos"
)
cursor = conn.cursor()


def create_table():
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS items (
        name VARCHAR(255),
        price INT
        )"""
    )


def commit_the_changes():
    conn.commit()


def insert_data(name, price):
    try:
        cursor.execute("INSERT INTO items (name, price) VALUES (%s, %s)", (name, price))
    except db.Error as e:
        print(f"Error inserting data: {e}")
        return False
    return True


def get_all_items():
    try:
        cursor.execute("SELECT * FROM items ORDER BY name ASC")
        return cursor.fetchall()
    except db.Error as e:
        print(f"Error fetching all items: {e}")
        return False


def get_item_by_name(name):
    try:
        cursor.execute("SELECT * FROM items WHERE name=%s", (name,))
        return cursor.fetchone()
    except db.Error as e:
        print(f"Error fetching item by name: {e}")
        return False


def get_all_items_name():
    try:
        cursor.execute("SELECT name FROM items ORDER BY name ASC")
        data = cursor.fetchall()
        return [item[0].lower() for item in data]
    except db.Error as e:
        print(f"Error fetching all item names: {e}")
        return False


def modify_item_price(name, price):
    try:
        cursor.execute("UPDATE items SET price = %s WHERE name = %s", (price, name))
        conn.commit()
        return True
    except db.Error as e:
        print(f"Error modifying item price: {e}")
        return False


def delete_item(name):
    try:
        cursor.execute("DELETE FROM items WHERE name = %s", (name,))
        conn.commit()
        return True
    except db.Error as e:
        print(f"Error deleting item: {e}")
        return False


def end_connection():
    conn.close()
