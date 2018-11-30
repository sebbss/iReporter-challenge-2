from flask import jsonify

def validate_flag(createdBy, location, description, flag_type, status, video, image):
	#check empty feilds
	if not createdBy or not location or not description or not flag_type:
		return jsonify({'error message':'createdBy, location and description is required'})

	#check for valid feilds
	if not isinstance(status, str) or not isinstance(flag_type str):
		return jsonify({'error message':'status and flag_type have to be strings'})
		



