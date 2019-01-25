from flask import request, jsonify
from app.models.flags import Flag
from app.app import app
from app.utils.validators import validate_flag_data
from app.utils.helpers import token_required
from flask_jwt_extended import jwt_required
red_flag = Flag()

"""create a red flag"""


@app.route("/ireporter/api/v1/flag", methods=['POST'])
@token_required
def createFlag(current_user):
	user=current_user['user']

	createdby = user['user_id']
	flag_data = request.get_json()
	location = flag_data['location']
	description = flag_data['description']
	video = flag_data['video']
	image = flag_data['image']
	res = validate_flag_data(description,video,image,location)
	if res:
		return res
	new_flag = red_flag.create_redflag(location, description, video, image,createdby)
	return jsonify({
        'status': 201,
        'data': [
            {
                'id':new_flag[0],
                'message':'created red-flag'
            }]
    }), 201


"""get all red-flags"""


@app.route("/ireporter/api/v1/flags")
@token_required
def get_allFlags(current_user):
	response = red_flag.get_flags()
	return jsonify({'status':200 ,'flags':response}), 200


"""get a specific red-flag"""

@app.route("/ireporter/api/v1/flags/<int:flag_id>")
@token_required
def get_aRedflag(current_user,flag_id):
	flag = red_flag.get_flag_by_id(flag_id)
	if flag:
		return jsonify(flag)
	return jsonify({'message':'flag with that id doesnot exist'})

"""delete a red-flag"""


@app.route("/ireporter/api/v1/flags/<int:flag_id>", methods = ['DELETE'])
@token_required
def delete(current_user,flag_id):
	flag_delete = red_flag.delete_flag(flag_id)
	if flag_delete:
		return jsonify({
				'status': 202,
        		'data': [
            	{	'id':flag_delete[0],
            	    'message':'red-flag record has been deleted'
            	}]
			}), 202
	return jsonify({'message':'the flag your trying to delete doesnot exist'}), 400

"""update red_flag status"""

@app.route("/red_flags/<int:flag_id>/status",methods=['PATCH'])
@token_required
def update_status(current_user,flag_id):
	status = request.get_json()
	current = current_user['user']
	print (current)
	if current['isAdmin'] == 'True':
		update_data = red_flag.update_status(status,flag_id)
		if update_data:
			return jsonify( {
					'status': 200,
        			'data': [
            			{	'id':flag_id,
            			    'message':'udated red-flag record description'
            				}]
						})
		return jsonify({'message':'no flag with that id'})
	return jsonify({'message':'not authorized to view this'})





"""Update a red-flag"""

@app.route("/ireporter/api/v1/flags/<int:flag_id>/description",endpoint = 'description', methods = ['PATCH'])
@app.route("/ireporter/api/v1/flags/<int:flag_id>/location",endpoint = 'location', methods = ['PATCH'])
@token_required
def update(current_user,flag_id):
	
	data = request.get_json()
	update_data = red_flag.update_redflag_description(flag_id, data, request.endpoint)
	if update_data:	
		return jsonify(update_data)
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




