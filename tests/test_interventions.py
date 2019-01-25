from unittest import TestCase
from app.app import app
import json
from app.models.db import Database
from app.models.user import User,LoginUser
from app.utils.helpers import encode_token
db = Database()
class TestInterventionRoutes(TestCase):
    def setUp(self):
        db.create_db_tables()
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
        self.flag_data = {
            'location': ' bwaise',
            'description': 'corruption',
            'image': 'image',
            'video': 'video'
        }
        self.flag_data2 = {
            'description': 'misuse of funds'
        }
        self.flag_data3 = {
            'location': 'gayaza'
        }


    def tearDown(self):
        db.drop_tables()

    def getToken(self):
        with self.test_app as cli:
            response = cli.post('/register', content_type='application/json', data=json.dumps(self.users))
            identity = {'username':'sebbss','user_id':1,'isAdmin':'true'}
            result = encode_token(identity).decode('utf-8')
            return result


    def test_Intervention_creation_withToken(self):
        token = self.getToken()
        with self.test_app as cli:
            
            response = cli.post("/ireporter/api/v2/intervention", content_type="application/json",headers=dict(Authorization= 'Bearer '+token), data=json.dumps(self.flag_data))
            self.assertEqual(response.status_code,201)
            self.assertIn('created intervention', str(response.data))

    def test_getAllInterventions(self):
        token = self.getToken()
        with self.test_app as cli:
            response = cli.get("/ireporter/api/v2/interventions",headers=dict(Authorization= 'Bearer '+token))
            self.assertEqual(response.status_code, 200)

    def test_getAllintervention_invalidToken(self):
        with self.test_app as cli:
            response = cli.get("/ireporter/api/v2/interventions",headers=dict(Authorization= 'Bearer sdbnvv'))
            self.assertEqual(response.status_code, 403)
            self.assertIn('token is invalid', str(response.data))



    def test_getIntervention(self):
        token = self.getToken()
        with self.test_app as cli:
            post = cli.post('/ireporter/api/v2/intervention',content_type="application/json",headers=dict(Authorization= 'Bearer '+token), data=json.dumps(self.flag_data))
            response = cli.get("/ireporter/api/v2/intervention/1",headers=dict(Authorization= 'Bearer '+token))
            self.assertIsNotNone(response)
            self.assertIn('corruption', str(response.data))
            self.assertEqual(response.status_code, 200)
            response2 = cli.get("/ireporter/api/v2/intervention/1",headers=dict(Authorization= 'Bearer '))
            self.assertIn('token is missing', str(response2.data))

    def test_delete_intervention(self):
        token = self.getToken()
        with self.test_app as cli:
            post = cli.post('/ireporter/api/v2/intervention',content_type="application/json",headers=dict(Authorization= 'Bearer '+token), data=json.dumps(self.flag_data))

            resp = cli.delete("/ireporter/api/v2/intervention/1",headers=dict(Authorization= 'Bearer '+token))
            self.assertEqual(resp.status_code, 202)
            post2 = cli.post('ireporter/api/v1/flag',content_type="application/json",headers=dict(Authorization= 'Bearer '+token), data=json.dumps(self.flag_data))
            resp2 = cli.delete("/ireporter/api/v2/intervention/1",headers=dict(Authorization= 'Bearer hbskk'))
            self.assertIn('token is invalid', str(resp2.data))



    def test_update_interv_description(self):
        token = self.getToken()
        with self.test_app as cli:
            post = cli.post('/ireporter/api/v2/intervention',content_type="application/json",headers=dict(Authorization= 'Bearer '+token), data=json.dumps(self.flag_data))
            updt = cli.patch("/ireporter/api/v1/flags/1/description", content_type="application/json",headers=dict(Authorization= 'Bearer '+token),data=json.dumps(self.flag_data2))
            self.assertEqual(updt.status_code,200)
            

    def test_update_interv_location(self):
        token = self.getToken()
        with self.test_app as cli:
            post = cli.post('/ireporter/api/v2/intervention',content_type="application/json",headers=dict(Authorization= 'Bearer '+token), data=json.dumps(self.flag_data))
            updt = cli.patch("/ireporter/api/v2/intervention/1/location", content_type="application/json",headers=dict(Authorization= 'Bearer '+token),data=json.dumps(self.flag_data3))
            self.assertEqual(updt.status_code,200)
            response = cli.get("/ireporter/api/v2/intervention/1",headers=dict(Authorization= 'Bearer '+token))
            self.assertIn('gayaza', str(response.data))