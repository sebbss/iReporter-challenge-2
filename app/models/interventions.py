from .db import Database

class Intervention:

	def __init__(self):
		self.db=Database()


	def create_intervention(self, location, description, image, video, createdby):

		query = "INSERT INTO red_flags (location, description, image,video,createdby) VALUES ('{}','{}','{}','{}','{}') RETURNING flag_id".format(location,description,image,video,createdby)
		self.db.cursor.execute(query)
		res=self.db.cursor.fetchone()
		return res

	def update_intervention_location(self,flag_id, location):
		interv = self.get_flag_by_id(flag_id)
		if interv and interv['status']=='none':
			query = "UPDATE red_flags SET location='{}' WHERE flag_id = {} ".format(flag_id,location)
			self.db.cursor.execute(query)
			self.db.connection.commit()
		return None

	def update_intervention_description(self, flag_id, data,endpoint):
		interv = self.get_intervention_by_id(flag_id)
		if interv and interv['status']=='none':
			
			if endpoint == 'description':
				description = data['description']
				query1 = "UPDATE interventions SET description='{}' WHERE flag_id = {} ".format(description,flag_id)
				self.db.cursor.execute(query1)
				self.db.connection.commit()
				message = {
				'status': 200,
        		'data': [
            	{	'id':flag_id,
            	    'message':'udated red-flag record description'
            	}]
				}
				return message
			location = data['location']
			query2 = "UPDATE interventions SET location='{}' WHERE flag_id = {} ".format(location,flag_id)
			self.db.cursor.execute(query2)
			self.db.connection.commit()
			message = {
				'status': 200,
        		'data': [
            	{	'id':flag_id,
            	    'message':'updated intervention record location'
            	}]
				}
			return message
		return None

	def update_status(self,data,flag_id):
		flag = self.intervention_by_id(flag_id)

		status = data['status']
		if flag:
			query = "UPDATE intervention SET status = '{}' WHERE flag_id = {} RETURNING flag_id".format(status,flag_id)
			self.db.cursor.execute(query)
			res = self.db.cursor.fetchone()
			return res
		return None


	def get_all_interventions(self):
		query = "SELECT * FROM interventions"
		result = self.db.fetch_all(query)
		return result


	def get_intervention_by_id(self, _id):
		query = "SELECT * FROM interventions WHERE flag_id = '{}'".format(_id)
		return self.db.fetch_one(query)

	def delete_flag(self, flag_id):
		red_flag = self.get_intervention_by_id(flag_id)
		if red_flag:
			query = "DELETE FROM intervention WHERE flag_id = '{}' RETURNING flag_id".format(flag_id)
			self.db.cursor.execute(query)
			_id = self.db.cursor.fetchone()
			return _id
		return None