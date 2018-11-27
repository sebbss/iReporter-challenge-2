from flask import request, jsonify
from app.models.flags import Flag
from app.app import app
red_flags = Flag()

"""create a red flag"""

@app.route("/ireporter/api/v1/flag", methods = ['POST'])
def createFlag():
	flag_data = request.get_json()
	new_flag = red_flags.create_redflag(flag_data)
	return jsonify({'message':'created flag record','flag_id':new_flag['_id']})
