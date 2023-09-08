from flask import Flask, render_template, jsonify
from flask_cors import CORS
from database.database import *

db = Database()
app = Flask(__name__)
app.con

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