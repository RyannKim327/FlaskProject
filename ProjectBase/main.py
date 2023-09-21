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
@app.route("/api/login", method=["POST"])
def api_login():
	db = Database()
	if request.method == "POST":
		user = request.data.user
		password = request.data.password
		data = db.checkUser(user, password)
		if len(data) > 0:
			return jsonify({
				"status"
			})
	else:
		return jsonify({
			"status": 404,
			"msg": "Not found"
		})

@app.route("/api/register", method=["POST"])
def api_register():
	db = Database()
	if request.method == "POST":
		pass
	else:
		return jsonify({
			"status": 404,
			"msg": "Not found"
		})

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
				"status": True,
				"msg": "Existing"
			}
		else:
			data = {
				"status": False,
				"msg": "Not Existing"
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