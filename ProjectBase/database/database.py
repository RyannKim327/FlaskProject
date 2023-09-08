import sqlite3

con = sqlite3.connect("db.sqlite")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users ('ID', 'usn', 'pass')")

con.commit()