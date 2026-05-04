from django.test import TestCase
from .models import MenuItem

class MenuItemTest(TestCase):

    def test_create_item(self):
        item = MenuItem.objects.create(
            title="IceCream",
            price=10.00,
            inventory=5
        )

        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 10.00)
        self.assertEqual(item.inventory, 5)