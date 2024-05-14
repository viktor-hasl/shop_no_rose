from django.test import TestCase
from django.urls import reverse



class IndexViewTest(TestCase):

    def test_index_view_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_cart_view_status_code(self):
        response = self.client.get(reverse('cart_detail'))
        self.assertEqual(response.status_code, 200)

    def test_order_view_status_code(self):
        response = self.client.get(reverse('order'))
        self.assertEqual(response.status_code, 200)
