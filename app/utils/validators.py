from flask import jsonify

def validate_flag(**flag_data):
	#check empty feilds
	for value in flag_data.values():
		if value == "":
			return jsonify({'error message':'createdBy, location, description, status,video and image is required'})

	#check for valid feilds
	# if not isinstance(flag_data['status'], str) or not isinstance(flag_data['flag_type'], str) or not isinstance(flag_data['location'], str):
	# 	return jsonify({'error message':'status and flag_type have to be strings'})

	return None 
