import sqlite3, hashlib, json

class Database:
	def __init__(self):
		self.con = sqlite3.connect("ProjectBase/database/db.sqlite", check_same_thread=False)
		self.cur = self.con.cursor()
		self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
			'ID' INTEGER PRIMARY KEY NOT NULL, 
			'usn' TEXT, 
			'pass' TEXT
		)""")
		self.cur.execute("""CREATE TABLE IF NOT EXISTS messages (
			'ID' INTEGER PRIMARY KEY NOT NULL, 
			'_from' TEXT, 
			'_to' TEXT,
			'msg' TEXT
		)""")
		self.con.commit()

	def __hash__(self, data: str):
		return hashlib.sha384(data.encode()).hexdigest()

	# User
	def addUser(self,name: str, password: str):
		password = hash(password)
		self.cur.execute(f"INSERT INTO users (usn, pass) VALUES (?, ?)", (name, password))
		self.con.commit()

	def getUsers(self, usn: str = "", id = ""):
		if usn == "":
			res = self.cur.execute("SELECT * FROM users")
		elif id != "":
			res = self.cur.execute("SELECT * FROM users WHERE ID = ?", (id))		
		else:
			res = self.cur.execute("SELECT * FROM users WHERE usn LIKE '%?%'", (usn))		
		return res.fetchall()

	def deleteUser(self, _id: str):
		self.cur.execute(f"DELETE FROM users WHERE ID = ?", (_id))
		self.con.commit()
	
	def getCurrentUser(self, cookie):
		_id = cookie.get("user")
		res = self.cur.execute(f"SELECT * FROM users WHERE ID = ?", (_id))
		return res.fetchall()
		

	# Message
	def createMessage(self, _from: str, _to: str, msg: str):
		self.cur.execute(f"INSERT INTO messages (_from, _to, msg) VALUES (?, ?, ?)", (_from, _to, msg))
		self.con.commit()
	
	def getMessageList(self, _usr: str):
		res = self.cur.execute(f"SELECT * FROM messages WHERE _from = '?' OR _to = '?'", (_usr, _usr))
		return res.fetchall()
	
	def getMessage(self, _from: str, _to: str):
		res = self.cur.execute(f"SELECT * FROM messages WHERE (_from = ? AND _to = ?) OR (_from = ? AND _to = ?) ORDER BY ID DESC", (_from, _to, _to, _from))
		return res.fetchall()