from .db import Database

class Intervention:

	def __init__(self):
		self.db=Database()


	def create_intervention(self, location, description, image, video, createdby):

		query = "INSERT INTO red_flags (location, description, image,video,createdby) VALUES ('{}','{}','{}','{}','{}') RETURNING flag_id".format(location,description,image,video,createdby)
		self.db.cursor.execute(query)
		res=self.db.cursor.fetchone()
		return res
