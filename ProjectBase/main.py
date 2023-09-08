from flask import Flask, render_template
from database.database import *

db = Database()
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
	# data = db.getUsers()
	# return f"<h1>{data}</h1>"