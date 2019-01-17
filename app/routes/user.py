from flask import request, jsonify
from app.models.user import User, users, LoginUser
from app.app import app
from flask_jwt_extended import create_access_token



"""Register user"""

@app.route("/register", methods = ['POST'])
def create_user():
	data = request.get_json()
	for u in users:
		if data['username']==u['username']:
			return jsonify({'message':'username already exists'}),400

	new_user = User(firstname=data['firstname'], lastname=data['lastname'], email=data['email'], phoneNumber=data['phoneNumber'], username=data['username'], isAdmin=data['isAdmin'], password=data['password'])
	new_user.registerUser()
	return jsonify({'message':'you have been successfully registered'})

'''login user'''
@app.route("/login", methods = ['POST'])
def login():
	data = request.get_json()
	for u in users:
		if data['username']==u['username'] and data['password']==u['password']:
			user = LoginUser(username=data['username'], password=data['password'])
			identify = user.login()
			access_token = create_access_token(identity=identify)
			return jsonify({'access-token': access_token}), 200
		return jsonify({'message':'invalid credentials'}),401