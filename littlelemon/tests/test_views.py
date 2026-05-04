from django.test import TestCase
from restaurant.models import MenuItem
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        # create user
        self.user = User.objects.create_user(username="test", password="test123")

        # login user
        self.client.login(username="test", password="test123")

        MenuItem.objects.create(title="Pizza", price=100, inventory=10)
        MenuItem.objects.create(title="Burger", price=50, inventory=20)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)