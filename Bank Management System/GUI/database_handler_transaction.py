import sqlite3

connection = sqlite3.connect("transactions.db", isolation_level=None)
cur = connection.cursor()


def create_table():
    try:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Transactions(
            transaction_id INTEGER,
            transaction_type TEXT NOT NULL,
            transaction_amount INTEGER NOT NULL,
            transaction_date TEXT NOT NULL,
            transaction_time TEXT NOT NULL
        )
        """)
    except sqlite3.Error as e:
        print(e)
        return False
    return True
    


def add_record(transaction_object):
    try:
        cur.execute("INSERT INTO Transactions(transaction_id, transaction_type, transaction_amount, transaction_date, transaction_time) VALUES(?,?,?,?,?)",
                    (transaction_object.transaction_id, transaction_object.transaction_type, transaction_object.transaction_amount, transaction_object.transaction_date, transaction_object.transaction_time))
    except sqlite3.Error as e:
        print(e)
        return False

def search(name):
    try:
        results_list = []
        results = cur.execute("SELECT * FROM Transactions WHERE transaction_id=?", (name,)).fetchall()
        for result in results:
            results_list.append(result)
    except sqlite3.Error as e:
        print(e)
        return False

    if results_list:
        return results_list
    else:
        return False

def delete_record(name):
    try:
        cur.execute("DELETE from Transactions WHERE id=?", (name,))
        
    except sqlite3.Error as e:
        print(e)
        return False


def close_connection():
    connection.close()

def commit_changes():
    connection.commit()
