import sqlite3

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
	cur.execute()
	con.commit()