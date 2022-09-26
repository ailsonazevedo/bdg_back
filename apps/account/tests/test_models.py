from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

class AccountTestCase(APITestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_create_account(self):
        data = {
            "full_name": "user de teste",
            "email": "teste@gmail.com",
            "phone": "86988379740",
            "address": {
                "name": "Home",
                "street": "Rua de Tal",
                "number": "1560",
                "complement": "perto do posto",
                "district": "Centro",
                "zipcode": "64000040",
                "region": 1
            },
            "user": {
                "username": "testeuser",
                "password": "teste124"
            }
        }
        response = self.client.post('/api/v1/account/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)