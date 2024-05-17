import sqlite3


def create_table_account():
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    cur.execute("CREATE TABLE Account(acc_name text, acc_type text, acc_money integer, acc_pass text)")

    connection.commit()
    connection.close()


def create_table_holder():
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    cur.execute("CREATE TABLE Holder(name text, phone text, email text, address text)")

    connection.commit()
    connection.close()


def add_record_account(name, acc_type, balance, password):
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    try:
        cur.execute("INSERT INTO Account VALUES(?,?,?,?)", (name, acc_type, balance, password))
    except:
        create_table_account()
        create_table_holder()
        add_record_account(name, acc_type, balance, password)

    connection.commit()
    connection.close()


def add_record_holder(name, phone, email, address):
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    try:
        cur.execute("INSERT INTO Holder VALUES(?,?,?,?)", (name, phone, email, address))
    except:
        create_table_account()
        create_table_holder()
        add_record_holder(name, phone, email, address)

    connection.commit()
    connection.close()


def show_all():
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    try:
        return cur.execute("SELECT * FROM Account ORDER BY acc_name ASC").fetchall()
    except:
        create_table_account()
        create_table_holder()
        show_all()

    connection.commit()
    connection.close()


def show_one(word, table, field):
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    try:
        cur.execute(f"SELECT * FROM {table} WHERE {field}=?", (word,))
        results = cur.fetchall()

        if results:
            return results
        else:
            return False
    except:
        create_table_account()
        create_table_holder()

    connection.commit()
    connection.close()


# def search(word, mode):
# 	results = ""
# 	connection = sqlite3.connect("data.db")
# 	cur = connection.cursor()

# 	try:
# 			results = cur.execute("SELECT * FROM Account").fetchall()
# 	except:
# 		create_table()
# 		search(word, mode)
# 	if mode == "Name":
# 		for i in results:
# 			if word in i[0]:
# 				return True
# 			else:
# 				return False
# 	else:
# 		for i in results:
# 			if word in i[1]:
# 				return True
# 			else:
# 				return False

# 	connection.commit()
# 	connection.close()


def update_record(name, money):
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    try:
        cur.execute("UPDATE Account SET acc_money = ? WHERE acc_name = ?", (money, name))
    except:
        create_table_account()
        create_table_holder()

    connection.commit()
    connection.close()


def delete_record(name):
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()

    try:
        cur.execute("DELETE from Account WHERE acc_name=?", (name,))
    except:
        create_table_account()
        create_table_holder()

    connection.commit()
    connection.close()
