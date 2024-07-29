import sqlite3

connection = sqlite3.connect("users.db", isolation_level=None)
cur = connection.cursor()


def create_table():
    try:
        cur.execute("""
        CREATE TABLE User(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            email TEXT,
            address TEXT,
            account_type TEXT,
            balance INTEGER,
            password TEXT
        )
        """)
    except sqlite3.Error as e:
        print(e)
        return False
    


def add_record(user):
    try:
        cur.execute("INSERT INTO User(name, phone, email, address, account_type, balance, password) VALUES(?,?,?,?,?,?,?)",
                    (user.name, user.phone, user.email, user.address, user.account_type, user.balance, user.password))

    except sqlite3.Error as e:
        print(e)
        return False


def show_all_name():
    list_of_names = []
    try:
        results = cur.execute("SELECT name FROM User ORDER BY name ASC").fetchall()
        list_of_names = [result[0] for result in results]
        return list_of_names    
    except sqlite3.Error as e:
        print(e)
        return False

    


def search(name):
    try:
        results = cur.execute("SELECT * FROM User WHERE name=?", (name,)).fetchone()
    except sqlite3.Error as e:
        print(e)
        return False

    if results:
        return results
    else:
        return False


def update_record(user, new_name):
    try:
        user_id = search(user.name)[0]
        cur.execute("UPDATE User SET name=?, phone=?, email=?, address=?, account_type=?, balance=?, password=? WHERE user_id=?",
                    (new_name, user.phone, user.email, user.address, user.account_type, user.balance, user.password, user_id))        
    except sqlite3.Error as e:
        print(e)
        return False


def delete_record(name):
    try:
        cur.execute("DELETE from User WHERE name=?", (name,))
        
    except sqlite3.Error as e:
        print(e)
        return False


def close_connection():
    connection.close()

def commit_changes():
    connection.commit()
