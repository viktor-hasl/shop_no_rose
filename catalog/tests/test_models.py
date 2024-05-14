from django.test import TestCase
from catalog.models import Product


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            title_product='Роза красная',
            ruler=None,
            price=100.00,
            img='product/rose.jpg'
        )

    def test_title_product(self):
        product = Product.objects.get(id=1)
        self.assertEqual(str(product), 'Роза красная')

    def test_price(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.price, 100.00)

    def test_img_upload_path(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.img.url, '/media/product/rose.jpg')

