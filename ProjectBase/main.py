from flask import Flask, render_template
from database.database import *

db = Database()
app = Flask(__name__)

@app.route("/")
def index():
	db.deleteUser("1")
	return render_template("index.html")