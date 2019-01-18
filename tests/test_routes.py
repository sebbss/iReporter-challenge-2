from unittest import TestCase
from app.app import app
import json


class TestRoutes(TestCase):
    def setUp(self):
        self.test_app = app.test_client()
        self.flag_data = {
            'createdBy': 'james',
            'location': ' bwaise',
            'description': 'corruption',
            'image': 'image',
            'video': 'video'
        }
        self.flag_data2 = {
            'createdBy': 'james',
            'location': ' bwaise',
            'description': 'corruption',
            'image': 'image',
            'video': 'video'
        }
        self.flag_data3 = {
            'description': 'misuse of funds'
        }
        self.flag_data4 = {
            'location': 'gayaza'
        }
        self.users = {
            "firstname": "joseph",
            "lastname": "senabulya",
            "email": "jsenabulya2@gmail.com",
            "phoneNumber": "0779556964",
            "username": "sebbss",
            "isAdmin": "true",
            "password": "pass"
        }
        self.users2= {
            "firstname": "joseph",
            "lastname": "senabulya",
            "email": "jsenabulya2gmail.com",
            "phoneNumber": "0779556964",
            "username": "sebbss",
            "isAdmin": "true",
            "password": "pass"
        }


    def register_user(self):
    	return self.test_app.post('/register', content_type='application/json', data=json.dumps(self.users))

    def loginUser(self):
    	return self.test_app.post('/login', content_type='application/json', data=json.dumps({"username":"sebbss","password":"pass"}))

    def test_FlagCreation(self):
    	with self.test_app as cli:
    		response = cli.post('ireporter/api/v1/flag', content_type="application/json", data=json.dumps(self.flag_data))
    		self.assertEqual(response.status_code, 201)
    		self.assertIn('created red-flag', str(response.data))

    def test_getAllFlags(self):
        with self.test_app as cli:
            response = cli.get('ireporter/api/v1/flags')
            self.assertEqual(response.status_code, 200)

    def test_getAredFlag(self):
        with self.test_app as cli:
            post = cli.post('ireporter/api/v1/flag',
                            content_type="application/json", data=json.dumps(self.flag_data))
            response = cli.get("/ireporter/api/v1/flags/1")
            self.assertIsNotNone(response)
            self.assertIn('corruption', str(response.data))
            self.assertIn('james', str(response.data))

    def test_deleteRedflag(self):
        with self.test_app as cli:
            post = cli.post('ireporter/api/v1/flag',
                            content_type="application/json", data=json.dumps(self.flag_data2))
            print(cli.get('ireporter/api/v1/flags'))
            resp = cli.delete("/ireporter/api/v1/flags/2")
            self.assertEqual(resp.status_code, 202)

    def test_update_description(self):
        with self.test_app as cli:
            updt = cli.patch("/ireporter/api/v1/flags/1/description", content_type="application/json",
                             data=json.dumps(self.flag_data3))
            response = cli.get("/ireporter/api/v1/flags/1")
            self.assertIn('misuse of funds', str(response.data))

    def test_update_location(self):
        with self.test_app as cli:
            updt = cli.patch("/ireporter/api/v1/flags/1/location", content_type="application/json",
                             data=json.dumps(self.flag_data4))
            response = cli.get("/ireporter/api/v1/flags/1")
            self.assertIn('gayaza', str(response.data))

    def test_update_withInvalid_id(self):
        with self.test_app as cli:
            updt = cli.patch("/ireporter/api/v1/flags/4/description", content_type="application/json",
                             data=json.dumps(self.flag_data3))
            print(updt.data)
            self.assertIn(
                'the red-flag either doesnot exist or cannot be edited', str(updt.data))

    def test_registerUser(self):
    	with self.test_app as cli:
    		res = cli.post('/register', content_type='application/json', data=json.dumps(self.users))
    		res2 = cli.post('/register', content_type='application/json', data=json.dumps(self.users))
    	self.assertEqual(res.status_code,201)
    	self.assertIn('username already exists',str(res2.data))


    def test_user_Invalid_email(self):
    	with self.test_app as cli:
    		res = cli.post('/register', content_type='application/json', data=json.dumps(self.users2))
    		self.assertIn('email is invalid',str(res.data))
