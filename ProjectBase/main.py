from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from database.database import *

db = Database()
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={
	r'/*': {
		"origins": "*"
	}
})

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

@app.route("/api/check-user", method=["POST"])
def api_checkUser():
	if request.method == "POST":
		return request.data
	else:
		return "hehe"