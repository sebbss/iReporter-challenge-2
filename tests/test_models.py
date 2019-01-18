from datetime import datetime
from unittest import TestCase
from app.models.flags import Flag

class TestModel(TestCase):
	def setUp(self):
		self.flag = Flag()
		self.date = str(datetime.utcnow())
		self.flag_data = {
            'createdBy': 'james',
            'location': ' bwaise',
            'description': 'corruption',
            'image': 'image',
            'video': 'video'
        }


	def test_flag_creation(self):
		resp = self.flag.create_redflag(self.flag_data)
		self.assertIn('james',str(resp))
		self.assertIn('bwaise',str(resp))
		self.assertIn('corruption',str(resp))
		self.assertIn('video',str(resp))
		self.assertIn('image',str(resp))
		self.assertEqual(resp['_id'], 1)





		
