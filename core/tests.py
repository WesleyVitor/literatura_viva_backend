from rest_framework.test import APITestCase
from django.urls import reverse

class HomeTest(APITestCase):
    def test_response_hello_world(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'message': 'Hello World!'})