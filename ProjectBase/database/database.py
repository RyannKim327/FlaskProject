import sqlite3, hashlib

def hash(data: str):
	return hashlib.sha384(data.encode()).hexdigest()

con = sqlite3.connect("db.sqlite")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
	'ID' INTEGER PRIMARY KEY NOT NULL, 
	'usn' TEXT, 
	'pass' TEXT
)""")

con.commit()

# User
def addUser(name: str, password: str):
	con = sqlite3.connect("db.sqlite")
	cur = con.cursor()
	password = hash(password)
	cur.execute(f"INSERT INTO users (usn, pass) VALUES (?, ?)", (name, password))
	con.commit()

def deleteUser(_id: int):
	con = sqlite3.connect("db.sqlite")
	cur = con.cursor()
	cur.execute(f"DELETE FROM users	WHERE ID = ?", (_id))
	con.commit()