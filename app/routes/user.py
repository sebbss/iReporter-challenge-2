from flask import request, jsonify
from app.models.user import User, LoginUser
from app.app import app
from validate_email import validate_email
from app.utils.validators import validate_user_strings , invalid_password
from app.utils.helpers import encode_token
from app.models.db import Database

db = Database()

"""Register user"""


@app.route("/register", methods=['POST'])
def create_user():
    data = request.get_json()
    valid_email = validate_email(data['email'])

    if not valid_email:
        return jsonify({'message': 'email is invalid'}), 400
    if len(data['email'])>200:
        return jsonify({'message':'email is too long'})
    invalid_data = validate_user_strings(data['firstname'],data['lastname'],data['username'],data['phoneNumber'])
    if invalid_data:
        return invalid_data
    # if invalid_password(data['password']):
    #     return jsonify({'message':'password should contain a capital letter, a special character and a number'})

    new_user = User(firstname=data['firstname'], lastname=data['lastname'], 
                    phoneNumber=data['phoneNumber'], username=data['username'],email = data['email'] ,isAdmin=data['isAdmin'], password=data['password'])

    reg = new_user.registerUser()

    identity = {'username':data['username'],'user_id':reg[0],'isAdmin':data['isAdmin']}
    access_token = encode_token(identity)
    return jsonify({
        'status': 201,
        'data': [
                {
                'token': access_token.decode('utf-8'),
                'user':identity
                }]
            }), 201

'''login user'''


@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = LoginUser(username, password)
    identity = user.login()
    if identity:
        access_token = encode_token(identity)
        return jsonify({
        'status': 200,
        'data': [
                {
                'token': access_token.decode('utf-8'),
                'user':identity
                }]
            }), 200
    return jsonify({'message': 'invalid credentials'}), 401
