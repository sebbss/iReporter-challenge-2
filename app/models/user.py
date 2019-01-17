from datetime import datetime
users = []

class User:
	def __init__(self, firstname, lastname, email, phoneNumber, username, isAdmin, password):
		self._id = 2000
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.phoneNumber = phoneNumber
		self.username = username 
		self.isAdmin = isAdmin
		self.password =password



	def registerUser(self):
		self._id = self._id+1
		self.registered = str(datetime.utcnow())
		new_user = {
				'id':self._id,
				'registered':self.registered,
				'firstname':self.firstname,
				'lastname':self.lastname,
				'email':self.email,
				'phoneNumber':self.phoneNumber,
				'username':self.username,
				'isAdmin':self.isAdmin,
				'password':self.password
					}
		users.append(new_user)
		return new_user


class LoginUser:
	def __init__(self, username, password):
		self.password = password
		self.username = username
	def login(self):
		for user in users:
			if user['username'] == self.username and user['password'] == self.password:
				return user['username']





