import sqlite3, hashlib

class Database:
	def __init__(self):
		self.con = sqlite3.connect("db.sqlite", check_same_thread=False)
		self.cur = self.con.cursor()
		self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
			'ID' INTEGER PRIMARY KEY NOT NULL, 
			'usn' TEXT, 
			'pass' TEXT
		)""")
		self.cur.execute("""CREATE TABLE IF NOT EXISTS messages (
			'ID' INTEGER PRIMARY KEY NOT NULL, 
			'from' TEXT, 
			'to' TEXT,
			'msg' TEXT
		)""")
		self.con.commit()

	def __hash__(data: str):
		return hashlib.sha384(data.encode()).hexdigest()

	# User
	def addUser(self,name: str, password: str):
		password = hash(password)
		self.cur.execute(f"INSERT INTO users (usn, pass) VALUES (?, ?)", (name, password))
		self.con.commit()

	def getUsers(self, usn: str = ""):
		if usn == "":
			res = self.cur.execute("SELECT * FROM users")
		else:
			res = self.cur.execute("SELECT * FROM users WHERE usn LIKE '%?%'", usn)		
		return res.fetchall()

	def deleteUser(self, _id: str):
		self.cur.execute(f"DELETE FROM users WHERE ID = ?", (_id))
		self.con.commit()

	# Message
	def createMessage(self, _from: str, _to: str, msg: str):
		self.cur.execute(f"INSERT INTO messages (from, to, msg) VALUES (?, ?, ?)", (_from, _to, msg))
		self.con.commit()
	
	def getMessage(self, _usr: str):
		self.cur.execute(f"")