from flask import jsonify
import re


def validate_flag_data(description, location):
    if not description:
        return jsonify({'message':'description cannot be empty'})
    if not location:
        return jsonify({'message':'location cannot be empty'})
    
	

def validate_user_strings(firstname, lastname, username, phonenumber):
    if not firstname and not lastname and not username:
        return jsonify({'message':'firstname, lastname, username cannot be empty'})
    if not firstname.isalpha():
        return jsonify({'message':'firstname has to be in alphabetical letters and shouldnt contain spaces'})
    if not lastname.isalpha():
        return jsonify({'message':'lastname has to be in alphabetical letters and shouldnt contain spaces'})
    if not username.isalpha():
        return jsonify({'message':'username has to be in alphabetical letters and shouldnt contain spaces'})

    
    if len(firstname)>15 or len(lastname)>15 or len(username)>15:

        return jsonify({'message':'firstname or lastname or username shouldnt be more than 15 characters'})
    if len(phonenumber)>10 or  not phonenumber.isdigit():
        return jsonify({'message':'phone number has to be in digits and shouldnt exceed 10 digits'})
    if phonenumber.isspace():
        return jsonify({'message':'phonenumber shouldnt contain spaces'})

def invalid_password(password):
    if not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        return True

def validate_isAdmin(isAdmin):
    if not isAdmin:
        return jsonify({"message":"isAdmin shoulnot be empty"})
    if isAdmin not in ['True','False']:
        return jsonify({'message':'isAdmin should either be True or False'})

def validate_status(status):
    if status not in ['resolved','under investigation','rejected']:
        return jsonify({'message':'status should either be resolved,under investigation or rejected'})