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
        CREATE TABLE IF NOT EXISTS cashier (
        number INT AUTO_INCREMENT PRIMARY KEY,
        cashier_name VARCHAR(255),
        password VARCHAR(255)
        )
        """
    )


def commit_the_changes():
    conn.commit()


def insert_data(name, password):
    cursor.execute("INSERT INTO cashier (cashier_name, password) VALUES (%s, %s)", (name, password))


def get_all_items():
    try:
        cursor.execute("SELECT * FROM cashier ORDER BY cashier_name ASC")
        return cursor.fetchall()
    except db.Error as e:
        print(f"Error: {e}")
        return False


def get_item_by_name(word):
    cursor.execute("SELECT * FROM cashier WHERE cashier_name=%s", (word,))
    return cursor.fetchone()


def get_all_items_name():
    try:
        cursor.execute("SELECT cashier_name FROM cashier ORDER BY cashier_name ASC")
        data = cursor.fetchall()
        return [item[0].lower() for item in data]
    except db.Error as e:
        print(f"Error: {e}")
        return False


def end_connection():
    conn.close()
