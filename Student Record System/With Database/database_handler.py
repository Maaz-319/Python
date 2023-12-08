import sqlite3


def create_table():
	connection = sqlite3.connect("data.db")
	cur = connection.cursor()
	
	cur.execute("""CREATE TABLE Students(
		Student_Name text,
		Father_Name text,
		contact_no text
	)""")
	print("Done")
	
	connection.commit()
	connection.close()


def add_record(std_name, fath_name, contact_no):
	connection = sqlite3.connect("data.db")
	cur = connection.cursor()
	
	try:
		cur.execute("INSERT INTO Students VALUES(?,?,?)", (std_name, fath_name, contact_no))
	except:
		create_table()
		add_record(std_name, fath_name, contact_no)
	
	connection.commit()
	connection.close()


def show_all(direction):
	connection = sqlite3.connect("data.db")
	cur = connection.cursor()

	try:
		query = f"SELECT Student_Name FROM Students ORDER BY Student_Name {direction}"
		return cur.execute(query).fetchall()
	except sqlite3.Error as e:
		create_table()
		show_all(key, direction)

	connection.commit()
	connection.close()


def show_by_Stud_name(name):
	connection = sqlite3.connect("data.db")
	cur = connection.cursor()

	try:
		cur.execute("SELECT rowid, * FROM Students WHERE Student_Name = ?", (name,))
		results = cur.fetchall()

		if results:
			return results
		else:
			return False
	except sqlite3.Error as e:
		# create_table()
		return e

	connection.commit()
	connection.close()


def show_by_roll_no(roll_no):
	connection = sqlite3.connect("data.db")
	cur = connection.cursor()

	try:
		cur.execute("SELECT rowid, * FROM Students WHERE rowid = ?", (roll_no,))
		results = cur.fetchall()

		if results:
			return results
		else:
			return False
	except sqlite3.Error as e:
		create_table()
		return e

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


# def update_record(name, money):
# 	connection = sqlite3.connect("data.db")
# 	cur = connection.cursor()

# 	try:
# 		cur.execute("UPDATE Account SET acc_money = ? WHERE acc_name = ?", (money, name))
# 	except:
# 		create_table()

# 	connection.commit()
# 	connection.close()


# def delete_record(name):
# 	connection = sqlite3.connect("data.db")
# 	cur = connection.cursor()

# 	try:
# 		cur.execute("DELETE from Account WHERE acc_name=?", (name,))
# 	except:
# 		create_table()

# 	connection.commit()
# 	connection.close()