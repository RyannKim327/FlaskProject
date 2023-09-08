import sqlite3, hashlib

def hash(data: str):
	return hashlib.sha384(data.encode()).hexdigest()

con = sqlite3.connect("db.sqlite")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
	'ID' INTEGER AUTO INCREMENT, 
	'usn' TEXT, 
	'pass' TEXT
)""")

con.commit()

# User
def addUser(name: str, password: str):
	password = hash(password)
	cur.execute(f"INSERT INTO users (usn, pass) VALUES (?, ?)")
	con.commit()