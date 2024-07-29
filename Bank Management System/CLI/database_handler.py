import sqlite3

results = None
connection = sqlite3.connect("data.db", isolation_level=None)


def create_tables():
    global results, connection

    cur = connection.cursor()

    cur.execute("""
    CREATE TABLE Account(
        name TEXT,
        acc_type TEXT, 
        acc_money INTEGER,
        acc_pass TEXT,
        FOREIGN KEY(name) REFERENCES Holder(name)
    )
    """)
    cur.execute("CREATE TABLE Holder(name text PRIMARY KEY, phone text, email text, address text)")

    connection.commit()


def add_record(objects):
    global connection

    connection.execute("PRAGMA foreign_keys = 1")
    cur = connection.cursor()

    try:
        cur.execute("INSERT INTO Holder VALUES(?,?,?,?)",
                    (objects.holder_name, objects.phone, objects.email, objects.address))
        cur.execute("INSERT INTO Account VALUES(?,?,?,?)",
                    (objects.holder_name, objects.account_object.acc_type, objects.account_object.balance,
                     objects.account_object.password))

        connection.commit()
    except sqlite3.OperationalError:
        connection.rollback()
        create_tables()


def show_all():
    global connection

    cur = connection.cursor()

    try:
        return cur.execute("SELECT * FROM Account ORDER BY acc_name ASC").fetchall()
    except sqlite3.OperationalError:
        create_tables()
        show_all()

    connection.commit()


def search(word, table):
    global results, connection

    cur = connection.cursor()
    try:
        cur.execute(f"SELECT * FROM {table} WHERE name=?", (word,))
        results = cur.fetchall()

        connection.commit()
    except sqlite3.OperationalError:
        connection.rollback()
        create_tables()

    if results:
        return results
    else:
        return False


def update_record(name, money):
    global connection

    cur = connection.cursor()

    try:
        cur.execute("UPDATE Account SET acc_money = ? WHERE name = ?", (money, name))

        connection.commit()
    except sqlite3.OperationalError:
        connection.rollback()
        create_tables()


def delete_record(name):
    global connection

    cur = connection.cursor()

    try:
        cur.execute("DELETE from Account WHERE acc_name=?", (name,))
        connection.commit()
    except sqlite3.OperationalError:
        connection.rollback()
        create_tables()


def close_database_connection():
    global connection

    connection.close()