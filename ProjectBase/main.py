from flask import Flask, render_template, jsonify
from database.database import *

db = Database()
app = Flask(__name__)

# Frontend connection
@app.route("/")
def index():
	return render_template("index.html")

# Api Integration
@app.route("/api/users")
def api_user():
	return jsonify({
		"users": "sample"
	})