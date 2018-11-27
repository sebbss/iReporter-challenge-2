from datetime import datetime
class Flag:
	def __init__(self):
		self.idcounter = 0
		self.flags = []
		

	def create_redflag(self, flag_data):
		self.createdOn = str(datetime.utcnow())
		self.idcounter = self.idcounter + 1
		new_flag = {
				'_id': self.idcounter,
				'createdOn': self.createdOn,
				'type':flag_data['type'],
				'createdBy':flag_data['createdBy'],
				'location':flag_data['location'],
				'description':flag_data['description'],
				'image':flag_data['image'],
				'video':flag_data['video']
		}
		self.flags.append(new_flag)
		return new_flag


    