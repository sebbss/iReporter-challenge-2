from flask import request, jsonify
from app.models.user import User
from app.app import app
user = User()


"""Register user"""

@app.route("/ireporter/api/v1/register", methods = ['POST'])
def create_user():
	userdata = request.get_json()
	new_user = user.register_user(userdata)
	return jsonify({'message':'you have been successfully registered'})