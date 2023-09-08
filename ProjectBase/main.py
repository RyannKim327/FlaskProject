from flask import Flask, render_template
from database.database import *
app = Flask(__name__)

@app.route("/")
def index():
	addUser("RySes 2", "hehe")
	return render_template("index.html")