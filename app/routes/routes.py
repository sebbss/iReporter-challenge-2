from flask import request, jsonify
from app.models.models import Model
from app.app import app
from app.utils.validators import validate_flag_data
from app.utils.helpers import token_required

incident = Model()

"""create incident"""
@app.route("/ireporter/api/v2/intervention",endpoint= 'intervention', methods=['POST'])
@app.route("/ireporter/api/v1/flag",endpoint = 'red_flag', methods=['POST'])
@token_required
def create_incident(current_user):
	user=current_user['user']
	createdby = user['user_id']
	flag_data = request.get_json()
	location = flag_data['location']
	description = flag_data['description']
	video = flag_data['video']
	image = flag_data['image']
	res = validate_flag_data(description,video,image,location)
	if res:
		return res, 400
	if request.endpoint=='intervention':
		result = incident.createFlag(location,description,image,video,createdby,"interventions") 
		return jsonify(result),201
	elif request.endpoint=='red_flag':
		result = incident.createFlag(location,description,image,video,createdby,"red_flags") 
		return jsonify(result),201
	return jsonify ({'message':'url is invalid'}),400

"""get all incidents"""
@app.route("/ireporter/api/v2/interventions", endpoint= 'interv')
@app.route("/ireporter/api/v1/flags", endpoint= 'red')
@token_required
def get_all(current_user):
	if request.endpoint == 'interv':
		return jsonify(incident.get_all("interventions")), 200
	elif request.endpoint == 'red':
		return jsonify(incident.get_all("red_flags")), 200
	return jsonify ({'message':'url is invalid'}),400

"""get a specific incident"""
@app.route("/ireporter/api/v2/intervention/<int:flag_id>",endpoint = 'inter')
@app.route("/ireporter/api/v1/flags/<int:flag_id>",endpoint='red_f')
@token_required

def get_specific(current_user,flag_id):
	if request.endpoint == 'inter':
		return jsonify(incident.get_one(flag_id,"interventions"))
	elif request.endpoint == 'red_f':
		return jsonify(incident.get_one(flag_id,"red_flags"))
	return jsonify ({'message':'url is invalid'}),400

"""delete an incident"""

@app.route("/ireporter/api/v2/intervention/<int:flag_id>",endpoint='interv1', methods = ['DELETE'])
@app.route("/ireporter/api/v1/flags/<int:flag_id>",endpoint='red_flag1' ,methods = ['DELETE'])
@token_required
def delete(current_user,flag_id):
	if request.endpoint == 'interv1':
		return jsonify(incident.delete(flag_id,"interventions")),202
	elif request.endpoint == 'red_flag1':
		return jsonify(incident.delete(flag_id,"red_flags")),202
	return jsonify ({'message':'url is invalid'}),400


"""update status"""
@app.route("/interventions/<int:flag_id>/status",endpoint = 'interv2',methods=['PATCH'])
@app.route("/red_flags/<int:flag_id>/status",endpoint='red_flag2',methods=['PATCH'])
@token_required
def update_status(current_user,flag_id):
	status = request.get_json()
	if request.endpoint == 'interv2':
		return jsonify(incident.update_status('status',status['status'],"interventions",flag_id))
	elif request.endpoint == 'red_flag2':
		return jsonify(incident.update_status('status',status['status'],"red_flags",flag_id))
	return jsonify ({'message':'url is invalid'}),400

"""update data"""
@app.route("/ireporter/api/v2/intervention/<int:flag_id>/description",endpoint = 'des', methods = ['PATCH'])
@app.route("/ireporter/api/v2/intervention/<int:flag_id>/location",endpoint = 'loc', methods = ['PATCH'])
@app.route("/ireporter/api/v1/flags/<int:flag_id>/description",endpoint = 'description', methods = ['PATCH'])
@app.route("/ireporter/api/v1/flags/<int:flag_id>/location",endpoint = 'location', methods = ['PATCH'])
@token_required
def update_data(current_user,flag_id):
	data = request.get_json()
	if request.endpoint == 'des':
		return jsonify(incident.update_data('description',flag_id,data['description'],"interventions"))
	elif request.endpoint == 'loc':
		return jsonify(incident.update_data('location',flag_id,data['location'],"interventions"))
	elif request.endpoint == 'description':
		return jsonify(incident.update_data('description',flag_id,data['description'],"red_flags"))
	elif request.endpoint == 'location':
		return jsonify(incident.update_data('location',flag_id,data['location'],"red_flags"))
	return jsonify ({'message':'url is invalid'}),400