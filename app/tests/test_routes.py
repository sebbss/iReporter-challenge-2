from unittest import TestCase
from app.models.flags import Flag
from app.app import app
import json

class TestRoutes(TestCase):
	def setUp(self):
		self.test_app = app.test_client()
		self.flag = Flag()
		self.flag_data = {
				'flag_type':'red-flag',
				'createdBy': 'james',
				'location':' bwaise',
				'description':'corruption',
				'image':'image',
				'video':'video',
				'status':'none'
		}
		self.flag_data2 = {
				'flag_type':'red-flag',
				'createdBy': 'james',
				'location':' bwaise',
				'description':'corruption',
				'image':'image',
				'video':'video',
				'status':'none'
		}
	

	def test_FlagCreation(self):
		with self.test_app as cli:
			response = cli.post('ireporter/api/v1/flag',content_type="application/json",data=json.dumps(self.flag_data))
			self.assertEqual(response.status_code, 201)
			self.assertIn('created red-flag', str(response.data))

	def test_getAllFlags(self):
		with self.test_app as cli:
			response = cli.get('ireporter/api/v1/flags')
			self.assertEqual(response.status_code, 200)

	def test_getAredFlag(self):
		with self.test_app as cli:
			post = cli.post('ireporter/api/v1/flag',content_type="application/json",data=json.dumps(self.flag_data))
			response = cli.get("/ireporter/api/v1/flags/1")
			self.assertIsNotNone(response)
			self.assertIn('red-flag',str(response.data))
			self.assertIn('james', str(response.data))


	def test_deleteRedflag(self):
		with self.test_app as cli:
			post = cli.post('ireporter/api/v1/flag',content_type="application/json",data=json.dumps(self.flag_data2))
			print(cli.get('ireporter/api/v1/flags'))
			resp = cli.delete("/ireporter/api/v1/flags/2")
			self.assertEqual(resp.status_code, 202)

