from flask import request, jsonify
from app.models.flags import Flag
from app.app import app
from app.utils.validators import validate_flag_data
from app.utils.helpers import token_required
from flask_jwt_extended import jwt_required
red_flag = Flag()

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
	new_flag = red_flag.create_redflag(location, description, video, image,createdby)
	return jsonify({
        'status': 201,
        'data': [
            {
                'id':new_flag[0],
                'message':'created red-flag'
            }]
    }), 201