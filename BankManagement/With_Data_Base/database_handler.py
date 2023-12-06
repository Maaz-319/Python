import sqlite3


def create_table():
	connection = sqlite3.connect("data.db")
	cur = connection.cursor()
	
	cur.execute("""CREATE TABLE Account(
		acc_name text,
		acc_pass text,
		acc_money integer
	)""")
	print("Done")
	
	connection.commit()
	connection.close()


def add_record(name, password, balance):
	connection = sqlite3.connect("data.db")
	cur = connection.cursor()
	
	try:
		cur.execute("INSERT INTO Account VALUES(?,?,?)", (name, password, balance))
	except:
		create_table()
		add_record(name, password, balance)
	
	connection.commit()
	connection.close()


def show_all():
	connection = sqlite3.connect("data.db")
	cur = connection.cursor()

	try:
		return cur.execute("SELECT * FROM Account ORDER BY acc_name ASC").fetchall()
	except:
		create_table()
		show_all()

	connection.commit()
	connection.close()


def show_one(word):
	connection = sqlite3.connect("data.db")
	cur = connection.cursor()

	try:
		cur.execute("SELECT * FROM Account WHERE acc_name=?", (word,))
		results = cur.fetchall()

		if results:
			return results
		else:
			return False
	except sqlite3.Error as e:
		return e
		create_table()

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
		create_table()

	connection.commit()
	connection.close()


def delete_record(name):
	connection = sqlite3.connect("data.db")
	cur = connection.cursor()

	try:
		cur.execute("DELETE from Account WHERE acc_name=?", (name,))
	except:
		create_table()

	connection.commit()
	connection.close()