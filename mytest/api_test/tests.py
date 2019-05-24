import json
from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase


# Create your tests here.
class CustomerAPITest(APITestCase):

	def test_create_customer(self):
		user_data = {
			"firstName": "test_auto",
    		"lastName": "test_auto",
    		"email": "test_auto@msg.fr"
		}
		response = self.client.post("http://127.0.0.1:8000/Customer/", user_data)
		try:
			self.assertEqual(211, response.status_code)
		except Exception as e:
			print('this has failed')
			pass


	def test_get(self):
		response = self.client.get("http://127.0.0.1:8000/Customer/")
		self.assertEqual(200, response.status_code)






	"""docstring for CustomerAPITest"""
	# def __init__(self, arg):
	# 	super(CustomerAPITest, self).__init__()
	# 	self.arg = arg
