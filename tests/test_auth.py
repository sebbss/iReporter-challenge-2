from unittest import TestCase
from app.app import app
import json
from app.models.db import Database
from app.models.user import User, LoginUser
from app.utils.helpers import encode_token


class TestAuth(TestCase):

    """class for testing auth endpoints"""

    def setUp(self):
        self.test_app = app.test_client()
        self.users = {
            "firstname": "joseph",
            "lastname": "senabulya",
            "email": "jsenabulya2@gmail.com",
            "phoneNumber": "0779556964",
            "username": "sebbss",
            "isAdmin": "True",
            "password": "Blue@line2"
        }
        self.users2 = {
            "firstname": "joseph",
            "lastname": "senabulya",
            "email": "jsenabulya2gmail.com",
            "phoneNumber": "0779556964",
            "username": "sebbss",
            "isAdmin": "true",
            "password": "pass"
        }
        self.users3 = {
            "firstname": "jose ph",
            "lastname": "senabulya",
            "email": "jsenabulya2@gmail.com",
            "phoneNumber": "0779556964",
            "username": "sebbss",
            "isAdmin": "true",
            "password": "pass"
        }
        self.users4 = {
            "firstname": "joseph",
            "lastname": "senabu lya",
            "email": "jsenabulya2@gmail.com",
            "phoneNumber": "0779556964",
            "username": "sebbs",
            "isAdmin": "true",
            "password": "pass"
        }
        self.users5 = {
            "firstname": "joseph",
            "lastname": "senabulya",
            "email": "jsenabulya2@gmail.com",
            "phoneNumber": "0779556964",
            "username": "se bbs",
            "isAdmin": "true",
            "password": "pass"
        }
        self.users6 = {
            "username": "sebbss",
            "password": "Blue@line2"
        }
    def test_register_login(self):
        with self.test_app as cli:
            response = cli.post('/register', content_type='application/json', data=json.dumps(self.users))
            self.assertEqual(response.status_code, 201)
            resp = cli.post('/login', content_type='application/json', data=json.dumps(self.users6))
            self.assertEqual(resp.status_code, 200)
            invalid_login = cli.post('/login', content_type='application/json', data=json.dumps({"username":"yea","password":"hsf"}))
            self.assertIn('invalid credentials',str(invalid_login.data))
            

    def test_invalid_email(self):
        with self.test_app as cli:
            response = cli.post('/register', content_type='application/json', data=json.dumps(self.users2))
            self.assertIn('email is invalid',str(response.data))

    def test_invalidData(self):
        with self.test_app as cli:
            response = cli.post('/register', content_type='application/json', data=json.dumps(self.users3))
            self.assertIn('firstname has to be in alphabetical letters and shouldnt contain spaces',str(response.data))
            response = cli.post('/register', content_type='application/json', data=json.dumps(self.users4))
            self.assertIn('lastname has to be in alphabetical letters and shouldnt contain spaces',str(response.data))
            response = cli.post('/register', content_type='application/json', data=json.dumps(self.users5))
            self.assertIn('username has to be in alphabetical letters and shouldnt contain spaces',str(response.data))
            


    



        
        
