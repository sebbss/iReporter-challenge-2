from flask import jsonify
def validate_flag(**flag_data):
	#check empty feilds
	for value in flag_data.values():
		if value == "":
			return jsonify({'error message':'createdBy, location, description,video and image is required'})



	return None 

def string_validator(string_param):
    special_characters ='$#@%&*!'
    special_character = 0
    for character in string_param:
       
        if special_characters.find(character) != -1:
            special_character +=1

    if special_character >= 1:
        return "special character exists"
    