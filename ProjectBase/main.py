from flask import Flask, render_template
from database.database import *
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")