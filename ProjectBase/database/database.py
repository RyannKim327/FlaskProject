import sqlite3, hashlib

class Database:
	def __init__(self):
		self.con = sqlite3.connect("db.sqlite")
		self.cur = self.con.cursor()
		self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
			'ID' INTEGER PRIMARY KEY NOT NULL, 
			'usn' TEXT, 
			'pass' TEXT
		)""")
		self.con.commit()

	def __hash__(data: str):
		return hashlib.sha384(data.encode()).hexdigest()

	# User
	def addUser(self,name: str, password: str):
		password = hash(password)
		self.cur.execute(f"INSERT INTO users (usn, pass) VALUES (?, ?)", (name, password))
		self.con.commit()

	def getUsers(self, usn: str):
		if usn == "":
			return []
		else:
			self.cur.execute("SELECT * FROM users WHERE usn LIKE '%?%'", usn)

	def deleteUser(self, _id: str):
		self.cur.execute(f"DELETE FROM users WHERE ID = {_id}")
		self.con.commit()
	