from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from database.database import *

db = Database()
app = Flask(__name__, static_url_path="/static")
app.config.from_object(__name__)

CORS(app, resources={
	r'/*': {
		"origins": "*"
	}
})

# Frontend connection
@app.route("/")
def index():
	Database()
	return render_template("index.html")

# Api Integration
@app.route("/api/users")
def api_user():
	db = Database()
	users = db.getUsers()
	return jsonify({
		"users": users
	})

@app.route("/api/check-user", methods=["POST"])
def api_checkUser():
	if request.method == "POST":
		db = Database()
		user = request.data.user
		usn = db.getUsers(id=user)
		if usn > 0:
			data = {
				"status": True
			}
		return data
	else:
		return "hehe"

# Get Credentials
@app.route("/creds-user")
def getCookies():
	return jsonify({
		"data": request.cookies.get("user")
	})

@app.route("/creds-logged")
def logged():
	if request.cookies.get("user") != "":
		db  = Database()
		user = db.getCurrentUser(request.cookies)
		if len(user) > 0:
			return jsonify({
				"status": True,
				"data": "Logged in"
			})
		else:
			return jsonify({
				"status": False,
				"data": "Invalids"
			})
	return jsonify({-
		"status": False,
		"data": "Invalids"
	})