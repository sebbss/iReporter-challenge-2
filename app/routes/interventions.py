from flask import request, jsonify
from app.models.interventions import Intervention
from app.app import app
from app.utils.validators import validate_flag_data
from app.utils.helpers import token_required
from flask_jwt_extended import jwt_required
intervention = Intervention()

"""create an intervention"""


@app.route("/ireporter/api/v2/intervention", methods=['POST'])
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
	new_flag = intervention.create_intervention(location, description, video, image,createdby)
	return jsonify({
        'status': 201,
        'data': [
            {
                'id':new_flag[0],
                'message':'created intervention'
            }]
    }), 201


"""get all interventions"""


@app.route("/ireporter/api/v2/interventions")
@token_required
def get_interventons(current_user):
	response = intervention.get_flags()
	return jsonify({'status':200 ,'interventions':response}), 200

"""get a specific intervention"""


@app.route("/ireporter/api/v2/intervention/<int:flag_id>")
@token_required
def get_anIntervention(flag_id,current_user):
	flag = intervention.get_anIntervention(flag_id)
	if flag:
		return jsonify(flag)
	return jsonify({'message':'intervention with that id doesnot exist'})

"""delete an intervention"""


@app.route("/ireporter/api/v2/intervention/<int:flag_id>", methods = ['DELETE'])
@token_required
def delete(current_user,flag_id):
	flag_delete = intervention.delete_flag(flag_id)
	if flag_delete:
		return jsonify({
				'status': 202,
        		'data': [
            	{	'id':flag_delete[0],
            	    'message':'intervention record has been deleted'
            	}]
			}), 202
	return jsonify({'message':'the intervention your trying to delete doesnot exist'}), 400

"""update intervention status"""

@app.route("/interventions/<int:flag_id>/status",methods=['PATCH'])
@token_required
def update_status(current_user,flag_id):
	status = request.get_json()
	current = current_user['user']
	print (current)
	if current['isAdmin'] == True:
		update_data = red_flag.update_status(status,flag_id)
		if update_data:
			return jsonify( {
					'status': 200,
        			'data': [
            			{	'id':flag_id,
            			    'message':'updated intervention record description'
            				}]
						})
		return jsonify({'message':'no intervention with that id'})
	return jsonify({'message':'not authorized to view this'})

"""Update an intervention"""

@app.route("/ireporter/api/v2/intervention/<int:flag_id>/description",endpoint = 'description', methods = ['PATCH'])
@app.route("/ireporter/api/v2/intervention/<int:flag_id>/location",endpoint = 'location', methods = ['PATCH'])
@token_required
def update(current_user,flag_id):
	
	data = request.get_json()
	update_data = intervention.update_intervention(flag_id, data, request.endpoint)
	if update_data:	
		return jsonify(update_data)
	return jsonify({'message':'the red-flag either doesnot exist or cannot be edited'})