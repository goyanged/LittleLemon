from django.test import TestCase
from restaurant.models import Menu

class MenuTestCase(TestCase):
    def test_get_item(self):
        menu = Menu(Title='spagetti', Price=7.99, Inventory=10)
        self.assertEqual(str(menu), 'spagetti : 7.99')