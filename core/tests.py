from django.urls import reverse

from rest_framework.test import APITestCase
from model_bakery import baker

from core.services import JWTAuthenticationService

class HomeTest(APITestCase):
    def test_response_hello_world(self):
        user = baker.make("User", email="test@gmail.com", password="1234-abc", username="teste")

        token = JWTAuthenticationService.generate_access_token(user)['token']
        
        response = self.client.get(reverse('home'),  format='json', HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'message': 'Hello World!'})