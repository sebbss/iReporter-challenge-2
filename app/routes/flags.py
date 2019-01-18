from flask import request, jsonify
from app.models.flags import Flag
from app.app import app
from app.utils.validators import validate_flag
from flask_jwt_extended import jwt_required
red_flag = Flag()

"""create a red flag"""


@app.route("/ireporter/api/v1/flag", methods=['POST'])
def createFlag():
	
    flag_data = request.get_json()
    res = validate_flag(**flag_data)
    if res:
    	return res
    new_flag = red_flag.create_redflag(flag_data)
    return jsonify({
        'status': 201,
        'data': [
            {
                'id': new_flag['_id'],
                'message':'created red-flag'
            }]
    }), 201


"""get all red-flags"""

@app.route("/ireporter/api/v1/flags")
def get_allFlags():
	response = red_flag.get_flags()
	print(response)
	return jsonify({'status':200 ,'flags':response}), 200


"""get a specific red-flag"""

@jwt_required
@app.route("/ireporter/api/v1/flags/<int:flag_id>")
def get_aRedflag(flag_id):
	flag = red_flag.get_flag_by_id(flag_id)
	if flag:
		return jsonify(flag)
	return jsonify({'message':'flag with that id doesnot exist'})

"""delete a red-flag"""

@app.route("/ireporter/api/v1/flags/<int:flag_id>", methods = ['DELETE'])
def delete(flag_id):
	flag = red_flag.get_flag_by_id(flag_id)
	if flag:
		red_flag.flags = red_flag.delete_flag(flag_id)
		return jsonify({
				'status': 202,
        		'data': [
            	{	'id':flag['_id'],
            	    'message':'red-flag record has been deleted'
            	}]
			}), 202
	return jsonify({'message':'the flag your trying to delete doesnot exist'}), 400


"""Update a red-flag"""


@app.route("/ireporter/api/v1/flags/<int:flag_id>/description",endpoint = 'description', methods = ['PATCH'])
@app.route("/ireporter/api/v1/flags/<int:flag_id>/location",endpoint = 'location', methods = ['PATCH'])
def update(flag_id):
	flag_data = request.get_json()
	flag = red_flag.get_flag_by_id(flag_id)
	if flag and flag['status']=='none':
		if request.endpoint == 'description':
			flag.update(description=flag_data['description'])
			message = {
				'status': 200,
        		'data': [
            	{	'id':flag['_id'],
            	    'message':'udated red-flag record description'
            	}]
			}
		else:
			flag.update(location=flag_data['location'])
			message = {
				'status': 200,
        		'data': [
            	{	'id':flag['_id'],
            	    'message':'udated red-flag record location'
            	}]
			}
		return jsonify(message)
	return jsonify({'message':'the red-flag either doesnot exist or cannot be edited'})


"""heroku webpage"""

ireporter = '''<!DOCTYPE html>
				<html lang="en">
					<head>
						<meta charset="UTF-8">
						<title>iReporter</title>
					</head>
					<body>
						<h1>iReporter</h1>
						<p><a href="https://joseph-api.herokuapp.com/ireporter/api/v1/flags">get all red-flags</a></p>
					</body>
				</html>'''
@app.route('/')
def index():
    return ireporter




