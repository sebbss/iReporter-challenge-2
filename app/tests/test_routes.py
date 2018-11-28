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

	def test_apiFlagCreation(self):
		with self.test_app as cli:
			# new_flag = self.flag.create_redflag()
			response = cli.post('ireporter/api/v1/flag',content_type="application/json",data=json.dumps(self.flag_data))
			self.assertEqual(response.status_code, 200)
			self.assertIn('created red-flag', str(response.data))