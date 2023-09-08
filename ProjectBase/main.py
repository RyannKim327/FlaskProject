from flask import Flask, render_template
from database.database import *
import json

db = Database()
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/api/user")
def api_user():
	return json.dumps({
		"users": "sample"
	})