from datetime import datetime
from .db import Database
from flask import jsonify

class User:
	def __init__(self, firstname, lastname, phoneNumber,email, username, password):
		self.db = Database()
		
		self.firstname = firstname
		self.lastname = lastname
		self.phoneNumber = phoneNumber
		self.username = username
		self.email = email
		self.password =password



	def registerUser(self,username,email):
		resp_username = self.find_user_by_username(username)
		resp_email = self.find_user_by_email(email)
		if resp_email or resp_username:
			return None
		query = "INSERT INTO users (username, password, email,firstname, lastname, phoneNumber) VALUES ('{}', '{}', '{}', '{}','{}', '{}') RETURNING user_id".format(self.username, self.password, self.email,self.firstname, self.lastname, self.phoneNumber)
		self.db.cursor.execute(query)
		res = self.db.cursor.fetchone()
		return res
		


	def find_user_by_username(self,username):
		query = "SELECT * FROM users WHERE username = '{}'".format(username)
		return self.db.fetch_one(query)

	def find_user_by_email(self,email):
		query = "SELECT * FROM users WHERE email = '{}'".format(email)
		return self.db.fetch_one(query)




class LoginUser:
	def __init__(self, username, password):
		self.db = Database()
		self.password = password
		self.username = username
	def login(self):
		query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(self.username,self.password)
		self.db.cursor.execute(query)
		user = self.db.cursor.fetchone()
		print(user)
		if user:
			return {'usename':user[1], 'user_id':user[0],'isAdmin':user[3],'registered':user[8].__str__()}
		return None