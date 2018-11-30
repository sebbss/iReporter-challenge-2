from flask import request, jsonify
from app.models.flags import Flag
from app.app import app
red_flag = Flag()

"""create a red flag"""


@app.route("/ireporter/api/v1/flag", methods=['POST'])
def createFlag():
    flag_data = request.get_json()
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







