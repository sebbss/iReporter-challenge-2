from datetime import datetime
class User:
	def __init__(self):
		self._id = 2000
		self.users = []

	def register_user(self, userdata):
		self._id = self._id+1
		self.registered = str(datetime.utcnow())
		new_user = {
				'id':self._id,
				'registered':self.registered,
				'firstname':userdata['firstname'],
				'lastname':userdata['lastname'],
				'email':userdata['email'],
				'phoneNumber':userdata['phoneNumber'],
				'username':userdata['username'],
				'isAdmin':userdata['isAdmin'],
				'password':userdata['password']
		}
		self.users.append(new_user)
		return new_user



