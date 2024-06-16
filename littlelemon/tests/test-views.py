from django.test import TestCase
from restaurant.models import Menu

class MenuItemsViews(TestCase):
    def setup(self):
        spagetti = Menu.objects.create(Title='spagetti', Price=7.99, Inventory=10)
        coke = Menu.objects.create(Title='coke', Price=2.99, Inventory=15)
    
    def test_getall(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'spagetti')
        self.assertContains(response, 'coke')