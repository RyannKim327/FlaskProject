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
	return render_template("index.html")

# Api Integration
@app.route("/api/users")
def api_user():
	return jsonify({
		"users": "sample"
	})

@app.route("/api/check-user", methods=["POST"])
def api_checkUser():
	print(request.data)
	if request.method == "POST":
		return request.data
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
	